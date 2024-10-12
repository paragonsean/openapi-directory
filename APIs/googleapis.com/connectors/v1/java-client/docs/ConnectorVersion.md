

# ConnectorVersion

ConnectorVersion indicates a specific version of a connector.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authConfigTemplates** | [**List&lt;AuthConfigTemplate&gt;**](AuthConfigTemplate.md) | Output only. List of auth configs supported by the Connector Version. |  [optional] [readonly] |
|**configVariableTemplates** | [**List&lt;ConfigVariableTemplate&gt;**](ConfigVariableTemplate.md) | Output only. List of config variables needed to create a connection. |  [optional] [readonly] |
|**connectorInfraConfig** | [**ConnectorInfraConfig**](ConnectorInfraConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. Created time. |  [optional] [readonly] |
|**destinationConfigTemplates** | [**List&lt;DestinationConfigTemplate&gt;**](DestinationConfigTemplate.md) | Output only. List of destination configs needed to create a connection. |  [optional] [readonly] |
|**displayName** | **String** | Output only. Display name. |  [optional] [readonly] |
|**egressControlConfig** | [**EgressControlConfig**](EgressControlConfig.md) |  |  [optional] |
|**eventingConfigTemplate** | [**EventingConfigTemplate**](EventingConfigTemplate.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Output only. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |  [optional] [readonly] |
|**launchStage** | [**LaunchStageEnum**](#LaunchStageEnum) | Output only. Flag to mark the version indicating the launch stage. |  [optional] [readonly] |
|**name** | **String** | Output only. Resource name of the Version. Format: projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}/versions/{version} Only global location is supported for Connector resource. |  [optional] [readonly] |
|**releaseVersion** | **String** | Output only. ReleaseVersion of the connector, for example: \&quot;1.0.1-alpha\&quot;. |  [optional] [readonly] |
|**roleGrant** | [**RoleGrant**](RoleGrant.md) |  |  [optional] |
|**roleGrants** | [**List&lt;RoleGrant&gt;**](RoleGrant.md) | Output only. Role grant configurations for this connector version. |  [optional] [readonly] |
|**sslConfigTemplate** | [**SslConfigTemplate**](SslConfigTemplate.md) |  |  [optional] |
|**supportedRuntimeFeatures** | [**SupportedRuntimeFeatures**](SupportedRuntimeFeatures.md) |  |  [optional] |
|**unsupportedConnectionTypes** | [**List&lt;UnsupportedConnectionTypesEnum&gt;**](#List&lt;UnsupportedConnectionTypesEnum&gt;) | Output only. Unsupported connection types. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Updated time. |  [optional] [readonly] |



## Enum: LaunchStageEnum

| Name | Value |
|---- | -----|
| LAUNCH_STAGE_UNSPECIFIED | &quot;LAUNCH_STAGE_UNSPECIFIED&quot; |
| PREVIEW | &quot;PREVIEW&quot; |
| GA | &quot;GA&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |
| PRIVATE_PREVIEW | &quot;PRIVATE_PREVIEW&quot; |



## Enum: List&lt;UnsupportedConnectionTypesEnum&gt;

| Name | Value |
|---- | -----|
| CONNECTION_TYPE_UNSPECIFIED | &quot;CONNECTION_TYPE_UNSPECIFIED&quot; |
| CONNECTION_WITH_EVENTING | &quot;CONNECTION_WITH_EVENTING&quot; |
| ONLY_CONNECTION | &quot;ONLY_CONNECTION&quot; |
| ONLY_EVENTING | &quot;ONLY_EVENTING&quot; |



