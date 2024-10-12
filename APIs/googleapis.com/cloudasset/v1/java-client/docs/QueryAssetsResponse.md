

# QueryAssetsResponse

QueryAssets response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**done** | **Boolean** | The query response, which can be either an &#x60;error&#x60; or a valid &#x60;response&#x60;. If &#x60;done&#x60; &#x3D;&#x3D; &#x60;false&#x60; and the query result is being saved in a output, the output_config field will be set. If &#x60;done&#x60; &#x3D;&#x3D; &#x60;true&#x60;, exactly one of &#x60;error&#x60;, &#x60;query_result&#x60; or &#x60;output_config&#x60; will be set. |  [optional] |
|**error** | [**Status**](Status.md) |  |  [optional] |
|**jobReference** | **String** | Reference to a query job. |  [optional] |
|**outputConfig** | [**QueryAssetsOutputConfig**](QueryAssetsOutputConfig.md) |  |  [optional] |
|**queryResult** | [**QueryResult**](QueryResult.md) |  |  [optional] |



