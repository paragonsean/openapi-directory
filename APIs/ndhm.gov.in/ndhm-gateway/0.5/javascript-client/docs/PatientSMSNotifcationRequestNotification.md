# Gateway.PatientSMSNotifcationRequestNotification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**careContextInfo** | **String** | Information about care context or visit for which the SMS is being sent. | 
**deeplinkUrl** | **String** | A link pointing to digital health records of the patient. PHR App&#39;s deeplink will be sent in SMS if this field is not provided. | [optional] 
**hip** | [**PatientSMSNotifcationRequestNotificationHip**](PatientSMSNotifcationRequestNotificationHip.md) |  | 
**phoneNo** | **String** | Phone number of the receiver with country code | 
**receiverName** | **String** | Name of the reciever/patient. Receiver&#39;s name will not be sent if not provided. | [optional] 


