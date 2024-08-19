

# LegalArrangementDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**ViasAddress**](ViasAddress.md) | The address of the legal arrangement. |  |
|**legalArrangementCode** | **String** | Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement. Use only when updating an account holder. If you include this field when creating an account holder, the request will fail. |  [optional] |
|**legalArrangementEntities** | [**List&lt;LegalArrangementEntityDetail&gt;**](LegalArrangementEntityDetail.md) | An array containing information about other entities that are part of the legal arrangement. |  [optional] |
|**legalArrangementReference** | **String** | Your reference for the legal arrangement. Must be between 3 to 128 characters. |  [optional] |
|**legalForm** | [**LegalFormEnum**](#LegalFormEnum) | The form of legal arrangement. Required if &#x60;type&#x60; is **Trust** or **Partnership**.  The possible values depend on the &#x60;type&#x60;.  - For &#x60;type&#x60; **Trust**:  **CashManagementTrust**, **CorporateUnitTrust**, **DeceasedEstate**, **DiscretionaryInvestmentTrust**, **DiscretionaryServicesManagementTrust**, **DiscretionaryTradingTrust**, **FirstHomeSaverAccountsTrust**, **FixedTrust**, **FixedUnitTrust**, **HybridTrust**, **ListedPublicUnitTrust**, **OtherTrust**, **PooledSuperannuationTrust**, **PublicTradingTrust**, or **UnlistedPublicUnitTrust**.  - For &#x60;type&#x60; **Partnership**: **LimitedPartnership**, **FamilyPartnership**, or **OtherPartnership** |  [optional] |
|**name** | **String** | The legal name of the legal arrangement. Minimum length: 3 characters. |  |
|**registrationNumber** | **String** | The registration number of the legal arrangement. |  [optional] |
|**taxNumber** | **String** | The tax identification number of the legal arrangement. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The [type of legal arrangement](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/legal-arrangements#types-of-legal-arrangements).  Possible values:  - **Association**   - **Partnership**   - **SoleProprietorship**   - **Trust**    |  |



## Enum: LegalFormEnum

| Name | Value |
|---- | -----|
| CASH_MANAGEMENT_TRUST | &quot;CashManagementTrust&quot; |
| CORPORATE_UNIT_TRUST | &quot;CorporateUnitTrust&quot; |
| DECEASED_ESTATE | &quot;DeceasedEstate&quot; |
| DISCRETIONARY_INVESTMENT_TRUST | &quot;DiscretionaryInvestmentTrust&quot; |
| DISCRETIONARY_SERVICES_MANAGEMENT_TRUST | &quot;DiscretionaryServicesManagementTrust&quot; |
| DISCRETIONARY_TRADING_TRUST | &quot;DiscretionaryTradingTrust&quot; |
| FIRST_HOME_SAVER_ACCOUNTS_TRUST | &quot;FirstHomeSaverAccountsTrust&quot; |
| FIXED_TRUST | &quot;FixedTrust&quot; |
| FIXED_UNIT_TRUST | &quot;FixedUnitTrust&quot; |
| HYBRID_TRUST | &quot;HybridTrust&quot; |
| LISTED_PUBLIC_UNIT_TRUST | &quot;ListedPublicUnitTrust&quot; |
| OTHER_TRUST | &quot;OtherTrust&quot; |
| POOLED_SUPERANNUATION_TRUST | &quot;PooledSuperannuationTrust&quot; |
| PUBLIC_TRADING_TRUST | &quot;PublicTradingTrust&quot; |
| UNLISTED_PUBLIC_UNIT_TRUST | &quot;UnlistedPublicUnitTrust&quot; |
| LIMITED_PARTNERSHIP | &quot;LimitedPartnership&quot; |
| FAMILY_PARTNERSHIP | &quot;FamilyPartnership&quot; |
| OTHER_PARTNERSHIP | &quot;OtherPartnership&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ASSOCIATION | &quot;Association&quot; |
| PARTNERSHIP | &quot;Partnership&quot; |
| SOLE_PROPRIETORSHIP | &quot;SoleProprietorship&quot; |
| TRUST | &quot;Trust&quot; |



