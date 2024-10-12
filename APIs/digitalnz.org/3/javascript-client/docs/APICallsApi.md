# DigitalNzApi.APICallsApi

All URIs are relative to *https://api.digitalnz.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recordsFormatGet**](APICallsApi.md#recordsFormatGet) | **GET** /records.{format} | Run queries against DigitalNZ metadata search service.
[**recordsRecordIdFormatGet**](APICallsApi.md#recordsRecordIdFormatGet) | **GET** /records/{record_id}.{format} | View metadata associated with a single record.
[**recordsRecordIdMoreLikeThisFormatGet**](APICallsApi.md#recordsRecordIdMoreLikeThisFormatGet) | **GET** /records/{record_id}/more_like_this.{format} | The \&quot;More Like This\&quot; call returns similar records to the specified ID. 



## recordsFormatGet

> RecordsFormatGet200Response recordsFormatGet(format, opts)

Run queries against DigitalNZ metadata search service.

This is the main search endpoint allowing queries against the records database.

### Example

```javascript
import DigitalNzApi from 'digital_nz_api';
let defaultClient = DigitalNzApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DigitalNzApi.APICallsApi();
let format = "format_example"; // String | Note - There is a small difference with some field names in the response between JSON and XML.   When a field name has more than one word, JSON format will separate the words with an underscore, eg. \"content_partner\", whereas XML uses a hyphenated naming convention, eg. \"content-partner\". 
let opts = {
  'authenticationToken': "authenticationToken_example", // String | The DigitalNZ API no longer requires a key to access public content. However, if you plan on using the API regularly, expect to be a high volume consumer or are planning on creating an application, we encourage you to use an API key so that we can: - provide targeted help and support - increase your query throughput (by negotiation) - notify you directly of changes to the API - gather usage metrics to help improve the service    API requests that do not pass a valid API key/token are treated as unauthenticated. A maximum rate limit applies across all unauthenticated requests. This rate limit is in place to protect the service from overuse, resulting in unsustainable costs, or potential attack.  **Getting an API key**   [Create a DigitalNZ account](https://digitalnz.org/sign_up), log in and select \"[my API key](https://digitalnz.org/api_keys/edit)\" from your username drop-down menu (on the right hand side)'. The key is a long string of jumbled letters and numbers (hash) that is unique to you. You are required to keep the key secret. (Refer to the [Developer API Terms of Use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use) for more information).  **Using an API key**   When you make a call to the API you'll need to pass the key in a custom HTTP header: ‘Authentication-Token’. For example, a query using the ‘curl’ command might look like the following (where ‘{YOUR_API_KEY}’ is replaced with a valid API key):  `curl -H \"Authentication-Token:{YOUR_API_KEY}\" http://api.digitalnz.org/v3/records.json?text=kiwi` 
  'text': "text_example", // String | This field enables queries based on one or more search terms and provides the functionality of the main search box on [digitalnz.org](https://digitalnz.org). Search terms can be combined with boolean operators (AND, OR).   A minus sign excludes certain terms, eg. \"-horse\".   An asterisk (\\*) acts as a wildcard, eg. \"ted*\".   Multiple search terms are combined with an AND by default.   Examples: `\"moustache\"`, `\"Wanganui OR Whanganui\"`,  `\"-paperspast\"`, `\"ted*\"` 
  'andCategory': "andCategory_example", // String | These are the same categories that are used across the tabs in [digitalnz.org](https://digitalnz.org/records?text=&tab=Videos)
  'andContentPartner': "andContentPartner_example", // String | Allows filtering for records from a particular Content Partner.   Examples: `\"Ministry for Culture and Heritage\"` `\"Trove\"` `\"V.C. Browne & Son\"`    *Tip* - To see a list of Content Partners available for filtering use the *facets* parameter, eg. *\"&facets=content_partner\"*.   
  'andPrimaryCollection': "andPrimaryCollection_example", // String | Allows filtering for records from a particular *primary_collection*.   Examples: `\"Puke Ariki\"` `\"NZHistory\"` `\"TAPUHI\"`      *Tip* - To see a list of Primary_Collections available for filtering use the *facets* parameter, eg. *\"&facets=primary_collection\"*.    
  'andCollection': "andCollection_example", // String | Allows filtering for records from a particular Collection. Collections can be thought of as sub-collections or groupings under Primary_Collections.   Examples: `\"Music 101\"` `\"Mollusks\"` `\"Wairarapa Daily Times\"`    *Tip* - To see a list of Collections available for filtering use the *facets* parameter, eg. *\"&facets=collection\"*.  
  'andUsage': "andUsage_example", // String | 
  'andSubject': "andSubject_example", // String | Examples: `\"Cats\"` `\"Weddings\"` `\"climb*\"` 
  'andDcType': "andDcType_example", // String | Examples: `\"Conference item\"` `\"Magazines\"` 
  'andFormat': "andFormat_example", // String | Examples: `\"Photolithographs\"` `\"Glass*\"` 
  'andPlacename': "andPlacename_example", // String | This field can be used for text-based location search. For a more advanced coordinate-based search, see the \"geo_bbox\" field below.   Examples: `\"Scott Base\"` `\"Wainuiomata\"` `\"castle*\"` 
  'andCreator': "andCreator_example", // String | Examples: `\"Revelle Jackson\"` `\"Nicholas Chevalier\"` `\"Rita Angus\"` 
  'andTitle': "andTitle_example", // String | Examples: `\"Pukeko\"` `\"Club\"` `\"Break*\"`\" 
  'andDate': "andDate_example", // String | This field can be useful for querying and sorting (see the 'sort' param further down). But it should be noted that, as with some other fields, **not all records have date metadata associated**. There is good coverage of date metadata within certain collections, but there are plenty with no date information at all. So, if you query for records from a specific date you may get some matching results, but might also be missing other potentially relevant records that don't have date metadata available.   Example: `\"1970-12-25\"`  *Tip* - There is a related (but not searchable) field that is returned on each record (where available), that often has a more human readable version of the date information, called 'display_date'. 
  'andYear': "andYear_example", // String | This field allows searching specifically by year. The metadata is derived from the same date information that is searchable and returned in the date field. It is possible to search across a range using syntax the following syntax `[{start year} TO {end year}]`.   Example: `\"1893\"` `\"[1982 TO 1987]\"` 
  'andDecade': "andDecade_example", // String | This field allows searching specifically by decade. The metadata is derived from the same date information that is searchable and returned in the date field.   Example: `\"1850\"` `\"1990\"` 
  'andCentury': "andCentury_example", // String | This field allows searching specifically by century. The metadata is derived from the same date information that is searchable and returned in the date field.   Example: `\"1900\"` `\"2000\"` 
  'withoutFilterField': "withoutFilterField_example", // String | All of the above `and[___][]` filters in this document are also able to be used with this syntax to exclude specific matches. For example to exclude Papers Past content `&without[primary_collection]=Papers+Past` 
  'andOrFilterField': "andOrFilterField_example", // String | All of the above `and[___][]` filters in this document are also able to be used with the `and[or][___][]` syntax to allow multi-select *OR* queries within one field.   Basic example:  - To filter your results to only those with a category or Audio or Videos:    `&and[or][category][]=Audio&and[or][category][]=Videos`     In order to combine *OR* filters across multiple fields the syntax needs to be nested as follows   Nested examples:   - To search for *(year is 2014 OR 2015) AND (primary_collection is TAPUHI OR Public Address)*    `&and[or][year][]=2015&and[or][year][]=2014&and[and][or][primary_collection][]=TAPUHI&and[and][or][primary_collection][]=Public+Address`    - To search for *(category is Images OR Video) AND (subject is cat OR cats)*    `&and[or][category][]=Images&and[or][category][]=Videos&and[and][or][subject][]=cat&and[and][or][subject][]=cats`   
  'andIsCommercialUse': true, // Boolean | Some DigitalNZ partners offer their metadata for use in commercial applications. This content can be identified through the *is_commercial_use* flag. Only API results where the *is_commercial_use* field set to True can be used for commercial purposes. Check out the [terms of use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use#commercial_use_terms) for more information. 
  'andHasLargeThumbnailUrl': "andHasLargeThumbnailUrl_example", // String | Filters results to only those records that have an image available in the *large_thumbnail_url* field.   **Note:** There is an issue with this field where, in order to get results, it needs to be specified with \"Y\" or not specified at all. 
  'andHasLatLng': true, // Boolean | Filters results to only those records that have latitude and longitude coordinates present in the metadata.    *Tip* - To see the location metadata you'll need to specifically request that field using the *fields* parameter - *\"&fields=verbose,locations\"*  as it is not part of the default, or verbose field sets. 
  'geoBbox': "geoBbox_example", // String | A geographic bounding box scoping a search to a geographic region. Order of latitude-longitude coordinates is north, west, south, east.   For example, filtering the Wellington region would be *\"&geo_bbox=-41,174,-42,175\"* 
  'fields': "fields_example", // String | Comma-separated whitelist of fields to be returned. The syntax *\"&fields=verbose\"* can be used to return the bulk of the fields, or you can customise which fields you are interested in, eg. *\"&fields=id,title,subject,collection,landing_url,locations\"*. 
  'sort': "sort_example", // String | Used to control the order of the results in conjunction with the *direction* field.   - *syndication_date* - is the creation date of the record within DigitalNZ, ie. when DigitalNZ first harvested the record.   - *date* - is the date metadata (if present) associated with the record.        To sort the search results with newest records at the top use: \"&sort=syndication_date&direction=desc\" 
  'direction': "'asc'", // String | Used in conjunction with *sort* to order the results  - *asc* - Ascending, oldest first.  - *desc* - Descending, newest first. 
  'page': 1, // Number | Specify which page of results to return.
  'perPage': 20, // Number | The number of records to return per page of search results.
  'facets': ["null"], // [String] | Shows a breakdown of record counts for the specified facets based on the current result set. In the [DigitalNZ search interface](https://digitalnz.org/records) these facets are used to list the values filterable for each field. A comma-separated list will return multiple facets in one call. 
  'facetsPage': 56, // Number | This value specifies which page of facet results to return. Allowing pagination through large lists of facet values.
  'facetsPerPage': 10, // Number | The number of facets to return per page of facet results.
  'excludeFiltersFromFacets': false // Boolean | This field can be used when filtering into some facets, to maintain the context of the wider facet values. A common use case is to allow the results of a search to be filtered down into a specific category (eg Audio), while still showing the other possible filter options as facet counts (eg. Images, Audio, Video, etc). Setting this to 'true' will not effect the search results returned but will ignore all search filters (eg. \"and[category]=Audio\") when calculating the facet counts.  
};
apiInstance.recordsFormatGet(format, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **String**| Note - There is a small difference with some field names in the response between JSON and XML.   When a field name has more than one word, JSON format will separate the words with an underscore, eg. \&quot;content_partner\&quot;, whereas XML uses a hyphenated naming convention, eg. \&quot;content-partner\&quot;.  | 
 **authenticationToken** | **String**| The DigitalNZ API no longer requires a key to access public content. However, if you plan on using the API regularly, expect to be a high volume consumer or are planning on creating an application, we encourage you to use an API key so that we can: - provide targeted help and support - increase your query throughput (by negotiation) - notify you directly of changes to the API - gather usage metrics to help improve the service    API requests that do not pass a valid API key/token are treated as unauthenticated. A maximum rate limit applies across all unauthenticated requests. This rate limit is in place to protect the service from overuse, resulting in unsustainable costs, or potential attack.  **Getting an API key**   [Create a DigitalNZ account](https://digitalnz.org/sign_up), log in and select \&quot;[my API key](https://digitalnz.org/api_keys/edit)\&quot; from your username drop-down menu (on the right hand side)&#39;. The key is a long string of jumbled letters and numbers (hash) that is unique to you. You are required to keep the key secret. (Refer to the [Developer API Terms of Use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use) for more information).  **Using an API key**   When you make a call to the API you&#39;ll need to pass the key in a custom HTTP header: ‘Authentication-Token’. For example, a query using the ‘curl’ command might look like the following (where ‘{YOUR_API_KEY}’ is replaced with a valid API key):  &#x60;curl -H \&quot;Authentication-Token:{YOUR_API_KEY}\&quot; http://api.digitalnz.org/v3/records.json?text&#x3D;kiwi&#x60;  | [optional] 
 **text** | **String**| This field enables queries based on one or more search terms and provides the functionality of the main search box on [digitalnz.org](https://digitalnz.org). Search terms can be combined with boolean operators (AND, OR).   A minus sign excludes certain terms, eg. \&quot;-horse\&quot;.   An asterisk (\\*) acts as a wildcard, eg. \&quot;ted*\&quot;.   Multiple search terms are combined with an AND by default.   Examples: &#x60;\&quot;moustache\&quot;&#x60;, &#x60;\&quot;Wanganui OR Whanganui\&quot;&#x60;,  &#x60;\&quot;-paperspast\&quot;&#x60;, &#x60;\&quot;ted*\&quot;&#x60;  | [optional] 
 **andCategory** | **String**| These are the same categories that are used across the tabs in [digitalnz.org](https://digitalnz.org/records?text&#x3D;&amp;tab&#x3D;Videos) | [optional] 
 **andContentPartner** | **String**| Allows filtering for records from a particular Content Partner.   Examples: &#x60;\&quot;Ministry for Culture and Heritage\&quot;&#x60; &#x60;\&quot;Trove\&quot;&#x60; &#x60;\&quot;V.C. Browne &amp; Son\&quot;&#x60;    *Tip* - To see a list of Content Partners available for filtering use the *facets* parameter, eg. *\&quot;&amp;facets&#x3D;content_partner\&quot;*.    | [optional] 
 **andPrimaryCollection** | **String**| Allows filtering for records from a particular *primary_collection*.   Examples: &#x60;\&quot;Puke Ariki\&quot;&#x60; &#x60;\&quot;NZHistory\&quot;&#x60; &#x60;\&quot;TAPUHI\&quot;&#x60;      *Tip* - To see a list of Primary_Collections available for filtering use the *facets* parameter, eg. *\&quot;&amp;facets&#x3D;primary_collection\&quot;*.     | [optional] 
 **andCollection** | **String**| Allows filtering for records from a particular Collection. Collections can be thought of as sub-collections or groupings under Primary_Collections.   Examples: &#x60;\&quot;Music 101\&quot;&#x60; &#x60;\&quot;Mollusks\&quot;&#x60; &#x60;\&quot;Wairarapa Daily Times\&quot;&#x60;    *Tip* - To see a list of Collections available for filtering use the *facets* parameter, eg. *\&quot;&amp;facets&#x3D;collection\&quot;*.   | [optional] 
 **andUsage** | **String**|  | [optional] 
 **andSubject** | **String**| Examples: &#x60;\&quot;Cats\&quot;&#x60; &#x60;\&quot;Weddings\&quot;&#x60; &#x60;\&quot;climb*\&quot;&#x60;  | [optional] 
 **andDcType** | **String**| Examples: &#x60;\&quot;Conference item\&quot;&#x60; &#x60;\&quot;Magazines\&quot;&#x60;  | [optional] 
 **andFormat** | **String**| Examples: &#x60;\&quot;Photolithographs\&quot;&#x60; &#x60;\&quot;Glass*\&quot;&#x60;  | [optional] 
 **andPlacename** | **String**| This field can be used for text-based location search. For a more advanced coordinate-based search, see the \&quot;geo_bbox\&quot; field below.   Examples: &#x60;\&quot;Scott Base\&quot;&#x60; &#x60;\&quot;Wainuiomata\&quot;&#x60; &#x60;\&quot;castle*\&quot;&#x60;  | [optional] 
 **andCreator** | **String**| Examples: &#x60;\&quot;Revelle Jackson\&quot;&#x60; &#x60;\&quot;Nicholas Chevalier\&quot;&#x60; &#x60;\&quot;Rita Angus\&quot;&#x60;  | [optional] 
 **andTitle** | **String**| Examples: &#x60;\&quot;Pukeko\&quot;&#x60; &#x60;\&quot;Club\&quot;&#x60; &#x60;\&quot;Break*\&quot;&#x60;\&quot;  | [optional] 
 **andDate** | **String**| This field can be useful for querying and sorting (see the &#39;sort&#39; param further down). But it should be noted that, as with some other fields, **not all records have date metadata associated**. There is good coverage of date metadata within certain collections, but there are plenty with no date information at all. So, if you query for records from a specific date you may get some matching results, but might also be missing other potentially relevant records that don&#39;t have date metadata available.   Example: &#x60;\&quot;1970-12-25\&quot;&#x60;  *Tip* - There is a related (but not searchable) field that is returned on each record (where available), that often has a more human readable version of the date information, called &#39;display_date&#39;.  | [optional] 
 **andYear** | **String**| This field allows searching specifically by year. The metadata is derived from the same date information that is searchable and returned in the date field. It is possible to search across a range using syntax the following syntax &#x60;[{start year} TO {end year}]&#x60;.   Example: &#x60;\&quot;1893\&quot;&#x60; &#x60;\&quot;[1982 TO 1987]\&quot;&#x60;  | [optional] 
 **andDecade** | **String**| This field allows searching specifically by decade. The metadata is derived from the same date information that is searchable and returned in the date field.   Example: &#x60;\&quot;1850\&quot;&#x60; &#x60;\&quot;1990\&quot;&#x60;  | [optional] 
 **andCentury** | **String**| This field allows searching specifically by century. The metadata is derived from the same date information that is searchable and returned in the date field.   Example: &#x60;\&quot;1900\&quot;&#x60; &#x60;\&quot;2000\&quot;&#x60;  | [optional] 
 **withoutFilterField** | **String**| All of the above &#x60;and[___][]&#x60; filters in this document are also able to be used with this syntax to exclude specific matches. For example to exclude Papers Past content &#x60;&amp;without[primary_collection]&#x3D;Papers+Past&#x60;  | [optional] 
 **andOrFilterField** | **String**| All of the above &#x60;and[___][]&#x60; filters in this document are also able to be used with the &#x60;and[or][___][]&#x60; syntax to allow multi-select *OR* queries within one field.   Basic example:  - To filter your results to only those with a category or Audio or Videos:    &#x60;&amp;and[or][category][]&#x3D;Audio&amp;and[or][category][]&#x3D;Videos&#x60;     In order to combine *OR* filters across multiple fields the syntax needs to be nested as follows   Nested examples:   - To search for *(year is 2014 OR 2015) AND (primary_collection is TAPUHI OR Public Address)*    &#x60;&amp;and[or][year][]&#x3D;2015&amp;and[or][year][]&#x3D;2014&amp;and[and][or][primary_collection][]&#x3D;TAPUHI&amp;and[and][or][primary_collection][]&#x3D;Public+Address&#x60;    - To search for *(category is Images OR Video) AND (subject is cat OR cats)*    &#x60;&amp;and[or][category][]&#x3D;Images&amp;and[or][category][]&#x3D;Videos&amp;and[and][or][subject][]&#x3D;cat&amp;and[and][or][subject][]&#x3D;cats&#x60;    | [optional] 
 **andIsCommercialUse** | **Boolean**| Some DigitalNZ partners offer their metadata for use in commercial applications. This content can be identified through the *is_commercial_use* flag. Only API results where the *is_commercial_use* field set to True can be used for commercial purposes. Check out the [terms of use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use#commercial_use_terms) for more information.  | [optional] 
 **andHasLargeThumbnailUrl** | **String**| Filters results to only those records that have an image available in the *large_thumbnail_url* field.   **Note:** There is an issue with this field where, in order to get results, it needs to be specified with \&quot;Y\&quot; or not specified at all.  | [optional] 
 **andHasLatLng** | **Boolean**| Filters results to only those records that have latitude and longitude coordinates present in the metadata.    *Tip* - To see the location metadata you&#39;ll need to specifically request that field using the *fields* parameter - *\&quot;&amp;fields&#x3D;verbose,locations\&quot;*  as it is not part of the default, or verbose field sets.  | [optional] 
 **geoBbox** | **String**| A geographic bounding box scoping a search to a geographic region. Order of latitude-longitude coordinates is north, west, south, east.   For example, filtering the Wellington region would be *\&quot;&amp;geo_bbox&#x3D;-41,174,-42,175\&quot;*  | [optional] 
 **fields** | **String**| Comma-separated whitelist of fields to be returned. The syntax *\&quot;&amp;fields&#x3D;verbose\&quot;* can be used to return the bulk of the fields, or you can customise which fields you are interested in, eg. *\&quot;&amp;fields&#x3D;id,title,subject,collection,landing_url,locations\&quot;*.  | [optional] 
 **sort** | **String**| Used to control the order of the results in conjunction with the *direction* field.   - *syndication_date* - is the creation date of the record within DigitalNZ, ie. when DigitalNZ first harvested the record.   - *date* - is the date metadata (if present) associated with the record.        To sort the search results with newest records at the top use: \&quot;&amp;sort&#x3D;syndication_date&amp;direction&#x3D;desc\&quot;  | [optional] 
 **direction** | **String**| Used in conjunction with *sort* to order the results  - *asc* - Ascending, oldest first.  - *desc* - Descending, newest first.  | [optional] [default to &#39;asc&#39;]
 **page** | **Number**| Specify which page of results to return. | [optional] [default to 1]
 **perPage** | **Number**| The number of records to return per page of search results. | [optional] [default to 20]
 **facets** | [**[String]**](String.md)| Shows a breakdown of record counts for the specified facets based on the current result set. In the [DigitalNZ search interface](https://digitalnz.org/records) these facets are used to list the values filterable for each field. A comma-separated list will return multiple facets in one call.  | [optional] 
 **facetsPage** | **Number**| This value specifies which page of facet results to return. Allowing pagination through large lists of facet values. | [optional] 
 **facetsPerPage** | **Number**| The number of facets to return per page of facet results. | [optional] [default to 10]
 **excludeFiltersFromFacets** | **Boolean**| This field can be used when filtering into some facets, to maintain the context of the wider facet values. A common use case is to allow the results of a search to be filtered down into a specific category (eg Audio), while still showing the other possible filter options as facet counts (eg. Images, Audio, Video, etc). Setting this to &#39;true&#39; will not effect the search results returned but will ignore all search filters (eg. \&quot;and[category]&#x3D;Audio\&quot;) when calculating the facet counts.   | [optional] [default to false]

### Return type

[**RecordsFormatGet200Response**](RecordsFormatGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## recordsRecordIdFormatGet

> Record recordsRecordIdFormatGet(recordId, format, opts)

View metadata associated with a single record.

If you know its &#x60;record_id&#x60; you can use this endpoint to view all metadata associated with that specific record. 

### Example

```javascript
import DigitalNzApi from 'digital_nz_api';
let defaultClient = DigitalNzApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DigitalNzApi.APICallsApi();
let recordId = 189089; // Number | Every record has a unique, persistent *record_id*.
let format = "format_example"; // String | Note - There is a small difference with some field names in the response between JSON and XML.   When a field name has more than one word, JSON format will separate the words with an underscore, eg. \"content_partner\", whereas XML uses a hyphenated naming convention, eg. \"content-partner\". 
let opts = {
  'authenticationToken': "authenticationToken_example", // String | The DigitalNZ API no longer requires a key to access public content. However, if you plan on using the API regularly, expect to be a high volume consumer or are planning on creating an application, we encourage you to use an API key so that we can: - provide targeted help and support - increase your query throughput (by negotiation) - notify you directly of changes to the API - gather usage metrics to help improve the service    API requests that do not pass a valid API key/token are treated as unauthenticated. A maximum rate limit applies across all unauthenticated requests. This rate limit is in place to protect the service from overuse, resulting in unsustainable costs, or potential attack.  **Getting an API key**   [Create a DigitalNZ account](https://digitalnz.org/sign_up), log in and select \"[my API key](https://digitalnz.org/api_keys/edit)\" from your username drop-down menu (on the right hand side)'. The key is a long string of jumbled letters and numbers (hash) that is unique to you. You are required to keep the key secret. (Refer to the [Developer API Terms of Use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use) for more information).  **Using an API key**   When you make a call to the API you'll need to pass the key in a custom HTTP header: ‘Authentication-Token’. For example, a query using the ‘curl’ command might look like the following (where ‘{YOUR_API_KEY}’ is replaced with a valid API key):  `curl -H \"Authentication-Token:{YOUR_API_KEY}\" http://api.digitalnz.org/v3/records.json?text=kiwi` 
  'fields': "fields_example" // String | Comma-separated whitelist of fields to be returned. The syntax *\"&fields=verbose\"* can be used to return the bulk of the fields, or you can customise which fields you are interested in, eg. *\"&fields=id,title,subject,collection,landing_url,locations\"*. 
};
apiInstance.recordsRecordIdFormatGet(recordId, format, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recordId** | **Number**| Every record has a unique, persistent *record_id*. | 
 **format** | **String**| Note - There is a small difference with some field names in the response between JSON and XML.   When a field name has more than one word, JSON format will separate the words with an underscore, eg. \&quot;content_partner\&quot;, whereas XML uses a hyphenated naming convention, eg. \&quot;content-partner\&quot;.  | 
 **authenticationToken** | **String**| The DigitalNZ API no longer requires a key to access public content. However, if you plan on using the API regularly, expect to be a high volume consumer or are planning on creating an application, we encourage you to use an API key so that we can: - provide targeted help and support - increase your query throughput (by negotiation) - notify you directly of changes to the API - gather usage metrics to help improve the service    API requests that do not pass a valid API key/token are treated as unauthenticated. A maximum rate limit applies across all unauthenticated requests. This rate limit is in place to protect the service from overuse, resulting in unsustainable costs, or potential attack.  **Getting an API key**   [Create a DigitalNZ account](https://digitalnz.org/sign_up), log in and select \&quot;[my API key](https://digitalnz.org/api_keys/edit)\&quot; from your username drop-down menu (on the right hand side)&#39;. The key is a long string of jumbled letters and numbers (hash) that is unique to you. You are required to keep the key secret. (Refer to the [Developer API Terms of Use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use) for more information).  **Using an API key**   When you make a call to the API you&#39;ll need to pass the key in a custom HTTP header: ‘Authentication-Token’. For example, a query using the ‘curl’ command might look like the following (where ‘{YOUR_API_KEY}’ is replaced with a valid API key):  &#x60;curl -H \&quot;Authentication-Token:{YOUR_API_KEY}\&quot; http://api.digitalnz.org/v3/records.json?text&#x3D;kiwi&#x60;  | [optional] 
 **fields** | **String**| Comma-separated whitelist of fields to be returned. The syntax *\&quot;&amp;fields&#x3D;verbose\&quot;* can be used to return the bulk of the fields, or you can customise which fields you are interested in, eg. *\&quot;&amp;fields&#x3D;id,title,subject,collection,landing_url,locations\&quot;*.  | [optional] 

### Return type

[**Record**](Record.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## recordsRecordIdMoreLikeThisFormatGet

> RecordsRecordIdMoreLikeThisFormatGet200Response recordsRecordIdMoreLikeThisFormatGet(recordId, format, opts)

The \&quot;More Like This\&quot; call returns similar records to the specified ID. 

This feature returns a set of search results that are similar (ie have similar metadata) to a specific record. 

### Example

```javascript
import DigitalNzApi from 'digital_nz_api';
let defaultClient = DigitalNzApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DigitalNzApi.APICallsApi();
let recordId = 35806021; // Number | Every record has a unique, persistent *record_id*.
let format = "format_example"; // String | Note - There is a small difference with some field names in the response between JSON and XML.   When a field name has more than one word, JSON format will separate the words with an underscore, eg. \"content_partner\", whereas XML uses a hyphenated naming convention, eg. \"content-partner\". 
let opts = {
  'authenticationToken': "authenticationToken_example", // String | The DigitalNZ API no longer requires a key to access public content. However, if you plan on using the API regularly, expect to be a high volume consumer or are planning on creating an application, we encourage you to use an API key so that we can: - provide targeted help and support - increase your query throughput (by negotiation) - notify you directly of changes to the API - gather usage metrics to help improve the service    API requests that do not pass a valid API key/token are treated as unauthenticated. A maximum rate limit applies across all unauthenticated requests. This rate limit is in place to protect the service from overuse, resulting in unsustainable costs, or potential attack.  **Getting an API key**   [Create a DigitalNZ account](https://digitalnz.org/sign_up), log in and select \"[my API key](https://digitalnz.org/api_keys/edit)\" from your username drop-down menu (on the right hand side)'. The key is a long string of jumbled letters and numbers (hash) that is unique to you. You are required to keep the key secret. (Refer to the [Developer API Terms of Use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use) for more information).  **Using an API key**   When you make a call to the API you'll need to pass the key in a custom HTTP header: ‘Authentication-Token’. For example, a query using the ‘curl’ command might look like the following (where ‘{YOUR_API_KEY}’ is replaced with a valid API key):  `curl -H \"Authentication-Token:{YOUR_API_KEY}\" http://api.digitalnz.org/v3/records.json?text=kiwi` 
  'fields': "fields_example", // String | Comma-separated whitelist of fields to be returned. The syntax *\"&fields=verbose\"* can be used to return the bulk of the fields, or you can customise which fields you are interested in, eg. *\"&fields=id,title,subject,collection,landing_url,locations\"*. 
  'mltFields': "mltFields_example", // String | Comma-separated list of fields used to evaluate relatedness. Available fields to compare are *title* and *subject*, eg *&mlt_fields=title,subject* or *&mlt_fields=title*. 
  'filtering': "filtering_example" // String | More Like This (MLT) queries can be filtered in the same ways as regular searches, using the same syntax outined in the GET /records call above. This enables things like scoping the related records to only return Images eg *&and[category]=Images*, or to only show related records from a specific content partner eg *&and[content_partner]=Puke+Ariki*. 
};
apiInstance.recordsRecordIdMoreLikeThisFormatGet(recordId, format, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recordId** | **Number**| Every record has a unique, persistent *record_id*. | 
 **format** | **String**| Note - There is a small difference with some field names in the response between JSON and XML.   When a field name has more than one word, JSON format will separate the words with an underscore, eg. \&quot;content_partner\&quot;, whereas XML uses a hyphenated naming convention, eg. \&quot;content-partner\&quot;.  | 
 **authenticationToken** | **String**| The DigitalNZ API no longer requires a key to access public content. However, if you plan on using the API regularly, expect to be a high volume consumer or are planning on creating an application, we encourage you to use an API key so that we can: - provide targeted help and support - increase your query throughput (by negotiation) - notify you directly of changes to the API - gather usage metrics to help improve the service    API requests that do not pass a valid API key/token are treated as unauthenticated. A maximum rate limit applies across all unauthenticated requests. This rate limit is in place to protect the service from overuse, resulting in unsustainable costs, or potential attack.  **Getting an API key**   [Create a DigitalNZ account](https://digitalnz.org/sign_up), log in and select \&quot;[my API key](https://digitalnz.org/api_keys/edit)\&quot; from your username drop-down menu (on the right hand side)&#39;. The key is a long string of jumbled letters and numbers (hash) that is unique to you. You are required to keep the key secret. (Refer to the [Developer API Terms of Use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use) for more information).  **Using an API key**   When you make a call to the API you&#39;ll need to pass the key in a custom HTTP header: ‘Authentication-Token’. For example, a query using the ‘curl’ command might look like the following (where ‘{YOUR_API_KEY}’ is replaced with a valid API key):  &#x60;curl -H \&quot;Authentication-Token:{YOUR_API_KEY}\&quot; http://api.digitalnz.org/v3/records.json?text&#x3D;kiwi&#x60;  | [optional] 
 **fields** | **String**| Comma-separated whitelist of fields to be returned. The syntax *\&quot;&amp;fields&#x3D;verbose\&quot;* can be used to return the bulk of the fields, or you can customise which fields you are interested in, eg. *\&quot;&amp;fields&#x3D;id,title,subject,collection,landing_url,locations\&quot;*.  | [optional] 
 **mltFields** | **String**| Comma-separated list of fields used to evaluate relatedness. Available fields to compare are *title* and *subject*, eg *&amp;mlt_fields&#x3D;title,subject* or *&amp;mlt_fields&#x3D;title*.  | [optional] 
 **filtering** | **String**| More Like This (MLT) queries can be filtered in the same ways as regular searches, using the same syntax outined in the GET /records call above. This enables things like scoping the related records to only return Images eg *&amp;and[category]&#x3D;Images*, or to only show related records from a specific content partner eg *&amp;and[content_partner]&#x3D;Puke+Ariki*.  | [optional] 

### Return type

[**RecordsRecordIdMoreLikeThisFormatGet200Response**](RecordsRecordIdMoreLikeThisFormatGet200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

