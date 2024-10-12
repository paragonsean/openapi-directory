# TreatiesApi.TreatyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBusinessItemsByTreatyId**](TreatyApi.md#getBusinessItemsByTreatyId) | **GET** /api/Treaty/{id}/BusinessItems | Returns business items belonging to the treaty with ID.
[**getTreaties**](TreatyApi.md#getTreaties) | **GET** /api/Treaty | Returns a list of treaties.
[**getTreatyById**](TreatyApi.md#getTreatyById) | **GET** /api/Treaty/{id} | Returns a treaty by ID.



## getBusinessItemsByTreatyId

> BusinessItemResourceCollection getBusinessItemsByTreatyId(id)

Returns business items belonging to the treaty with ID.

### Example

```javascript
import TreatiesApi from 'treaties_api';

let apiInstance = new TreatiesApi.TreatyApi();
let id = "id_example"; // String | Business items belonging to treaty with the ID specified
apiInstance.getBusinessItemsByTreatyId(id, (error, data, response) => {
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
 **id** | **String**| Business items belonging to treaty with the ID specified | 

### Return type

[**BusinessItemResourceCollection**](BusinessItemResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getTreaties

> TreatyResourceCollection getTreaties(opts)

Returns a list of treaties.

### Example

```javascript
import TreatiesApi from 'treaties_api';

let apiInstance = new TreatiesApi.TreatyApi();
let opts = {
  'searchText': "searchText_example", // String | Treaties which contains the search text specified
  'governmentOrganisationId': 56, // Number | Treaties with the government organisation id specified
  'series': new TreatiesApi.SeriesMembershipType(), // SeriesMembershipType | Treaties with the series membership type specified
  'parliamentaryProcess': new TreatiesApi.ParliamentaryProcess(), // ParliamentaryProcess | Treaties where the parliamentary process is concluded or notconcluded
  'debateScheduled': true, // Boolean | Treaties which contain a scheduled debate
  'motionToNotRatify': true, // Boolean | Treaties which contain a motion to not ratify
  'recommendedNotRatify': true, // Boolean | Treaties which are recommended to not ratify
  'house': new TreatiesApi.House(), // House | Treaties which are laid in the specified house
  'skip': 56, // Number | The number of records to skip from the first, default is 0
  'take': 56 // Number | The number of records to return, default is 20
};
apiInstance.getTreaties(opts, (error, data, response) => {
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
 **searchText** | **String**| Treaties which contains the search text specified | [optional] 
 **governmentOrganisationId** | **Number**| Treaties with the government organisation id specified | [optional] 
 **series** | [**SeriesMembershipType**](.md)| Treaties with the series membership type specified | [optional] 
 **parliamentaryProcess** | [**ParliamentaryProcess**](.md)| Treaties where the parliamentary process is concluded or notconcluded | [optional] 
 **debateScheduled** | **Boolean**| Treaties which contain a scheduled debate | [optional] 
 **motionToNotRatify** | **Boolean**| Treaties which contain a motion to not ratify | [optional] 
 **recommendedNotRatify** | **Boolean**| Treaties which are recommended to not ratify | [optional] 
 **house** | [**House**](.md)| Treaties which are laid in the specified house | [optional] 
 **skip** | **Number**| The number of records to skip from the first, default is 0 | [optional] 
 **take** | **Number**| The number of records to return, default is 20 | [optional] 

### Return type

[**TreatyResourceCollection**](TreatyResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## getTreatyById

> TreatyResource getTreatyById(id)

Returns a treaty by ID.

### Example

```javascript
import TreatiesApi from 'treaties_api';

let apiInstance = new TreatiesApi.TreatyApi();
let id = "id_example"; // String | Treaty with ID specified
apiInstance.getTreatyById(id, (error, data, response) => {
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
 **id** | **String**| Treaty with ID specified | 

### Return type

[**TreatyResource**](TreatyResource.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

