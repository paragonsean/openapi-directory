# RecommendationsAiBeta.GoogleCloudRecommendationengineV1beta1EventDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventAttributes** | [**GoogleCloudRecommendationengineV1beta1FeatureMap**](GoogleCloudRecommendationengineV1beta1FeatureMap.md) |  | [optional] 
**experimentIds** | **[String]** | Optional. A list of identifiers for the independent experiment groups this user event belongs to. This is used to distinguish between user events associated with different experiment setups (e.g. using Recommendation Engine system, using different recommendation models). | [optional] 
**pageViewId** | **String** | Optional. A unique id of a web page view. This should be kept the same for all user events triggered from the same pageview. For example, an item detail page view could trigger multiple events as the user is browsing the page. The &#x60;pageViewId&#x60; property should be kept the same for all these events so that they can be grouped together properly. This &#x60;pageViewId&#x60; will be automatically generated if using the JavaScript pixel. | [optional] 
**recommendationToken** | **String** | Optional. Recommendation token included in the recommendation prediction response. This field enables accurate attribution of recommendation model performance. This token enables us to accurately attribute page view or purchase back to the event and the particular predict response containing this clicked/purchased item. If user clicks on product K in the recommendation results, pass the &#x60;PredictResponse.recommendationToken&#x60; property as a url parameter to product K&#39;s page. When recording events on product K&#39;s page, log the PredictResponse.recommendation_token to this field. Optional, but highly encouraged for user events that are the result of a recommendation prediction query. | [optional] 
**referrerUri** | **String** | Optional. The referrer url of the current page. When using the JavaScript pixel, this value is filled in automatically. | [optional] 
**uri** | **String** | Optional. Complete url (window.location.href) of the user&#39;s current page. When using the JavaScript pixel, this value is filled in automatically. Maximum length 5KB. | [optional] 


