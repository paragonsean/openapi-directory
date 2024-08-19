

# EntitiesEntityPresentationInfo

Defines additional information about an entity such as type hints.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityScenario** | [**EntityScenarioEnum**](#EntityScenarioEnum) | The supported scenario. |  |
|**entityTypeDisplayHint** | **String** | A display version of the entity hint. For example, if entityTypeHints is Artist, this field may be set to American Singer. |  [optional] [readonly] |
|**entityTypeHints** | [**List&lt;EntityTypeHintsEnum&gt;**](#List&lt;EntityTypeHintsEnum&gt;) | A list of hints that indicate the entity&#39;s type. The list could contain a single hint such as Movie or a list of hints such as Place, LocalBusiness, Restaurant. Each successive hint in the array narrows the entity&#39;s type. |  [optional] [readonly] |



## Enum: EntityScenarioEnum

| Name | Value |
|---- | -----|
| DOMINANT_ENTITY | &quot;DominantEntity&quot; |
| DISAMBIGUATION_ITEM | &quot;DisambiguationItem&quot; |
| LIST_ITEM | &quot;ListItem&quot; |



## Enum: List&lt;EntityTypeHintsEnum&gt;

| Name | Value |
|---- | -----|
| GENERIC | &quot;Generic&quot; |
| PERSON | &quot;Person&quot; |
| PLACE | &quot;Place&quot; |
| MEDIA | &quot;Media&quot; |
| ORGANIZATION | &quot;Organization&quot; |
| LOCAL_BUSINESS | &quot;LocalBusiness&quot; |
| RESTAURANT | &quot;Restaurant&quot; |
| HOTEL | &quot;Hotel&quot; |
| TOURIST_ATTRACTION | &quot;TouristAttraction&quot; |
| TRAVEL | &quot;Travel&quot; |
| CITY | &quot;City&quot; |
| COUNTRY | &quot;Country&quot; |
| ATTRACTION | &quot;Attraction&quot; |
| HOUSE | &quot;House&quot; |
| STATE | &quot;State&quot; |
| RADIO_STATION | &quot;RadioStation&quot; |
| STREET_ADDRESS | &quot;StreetAddress&quot; |
| NEIGHBORHOOD | &quot;Neighborhood&quot; |
| LOCALITY | &quot;Locality&quot; |
| POSTAL_CODE | &quot;PostalCode&quot; |
| REGION | &quot;Region&quot; |
| SUB_REGION | &quot;SubRegion&quot; |
| MINOR_REGION | &quot;MinorRegion&quot; |
| CONTINENT | &quot;Continent&quot; |
| POINT_OF_INTEREST | &quot;PointOfInterest&quot; |
| OTHER | &quot;Other&quot; |
| MOVIE | &quot;Movie&quot; |
| BOOK | &quot;Book&quot; |
| TELEVISION_SHOW | &quot;TelevisionShow&quot; |
| TELEVISION_SEASON | &quot;TelevisionSeason&quot; |
| VIDEO_GAME | &quot;VideoGame&quot; |
| MUSIC_ALBUM | &quot;MusicAlbum&quot; |
| MUSIC_RECORDING | &quot;MusicRecording&quot; |
| MUSIC_GROUP | &quot;MusicGroup&quot; |
| COMPOSITION | &quot;Composition&quot; |
| THEATER_PLAY | &quot;TheaterPlay&quot; |
| EVENT | &quot;Event&quot; |
| ACTOR | &quot;Actor&quot; |
| ARTIST | &quot;Artist&quot; |
| ATTORNEY | &quot;Attorney&quot; |
| SPECIALITY | &quot;Speciality&quot; |
| COLLEGE_OR_UNIVERSITY | &quot;CollegeOrUniversity&quot; |
| SCHOOL | &quot;School&quot; |
| FOOD | &quot;Food&quot; |
| DRUG | &quot;Drug&quot; |
| ANIMAL | &quot;Animal&quot; |
| SPORTS_TEAM | &quot;SportsTeam&quot; |
| PRODUCT | &quot;Product&quot; |
| CAR | &quot;Car&quot; |



