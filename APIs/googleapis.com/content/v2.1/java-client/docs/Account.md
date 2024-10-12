

# Account

Account data. After the creation of a new account it may take a few minutes before it's fully operational. The methods delete, insert, and update require the admin role.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountManagement** | **String** | Output only. How the account is managed. Acceptable values are: - \&quot;&#x60;manual&#x60;\&quot; - \&quot;&#x60;automatic&#x60;\&quot;  |  [optional] [readonly] |
|**adsLinks** | [**List&lt;AccountAdsLink&gt;**](AccountAdsLink.md) | Linked Ads accounts that are active or pending approval. To create a new link request, add a new link with status &#x60;active&#x60; to the list. It will remain in a &#x60;pending&#x60; state until approved or rejected either in the Ads interface or through the Google Ads API. To delete an active link, or to cancel a link request, remove it from the list. |  [optional] |
|**adultContent** | **Boolean** | Indicates whether the merchant sells adult content. |  [optional] |
|**automaticImprovements** | [**AccountAutomaticImprovements**](AccountAutomaticImprovements.md) |  |  [optional] |
|**automaticLabelIds** | **List&lt;String&gt;** | Automatically created label IDs that are assigned to the account by CSS Center. |  [optional] |
|**businessIdentity** | [**AccountBusinessIdentity**](AccountBusinessIdentity.md) |  |  [optional] |
|**businessInformation** | [**AccountBusinessInformation**](AccountBusinessInformation.md) |  |  [optional] |
|**conversionSettings** | [**AccountConversionSettings**](AccountConversionSettings.md) |  |  [optional] |
|**cssId** | **String** | ID of CSS the account belongs to. |  [optional] |
|**googleMyBusinessLink** | [**AccountGoogleMyBusinessLink**](AccountGoogleMyBusinessLink.md) |  |  [optional] |
|**id** | **String** | Required. 64-bit Merchant Center account ID. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#account&#x60;\&quot;. |  [optional] |
|**labelIds** | **List&lt;String&gt;** | Manually created label IDs that are assigned to the account by CSS. |  [optional] |
|**name** | **String** | Required. Display name for the account. |  [optional] |
|**sellerId** | **String** | Client-specific, locally-unique, internal ID for the child account. |  [optional] |
|**users** | [**List&lt;AccountUser&gt;**](AccountUser.md) | Users with access to the account. Every account (except for subaccounts) must have at least one admin user. |  [optional] |
|**websiteUrl** | **String** | The merchant&#39;s website. |  [optional] |
|**youtubeChannelLinks** | [**List&lt;AccountYouTubeChannelLink&gt;**](AccountYouTubeChannelLink.md) | Linked YouTube channels that are active or pending approval. To create a new link request, add a new link with status &#x60;active&#x60; to the list. It will remain in a &#x60;pending&#x60; state until approved or rejected in the YT Creator Studio interface. To delete an active link, or to cancel a link request, remove it from the list. |  [optional] |



