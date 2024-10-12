# ApiManagementClient.ApiCreateOrUpdateRequestProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiType** | **String** | Type of Api to create.   * &#x60;http&#x60; creates a SOAP to REST API   * &#x60;soap&#x60; creates a SOAP pass-through API . | [optional] 
**format** | **String** | Format of the Content in which the API is getting imported. | [optional] 
**value** | **String** | Content value when Importing an API. | [optional] 
**wsdlSelector** | [**ApiCreateOrUpdateRequestPropertiesWsdlSelector**](ApiCreateOrUpdateRequestPropertiesWsdlSelector.md) |  | [optional] 



## Enum: ApiTypeEnum


* `http` (value: `"http"`)

* `soap` (value: `"soap"`)





## Enum: FormatEnum


* `wadl-xml` (value: `"wadl-xml"`)

* `wadl-link-json` (value: `"wadl-link-json"`)

* `swagger-json` (value: `"swagger-json"`)

* `swagger-link-json` (value: `"swagger-link-json"`)

* `wsdl` (value: `"wsdl"`)

* `wsdl-link` (value: `"wsdl-link"`)

* `openapi` (value: `"openapi"`)

* `openapi+json` (value: `"openapi+json"`)

* `openapi-link` (value: `"openapi-link"`)

* `openapi+json-link` (value: `"openapi+json-link"`)




