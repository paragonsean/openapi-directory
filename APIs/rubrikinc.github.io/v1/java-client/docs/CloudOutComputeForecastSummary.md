

# CloudOutComputeForecastSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computeCostInUSD** | **List&lt;Long&gt;** | The cost of running a compute instance. The list contains up to forecastPeriodInGranularityUnit values, one for each granularity. For example, for a 3-year forecast period with a granularity of &#39;year&#39;, the list contains 3 values, the first value for the first year, the second value for the second year, and the third value for the third year. |  |
|**computeDurationInHrs** | **List&lt;Long&gt;** | Number of hours for which a compute instance is used. The list contains up to forecastPeriodInGranularityUnit values, one for each granularity. For example, for a 3-year forecast period with a granularity of &#39;year&#39;, the list contains 3 values, the first value for the first year, the second value for the second year, and the third value for the third year. |  |



