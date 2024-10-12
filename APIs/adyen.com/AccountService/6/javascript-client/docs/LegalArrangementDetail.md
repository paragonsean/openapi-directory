# AccountApi.LegalArrangementDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**ViasAddress**](ViasAddress.md) | The address of the legal arrangement. | 
**legalArrangementCode** | **String** | Adyen-generated unique alphanumeric identifier (UUID) for the entry, returned in the response when you create a legal arrangement. Use only when updating an account holder. If you include this field when creating an account holder, the request will fail. | [optional] 
**legalArrangementEntities** | [**[LegalArrangementEntityDetail]**](LegalArrangementEntityDetail.md) | An array containing information about other entities that are part of the legal arrangement. | [optional] 
**legalArrangementReference** | **String** | Your reference for the legal arrangement. Must be between 3 to 128 characters. | [optional] 
**legalForm** | **String** | The form of legal arrangement. Required if &#x60;type&#x60; is **Trust** or **Partnership**.  The possible values depend on the &#x60;type&#x60;.  - For &#x60;type&#x60; **Trust**:  **CashManagementTrust**, **CorporateUnitTrust**, **DeceasedEstate**, **DiscretionaryInvestmentTrust**, **DiscretionaryServicesManagementTrust**, **DiscretionaryTradingTrust**, **FirstHomeSaverAccountsTrust**, **FixedTrust**, **FixedUnitTrust**, **HybridTrust**, **ListedPublicUnitTrust**, **OtherTrust**, **PooledSuperannuationTrust**, **PublicTradingTrust**, or **UnlistedPublicUnitTrust**.  - For &#x60;type&#x60; **Partnership**: **LimitedPartnership**, **FamilyPartnership**, or **OtherPartnership** | [optional] 
**name** | **String** | The legal name of the legal arrangement. Minimum length: 3 characters. | 
**registrationNumber** | **String** | The registration number of the legal arrangement. | [optional] 
**taxNumber** | **String** | The tax identification number of the legal arrangement. | [optional] 
**type** | **String** | The [type of legal arrangement](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/legal-arrangements#types-of-legal-arrangements).  Possible values:  - **Association**   - **Partnership**   - **SoleProprietorship**   - **Trust**    | 



## Enum: LegalFormEnum


* `CashManagementTrust` (value: `"CashManagementTrust"`)

* `CorporateUnitTrust` (value: `"CorporateUnitTrust"`)

* `DeceasedEstate` (value: `"DeceasedEstate"`)

* `DiscretionaryInvestmentTrust` (value: `"DiscretionaryInvestmentTrust"`)

* `DiscretionaryServicesManagementTrust` (value: `"DiscretionaryServicesManagementTrust"`)

* `DiscretionaryTradingTrust` (value: `"DiscretionaryTradingTrust"`)

* `FirstHomeSaverAccountsTrust` (value: `"FirstHomeSaverAccountsTrust"`)

* `FixedTrust` (value: `"FixedTrust"`)

* `FixedUnitTrust` (value: `"FixedUnitTrust"`)

* `HybridTrust` (value: `"HybridTrust"`)

* `ListedPublicUnitTrust` (value: `"ListedPublicUnitTrust"`)

* `OtherTrust` (value: `"OtherTrust"`)

* `PooledSuperannuationTrust` (value: `"PooledSuperannuationTrust"`)

* `PublicTradingTrust` (value: `"PublicTradingTrust"`)

* `UnlistedPublicUnitTrust` (value: `"UnlistedPublicUnitTrust"`)

* `LimitedPartnership` (value: `"LimitedPartnership"`)

* `FamilyPartnership` (value: `"FamilyPartnership"`)

* `OtherPartnership` (value: `"OtherPartnership"`)





## Enum: TypeEnum


* `Association` (value: `"Association"`)

* `Partnership` (value: `"Partnership"`)

* `SoleProprietorship` (value: `"SoleProprietorship"`)

* `Trust` (value: `"Trust"`)




