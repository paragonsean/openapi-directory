

# Trust


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
|**type** | [**TypeEnum**](#TypeEnum) | Type of trust.  Possible values for Australian trusts: **cashManagementTrust**, **corporateUnitTrust**, **deceasedEstate**, **discretionaryInvestmentTrust**, **discretionaryServicesManagementTrust**, **discretionaryTradingTrust**, **firstHomeSaverAccountsTrust**, **fixedTrust**, **fixedUnitTrust**, **hybridTrust**, **listedPublicUnitTrust**, **otherTrust**, **pooledSuperannuationTrust**, **publicTradingTrust**, **unlistedPublicUnitTrust**. |  |
|**undefinedBeneficiaryInfo** | [**List&lt;UndefinedBeneficiary&gt;**](UndefinedBeneficiary.md) | The undefined beneficiary information of the entity. |  [optional] |
|**vatAbsenceReason** | [**VatAbsenceReasonEnum**](#VatAbsenceReasonEnum) | The reason for not providing a VAT number.  Possible values: **industryExemption**, **belowTaxThreshold**. |  [optional] |
|**vatNumber** | **String** | The VAT number. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CASH_MANAGEMENT_TRUST | &quot;cashManagementTrust&quot; |
| CORPORATE_UNIT_TRUST | &quot;corporateUnitTrust&quot; |
| DECEASED_ESTATE | &quot;deceasedEstate&quot; |
| DISCRETIONARY_INVESTMENT_TRUST | &quot;discretionaryInvestmentTrust&quot; |
| DISCRETIONARY_SERVICES_MANAGEMENT_TRUST | &quot;discretionaryServicesManagementTrust&quot; |
| DISCRETIONARY_TRADING_TRUST | &quot;discretionaryTradingTrust&quot; |
| FIRST_HOME_SAVER_ACCOUNTS_TRUST | &quot;firstHomeSaverAccountsTrust&quot; |
| FIXED_TRUST | &quot;fixedTrust&quot; |
| FIXED_UNIT_TRUST | &quot;fixedUnitTrust&quot; |
| HYBRID_TRUST | &quot;hybridTrust&quot; |
| LISTED_PUBLIC_UNIT_TRUST | &quot;listedPublicUnitTrust&quot; |
| OTHER_TRUST | &quot;otherTrust&quot; |
| POOLED_SUPERANNUATION_TRUST | &quot;pooledSuperannuationTrust&quot; |
| PUBLIC_TRADING_TRUST | &quot;publicTradingTrust&quot; |
| UNLISTED_PUBLIC_UNIT_TRUST | &quot;unlistedPublicUnitTrust&quot; |



## Enum: VatAbsenceReasonEnum

| Name | Value |
|---- | -----|
| INDUSTRY_EXEMPTION | &quot;industryExemption&quot; |
| BELOW_TAX_THRESHOLD | &quot;belowTaxThreshold&quot; |



