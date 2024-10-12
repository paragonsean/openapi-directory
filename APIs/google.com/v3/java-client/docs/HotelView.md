

# HotelView

A hotel view.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataIssueDetail** | [**List&lt;DataIssueDetail&gt;**](DataIssueDetail.md) | The type and severity of each data quality issue in the feed. If your feed contains data issues, update the feed and resubmit it. For more information, refer to this article. |  [optional] |
|**dataIssues** | [**List&lt;DataIssuesEnum&gt;**](#List&lt;DataIssuesEnum&gt;) | DEPRECATED. Indicates that the hotel has data quality issues. The value of this field indicates the type of error. This has been replaced with the data_issue_detail field. If your feed contains data issues, update the feed and resubmit it. For more information, refer to this article. |  [optional] |
|**googleClusterId** | **String** | The Google Maps identifier for the hotel. |  [optional] |
|**googleHotelDisplayName** | **String** | Google&#39;s hotel name. |  [optional] |
|**googleHotelId** | **String** | Google&#39;s canonical ID for the hotel. |  [optional] |
|**liveOnGoogle** | **Boolean** | Optional. Whether the hotel appears in Google&#39;s hotel booking links. Declaration &amp; behavior to get detection of presence/absence in JSON conversion. |  [optional] |
|**matchStatus** | [**MatchStatusEnum**](#MatchStatusEnum) | Current matching status of the hotel. |  [optional] |
|**overclusteredPartnerHotelIds** | **List&lt;String&gt;** | Other hotels with which the hotel is overclustered. If your feed contains overclustered hotels, update the feed and resubmit it. To do this, you can use the manual match tool. |  [optional] |
|**partnerHotelDisplayName** | **String** | Partner&#39;s hotel name. |  [optional] |
|**partnerHotelId** | **String** | The unique ID of the hotel that the partner provides in their Hotel List Feed. |  [optional] |
|**primaryOverclusteredPartnerHotelId** | **String** | The primary hotel in the overclustered set. |  [optional] |
|**propertyDetails** | **String** | Optional. A URL to the property on Google. Only available for properties that are listed. |  [optional] |



## Enum: List&lt;DataIssuesEnum&gt;

| Name | Value |
|---- | -----|
| FEED_DATA_ISSUE_UNSPECIFIED | &quot;FEED_DATA_ISSUE_UNSPECIFIED&quot; |
| FEED_DATA_ISSUE_UNKNOWN | &quot;FEED_DATA_ISSUE_UNKNOWN&quot; |
| NO_DATA_ISSUE | &quot;NO_DATA_ISSUE&quot; |
| DUPLICATE_ADDRESS | &quot;DUPLICATE_ADDRESS&quot; |
| MISSING_PHYSICAL_STREET_ADDRESS | &quot;MISSING_PHYSICAL_STREET_ADDRESS&quot; |
| MISSING_STREET_NAME | &quot;MISSING_STREET_NAME&quot; |
| MISSING_STREET_NUMBER | &quot;MISSING_STREET_NUMBER&quot; |
| MISSING_ADDRESS | &quot;MISSING_ADDRESS&quot; |
| MISSING_COUNTRY | &quot;MISSING_COUNTRY&quot; |
| INVALID_POSTAL_CODE | &quot;INVALID_POSTAL_CODE&quot; |
| INVALID_POSTAL_CODE_SUFFIX | &quot;INVALID_POSTAL_CODE_SUFFIX&quot; |
| UNEXPECTED_POSTAL_CODE_SUFFIX | &quot;UNEXPECTED_POSTAL_CODE_SUFFIX&quot; |
| UNEXPECTED_POSTAL_CODE | &quot;UNEXPECTED_POSTAL_CODE&quot; |
| INVALID_AMENITIES | &quot;INVALID_AMENITIES&quot; |
| INVALID_EMAIL_ADDRESS | &quot;INVALID_EMAIL_ADDRESS&quot; |
| DUPLICATE_LATLONG | &quot;DUPLICATE_LATLONG&quot; |
| LATLONG_INCONSISTENT_WITH_ADDRESS | &quot;LATLONG_INCONSISTENT_WITH_ADDRESS&quot; |
| MISSING_LATLONG | &quot;MISSING_LATLONG&quot; |
| COULD_NOT_GEOCODE | &quot;COULD_NOT_GEOCODE&quot; |
| MISSING_HOTEL_NAME | &quot;MISSING_HOTEL_NAME&quot; |
| HOTEL_NAME_EMPTY | &quot;HOTEL_NAME_EMPTY&quot; |
| INVALID_HOTEL_NAME | &quot;INVALID_HOTEL_NAME&quot; |
| HOTEL_NAME_TOO_LONG | &quot;HOTEL_NAME_TOO_LONG&quot; |
| PARSE_ERROR_IN_XML | &quot;PARSE_ERROR_IN_XML&quot; |
| UNEXPECTED_ATTRIBUTE_IN_XML | &quot;UNEXPECTED_ATTRIBUTE_IN_XML&quot; |
| DUPLICATE_PHONE_NUMBER | &quot;DUPLICATE_PHONE_NUMBER&quot; |
| MISSING_PHONE_NUMBER | &quot;MISSING_PHONE_NUMBER&quot; |
| MISSING_VOICE_PHONE_NUMBER | &quot;MISSING_VOICE_PHONE_NUMBER&quot; |
| INVALID_PHONE_NUMBER_FORMAT | &quot;INVALID_PHONE_NUMBER_FORMAT&quot; |
| INVALID_PHONE_NUMBER | &quot;INVALID_PHONE_NUMBER&quot; |
| INVALID_PHONE_NUMBER_COUNTRY_CODE | &quot;INVALID_PHONE_NUMBER_COUNTRY_CODE&quot; |
| PHONE_NUMBER_TOO_LONG | &quot;PHONE_NUMBER_TOO_LONG&quot; |
| PHONE_NUMBER_TOO_SHORT | &quot;PHONE_NUMBER_TOO_SHORT&quot; |
| INVALID_WEBSITE_URL | &quot;INVALID_WEBSITE_URL&quot; |
| ADWORDS_ATTRIBUTE_TOO_LONG | &quot;ADWORDS_ATTRIBUTE_TOO_LONG&quot; |
| BRAND_NOT_ALLOWED | &quot;BRAND_NOT_ALLOWED&quot; |
| FLAGGED_DUE_TO_SUSPICIOUS_METADATA | &quot;FLAGGED_DUE_TO_SUSPICIOUS_METADATA&quot; |
| NOT_ENOUGH_IMAGES_PROVIDED | &quot;NOT_ENOUGH_IMAGES_PROVIDED&quot; |
| IMAGE_PROCESSING_IN_PROGRESS | &quot;IMAGE_PROCESSING_IN_PROGRESS&quot; |
| CANNOT_FETCH_IMAGES | &quot;CANNOT_FETCH_IMAGES&quot; |
| INCOMPATIBLE_IMAGE_SIZE_OR_LOW_QUALITY | &quot;INCOMPATIBLE_IMAGE_SIZE_OR_LOW_QUALITY&quot; |
| MISSING_LANG_IN_RAW_LISTING | &quot;MISSING_LANG_IN_RAW_LISTING&quot; |
| IS_HOTEL | &quot;IS_HOTEL&quot; |
| MISSING_REQ_ATTR | &quot;MISSING_REQ_ATTR&quot; |
| MISSING_NAME | &quot;MISSING_NAME&quot; |
| MISSING_LANG_IN_NAME | &quot;MISSING_LANG_IN_NAME&quot; |
| VR_NAME_TOO_LONG | &quot;VR_NAME_TOO_LONG&quot; |
| TEST_PROPERTY | &quot;TEST_PROPERTY&quot; |
| NON_VR_ACCOMMODATION_TYPE_BASED_ON_LISTING_NAME | &quot;NON_VR_ACCOMMODATION_TYPE_BASED_ON_LISTING_NAME&quot; |
| BRAND_NAME_TOO_LONG | &quot;BRAND_NAME_TOO_LONG&quot; |
| MISSING_BRAND_NAME | &quot;MISSING_BRAND_NAME&quot; |
| INVALID_REVIEW_RATING | &quot;INVALID_REVIEW_RATING&quot; |
| INVALID_CHECKIN_FORMAT | &quot;INVALID_CHECKIN_FORMAT&quot; |
| INVALID_CHECKOUT_FORMAT | &quot;INVALID_CHECKOUT_FORMAT&quot; |



## Enum: MatchStatusEnum

| Name | Value |
|---- | -----|
| MATCH_STATUS_UNSPECIFIED | &quot;MATCH_STATUS_UNSPECIFIED&quot; |
| MATCH_STATUS_UNKNOWN | &quot;MATCH_STATUS_UNKNOWN&quot; |
| NOT_MATCHED | &quot;NOT_MATCHED&quot; |
| MATCHED | &quot;MATCHED&quot; |
| MAP_OVERLAP | &quot;MAP_OVERLAP&quot; |



