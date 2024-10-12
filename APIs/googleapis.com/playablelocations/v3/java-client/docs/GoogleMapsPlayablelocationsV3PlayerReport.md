

# GoogleMapsPlayablelocationsV3PlayerReport

A report submitted by a player about a playable location that is considered inappropriate for use in the game.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageCode** | **String** | Language code (in BCP-47 format) indicating the language of the freeform description provided in &#x60;reason_details&#x60;. Examples are \&quot;en\&quot;, \&quot;en-US\&quot; or \&quot;ja-Latn\&quot;. For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier. |  [optional] |
|**locationName** | **String** | Required. The name of the playable location. |  [optional] |
|**reasonDetails** | **String** | Required. A free-form description detailing why the playable location is considered bad. |  [optional] |
|**reasons** | [**List&lt;ReasonsEnum&gt;**](#List&lt;ReasonsEnum&gt;) | Required. One or more reasons why this playable location is considered bad. |  [optional] |



## Enum: List&lt;ReasonsEnum&gt;

| Name | Value |
|---- | -----|
| BAD_LOCATION_REASON_UNSPECIFIED | &quot;BAD_LOCATION_REASON_UNSPECIFIED&quot; |
| OTHER | &quot;OTHER&quot; |
| NOT_PEDESTRIAN_ACCESSIBLE | &quot;NOT_PEDESTRIAN_ACCESSIBLE&quot; |
| NOT_OPEN_TO_PUBLIC | &quot;NOT_OPEN_TO_PUBLIC&quot; |
| PERMANENTLY_CLOSED | &quot;PERMANENTLY_CLOSED&quot; |
| TEMPORARILY_INACCESSIBLE | &quot;TEMPORARILY_INACCESSIBLE&quot; |



