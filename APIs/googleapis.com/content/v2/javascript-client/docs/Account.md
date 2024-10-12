# ContentApiForShopping.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adultContent** | **Boolean** | Indicates whether the merchant sells adult content. | [optional] 
**adwordsLinks** | [**[AccountAdwordsLink]**](AccountAdwordsLink.md) | List of linked AdWords accounts that are active or pending approval. To create a new link request, add a new link with status &#x60;active&#x60; to the list. It will remain in a &#x60;pending&#x60; state until approved or rejected either in the AdWords interface or through the AdWords API. To delete an active link, or to cancel a link request, remove it from the list. | [optional] 
**businessInformation** | [**AccountBusinessInformation**](AccountBusinessInformation.md) |  | [optional] 
**googleMyBusinessLink** | [**AccountGoogleMyBusinessLink**](AccountGoogleMyBusinessLink.md) |  | [optional] 
**id** | **String** | Required for update. Merchant Center account ID. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#account&#x60;\&quot; | [optional] 
**name** | **String** | Required. Display name for the account. | [optional] 
**reviewsUrl** | **String** | [DEPRECATED] This field is never returned and will be ignored if provided. | [optional] 
**sellerId** | **String** | Client-specific, locally-unique, internal ID for the child account. | [optional] 
**users** | [**[AccountUser]**](AccountUser.md) | Users with access to the account. Every account (except for subaccounts) must have at least one admin user. | [optional] 
**websiteUrl** | **String** | The merchant&#39;s website. | [optional] 
**youtubeChannelLinks** | [**[AccountYouTubeChannelLink]**](AccountYouTubeChannelLink.md) | List of linked YouTube channels that are active or pending approval. To create a new link request, add a new link with status &#x60;active&#x60; to the list. It will remain in a &#x60;pending&#x60; state until approved or rejected in the YT Creator Studio interface. To delete an active link, or to cancel a link request, remove it from the list. | [optional] 


