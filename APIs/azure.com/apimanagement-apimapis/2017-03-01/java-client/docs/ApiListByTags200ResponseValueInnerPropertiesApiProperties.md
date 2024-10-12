

# ApiListByTags200ResponseValueInnerPropertiesApiProperties

Api Entity Properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersionSet** | [**ApiListByTags200ResponseValueInnerPropertiesApiPropertiesApiVersionSet**](ApiListByTags200ResponseValueInnerPropertiesApiPropertiesApiVersionSet.md) |  |  [optional] |
|**displayName** | **String** | API name. |  [optional] |
|**path** | **String** | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. |  |
|**protocols** | [**List&lt;ProtocolsEnum&gt;**](#List&lt;ProtocolsEnum&gt;) | Describes on which protocols the operations in this API can be invoked. |  [optional] |
|**serviceUrl** | **String** | Absolute URL of the backend service implementing this API. |  [optional] |



## Enum: List&lt;ProtocolsEnum&gt;

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| HTTPS | &quot;https&quot; |



