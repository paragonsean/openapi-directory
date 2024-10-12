# DaniWebConnectApi.AutocompletesApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocompletesGet**](AutocompletesApi.md#autocompletesGet) | **GET** /autocompletes | 



## autocompletesGet

> EndpointGetAutocompletes autocompletesGet(opts)



Retrieve an array of names and locations, filtered by category, that begin with the query string passed in. Ideally used for search autocomplete dropdowns, as the search functionality filters against name and location. The four potential categories are: &#x60;conversations&#x60; for names of users you are in existing conversations with; &#x60;matches&#x60; for names of users you have previously skipped over; &#x60;people&#x60; for names of all other users; &#x60;locations&#x60; for locations of users. Only users and their locations who exist with the current access token&#39;s bubble are considered.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.AutocompletesApi();
let opts = {
  'query': "query_example" // String | 
};
apiInstance.autocompletesGet(opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] 

### Return type

[**EndpointGetAutocompletes**](EndpointGetAutocompletes.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

