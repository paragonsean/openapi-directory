

# TimeSeriesData

Represents the values of a time series associated with a TimeSeriesDescriptor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**labelValues** | [**List&lt;LabelValue&gt;**](LabelValue.md) | The values of the labels in the time series identifier, given in the same order as the label_descriptors field of the TimeSeriesDescriptor associated with this object. Each value must have a value of the type given in the corresponding entry of label_descriptors. |  [optional] |
|**pointData** | [**List&lt;PointData&gt;**](PointData.md) | The points in the time series. |  [optional] |



