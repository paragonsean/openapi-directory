

# Recommendation

Recommendations are suggested ways to improve your merchant account's performance. For example, to engage with a feature, or start using a new Google product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalCallToAction** | [**List&lt;RecommendationCallToAction&gt;**](RecommendationCallToAction.md) | Output only. CTAs of this recommendation. Repeated. |  [optional] [readonly] |
|**additionalDescriptions** | [**List&lt;RecommendationDescription&gt;**](RecommendationDescription.md) | Output only. List of additional localized descriptions for a recommendation. Localication uses the &#x60;languageCode&#x60; field in &#x60;GenerateRecommendations&#x60; requests. Not all description types are guaranteed to be present and we recommend to rely on default description. |  [optional] [readonly] |
|**creative** | [**List&lt;RecommendationCreative&gt;**](RecommendationCreative.md) | Output only. Any creatives attached to the recommendation. Repeated. |  [optional] [readonly] |
|**defaultCallToAction** | [**RecommendationCallToAction**](RecommendationCallToAction.md) |  |  [optional] |
|**defaultDescription** | **String** | Optional. Localized recommendation description. The localization the {@link &#x60;GenerateRecommendationsRequest.language_code&#x60;} field in {@link &#x60;GenerateRecommendationsRequest&#x60;} requests. |  [optional] |
|**numericalImpact** | **Integer** | Optional. A numerical score of the impact from the recommendation&#39;s description. For example, a recommendation might suggest an upward trend in sales for a certain product. Higher number means larger impact. |  [optional] |
|**paid** | **Boolean** | Optional. Indicates whether a user needs to pay when they complete the user journey suggested by the recommendation. |  [optional] |
|**recommendationName** | **String** | Optional. Localized recommendation name. The localization uses the {@link &#x60;GenerateRecommendationsRequest.language_code&#x60;} field in {@link &#x60;GenerateRecommendationsRequest&#x60;} requests. |  [optional] |
|**subType** | **String** | Optional. Subtype of the recommendations. Only applicable when multiple recommendations can be generated per type, and is used as an identifier of recommendation under the same recommendation type. |  [optional] |
|**title** | **String** | Optional. Localized Recommendation Title. Localization uses the {@link &#x60;GenerateRecommendationsRequest.language_code&#x60;} field in {@link &#x60;GenerateRecommendationsRequest&#x60;} requests. |  [optional] |
|**type** | **String** | Output only. Type of the recommendation. List of currently available recommendation types: - OPPORTUNITY_CREATE_NEW_COLLECTION - OPPORTUNITY_CREATE_EMAIL_CAMPAIGN |  [optional] [readonly] |



