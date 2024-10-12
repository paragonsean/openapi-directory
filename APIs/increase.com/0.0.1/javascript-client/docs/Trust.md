# IncreaseApi.Trust

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address2**](Address2.md) |  | 
**category** | **String** | Whether the trust is &#x60;revocable&#x60; or &#x60;irrevocable&#x60;. | 
**formationDocumentFileId** | **String** | The ID for the File containing the formation document of the trust. | 
**formationState** | **String** | The two-letter United States Postal Service (USPS) abbreviation for the state in which the trust was formed. | 
**grantor** | [**Individual3**](Individual3.md) |  | 
**name** | **String** | The trust&#39;s name | 
**taxIdentifier** | **String** | The Employer Identification Number (EIN) of the trust itself. | 
**trustees** | [**[TrusteesElement]**](TrusteesElement.md) | The trustees of the trust. | 



## Enum: CategoryEnum


* `revocable` (value: `"revocable"`)

* `irrevocable` (value: `"irrevocable"`)




