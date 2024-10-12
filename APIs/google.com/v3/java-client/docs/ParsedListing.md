

# ParsedListing

A parsed listing

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brand** | **String** | If not empty, it indicates that this listing belongs to a brand of the feed. |  [optional] |
|**category** | [**List&lt;LocalizedText&gt;**](LocalizedText.md) | The partner provided category (accommodation type) of the property. |  [optional] |
|**dataIssueDetail** | [**List&lt;DataIssueDetail&gt;**](DataIssueDetail.md) | Data issues about this listing |  [optional] |
|**description** | [**List&lt;LocalizedText&gt;**](LocalizedText.md) | Description of the property. |  [optional] |
|**image** | [**List&lt;Image&gt;**](Image.md) | Images associated with this listing, localized. |  [optional] |
|**imprecisionRadiusMeters** | **Integer** | Represents the accuracy of the location. The listing can be anywhere within the defined circular area. |  [optional] |
|**isServed** | **Boolean** | Whether the listing can be served based on non image data alone. |  [optional] |
|**listingName** | [**List&lt;LocalizedText&gt;**](LocalizedText.md) | List of localized names. |  [optional] |
|**location** | [**LatLng**](LatLng.md) |  |  [optional] |
|**partnerListId** | **String** | The list id on partner lec feed, provided by partner. |  [optional] |
|**regionCode** | **String** | The country code where the listing is located. |  [optional] |
|**review** | [**List&lt;Review&gt;**](Review.md) | Reviews associated with this listing. Each review proto has a single language attached to it. |  [optional] |
|**unitAttributes** | **Map&lt;String, String&gt;** | VR List attribute. |  [optional] |



