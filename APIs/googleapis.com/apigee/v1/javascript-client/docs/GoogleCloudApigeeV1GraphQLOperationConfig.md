# ApigeeApi.GoogleCloudApigeeV1GraphQLOperationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiSource** | **String** | Required. Name of the API proxy endpoint or remote service with which the GraphQL operation and quota are associated. | [optional] 
**attributes** | [**[GoogleCloudApigeeV1Attribute]**](GoogleCloudApigeeV1Attribute.md) | Custom attributes associated with the operation. | [optional] 
**operations** | [**[GoogleCloudApigeeV1GraphQLOperation]**](GoogleCloudApigeeV1GraphQLOperation.md) | Required. List of GraphQL name/operation type pairs for the proxy or remote service to which quota will be applied. If only operation types are specified, the quota will be applied to all GraphQL requests irrespective of the GraphQL name. **Note**: Currently, you can specify only a single GraphQLOperation. Specifying more than one will cause the operation to fail. | [optional] 
**quota** | [**GoogleCloudApigeeV1Quota**](GoogleCloudApigeeV1Quota.md) |  | [optional] 


