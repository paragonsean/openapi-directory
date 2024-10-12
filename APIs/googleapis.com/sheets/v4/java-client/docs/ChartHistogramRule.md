

# ChartHistogramRule

Allows you to organize numeric values in a source data column into buckets of constant size.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intervalSize** | **Double** | The size of the buckets that are created. Must be positive. |  [optional] |
|**maxValue** | **Double** | The maximum value at which items are placed into buckets. Values greater than the maximum are grouped into a single bucket. If omitted, it is determined by the maximum item value. |  [optional] |
|**minValue** | **Double** | The minimum value at which items are placed into buckets. Values that are less than the minimum are grouped into a single bucket. If omitted, it is determined by the minimum item value. |  [optional] |



