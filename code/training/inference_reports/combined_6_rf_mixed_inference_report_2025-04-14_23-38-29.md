# Mixed Traffic Inference Summary

**Generated:** 2025-04-14 23:38:29

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

---
## Summary Table (Best per Threshold)

Note: Conditional formatting is only visible in the Jupyter Notebook.

| Framework   |   Threshold |   F1 (C2) |   Recall (C2) |    AUC |
|:------------|------------:|----------:|--------------:|-------:|
| merlin_1    |         0.3 |    0.5606 |        0.6842 | 0.9299 |
| merlin_1    |         0.4 |    0.5822 |        0.6165 | 0.9299 |
| merlin_1    |         0.5 |    0.587  |        0.5539 | 0.9299 |
| sliver_0    |         0.3 |    0.7306 |        0.7109 | 0.9555 |
| sliver_0    |         0.4 |    0.7147 |        0.6261 | 0.9555 |
| sliver_0    |         0.5 |    0.6667 |        0.5452 | 0.9555 |
| sliver_1    |         0.3 |    0.5109 |        0.6492 | 0.9137 |
| sliver_1    |         0.4 |    0.5181 |        0.5723 | 0.9137 |
| sliver_1    |         0.5 |    0.5175 |        0.5015 | 0.9137 |
