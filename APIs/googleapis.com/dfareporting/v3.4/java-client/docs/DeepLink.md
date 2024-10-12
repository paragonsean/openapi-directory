

# DeepLink

Contains information about a landing page deep link.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appUrl** | **String** | The URL of the mobile app being linked to. |  [optional] |
|**fallbackUrl** | **String** | The fallback URL. This URL will be served to users who do not have the mobile app installed. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#deepLink\&quot;. |  [optional] |
|**mobileApp** | [**MobileApp**](MobileApp.md) |  |  [optional] |
|**remarketingListIds** | **List&lt;String&gt;** | Ads served to users on these remarketing lists will use this deep link. Applicable when mobileApp.directory is APPLE_APP_STORE. |  [optional] |



