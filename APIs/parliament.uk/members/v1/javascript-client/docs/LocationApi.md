# MembersApi.LocationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiLocationBrowseLocationTypeLocationNameGet**](LocationApi.md#apiLocationBrowseLocationTypeLocationNameGet) | **GET** /api/Location/Browse/{locationType}/{locationName} | Returns a list of locations, both parent and child
[**apiLocationConstituencyIdElectionResultElectionIdGet**](LocationApi.md#apiLocationConstituencyIdElectionResultElectionIdGet) | **GET** /api/Location/Constituency/{id}/ElectionResult/{electionId} | Returns an election result by constituency and election id
[**apiLocationConstituencyIdElectionResultLatestGet**](LocationApi.md#apiLocationConstituencyIdElectionResultLatestGet) | **GET** /api/Location/Constituency/{id}/ElectionResult/Latest | Returns latest election result by constituency id
[**apiLocationConstituencyIdElectionResultsGet**](LocationApi.md#apiLocationConstituencyIdElectionResultsGet) | **GET** /api/Location/Constituency/{id}/ElectionResults | Returns a list of election results by constituency ID
[**apiLocationConstituencyIdGeometryGet**](LocationApi.md#apiLocationConstituencyIdGeometryGet) | **GET** /api/Location/Constituency/{id}/Geometry | Returns geometry by constituency ID
[**apiLocationConstituencyIdGet**](LocationApi.md#apiLocationConstituencyIdGet) | **GET** /api/Location/Constituency/{id} | Returns a constituency by ID
[**apiLocationConstituencyIdRepresentationsGet**](LocationApi.md#apiLocationConstituencyIdRepresentationsGet) | **GET** /api/Location/Constituency/{id}/Representations | Returns a list of representations by constituency ID
[**apiLocationConstituencyIdSynopsisGet**](LocationApi.md#apiLocationConstituencyIdSynopsisGet) | **GET** /api/Location/Constituency/{id}/Synopsis | Returns a synopsis by constituency ID
[**apiLocationConstituencySearchGet**](LocationApi.md#apiLocationConstituencySearchGet) | **GET** /api/Location/Constituency/Search | Returns a list of constituencies



## apiLocationBrowseLocationTypeLocationNameGet

> LocationItem apiLocationBrowseLocationTypeLocationNameGet(locationType, locationName)

Returns a list of locations, both parent and child

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LocationApi();
let locationType = new MembersApi.LocationType(); // LocationType | Location by type of location
let locationName = "locationName_example"; // String | Location by name specified
apiInstance.apiLocationBrowseLocationTypeLocationNameGet(locationType, locationName, (error, data, response) => {
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
 **locationType** | [**LocationType**](.md)| Location by type of location | 
 **locationName** | **String**| Location by name specified | 

### Return type

[**LocationItem**](LocationItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiLocationConstituencyIdElectionResultElectionIdGet

> ElectionResultItem apiLocationConstituencyIdElectionResultElectionIdGet(id, electionId)

Returns an election result by constituency and election id

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LocationApi();
let id = 56; // Number | Election result by constituency id
let electionId = 56; // Number | Election result by election id
apiInstance.apiLocationConstituencyIdElectionResultElectionIdGet(id, electionId, (error, data, response) => {
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
 **id** | **Number**| Election result by constituency id | 
 **electionId** | **Number**| Election result by election id | 

### Return type

[**ElectionResultItem**](ElectionResultItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiLocationConstituencyIdElectionResultLatestGet

> ElectionResultItem apiLocationConstituencyIdElectionResultLatestGet(id)

Returns latest election result by constituency id

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LocationApi();
let id = 56; // Number | Latest election result by constituency id
apiInstance.apiLocationConstituencyIdElectionResultLatestGet(id, (error, data, response) => {
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
 **id** | **Number**| Latest election result by constituency id | 

### Return type

[**ElectionResultItem**](ElectionResultItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiLocationConstituencyIdElectionResultsGet

> ElectionResultListItem apiLocationConstituencyIdElectionResultsGet(id)

Returns a list of election results by constituency ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LocationApi();
let id = 56; // Number | Elections results by constituency ID
apiInstance.apiLocationConstituencyIdElectionResultsGet(id, (error, data, response) => {
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
 **id** | **Number**| Elections results by constituency ID | 

### Return type

[**ElectionResultListItem**](ElectionResultListItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiLocationConstituencyIdGeometryGet

> StringItem apiLocationConstituencyIdGeometryGet(id)

Returns geometry by constituency ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LocationApi();
let id = 56; // Number | Geometry by constituency ID
apiInstance.apiLocationConstituencyIdGeometryGet(id, (error, data, response) => {
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
 **id** | **Number**| Geometry by constituency ID | 

### Return type

[**StringItem**](StringItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiLocationConstituencyIdGet

> ConstituencyItem apiLocationConstituencyIdGet(id)

Returns a constituency by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LocationApi();
let id = 56; // Number | Constituency by ID
apiInstance.apiLocationConstituencyIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Constituency by ID | 

### Return type

[**ConstituencyItem**](ConstituencyItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiLocationConstituencyIdRepresentationsGet

> ConstituencyRepresentationListItem apiLocationConstituencyIdRepresentationsGet(id)

Returns a list of representations by constituency ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LocationApi();
let id = 56; // Number | Representations by constituency ID
apiInstance.apiLocationConstituencyIdRepresentationsGet(id, (error, data, response) => {
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
 **id** | **Number**| Representations by constituency ID | 

### Return type

[**ConstituencyRepresentationListItem**](ConstituencyRepresentationListItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiLocationConstituencyIdSynopsisGet

> StringItem apiLocationConstituencyIdSynopsisGet(id)

Returns a synopsis by constituency ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LocationApi();
let id = 56; // Number | Synopsis by constituency ID
apiInstance.apiLocationConstituencyIdSynopsisGet(id, (error, data, response) => {
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
 **id** | **Number**| Synopsis by constituency ID | 

### Return type

[**StringItem**](StringItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiLocationConstituencySearchGet

> ConstituencyMembersServiceSearchResult apiLocationConstituencySearchGet(opts)

Returns a list of constituencies

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.LocationApi();
let opts = {
  'searchText': "searchText_example", // String | Constituencies containing serach term in their name
  'skip': 0, // Number | The number of records to skip from the first, default is 0
  'take': 20 // Number | The number of records to return, default is 20. Maximum is 20
};
apiInstance.apiLocationConstituencySearchGet(opts, (error, data, response) => {
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
 **searchText** | **String**| Constituencies containing serach term in their name | [optional] 
 **skip** | **Number**| The number of records to skip from the first, default is 0 | [optional] [default to 0]
 **take** | **Number**| The number of records to return, default is 20. Maximum is 20 | [optional] [default to 20]

### Return type

[**ConstituencyMembersServiceSearchResult**](ConstituencyMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

