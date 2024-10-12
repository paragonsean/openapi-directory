

# ProductApiCreateOrUpdate200Response

Api Contract Details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Identifier of the Entity |  [optional] |
|**name** | **String** | API name. |  [optional] |
|**path** | **String** | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. |  |
|**protocols** | [**List&lt;ProtocolsEnum&gt;**](#List&lt;ProtocolsEnum&gt;) | Describes on which protocols the operations in this API can be invoked. |  [optional] |
|**serviceUrl** | **String** | Absolute URL of the backend service implementing this API. |  [optional] |
|**apiRevision** | **String** | Describes the Revision of the Api. If no value is provided, default revision 1 is created |  [optional] |
|**authenticationSettings** | [**ProductApiCreateOrUpdate200ResponseAllOfAllOfAuthenticationSettings**](ProductApiCreateOrUpdate200ResponseAllOfAllOfAuthenticationSettings.md) |  |  [optional] |
|**description** | **String** | Description of the API. May include HTML formatting tags. |  [optional] |
|**isCurrent** | **Boolean** | Indicates if API revision is current api revision. |  [optional] |
|**isOnline** | **Boolean** | Indicates if API revision is accessible via the gateway. |  [optional] |
|**subscriptionKeyParameterNames** | [**ProductApiCreateOrUpdate200ResponseAllOfAllOfSubscriptionKeyParameterNames**](ProductApiCreateOrUpdate200ResponseAllOfAllOfSubscriptionKeyParameterNames.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of API. |  [optional] |



## Enum: List&lt;ProtocolsEnum&gt;

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| HTTPS | &quot;https&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| SOAP | &quot;soap&quot; |



