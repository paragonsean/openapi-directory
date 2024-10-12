

# RecommendationCallToAction

Call to action (CTA) that explains how a merchant can implement this recommendation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intent** | **String** | Output only. Intent of the action. This value describes the intent (for example, &#x60;OPEN_CREATE_EMAIL_CAMPAIGN_FLOW&#x60;) and can vary from recommendation to recommendation. This value can change over time for the same recommendation. Currently available intent values: - OPEN_CREATE_EMAIL_CAMPAIGN_FLOW: Opens a user journey where they can create a marketing email campaign. (No default URL) - OPEN_CREATE_COLLECTION_TAB: Opens a user journey where they can [create a collection](https://support.google.com/merchants/answer/9703228) for their Merchant account. (No default URL) |  [optional] [readonly] |
|**localizedText** | **String** | Output only. Localized text of the CTA. Optional. |  [optional] [readonly] |
|**uri** | **String** | Optional. URL of the CTA. This field will only be set for some recommendations where there is a suggested landing URL. Otherwise it will be set to an empty string. We recommend developers to use their own custom landing page according to the description of the intent field above when this uri field is empty. |  [optional] |



