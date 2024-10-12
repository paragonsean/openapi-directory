# PlayableLocationsApi.GoogleMapsPlayablelocationsV3PlayerReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**languageCode** | **String** | Language code (in BCP-47 format) indicating the language of the freeform description provided in &#x60;reason_details&#x60;. Examples are \&quot;en\&quot;, \&quot;en-US\&quot; or \&quot;ja-Latn\&quot;. For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier. | [optional] 
**locationName** | **String** | Required. The name of the playable location. | [optional] 
**reasonDetails** | **String** | Required. A free-form description detailing why the playable location is considered bad. | [optional] 
**reasons** | **[String]** | Required. One or more reasons why this playable location is considered bad. | [optional] 



## Enum: [ReasonsEnum]


* `BAD_LOCATION_REASON_UNSPECIFIED` (value: `"BAD_LOCATION_REASON_UNSPECIFIED"`)

* `OTHER` (value: `"OTHER"`)

* `NOT_PEDESTRIAN_ACCESSIBLE` (value: `"NOT_PEDESTRIAN_ACCESSIBLE"`)

* `NOT_OPEN_TO_PUBLIC` (value: `"NOT_OPEN_TO_PUBLIC"`)

* `PERMANENTLY_CLOSED` (value: `"PERMANENTLY_CLOSED"`)

* `TEMPORARILY_INACCESSIBLE` (value: `"TEMPORARILY_INACCESSIBLE"`)




