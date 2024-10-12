# PeopleApi.Person

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[Address]**](Address.md) | The person&#39;s street addresses. | [optional] 
**ageRange** | **String** | Output only. **DEPRECATED** (Please use &#x60;person.ageRanges&#x60; instead) The person&#39;s age range. | [optional] [readonly] 
**ageRanges** | [**[AgeRangeType]**](AgeRangeType.md) | Output only. The person&#39;s age ranges. | [optional] [readonly] 
**biographies** | [**[Biography]**](Biography.md) | The person&#39;s biographies. This field is a singleton for contact sources. | [optional] 
**birthdays** | [**[Birthday]**](Birthday.md) | The person&#39;s birthdays. This field is a singleton for contact sources. | [optional] 
**braggingRights** | [**[BraggingRights]**](BraggingRights.md) | **DEPRECATED**: No data will be returned The person&#39;s bragging rights. | [optional] 
**calendarUrls** | [**[CalendarUrl]**](CalendarUrl.md) | The person&#39;s calendar URLs. | [optional] 
**clientData** | [**[ClientData]**](ClientData.md) | The person&#39;s client data. | [optional] 
**coverPhotos** | [**[CoverPhoto]**](CoverPhoto.md) | Output only. The person&#39;s cover photos. | [optional] [readonly] 
**emailAddresses** | [**[EmailAddress]**](EmailAddress.md) | The person&#39;s email addresses. For &#x60;people.connections.list&#x60; and &#x60;otherContacts.list&#x60; the number of email addresses is limited to 100. If a Person has more email addresses the entire set can be obtained by calling GetPeople. | [optional] 
**etag** | **String** | The [HTTP entity tag](https://en.wikipedia.org/wiki/HTTP_ETag) of the resource. Used for web cache validation. | [optional] 
**events** | [**[Event]**](Event.md) | The person&#39;s events. | [optional] 
**externalIds** | [**[ExternalId]**](ExternalId.md) | The person&#39;s external IDs. | [optional] 
**fileAses** | [**[FileAs]**](FileAs.md) | The person&#39;s file-ases. | [optional] 
**genders** | [**[Gender]**](Gender.md) | The person&#39;s genders. This field is a singleton for contact sources. | [optional] 
**imClients** | [**[ImClient]**](ImClient.md) | The person&#39;s instant messaging clients. | [optional] 
**interests** | [**[Interest]**](Interest.md) | The person&#39;s interests. | [optional] 
**locales** | [**[Locale]**](Locale.md) | The person&#39;s locale preferences. | [optional] 
**locations** | [**[Location]**](Location.md) | The person&#39;s locations. | [optional] 
**memberships** | [**[Membership]**](Membership.md) | The person&#39;s group memberships. | [optional] 
**metadata** | [**PersonMetadata**](PersonMetadata.md) |  | [optional] 
**miscKeywords** | [**[MiscKeyword]**](MiscKeyword.md) | The person&#39;s miscellaneous keywords. | [optional] 
**names** | [**[Name]**](Name.md) | The person&#39;s names. This field is a singleton for contact sources. | [optional] 
**nicknames** | [**[Nickname]**](Nickname.md) | The person&#39;s nicknames. | [optional] 
**occupations** | [**[Occupation]**](Occupation.md) | The person&#39;s occupations. | [optional] 
**organizations** | [**[Organization]**](Organization.md) | The person&#39;s past or current organizations. | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) | The person&#39;s phone numbers. For &#x60;people.connections.list&#x60; and &#x60;otherContacts.list&#x60; the number of phone numbers is limited to 100. If a Person has more phone numbers the entire set can be obtained by calling GetPeople. | [optional] 
**photos** | [**[Photo]**](Photo.md) | Output only. The person&#39;s photos. | [optional] [readonly] 
**relations** | [**[Relation]**](Relation.md) | The person&#39;s relations. | [optional] 
**relationshipInterests** | [**[RelationshipInterest]**](RelationshipInterest.md) | Output only. **DEPRECATED**: No data will be returned The person&#39;s relationship interests. | [optional] [readonly] 
**relationshipStatuses** | [**[RelationshipStatus]**](RelationshipStatus.md) | Output only. **DEPRECATED**: No data will be returned The person&#39;s relationship statuses. | [optional] [readonly] 
**residences** | [**[Residence]**](Residence.md) | **DEPRECATED**: (Please use &#x60;person.locations&#x60; instead) The person&#39;s residences. | [optional] 
**resourceName** | **String** | The resource name for the person, assigned by the server. An ASCII string in the form of &#x60;people/{person_id}&#x60;. | [optional] 
**sipAddresses** | [**[SipAddress]**](SipAddress.md) | The person&#39;s SIP addresses. | [optional] 
**skills** | [**[Skill]**](Skill.md) | The person&#39;s skills. | [optional] 
**taglines** | [**[Tagline]**](Tagline.md) | Output only. **DEPRECATED**: No data will be returned The person&#39;s taglines. | [optional] [readonly] 
**urls** | [**[Url]**](Url.md) | The person&#39;s associated URLs. | [optional] 
**userDefined** | [**[UserDefined]**](UserDefined.md) | The person&#39;s user defined data. | [optional] 



## Enum: AgeRangeEnum


* `AGE_RANGE_UNSPECIFIED` (value: `"AGE_RANGE_UNSPECIFIED"`)

* `LESS_THAN_EIGHTEEN` (value: `"LESS_THAN_EIGHTEEN"`)

* `EIGHTEEN_TO_TWENTY` (value: `"EIGHTEEN_TO_TWENTY"`)

* `TWENTY_ONE_OR_OLDER` (value: `"TWENTY_ONE_OR_OLDER"`)




