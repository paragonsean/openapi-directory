

# CreativeServingRestrictionsInnerContextsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auctionType** | **List&lt;String&gt;** | Only set when contextType&#x3D;AUCTION_TYPE. Represents the auction types this restriction applies to. |  [optional] |
|**contextType** | **String** | The type of context (e.g., location, platform, auction type, SSL-ness). |  [optional] |
|**geoCriteriaId** | **List&lt;Integer&gt;** | Only set when contextType&#x3D;LOCATION. Represents the geo criterias this restriction applies to. Impressions are considered to match a context if either the user location or publisher location matches a given geoCriteriaId. |  [optional] |
|**platform** | **List&lt;String&gt;** | Only set when contextType&#x3D;PLATFORM. Represents the platforms this restriction applies to. |  [optional] |



