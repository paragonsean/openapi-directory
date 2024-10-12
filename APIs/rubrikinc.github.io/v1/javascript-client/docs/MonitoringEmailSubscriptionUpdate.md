# RubrikRestApi.MonitoringEmailSubscriptionUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**[SubscriptionAttachmentType]**](SubscriptionAttachmentType.md) | Attachment files to send with the subscription. | 
**emailAddresses** | **[String]** | Email addresses to send monitoring subscriptions to. | 
**jobStates** | [**[JobMonitoringState]**](JobMonitoringState.md) | User-selected job states. | 
**timeAttributes** | [**SubscriptionScheduleTimeAttributes**](SubscriptionScheduleTimeAttributes.md) |  | 
**assumeOwnership** | **Boolean** | Changes the owner of an email subscription object to the username of the account that is logged into the current session. | [optional] 
**id** | **String** | ID assigned to an email subscription object. | 


