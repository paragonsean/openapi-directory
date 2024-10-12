# AgcoApi.PackagesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**packagesDeletePackage**](PackagesApi.md#packagesDeletePackage) | **DELETE** /api/v2/Packages/{ID} | Delete a Package.
[**packagesGetPackage**](PackagesApi.md#packagesGetPackage) | **GET** /api/v2/Packages/{ID} | Find a Package.
[**packagesGetPackages**](PackagesApi.md#packagesGetPackages) | **GET** /api/v2/Packages | List Packages.
[**packagesPostPackage**](PackagesApi.md#packagesPostPackage) | **POST** /api/v2/Packages | Add a Package to the Update System.
[**packagesPutPackage**](PackagesApi.md#packagesPutPackage) | **PUT** /api/v2/Packages/{ID} | Modify a Packge to the Update System.



## packagesDeletePackage

> packagesDeletePackage(ID)

Delete a Package.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackagesApi();
let ID = "ID_example"; // String | The Package ID to Delete
apiInstance.packagesDeletePackage(ID, (error, data, response) => {
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
 **ID** | **String**| The Package ID to Delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## packagesGetPackage

> UpdateSystemModelsPackage packagesGetPackage(ID)

Find a Package.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackagesApi();
let ID = "ID_example"; // String | The Package ID to Search for
apiInstance.packagesGetPackage(ID, (error, data, response) => {
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
 **ID** | **String**| The Package ID to Search for | 

### Return type

[**UpdateSystemModelsPackage**](UpdateSystemModelsPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## packagesGetPackages

> APIPagedResponseUpdateSystemModelsPackage packagesGetPackages(opts)

List Packages.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackagesApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56, // Number | Optional. The page offset. The default page offset is 0.
  'packageTypeID': "packageTypeID_example", // String | Optional. If provided, filters by PackageTypeID.
  'version': 56, // Number | Optional. If provided, filters by Version.
  'released': true // Boolean | Optional. If provided, filters by Released.
};
apiInstance.packagesGetPackages(opts, (error, data, response) => {
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
 **packageTypeID** | **String**| Optional. If provided, filters by PackageTypeID. | [optional] 
 **version** | **Number**| Optional. If provided, filters by Version. | [optional] 
 **released** | **Boolean**| Optional. If provided, filters by Released. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsPackage**](APIPagedResponseUpdateSystemModelsPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## packagesPostPackage

> String packagesPostPackage(updateSystemModelsPackage)

Add a Package to the Update System.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackagesApi();
let updateSystemModelsPackage = new AgcoApi.UpdateSystemModelsPackage(); // UpdateSystemModelsPackage | The package to add.
apiInstance.packagesPostPackage(updateSystemModelsPackage, (error, data, response) => {
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
 **updateSystemModelsPackage** | [**UpdateSystemModelsPackage**](UpdateSystemModelsPackage.md)| The package to add. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## packagesPutPackage

> packagesPutPackage(ID, updateSystemModelsPackage)

Modify a Packge to the Update System.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackagesApi();
let ID = "ID_example"; // String | The unique ID of the Package
let updateSystemModelsPackage = new AgcoApi.UpdateSystemModelsPackage(); // UpdateSystemModelsPackage | The package to update.
apiInstance.packagesPutPackage(ID, updateSystemModelsPackage, (error, data, response) => {
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
 **ID** | **String**| The unique ID of the Package | 
 **updateSystemModelsPackage** | [**UpdateSystemModelsPackage**](UpdateSystemModelsPackage.md)| The package to update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

