# RocketServices.ProfileSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **String** | Hex color value assigned to the profile. | [optional] 
**heroAutoplay** | **Boolean** | Gets the Hero row clip auto playback enabled | [optional] 
**heroWithAudio** | **Boolean** | Gets the Hero row clip auto playback audio enabled | [optional] 
**id** | **String** | The id of the profile. | 
**isActive** | **Boolean** | Whether the profile is active or not.  **DEPRECATED** - Always true. Inactive profiles are no longer returned.  | 
**languageCode** | **String** | The code of the preferred language for the profile. Must be a valid ISO language code e.g. \&quot;en-US\&quot; and must match the code of one of the languages specified in the app config. See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 
**marketingEnabled** | **Boolean** | Whether the profile has opted in or out of marketing material.  **DEPRECATED** - Marketing material is no longer tied to profiles, only account. See &#x60;Account.marketingEnabled&#x60;.  | 
**maxRatingContentFilter** | [**ClassificationSummary**](ClassificationSummary.md) |  | [optional] 
**minRatingPlaybackGuard** | [**ClassificationSummary**](ClassificationSummary.md) |  | [optional] 
**name** | **String** | The unique name of the profile. | 
**pinEnabled** | **Boolean** | Whether a pin is required to enter the profile. | 
**purchaseEnabled** | **Boolean** | Whether the profile can make purchases with the account payment options. | 
**segments** | **[String]** | The segments a profile has been placed under | 


