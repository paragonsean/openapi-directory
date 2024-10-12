# StreamChatApi.CheckPushRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apnTemplate** | **String** | Push message template for APN | [optional] 
**firebaseDataTemplate** | **String** | Push message data template for Firebase | [optional] 
**firebaseTemplate** | **String** | Push message template for Firebase | [optional] 
**messageId** | **String** | Message ID to send push notification for | [optional] 
**pushProviderName** | **String** | Name of push provider | [optional] 
**pushProviderType** | **String** | Push provider type | [optional] 
**skipDevices** | **Boolean** | Don&#39;t require existing devices to render templates | [optional] 
**user** | [**UserObjectRequest**](UserObjectRequest.md) |  | [optional] 
**userId** | **String** |  | [optional] 



## Enum: PushProviderTypeEnum


* `firebase` (value: `"firebase"`)

* `apn` (value: `"apn"`)

* `huawei` (value: `"huawei"`)

* `xiaomi` (value: `"xiaomi"`)




