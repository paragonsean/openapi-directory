# ConnectorsApi.ConnectorVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authConfigTemplates** | [**[AuthConfigTemplate]**](AuthConfigTemplate.md) | Output only. List of auth configs supported by the Connector Version. | [optional] [readonly] 
**configVariableTemplates** | [**[ConfigVariableTemplate]**](ConfigVariableTemplate.md) | Output only. List of config variables needed to create a connection. | [optional] [readonly] 
**connectorInfraConfig** | [**ConnectorInfraConfig**](ConnectorInfraConfig.md) |  | [optional] 
**createTime** | **String** | Output only. Created time. | [optional] [readonly] 
**destinationConfigTemplates** | [**[DestinationConfigTemplate]**](DestinationConfigTemplate.md) | Output only. List of destination configs needed to create a connection. | [optional] [readonly] 
**displayName** | **String** | Output only. Display name. | [optional] [readonly] 
**egressControlConfig** | [**EgressControlConfig**](EgressControlConfig.md) |  | [optional] 
**eventingConfigTemplate** | [**EventingConfigTemplate**](EventingConfigTemplate.md) |  | [optional] 
**labels** | **{String: String}** | Output only. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources | [optional] [readonly] 
**launchStage** | **String** | Output only. Flag to mark the version indicating the launch stage. | [optional] [readonly] 
**name** | **String** | Output only. Resource name of the Version. Format: projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}/versions/{version} Only global location is supported for Connector resource. | [optional] [readonly] 
**releaseVersion** | **String** | Output only. ReleaseVersion of the connector, for example: \&quot;1.0.1-alpha\&quot;. | [optional] [readonly] 
**roleGrant** | [**RoleGrant**](RoleGrant.md) |  | [optional] 
**roleGrants** | [**[RoleGrant]**](RoleGrant.md) | Output only. Role grant configurations for this connector version. | [optional] [readonly] 
**sslConfigTemplate** | [**SslConfigTemplate**](SslConfigTemplate.md) |  | [optional] 
**supportedRuntimeFeatures** | [**SupportedRuntimeFeatures**](SupportedRuntimeFeatures.md) |  | [optional] 
**unsupportedConnectionTypes** | **[String]** | Output only. Unsupported connection types. | [optional] [readonly] 
**updateTime** | **String** | Output only. Updated time. | [optional] [readonly] 



## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `PREVIEW` (value: `"PREVIEW"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)

* `PRIVATE_PREVIEW` (value: `"PRIVATE_PREVIEW"`)





## Enum: [UnsupportedConnectionTypesEnum]


* `CONNECTION_TYPE_UNSPECIFIED` (value: `"CONNECTION_TYPE_UNSPECIFIED"`)

* `CONNECTION_WITH_EVENTING` (value: `"CONNECTION_WITH_EVENTING"`)

* `ONLY_CONNECTION` (value: `"ONLY_CONNECTION"`)

* `ONLY_EVENTING` (value: `"ONLY_EVENTING"`)




