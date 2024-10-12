

# GoogleCloudServicebrokerV1beta1CreateServiceInstanceResponse

Response for the `CreateServiceInstance()` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Used to communicate description of the response. Usually for non-standard error codes. https://github.com/openservicebrokerapi/servicebroker/blob/master/spec.md#service-broker-errors |  [optional] |
|**operation** | **String** | If broker executes operation asynchronously, this is the operation ID that can be polled to check the completion status of said operation. This broker always will return a non-empty operation on success. |  [optional] |



