

# ApiContract

API details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | API identifier path: /apis/{apiId} |  [optional] [readonly] |
|**name** | **String** | API name. |  |
|**path** | **String** | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. |  |
|**protocols** | [**List&lt;ProtocolsEnum&gt;**](#List&lt;ProtocolsEnum&gt;) | Describes on which protocols the operations in this API can be invoked. |  |
|**serviceUrl** | **String** | Absolute URL of the backend service implementing this API. |  |
|**authenticationSettings** | [**AuthenticationSettingsContract**](AuthenticationSettingsContract.md) |  |  [optional] |
|**description** | **String** | Description of the API. May include HTML formatting tags. |  [optional] |
|**subscriptionKeyParameterNames** | [**SubscriptionKeyParameterNamesContract**](SubscriptionKeyParameterNamesContract.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of API. |  [optional] |



## Enum: List&lt;ProtocolsEnum&gt;

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| SOAP | &quot;Soap&quot; |



