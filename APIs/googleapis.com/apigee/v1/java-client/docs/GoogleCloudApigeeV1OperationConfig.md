

# GoogleCloudApigeeV1OperationConfig

Binds the resources in an API proxy or remote service with the allowed REST methods and associated quota enforcement.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiSource** | **String** | Required. Name of the API proxy or remote service with which the resources, methods, and quota are associated. |  [optional] |
|**attributes** | [**List&lt;GoogleCloudApigeeV1Attribute&gt;**](GoogleCloudApigeeV1Attribute.md) | Custom attributes associated with the operation. |  [optional] |
|**operations** | [**List&lt;GoogleCloudApigeeV1Operation&gt;**](GoogleCloudApigeeV1Operation.md) | List of resource/method pairs for the API proxy or remote service to which quota will applied. **Note**: Currently, you can specify only a single resource/method pair. The call will fail if more than one resource/method pair is provided. |  [optional] |
|**quota** | [**GoogleCloudApigeeV1Quota**](GoogleCloudApigeeV1Quota.md) |  |  [optional] |



