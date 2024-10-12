# ThePlaidApi.DepositSwitchCreateRequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactionItemAccessTokens** | **[String]** | An array of access tokens corresponding to transaction items to use when attempting to match the user to their Payroll Provider. These tokens must be created by the same client id as the one creating the switch, and have access to the transactions product. | [optional] 
**webhook** | **String** | The URL registered to receive webhooks when the status of a deposit switch request has changed.  | [optional] 


