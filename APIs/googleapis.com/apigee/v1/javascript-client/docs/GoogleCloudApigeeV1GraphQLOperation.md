# ApigeeApi.GoogleCloudApigeeV1GraphQLOperation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **String** | GraphQL operation name. The name and operation type will be used to apply quotas. If no name is specified, the quota will be applied to all GraphQL operations irrespective of their operation names in the payload. | [optional] 
**operationTypes** | **[String]** | Required. GraphQL operation types. Valid values include &#x60;query&#x60; or &#x60;mutation&#x60;. **Note**: Apigee does not currently support &#x60;subscription&#x60; types. | [optional] 


