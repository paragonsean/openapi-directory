

# AppAssignedTargetingOptionDetails

Details for assigned app targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_APP`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | Required. The ID of the app. Android&#39;s Play store app uses bundle ID, for example &#x60;com.google.android.gm&#x60;. Apple&#39;s App store app ID uses 9 digit string, for example &#x60;422689480&#x60;. |  [optional] |
|**appPlatform** | [**AppPlatformEnum**](#AppPlatformEnum) | Indicates the platform of the targeted app. If this field is not specified, the app platform will be assumed to be mobile (i.e., Android or iOS), and we will derive the appropriate mobile platform from the app ID. |  [optional] |
|**displayName** | **String** | Output only. The display name of the app. |  [optional] [readonly] |
|**negative** | **Boolean** | Indicates if this option is being negatively targeted. |  [optional] |



## Enum: AppPlatformEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;APP_PLATFORM_UNSPECIFIED&quot; |
| IOS | &quot;APP_PLATFORM_IOS&quot; |
| ANDROID | &quot;APP_PLATFORM_ANDROID&quot; |
| ROKU | &quot;APP_PLATFORM_ROKU&quot; |
| AMAZON_FIRETV | &quot;APP_PLATFORM_AMAZON_FIRETV&quot; |
| PLAYSTATION | &quot;APP_PLATFORM_PLAYSTATION&quot; |
| APPLE_TV | &quot;APP_PLATFORM_APPLE_TV&quot; |
| XBOX | &quot;APP_PLATFORM_XBOX&quot; |
| SAMSUNG_TV | &quot;APP_PLATFORM_SAMSUNG_TV&quot; |
| ANDROID_TV | &quot;APP_PLATFORM_ANDROID_TV&quot; |
| GENERIC_CTV | &quot;APP_PLATFORM_GENERIC_CTV&quot; |



