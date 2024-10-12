# CloudSearchApi.PollItemsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectorName** | **String** | The name of connector making this call. Format: datasources/{source_id}/connectors/{ID} | [optional] 
**debugOptions** | [**DebugOptions**](DebugOptions.md) |  | [optional] 
**limit** | **Number** | Maximum number of items to return. The maximum value is 100 and the default value is 20. | [optional] 
**queue** | **String** | Queue name to fetch items from. If unspecified, PollItems will fetch from &#39;default&#39; queue. The maximum length is 100 characters. | [optional] 
**statusCodes** | **[String]** | Limit the items polled to the ones with these statuses. | [optional] 



## Enum: [StatusCodesEnum]


* `CODE_UNSPECIFIED` (value: `"CODE_UNSPECIFIED"`)

* `ERROR` (value: `"ERROR"`)

* `MODIFIED` (value: `"MODIFIED"`)

* `NEW_ITEM` (value: `"NEW_ITEM"`)

* `ACCEPTED` (value: `"ACCEPTED"`)




