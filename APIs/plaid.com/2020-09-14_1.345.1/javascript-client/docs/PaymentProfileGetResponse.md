# ThePlaidApi.PaymentProfileGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the time the given Payment Profile was created at | 
**deletedAt** | **Date** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the time the given Payment Profile was deleted at. Always &#x60;null&#x60; if the Payment Profile has not been deleted | 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**status** | [**PaymentProfileStatus**](PaymentProfileStatus.md) |  | 
**updatedAt** | **Date** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the last time the given Payment Profile was updated at | 


