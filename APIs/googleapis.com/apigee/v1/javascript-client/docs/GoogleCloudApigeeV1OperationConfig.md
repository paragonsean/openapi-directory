# ApigeeApi.GoogleCloudApigeeV1OperationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiSource** | **String** | Required. Name of the API proxy or remote service with which the resources, methods, and quota are associated. | [optional] 
**attributes** | [**[GoogleCloudApigeeV1Attribute]**](GoogleCloudApigeeV1Attribute.md) | Custom attributes associated with the operation. | [optional] 
**operations** | [**[GoogleCloudApigeeV1Operation]**](GoogleCloudApigeeV1Operation.md) | List of resource/method pairs for the API proxy or remote service to which quota will applied. **Note**: Currently, you can specify only a single resource/method pair. The call will fail if more than one resource/method pair is provided. | [optional] 
**quota** | [**GoogleCloudApigeeV1Quota**](GoogleCloudApigeeV1Quota.md) |  | [optional] 


