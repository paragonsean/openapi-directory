# PlatformApi.Recipient

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Client ID of recipient | [optional] 
**deviceId** | **String** | Client ID of recipient | [optional] 
**deviceToken** | **String** | when using APNs, specifies the required device token. | [optional] 
**registrationToken** | **String** | when using GCM or FCM, specifies the required registration token. | [optional] 
**transportType** | **String** | Defines which push platform is being used. | [optional] 



## Enum: TransportTypeEnum


* `apns` (value: `"apns"`)

* `fcm` (value: `"fcm"`)

* `gcm` (value: `"gcm"`)




