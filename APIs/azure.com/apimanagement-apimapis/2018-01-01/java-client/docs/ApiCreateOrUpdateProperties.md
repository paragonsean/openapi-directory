

# ApiCreateOrUpdateProperties

Api Create or Update Properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiType** | [**ApiTypeEnum**](#ApiTypeEnum) | Type of Api to create.   * &#x60;http&#x60; creates a SOAP to REST API   * &#x60;soap&#x60; creates a SOAP pass-through API . |  [optional] |
|**contentFormat** | [**ContentFormatEnum**](#ContentFormatEnum) | Format of the Content in which the API is getting imported. |  [optional] |
|**contentValue** | **String** | Content value when Importing an API. |  [optional] |
|**wsdlSelector** | [**Object**](Object.md) | Criteria to limit import of WSDL to a subset of the document. |  [optional] |
|**apiVersionSet** | [**ApiVersionSetContractDetails**](ApiVersionSetContractDetails.md) |  |  [optional] |
|**displayName** | **String** | API name. |  [optional] |
|**path** | **String** | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. |  |
|**protocols** | [**List&lt;ProtocolsEnum&gt;**](#List&lt;ProtocolsEnum&gt;) | Describes on which protocols the operations in this API can be invoked. |  [optional] |
|**serviceUrl** | **String** | Absolute URL of the backend service implementing this API. |  [optional] |
|**apiRevision** | **String** | Describes the Revision of the Api. If no value is provided, default revision 1 is created |  [optional] |
|**apiRevisionDescription** | **String** | Description of the Api Revision. |  [optional] |
|**apiVersion** | **String** | Indicates the Version identifier of the API if the API is versioned |  [optional] |
|**apiVersionDescription** | **String** | Description of the Api Version. |  [optional] |
|**apiVersionSetId** | **String** | A resource identifier for the related ApiVersionSet. |  [optional] |
|**authenticationSettings** | [**ApiEntityBaseContractAuthenticationSettings**](ApiEntityBaseContractAuthenticationSettings.md) |  |  [optional] |
|**description** | **String** | Description of the API. May include HTML formatting tags. |  [optional] |
|**isCurrent** | **Boolean** | Indicates if API revision is current api revision. |  [optional] [readonly] |
|**isOnline** | **Boolean** | Indicates if API revision is accessible via the gateway. |  [optional] [readonly] |
|**subscriptionKeyParameterNames** | [**ApiEntityBaseContractSubscriptionKeyParameterNames**](ApiEntityBaseContractSubscriptionKeyParameterNames.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of API. |  [optional] |



## Enum: ApiTypeEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| SOAP | &quot;soap&quot; |



## Enum: ContentFormatEnum

| Name | Value |
|---- | -----|
| WADL_XML | &quot;wadl-xml&quot; |
| WADL_LINK_JSON | &quot;wadl-link-json&quot; |
| SWAGGER_JSON | &quot;swagger-json&quot; |
| SWAGGER_LINK_JSON | &quot;swagger-link-json&quot; |
| WSDL | &quot;wsdl&quot; |
| WSDL_LINK | &quot;wsdl-link&quot; |



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



