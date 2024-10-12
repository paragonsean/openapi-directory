

# Service

A service status record

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseUrl** | **String** | The url to reach the service, including port as needed |  [optional] |
|**hostid** | **String** | The unique id of the host on which the service is executing |  [optional] |
|**serviceDetail** | [**StatusResponse**](StatusResponse.md) |  |  [optional] |
|**servicename** | **String** | Registered service name |  [optional] |
|**status** | **Boolean** |  |  [optional] |
|**statusMessage** | **String** | A state indicating the condition of the service. Normal operation is &#39;registered&#39; |  [optional] |
|**version** | **String** | The version of the service as reported by the service implementation on registration |  [optional] |



