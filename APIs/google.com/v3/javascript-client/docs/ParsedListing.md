# TravelPartnerApi.ParsedListing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **String** | If not empty, it indicates that this listing belongs to a brand of the feed. | [optional] 
**category** | [**[LocalizedText]**](LocalizedText.md) | The partner provided category (accommodation type) of the property. | [optional] 
**dataIssueDetail** | [**[DataIssueDetail]**](DataIssueDetail.md) | Data issues about this listing | [optional] 
**description** | [**[LocalizedText]**](LocalizedText.md) | Description of the property. | [optional] 
**image** | [**[Image]**](Image.md) | Images associated with this listing, localized. | [optional] 
**imprecisionRadiusMeters** | **Number** | Represents the accuracy of the location. The listing can be anywhere within the defined circular area. | [optional] 
**isServed** | **Boolean** | Whether the listing can be served based on non image data alone. | [optional] 
**listingName** | [**[LocalizedText]**](LocalizedText.md) | List of localized names. | [optional] 
**location** | [**LatLng**](LatLng.md) |  | [optional] 
**partnerListId** | **String** | The list id on partner lec feed, provided by partner. | [optional] 
**regionCode** | **String** | The country code where the listing is located. | [optional] 
**review** | [**[Review]**](Review.md) | Reviews associated with this listing. Each review proto has a single language attached to it. | [optional] 
**unitAttributes** | **{String: String}** | VR List attribute. | [optional] 


