

# UnincorporatedPartnership


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countryOfGoverningLaw** | **String** | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the governing country. |  |
|**dateOfIncorporation** | **String** | The date when the legal arrangement was incorporated in YYYY-MM-DD format. |  [optional] |
|**doingBusinessAs** | **String** | The registered name, if different from the &#x60;name&#x60;. |  [optional] |
|**name** | **String** | The legal name. |  |
|**principalPlaceOfBusiness** | [**Address**](Address.md) | The business address. Required if the principal place of business is different from the &#x60;registeredAddress&#x60;. |  [optional] |
|**registeredAddress** | [**Address**](Address.md) | The address registered at the registrar, such as the Chamber of Commerce. |  |
|**registrationNumber** | **String** | The registration number. |  [optional] |
|**taxInformation** | [**List&lt;TaxInformation&gt;**](TaxInformation.md) | The tax information of the entity. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of Partnership.  Possible values: *  **limitedPartnership** *  **generalPartnership** *  **familyPartnership** *  **commercialPartnership** *  **publicPartnership** *  **otherPartnership** *  **gbr** *  **gmbh** *  **kgaa** *  **cv** *  **vof** *  **maatschap** *  **privateFundLimitedPartnership** *  **businessTrustEntity** *  **businessPartnership** *  **limitedLiabilityPartnership** *  **eg** *  **cooperative** *  **vos** *  **comunidadDeBienes** *  **herenciaYacente** *  **comunidadDePropietarios** *  **sep** *  **sca** *  **bt** *  **kkt** *  **scs** *  **snc**   |  |
|**vatAbsenceReason** | [**VatAbsenceReasonEnum**](#VatAbsenceReasonEnum) | The reason for not providing a VAT number.  Possible values: **industryExemption**, **belowTaxThreshold**. |  [optional] |
|**vatNumber** | **String** | The VAT number. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LIMITED_PARTNERSHIP | &quot;limitedPartnership&quot; |
| GENERAL_PARTNERSHIP | &quot;generalPartnership&quot; |
| FAMILY_PARTNERSHIP | &quot;familyPartnership&quot; |
| COMMERCIAL_PARTNERSHIP | &quot;commercialPartnership&quot; |
| PUBLIC_PARTNERSHIP | &quot;publicPartnership&quot; |
| OTHER_PARTNERSHIP | &quot;otherPartnership&quot; |
| GBR | &quot;gbr&quot; |
| GMBH | &quot;gmbh&quot; |
| KGAA | &quot;kgaa&quot; |
| CV | &quot;cv&quot; |
| VOF | &quot;vof&quot; |
| MAATSCHAP | &quot;maatschap&quot; |
| PRIVATE_FUND_LIMITED_PARTNERSHIP | &quot;privateFundLimitedPartnership&quot; |
| BUSINESS_TRUST_ENTITY | &quot;businessTrustEntity&quot; |
| BUSINESS_PARTNERSHIP | &quot;businessPartnership&quot; |
| LIMITED_LIABILITY_PARTNERSHIP | &quot;limitedLiabilityPartnership&quot; |
| EG | &quot;eg&quot; |
| COOPERATIVE | &quot;cooperative&quot; |
| VOS | &quot;vos&quot; |
| COMUNIDAD_DE_BIENES | &quot;comunidadDeBienes&quot; |
| HERENCIA_YACENTE | &quot;herenciaYacente&quot; |
| COMUNIDAD_DE_PROPIETARIOS | &quot;comunidadDePropietarios&quot; |
| SEP | &quot;sep&quot; |
| SCA | &quot;sca&quot; |
| BT | &quot;bt&quot; |
| KKT | &quot;kkt&quot; |
| SCS | &quot;scs&quot; |
| SNC | &quot;snc&quot; |



## Enum: VatAbsenceReasonEnum

| Name | Value |
|---- | -----|
| INDUSTRY_EXEMPTION | &quot;industryExemption&quot; |
| BELOW_TAX_THRESHOLD | &quot;belowTaxThreshold&quot; |



