

# LatencyMetric

Defines the properties of a latency metric used in the latency scorecard

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aCLower95CI** | **BigDecimal** | The lower end of the 95% confidence interval for endpoint A |  [optional] [readonly] |
|**aHUpper95CI** | **BigDecimal** | The upper end of the 95% confidence interval for endpoint A |  [optional] [readonly] |
|**aValue** | **BigDecimal** | The metric value of the A endpoint |  [optional] [readonly] |
|**bCLower95CI** | **BigDecimal** | The lower end of the 95% confidence interval for endpoint B |  [optional] [readonly] |
|**bUpper95CI** | **BigDecimal** | The upper end of the 95% confidence interval for endpoint B |  [optional] [readonly] |
|**bValue** | **BigDecimal** | The metric value of the B endpoint |  [optional] [readonly] |
|**delta** | **BigDecimal** | The difference in value between endpoint A and B |  [optional] [readonly] |
|**deltaPercent** | **BigDecimal** | The percent difference between endpoint A and B |  [optional] [readonly] |
|**endDateTimeUTC** | **String** | The end time of the Latency Scorecard in UTC |  [optional] [readonly] |
|**name** | **String** | The name of the Latency Metric |  [optional] [readonly] |



