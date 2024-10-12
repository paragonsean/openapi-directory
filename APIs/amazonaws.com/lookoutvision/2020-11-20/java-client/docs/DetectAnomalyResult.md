

# DetectAnomalyResult

The prediction results from a call to <a>DetectAnomalies</a>. <code>DetectAnomalyResult</code> includes classification information for the prediction (<code>IsAnomalous</code> and <code>Confidence</code>). If the model you use is an image segementation model, <code>DetectAnomalyResult</code> also includes segmentation information (<code>Anomalies</code> and <code>AnomalyMask</code>). Classification information is calculated separately from segmentation information and you shouldn't assume a relationship between them.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**source** | [**DetectAnomalyResultSource**](DetectAnomalyResultSource.md) |  |  [optional] |
|**isAnomalous** | [**Boolean**](Boolean.md) |  |  [optional] |
|**confidence** | [**Float**](Float.md) |  |  [optional] |
|**anomalies** | [**List**](List.md) |  |  [optional] |
|**anomalyMask** | [**String**](String.md) |  |  [optional] |



