# ConfigurationWebhooks.VerificationErrorRecursive

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **[String]** | Contains the capabilities that the verification error applies to. | [optional] 
**code** | **String** | The verification error code. | [optional] 
**message** | **String** | A description of the error. | [optional] 
**remediatingActions** | [**[RemediatingAction]**](RemediatingAction.md) | Contains the actions that you can take to resolve the verification error. | [optional] 
**type** | **String** | The type of error.   Possible values: **invalidInput**, **dataMissing**. | [optional] 



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

* `invalidInput` (value: `"invalidInput"`)

* `pendingStatus` (value: `"pendingStatus"`)




