

# Record

*NOTE:* There are a lot of fields that are very rarely used in DigitalNZ. For instance there are custom built fields that are only relevant, and only found on specific collections. The schema below focuses on the most common / well populated fields and does not show every possible field available for a single record.  

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**List&lt;CategoryEnum&gt;**](#List&lt;CategoryEnum&gt;) | There will always be at least 1 human-readable category label in this field. |  [optional] |
|**collection** | **List&lt;String&gt;** | In addition to the top level *\&quot;display_collection\&quot;* above, this field can also contain sub-collections or groupings within the main collection.   |  [optional] |
|**collectionTitle** | **List&lt;String&gt;** | For historic reasons this is a duplicate of the previous field (\&quot;collection\&quot;). |  [optional] |
|**contentPartner** | **List&lt;String&gt;** | Name of the organisation(s), institution(s), or individual(s) making content available through DigitalNZ. This metadata will be present on all records and is usually the name of the organisation that has agreed to the DigitalNZ Metadata Contribution Terms. |  [optional] |
|**copyright** | [**List&lt;CopyrightEnum&gt;**](#List&lt;CopyrightEnum&gt;) | A copyright statement applying to the object referenced by this record. This field may be empty. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date the record was initially harvested into DigitalNZ. |  [optional] |
|**creator** | **List&lt;String&gt;** | The name&#39;s of the people, organisations, institutions, services etc. who created the content (eg. the photographer, artist, writer or author). |  [optional] |
|**date** | **List&lt;String&gt;** | Date information associated with this record (e.g. 1996-01-01T00:00:00.000Z). This field may be empty. |  [optional] |
|**dcIdentifier** | **List&lt;String&gt;** | Identifiers relating to the content from the content partner&#39;s system. |  [optional] |
|**description** | **String** | Description of the record. Most records have a description. |  [optional] |
|**displayCollection** | **String** | The single main collection or website that the item belongs to. This metadata will be present on all records. |  [optional] |
|**displayContentPartner** | **String** | The main Content Partner, for cases when there are more than one. This metadata will be present on all records. |  [optional] |
|**displayDate** | **String** | Where provided, this field contains a human readable version of the date information. |  [optional] |
|**id** | **Integer** | All records have a unique identifier used within the DigitalNZ system. |  [optional] |
|**landingUrl** | **String** | This field will always contain a URL of the item on the content partner&#39;s website.   *Note:* Please use the source_url when providing HTML links.  |  [optional] |
|**largeThumbnailUrl** | **String** | URL for a larger thumbnail image with a width of up to 800px. NOTE - the API Terms do not extend rights to the use of images accessable throught the *large_thumbnail_url* field. |  [optional] |
|**locations** | [**List&lt;RecordLocationsInner&gt;**](RecordLocationsInner.md) | Geographical location information including latitude and longitude co-ordinates, text based location information, and details about where the location information comes from (eg. \&quot;Location provided by Museum of New Zealand Te Papa Tongarewa\&quot;)  |  [optional] |
|**primaryCollection** | **List&lt;String&gt;** | In most cases this is the same as *display_collection*, but will occasionally a second value. |  [optional] |
|**rights** | **String** | Rights information. Can be a rights statement explaining the rights of the record or a link to a webpage with more detailed rights information. |  [optional] |
|**rightsUrl** | **List&lt;String&gt;** | An array of HTTP URLs resolving to a rights statement or terms of use information for the resource. |  [optional] |
|**sourceUrl** | **String** | This URL will always be present and provides a redirect to the landing_url. This link should be used as the main click-through to the content. Passing users through this link allows DNZ to count the number of click-throughs, as well as trigger link-checking activities that help clean up stale links in DigitalNZ. |  [optional] |
|**subject** | **List&lt;String&gt;** | Keywords about the content. |  [optional] |
|**thumbnailUrl** | **String** | URL for a thumbnail image of the content. The size varies depending on what is available but we aim for a width of 250px. This field is mostly populated on records with a &#39;category&#39; of &#39;Images&#39;, but is also sometimes found on others (eg. \&quot;Videos\&quot;).  |  [optional] |
|**title** | **String** | Title of the record. All records should have a title. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date the record was last updated/re-harvested into DigitalNZ. |  [optional] |
|**usage** | [**List&lt;UsageEnum&gt;**](#List&lt;UsageEnum&gt;) | This field is always present and contains human-understandable information about how the item may be used based on its copyright/license. |  [optional] |



## Enum: List&lt;CategoryEnum&gt;

| Name | Value |
|---- | -----|
| NEWSPAPERS | &quot;Newspapers&quot; |
| IMAGES | &quot;Images&quot; |
| BOOKS | &quot;Books&quot; |
| ARTICLES | &quot;Articles&quot; |
| JOURNALS | &quot;Journals&quot; |
| ARCHIVES | &quot;Archives&quot; |
| AUDIO | &quot;Audio&quot; |
| OTHER | &quot;Other&quot; |
| MANUSCRIPTS | &quot;Manuscripts&quot; |
| REFERENCE_SOURCES | &quot;Reference sources&quot; |
| RESEARCH_PAPERS | &quot;Research papers&quot; |
| VIDEOS | &quot;Videos&quot; |
| MUSIC_SCORE | &quot;Music Score&quot; |
| GROUPS | &quot;Groups&quot; |
| DATA | &quot;Data&quot; |
| WEBSITES | &quot;Websites&quot; |
| SETS | &quot;Sets&quot; |



## Enum: List&lt;CopyrightEnum&gt;

| Name | Value |
|---- | -----|
| ALL_RIGHTS_RESERVED | &quot;All rights reserved&quot; |
| SOME_RIGHTS_RESERVED | &quot;Some rights reserved&quot; |
| NO_KNOWN_COPYRIGHT_RESTRICTIONS | &quot;No known copyright restrictions&quot; |
| UNKNOWN | &quot;Unknown&quot; |



## Enum: List&lt;UsageEnum&gt;

| Name | Value |
|---- | -----|
| ALL_RIGHTS_RESERVED | &quot;All rights reserved&quot; |
| SHARE | &quot;Share&quot; |
| MODIFY | &quot;Modify&quot; |
| USE_COMMERCIALLY | &quot;Use commercially&quot; |
| UNKNOWN | &quot;Unknown&quot; |



