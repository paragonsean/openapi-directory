# LegalEntityManagementApi.UnincorporatedPartnership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countryOfGoverningLaw** | **String** | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. | 
**dateOfIncorporation** | **String** | The date when the legal arrangement was incorporated in YYYY-MM-DD format. | [optional] 
**description** | **String** | Short description about the Legal Arrangement. | [optional] 
**doingBusinessAs** | **String** | The registered name, if different from the &#x60;name&#x60;. | [optional] 
**name** | **String** | The legal name. | 
**principalPlaceOfBusiness** | [**Address**](Address.md) | The business address. Required if the principal place of business is different from the &#x60;registeredAddress&#x60;. | [optional] 
**registeredAddress** | [**Address**](Address.md) | The address registered at the registrar, such as the Chamber of Commerce. | 
**registrationNumber** | **String** | The registration number. | [optional] 
**taxInformation** | [**[TaxInformation]**](TaxInformation.md) | The tax information of the entity. | [optional] 
**type** | **String** | Type of Partnership.  Possible values: *  **limitedPartnership** *  **generalPartnership** *  **familyPartnership** *  **commercialPartnership** *  **publicPartnership** *  **otherPartnership** *  **gbr** *  **gmbh** *  **kgaa** *  **cv** *  **vof** *  **maatschap** *  **privateFundLimitedPartnership** *  **businessTrustEntity** *  **businessPartnership** *  **limitedLiabilityPartnership** *  **eg** *  **cooperative** *  **vos** *  **comunidadDeBienes** *  **herenciaYacente** *  **comunidadDePropietarios** *  **sep** *  **sca** *  **bt** *  **kkt** *  **scs** *  **snc**   | 
**vatAbsenceReason** | **String** | The reason for not providing a VAT number.  Possible values: **industryExemption**, **belowTaxThreshold**. | [optional] 
**vatNumber** | **String** | The VAT number. | [optional] 



## Enum: TypeEnum


* `limitedPartnership` (value: `"limitedPartnership"`)

* `generalPartnership` (value: `"generalPartnership"`)

* `familyPartnership` (value: `"familyPartnership"`)

* `commercialPartnership` (value: `"commercialPartnership"`)

* `publicPartnership` (value: `"publicPartnership"`)

* `otherPartnership` (value: `"otherPartnership"`)

* `gbr` (value: `"gbr"`)

* `gmbh` (value: `"gmbh"`)

* `kgaa` (value: `"kgaa"`)

* `cv` (value: `"cv"`)

* `vof` (value: `"vof"`)

* `maatschap` (value: `"maatschap"`)

* `privateFundLimitedPartnership` (value: `"privateFundLimitedPartnership"`)

* `businessTrustEntity` (value: `"businessTrustEntity"`)

* `businessPartnership` (value: `"businessPartnership"`)

* `limitedLiabilityPartnership` (value: `"limitedLiabilityPartnership"`)

* `eg` (value: `"eg"`)

* `cooperative` (value: `"cooperative"`)

* `vos` (value: `"vos"`)

* `comunidadDeBienes` (value: `"comunidadDeBienes"`)

* `herenciaYacente` (value: `"herenciaYacente"`)

* `comunidadDePropietarios` (value: `"comunidadDePropietarios"`)

* `sep` (value: `"sep"`)

* `sca` (value: `"sca"`)

* `bt` (value: `"bt"`)

* `kkt` (value: `"kkt"`)

* `scs` (value: `"scs"`)

* `snc` (value: `"snc"`)





## Enum: VatAbsenceReasonEnum


* `industryExemption` (value: `"industryExemption"`)

* `belowTaxThreshold` (value: `"belowTaxThreshold"`)




