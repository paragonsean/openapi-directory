# LegalEntityManagementApi.VerificationErrorRecursive

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **[String]** | Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing the settings for the capability. | [optional] 
**code** | **String** | The general error code. | [optional] 
**message** | **String** | The general error message. | [optional] 
**remediatingActions** | [**[RemediatingAction]**](RemediatingAction.md) | An object containing possible solutions to fix a verification error. | [optional] 
**type** | **String** | The type of error. | [optional] 



## Enum: [CapabilitiesEnum]


* `acceptExternalFunding` (value: `"acceptExternalFunding"`)

* `acceptPspFunding` (value: `"acceptPspFunding"`)

* `acceptTransactionInRestrictedCountries` (value: `"acceptTransactionInRestrictedCountries"`)

* `acceptTransactionInRestrictedCountriesCommercial` (value: `"acceptTransactionInRestrictedCountriesCommercial"`)

* `acceptTransactionInRestrictedCountriesConsumer` (value: `"acceptTransactionInRestrictedCountriesConsumer"`)

* `acceptTransactionInRestrictedIndustries` (value: `"acceptTransactionInRestrictedIndustries"`)

* `acceptTransactionInRestrictedIndustriesCommercial` (value: `"acceptTransactionInRestrictedIndustriesCommercial"`)

* `acceptTransactionInRestrictedIndustriesConsumer` (value: `"acceptTransactionInRestrictedIndustriesConsumer"`)

* `acquiring` (value: `"acquiring"`)

* `atmWithdrawal` (value: `"atmWithdrawal"`)

* `atmWithdrawalCommercial` (value: `"atmWithdrawalCommercial"`)

* `atmWithdrawalConsumer` (value: `"atmWithdrawalConsumer"`)

* `atmWithdrawalInRestrictedCountries` (value: `"atmWithdrawalInRestrictedCountries"`)

* `atmWithdrawalInRestrictedCountriesCommercial` (value: `"atmWithdrawalInRestrictedCountriesCommercial"`)

* `atmWithdrawalInRestrictedCountriesConsumer` (value: `"atmWithdrawalInRestrictedCountriesConsumer"`)

* `authorisedPaymentInstrumentUser` (value: `"authorisedPaymentInstrumentUser"`)

* `getGrantOffers` (value: `"getGrantOffers"`)

* `issueBankAccount` (value: `"issueBankAccount"`)

* `issueCard` (value: `"issueCard"`)

* `issueCardCommercial` (value: `"issueCardCommercial"`)

* `issueCardConsumer` (value: `"issueCardConsumer"`)

* `localAcceptance` (value: `"localAcceptance"`)

* `payout` (value: `"payout"`)

* `payoutToTransferInstrument` (value: `"payoutToTransferInstrument"`)

* `processing` (value: `"processing"`)

* `receiveFromBalanceAccount` (value: `"receiveFromBalanceAccount"`)

* `receiveFromPlatformPayments` (value: `"receiveFromPlatformPayments"`)

* `receiveFromThirdParty` (value: `"receiveFromThirdParty"`)

* `receiveFromTransferInstrument` (value: `"receiveFromTransferInstrument"`)

* `receiveGrants` (value: `"receiveGrants"`)

* `receivePayments` (value: `"receivePayments"`)

* `sendToBalanceAccount` (value: `"sendToBalanceAccount"`)

* `sendToThirdParty` (value: `"sendToThirdParty"`)

* `sendToTransferInstrument` (value: `"sendToTransferInstrument"`)

* `thirdPartyFunding` (value: `"thirdPartyFunding"`)

* `useCard` (value: `"useCard"`)

* `useCardCommercial` (value: `"useCardCommercial"`)

* `useCardConsumer` (value: `"useCardConsumer"`)

* `useCardInRestrictedCountries` (value: `"useCardInRestrictedCountries"`)

* `useCardInRestrictedCountriesCommercial` (value: `"useCardInRestrictedCountriesCommercial"`)

* `useCardInRestrictedCountriesConsumer` (value: `"useCardInRestrictedCountriesConsumer"`)

* `useCardInRestrictedIndustries` (value: `"useCardInRestrictedIndustries"`)

* `useCardInRestrictedIndustriesCommercial` (value: `"useCardInRestrictedIndustriesCommercial"`)

* `useCardInRestrictedIndustriesConsumer` (value: `"useCardInRestrictedIndustriesConsumer"`)

* `withdrawFromAtm` (value: `"withdrawFromAtm"`)

* `withdrawFromAtmCommercial` (value: `"withdrawFromAtmCommercial"`)

* `withdrawFromAtmConsumer` (value: `"withdrawFromAtmConsumer"`)

* `withdrawFromAtmInRestrictedCountries` (value: `"withdrawFromAtmInRestrictedCountries"`)

* `withdrawFromAtmInRestrictedCountriesCommercial` (value: `"withdrawFromAtmInRestrictedCountriesCommercial"`)

* `withdrawFromAtmInRestrictedCountriesConsumer` (value: `"withdrawFromAtmInRestrictedCountriesConsumer"`)





## Enum: TypeEnum


* `dataMissing` (value: `"dataMissing"`)

* `dataReview` (value: `"dataReview"`)

* `invalidInput` (value: `"invalidInput"`)

* `pendingStatus` (value: `"pendingStatus"`)

* `rejected` (value: `"rejected"`)




