

# UpdateNetworkTrafficAnalysisRequestCustomPieChartItemsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the custom pie chart item. |  |
|**type** | [**TypeEnum**](#TypeEnum) |     The signature type for the custom pie chart item. Can be one of &#39;host&#39;, &#39;port&#39; or &#39;ipRange&#39;.  |  |
|**value** | **String** |     The value of the custom pie chart item. Valid syntax depends on the signature type of the chart item     (see sample request/response for more details).  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HOST | &quot;host&quot; |
| IP_RANGE | &quot;ipRange&quot; |
| PORT | &quot;port&quot; |



