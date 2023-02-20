m_dict = {'0': 'Arts', '1': 'Business', '2': 'Computers', '3': 'Games', '4': 'Health', '5': 'Home',
                      '6': 'Kids', '7': 'News',
                      '8': 'Recreation', '9': 'Reference', '10': 'Science', '11': 'Shopping', '12': 'Society',
                      '13': 'Sports'}
svc = '    Support Vector Classification\n\
                    \t           precision   recall  f1-score   support \n\n\
      Arts        \t\t0.52\t0.79\t0.62\t210\n\
      Business    \t\t0.32\t0.90\t0.48\t172\n\
      Computers   \t\t0.71\t0.47\t0.57\t158\n\
      Games       \t\t0.91\t0.55\t0.69\t178\n\
      Health      \t\t0.36\t0.33\t0.35\t184\n\
      Home        \t\t0.66\t0.55\t0.60\t155\n\
      Kids        \t\t0.65\t0.42\t0.51\t180\n\
      News        \t\t0.60\t0.64\t0.62\t174\n\
      Recreation  \t\t0.56\t0.26\t0.35\t160\n\
      Reference   \t\t0.78\t0.65\t0.71\t167\n\
      Science     \t\t0.86\t0.72\t0.79\t193\n\
      Shopping    \t\t0.52\t0.42\t0.47\t163\n\
      Society     \t\t0.77\t0.66\t0.71\t151\n\
      Sports      \t\t0.96\t0.96\t0.96\t134\n\n\
      accuracy    \t\t\t\t0.59       2379\n\
      macro avg   \t\t0.66\t0.59\t0.60\t2379\n\
      weighted avg\t0.65\t0.59\t0.60\t2379'

dtc = f'    Decision Tree Classifier\n\
                    \t           precision   recall  f1-score   support\n\n\
      Arts        \t\t0.52\t0.71\t0.60\t210\n\
      Business    \t\t0.25\t0.94\t0.40\t172\n\
      Computers   \t\t0.55\t0.33\t0.41\t158\n\
      Games       \t\t0.85\t0.54\t0.66\t178\n\
      Health      \t\t0.42\t0.24\t0.30\t184\n\
      Home        \t\t0.57\t0.42\t0.48\t155\n\
      Kids        \t\t0.58\t0.32\t0.41\t180\n\
      News        \t\t0.49\t0.61\t0.54\t174\n\
      Recreation  \t\t0.33\t0.21\t0.26\t160\n\
      Reference   \t\t0.70\t0.51\t0.59\t167\n\
      Science     \t\t0.79\t0.52\t0.63\t193\n\
      Shopping    \t\t0.53\t0.33\t0.41\t163\n\
      Society     \t\t0.69\t0.57\t0.62\t151\n\
      Sports      \t\t0.97\t0.95\t0.96\t134\n\n\
      accuracy    \t\t\t\t0.51      \t2379\n\
      macro avg   \t\t0.59\t0.51\t0.52\t2379\n\
      weighted avg\t\t0.58\t0.51\t0.52\t2379'

sgd = f'    SGDClassifier\n\
                    \t           precision   recall  f1-score   support\n\n\
      Arts        \t\t0.52\t0.79\t0.63\t210\n\
      Business    \t\t0.32\t0.90\t0.47\t172\n\
      Computers   \t\t0.66\t0.51\t0.57\t158\n\
      Games       \t\t0.83\t0.61\t0.70\t178\n\
      Health      \t\t0.55\t0.33\t0.41\t184\n\
      Home        \t\t0.60\t0.59\t0.59\t155\n\
      Kids        \t\t0.69\t0.45\t0.54\t180\n\
      News        \t\t0.60\t0.61\t0.60\t174\n\
      Recreation  \t\t0.54\t0.24\t0.33\t160\n\
      Reference   \t\t0.78\t0.68\t0.73\t167\n\
      Science     \t\t0.78\t0.75\t0.77\t193\n\
      Shopping    \t\t0.65\t0.38\t0.48\t163\n\
      Society     \t\t0.81\t0.70\t0.75\t151\n\
      Sports      \t\t0.93\t0.96\t0.94\t134\n\n\
      accuracy    \t\t\t\t0.61      \t2379\n\
      macro avg   \t\t0.66\t0.61\t0.61\t2379\n\
      weighted avg\t\t0.66\t0.61\t0.61\t2379'

mnb = f'    MultinomialNB\n\
                    \t           precision   recall  f1-score   support\n\n\
      Arts        \t\t0.51\t0.85\t0.64\t210\n\
      Business    \t\t0.96\t0.40\t0.57\t172\n\
      Computers   \t\t0.69\t0.47\t0.56\t158\n\
      Games       \t\t0.76\t0.61\t0.68\t178\n\
      Health      \t\t0.87\t0.22\t0.35\t184\n\
      Home        \t\t0.63\t0.54\t0.58\t155\n\
      Kids        \t\t0.67\t0.38\t0.48\t180\n\
      News        \t\t0.67\t0.38\t0.49\t174\n\
      Recreation  \t\t0.71\t0.20\t0.31\t160\n\
      Reference   \t\t0.79\t0.65\t0.71\t167\n\
      Science     \t\t0.25\t0.85\t0.39\t193\n\
      Shopping    \t\t0.63\t0.42\t0.51\t163\n\
      Society     \t\t0.82\t0.68\t0.74\t151\n\
      Sports      \t\t0.51\t0.98\t0.67\t134\n\n\
      accuracy    \t\t\t\t0.54      \t2379\n\
      macro avg   \t\t0.68\t0.54\t0.55\t2379\n\
      weighted avg\t\t0.67\t0.54\t0.54\t2379'

