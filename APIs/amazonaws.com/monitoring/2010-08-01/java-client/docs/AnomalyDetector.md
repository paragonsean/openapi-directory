

# AnomalyDetector

An anomaly detection model associated with a particular CloudWatch metric, statistic, or metric math expression. You can use the model to display a band of expected, normal values when the metric is graphed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namespace** | [**String**](String.md) |  |  [optional] |
|**metricName** | [**String**](String.md) |  |  [optional] |
|**dimensions** | [**List**](List.md) |  |  [optional] |
|**stat** | [**String**](String.md) |  |  [optional] |
|**_configuration** | [**AnomalyDetectorConfiguration**](AnomalyDetectorConfiguration.md) |  |  [optional] |
|**stateValue** | [**AnomalyDetectorStateValue**](AnomalyDetectorStateValue.md) |  |  [optional] |
|**singleMetricAnomalyDetector** | [**AnomalyDetectorSingleMetricAnomalyDetector**](AnomalyDetectorSingleMetricAnomalyDetector.md) |  |  [optional] |
|**metricMathAnomalyDetector** | [**AnomalyDetectorMetricMathAnomalyDetector**](AnomalyDetectorMetricMathAnomalyDetector.md) |  |  [optional] |



