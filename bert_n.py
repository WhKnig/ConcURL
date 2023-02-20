import pandas as pd
import torch
import numpy as np
from transformers import BertTokenizer
from torch import nn
from transformers import BertModel
from torch.optim import Adam
from tqdm import tqdm
import pickle

tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
labels = {'Arts':0,
          'Society':1,
          'Computers':2,
          'Science':3,
          'Sports':4,
          'Recreation':5,
          'Reference':6,
          'Games':7,
          'Kids':8,
          'Business': 9,
          'Shopping': 10,
          'Health': 11,
          }

class Dataset(torch.utils.data.Dataset):

    def __init__(self, df):

        self.labels = [labels[label] for label in df['label']]
        #self.texts = [tokenizer(text, padding='max_length', max_length = 512, truncation=True, return_tensors="pt") for text in df['lemm']]

    def classes(self):
        return self.labels

    def __len__(self):
        return len(self.labels)

    def get_batch_labels(self, idx):
        # Fetch a batch of labels
        return np.array(self.labels[idx])

    # def get_batch_texts(self, idx):
    #     # Fetch a batch of inputs
    #     return self.texts[idx]

    def __getitem__(self, idx):

        #batch_texts = self.get_batch_texts(idx)
        batch_y = self.get_batch_labels(idx)

        #return batch_texts, batch_y
        return batch_y


class BertClassifier(nn.Module):

    def __init__(self, dropout=0.5):

        super(BertClassifier, self).__init__()

        self.bert = BertModel.from_pretrained('bert-base-cased')
        self.dropout = nn.Dropout(dropout)
        self.linear = nn.Linear(768, 13)
        self.relu = nn.ReLU()

    def forward(self, input_id, mask):

        _, pooled_output = self.bert(input_ids= input_id, attention_mask=mask,return_dict=False)
        dropout_output = self.dropout(pooled_output)
        linear_output = self.linear(dropout_output)
        final_layer = self.relu(linear_output)

        return final_layer

def train(model, train_data, val_data, learning_rate, epochs):
    train, val = Dataset(train_data), Dataset(val_data)

    train_dataloader = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
    val_dataloader = torch.utils.data.DataLoader(val, batch_size=10)
    use_cuda = torch.cuda.is_available()
    if use_cuda:
        print("Using GPU: {}\n".format(torch.cuda.get_device_name()))
        device = torch.device('cuda')
    else:
        print("\nGPU not found. Using CPU: {}\n".format(platform.processor()))
        device = torch.device('cpu')
    criterion = nn.CrossEntropyLoss()
    optimizer = Adam(model.parameters(), lr=learning_rate)

    if use_cuda:
        model = model.cuda()
        criterion = criterion.cuda()

    for epoch_num in range(epochs):

        total_acc_train = 0
        total_loss_train = 0

        for train_input, train_label in tqdm(train_dataloader):
            train_label = train_label.to(device)
            mask = train_input['attention_mask'].to(device)
            input_id = train_input['input_ids'].squeeze(1).to(device)
            output = model(input_id, mask)

            batch_loss = criterion(output, train_label.long())
            total_loss_train += batch_loss.item()

            acc = (output.argmax(dim=1) == train_label).sum().item()
            total_acc_train += acc

            model.zero_grad()
            batch_loss.backward()
            optimizer.step()

        total_acc_val = 0
        total_loss_val = 0

        with torch.no_grad():

            for val_input, val_label in val_dataloader:
                val_label = val_label.to(device)
                mask = val_input['attention_mask'].to(device)
                input_id = val_input['input_ids'].squeeze(1).to(device)

                output = model(input_id, mask)

                batch_loss = criterion(output, val_label.long())
                total_loss_val += batch_loss.item()

                acc = (output.argmax(dim=1) == val_label).sum().item()
                total_acc_val += acc

        if epoch_num > 14:
            torch.save(model.state_dict(), f'/content/{epoch_num}.pt')

        print(
            f'Epochs: {epoch_num + 1} | Train Loss: {total_loss_train / len(train_data): .3f} \
                | Train Accuracy: {total_acc_train / len(train_data): .3f} \
                | Val Loss: {total_loss_val / len(val_data): .3f} \
                | Val Accuracy: {total_acc_val / len(val_data): .3f}')



def main(df):
    #df = pd.DataFrame(columns = ['link', 'label'])
    test = Dataset(df)
    test_dataloader = torch.utils.data.DataLoader(test, batch_size=0)
    model = torch.load(open('bert.sav', 'rb'))
    with torch.no_grad():

        for test_input, test_label in test_dataloader:
              mask = test_input['attention_mask']
              input_id = test_input['input_ids'].squeeze(1)

              output = model(input_id, mask)
    print(output)
    df.loc[len(df.index)-1, 'label'] = output
    return df
