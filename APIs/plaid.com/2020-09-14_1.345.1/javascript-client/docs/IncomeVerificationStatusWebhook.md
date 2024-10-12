# ThePlaidApi.IncomeVerificationStatusWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**itemId** | **String** | The Item ID associated with the verification. | 
**userId** | **String** | The Plaid &#x60;user_id&#x60; of the User associated with this webhook, warning, or error. | [optional] 
**verificationStatus** | **String** | &#x60;VERIFICATION_STATUS_PROCESSING_COMPLETE&#x60;: The income verification status processing has completed. If the user uploaded multiple documents, this webhook will fire when all documents have finished processing. Call the &#x60;/income/verification/paystubs/get&#x60; endpoint and check the document metadata to see which documents were successfully parsed.  &#x60;VERIFICATION_STATUS_PROCESSING_FAILED&#x60;: A failure occurred when attempting to process the verification documentation.  &#x60;VERIFICATION_STATUS_PENDING_APPROVAL&#x60;: (deprecated) The income verification has been sent to the user for review. | 
**webhookCode** | **String** | &#x60;INCOME_VERIFICATION&#x60; | 
**webhookType** | **String** | &#x60;\&quot;INCOME\&quot;&#x60; | 


