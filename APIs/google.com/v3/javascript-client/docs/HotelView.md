# TravelPartnerApi.HotelView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataIssueDetail** | [**[DataIssueDetail]**](DataIssueDetail.md) | The type and severity of each data quality issue in the feed. If your feed contains data issues, update the feed and resubmit it. For more information, refer to this article. | [optional] 
**dataIssues** | **[String]** | DEPRECATED. Indicates that the hotel has data quality issues. The value of this field indicates the type of error. This has been replaced with the data_issue_detail field. If your feed contains data issues, update the feed and resubmit it. For more information, refer to this article. | [optional] 
**googleClusterId** | **String** | The Google Maps identifier for the hotel. | [optional] 
**googleHotelDisplayName** | **String** | Google&#39;s hotel name. | [optional] 
**googleHotelId** | **String** | Google&#39;s canonical ID for the hotel. | [optional] 
**liveOnGoogle** | **Boolean** | Optional. Whether the hotel appears in Google&#39;s hotel booking links. Declaration &amp; behavior to get detection of presence/absence in JSON conversion. | [optional] 
**matchStatus** | **String** | Current matching status of the hotel. | [optional] 
**overclusteredPartnerHotelIds** | **[String]** | Other hotels with which the hotel is overclustered. If your feed contains overclustered hotels, update the feed and resubmit it. To do this, you can use the manual match tool. | [optional] 
**partnerHotelDisplayName** | **String** | Partner&#39;s hotel name. | [optional] 
**partnerHotelId** | **String** | The unique ID of the hotel that the partner provides in their Hotel List Feed. | [optional] 
**primaryOverclusteredPartnerHotelId** | **String** | The primary hotel in the overclustered set. | [optional] 
**propertyDetails** | **String** | Optional. A URL to the property on Google. Only available for properties that are listed. | [optional] 



## Enum: [DataIssuesEnum]


* `FEED_DATA_ISSUE_UNSPECIFIED` (value: `"FEED_DATA_ISSUE_UNSPECIFIED"`)

* `FEED_DATA_ISSUE_UNKNOWN` (value: `"FEED_DATA_ISSUE_UNKNOWN"`)

* `NO_DATA_ISSUE` (value: `"NO_DATA_ISSUE"`)

* `DUPLICATE_ADDRESS` (value: `"DUPLICATE_ADDRESS"`)

* `MISSING_PHYSICAL_STREET_ADDRESS` (value: `"MISSING_PHYSICAL_STREET_ADDRESS"`)

* `MISSING_STREET_NAME` (value: `"MISSING_STREET_NAME"`)

* `MISSING_STREET_NUMBER` (value: `"MISSING_STREET_NUMBER"`)

* `MISSING_ADDRESS` (value: `"MISSING_ADDRESS"`)

* `MISSING_COUNTRY` (value: `"MISSING_COUNTRY"`)

* `INVALID_POSTAL_CODE` (value: `"INVALID_POSTAL_CODE"`)

* `INVALID_POSTAL_CODE_SUFFIX` (value: `"INVALID_POSTAL_CODE_SUFFIX"`)

* `UNEXPECTED_POSTAL_CODE_SUFFIX` (value: `"UNEXPECTED_POSTAL_CODE_SUFFIX"`)

* `UNEXPECTED_POSTAL_CODE` (value: `"UNEXPECTED_POSTAL_CODE"`)

* `INVALID_AMENITIES` (value: `"INVALID_AMENITIES"`)

* `INVALID_EMAIL_ADDRESS` (value: `"INVALID_EMAIL_ADDRESS"`)

* `DUPLICATE_LATLONG` (value: `"DUPLICATE_LATLONG"`)

* `LATLONG_INCONSISTENT_WITH_ADDRESS` (value: `"LATLONG_INCONSISTENT_WITH_ADDRESS"`)

* `MISSING_LATLONG` (value: `"MISSING_LATLONG"`)

* `COULD_NOT_GEOCODE` (value: `"COULD_NOT_GEOCODE"`)

* `MISSING_HOTEL_NAME` (value: `"MISSING_HOTEL_NAME"`)

* `HOTEL_NAME_EMPTY` (value: `"HOTEL_NAME_EMPTY"`)

* `INVALID_HOTEL_NAME` (value: `"INVALID_HOTEL_NAME"`)

* `HOTEL_NAME_TOO_LONG` (value: `"HOTEL_NAME_TOO_LONG"`)

* `PARSE_ERROR_IN_XML` (value: `"PARSE_ERROR_IN_XML"`)

* `UNEXPECTED_ATTRIBUTE_IN_XML` (value: `"UNEXPECTED_ATTRIBUTE_IN_XML"`)

* `DUPLICATE_PHONE_NUMBER` (value: `"DUPLICATE_PHONE_NUMBER"`)

* `MISSING_PHONE_NUMBER` (value: `"MISSING_PHONE_NUMBER"`)

* `MISSING_VOICE_PHONE_NUMBER` (value: `"MISSING_VOICE_PHONE_NUMBER"`)

* `INVALID_PHONE_NUMBER_FORMAT` (value: `"INVALID_PHONE_NUMBER_FORMAT"`)

* `INVALID_PHONE_NUMBER` (value: `"INVALID_PHONE_NUMBER"`)

* `INVALID_PHONE_NUMBER_COUNTRY_CODE` (value: `"INVALID_PHONE_NUMBER_COUNTRY_CODE"`)

* `PHONE_NUMBER_TOO_LONG` (value: `"PHONE_NUMBER_TOO_LONG"`)

* `PHONE_NUMBER_TOO_SHORT` (value: `"PHONE_NUMBER_TOO_SHORT"`)

* `INVALID_WEBSITE_URL` (value: `"INVALID_WEBSITE_URL"`)

* `ADWORDS_ATTRIBUTE_TOO_LONG` (value: `"ADWORDS_ATTRIBUTE_TOO_LONG"`)

* `BRAND_NOT_ALLOWED` (value: `"BRAND_NOT_ALLOWED"`)

* `FLAGGED_DUE_TO_SUSPICIOUS_METADATA` (value: `"FLAGGED_DUE_TO_SUSPICIOUS_METADATA"`)

* `NOT_ENOUGH_IMAGES_PROVIDED` (value: `"NOT_ENOUGH_IMAGES_PROVIDED"`)

* `IMAGE_PROCESSING_IN_PROGRESS` (value: `"IMAGE_PROCESSING_IN_PROGRESS"`)

* `CANNOT_FETCH_IMAGES` (value: `"CANNOT_FETCH_IMAGES"`)

* `INCOMPATIBLE_IMAGE_SIZE_OR_LOW_QUALITY` (value: `"INCOMPATIBLE_IMAGE_SIZE_OR_LOW_QUALITY"`)

* `MISSING_LANG_IN_RAW_LISTING` (value: `"MISSING_LANG_IN_RAW_LISTING"`)

* `IS_HOTEL` (value: `"IS_HOTEL"`)

* `MISSING_REQ_ATTR` (value: `"MISSING_REQ_ATTR"`)

* `MISSING_NAME` (value: `"MISSING_NAME"`)

* `MISSING_LANG_IN_NAME` (value: `"MISSING_LANG_IN_NAME"`)

* `VR_NAME_TOO_LONG` (value: `"VR_NAME_TOO_LONG"`)

* `TEST_PROPERTY` (value: `"TEST_PROPERTY"`)

* `NON_VR_ACCOMMODATION_TYPE_BASED_ON_LISTING_NAME` (value: `"NON_VR_ACCOMMODATION_TYPE_BASED_ON_LISTING_NAME"`)

* `BRAND_NAME_TOO_LONG` (value: `"BRAND_NAME_TOO_LONG"`)

* `MISSING_BRAND_NAME` (value: `"MISSING_BRAND_NAME"`)

* `INVALID_REVIEW_RATING` (value: `"INVALID_REVIEW_RATING"`)

* `INVALID_CHECKIN_FORMAT` (value: `"INVALID_CHECKIN_FORMAT"`)

* `INVALID_CHECKOUT_FORMAT` (value: `"INVALID_CHECKOUT_FORMAT"`)





## Enum: MatchStatusEnum


* `MATCH_STATUS_UNSPECIFIED` (value: `"MATCH_STATUS_UNSPECIFIED"`)

* `MATCH_STATUS_UNKNOWN` (value: `"MATCH_STATUS_UNKNOWN"`)

* `NOT_MATCHED` (value: `"NOT_MATCHED"`)

* `MATCHED` (value: `"MATCHED"`)

* `MAP_OVERLAP` (value: `"MAP_OVERLAP"`)




