# BigQueryApi.AggregateClassificationMetrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accuracy** | **Number** | Accuracy is the fraction of predictions given the correct label. For multiclass this is a micro-averaged metric. | [optional] 
**f1Score** | **Number** | The F1 score is an average of recall and precision. For multiclass this is a macro-averaged metric. | [optional] 
**logLoss** | **Number** | Logarithmic Loss. For multiclass this is a macro-averaged metric. | [optional] 
**precision** | **Number** | Precision is the fraction of actual positive predictions that had positive actual labels. For multiclass this is a macro-averaged metric treating each class as a binary classifier. | [optional] 
**recall** | **Number** | Recall is the fraction of actual positive labels that were given a positive prediction. For multiclass this is a macro-averaged metric. | [optional] 
**rocAuc** | **Number** | Area Under a ROC Curve. For multiclass this is a macro-averaged metric. | [optional] 
**threshold** | **Number** | Threshold at which the metrics are computed. For binary classification models this is the positive class threshold. For multi-class classfication models this is the confidence threshold. | [optional] 


