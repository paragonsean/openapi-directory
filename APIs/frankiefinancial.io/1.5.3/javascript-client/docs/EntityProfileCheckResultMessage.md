# FrankieFinancialApi.EntityProfileCheckResultMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkClass** | **String** | The class of checks to which this check type belongs. One of: - kyc - aml - fraud - none  | [optional] 
**checkType** | **String** | A single check type that this result message applies to. | [optional] 
**code** | **String** | Alphanumeric code that is unique for each failure message to simplify result processing and display. Values to be decided.  | [optional] 
**message** | **String** | Short description of why not passed | [optional] 
**result** | **String** | The current state of the check. One of: - PASS - FAIL - UNCHECKED: Not attempted or service not available. For example AML not attempted if KYC fails. - NA: Not required. For example Visa check when there is no visa document and your account configuration indicates the check can be skipped.  | [optional] 


