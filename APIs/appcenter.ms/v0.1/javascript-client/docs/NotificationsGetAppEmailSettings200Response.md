# AppCenterClient.NotificationsGetAppEmailSettings200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestId** | **String** | Unique request | 
**eTag** | **String** | The ETag of the entity | [optional] 
**enabled** | **Boolean** | Allows to forcefully disable emails on app or user level | 
**settings** | [**[NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner]**](NotificationsGetAppEmailSettings200ResponseAllOfAllOfSettingsInner.md) | The settings the user has for the app | 
**userId** | **String** | The unique id (UUID) of the user | [optional] 
**appId** | **String** | Application ID | [optional] 
**userEnabled** | **Boolean** | A flag indicating if settings are enabled at user/global level | 


