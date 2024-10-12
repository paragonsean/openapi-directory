# YouTubeDataApiV3.ActivityContentDetailsPromotedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adTag** | **String** | The URL the client should fetch to request a promoted item. | [optional] 
**clickTrackingUrl** | **String** | The URL the client should ping to indicate that the user clicked through on this promoted item. | [optional] 
**creativeViewUrl** | **String** | The URL the client should ping to indicate that the user was shown this promoted item. | [optional] 
**ctaType** | **String** | The type of call-to-action, a message to the user indicating action that can be taken. | [optional] 
**customCtaButtonText** | **String** | The custom call-to-action button text. If specified, it will override the default button text for the cta_type. | [optional] 
**descriptionText** | **String** | The text description to accompany the promoted item. | [optional] 
**destinationUrl** | **String** | The URL the client should direct the user to, if the user chooses to visit the advertiser&#39;s website. | [optional] 
**forecastingUrl** | **[String]** | The list of forecasting URLs. The client should ping all of these URLs when a promoted item is not available, to indicate that a promoted item could have been shown. | [optional] 
**impressionUrl** | **[String]** | The list of impression URLs. The client should ping all of these URLs to indicate that the user was shown this promoted item. | [optional] 
**videoId** | **String** | The ID that YouTube uses to uniquely identify the promoted video. | [optional] 



## Enum: CtaTypeEnum


* `ctaTypeUnspecified` (value: `"ctaTypeUnspecified"`)

* `visitAdvertiserSite` (value: `"visitAdvertiserSite"`)




