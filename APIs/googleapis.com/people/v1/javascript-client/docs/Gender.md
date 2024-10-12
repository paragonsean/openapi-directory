# PeopleApi.Gender

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressMeAs** | **String** | Free form text field for pronouns that should be used to address the person. Common values are: * &#x60;he&#x60;/&#x60;him&#x60; * &#x60;she&#x60;/&#x60;her&#x60; * &#x60;they&#x60;/&#x60;them&#x60; | [optional] 
**formattedValue** | **String** | Output only. The value of the gender translated and formatted in the viewer&#39;s account locale or the &#x60;Accept-Language&#x60; HTTP header locale. Unspecified or custom value are not localized. | [optional] [readonly] 
**metadata** | [**FieldMetadata**](FieldMetadata.md) |  | [optional] 
**value** | **String** | The gender for the person. The gender can be custom or one of these predefined values: * &#x60;male&#x60; * &#x60;female&#x60; * &#x60;unspecified&#x60; | [optional] 


