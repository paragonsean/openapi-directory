

# CustomConnector

CustomConnector represents the custom connector defined by the customer as part of byoc.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeConnectorVersions** | **List&lt;String&gt;** | Optional. Active connector versions. |  [optional] |
|**createTime** | **String** | Output only. Created time. |  [optional] [readonly] |
|**customConnectorType** | [**CustomConnectorTypeEnum**](#CustomConnectorTypeEnum) | Required. Type of the custom connector. |  [optional] |
|**description** | **String** | Optional. Description of the resource. |  [optional] |
|**displayName** | **String** | Optional. Display name. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |  [optional] |
|**logo** | **String** | Optional. Logo of the resource. |  [optional] |
|**name** | **String** | Identifier. Resource name of the CustomConnector. Format: projects/{project}/locations/{location}/customConnectors/{connector} |  [optional] |
|**updateTime** | **String** | Output only. Updated time. |  [optional] [readonly] |



## Enum: CustomConnectorTypeEnum

| Name | Value |
|---- | -----|
| CUSTOM_CONNECTOR_TYPE_UNSPECIFIED | &quot;CUSTOM_CONNECTOR_TYPE_UNSPECIFIED&quot; |
| OPEN_API | &quot;OPEN_API&quot; |
| PROTO | &quot;PROTO&quot; |



