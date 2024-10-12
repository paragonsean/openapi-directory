

# UpdateNetworkTrafficAnalysisRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customPieChartItems** | [**List&lt;UpdateNetworkTrafficAnalysisRequestCustomPieChartItemsInner&gt;**](UpdateNetworkTrafficAnalysisRequestCustomPieChartItemsInner.md) | The list of items that make up the custom pie chart for traffic reporting. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) |     The traffic analysis mode for the network. Can be one of &#39;disabled&#39; (do not collect traffic types),     &#39;basic&#39; (collect generic traffic categories), or &#39;detailed&#39; (collect destination hostnames).  |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;basic&quot; |
| DETAILED | &quot;detailed&quot; |
| DISABLED | &quot;disabled&quot; |



