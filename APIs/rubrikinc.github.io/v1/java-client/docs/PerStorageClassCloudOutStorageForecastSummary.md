

# PerStorageClassCloudOutStorageForecastSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storageClass** | **String** | Storage class of the cloud archival location. |  |
|**storageCostInUSD** | **List&lt;Long&gt;** | Storage costs, in USD, for a particular storage class in the cloud archival location. The list contains forecastPeriodInGranularityUnit values, one for each granularity period. For example, for a 3-year forecast period with a granularity of &#39;year&#39;, the list contains 3 values. The first value corresponds to the first year, the second value corresponds to the second year, and the third value corresponds to the third year. |  |
|**storageUsedInGB** | **List&lt;Long&gt;** | Storage values, in GBs, used on a particular storage class in the cloud archival location. The number of values in the list is specified by the value of the forecastPeriodInGranularityUnit parameter. Each value in the list is for the last day of the granularity period. For example, for a 3-year forecast period with a granularity of &#39;year&#39;, the list contains 3 values. First value corresponds to the last day of the first year. Second value corresponds to the last day of the second year. Third value corresponds to the last day of the third year. |  |



