

# ApiCreateOrUpdateRequestProperties

Api Create or Update Properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiType** | [**ApiTypeEnum**](#ApiTypeEnum) | Type of Api to create.   * &#x60;http&#x60; creates a SOAP to REST API   * &#x60;soap&#x60; creates a SOAP pass-through API . |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) | Format of the Content in which the API is getting imported. |  [optional] |
|**value** | **String** | Content value when Importing an API. |  [optional] |
|**wsdlSelector** | [**ApiCreateOrUpdateRequestPropertiesWsdlSelector**](ApiCreateOrUpdateRequestPropertiesWsdlSelector.md) |  |  [optional] |



## Enum: ApiTypeEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| SOAP | &quot;soap&quot; |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| WADL_XML | &quot;wadl-xml&quot; |
| WADL_LINK_JSON | &quot;wadl-link-json&quot; |
| SWAGGER_JSON | &quot;swagger-json&quot; |
| SWAGGER_LINK_JSON | &quot;swagger-link-json&quot; |
| WSDL | &quot;wsdl&quot; |
| WSDL_LINK | &quot;wsdl-link&quot; |
| OPENAPI | &quot;openapi&quot; |
| OPENAPI_JSON | &quot;openapi+json&quot; |
| OPENAPI_LINK | &quot;openapi-link&quot; |
| OPENAPI_JSON_LINK | &quot;openapi+json-link&quot; |



