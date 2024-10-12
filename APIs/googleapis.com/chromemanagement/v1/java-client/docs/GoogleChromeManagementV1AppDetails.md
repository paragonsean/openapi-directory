

# GoogleChromeManagementV1AppDetails

Resource representing app details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**androidAppInfo** | [**GoogleChromeManagementV1AndroidAppInfo**](GoogleChromeManagementV1AndroidAppInfo.md) |  |  [optional] |
|**appId** | **String** | Output only. Unique store identifier for the item. Examples: \&quot;gmbmikajjgmnabiglmofipeabaddhgne\&quot; for the Save to Google Drive Chrome extension, \&quot;com.google.android.apps.docs\&quot; for the Google Drive Android app. |  [optional] [readonly] |
|**chromeAppInfo** | [**GoogleChromeManagementV1ChromeAppInfo**](GoogleChromeManagementV1ChromeAppInfo.md) |  |  [optional] |
|**description** | **String** | Output only. App&#39;s description. |  [optional] [readonly] |
|**detailUri** | **String** | Output only. The uri for the detail page of the item. |  [optional] [readonly] |
|**displayName** | **String** | Output only. App&#39;s display name. |  [optional] [readonly] |
|**firstPublishTime** | **String** | Output only. First published time. |  [optional] [readonly] |
|**homepageUri** | **String** | Output only. Home page or Website uri. |  [optional] [readonly] |
|**iconUri** | **String** | Output only. A link to an image that can be used as an icon for the product. |  [optional] [readonly] |
|**isPaidApp** | **Boolean** | Output only. Indicates if the app has to be paid for OR has paid content. |  [optional] [readonly] |
|**latestPublishTime** | **String** | Output only. Latest published time. |  [optional] [readonly] |
|**name** | **String** | Output only. Format: name&#x3D;customers/{customer_id}/apps/{chrome|android|web}/{app_id}@{version} |  [optional] [readonly] |
|**privacyPolicyUri** | **String** | Output only. The URI pointing to the privacy policy of the app, if it was provided by the developer. Version-specific field that will only be set when the requested app version is found. |  [optional] [readonly] |
|**publisher** | **String** | Output only. The publisher of the item. |  [optional] [readonly] |
|**reviewNumber** | **String** | Output only. Number of reviews received. Chrome Web Store review information will always be for the latest version of an app. |  [optional] [readonly] |
|**reviewRating** | **Float** | Output only. The rating of the app (on 5 stars). Chrome Web Store review information will always be for the latest version of an app. |  [optional] [readonly] |
|**revisionId** | **String** | Output only. App version. A new revision is committed whenever a new version of the app is published. |  [optional] [readonly] |
|**serviceError** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. App type. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| APP_ITEM_TYPE_UNSPECIFIED | &quot;APP_ITEM_TYPE_UNSPECIFIED&quot; |
| CHROME | &quot;CHROME&quot; |
| ANDROID | &quot;ANDROID&quot; |
| WEB | &quot;WEB&quot; |



