# SalesLoftPlatform.Email

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**bounced** | **Boolean** | Whether this email bounced | [optional] 
**cadence** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**clickTracking** | **Boolean** | Whether this email had click tracking enabled | [optional] 
**counts** | [**EmailCounts**](EmailCounts.md) |  | [optional] 
**createdAt** | **Date** | Datetime of when the email was created | [optional] 
**crmActivity** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**emailTemplate** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**errorMessage** | **String** | Error message of the email. This field has been determined sensitive and requires a specific scope to access it. | [optional] 
**headers** | **Object** | Selected headers that are included if this email used them. Available keys are: cc, bcc | [optional] 
**id** | **Number** | ID of Email | [optional] 
**mailing** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**personalization** | **String** | Percentage of this email that has been personalized | [optional] 
**recipient** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**recipientEmailAddress** | **String** | Email address of the recipient | [optional] 
**sendAfter** | **Date** | When this email will be sent, or null if already sent | [optional] 
**sentAt** | **Date** | When this email was sent, or null if it was not sent | [optional] 
**status** | **String** | Status of this email through the sending process. Possible values are: sent, sent_from_gmail, sent_from_external, pending, pending_reply_check, scheduled, sending, delivering, failed, cancelled, pending_through_gmail, pending_through_external | [optional] 
**step** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**subject** | **String** | Subject of the email. This field has been determined sensitive and requires a specific scope to access it. | [optional] 
**task** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**updatedAt** | **Date** | Datetime of when the email was last updated | [optional] 
**user** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**viewTracking** | **Boolean** | Whether this email had view tracking enabled | [optional] 


