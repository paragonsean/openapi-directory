

# VerificationError


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capabilities** | [**List&lt;CapabilitiesEnum&gt;**](#List&lt;CapabilitiesEnum&gt;) | Contains key-value pairs that specify the actions that the legal entity can do in your platform. The key is a capability required for your integration. For example, **issueCard** for Issuing.The value is an object containing the settings for the capability. |  [optional] |
|**code** | **String** | The general error code. |  [optional] |
|**message** | **String** | The general error message. |  [optional] |
|**remediatingActions** | [**List&lt;RemediatingAction&gt;**](RemediatingAction.md) | An object containing possible solutions to fix a verification error. |  [optional] |
|**subErrors** | [**List&lt;VerificationErrorRecursive&gt;**](VerificationErrorRecursive.md) | An array containing more granular information about the cause of the verification error. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of error. |  [optional] |



## Enum: List&lt;CapabilitiesEnum&gt;

| Name | Value |
|---- | -----|
| ACCEPT_EXTERNAL_FUNDING | &quot;acceptExternalFunding&quot; |
| ACCEPT_PSP_FUNDING | &quot;acceptPspFunding&quot; |
| ACCEPT_TRANSACTION_IN_RESTRICTED_COUNTRIES | &quot;acceptTransactionInRestrictedCountries&quot; |
| ACCEPT_TRANSACTION_IN_RESTRICTED_COUNTRIES_COMMERCIAL | &quot;acceptTransactionInRestrictedCountriesCommercial&quot; |
| ACCEPT_TRANSACTION_IN_RESTRICTED_COUNTRIES_CONSUMER | &quot;acceptTransactionInRestrictedCountriesConsumer&quot; |
| ACCEPT_TRANSACTION_IN_RESTRICTED_INDUSTRIES | &quot;acceptTransactionInRestrictedIndustries&quot; |
| ACCEPT_TRANSACTION_IN_RESTRICTED_INDUSTRIES_COMMERCIAL | &quot;acceptTransactionInRestrictedIndustriesCommercial&quot; |
| ACCEPT_TRANSACTION_IN_RESTRICTED_INDUSTRIES_CONSUMER | &quot;acceptTransactionInRestrictedIndustriesConsumer&quot; |
| ACQUIRING | &quot;acquiring&quot; |
| ATM_WITHDRAWAL | &quot;atmWithdrawal&quot; |
| ATM_WITHDRAWAL_COMMERCIAL | &quot;atmWithdrawalCommercial&quot; |
| ATM_WITHDRAWAL_CONSUMER | &quot;atmWithdrawalConsumer&quot; |
| ATM_WITHDRAWAL_IN_RESTRICTED_COUNTRIES | &quot;atmWithdrawalInRestrictedCountries&quot; |
| ATM_WITHDRAWAL_IN_RESTRICTED_COUNTRIES_COMMERCIAL | &quot;atmWithdrawalInRestrictedCountriesCommercial&quot; |
| ATM_WITHDRAWAL_IN_RESTRICTED_COUNTRIES_CONSUMER | &quot;atmWithdrawalInRestrictedCountriesConsumer&quot; |
| AUTHORISED_PAYMENT_INSTRUMENT_USER | &quot;authorisedPaymentInstrumentUser&quot; |
| GET_GRANT_OFFERS | &quot;getGrantOffers&quot; |
| ISSUE_BANK_ACCOUNT | &quot;issueBankAccount&quot; |
| ISSUE_CARD | &quot;issueCard&quot; |
| ISSUE_CARD_COMMERCIAL | &quot;issueCardCommercial&quot; |
| ISSUE_CARD_CONSUMER | &quot;issueCardConsumer&quot; |
| LOCAL_ACCEPTANCE | &quot;localAcceptance&quot; |
| PAYOUT | &quot;payout&quot; |
| PAYOUT_TO_TRANSFER_INSTRUMENT | &quot;payoutToTransferInstrument&quot; |
| PROCESSING | &quot;processing&quot; |
| RECEIVE_FROM_BALANCE_ACCOUNT | &quot;receiveFromBalanceAccount&quot; |
| RECEIVE_FROM_PLATFORM_PAYMENTS | &quot;receiveFromPlatformPayments&quot; |
| RECEIVE_FROM_THIRD_PARTY | &quot;receiveFromThirdParty&quot; |
| RECEIVE_FROM_TRANSFER_INSTRUMENT | &quot;receiveFromTransferInstrument&quot; |
| RECEIVE_GRANTS | &quot;receiveGrants&quot; |
| RECEIVE_PAYMENTS | &quot;receivePayments&quot; |
| SEND_TO_BALANCE_ACCOUNT | &quot;sendToBalanceAccount&quot; |
| SEND_TO_THIRD_PARTY | &quot;sendToThirdParty&quot; |
| SEND_TO_TRANSFER_INSTRUMENT | &quot;sendToTransferInstrument&quot; |
| THIRD_PARTY_FUNDING | &quot;thirdPartyFunding&quot; |
| USE_CARD | &quot;useCard&quot; |
| USE_CARD_COMMERCIAL | &quot;useCardCommercial&quot; |
| USE_CARD_CONSUMER | &quot;useCardConsumer&quot; |
| USE_CARD_IN_RESTRICTED_COUNTRIES | &quot;useCardInRestrictedCountries&quot; |
| USE_CARD_IN_RESTRICTED_COUNTRIES_COMMERCIAL | &quot;useCardInRestrictedCountriesCommercial&quot; |
| USE_CARD_IN_RESTRICTED_COUNTRIES_CONSUMER | &quot;useCardInRestrictedCountriesConsumer&quot; |
| USE_CARD_IN_RESTRICTED_INDUSTRIES | &quot;useCardInRestrictedIndustries&quot; |
| USE_CARD_IN_RESTRICTED_INDUSTRIES_COMMERCIAL | &quot;useCardInRestrictedIndustriesCommercial&quot; |
| USE_CARD_IN_RESTRICTED_INDUSTRIES_CONSUMER | &quot;useCardInRestrictedIndustriesConsumer&quot; |
| WITHDRAW_FROM_ATM | &quot;withdrawFromAtm&quot; |
| WITHDRAW_FROM_ATM_COMMERCIAL | &quot;withdrawFromAtmCommercial&quot; |
| WITHDRAW_FROM_ATM_CONSUMER | &quot;withdrawFromAtmConsumer&quot; |
| WITHDRAW_FROM_ATM_IN_RESTRICTED_COUNTRIES | &quot;withdrawFromAtmInRestrictedCountries&quot; |
| WITHDRAW_FROM_ATM_IN_RESTRICTED_COUNTRIES_COMMERCIAL | &quot;withdrawFromAtmInRestrictedCountriesCommercial&quot; |
| WITHDRAW_FROM_ATM_IN_RESTRICTED_COUNTRIES_CONSUMER | &quot;withdrawFromAtmInRestrictedCountriesConsumer&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DATA_MISSING | &quot;dataMissing&quot; |
| DATA_REVIEW | &quot;dataReview&quot; |
| INVALID_INPUT | &quot;invalidInput&quot; |
| PENDING_STATUS | &quot;pendingStatus&quot; |
| REJECTED | &quot;rejected&quot; |



