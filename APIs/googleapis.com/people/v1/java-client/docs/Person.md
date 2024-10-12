

# Person

Information about a person merged from various data sources such as the authenticated user's contacts and profile data. Most fields can have multiple items. The items in a field have no guaranteed order, but each non-empty field is guaranteed to have exactly one field with `metadata.primary` set to true.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;Address&gt;**](Address.md) | The person&#39;s street addresses. |  [optional] |
|**ageRange** | [**AgeRangeEnum**](#AgeRangeEnum) | Output only. **DEPRECATED** (Please use &#x60;person.ageRanges&#x60; instead) The person&#39;s age range. |  [optional] [readonly] |
|**ageRanges** | [**List&lt;AgeRangeType&gt;**](AgeRangeType.md) | Output only. The person&#39;s age ranges. |  [optional] [readonly] |
|**biographies** | [**List&lt;Biography&gt;**](Biography.md) | The person&#39;s biographies. This field is a singleton for contact sources. |  [optional] |
|**birthdays** | [**List&lt;Birthday&gt;**](Birthday.md) | The person&#39;s birthdays. This field is a singleton for contact sources. |  [optional] |
|**braggingRights** | [**List&lt;BraggingRights&gt;**](BraggingRights.md) | **DEPRECATED**: No data will be returned The person&#39;s bragging rights. |  [optional] |
|**calendarUrls** | [**List&lt;CalendarUrl&gt;**](CalendarUrl.md) | The person&#39;s calendar URLs. |  [optional] |
|**clientData** | [**List&lt;ClientData&gt;**](ClientData.md) | The person&#39;s client data. |  [optional] |
|**coverPhotos** | [**List&lt;CoverPhoto&gt;**](CoverPhoto.md) | Output only. The person&#39;s cover photos. |  [optional] [readonly] |
|**emailAddresses** | [**List&lt;EmailAddress&gt;**](EmailAddress.md) | The person&#39;s email addresses. For &#x60;people.connections.list&#x60; and &#x60;otherContacts.list&#x60; the number of email addresses is limited to 100. If a Person has more email addresses the entire set can be obtained by calling GetPeople. |  [optional] |
|**etag** | **String** | The [HTTP entity tag](https://en.wikipedia.org/wiki/HTTP_ETag) of the resource. Used for web cache validation. |  [optional] |
|**events** | [**List&lt;Event&gt;**](Event.md) | The person&#39;s events. |  [optional] |
|**externalIds** | [**List&lt;ExternalId&gt;**](ExternalId.md) | The person&#39;s external IDs. |  [optional] |
|**fileAses** | [**List&lt;FileAs&gt;**](FileAs.md) | The person&#39;s file-ases. |  [optional] |
|**genders** | [**List&lt;Gender&gt;**](Gender.md) | The person&#39;s genders. This field is a singleton for contact sources. |  [optional] |
|**imClients** | [**List&lt;ImClient&gt;**](ImClient.md) | The person&#39;s instant messaging clients. |  [optional] |
|**interests** | [**List&lt;Interest&gt;**](Interest.md) | The person&#39;s interests. |  [optional] |
|**locales** | [**List&lt;Locale&gt;**](Locale.md) | The person&#39;s locale preferences. |  [optional] |
|**locations** | [**List&lt;Location&gt;**](Location.md) | The person&#39;s locations. |  [optional] |
|**memberships** | [**List&lt;Membership&gt;**](Membership.md) | The person&#39;s group memberships. |  [optional] |
|**metadata** | [**PersonMetadata**](PersonMetadata.md) |  |  [optional] |
|**miscKeywords** | [**List&lt;MiscKeyword&gt;**](MiscKeyword.md) | The person&#39;s miscellaneous keywords. |  [optional] |
|**names** | [**List&lt;Name&gt;**](Name.md) | The person&#39;s names. This field is a singleton for contact sources. |  [optional] |
|**nicknames** | [**List&lt;Nickname&gt;**](Nickname.md) | The person&#39;s nicknames. |  [optional] |
|**occupations** | [**List&lt;Occupation&gt;**](Occupation.md) | The person&#39;s occupations. |  [optional] |
|**organizations** | [**List&lt;Organization&gt;**](Organization.md) | The person&#39;s past or current organizations. |  [optional] |
|**phoneNumbers** | [**List&lt;PhoneNumber&gt;**](PhoneNumber.md) | The person&#39;s phone numbers. For &#x60;people.connections.list&#x60; and &#x60;otherContacts.list&#x60; the number of phone numbers is limited to 100. If a Person has more phone numbers the entire set can be obtained by calling GetPeople. |  [optional] |
|**photos** | [**List&lt;Photo&gt;**](Photo.md) | Output only. The person&#39;s photos. |  [optional] [readonly] |
|**relations** | [**List&lt;Relation&gt;**](Relation.md) | The person&#39;s relations. |  [optional] |
|**relationshipInterests** | [**List&lt;RelationshipInterest&gt;**](RelationshipInterest.md) | Output only. **DEPRECATED**: No data will be returned The person&#39;s relationship interests. |  [optional] [readonly] |
|**relationshipStatuses** | [**List&lt;RelationshipStatus&gt;**](RelationshipStatus.md) | Output only. **DEPRECATED**: No data will be returned The person&#39;s relationship statuses. |  [optional] [readonly] |
|**residences** | [**List&lt;Residence&gt;**](Residence.md) | **DEPRECATED**: (Please use &#x60;person.locations&#x60; instead) The person&#39;s residences. |  [optional] |
|**resourceName** | **String** | The resource name for the person, assigned by the server. An ASCII string in the form of &#x60;people/{person_id}&#x60;. |  [optional] |
|**sipAddresses** | [**List&lt;SipAddress&gt;**](SipAddress.md) | The person&#39;s SIP addresses. |  [optional] |
|**skills** | [**List&lt;Skill&gt;**](Skill.md) | The person&#39;s skills. |  [optional] |
|**taglines** | [**List&lt;Tagline&gt;**](Tagline.md) | Output only. **DEPRECATED**: No data will be returned The person&#39;s taglines. |  [optional] [readonly] |
|**urls** | [**List&lt;Url&gt;**](Url.md) | The person&#39;s associated URLs. |  [optional] |
|**userDefined** | [**List&lt;UserDefined&gt;**](UserDefined.md) | The person&#39;s user defined data. |  [optional] |



## Enum: AgeRangeEnum

| Name | Value |
|---- | -----|
| AGE_RANGE_UNSPECIFIED | &quot;AGE_RANGE_UNSPECIFIED&quot; |
| LESS_THAN_EIGHTEEN | &quot;LESS_THAN_EIGHTEEN&quot; |
| EIGHTEEN_TO_TWENTY | &quot;EIGHTEEN_TO_TWENTY&quot; |
| TWENTY_ONE_OR_OLDER | &quot;TWENTY_ONE_OR_OLDER&quot; |



