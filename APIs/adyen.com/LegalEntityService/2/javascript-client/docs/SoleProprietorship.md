# LegalEntityManagementApi.SoleProprietorship

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countryOfGoverningLaw** | **String** | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. | 
**dateOfIncorporation** | **String** | The date when the legal arrangement was incorporated in YYYY-MM-DD format. | [optional] 
**doingBusinessAs** | **String** | The registered name, if different from the &#x60;name&#x60;. | [optional] 
**name** | **String** | The legal name. | 
**principalPlaceOfBusiness** | [**Address**](Address.md) | The business address. Required if the principal place of business is different from the &#x60;registeredAddress&#x60;. | [optional] 
**registeredAddress** | [**Address**](Address.md) | The address registered at the registrar, such as the Chamber of Commerce. | 
**registrationNumber** | **String** | The registration number. | [optional] 
**taxInformation** | [**[TaxInformation]**](TaxInformation.md) | The tax information of the entity. | [optional] 
**vatAbsenceReason** | **String** | The reason for not providing a VAT number.  Possible values: **industryExemption**, **belowTaxThreshold**. | [optional] 
**vatNumber** | **String** | The VAT number. | [optional] 



## Enum: VatAbsenceReasonEnum


* `industryExemption` (value: `"industryExemption"`)

* `belowTaxThreshold` (value: `"belowTaxThreshold"`)




