

# ApiUpdateRequestProperties

API update contract properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | API name. |  [optional] |
|**path** | **String** | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. |  [optional] |
|**protocols** | [**List&lt;ProtocolsEnum&gt;**](#List&lt;ProtocolsEnum&gt;) | Describes on which protocols the operations in this API can be invoked. |  [optional] |
|**serviceUrl** | **String** | Absolute URL of the backend service implementing this API. |  [optional] |



## Enum: List&lt;ProtocolsEnum&gt;

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| HTTPS | &quot;https&quot; |



