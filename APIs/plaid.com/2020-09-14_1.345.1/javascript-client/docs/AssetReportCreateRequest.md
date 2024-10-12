# ThePlaidApi.AssetReportCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTokens** | **[String]** | An array of access tokens corresponding to the Items that will be included in the report. The &#x60;assets&#x60; product must have been initialized for the Items during link; the Assets product cannot be added after initialization. | [optional] 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**daysRequested** | **Number** | The maximum integer number of days of history to include in the Asset Report. If using Fannie Mae Day 1 Certainty, &#x60;days_requested&#x60; must be at least 61 for new originations or at least 31 for refinancings.  An Asset Report requested with \&quot;Additional History\&quot; (that is, with more than 61 days of transaction history) will incur an Additional History fee. | 
**options** | [**AssetReportCreateRequestOptions**](AssetReportCreateRequestOptions.md) |  | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**userToken** | **String** | The user token associated with the User for which to create an asset report for. All items associated with the User will be included in the report. | [optional] 


