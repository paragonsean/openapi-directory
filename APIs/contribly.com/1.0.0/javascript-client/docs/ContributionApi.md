# Contribly.ContributionApi

All URIs are relative to *https://api.contribly.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contributionRefinementTypesGet**](ContributionApi.md#contributionRefinementTypesGet) | **GET** /contribution-refinement-types | List valid contribution refinement types
[**contributionRefinementsGet**](ContributionApi.md#contributionRefinementsGet) | **GET** /contribution-refinements | List contribution refinement options
[**contributionsGet**](ContributionApi.md#contributionsGet) | **GET** /contributions | List contributions
[**contributionsIdDelete**](ContributionApi.md#contributionsIdDelete) | **DELETE** /contributions/{id} | Delete this contribution
[**contributionsIdFlagPost**](ContributionApi.md#contributionsIdFlagPost) | **POST** /contributions/{id}/flag | Raise a flag against this contribution
[**contributionsIdGet**](ContributionApi.md#contributionsIdGet) | **GET** /contributions/{id} | Get a single contribution by id
[**contributionsIdLikePost**](ContributionApi.md#contributionsIdLikePost) | **POST** /contributions/{id}/like | Allows a user to mark a contribution as liked
[**contributionsIdLikesGet**](ContributionApi.md#contributionsIdLikesGet) | **GET** /contributions/{id}/likes | List users who have liked this contributions
[**contributionsIdModeratePost**](ContributionApi.md#contributionsIdModeratePost) | **POST** /contributions/{id}/moderate | Perform a moderation action on this contribution
[**contributionsPost**](ContributionApi.md#contributionsPost) | **POST** /contributions | Create a new contribution
[**exportPost**](ContributionApi.md#exportPost) | **POST** /export | Export contributions.
[**exportSummaryPost**](ContributionApi.md#exportSummaryPost) | **POST** /export-summary | Export contributions preflight summary.
[**exportsIdGet**](ContributionApi.md#exportsIdGet) | **GET** /exports/{id} | Get a single export job; poll to follow export progress.



## contributionRefinementTypesGet

> [String] contributionRefinementTypesGet()

List valid contribution refinement types

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
apiInstance.contributionRefinementTypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contributionRefinementsGet

> {String: [String]} contributionRefinementsGet(opts)

List contribution refinement options

Given a contribution list query determine the available filter options. Can be used to generate the UI to refinement a filter.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let opts = {
  'assignment': "assignment_example", // String | Restrict results to contributions submitted to this assignment.
  'country': "country_example", // String | Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to contributions created before this date time.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to contributions created after this date time.
  'geohash': "geohash_example", // String | Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
  'hasLocation': true, // Boolean | Restrict results to contributions which have a publicly visible location.
  'latLong': "latLong_example", // String | Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
  'radius': 3.4, // Number | When limiting result by location with the latLong parameter, specify the radius in kilometers.
  'mediaType': "mediaType_example", // String | Restrict results to contributions which include a media file of the given type (ie. image / video)
  'ownedBy': "ownedBy_example", // String | Restrict results to contributions which are fall under the jurisdiction by this user.
  'q': "q_example", // String | Restrict results to contributions whose headline text matches this keyword.
  'urlWords': "urlWords_example", // String | Locate a specific contribution by URL words
  'user': "user_example", // String | Restrict results to contributions by this user identified by id.
  'refinements': "refinements_example", // String | Comma seperated list of refinement names.
  'refinementSize': 3.4 // Number | Number of refinement options to return.
};
apiInstance.contributionRefinementsGet(opts, (error, data, response) => {
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
 **assignment** | **String**| Restrict results to contributions submitted to this assignment. | [optional] 
 **country** | **String**| Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code). | [optional] 
 **createdBefore** | **Date**| Limit results to contributions created before this date time. | [optional] 
 **createdAfter** | **Date**| Limit results to contributions created after this date time. | [optional] 
 **geohash** | **String**| Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes) | [optional] 
 **hasLocation** | **Boolean**| Restrict results to contributions which have a publicly visible location. | [optional] 
 **latLong** | **String**| Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius | [optional] 
 **radius** | **Number**| When limiting result by location with the latLong parameter, specify the radius in kilometers. | [optional] 
 **mediaType** | **String**| Restrict results to contributions which include a media file of the given type (ie. image / video) | [optional] 
 **ownedBy** | **String**| Restrict results to contributions which are fall under the jurisdiction by this user. | [optional] 
 **q** | **String**| Restrict results to contributions whose headline text matches this keyword. | [optional] 
 **urlWords** | **String**| Locate a specific contribution by URL words | [optional] 
 **user** | **String**| Restrict results to contributions by this user identified by id. | [optional] 
 **refinements** | **String**| Comma seperated list of refinement names. | [optional] 
 **refinementSize** | **Number**| Number of refinement options to return. | [optional] 

### Return type

**{String: [String]}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contributionsGet

> [Contribution] contributionsGet(opts)

List contributions

Retrieve contributions.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let opts = {
  'assignment': "assignment_example", // String | Restrict results to contributions submitted to this assignment.
  'country': "country_example", // String | Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to contributions created before this date time.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to contributions created after this date time.
  'createdDay': new Date("2013-10-20"), // Date | Limit results to contributions created on this day.
  'createdMonth': "createdMonth_example", // String | Limit results to contributions created during this month.
  'geohash': "geohash_example", // String | Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
  'hasLocation': true, // Boolean | Restrict results to contributions which have a publicly visible location.
  'latLong': "latLong_example", // String | Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
  'radius': 3.4, // Number | When limiting result by location with the latLong parameter, specify the radius in kilometers.
  'mediaType': "mediaType_example", // String | Restrict results to contributions which include a media file of the given type (ie. image / video)
  'ownedBy': "ownedBy_example", // String | Restrict results to contributions which are fall under the jurisdiction by this user.
  'q': "q_example", // String | Restrict results to contributions whose headline text matches this keyword.
  'urlWords': "urlWords_example", // String | Locate a specific contribution by URL words
  'user': "user_example", // String | Restrict results to contributions by this user identified by id.
  'ids': "ids_example", // String | Restrict results to a list of specific contributions identified by a comma seperated list of ids.
  'format': "format_example" // String | Select output format. 'json' or 'rss'. Defaults to JSON.
};
apiInstance.contributionsGet(opts, (error, data, response) => {
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
 **assignment** | **String**| Restrict results to contributions submitted to this assignment. | [optional] 
 **country** | **String**| Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code). | [optional] 
 **createdBefore** | **Date**| Limit results to contributions created before this date time. | [optional] 
 **createdAfter** | **Date**| Limit results to contributions created after this date time. | [optional] 
 **createdDay** | **Date**| Limit results to contributions created on this day. | [optional] 
 **createdMonth** | **String**| Limit results to contributions created during this month. | [optional] 
 **geohash** | **String**| Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes) | [optional] 
 **hasLocation** | **Boolean**| Restrict results to contributions which have a publicly visible location. | [optional] 
 **latLong** | **String**| Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius | [optional] 
 **radius** | **Number**| When limiting result by location with the latLong parameter, specify the radius in kilometers. | [optional] 
 **mediaType** | **String**| Restrict results to contributions which include a media file of the given type (ie. image / video) | [optional] 
 **ownedBy** | **String**| Restrict results to contributions which are fall under the jurisdiction by this user. | [optional] 
 **q** | **String**| Restrict results to contributions whose headline text matches this keyword. | [optional] 
 **urlWords** | **String**| Locate a specific contribution by URL words | [optional] 
 **user** | **String**| Restrict results to contributions by this user identified by id. | [optional] 
 **ids** | **String**| Restrict results to a list of specific contributions identified by a comma seperated list of ids. | [optional] 
 **format** | **String**| Select output format. &#39;json&#39; or &#39;rss&#39;. Defaults to JSON. | [optional] 

### Return type

[**[Contribution]**](Contribution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contributionsIdDelete

> Contribution contributionsIdDelete(id)

Delete this contribution

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let id = "id_example"; // String | Id of the contribution to delete
apiInstance.contributionsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| Id of the contribution to delete | 

### Return type

[**Contribution**](Contribution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contributionsIdFlagPost

> Flag contributionsIdFlagPost(id, flag)

Raise a flag against this contribution

Allows end users to bring potential issues with publicly visible content to the attention of moderators.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let id = "id_example"; // String | Id of the contribution to flag
let flag = new Contribly.Flag(); // Flag | Flag to be created
apiInstance.contributionsIdFlagPost(id, flag, (error, data, response) => {
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
 **id** | **String**| Id of the contribution to flag | 
 **flag** | [**Flag**](Flag.md)| Flag to be created | 

### Return type

[**Flag**](Flag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contributionsIdGet

> Contribution contributionsIdGet(id)

Get a single contribution by id

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let id = "id_example"; // String | Id of the contribution to return
apiInstance.contributionsIdGet(id, (error, data, response) => {
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
 **id** | **String**| Id of the contribution to return | 

### Return type

[**Contribution**](Contribution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contributionsIdLikePost

> Number contributionsIdLikePost(id)

Allows a user to mark a contribution as liked

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let id = "id_example"; // String | Id of the contribution
apiInstance.contributionsIdLikePost(id, (error, data, response) => {
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
 **id** | **String**| Id of the contribution | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contributionsIdLikesGet

> [String] contributionsIdLikesGet(id)

List users who have liked this contributions

Returns a list of user ids of users who have liked this conribution

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let id = "id_example"; // String | Id of the contribution
apiInstance.contributionsIdLikesGet(id, (error, data, response) => {
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
 **id** | **String**| Id of the contribution | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contributionsIdModeratePost

> String contributionsIdModeratePost(id, moderationHistoryItemSubmission)

Perform a moderation action on this contribution

Allows the contribution to approved of rejected.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let id = "id_example"; // String | Id of the contribution to moderate
let moderationHistoryItemSubmission = new Contribly.ModerationHistoryItemSubmission(); // ModerationHistoryItemSubmission | A moderation action
apiInstance.contributionsIdModeratePost(id, moderationHistoryItemSubmission, (error, data, response) => {
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
 **id** | **String**| Id of the contribution to moderate | 
 **moderationHistoryItemSubmission** | [**ModerationHistoryItemSubmission**](ModerationHistoryItemSubmission.md)| A moderation action | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contributionsPost

> Contribution contributionsPost(contribution)

Create a new contribution

### Example

```javascript
import Contribly from 'contribly';
let defaultClient = Contribly.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Contribly.ContributionApi();
let contribution = new Contribly.Contribution(); // Contribution | Contribution object to be created
apiInstance.contributionsPost(contribution, (error, data, response) => {
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
 **contribution** | [**Contribution**](Contribution.md)| Contribution object to be created | 

### Return type

[**Contribution**](Contribution.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## exportPost

> Export exportPost(opts)

Export contributions.

Begin an export job. Returns a export job which can be polled to follow the progress of an export.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let opts = {
  'assignment': "assignment_example", // String | Restrict results to contributions submitted to this assignment.
  'country': "country_example", // String | Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to contributions created before this date time.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to contributions created after this date time.
  'geohash': "geohash_example", // String | Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
  'hasLocation': true, // Boolean | Restrict results to contributions which have a publicly visible location.
  'latLong': "latLong_example", // String | Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
  'radius': 3.4, // Number | When limiting result by location with the latLong parameter, specify the radius in kilometers.
  'mediaType': "mediaType_example", // String | Restrict results to contributions which include a media file of the given type (ie. image / video)
  'ownedBy': "ownedBy_example", // String | Restrict results to contributions which are fall under the jurisdiction by this user.
  'q': "q_example", // String | Restrict results to contributions whose headline text matches this keyword.
  'urlWords': "urlWords_example", // String | Locate a specific contribution by URL words
  'user': "user_example", // String | Restrict results to contributions by this user identified by id.
  'tagged': true, // Boolean | Should exported media files be tagged with metadata. Deprecated; use format instead.
  'combined': true, // Boolean | Included a combined file with all contribution text.
  'individual': true, // Boolean | Include individual text files for each contribution.
  'format': "format_example", // String | Media format to export; none, fullsize, tagged or original.
  'json': true // Boolean | Include raw JSON for each contribution.
};
apiInstance.exportPost(opts, (error, data, response) => {
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
 **assignment** | **String**| Restrict results to contributions submitted to this assignment. | [optional] 
 **country** | **String**| Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code). | [optional] 
 **createdBefore** | **Date**| Limit results to contributions created before this date time. | [optional] 
 **createdAfter** | **Date**| Limit results to contributions created after this date time. | [optional] 
 **geohash** | **String**| Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes) | [optional] 
 **hasLocation** | **Boolean**| Restrict results to contributions which have a publicly visible location. | [optional] 
 **latLong** | **String**| Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius | [optional] 
 **radius** | **Number**| When limiting result by location with the latLong parameter, specify the radius in kilometers. | [optional] 
 **mediaType** | **String**| Restrict results to contributions which include a media file of the given type (ie. image / video) | [optional] 
 **ownedBy** | **String**| Restrict results to contributions which are fall under the jurisdiction by this user. | [optional] 
 **q** | **String**| Restrict results to contributions whose headline text matches this keyword. | [optional] 
 **urlWords** | **String**| Locate a specific contribution by URL words | [optional] 
 **user** | **String**| Restrict results to contributions by this user identified by id. | [optional] 
 **tagged** | **Boolean**| Should exported media files be tagged with metadata. Deprecated; use format instead. | [optional] 
 **combined** | **Boolean**| Included a combined file with all contribution text. | [optional] 
 **individual** | **Boolean**| Include individual text files for each contribution. | [optional] 
 **format** | **String**| Media format to export; none, fullsize, tagged or original. | [optional] 
 **json** | **Boolean**| Include raw JSON for each contribution. | [optional] 

### Return type

[**Export**](Export.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportSummaryPost

> ExportSummary exportSummaryPost(opts)

Export contributions preflight summary.

Provide a preflight summary of an export request.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let opts = {
  'assignment': "assignment_example", // String | Restrict results to contributions submitted to this assignment.
  'country': "country_example", // String | Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code).
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to contributions created before this date time.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Limit results to contributions created after this date time.
  'geohash': "geohash_example", // String | Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes)
  'hasLocation': true, // Boolean | Restrict results to contributions which have a publicly visible location.
  'latLong': "latLong_example", // String | Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius
  'radius': 3.4, // Number | When limiting result by location with the latLong parameter, specify the radius in kilometers.
  'mediaType': "mediaType_example", // String | Restrict results to contributions which include a media file of the given type (ie. image / video)
  'ownedBy': "ownedBy_example", // String | Restrict results to contributions which are fall under the jurisdiction by this user.
  'q': "q_example", // String | Restrict results to contributions whose headline text matches this keyword.
  'urlWords': "urlWords_example", // String | Locate a specific contribution by URL words
  'user': "user_example" // String | Restrict results to contributions by this user identified by id.
};
apiInstance.exportSummaryPost(opts, (error, data, response) => {
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
 **assignment** | **String**| Restrict results to contributions submitted to this assignment. | [optional] 
 **country** | **String**| Limit results to contributions which have a publicly visible location within the given country (specified by two letter country code). | [optional] 
 **createdBefore** | **Date**| Limit results to contributions created before this date time. | [optional] 
 **createdAfter** | **Date**| Limit results to contributions created after this date time. | [optional] 
 **geohash** | **String**| Restrict results to contributions which have specified a location which falls within this geohash (or comma seperated list of multiple geohashes) | [optional] 
 **hasLocation** | **Boolean**| Restrict results to contributions which have a publicly visible location. | [optional] 
 **latLong** | **String**| Limit results to contributions with location near this latitude and longitude (comma seperated lat/long pair). Also see radius | [optional] 
 **radius** | **Number**| When limiting result by location with the latLong parameter, specify the radius in kilometers. | [optional] 
 **mediaType** | **String**| Restrict results to contributions which include a media file of the given type (ie. image / video) | [optional] 
 **ownedBy** | **String**| Restrict results to contributions which are fall under the jurisdiction by this user. | [optional] 
 **q** | **String**| Restrict results to contributions whose headline text matches this keyword. | [optional] 
 **urlWords** | **String**| Locate a specific contribution by URL words | [optional] 
 **user** | **String**| Restrict results to contributions by this user identified by id. | [optional] 

### Return type

[**ExportSummary**](ExportSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportsIdGet

> Export exportsIdGet(id)

Get a single export job; poll to follow export progress.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.ContributionApi();
let id = "id_example"; // String | Id of the export job to return
apiInstance.exportsIdGet(id, (error, data, response) => {
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
 **id** | **String**| Id of the export job to return | 

### Return type

[**Export**](Export.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

