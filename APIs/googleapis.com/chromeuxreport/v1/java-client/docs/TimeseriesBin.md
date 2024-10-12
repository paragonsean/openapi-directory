

# TimeseriesBin

A bin is a discrete portion of data spanning from start to end, or if no end is given, then from start to +inf. A bin's start and end values are given in the value type of the metric it represents. For example, \"first contentful paint\" is measured in milliseconds and exposed as ints, therefore its metric bins will use int32s for its start and end types. However, \"cumulative layout shift\" is measured in unitless decimals and is exposed as a decimal encoded as a string, therefore its metric bins will use strings for its value type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**densities** | **List&lt;Double&gt;** | The proportion of users that experienced this bin&#39;s value for the given metric in a given collection period; the index for each of these entries corresponds to an entry in the CollectionPeriods field in the HistoryRecord message, which describes when the density was observed in the field. Thus, the length of this list of densities is equal to the length of the CollectionPeriods field in the HistoryRecord message. |  [optional] |
|**end** | **Object** | End is the end of the data bin. If end is not populated, then the bin has no end and is valid from start to +inf. |  [optional] |
|**start** | **Object** | Start is the beginning of the data bin. |  [optional] |



