# ApigeeApi.GoogleCloudApigeeV1GrpcOperationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiSource** | **String** | Required. Name of the API proxy with which the gRPC operation and quota are associated. | [optional] 
**attributes** | [**[GoogleCloudApigeeV1Attribute]**](GoogleCloudApigeeV1Attribute.md) | Custom attributes associated with the operation. | [optional] 
**methods** | **[String]** | List of unqualified gRPC method names for the proxy to which quota will be applied. If this field is empty, the Quota will apply to all operations on the gRPC service defined on the proxy. Example: Given a proxy that is configured to serve com.petstore.PetService, the methods com.petstore.PetService.ListPets and com.petstore.PetService.GetPet would be specified here as simply [\&quot;ListPets\&quot;, \&quot;GetPet\&quot;]. | [optional] 
**quota** | [**GoogleCloudApigeeV1Quota**](GoogleCloudApigeeV1Quota.md) |  | [optional] 
**service** | **String** | Required. gRPC Service name associated to be associated with the API proxy, on which quota rules can be applied upon. | [optional] 


