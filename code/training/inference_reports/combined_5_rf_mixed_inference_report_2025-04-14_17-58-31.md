# Mixed Traffic Inference Summary

**Generated:** 2025-04-14 17:58:31

## Notes
Used the `combined_5_rf` model to evaluate mixed traffic from various frameworks.

## metasploit_mixed_1.csv

- AUC (threshold-independent): `0.9516`

### Threshold 0.3
- Accuracy: `0.9324`
```
              precision    recall  f1-score   support

           0     0.9728    0.9514    0.9620     13697
           1     0.6346    0.7604    0.6918      1519

    accuracy                         0.9324     15216
   macro avg     0.8037    0.8559    0.8269     15216
weighted avg     0.9391    0.9324    0.9350     15216
```

### Threshold 0.4
- Accuracy: `0.9397`
```
              precision    recall  f1-score   support

           0     0.9667    0.9663    0.9665     13697
           1     0.6975    0.6998    0.6987      1519

    accuracy                         0.9397     15216
   macro avg     0.8321    0.8331    0.8326     15216
weighted avg     0.9398    0.9397    0.9398     15216
```

### Threshold 0.5
- Accuracy: `0.9407`
```
              precision    recall  f1-score   support

           0     0.9621    0.9724    0.9672     13697
           1     0.7247    0.6550    0.6881      1519

    accuracy                         0.9407     15216
   macro avg     0.8434    0.8137    0.8277     15216
weighted avg     0.9384    0.9407    0.9394     15216
```

## covenant_mixed_0.csv

- AUC (threshold-independent): `0.9307`

### Threshold 0.3
- Accuracy: `0.8992`
```
              precision    recall  f1-score   support

           0     0.9755    0.9112    0.9422     10903
           1     0.4903    0.7883    0.6045      1181

    accuracy                         0.8992     12084
   macro avg     0.7329    0.8498    0.7734     12084
weighted avg     0.9280    0.8992    0.9092     12084
```

### Threshold 0.4
- Accuracy: `0.9128`
```
              precision    recall  f1-score   support

           0     0.9669    0.9353    0.9509     10903
           1     0.5413    0.7045    0.6122      1181

    accuracy                         0.9128     12084
   macro avg     0.7541    0.8199    0.7815     12084
weighted avg     0.9253    0.9128    0.9178     12084
```

### Threshold 0.5
- Accuracy: `0.9184`
```
              precision    recall  f1-score   support

           0     0.9605    0.9485    0.9545     10903
           1     0.5740    0.6401    0.6053      1181

    accuracy                         0.9184     12084
   macro avg     0.7673    0.7943    0.7799     12084
weighted avg     0.9228    0.9184    0.9204     12084
```

## empire_mixed_0.csv

- AUC (threshold-independent): `0.9874`

### Threshold 0.3
- Accuracy: `0.9674`
```
              precision    recall  f1-score   support

           0     0.9909    0.9732    0.9820     12718
           1     0.7699    0.9092    0.8338      1255

    accuracy                         0.9674     13973
   macro avg     0.8804    0.9412    0.9079     13973
weighted avg     0.9710    0.9674    0.9686     13973
```

### Threshold 0.4
- Accuracy: `0.9685`
```
              precision    recall  f1-score   support

           0     0.9858    0.9796    0.9826     12718
           1     0.8052    0.8566    0.8301      1255

    accuracy                         0.9685     13973
   macro avg     0.8955    0.9181    0.9064     13973
weighted avg     0.9695    0.9685    0.9689     13973
```

### Threshold 0.5
- Accuracy: `0.9674`
```
              precision    recall  f1-score   support

           0     0.9797    0.9845    0.9821     12718
           1     0.8349    0.7936    0.8137      1255

    accuracy                         0.9674     13973
   macro avg     0.9073    0.8891    0.8979     13973
weighted avg     0.9667    0.9674    0.9670     13973
```

## merlin_mixed_0.csv

- AUC (threshold-independent): `0.9710`

### Threshold 0.3
- Accuracy: `0.9736`
```
              precision    recall  f1-score   support

           0     0.9957    0.9774    0.9864     51746
           1     0.4014    0.7829    0.5307      1004

    accuracy                         0.9736     52750
   macro avg     0.6986    0.8801    0.7586     52750
weighted avg     0.9844    0.9736    0.9778     52750
```

### Threshold 0.4
- Accuracy: `0.9807`
```
              precision    recall  f1-score   support

           0     0.9944    0.9858    0.9901     51746
           1     0.4952    0.7161    0.5855      1004

    accuracy                         0.9807     52750
   macro avg     0.7448    0.8510    0.7878     52750
weighted avg     0.9849    0.9807    0.9824     52750
```

### Threshold 0.5
- Accuracy: `0.9834`
```
              precision    recall  f1-score   support

           0     0.9931    0.9899    0.9915     51746
           1     0.5551    0.6474    0.5977      1004

    accuracy                         0.9834     52750
   macro avg     0.7741    0.8187    0.7946     52750
weighted avg     0.9848    0.9834    0.9840     52750
```

## posh_mixed_0.csv

- AUC (threshold-independent): `0.9914`

### Threshold 0.3
- Accuracy: `0.9722`
```
              precision    recall  f1-score   support

           0     0.9923    0.9763    0.9843      9550
           1     0.8298    0.9387    0.8809      1174

    accuracy                         0.9722     10724
   macro avg     0.9111    0.9575    0.9326     10724
weighted avg     0.9745    0.9722    0.9730     10724
```

### Threshold 0.4
- Accuracy: `0.9745`
```
              precision    recall  f1-score   support

           0     0.9868    0.9846    0.9857      9550
           1     0.8770    0.8927    0.8848      1174

    accuracy                         0.9745     10724
   macro avg     0.9319    0.9386    0.9352     10724
weighted avg     0.9748    0.9745    0.9746     10724
```

### Threshold 0.5
- Accuracy: `0.9712`
```
              precision    recall  f1-score   support

           0     0.9784    0.9895    0.9839      9550
           1     0.9061    0.8220    0.8620      1174

    accuracy                         0.9712     10724
   macro avg     0.9422    0.9058    0.9230     10724
weighted avg     0.9705    0.9712    0.9706     10724
```

## sliver_mixed_0.csv

- AUC (threshold-independent): `0.9543`

### Threshold 0.3
- Accuracy: `0.9402`
```
              precision    recall  f1-score   support

           0     0.9620    0.9711    0.9665     14222
           1     0.7468    0.6898    0.7172      1757

    accuracy                         0.9402     15979
   macro avg     0.8544    0.8305    0.8419     15979
weighted avg     0.9384    0.9402    0.9391     15979
```

### Threshold 0.4
- Accuracy: `0.9435`
```
              precision    recall  f1-score   support

           0     0.9549    0.9830    0.9687     14222
           1     0.8191    0.6238    0.7082      1757

    accuracy                         0.9435     15979
   macro avg     0.8870    0.8034    0.8385     15979
weighted avg     0.9399    0.9435    0.9401     15979
```

### Threshold 0.5
- Accuracy: `0.9417`
```
              precision    recall  f1-score   support

           0     0.9481    0.9887    0.9680     14222
           1     0.8598    0.5618    0.6795      1757

    accuracy                         0.9417     15979
   macro avg     0.9039    0.7752    0.8237     15979
weighted avg     0.9384    0.9417    0.9362     15979
```

## sliver_mixed_1.csv

- AUC (threshold-independent): `0.9060`

### Threshold 0.3
- Accuracy: `0.8974`
```
              precision    recall  f1-score   support

           0     0.9658    0.9210    0.9429      3709
           1     0.4105    0.6277    0.4964       325

    accuracy                         0.8974      4034
   macro avg     0.6881    0.7743    0.7196      4034
weighted avg     0.9211    0.8974    0.9069      4034
```

### Threshold 0.4
- Accuracy: `0.9073`
```
              precision    recall  f1-score   support

           0     0.9587    0.9396    0.9491      3709
           1     0.4386    0.5385    0.4834       325

    accuracy                         0.9073      4034
   macro avg     0.6987    0.7390    0.7162      4034
weighted avg     0.9168    0.9073    0.9116      4034
```

### Threshold 0.5
- Accuracy: `0.9150`
```
              precision    recall  f1-score   support

           0     0.9532    0.9544    0.9538      3709
           1     0.4719    0.4646    0.4682       325

    accuracy                         0.9150      4034
   macro avg     0.7125    0.7095    0.7110      4034
weighted avg     0.9144    0.9150    0.9147      4034
```

---
## Summary Table (Best per Threshold)

Note: Conditional formatting is only visible in the Jupyter Notebook.

| Framework    |   Threshold |   F1 (C2) |   Recall (C2) |    AUC |
|:-------------|------------:|----------:|--------------:|-------:|
| covenant_0   |         0.3 |    0.6045 |        0.7883 | 0.9307 |
| covenant_0   |         0.4 |    0.6122 |        0.7045 | 0.9307 |
| covenant_0   |         0.5 |    0.6053 |        0.6401 | 0.9307 |
| empire_0     |         0.3 |    0.8338 |        0.9092 | 0.9874 |
| empire_0     |         0.4 |    0.8301 |        0.8566 | 0.9874 |
| empire_0     |         0.5 |    0.8137 |        0.7936 | 0.9874 |
| merlin_0     |         0.3 |    0.5307 |        0.7829 | 0.971  |
| merlin_0     |         0.4 |    0.5855 |        0.7161 | 0.971  |
| merlin_0     |         0.5 |    0.5977 |        0.6474 | 0.971  |
| metasploit_1 |         0.3 |    0.6918 |        0.7604 | 0.9516 |
| metasploit_1 |         0.4 |    0.6987 |        0.6998 | 0.9516 |
| metasploit_1 |         0.5 |    0.6881 |        0.655  | 0.9516 |
| posh_0       |         0.3 |    0.8809 |        0.9387 | 0.9914 |
| posh_0       |         0.4 |    0.8848 |        0.8927 | 0.9914 |
| posh_0       |         0.5 |    0.862  |        0.822  | 0.9914 |
| sliver_0     |         0.3 |    0.7172 |        0.6898 | 0.9543 |
| sliver_0     |         0.4 |    0.7082 |        0.6238 | 0.9543 |
| sliver_0     |         0.5 |    0.6795 |        0.5618 | 0.9543 |
| sliver_1     |         0.3 |    0.4964 |        0.6277 | 0.906  |
| sliver_1     |         0.4 |    0.4834 |        0.5385 | 0.906  |
| sliver_1     |         0.5 |    0.4682 |        0.4646 | 0.906  |
