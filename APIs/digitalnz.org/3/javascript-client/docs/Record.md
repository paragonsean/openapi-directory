# DigitalNzApi.Record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **[String]** | There will always be at least 1 human-readable category label in this field. | [optional] 
**collection** | **[String]** | In addition to the top level *\&quot;display_collection\&quot;* above, this field can also contain sub-collections or groupings within the main collection.   | [optional] 
**collectionTitle** | **[String]** | For historic reasons this is a duplicate of the previous field (\&quot;collection\&quot;). | [optional] 
**contentPartner** | **[String]** | Name of the organisation(s), institution(s), or individual(s) making content available through DigitalNZ. This metadata will be present on all records and is usually the name of the organisation that has agreed to the DigitalNZ Metadata Contribution Terms. | [optional] 
**copyright** | **[String]** | A copyright statement applying to the object referenced by this record. This field may be empty. | [optional] 
**createdAt** | **Date** | The date the record was initially harvested into DigitalNZ. | [optional] 
**creator** | **[String]** | The name&#39;s of the people, organisations, institutions, services etc. who created the content (eg. the photographer, artist, writer or author). | [optional] 
**date** | **[String]** | Date information associated with this record (e.g. 1996-01-01T00:00:00.000Z). This field may be empty. | [optional] 
**dcIdentifier** | **[String]** | Identifiers relating to the content from the content partner&#39;s system. | [optional] 
**description** | **String** | Description of the record. Most records have a description. | [optional] 
**displayCollection** | **String** | The single main collection or website that the item belongs to. This metadata will be present on all records. | [optional] 
**displayContentPartner** | **String** | The main Content Partner, for cases when there are more than one. This metadata will be present on all records. | [optional] 
**displayDate** | **String** | Where provided, this field contains a human readable version of the date information. | [optional] 
**id** | **Number** | All records have a unique identifier used within the DigitalNZ system. | [optional] 
**landingUrl** | **String** | This field will always contain a URL of the item on the content partner&#39;s website.   *Note:* Please use the source_url when providing HTML links.  | [optional] 
**largeThumbnailUrl** | **String** | URL for a larger thumbnail image with a width of up to 800px. NOTE - the API Terms do not extend rights to the use of images accessable throught the *large_thumbnail_url* field. | [optional] 
**locations** | [**[RecordLocationsInner]**](RecordLocationsInner.md) | Geographical location information including latitude and longitude co-ordinates, text based location information, and details about where the location information comes from (eg. \&quot;Location provided by Museum of New Zealand Te Papa Tongarewa\&quot;)  | [optional] 
**primaryCollection** | **[String]** | In most cases this is the same as *display_collection*, but will occasionally a second value. | [optional] 
**rights** | **String** | Rights information. Can be a rights statement explaining the rights of the record or a link to a webpage with more detailed rights information. | [optional] 
**rightsUrl** | **[String]** | An array of HTTP URLs resolving to a rights statement or terms of use information for the resource. | [optional] 
**sourceUrl** | **String** | This URL will always be present and provides a redirect to the landing_url. This link should be used as the main click-through to the content. Passing users through this link allows DNZ to count the number of click-throughs, as well as trigger link-checking activities that help clean up stale links in DigitalNZ. | [optional] 
**subject** | **[String]** | Keywords about the content. | [optional] 
**thumbnailUrl** | **String** | URL for a thumbnail image of the content. The size varies depending on what is available but we aim for a width of 250px. This field is mostly populated on records with a &#39;category&#39; of &#39;Images&#39;, but is also sometimes found on others (eg. \&quot;Videos\&quot;).  | [optional] 
**title** | **String** | Title of the record. All records should have a title. | [optional] 
**updatedAt** | **Date** | The date the record was last updated/re-harvested into DigitalNZ. | [optional] 
**usage** | **[String]** | This field is always present and contains human-understandable information about how the item may be used based on its copyright/license. | [optional] 



## Enum: [CategoryEnum]


* `Newspapers` (value: `"Newspapers"`)

* `Images` (value: `"Images"`)

* `Books` (value: `"Books"`)

* `Articles` (value: `"Articles"`)

* `Journals` (value: `"Journals"`)

* `Archives` (value: `"Archives"`)

* `Audio` (value: `"Audio"`)

* `Other` (value: `"Other"`)

* `Manuscripts` (value: `"Manuscripts"`)

* `Reference sources` (value: `"Reference sources"`)

* `Research papers` (value: `"Research papers"`)

* `Videos` (value: `"Videos"`)

* `Music Score` (value: `"Music Score"`)

* `Groups` (value: `"Groups"`)

* `Data` (value: `"Data"`)

* `Websites` (value: `"Websites"`)

* `Sets` (value: `"Sets"`)





## Enum: [CopyrightEnum]


* `All rights reserved` (value: `"All rights reserved"`)

* `Some rights reserved` (value: `"Some rights reserved"`)

* `No known copyright restrictions` (value: `"No known copyright restrictions"`)

* `Unknown` (value: `"Unknown"`)





## Enum: [UsageEnum]


* `All rights reserved` (value: `"All rights reserved"`)

* `Share` (value: `"Share"`)

* `Modify` (value: `"Modify"`)

* `Use commercially` (value: `"Use commercially"`)

* `Unknown` (value: `"Unknown"`)




