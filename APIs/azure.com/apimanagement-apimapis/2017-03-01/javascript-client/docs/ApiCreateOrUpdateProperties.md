# ApiManagementClient.ApiCreateOrUpdateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentFormat** | **String** | Format of the Content in which the API is getting imported. | [optional] 
**contentValue** | **String** | Content value when Importing an API. | [optional] 
**wsdlSelector** | **Object** | Criteria to limit import of WSDL to a subset of the document. | [optional] 
**apiVersionSet** | **Object** | Api Version Set Contract details. | [optional] 
**displayName** | **String** | API name. | [optional] 
**path** | **String** | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance. It is appended to the API endpoint base URL specified during the service instance creation to form a public URL for this API. | 
**protocols** | **[String]** | Describes on which protocols the operations in this API can be invoked. | [optional] 
**serviceUrl** | **String** | Absolute URL of the backend service implementing this API. | [optional] 
**apiRevision** | **String** | Describes the Revision of the Api. If no value is provided, default revision 1 is created | [optional] 
**apiVersion** | **String** | Indicates the Version identifier of the API if the API is versioned | [optional] 
**apiVersionSetId** | **String** | A resource identifier for the related ApiVersionSet. | [optional] 
**authenticationSettings** | [**ApiContractPropertiesAllOfAuthenticationSettings**](ApiContractPropertiesAllOfAuthenticationSettings.md) |  | [optional] 
**description** | **String** | Description of the API. May include HTML formatting tags. | [optional] 
**isCurrent** | **Boolean** | Indicates if API revision is current api revision. | [optional] [readonly] 
**isOnline** | **Boolean** | Indicates if API revision is accessible via the gateway. | [optional] [readonly] 
**subscriptionKeyParameterNames** | [**ApiContractPropertiesAllOfSubscriptionKeyParameterNames**](ApiContractPropertiesAllOfSubscriptionKeyParameterNames.md) |  | [optional] 
**type** | **String** | Type of API. | [optional] 



## Enum: ContentFormatEnum


* `wadl-xml` (value: `"wadl-xml"`)

* `wadl-link-json` (value: `"wadl-link-json"`)

* `swagger-json` (value: `"swagger-json"`)

* `swagger-link-json` (value: `"swagger-link-json"`)

* `wsdl` (value: `"wsdl"`)

* `wsdl-link` (value: `"wsdl-link"`)





## Enum: [ProtocolsEnum]


* `http` (value: `"http"`)

* `https` (value: `"https"`)





## Enum: TypeEnum


* `http` (value: `"http"`)

* `soap` (value: `"soap"`)




