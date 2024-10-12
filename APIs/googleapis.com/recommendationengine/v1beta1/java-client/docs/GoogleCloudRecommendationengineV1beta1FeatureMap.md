

# GoogleCloudRecommendationengineV1beta1FeatureMap

FeatureMap represents extra features that customers want to include in the recommendation model for catalogs/user events as categorical/numerical features.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoricalFeatures** | [**Map&lt;String, GoogleCloudRecommendationengineV1beta1FeatureMapStringList&gt;**](GoogleCloudRecommendationengineV1beta1FeatureMapStringList.md) | Categorical features that can take on one of a limited number of possible values. Some examples would be the brand/maker of a product, or country of a customer. Feature names and values must be UTF-8 encoded strings. For example: &#x60;{ \&quot;colors\&quot;: {\&quot;value\&quot;: [\&quot;yellow\&quot;, \&quot;green\&quot;]}, \&quot;sizes\&quot;: {\&quot;value\&quot;:[\&quot;S\&quot;, \&quot;M\&quot;]}&#x60; |  [optional] |
|**numericalFeatures** | [**Map&lt;String, GoogleCloudRecommendationengineV1beta1FeatureMapFloatList&gt;**](GoogleCloudRecommendationengineV1beta1FeatureMapFloatList.md) | Numerical features. Some examples would be the height/weight of a product, or age of a customer. Feature names must be UTF-8 encoded strings. For example: &#x60;{ \&quot;lengths_cm\&quot;: {\&quot;value\&quot;:[2.3, 15.4]}, \&quot;heights_cm\&quot;: {\&quot;value\&quot;:[8.1, 6.4]} }&#x60; |  [optional] |



