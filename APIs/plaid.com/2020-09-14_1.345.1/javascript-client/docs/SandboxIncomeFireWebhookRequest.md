# ThePlaidApi.SandboxIncomeFireWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**itemId** | **String** | The Item ID associated with the verification. | 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**userId** | **String** | The Plaid &#x60;user_id&#x60; of the User associated with this webhook, warning, or error. | [optional] 
**verificationStatus** | **String** | &#x60;VERIFICATION_STATUS_PROCESSING_COMPLETE&#x60;: The income verification status processing has completed. If the user uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the &#x60;/income/verification/paystubs/get&#x60; endpoint and check the document metadata to see which documents were successfully parsed.  &#x60;VERIFICATION_STATUS_PROCESSING_FAILED&#x60;: A failure occurred when attempting to process the verification documentation.  &#x60;VERIFICATION_STATUS_PENDING_APPROVAL&#x60;: (deprecated) The income verification has been sent to the user for review. | 
**webhook** | **String** | The URL to which the webhook should be sent. | 



## Enum: VerificationStatusEnum


* `PROCESSING_COMPLETE` (value: `"VERIFICATION_STATUS_PROCESSING_COMPLETE"`)

* `PROCESSING_FAILED` (value: `"VERIFICATION_STATUS_PROCESSING_FAILED"`)

* `PENDING_APPROVAL` (value: `"VERIFICATION_STATUS_PENDING_APPROVAL"`)




