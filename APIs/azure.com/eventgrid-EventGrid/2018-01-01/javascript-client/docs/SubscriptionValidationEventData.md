# EventGridClient.SubscriptionValidationEventData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validationCode** | **String** | The validation code sent by Azure Event Grid to validate an event subscription. To complete the validation handshake, the subscriber must either respond with this validation code as part of the validation response, or perform a GET request on the validationUrl (available starting version 2018-05-01-preview). | [optional] [readonly] 
**validationUrl** | **String** | The validation URL sent by Azure Event Grid (available starting version 2018-05-01-preview). To complete the validation handshake, the subscriber must either respond with the validationCode as part of the validation response, or perform a GET request on the validationUrl (available starting version 2018-05-01-preview). | [optional] [readonly] 


