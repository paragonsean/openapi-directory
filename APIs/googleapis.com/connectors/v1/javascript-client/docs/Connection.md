# ConnectorsApi.Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authConfig** | [**AuthConfig**](AuthConfig.md) |  | [optional] 
**configVariables** | [**[ConfigVariable]**](ConfigVariable.md) | Optional. Configuration for configuring the connection with an external system. | [optional] 
**connectionRevision** | **String** | Output only. Connection revision. This field is only updated when the connection is created or updated by User. | [optional] [readonly] 
**connectorVersion** | **String** | Required. Connector version on which the connection is created. The format is: projects/_*_/locations/_*_/providers/_*_/connectors/_*_/versions/_* Only global location is supported for ConnectorVersion resource. | [optional] 
**connectorVersionInfraConfig** | [**ConnectorVersionInfraConfig**](ConnectorVersionInfraConfig.md) |  | [optional] 
**connectorVersionLaunchStage** | **String** | Output only. Flag to mark the version indicating the launch stage. | [optional] [readonly] 
**createTime** | **String** | Output only. Created time. | [optional] [readonly] 
**description** | **String** | Optional. Description of the resource. | [optional] 
**destinationConfigs** | [**[DestinationConfig]**](DestinationConfig.md) | Optional. Configuration of the Connector&#39;s destination. Only accepted for Connectors that accepts user defined destination(s). | [optional] 
**envoyImageLocation** | **String** | Output only. GCR location where the envoy image is stored. formatted like: gcr.io/{bucketName}/{imageName} | [optional] [readonly] 
**eventingConfig** | [**EventingConfig**](EventingConfig.md) |  | [optional] 
**eventingEnablementType** | **String** | Optional. Eventing enablement type. Will be nil if eventing is not enabled. | [optional] 
**eventingRuntimeData** | [**EventingRuntimeData**](EventingRuntimeData.md) |  | [optional] 
**imageLocation** | **String** | Output only. GCR location where the runtime image is stored. formatted like: gcr.io/{bucketName}/{imageName} | [optional] [readonly] 
**isTrustedTester** | **Boolean** | Output only. Is trusted tester program enabled for the project. | [optional] [readonly] 
**labels** | **{String: String}** | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources | [optional] 
**lockConfig** | [**LockConfig**](LockConfig.md) |  | [optional] 
**logConfig** | [**ConnectorsLogConfig**](ConnectorsLogConfig.md) |  | [optional] 
**name** | **String** | Output only. Resource name of the Connection. Format: projects/{project}/locations/{location}/connections/{connection} | [optional] [readonly] 
**nodeConfig** | [**NodeConfig**](NodeConfig.md) |  | [optional] 
**serviceAccount** | **String** | Optional. Service account needed for runtime plane to access Google Cloud resources. | [optional] 
**serviceDirectory** | **String** | Output only. The name of the Service Directory service name. Used for Private Harpoon to resolve the ILB address. e.g. \&quot;projects/cloud-connectors-e2e-testing/locations/us-central1/namespaces/istio-system/services/istio-ingressgateway-connectors\&quot; | [optional] [readonly] 
**sslConfig** | [**SslConfig**](SslConfig.md) |  | [optional] 
**status** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**subscriptionType** | **String** | Output only. This subscription type enum states the subscription type of the project. | [optional] [readonly] 
**suspended** | **Boolean** | Optional. Suspended indicates if a user has suspended a connection or not. | [optional] 
**updateTime** | **String** | Output only. Updated time. | [optional] [readonly] 



## Enum: ConnectorVersionLaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `PREVIEW` (value: `"PREVIEW"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)

* `PRIVATE_PREVIEW` (value: `"PRIVATE_PREVIEW"`)





## Enum: EventingEnablementTypeEnum


* `EVENTING_ENABLEMENT_TYPE_UNSPECIFIED` (value: `"EVENTING_ENABLEMENT_TYPE_UNSPECIFIED"`)

* `EVENTING_AND_CONNECTION` (value: `"EVENTING_AND_CONNECTION"`)

* `ONLY_EVENTING` (value: `"ONLY_EVENTING"`)





## Enum: SubscriptionTypeEnum


* `SUBSCRIPTION_TYPE_UNSPECIFIED` (value: `"SUBSCRIPTION_TYPE_UNSPECIFIED"`)

* `PAY_G` (value: `"PAY_G"`)

* `PAID` (value: `"PAID"`)




