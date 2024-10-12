# NetworkConnectivityApi.ServiceConnectionPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Time when the ServiceConnectionMap was created. | [optional] [readonly] 
**description** | **String** | A description of this resource. | [optional] 
**etag** | **String** | Optional. The etag is computed by the server, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] 
**infrastructure** | **String** | Output only. The type of underlying resources used to create the connection. | [optional] [readonly] 
**labels** | **{String: String}** | User-defined labels. | [optional] 
**name** | **String** | Immutable. The name of a ServiceConnectionPolicy. Format: projects/{project}/locations/{location}/serviceConnectionPolicies/{service_connection_policy} See: https://google.aip.dev/122#fields-representing-resource-names | [optional] 
**network** | **String** | The resource path of the consumer network. Example: - projects/{projectNumOrId}/global/networks/{resourceId}. | [optional] 
**pscConfig** | [**PscConfig**](PscConfig.md) |  | [optional] 
**pscConnections** | [**[PscConnection]**](PscConnection.md) | Output only. [Output only] Information about each Private Service Connect connection. | [optional] [readonly] 
**serviceClass** | **String** | The service class identifier for which this ServiceConnectionPolicy is for. The service class identifier is a unique, symbolic representation of a ServiceClass. It is provided by the Service Producer. Google services have a prefix of gcp. For example, gcp-cloud-sql. 3rd party services do not. For example, test-service-a3dfcx. | [optional] 
**updateTime** | **String** | Output only. Time when the ServiceConnectionMap was updated. | [optional] [readonly] 



## Enum: InfrastructureEnum


* `INFRASTRUCTURE_UNSPECIFIED` (value: `"INFRASTRUCTURE_UNSPECIFIED"`)

* `PSC` (value: `"PSC"`)




