

# ApigatewayApi

An API that can be served by one or more Gateways.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Created time. |  [optional] [readonly] |
|**displayName** | **String** | Optional. Display name. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |  [optional] |
|**managedService** | **String** | Optional. Immutable. The name of a Google Managed Service ( https://cloud.google.com/service-infrastructure/docs/glossary#managed). If not specified, a new Service will automatically be created in the same project as this API. |  [optional] |
|**name** | **String** | Output only. Resource name of the API. Format: projects/{project}/locations/global/apis/{api} |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the API. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Updated time. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |



