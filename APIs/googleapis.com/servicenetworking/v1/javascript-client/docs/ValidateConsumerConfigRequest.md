# ServiceNetworkingApi.ValidateConsumerConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkServiceNetworkingUsePermission** | **Boolean** | Optional. The IAM permission check determines whether the consumer project has &#39;servicenetworking.services.use&#39; permission or not. | [optional] 
**consumerNetwork** | **String** | Required. The network that the consumer is using to connect with services. Must be in the form of projects/{project}/global/networks/{network} {project} is a project number, as in &#39;12345&#39; {network} is network name. | [optional] 
**consumerProject** | [**ConsumerProject**](ConsumerProject.md) |  | [optional] 
**rangeReservation** | [**RangeReservation**](RangeReservation.md) |  | [optional] 
**validateNetwork** | **Boolean** | The validations will be performed in the order listed in the ValidationError enum. The first failure will return. If a validation is not requested, then the next one will be performed. SERVICE_NETWORKING_NOT_ENABLED and NETWORK_NOT_PEERED checks are performed for all requests where validation is requested. NETWORK_NOT_FOUND and NETWORK_DISCONNECTED checks are done for requests that have validate_network set to true. | [optional] 


