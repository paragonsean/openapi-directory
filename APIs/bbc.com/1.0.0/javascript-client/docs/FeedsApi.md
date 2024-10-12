# BbcNitroApi.FeedsApi

All URIs are relative to *https://programmes.api.bbc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listAvailability**](FeedsApi.md#listAvailability) | **GET** /availabilities | Discover details of on-demand availability for programmes and their versions
[**listBroadcasts**](FeedsApi.md#listBroadcasts) | **GET** /broadcasts | Build schedules and find metadata for TV and radio broadcasts
[**listGroups**](FeedsApi.md#listGroups) | **GET** /groups | Find metadata for curated groups: seasons, collections, galleries or franchises
[**listImages**](FeedsApi.md#listImages) | **GET** /images | Find metadata for images
[**listItems**](FeedsApi.md#listItems) | **GET** /items | Look inside programmes to find segments: chapters, tracks and more
[**listMasterbrands**](FeedsApi.md#listMasterbrands) | **GET** /master_brands | List all Master Brands
[**listPeople**](FeedsApi.md#listPeople) | **GET** /people | Find the people behind and in programmes: cast, crew, guests and more
[**listPips**](FeedsApi.md#listPips) | **GET** /pips | Look inside pips entities
[**listProgrammeDetails**](FeedsApi.md#listProgrammeDetails) | **GET** /programme_details | Exposes programme information for a single pid
[**listProgrammes**](FeedsApi.md#listProgrammes) | **GET** /programmes | Start here for programmes metadata: Brands, Series, Episodes and Clips
[**listPromotions**](FeedsApi.md#listPromotions) | **GET** /promotions | Discover metadata for content promotions
[**listSchedules**](FeedsApi.md#listSchedules) | **GET** /schedules | Build schedules and find metadata for TV and radio broadcasts and webcasts
[**listServices**](FeedsApi.md#listServices) | **GET** /services | Information about the linear services used for broadcast transmissions
[**listVersions**](FeedsApi.md#listVersions) | **GET** /versions | Metadata on editorial programme versions: original, signed, audio-described, etc



## listAvailability

> Nitro listAvailability(opts)

Discover details of on-demand availability for programmes and their versions

Discover details of on-demand availability for programmes and their versions

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'sort': "sort_example", // String | Sorts: * scheduled_start: sort chronologically by scheduled start time/date, ascending 
  'sortDirection': "sortDirection_example", // String | Sort direction
  'availability': ["null"], // [String] | filter for subset of availabilities
  'descendantsOf': ["null"], // [String] | filter for subset of availabilities that have PID as ancestor
  'mediaSet': ["null"], // [String] | filter for subset of availabilities with media set
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'territory': ["null"], // [String] | filter for availabilities in given territory
  'debug': true // Boolean | Turn on debug information (undocumented)
};
apiInstance.listAvailability(opts, (error, data, response) => {
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
 **sort** | **String**| Sorts: * scheduled_start: sort chronologically by scheduled start time/date, ascending  | [optional] 
 **sortDirection** | **String**| Sort direction | [optional] 
 **availability** | [**[String]**](String.md)| filter for subset of availabilities | [optional] 
 **descendantsOf** | [**[String]**](String.md)| filter for subset of availabilities that have PID as ancestor | [optional] 
 **mediaSet** | [**[String]**](String.md)| filter for subset of availabilities with media set | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **territory** | [**[String]**](String.md)| filter for availabilities in given territory | [optional] 
 **debug** | **Boolean**| Turn on debug information (undocumented) | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listBroadcasts

> Nitro listBroadcasts(opts)

Build schedules and find metadata for TV and radio broadcasts

Fetch metadata about linear Broadcasts and Services, allowing the generation of Television and Radio schedules and other datasets for broadcast items. Use /schedules instead of this feed as it is more efficient. Broadcasts will be deprecated in the future.

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'sort': "sort_example", // String | Sorts: * start_date: sort chronologically by scheduled start time/date, ascending 
  'sortDirection': "sortDirection_example", // String | Sort direction
  'mixin': ["null"], // [String] | Mixins: * titles: return ancestor programme titles 
  'authority': ["null"], // [String] | filter for subset of broadcasts that have given authority
  'descendantsOf': ["null"], // [String] | filter for subset of broadcasts that are descendants of the given programme PID
  'endFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | filter for subset of broadcasts that end on or later than the specified datetime
  'endTo': new Date("2013-10-20T19:20:30+01:00"), // Date | filter for subset of broadcasts that end on or earlier than the specified datetime
  'format': ["null"], // [String] | filter for subset of broadcasts that are classified in the given format ID
  'genre': ["null"], // [String] | filter for subset of broadcasts that are classified in the given genre ID
  'id': ["null"], // [String] | filter for subset of broadcasts that have given identifier
  'item': ["null"], // [String] | filter for subset of broadcasts with the given item performed on it
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'people': "people_example", // String | filter for subset of broadcasts that have given contributor
  'pid': ["null"], // [String] | filter for subset of broadcasts having given PID
  'q': "q_example", // String | filter for subset of broadcasts matching supplied keyword/phrase (boolean operators permitted)
  'scheduleDay': new Date("2013-10-20"), // Date | filter for subset of broadcasts that start on the specified day (BBC time)
  'scheduleDayFrom': new Date("2013-10-20"), // Date | filter for subset of broadcasts that start on or after the specified day (BBC time)
  'scheduleDayTo': new Date("2013-10-20"), // Date | filter for subset of broadcasts that start on or before the specified day (BBC time)
  'serviceMasterBrand': ["null"], // [String] | filter for subset of broadcasts with given service master brand
  'sid': ["null"], // [String] | filter for subset of broadcasts that are on the specified linear service
  'startFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | filter for subset of broadcasts that start on or later than the specified datetime
  'startTo': new Date("2013-10-20T19:20:30+01:00"), // Date | filter for subset of broadcasts that start on or earlier than the specified datetime
  'version': ["null"] // [String] | filter for subset of broadcasts with given PID as their parent version
};
apiInstance.listBroadcasts(opts, (error, data, response) => {
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
 **sort** | **String**| Sorts: * start_date: sort chronologically by scheduled start time/date, ascending  | [optional] 
 **sortDirection** | **String**| Sort direction | [optional] 
 **mixin** | [**[String]**](String.md)| Mixins: * titles: return ancestor programme titles  | [optional] 
 **authority** | [**[String]**](String.md)| filter for subset of broadcasts that have given authority | [optional] 
 **descendantsOf** | [**[String]**](String.md)| filter for subset of broadcasts that are descendants of the given programme PID | [optional] 
 **endFrom** | **Date**| filter for subset of broadcasts that end on or later than the specified datetime | [optional] 
 **endTo** | **Date**| filter for subset of broadcasts that end on or earlier than the specified datetime | [optional] 
 **format** | [**[String]**](String.md)| filter for subset of broadcasts that are classified in the given format ID | [optional] 
 **genre** | [**[String]**](String.md)| filter for subset of broadcasts that are classified in the given genre ID | [optional] 
 **id** | [**[String]**](String.md)| filter for subset of broadcasts that have given identifier | [optional] 
 **item** | [**[String]**](String.md)| filter for subset of broadcasts with the given item performed on it | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **people** | **String**| filter for subset of broadcasts that have given contributor | [optional] 
 **pid** | [**[String]**](String.md)| filter for subset of broadcasts having given PID | [optional] 
 **q** | **String**| filter for subset of broadcasts matching supplied keyword/phrase (boolean operators permitted) | [optional] 
 **scheduleDay** | **Date**| filter for subset of broadcasts that start on the specified day (BBC time) | [optional] 
 **scheduleDayFrom** | **Date**| filter for subset of broadcasts that start on or after the specified day (BBC time) | [optional] 
 **scheduleDayTo** | **Date**| filter for subset of broadcasts that start on or before the specified day (BBC time) | [optional] 
 **serviceMasterBrand** | [**[String]**](String.md)| filter for subset of broadcasts with given service master brand | [optional] 
 **sid** | [**[String]**](String.md)| filter for subset of broadcasts that are on the specified linear service | [optional] 
 **startFrom** | **Date**| filter for subset of broadcasts that start on or later than the specified datetime | [optional] 
 **startTo** | **Date**| filter for subset of broadcasts that start on or earlier than the specified datetime | [optional] 
 **version** | [**[String]**](String.md)| filter for subset of broadcasts with given PID as their parent version | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listGroups

> Nitro listGroups(opts)

Find metadata for curated groups: seasons, collections, galleries or franchises

Long-lived curated collections of programmes and more, including Collections, Seasons, Franchises and Galleries

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'sort': "sort_example", // String | Sorts: * pid: sort alphabetically by PID 
  'sortDirection': "sortDirection_example", // String | Sort direction
  'mixin': ["null"], // [String] | Mixins: * alternate_images: mixin to return the alternate images for a group * group_for: mixin to return links to programme entities that group belongs to * images: mixin to add image information for a group * related_links: mixin to return related links for the group 
  'forDescendantsOf': "forDescendantsOf_example", // String | filter for groups related to given programme or its descendants
  'forProgramme': "forProgramme_example", // String | filter for subset of groups directly related to a given programme
  'group': "group_example", // String | filter for subset of groups which belong to the given group pid
  'groupType': ["null"], // [String] | filter for subset of groups that have the given group type
  'member': "member_example", // String | filter for subset of groups which contain an entity with the given pid as a member
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerId': ["null"], // [String] | filter for groups by partner ID
  'partnerPid': ["'s0000001'"], // [String] | filter for groups by partner PID
  'pid': ["null"], // [String] | filter for subset of seasons, collections, galleries or franchises having given PID
  'q': "q_example", // String | filter for subset of groups matching supplied keyword/phrase (boolean operators permitted)
  'embargoed': "embargoed_example" // String | Control return of embargoed items (undocumented)
};
apiInstance.listGroups(opts, (error, data, response) => {
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
 **sort** | **String**| Sorts: * pid: sort alphabetically by PID  | [optional] 
 **sortDirection** | **String**| Sort direction | [optional] 
 **mixin** | [**[String]**](String.md)| Mixins: * alternate_images: mixin to return the alternate images for a group * group_for: mixin to return links to programme entities that group belongs to * images: mixin to add image information for a group * related_links: mixin to return related links for the group  | [optional] 
 **forDescendantsOf** | **String**| filter for groups related to given programme or its descendants | [optional] 
 **forProgramme** | **String**| filter for subset of groups directly related to a given programme | [optional] 
 **group** | **String**| filter for subset of groups which belong to the given group pid | [optional] 
 **groupType** | [**[String]**](String.md)| filter for subset of groups that have the given group type | [optional] 
 **member** | **String**| filter for subset of groups which contain an entity with the given pid as a member | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerId** | [**[String]**](String.md)| filter for groups by partner ID | [optional] 
 **partnerPid** | [**[String]**](String.md)| filter for groups by partner PID | [optional] 
 **pid** | [**[String]**](String.md)| filter for subset of seasons, collections, galleries or franchises having given PID | [optional] 
 **q** | **String**| filter for subset of groups matching supplied keyword/phrase (boolean operators permitted) | [optional] 
 **embargoed** | **String**| Control return of embargoed items (undocumented) | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listImages

> Nitro listImages(opts)

Find metadata for images

Find metadata for images, particularly those in galleries

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'sort': "sort_example", // String | Sorts: * group_position: sort numerically by position, ascending only * pid: sort alphabetically by PID 
  'sortDirection': "sortDirection_example", // String | Sort direction
  'group': "group_example", // String | filter for images belonging to the given group (i.e. Gallery)
  'imageType': ["null"], // [String] | filter for images by type
  'isAlternateImageFor': "isAlternateImageFor_example", // String | filter for alternate images by entity PID
  'isImageFor': "isImageFor_example", // String | filter for images by entity PID
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerId': ["null"], // [String] | filter for images by partner ID
  'partnerPid': ["'s0000001'"], // [String] | filter for images by partner PID
  'pid': ["null"], // [String] | filter for subset of images having given PID
  'q': "q_example", // String | filter for subset of images matching supplied keyword/phrase (boolean operators permitted)
  'embargoed': "embargoed_example" // String | Control return of embargoed items (undocumented)
};
apiInstance.listImages(opts, (error, data, response) => {
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
 **sort** | **String**| Sorts: * group_position: sort numerically by position, ascending only * pid: sort alphabetically by PID  | [optional] 
 **sortDirection** | **String**| Sort direction | [optional] 
 **group** | **String**| filter for images belonging to the given group (i.e. Gallery) | [optional] 
 **imageType** | [**[String]**](String.md)| filter for images by type | [optional] 
 **isAlternateImageFor** | **String**| filter for alternate images by entity PID | [optional] 
 **isImageFor** | **String**| filter for images by entity PID | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerId** | [**[String]**](String.md)| filter for images by partner ID | [optional] 
 **partnerPid** | [**[String]**](String.md)| filter for images by partner PID | [optional] 
 **pid** | [**[String]**](String.md)| filter for subset of images having given PID | [optional] 
 **q** | **String**| filter for subset of images matching supplied keyword/phrase (boolean operators permitted) | [optional] 
 **embargoed** | **String**| Control return of embargoed items (undocumented) | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listItems

> Nitro listItems(opts)

Look inside programmes to find segments: chapters, tracks and more

Look inside programmes to find segments: chapters, tracks and more

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'sort': "sort_example", // String | Sorts: * pid: sort by pid, descending 
  'sortDirection': "sortDirection_example", // String | Sort direction
  'mixin': ["null"], // [String] | Mixins: * contributions: mixin to return information about contributors to items * images: mixin to add image information for an item * offset: mixin to return programme segment offsets, works in conjunction with programme filter * play_event: mixin to return programme segment events, works in conjunction with programme or segment_event filters 
  'authority': "authority_example", // String | filter for subset of items that have an ID issued by the given authority
  'id': ["null"], // [String] | filter for subset of items having given ID
  'idType': "idType_example", // String | filter for subset of items that have given an ID of the given type
  'itemType': ["null"], // [String] | filter for specific type(s) of items
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerId': ["null"], // [String] | filter for items by partner ID
  'partnerPid': ["'s0000001'"], // [String] | filter for items by partner PID
  'people': "people_example", // String | filter for subset of items that have specified person involved
  'pid': ["null"], // [String] | filter for subset of items matching one of the given PIDs
  'programme': "programme_example", // String | filter for subset of items that are part of the given programme
  'q': "q_example", // String | filter for subset of items matching supplied keyword/phrase (boolean operators permitted)
  'segmentEvent': "segmentEvent_example" // String | filter for item with the given segment_event
};
apiInstance.listItems(opts, (error, data, response) => {
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
 **sort** | **String**| Sorts: * pid: sort by pid, descending  | [optional] 
 **sortDirection** | **String**| Sort direction | [optional] 
 **mixin** | [**[String]**](String.md)| Mixins: * contributions: mixin to return information about contributors to items * images: mixin to add image information for an item * offset: mixin to return programme segment offsets, works in conjunction with programme filter * play_event: mixin to return programme segment events, works in conjunction with programme or segment_event filters  | [optional] 
 **authority** | **String**| filter for subset of items that have an ID issued by the given authority | [optional] 
 **id** | [**[String]**](String.md)| filter for subset of items having given ID | [optional] 
 **idType** | **String**| filter for subset of items that have given an ID of the given type | [optional] 
 **itemType** | [**[String]**](String.md)| filter for specific type(s) of items | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerId** | [**[String]**](String.md)| filter for items by partner ID | [optional] 
 **partnerPid** | [**[String]**](String.md)| filter for items by partner PID | [optional] 
 **people** | **String**| filter for subset of items that have specified person involved | [optional] 
 **pid** | [**[String]**](String.md)| filter for subset of items matching one of the given PIDs | [optional] 
 **programme** | **String**| filter for subset of items that are part of the given programme | [optional] 
 **q** | **String**| filter for subset of items matching supplied keyword/phrase (boolean operators permitted) | [optional] 
 **segmentEvent** | **String**| filter for item with the given segment_event | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listMasterbrands

> Nitro listMasterbrands(opts)

List all Master Brands

List all Master Brands

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'sort': "sort_example", // String | Sorts: * mid: sort by mid, ascending 
  'sortDirection': "sortDirection_example", // String | Sort direction
  'mixin': ["null"], // [String] | Mixins: * images: mixin to add image information for a masterbrand 
  'mid': ["null"], // [String] | filter for subset of masterbrands that have given identifier
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerId': ["null"], // [String] | filter for masterbrands by partner ID
  'partnerPid': ["'s0000001'"], // [String] | filter for masterbrands by partner PID
  'q': "q_example" // String | filter for subset of masterbrands matching supplied keyword/phrase (boolean operators permitted)
};
apiInstance.listMasterbrands(opts, (error, data, response) => {
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
 **sort** | **String**| Sorts: * mid: sort by mid, ascending  | [optional] 
 **sortDirection** | **String**| Sort direction | [optional] 
 **mixin** | [**[String]**](String.md)| Mixins: * images: mixin to add image information for a masterbrand  | [optional] 
 **mid** | [**[String]**](String.md)| filter for subset of masterbrands that have given identifier | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerId** | [**[String]**](String.md)| filter for masterbrands by partner ID | [optional] 
 **partnerPid** | [**[String]**](String.md)| filter for masterbrands by partner PID | [optional] 
 **q** | **String**| filter for subset of masterbrands matching supplied keyword/phrase (boolean operators permitted) | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listPeople

> Nitro listPeople(opts)

Find the people behind and in programmes: cast, crew, guests and more

The People feed allows you to search for the people and groups that contribute to programmes. This is the starting point for cast and crew credits, as well as finding contributors using external IDs (such as Wikipedia URLs)

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'authority': "authority_example", // String | filter for subset of people that have an ID issued by the given authority
  'hasExternalId': ["null"], // [String] | filter for people who have an external identifier
  'id': ["null"], // [String] | filter for subset of people having given ID
  'idType': "idType_example", // String | filter for subset of people that have given an ID of the given type
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerId': ["null"], // [String] | filter for people by partner ID
  'partnerPid': ["'s0000001'"], // [String] | filter for people by partner PID
  'pid': ["null"], // [String] | filter for subset of people having given PID
  'programme': "programme_example", // String | filter for subset of people that have contributed to the given programme pid
  'q': "q_example" // String | filter for subset of people matching supplied keyword/phrase (boolean operators permitted)
};
apiInstance.listPeople(opts, (error, data, response) => {
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
 **authority** | **String**| filter for subset of people that have an ID issued by the given authority | [optional] 
 **hasExternalId** | [**[String]**](String.md)| filter for people who have an external identifier | [optional] 
 **id** | [**[String]**](String.md)| filter for subset of people having given ID | [optional] 
 **idType** | **String**| filter for subset of people that have given an ID of the given type | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerId** | [**[String]**](String.md)| filter for people by partner ID | [optional] 
 **partnerPid** | [**[String]**](String.md)| filter for people by partner PID | [optional] 
 **pid** | [**[String]**](String.md)| filter for subset of people having given PID | [optional] 
 **programme** | **String**| filter for subset of people that have contributed to the given programme pid | [optional] 
 **q** | **String**| filter for subset of people matching supplied keyword/phrase (boolean operators permitted) | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listPips

> Nitro listPips(opts)

Look inside pips entities

Look inside pips entities

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'q': "q_example" // String | filter for subset of programmes matching supplied keyword/phrase (boolean operators permitted)
};
apiInstance.listPips(opts, (error, data, response) => {
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
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **q** | **String**| filter for subset of programmes matching supplied keyword/phrase (boolean operators permitted) | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listProgrammeDetails

> Nitro listProgrammeDetails(opts)

Exposes programme information for a single pid

Exposes programme information for a single pid

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerPid': "partnerPid_example", // String | Filter for programme information by partner PID
  'pid': "pid_example" // String | Filter for programme information for the provided PID
};
apiInstance.listProgrammeDetails(opts, (error, data, response) => {
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
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerPid** | **String**| Filter for programme information by partner PID | [optional] 
 **pid** | **String**| Filter for programme information for the provided PID | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listProgrammes

> Nitro listProgrammes(opts)

Start here for programmes metadata: Brands, Series, Episodes and Clips

Fetch metadata about Programmes (brands, series, episodes, clips). By applying different filter restrictions this feed can be used in many ways, for example to retrieve all series belonging to a brand, all the episodes and/or clips for a specific series, or any TLEO objects for a masterbrand. Other filters permit restricting to specific formats and/or genres, and you can request specific versions (for example Signed or Audio-Described). Parameters may be combined in any way suitable for your application.

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'sort': "sort_example", // String | Sorts: * group_position: sort numerically by position in group, ascending * pid: sort alphabetically by PID, descending * position: sort numerically by position, ascending * promotion: sort by promotion rank, ascending * release_date: sort chronologically by release date, descending * relevance: sort by weighting of search term (use with q parameter) * scheduled_start: sort chronologically by scheduled start time/date, ascending * strict_title: sort alphabetically by title, ascending * title: sort by title librarian style (ignoring leading 'The', 'A', etc), ascending * tree: sort by root pid and then preorder tree sort. Requires entities to have release date. 
  'sortDirection': "sortDirection_example", // String | Sort direction
  'mixin': ["null"], // [String] | Mixins: * alternate_images: mixin to return the alternate images for a programme * ancestor_titles: mixin to return ancestor programme titles * availability: mixin to return programme availability information * available_simulcasts: mixin to return information about programmes that are currently available as simulcasts * available_versions: mixin to return information about programmes that are currently available on demand * available_webcasts: mixin to return information about programmes that are currently available as webcasts * contributions: mixin to return information about contributors to a programme * duration: mixin to return original version duration in programme concept entities * genre_groupings: mixin to return list of genre groupings * genre_groups: mixin to return list of genre groups * images: mixin to add image information for a programme * is_embeddable: mixin to add embeddable information for a programme * previous_next: mixin to return the programmes which appear before and after a programme (as determined by the sort applied in the request) * programme_type: mixin to return the programme type * related_links: mixin to return information about related links to a programme * titles: mixin to return ancestor programme titles * versions_availability: mixin to return information about programmes that are currently available 
  'audioDescribed': ["null"], // [String] | filter for subset of programmes that are audio-described
  'availability': ["null"], // [String] | filter for subset of programmes that have availability
  'availabilityEntityType': ["null"], // [String] | additional filter when availability=available
  'availabilityFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | filter for subset of programmes that are available after or at the specified datetime
  'availabilityType': ["null"], // [String] | filter for a subset of programmes that are available for a given type
  'childrenOf': ["null"], // [String] | filter for subset of programmes that have PID as immediate parent
  'descendantsOf': ["null"], // [String] | filter for subset of programmes that have PID as ancestor
  'duration': ["null"], // [String] | filter for subset of programmes that have given duration
  'entityType': ["null"], // [String] | filter for subset of programmes that have given entity type
  'format': ["null"], // [String] | filter for subset of programmes with format
  'genre': ["null"], // [String] | filter for subset of programmes with genre
  'group': "group_example", // String | filter for subset of programmes which belong to the given group pid
  'initialLetter': "initialLetter_example", // String | filter for subset of programmes with title beginning with initial letter librarian style (ignoring leading 'The', 'An' (Welsh), etc) 0-9 a-z
  'initialLetterEnd': "initialLetterEnd_example", // String | Programmes with (librarian) titles whose initial letter is equal/before given letter. Use with initial_letter_start for a range
  'initialLetterStart': "initialLetterStart_example", // String | Programmes with (librarian) titles whose initial letter is equal/after given letter. Use with initial_letter_end for range.
  'initialLetterStrict': ["null"], // [String] | filter for subset of programmes with title beginning with initial letter
  'item': ["null"], // [String] | filter for subset of programmes with linked to versions which have the given item pids
  'masterBrand': ["null"], // [String] | filter for subset of programmes with master_brand
  'mediaSet': "mediaSet_example", // String | filter for subset of programmes with media set
  'mediaType': ["null"], // [String] | filter for subset of programmes with media type
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerId': ["null"], // [String] | filter for programmes by partner ID
  'partnerPid': ["'s0000001'"], // [String] | filter for programmes by partner PID
  'paymentType': ["null"], // [String] | filter for a subset of programmes that are of the given payment_type
  'people': "people_example", // String | filter for subset of programmes with contributions by given people PID
  'pid': ["null"], // [String] | filter for subset of programmes having given PID
  'promotedFor': "promotedFor_example", // String | filter for subset of programmes which are promoted for given service
  'q': "q_example", // String | filter for subset of programmes matching supplied keyword/phrase (boolean operators permitted)
  'signed': ["null"], // [String] | filter for subset of programmes that are signed
  'tagName': "tagName_example", // String | filter for subset of programmes with tag
  'tagScheme': "tagScheme_example", // String | filter for subset of programmes with a tag
  'tleo': ["null"], // [String] | filter for subset of programmes that are TLEOs
  'version': ["null"], // [String] | filter for subset of programmes with given PID as one of their versions
  'embargoed': "embargoed_example" // String | Control return of embargoed items (undocumented)
};
apiInstance.listProgrammes(opts, (error, data, response) => {
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
 **sort** | **String**| Sorts: * group_position: sort numerically by position in group, ascending * pid: sort alphabetically by PID, descending * position: sort numerically by position, ascending * promotion: sort by promotion rank, ascending * release_date: sort chronologically by release date, descending * relevance: sort by weighting of search term (use with q parameter) * scheduled_start: sort chronologically by scheduled start time/date, ascending * strict_title: sort alphabetically by title, ascending * title: sort by title librarian style (ignoring leading &#39;The&#39;, &#39;A&#39;, etc), ascending * tree: sort by root pid and then preorder tree sort. Requires entities to have release date.  | [optional] 
 **sortDirection** | **String**| Sort direction | [optional] 
 **mixin** | [**[String]**](String.md)| Mixins: * alternate_images: mixin to return the alternate images for a programme * ancestor_titles: mixin to return ancestor programme titles * availability: mixin to return programme availability information * available_simulcasts: mixin to return information about programmes that are currently available as simulcasts * available_versions: mixin to return information about programmes that are currently available on demand * available_webcasts: mixin to return information about programmes that are currently available as webcasts * contributions: mixin to return information about contributors to a programme * duration: mixin to return original version duration in programme concept entities * genre_groupings: mixin to return list of genre groupings * genre_groups: mixin to return list of genre groups * images: mixin to add image information for a programme * is_embeddable: mixin to add embeddable information for a programme * previous_next: mixin to return the programmes which appear before and after a programme (as determined by the sort applied in the request) * programme_type: mixin to return the programme type * related_links: mixin to return information about related links to a programme * titles: mixin to return ancestor programme titles * versions_availability: mixin to return information about programmes that are currently available  | [optional] 
 **audioDescribed** | [**[String]**](String.md)| filter for subset of programmes that are audio-described | [optional] 
 **availability** | [**[String]**](String.md)| filter for subset of programmes that have availability | [optional] 
 **availabilityEntityType** | [**[String]**](String.md)| additional filter when availability&#x3D;available | [optional] 
 **availabilityFrom** | **Date**| filter for subset of programmes that are available after or at the specified datetime | [optional] 
 **availabilityType** | [**[String]**](String.md)| filter for a subset of programmes that are available for a given type | [optional] 
 **childrenOf** | [**[String]**](String.md)| filter for subset of programmes that have PID as immediate parent | [optional] 
 **descendantsOf** | [**[String]**](String.md)| filter for subset of programmes that have PID as ancestor | [optional] 
 **duration** | [**[String]**](String.md)| filter for subset of programmes that have given duration | [optional] 
 **entityType** | [**[String]**](String.md)| filter for subset of programmes that have given entity type | [optional] 
 **format** | [**[String]**](String.md)| filter for subset of programmes with format | [optional] 
 **genre** | [**[String]**](String.md)| filter for subset of programmes with genre | [optional] 
 **group** | **String**| filter for subset of programmes which belong to the given group pid | [optional] 
 **initialLetter** | **String**| filter for subset of programmes with title beginning with initial letter librarian style (ignoring leading &#39;The&#39;, &#39;An&#39; (Welsh), etc) 0-9 a-z | [optional] 
 **initialLetterEnd** | **String**| Programmes with (librarian) titles whose initial letter is equal/before given letter. Use with initial_letter_start for a range | [optional] 
 **initialLetterStart** | **String**| Programmes with (librarian) titles whose initial letter is equal/after given letter. Use with initial_letter_end for range. | [optional] 
 **initialLetterStrict** | [**[String]**](String.md)| filter for subset of programmes with title beginning with initial letter | [optional] 
 **item** | [**[String]**](String.md)| filter for subset of programmes with linked to versions which have the given item pids | [optional] 
 **masterBrand** | [**[String]**](String.md)| filter for subset of programmes with master_brand | [optional] 
 **mediaSet** | **String**| filter for subset of programmes with media set | [optional] 
 **mediaType** | [**[String]**](String.md)| filter for subset of programmes with media type | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerId** | [**[String]**](String.md)| filter for programmes by partner ID | [optional] 
 **partnerPid** | [**[String]**](String.md)| filter for programmes by partner PID | [optional] 
 **paymentType** | [**[String]**](String.md)| filter for a subset of programmes that are of the given payment_type | [optional] 
 **people** | **String**| filter for subset of programmes with contributions by given people PID | [optional] 
 **pid** | [**[String]**](String.md)| filter for subset of programmes having given PID | [optional] 
 **promotedFor** | **String**| filter for subset of programmes which are promoted for given service | [optional] 
 **q** | **String**| filter for subset of programmes matching supplied keyword/phrase (boolean operators permitted) | [optional] 
 **signed** | [**[String]**](String.md)| filter for subset of programmes that are signed | [optional] 
 **tagName** | **String**| filter for subset of programmes with tag | [optional] 
 **tagScheme** | **String**| filter for subset of programmes with a tag | [optional] 
 **tleo** | [**[String]**](String.md)| filter for subset of programmes that are TLEOs | [optional] 
 **version** | [**[String]**](String.md)| filter for subset of programmes with given PID as one of their versions | [optional] 
 **embargoed** | **String**| Control return of embargoed items (undocumented) | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listPromotions

> Nitro listPromotions(opts)

Discover metadata for content promotions

Details of short-term editorially curated \&quot;promotions\&quot;, for instance those programmes featured on iPlayer today

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'mixin': ["null"], // [String] | Mixins: * related_links: mixin to return information about related links to a promotion 
  'context': "context_example", // String | filter for subset of promotions belonging to a given context
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerId': ["null"], // [String] | filter for promotions by partner ID
  'partnerPid': ["'s0000001'"], // [String] | filter for promotions by partner PID
  'pid': ["null"], // [String] | filter for subset of promotions having given PID
  'promotedBy': ["null"], // [String] | filter for subset of promotions having given promoted by
  'promotedFor': ["null"], // [String] | filter for subset of promotions having given promoted for
  'q': "q_example", // String | filter for subset of promotions matching supplied keyword/phrase (boolean operators permitted)
  'status': ["null"] // [String] | filter for subset of promotions with status
};
apiInstance.listPromotions(opts, (error, data, response) => {
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
 **mixin** | [**[String]**](String.md)| Mixins: * related_links: mixin to return information about related links to a promotion  | [optional] 
 **context** | **String**| filter for subset of promotions belonging to a given context | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerId** | [**[String]**](String.md)| filter for promotions by partner ID | [optional] 
 **partnerPid** | [**[String]**](String.md)| filter for promotions by partner PID | [optional] 
 **pid** | [**[String]**](String.md)| filter for subset of promotions having given PID | [optional] 
 **promotedBy** | [**[String]**](String.md)| filter for subset of promotions having given promoted by | [optional] 
 **promotedFor** | [**[String]**](String.md)| filter for subset of promotions having given promoted for | [optional] 
 **q** | **String**| filter for subset of promotions matching supplied keyword/phrase (boolean operators permitted) | [optional] 
 **status** | [**[String]**](String.md)| filter for subset of promotions with status | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listSchedules

> Nitro listSchedules(opts)

Build schedules and find metadata for TV and radio broadcasts and webcasts

Dates, Times, Schedules: when and where are programmes being shown?

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'sort': "sort_example", // String | Sorts: * start_date: sort chronologically by scheduled start time/date, ascending 
  'sortDirection': "sortDirection_example", // String | Sort direction
  'mixin': ["null"], // [String] | Mixins: * ancestor_titles: return ancestor programme titles * images: mixin to add image information for broadcasts and webcasts * titles: return ancestor programme titles 
  'authority': ["null"], // [String] | filter for subset of broadcasts and webcasts that have given authority
  'descendantsOf': ["null"], // [String] | filter for subset of broadcasts and webcasts that are descendants of the given programme PID
  'endFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | filter for subset of broadcasts and webcasts that end on or later than the specified datetime
  'endTo': new Date("2013-10-20T19:20:30+01:00"), // Date | filter for subset of broadcasts and webcasts that end on or earlier than the specified datetime
  'format': ["null"], // [String] | filter for subset of broadcasts and webcasts that are classified in the given format ID
  'genre': ["null"], // [String] | filter for subset of broadcasts and webcasts that are classified in the given genre ID
  'group': "group_example", // String | filter for subset of broadcasts and webcasts that have programmes in the given group
  'id': ["null"], // [String] | filter for subset of broadcasts and webcasts that have given identifier
  'idType': ["null"], // [String] | filter for subset of broadcasts and webcasts that have given id type
  'item': ["null"], // [String] | filter for subset of broadcasts and webcasts with the given item performed on it
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerId': ["null"], // [String] | filter for broadcasts and webcasts by partner ID
  'partnerPid': ["'s0000001'"], // [String] | filter for broadcasts and webcasts by partner PID
  'people': "people_example", // String | filter for subset of broadcasts and webcasts that have given contributor
  'pid': ["null"], // [String] | filter for subset of broadcasts and webcasts having given PID
  'q': "q_example", // String | filter for subset of broadcasts and webcasts matching supplied keyword/phrase (boolean operators permitted)
  'repeat': true, // Boolean | filter to show either only repeats or non-repeats
  'scheduleDay': new Date("2013-10-20"), // Date | filter for subset of broadcasts and webcasts that start on the specified day (BBC time)
  'scheduleDayFrom': new Date("2013-10-20"), // Date | filter for subset of broadcasts and webcasts that start on or after the specified day (BBC time)
  'scheduleDayTo': new Date("2013-10-20"), // Date | filter for subset of broadcasts and webcasts that start on or before the specified day (BBC time)
  'serviceMasterBrand': ["null"], // [String] | filter for subset of broadcasts and webcasts with given service master brand
  'sid': ["null"], // [String] | filter for subset of broadcasts and webcasts that are on the specified linear service
  'startFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | filter for subset of broadcasts and webcasts that start on or later than the specified datetime
  'startTo': new Date("2013-10-20T19:20:30+01:00"), // Date | filter for subset of broadcasts and webcasts that start on or earlier than the specified datetime
  'version': ["null"] // [String] | filter for subset of broadcasts and webcasts with given PID as their parent version
};
apiInstance.listSchedules(opts, (error, data, response) => {
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
 **sort** | **String**| Sorts: * start_date: sort chronologically by scheduled start time/date, ascending  | [optional] 
 **sortDirection** | **String**| Sort direction | [optional] 
 **mixin** | [**[String]**](String.md)| Mixins: * ancestor_titles: return ancestor programme titles * images: mixin to add image information for broadcasts and webcasts * titles: return ancestor programme titles  | [optional] 
 **authority** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts that have given authority | [optional] 
 **descendantsOf** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts that are descendants of the given programme PID | [optional] 
 **endFrom** | **Date**| filter for subset of broadcasts and webcasts that end on or later than the specified datetime | [optional] 
 **endTo** | **Date**| filter for subset of broadcasts and webcasts that end on or earlier than the specified datetime | [optional] 
 **format** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts that are classified in the given format ID | [optional] 
 **genre** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts that are classified in the given genre ID | [optional] 
 **group** | **String**| filter for subset of broadcasts and webcasts that have programmes in the given group | [optional] 
 **id** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts that have given identifier | [optional] 
 **idType** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts that have given id type | [optional] 
 **item** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts with the given item performed on it | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerId** | [**[String]**](String.md)| filter for broadcasts and webcasts by partner ID | [optional] 
 **partnerPid** | [**[String]**](String.md)| filter for broadcasts and webcasts by partner PID | [optional] 
 **people** | **String**| filter for subset of broadcasts and webcasts that have given contributor | [optional] 
 **pid** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts having given PID | [optional] 
 **q** | **String**| filter for subset of broadcasts and webcasts matching supplied keyword/phrase (boolean operators permitted) | [optional] 
 **repeat** | **Boolean**| filter to show either only repeats or non-repeats | [optional] 
 **scheduleDay** | **Date**| filter for subset of broadcasts and webcasts that start on the specified day (BBC time) | [optional] 
 **scheduleDayFrom** | **Date**| filter for subset of broadcasts and webcasts that start on or after the specified day (BBC time) | [optional] 
 **scheduleDayTo** | **Date**| filter for subset of broadcasts and webcasts that start on or before the specified day (BBC time) | [optional] 
 **serviceMasterBrand** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts with given service master brand | [optional] 
 **sid** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts that are on the specified linear service | [optional] 
 **startFrom** | **Date**| filter for subset of broadcasts and webcasts that start on or later than the specified datetime | [optional] 
 **startTo** | **Date**| filter for subset of broadcasts and webcasts that start on or earlier than the specified datetime | [optional] 
 **version** | [**[String]**](String.md)| filter for subset of broadcasts and webcasts with given PID as their parent version | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listServices

> Nitro listServices(opts)

Information about the linear services used for broadcast transmissions

The services feed exposes the linear broadcast \&quot;services\&quot; from PIPs. These are the actual services which broadcast programmes (eg bbc_one_oxford is the service for BBC One in Oxford).

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'endFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Return services that end on or later than the specified datetime
  'endTo': new Date("2013-10-20T19:20:30+01:00"), // Date | filter for subset of broadcasts that end on or earlier than the specified datetime
  'mid': ["null"], // [String] | filter for services by masterbrand MID
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerId': ["null"], // [String] | filter for services by partner ID
  'partnerPid': ["'s0000001'"], // [String] | filter for services by partner PID
  'q': "q_example", // String | filter for subset of services matching supplied keyword/phrase (boolean operators permitted)
  'serviceType': ["null"], // [String] | filter for specified type of linear services
  'sid': ["null"], // [String] | filter for specified linear service
  'startFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Return services that start on or later than the specified datetime
  'startTo': new Date("2013-10-20T19:20:30+01:00") // Date | Return services that start earlier than the specified datetime
};
apiInstance.listServices(opts, (error, data, response) => {
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
 **endFrom** | **Date**| Return services that end on or later than the specified datetime | [optional] 
 **endTo** | **Date**| filter for subset of broadcasts that end on or earlier than the specified datetime | [optional] 
 **mid** | [**[String]**](String.md)| filter for services by masterbrand MID | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerId** | [**[String]**](String.md)| filter for services by partner ID | [optional] 
 **partnerPid** | [**[String]**](String.md)| filter for services by partner PID | [optional] 
 **q** | **String**| filter for subset of services matching supplied keyword/phrase (boolean operators permitted) | [optional] 
 **serviceType** | [**[String]**](String.md)| filter for specified type of linear services | [optional] 
 **sid** | [**[String]**](String.md)| filter for specified linear service | [optional] 
 **startFrom** | **Date**| Return services that start on or later than the specified datetime | [optional] 
 **startTo** | **Date**| Return services that start earlier than the specified datetime | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listVersions

> Nitro listVersions(opts)

Metadata on editorial programme versions: original, signed, audio-described, etc

The versions feed exposes editorial \&quot;Versions\&quot; of programmes. These are concepts used to capture different presentations of an overall programme: for example, versions of a programme may include one with sign language, one with audio description, one edited for content and more. Versions are also important to understand for broadcasts: a linear broadcast or an ondemand is always of a specific version, not merely of a programme.

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.FeedsApi();
let opts = {
  'availability': ["null"], // [String] | filter for subset of versions that have availability
  'descendantsOf': ["null"], // [String] | filter for subset of versions having given programme PID
  'mediaSet': ["null"], // [String] | filter for subset of versions with availability in the given media set
  'page': 1, // Number | which page of results to return
  'pageSize': 10, // Number | number of results in each page
  'partnerId': ["null"], // [String] | filter for versions by partner ID
  'partnerPid': ["'s0000001'"], // [String] | filter for versions by partner PID
  'paymentType': ["null"], // [String] | filter for a subset of versions that are of the given payment_type
  'pid': ["null"], // [String] | filter for subset of versions having given PID
  'embargoed': "embargoed_example" // String | Control return of embargoed items (undocumented)
};
apiInstance.listVersions(opts, (error, data, response) => {
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
 **availability** | [**[String]**](String.md)| filter for subset of versions that have availability | [optional] 
 **descendantsOf** | [**[String]**](String.md)| filter for subset of versions having given programme PID | [optional] 
 **mediaSet** | [**[String]**](String.md)| filter for subset of versions with availability in the given media set | [optional] 
 **page** | **Number**| which page of results to return | [optional] [default to 1]
 **pageSize** | **Number**| number of results in each page | [optional] [default to 10]
 **partnerId** | [**[String]**](String.md)| filter for versions by partner ID | [optional] 
 **partnerPid** | [**[String]**](String.md)| filter for versions by partner PID | [optional] 
 **paymentType** | [**[String]**](String.md)| filter for a subset of versions that are of the given payment_type | [optional] 
 **pid** | [**[String]**](String.md)| filter for subset of versions having given PID | [optional] 
 **embargoed** | **String**| Control return of embargoed items (undocumented) | [optional] 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

