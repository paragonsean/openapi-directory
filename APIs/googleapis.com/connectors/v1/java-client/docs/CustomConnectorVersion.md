

# CustomConnectorVersion

CustomConnectorVersion indicates a specific version of a connector.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authConfig** | [**AuthConfig**](AuthConfig.md) |  |  [optional] |
|**backendVariableTemplates** | [**List&lt;ConfigVariableTemplate&gt;**](ConfigVariableTemplate.md) | Optional. Backend variables config templates. This translates to additional variable templates in connection. |  [optional] |
|**createTime** | **String** | Output only. Created time. |  [optional] [readonly] |
|**destinationConfigs** | [**List&lt;DestinationConfig&gt;**](DestinationConfig.md) | Optional. Destination config(s) for accessing connector facade/ proxy. This is used only when enable_backend_destination_config is true. |  [optional] |
|**enableBackendDestinationConfig** | **Boolean** | Optional. When enabled, the connector will be a facade/ proxy, and connects to the destination provided during connection creation. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |  [optional] |
|**name** | **String** | Output only. Identifier. Resource name of the Version. Format: projects/{project}/locations/{location}/customConnectors/{custom_connector}/customConnectorVersions/{custom_connector_version} |  [optional] [readonly] |
|**serviceAccount** | **String** | Optional. Service account used by runtime plane to access auth config secrets. |  [optional] |
|**specLocation** | **String** | Optional. Location of the custom connector spec. The location can be either a public url like &#x60;https://public-url.com/spec&#x60; Or a Google Cloud Storage location like &#x60;gs:///&#x60; |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the custom connector version. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Updated time. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |



