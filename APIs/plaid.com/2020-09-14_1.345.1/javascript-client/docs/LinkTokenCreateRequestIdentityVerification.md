# ThePlaidApi.LinkTokenCreateRequestIdentityVerification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent** | **Boolean** | A flag specifying whether the end user has already agreed to a privacy policy specifying that their data will be shared with Plaid for verification purposes.  If &#x60;gave_consent&#x60; is set to &#x60;true&#x60;, the &#x60;accept_tos&#x60; step will be marked as &#x60;skipped&#x60; and the end user&#39;s session will start at the next step requirement. | [optional] 
**gaveConsent** | **Boolean** | A flag specifying whether the end user has already agreed to a privacy policy specifying that their data will be shared with Plaid for verification purposes.  If &#x60;gave_consent&#x60; is set to &#x60;true&#x60;, the &#x60;accept_tos&#x60; step will be marked as &#x60;skipped&#x60; and the end user&#39;s session will start at the next step requirement. | [optional] [default to false]
**templateId** | **String** | ID of the associated Identity Verification template. | 


