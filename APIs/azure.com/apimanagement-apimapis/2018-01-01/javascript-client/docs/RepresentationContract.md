# ApiManagementClient.RepresentationContract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentType** | **String** | Specifies a registered or custom content type for this representation, e.g. application/xml. | 
**formParameters** | [**[ParameterContract]**](ParameterContract.md) | Collection of form parameters. Required if &#39;contentType&#39; value is either &#39;application/x-www-form-urlencoded&#39; or &#39;multipart/form-data&#39;.. | [optional] 
**sample** | **String** | An example of the representation. | [optional] 
**schemaId** | **String** | Schema identifier. Applicable only if &#39;contentType&#39; value is neither &#39;application/x-www-form-urlencoded&#39; nor &#39;multipart/form-data&#39;. | [optional] 
**typeName** | **String** | Type name defined by the schema. Applicable only if &#39;contentType&#39; value is neither &#39;application/x-www-form-urlencoded&#39; nor &#39;multipart/form-data&#39;. | [optional] 


