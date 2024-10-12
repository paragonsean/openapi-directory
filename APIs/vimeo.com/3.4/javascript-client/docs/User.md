# Vimeo.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **String** | The user&#39;s account type:  Option descriptions:  * &#x60;basic&#x60; - The user has a Vimeo Basic subscription.  * &#x60;business&#x60; - The user has a Vimeo Business subscription.  * &#x60;live_business&#x60; - The user has a Vimeo Business Live subscription.  * &#x60;live_premium&#x60; - The user has a Vimeo Premium subscription.  * &#x60;live_pro&#x60; - The user has a Vimeo PRO Live subscription.  * &#x60;plus&#x60; - The user has a Vimeo Plus subscription.  * &#x60;pro&#x60; - The user has a Vimeo Pro subscription.  * &#x60;pro_unlimited&#x60; - The user has a Vimeo PRO Unlimited subscription.  * &#x60;producer&#x60; - The user has a Vimeo Producer subscription.  | 
**bio** | **String** | The user&#39;s bio. | 
**contentFilter** | **[String]** | The user&#39;s content filters:  Option descriptions:  * &#x60;drugs&#x60; - Drugs or alcohol use.  * &#x60;language&#x60; - Profanity or sexually suggestive content.  * &#x60;nudity&#x60; - Nudity.  * &#x60;safe&#x60; - Suitable for all audiences.  * &#x60;unrated&#x60; - No rating.  * &#x60;violence&#x60; - Violent or graphic content.  | [optional] 
**createdTime** | **String** | The time in ISO 8601 format when the user account was created. | 
**email** | **String** | The user&#39;s email address. This data requires a bearer token with the &#x60;email&#x60; scope. | [optional] 
**link** | **String** | The absolute URL of this user&#39;s profile page. | 
**location** | **String** | The user&#39;s location. | 
**metadata** | [**UserMetadata**](UserMetadata.md) |  | 
**name** | **String** | The user&#39;s display name. | 
**pictures** | [**Picture**](Picture.md) | The active portrait of this user. | 
**preferences** | [**UserPreferences**](UserPreferences.md) |  | [optional] 
**resourceKey** | **String** | The user&#39;s resource key string. | 
**uploadQuota** | [**UserUploadQuota**](UserUploadQuota.md) |  | 
**uri** | **String** | The user&#39;s canonical relative URI. | 
**websites** | [**[UserWebsitesInner]**](UserWebsitesInner.md) | The user&#39;s websites. | 



## Enum: AccountEnum


* `basic` (value: `"basic"`)

* `business` (value: `"business"`)

* `live_business` (value: `"live_business"`)

* `live_premium` (value: `"live_premium"`)

* `live_pro` (value: `"live_pro"`)

* `plus` (value: `"plus"`)

* `pro` (value: `"pro"`)

* `pro_unlimited` (value: `"pro_unlimited"`)

* `producer` (value: `"producer"`)





## Enum: ContentFilterEnum





