

# PublisherProfileMobileApplication

A mobile application that contains a external app ID, name, and app store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appStore** | [**AppStoreEnum**](#AppStoreEnum) | The app store the app belongs to. Can be used to filter the response of the publisherProfiles.list method. |  [optional] |
|**externalAppId** | **String** | The external ID for the app from its app store. Can be used to filter the response of the publisherProfiles.list method. |  [optional] |
|**name** | **String** | The name of the app. |  [optional] |



## Enum: AppStoreEnum

| Name | Value |
|---- | -----|
| APP_STORE_TYPE_UNSPECIFIED | &quot;APP_STORE_TYPE_UNSPECIFIED&quot; |
| APPLE_ITUNES | &quot;APPLE_ITUNES&quot; |
| GOOGLE_PLAY | &quot;GOOGLE_PLAY&quot; |
| ROKU | &quot;ROKU&quot; |
| AMAZON_FIRE_TV | &quot;AMAZON_FIRE_TV&quot; |
| PLAYSTATION | &quot;PLAYSTATION&quot; |
| XBOX | &quot;XBOX&quot; |
| SAMSUNG_TV | &quot;SAMSUNG_TV&quot; |
| AMAZON | &quot;AMAZON&quot; |
| OPPO | &quot;OPPO&quot; |
| SAMSUNG | &quot;SAMSUNG&quot; |
| VIVO | &quot;VIVO&quot; |
| XIAOMI | &quot;XIAOMI&quot; |
| LG_TV | &quot;LG_TV&quot; |



