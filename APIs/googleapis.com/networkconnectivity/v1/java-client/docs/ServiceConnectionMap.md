

# ServiceConnectionMap

The ServiceConnectionMap resource. Next id: 15

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerPscConfigs** | [**List&lt;ConsumerPscConfig&gt;**](ConsumerPscConfig.md) | The PSC configurations on consumer side. |  [optional] |
|**consumerPscConnections** | [**List&lt;ConsumerPscConnection&gt;**](ConsumerPscConnection.md) | Output only. PSC connection details on consumer side. |  [optional] [readonly] |
|**createTime** | **String** | Output only. Time when the ServiceConnectionMap was created. |  [optional] [readonly] |
|**description** | **String** | A description of this resource. |  [optional] |
|**etag** | **String** | Optional. The etag is computed by the server, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |  [optional] |
|**infrastructure** | [**InfrastructureEnum**](#InfrastructureEnum) | Output only. The infrastructure used for connections between consumers/producers. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels. |  [optional] |
|**name** | **String** | Immutable. The name of a ServiceConnectionMap. Format: projects/{project}/locations/{location}/serviceConnectionMaps/{service_connection_map} See: https://google.aip.dev/122#fields-representing-resource-names |  [optional] |
|**producerPscConfigs** | [**List&lt;ProducerPscConfig&gt;**](ProducerPscConfig.md) | The PSC configurations on producer side. |  [optional] |
|**serviceClass** | **String** | The service class identifier this ServiceConnectionMap is for. The user of ServiceConnectionMap create API needs to have networkconnecitivty.serviceclasses.use iam permission for the service class. |  [optional] |
|**serviceClassUri** | **String** | Output only. The service class uri this ServiceConnectionMap is for. |  [optional] [readonly] |
|**token** | **String** | The token provided by the consumer. This token authenticates that the consumer can create a connecton within the specified project and network. |  [optional] |
|**updateTime** | **String** | Output only. Time when the ServiceConnectionMap was updated. |  [optional] [readonly] |



## Enum: InfrastructureEnum

| Name | Value |
|---- | -----|
| INFRASTRUCTURE_UNSPECIFIED | &quot;INFRASTRUCTURE_UNSPECIFIED&quot; |
| PSC | &quot;PSC&quot; |



