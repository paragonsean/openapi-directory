# IncreaseApi.CreateAnEntityParametersTrust

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CreateAnEntityParametersTrustAddress**](CreateAnEntityParametersTrustAddress.md) |  | 
**category** | **String** | Whether the trust is &#x60;revocable&#x60; or &#x60;irrevocable&#x60;. Irrevocable trusts require their own Employer Identification Number. Revocable trusts require information about the individual &#x60;grantor&#x60; who created the trust. | 
**formationDocumentFileId** | **String** | The identifier of the File containing the formation document of the trust. | [optional] 
**formationState** | **String** | The two-letter United States Postal Service (USPS) abbreviation for the state in which the trust was formed. | [optional] 
**grantor** | [**CreateAnEntityParametersTrustGrantor**](CreateAnEntityParametersTrustGrantor.md) |  | [optional] 
**name** | **String** | The legal name of the trust. | 
**taxIdentifier** | **String** | The Employer Identification Number (EIN) for the trust. Required if &#x60;category&#x60; is equal to &#x60;irrevocable&#x60;. | [optional] 
**trustees** | [**[CreateAnEntityParametersTrustTrusteesInner]**](CreateAnEntityParametersTrustTrusteesInner.md) | The trustees of the trust. | 



## Enum: CategoryEnum


* `revocable` (value: `"revocable"`)

* `irrevocable` (value: `"irrevocable"`)




