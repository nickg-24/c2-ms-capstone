# Mixed Traffic Inference Summary

**Generated:** 2025-05-19 22:36:07

## Notes
Used the `combined_6_rf` model to evaluate mixed traffic from various frameworks.

## merlin_mixed_1.csv

- AUC (threshold-independent): `0.9299`

### Threshold 0.3
- Accuracy: `0.9375`
```
              precision    recall  f1-score   support

           0     0.9799    0.9531    0.9663      6444
           1     0.4748    0.6842    0.5606       399

    accuracy                         0.9375      6843
   macro avg     0.7273    0.8187    0.7635      6843
weighted avg     0.9504    0.9375    0.9427      6843
```

### Threshold 0.4
- Accuracy: `0.9484`
```
              precision    recall  f1-score   support

           0     0.9761    0.9690    0.9725      6444
           1     0.5516    0.6165    0.5822       399

    accuracy                         0.9484      6843
   macro avg     0.7638    0.7928    0.7774      6843
weighted avg     0.9513    0.9484    0.9498      6843
```

### Threshold 0.5
- Accuracy: `0.9546`
```
              precision    recall  f1-score   support

           0     0.9726    0.9794    0.9760      6444
           1     0.6243    0.5539    0.5870       399

    accuracy                         0.9546      6843
   macro avg     0.7984    0.7666    0.7815      6843
weighted avg     0.9523    0.9546    0.9533      6843
```

## sliver_mixed_0.csv

- AUC (threshold-independent): `0.9555`

### Threshold 0.3
- Accuracy: `0.9424`
```
              precision    recall  f1-score   support

           0     0.9645    0.9710    0.9677     14222
           1     0.7515    0.7109    0.7306      1757

    accuracy                         0.9424     15979
   macro avg     0.8580    0.8409    0.8492     15979
weighted avg     0.9411    0.9424    0.9417     15979
```

### Threshold 0.4
- Accuracy: `0.9451`
```
              precision    recall  f1-score   support

           0     0.9552    0.9845    0.9696     14222
           1     0.8327    0.6261    0.7147      1757

    accuracy                         0.9451     15979
   macro avg     0.8939    0.8053    0.8422     15979
weighted avg     0.9417    0.9451    0.9416     15979
```

### Threshold 0.5
- Accuracy: `0.9400`
```
              precision    recall  f1-score   support

           0     0.9462    0.9888    0.9671     14222
           1     0.8577    0.5452    0.6667      1757

    accuracy                         0.9400     15979
   macro avg     0.9019    0.7670    0.8169     15979
weighted avg     0.9365    0.9400    0.9340     15979
```

## sliver_mixed_1.csv

- AUC (threshold-independent): `0.9137`

### Threshold 0.3
- Accuracy: `0.8999`
```
              precision    recall  f1-score   support

           0     0.9677    0.9218    0.9442      3709
           1     0.4212    0.6492    0.5109       325

    accuracy                         0.8999      4034
   macro avg     0.6944    0.7855    0.7276      4034
weighted avg     0.9237    0.8999    0.9093      4034
```

### Threshold 0.4
- Accuracy: `0.9142`
```
              precision    recall  f1-score   support

           0     0.9618    0.9442    0.9529      3709
           1     0.4733    0.5723    0.5181       325

    accuracy                         0.9142      4034
   macro avg     0.7176    0.7582    0.7355      4034
weighted avg     0.9225    0.9142    0.9179      4034
```

### Threshold 0.5
- Accuracy: `0.9246`
```
              precision    recall  f1-score   support

           0     0.9566    0.9617    0.9591      3709
           1     0.5344    0.5015    0.5175       325

    accuracy                         0.9246      4034
   macro avg     0.7455    0.7316    0.7383      4034
weighted avg     0.9225    0.9246    0.9235      4034
```

## covenant_mixed_0.csv

- AUC (threshold-independent): `0.9873`

### Threshold 0.3
- Accuracy: `0.9555`
```
              precision    recall  f1-score   support

           0     0.9952    0.9552    0.9748     10903
           1     0.6986    0.9577    0.8079      1181

    accuracy                         0.9555     12084
   macro avg     0.8469    0.9565    0.8913     12084
weighted avg     0.9662    0.9555    0.9585     12084
```

### Threshold 0.4
- Accuracy: `0.9633`
```
              precision    recall  f1-score   support

           0     0.9904    0.9686    0.9794     10903
           1     0.7593    0.9136    0.8294      1181

    accuracy                         0.9633     12084
   macro avg     0.8749    0.9411    0.9044     12084
weighted avg     0.9678    0.9633    0.9647     12084
```

### Threshold 0.5
- Accuracy: `0.9665`
```
              precision    recall  f1-score   support

           0     0.9874    0.9753    0.9813     10903
           1     0.7953    0.8848    0.8377      1181

    accuracy                         0.9665     12084
   macro avg     0.8913    0.9301    0.9095     12084
weighted avg     0.9686    0.9665    0.9673     12084
```

## empire_mixed_0.csv

- AUC (threshold-independent): `0.9987`

### Threshold 0.3
- Accuracy: `0.9887`
```
              precision    recall  f1-score   support

           0     0.9978    0.9898    0.9938     12718
           1     0.9042    0.9777    0.9395      1255

    accuracy                         0.9887     13973
   macro avg     0.9510    0.9837    0.9666     13973
weighted avg     0.9894    0.9887    0.9889     13973
```

### Threshold 0.4
- Accuracy: `0.9917`
```
              precision    recall  f1-score   support

           0     0.9967    0.9942    0.9954     12718
           1     0.9425    0.9665    0.9544      1255

    accuracy                         0.9917     13973
   macro avg     0.9696    0.9804    0.9749     13973
weighted avg     0.9918    0.9917    0.9917     13973
```

### Threshold 0.5
- Accuracy: `0.9922`
```
              precision    recall  f1-score   support

           0     0.9951    0.9963    0.9957     12718
           1     0.9621    0.9506    0.9563      1255

    accuracy                         0.9922     13973
   macro avg     0.9786    0.9735    0.9760     13973
weighted avg     0.9922    0.9922    0.9922     13973
```

## metasploit_mixed_1.csv

- AUC (threshold-independent): `0.9920`

### Threshold 0.3
- Accuracy: `0.9711`
```
              precision    recall  f1-score   support

           0     0.9951    0.9726    0.9838     13697
           1     0.7950    0.9572    0.8686      1519

    accuracy                         0.9711     15216
   macro avg     0.8951    0.9649    0.9262     15216
weighted avg     0.9752    0.9711    0.9723     15216
```

### Threshold 0.4
- Accuracy: `0.9749`
```
              precision    recall  f1-score   support

           0     0.9928    0.9792    0.9860     13697
           1     0.8330    0.9361    0.8816      1519

    accuracy                         0.9749     15216
   macro avg     0.9129    0.9577    0.9338     15216
weighted avg     0.9769    0.9749    0.9755     15216
```

### Threshold 0.5
- Accuracy: `0.9757`
```
              precision    recall  f1-score   support

           0     0.9909    0.9820    0.9865     13697
           1     0.8502    0.9190    0.8833      1519

    accuracy                         0.9757     15216
   macro avg     0.9206    0.9505    0.9349     15216
weighted avg     0.9769    0.9757    0.9762     15216
```

## posh_mixed_0.csv

- AUC (threshold-independent): `0.9988`

### Threshold 0.3
- Accuracy: `0.9870`
```
              precision    recall  f1-score   support

           0     0.9981    0.9873    0.9927      9550
           1     0.9052    0.9847    0.9433      1174

    accuracy                         0.9870     10724
   macro avg     0.9517    0.9860    0.9680     10724
weighted avg     0.9879    0.9870    0.9873     10724
```

### Threshold 0.4
- Accuracy: `0.9903`
```
              precision    recall  f1-score   support

           0     0.9974    0.9917    0.9945      9550
           1     0.9357    0.9787    0.9567      1174

    accuracy                         0.9903     10724
   macro avg     0.9665    0.9852    0.9756     10724
weighted avg     0.9906    0.9903    0.9904     10724
```

### Threshold 0.5
- Accuracy: `0.9916`
```
              precision    recall  f1-score   support

           0     0.9963    0.9942    0.9953      9550
           1     0.9539    0.9702    0.9620      1174

    accuracy                         0.9916     10724
   macro avg     0.9751    0.9822    0.9786     10724
weighted avg     0.9917    0.9916    0.9916     10724
```

---
## Summary Table (Best per Threshold)

Note: Conditional formatting is only visible in the Jupyter Notebook.

| Framework    |   Threshold |   F1 (C2) |   Recall (C2) |    AUC |
|:-------------|------------:|----------:|--------------:|-------:|
| covenant_0   |         0.3 |    0.8079 |        0.9577 | 0.9873 |
| covenant_0   |         0.4 |    0.8294 |        0.9136 | 0.9873 |
| covenant_0   |         0.5 |    0.8377 |        0.8848 | 0.9873 |
| empire_0     |         0.3 |    0.9395 |        0.9777 | 0.9987 |
| empire_0     |         0.4 |    0.9544 |        0.9665 | 0.9987 |
| empire_0     |         0.5 |    0.9563 |        0.9506 | 0.9987 |
| merlin_1     |         0.3 |    0.5606 |        0.6842 | 0.9299 |
| merlin_1     |         0.4 |    0.5822 |        0.6165 | 0.9299 |
| merlin_1     |         0.5 |    0.587  |        0.5539 | 0.9299 |
| metasploit_1 |         0.3 |    0.8686 |        0.9572 | 0.992  |
| metasploit_1 |         0.4 |    0.8816 |        0.9361 | 0.992  |
| metasploit_1 |         0.5 |    0.8833 |        0.919  | 0.992  |
| posh_0       |         0.3 |    0.9433 |        0.9847 | 0.9988 |
| posh_0       |         0.4 |    0.9567 |        0.9787 | 0.9988 |
| posh_0       |         0.5 |    0.962  |        0.9702 | 0.9988 |
| sliver_0     |         0.3 |    0.7306 |        0.7109 | 0.9555 |
| sliver_0     |         0.4 |    0.7147 |        0.6261 | 0.9555 |
| sliver_0     |         0.5 |    0.6667 |        0.5452 | 0.9555 |
| sliver_1     |         0.3 |    0.5109 |        0.6492 | 0.9137 |
| sliver_1     |         0.4 |    0.5181 |        0.5723 | 0.9137 |
| sliver_1     |         0.5 |    0.5175 |        0.5015 | 0.9137 |
