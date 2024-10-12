# ApigeeApi.GoogleCloudApigeeV1Environment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiProxyType** | **String** | Optional. API Proxy type supported by the environment. The type can be set when creating the Environment and cannot be changed. | [optional] 
**createdAt** | **String** | Output only. Creation time of this environment as milliseconds since epoch. | [optional] [readonly] 
**deploymentType** | **String** | Optional. Deployment type supported by the environment. The deployment type can be set when creating the environment and cannot be changed. When you enable archive deployment, you will be **prevented from performing** a [subset of actions](/apigee/docs/api-platform/local-development/overview#prevented-actions) within the environment, including: * Managing the deployment of API proxy or shared flow revisions * Creating, updating, or deleting resource files * Creating, updating, or deleting target servers | [optional] 
**description** | **String** | Optional. Description of the environment. | [optional] 
**displayName** | **String** | Optional. Display name for this environment. | [optional] 
**forwardProxyUri** | **String** | Optional. URI of the forward proxy to be applied to the runtime instances in this environment. Must be in the format of {scheme}://{hostname}:{port}. Note that the scheme must be one of \&quot;http\&quot; or \&quot;https\&quot;, and the port must be supplied. To remove a forward proxy setting, update the field to an empty value. Note: At this time, PUT operations to add forwardProxyUri to an existing environment fail if the environment has nodeConfig set up. To successfully add the forwardProxyUri setting in this case, include the NodeConfig details with the request. | [optional] 
**hasAttachedFlowHooks** | **Boolean** |  | [optional] 
**lastModifiedAt** | **String** | Output only. Last modification time of this environment as milliseconds since epoch. | [optional] [readonly] 
**name** | **String** | Required. Name of the environment. Values must match the regular expression &#x60;^[.\\\\p{Alnum}-_]{1,255}$&#x60; | [optional] 
**nodeConfig** | [**GoogleCloudApigeeV1NodeConfig**](GoogleCloudApigeeV1NodeConfig.md) |  | [optional] 
**properties** | [**GoogleCloudApigeeV1Properties**](GoogleCloudApigeeV1Properties.md) |  | [optional] 
**state** | **String** | Output only. State of the environment. Values other than ACTIVE means the resource is not ready to use. | [optional] [readonly] 
**type** | **String** | Optional. EnvironmentType selected for the environment. | [optional] 



## Enum: ApiProxyTypeEnum


* `API_PROXY_TYPE_UNSPECIFIED` (value: `"API_PROXY_TYPE_UNSPECIFIED"`)

* `PROGRAMMABLE` (value: `"PROGRAMMABLE"`)

* `CONFIGURABLE` (value: `"CONFIGURABLE"`)





## Enum: DeploymentTypeEnum


* `DEPLOYMENT_TYPE_UNSPECIFIED` (value: `"DEPLOYMENT_TYPE_UNSPECIFIED"`)

* `PROXY` (value: `"PROXY"`)

* `ARCHIVE` (value: `"ARCHIVE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)





## Enum: TypeEnum


* `ENVIRONMENT_TYPE_UNSPECIFIED` (value: `"ENVIRONMENT_TYPE_UNSPECIFIED"`)

* `BASE` (value: `"BASE"`)

* `INTERMEDIATE` (value: `"INTERMEDIATE"`)

* `COMPREHENSIVE` (value: `"COMPREHENSIVE"`)




