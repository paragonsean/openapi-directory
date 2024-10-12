

# PublisherProfileApiProto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audience** | **String** | Publisher provided info on its audience. |  [optional] |
|**buyerPitchStatement** | **String** | A pitch statement for the buyer |  [optional] |
|**directContact** | **String** | Direct contact for the publisher profile. |  [optional] |
|**exchange** | **String** | Exchange where this publisher profile is from. E.g. AdX, Rubicon etc... |  [optional] |
|**forecastInventory** | **String** |  |  [optional] |
|**googlePlusLink** | **String** | Link to publisher&#39;s Google+ page. |  [optional] |
|**isParent** | **Boolean** | True, if this is the parent profile, which represents all domains owned by the publisher. |  [optional] |
|**isPublished** | **Boolean** | True, if this profile is published. Deprecated for state. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;adexchangebuyer#publisherProfileApiProto\&quot;. |  [optional] |
|**logoUrl** | **String** | The url to the logo for the publisher. |  [optional] |
|**mediaKitLink** | **String** | The url for additional marketing and sales materials. |  [optional] |
|**name** | **String** |  |  [optional] |
|**overview** | **String** | Publisher provided overview. |  [optional] |
|**profileId** | **Integer** | The pair of (seller.account_id, profile_id) uniquely identifies a publisher profile for a given publisher. |  [optional] |
|**programmaticContact** | **String** | Programmatic contact for the publisher profile. |  [optional] |
|**publisherAppIds** | **List&lt;String&gt;** | The list of app IDs represented in this publisher profile. Empty if this is a parent profile. Deprecated in favor of publisher_app. |  [optional] |
|**publisherApps** | [**List&lt;MobileApplication&gt;**](MobileApplication.md) | The list of apps represented in this publisher profile. Empty if this is a parent profile. |  [optional] |
|**publisherDomains** | **List&lt;String&gt;** | The list of domains represented in this publisher profile. Empty if this is a parent profile. |  [optional] |
|**publisherProfileId** | **String** | Unique Id for publisher profile. |  [optional] |
|**publisherProvidedForecast** | [**PublisherProvidedForecast**](PublisherProvidedForecast.md) |  |  [optional] |
|**rateCardInfoLink** | **String** | Link to publisher rate card |  [optional] |
|**samplePageLink** | **String** | Link for a sample content page. |  [optional] |
|**seller** | [**Seller**](Seller.md) |  |  [optional] |
|**state** | **String** | State of the publisher profile. |  [optional] |
|**topHeadlines** | **List&lt;String&gt;** | Publisher provided key metrics and rankings. |  [optional] |



