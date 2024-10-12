# AgcoApi.BundlesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundlesDeleteBundle**](BundlesApi.md#bundlesDeleteBundle) | **DELETE** /api/v2/Bundles/{ID} | Delete a Bundle.
[**bundlesGetBundle**](BundlesApi.md#bundlesGetBundle) | **GET** /api/v2/Bundles/{ID} | Get a specific Bundle by ID.
[**bundlesGetBundles**](BundlesApi.md#bundlesGetBundles) | **GET** /api/v2/Bundles | Get the list of bundles.
[**bundlesPostBundle**](BundlesApi.md#bundlesPostBundle) | **POST** /api/v2/Bundles | Add a Bundle to the Update System.
[**bundlesPutBundle**](BundlesApi.md#bundlesPutBundle) | **PUT** /api/v2/Bundles/{ID} | Modify a Bundle in the Update System.



## bundlesDeleteBundle

> bundlesDeleteBundle(ID)

Delete a Bundle.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.BundlesApi();
let ID = "ID_example"; // String | The Bundle ID to Delete
apiInstance.bundlesDeleteBundle(ID, (error, data, response) => {
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
 **ID** | **String**| The Bundle ID to Delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## bundlesGetBundle

> UpdateSystemModelsBundle bundlesGetBundle(ID)

Get a specific Bundle by ID.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.BundlesApi();
let ID = "ID_example"; // String | The Bundle ID
apiInstance.bundlesGetBundle(ID, (error, data, response) => {
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
 **ID** | **String**| The Bundle ID | 

### Return type

[**UpdateSystemModelsBundle**](UpdateSystemModelsBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## bundlesGetBundles

> APIPagedResponseUpdateSystemModelsBundle bundlesGetBundles(opts)

Get the list of bundles.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.BundlesApi();
let opts = {
  'updateGroupID': "updateGroupID_example", // String | Optional. Filter by UpdateGroup ID.
  'active': true, // Boolean | Optional. Filter by active status.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56, // Number | Optional. The page offset. The default page offset is 0.
  'bundleNumber': 56 // Number | Optional. If provided, filters by BundleNumber.
};
apiInstance.bundlesGetBundles(opts, (error, data, response) => {
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
 **updateGroupID** | **String**| Optional. Filter by UpdateGroup ID. | [optional] 
 **active** | **Boolean**| Optional. Filter by active status. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 
 **bundleNumber** | **Number**| Optional. If provided, filters by BundleNumber. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsBundle**](APIPagedResponseUpdateSystemModelsBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## bundlesPostBundle

> String bundlesPostBundle(updateSystemModelsBundle)

Add a Bundle to the Update System.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.BundlesApi();
let updateSystemModelsBundle = new AgcoApi.UpdateSystemModelsBundle(); // UpdateSystemModelsBundle | The bundle to add
apiInstance.bundlesPostBundle(updateSystemModelsBundle, (error, data, response) => {
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
 **updateSystemModelsBundle** | [**UpdateSystemModelsBundle**](UpdateSystemModelsBundle.md)| The bundle to add | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## bundlesPutBundle

> bundlesPutBundle(ID, updateSystemModelsBundle)

Modify a Bundle in the Update System.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.BundlesApi();
let ID = "ID_example"; // String | The unique ID of the Bundle
let updateSystemModelsBundle = new AgcoApi.UpdateSystemModelsBundle(); // UpdateSystemModelsBundle | The bundle to modify
apiInstance.bundlesPutBundle(ID, updateSystemModelsBundle, (error, data, response) => {
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
 **ID** | **String**| The unique ID of the Bundle | 
 **updateSystemModelsBundle** | [**UpdateSystemModelsBundle**](UpdateSystemModelsBundle.md)| The bundle to modify | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

