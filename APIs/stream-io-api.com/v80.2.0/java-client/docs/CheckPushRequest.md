

# CheckPushRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apnTemplate** | **String** | Push message template for APN |  [optional] |
|**firebaseDataTemplate** | **String** | Push message data template for Firebase |  [optional] |
|**firebaseTemplate** | **String** | Push message template for Firebase |  [optional] |
|**messageId** | **String** | Message ID to send push notification for |  [optional] |
|**pushProviderName** | **String** | Name of push provider |  [optional] |
|**pushProviderType** | [**PushProviderTypeEnum**](#PushProviderTypeEnum) | Push provider type |  [optional] |
|**skipDevices** | **Boolean** | Don&#39;t require existing devices to render templates |  [optional] |
|**user** | **UserObjectRequest** |  |  [optional] |
|**userId** | **String** |  |  [optional] |



## Enum: PushProviderTypeEnum

| Name | Value |
|---- | -----|
| FIREBASE | &quot;firebase&quot; |
| APN | &quot;apn&quot; |
| HUAWEI | &quot;huawei&quot; |
| XIAOMI | &quot;xiaomi&quot; |



