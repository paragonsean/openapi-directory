# AgcoApi.PackageTypesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2PackageTypesIDGet**](PackageTypesApi.md#apiV2PackageTypesIDGet) | **GET** /api/v2/PackageTypes/{ID} | Get a specific Package Type.
[**packageTypesAddPackageTypeUser**](PackageTypesApi.md#packageTypesAddPackageTypeUser) | **POST** /api/v2/PackageTypes/{id}/Users/{userID} | Add a package type that a user can see.
[**packageTypesDelete**](PackageTypesApi.md#packageTypesDelete) | **DELETE** /api/v2/PackageTypes/{ID} | Delete a Package Type.
[**packageTypesGet**](PackageTypesApi.md#packageTypesGet) | **GET** /api/v2/PackageTypes | Get all of the Package Types.
[**packageTypesPost**](PackageTypesApi.md#packageTypesPost) | **POST** /api/v2/PackageTypes | Add a Package Type.
[**packageTypesPut**](PackageTypesApi.md#packageTypesPut) | **PUT** /api/v2/PackageTypes/{ID} | Modify a Package Type.
[**packageTypesRemovePackageTypeUser**](PackageTypesApi.md#packageTypesRemovePackageTypeUser) | **DELETE** /api/v2/PackageTypes/{id}/Users/{userID} | Deletes a package type a user could see.



## apiV2PackageTypesIDGet

> UpdateSystemModelsPackageType apiV2PackageTypesIDGet(ID)

Get a specific Package Type.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypesApi();
let ID = "ID_example"; // String | The Package Type ID
apiInstance.apiV2PackageTypesIDGet(ID, (error, data, response) => {
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
 **ID** | **String**| The Package Type ID | 

### Return type

[**UpdateSystemModelsPackageType**](UpdateSystemModelsPackageType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## packageTypesAddPackageTypeUser

> packageTypesAddPackageTypeUser(id, userID)

Add a package type that a user can see.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypesApi();
let id = "id_example"; // String | The ID of the Package Type
let userID = 56; // Number | The userID to link to the package type
apiInstance.packageTypesAddPackageTypeUser(id, userID, (error, data, response) => {
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
 **id** | **String**| The ID of the Package Type | 
 **userID** | **Number**| The userID to link to the package type | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## packageTypesDelete

> packageTypesDelete(ID)

Delete a Package Type.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypesApi();
let ID = "ID_example"; // String | The Package Type ID
apiInstance.packageTypesDelete(ID, (error, data, response) => {
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
 **ID** | **String**| The Package Type ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## packageTypesGet

> APIPagedResponseUpdateSystemModelsPackageType packageTypesGet(opts)

Get all of the Package Types.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypesApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56, // Number | Optional. The page offset. The default page offset is 0.
  'userID': 56 // Number | Optional. The user ID to sort packageTypes by the user's access
};
apiInstance.packageTypesGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 
 **userID** | **Number**| Optional. The user ID to sort packageTypes by the user&#39;s access | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsPackageType**](APIPagedResponseUpdateSystemModelsPackageType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## packageTypesPost

> String packageTypesPost(updateSystemModelsPackageType)

Add a Package Type.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypesApi();
let updateSystemModelsPackageType = new AgcoApi.UpdateSystemModelsPackageType(); // UpdateSystemModelsPackageType | The Package Type to add
apiInstance.packageTypesPost(updateSystemModelsPackageType, (error, data, response) => {
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
 **updateSystemModelsPackageType** | [**UpdateSystemModelsPackageType**](UpdateSystemModelsPackageType.md)| The Package Type to add | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## packageTypesPut

> packageTypesPut(ID, updateSystemModelsPackageType)

Modify a Package Type.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypesApi();
let ID = "ID_example"; // String | The ID of the Package Type
let updateSystemModelsPackageType = new AgcoApi.UpdateSystemModelsPackageType(); // UpdateSystemModelsPackageType | The Package Type to update
apiInstance.packageTypesPut(ID, updateSystemModelsPackageType, (error, data, response) => {
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
 **ID** | **String**| The ID of the Package Type | 
 **updateSystemModelsPackageType** | [**UpdateSystemModelsPackageType**](UpdateSystemModelsPackageType.md)| The Package Type to update | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## packageTypesRemovePackageTypeUser

> packageTypesRemovePackageTypeUser(id, userID)

Deletes a package type a user could see.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypesApi();
let id = "id_example"; // String | The ID of the Package Type
let userID = 56; // Number | The userID to link to the package type
apiInstance.packageTypesRemovePackageTypeUser(id, userID, (error, data, response) => {
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
 **id** | **String**| The ID of the Package Type | 
 **userID** | **Number**| The userID to link to the package type | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

