# EDrvApi.OrganizationsApi

All URIs are relative to *http://api.edrv.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOrganization**](OrganizationsApi.md#getOrganization) | **GET** /v1/organizations/{id} | 
[**getOrganizations**](OrganizationsApi.md#getOrganizations) | **GET** /v1/organizations | 
[**patchOrganization**](OrganizationsApi.md#patchOrganization) | **PATCH** /v1/organizations/{id} | 



## getOrganization

> getOrganization(id, opts)



Get one organization&#39;s data by id

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.OrganizationsApi();
let id = "id_example"; // String | ID of organization that needs to be fetched
let opts = {
  'includeLocations': true // Boolean | Populate locations
};
apiInstance.getOrganization(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of organization that needs to be fetched | 
 **includeLocations** | **Boolean**| Populate locations | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOrganizations

> getOrganizations(opts)



Get an array of all Organizations

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.OrganizationsApi();
let opts = {
  'paginateLimit': 20, // Number | Number of results per page
  'paginatePage': "paginatePage_example", // String | The queried page index
  'paginateEnabled': true, // Boolean | Enable pagination
  'sortBy': "'createdAt'", // String | Sort data by this key
  'sortOrder': "'desc'", // String | asc to sort ascending (default is desc - descending)
  'createdAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'createdAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'includeLocations': true // Boolean | Populate locations
};
apiInstance.getOrganizations(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paginateLimit** | **Number**| Number of results per page | [optional] [default to 20]
 **paginatePage** | **String**| The queried page index | [optional] 
 **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true]
 **sortBy** | **String**| Sort data by this key | [optional] [default to &#39;createdAt&#39;]
 **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to &#39;desc&#39;]
 **createdAtGte** | **Date**| Date as ISO String | [optional] 
 **createdAtLte** | **Date**| Date as ISO String | [optional] 
 **updatedAtGte** | **Date**| Date as ISO String | [optional] 
 **updatedAtLte** | **Date**| Date as ISO String | [optional] 
 **includeLocations** | **Boolean**| Populate locations | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## patchOrganization

> patchOrganization(id, patchOrganizationRequest)



Update an organization&#39;s data

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.OrganizationsApi();
let id = "id_example"; // String | ID of organization that needs to be updated
let patchOrganizationRequest = new EDrvApi.PatchOrganizationRequest(); // PatchOrganizationRequest | Include organization properties to create here
apiInstance.patchOrganization(id, patchOrganizationRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of organization that needs to be updated | 
 **patchOrganizationRequest** | [**PatchOrganizationRequest**](PatchOrganizationRequest.md)| Include organization properties to create here | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

