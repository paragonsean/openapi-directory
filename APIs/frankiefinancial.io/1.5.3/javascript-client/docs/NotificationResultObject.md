# FrankieFinancialApi.NotificationResultObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkId** | **String** | If you&#39;re calling a processing function of some kind, a check number will be issued. This field will only be present if the function you&#39;re calling would normally return a checkId (such as scan, verify, and compare).  | [optional] 
**documentId** | **String** | Only supplied if the original request was tied to a document. This will be the same ID that was sent in the original acceptance.  | [optional] 
**entityCustomerReference** | **String** | If the entity in entityId above has had an external service ID attached to it in the entity extraData with kvpKey &#x3D; customer_reference, then this is that kvpValue  | [optional] 
**entityId** | **String** | Only supplied if the original request was tied to an entity. This will be the same ID that was sent in the original acceptance.  | [optional] 
**_function** | **String** | Short description of the original function called, or function that was triggered.  | [optional] 
**functionResult** | [**EnumFunctionStatus**](EnumFunctionStatus.md) |  | [optional] 
**linkReference** | **String** | URI for resource containing more details about the reason for the notification.  | [optional] 
**message** | **String** | A brief, human readable message describing the reason for the notification.  | [optional] 
**notificationType** | [**EnumNotificationType**](EnumNotificationType.md) |  | [optional] 
**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  | [optional] 
**username** | **String** | The portal username that initiated the operation that led to this notification. If applicable and available.  | [optional] 


