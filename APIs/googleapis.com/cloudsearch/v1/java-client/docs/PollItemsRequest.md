

# PollItemsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectorName** | **String** | The name of connector making this call. Format: datasources/{source_id}/connectors/{ID} |  [optional] |
|**debugOptions** | [**DebugOptions**](DebugOptions.md) |  |  [optional] |
|**limit** | **Integer** | Maximum number of items to return. The maximum value is 100 and the default value is 20. |  [optional] |
|**queue** | **String** | Queue name to fetch items from. If unspecified, PollItems will fetch from &#39;default&#39; queue. The maximum length is 100 characters. |  [optional] |
|**statusCodes** | [**List&lt;StatusCodesEnum&gt;**](#List&lt;StatusCodesEnum&gt;) | Limit the items polled to the ones with these statuses. |  [optional] |



## Enum: List&lt;StatusCodesEnum&gt;

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| ERROR | &quot;ERROR&quot; |
| MODIFIED | &quot;MODIFIED&quot; |
| NEW_ITEM | &quot;NEW_ITEM&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |



