# AgcoApi.PackageTypetoBundlesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**packageTypetoBundlesDelete**](PackageTypetoBundlesApi.md#packageTypetoBundlesDelete) | **DELETE** /api/v2/PackageTypetoBundles | Delete a Package Type to Bundle Relationship.
[**packageTypetoBundlesGet**](PackageTypetoBundlesApi.md#packageTypetoBundlesGet) | **GET** /api/v2/PackageTypetoBundles | Get all of the Package Type to Bundle Relationships.
[**packageTypetoBundlesPost**](PackageTypetoBundlesApi.md#packageTypetoBundlesPost) | **POST** /api/v2/PackageTypetoBundles | Add a new Package Type ID to Bundle Relationship.
[**packageTypetoBundlesPut**](PackageTypetoBundlesApi.md#packageTypetoBundlesPut) | **PUT** /api/v2/PackageTypetoBundles | Update a Package Type ID to Bundle Relationship.



## packageTypetoBundlesDelete

> packageTypetoBundlesDelete(bundleID, packageTypeID)

Delete a Package Type to Bundle Relationship.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypetoBundlesApi();
let bundleID = "bundleID_example"; // String | The BundleID
let packageTypeID = "packageTypeID_example"; // String | The PackageTypeID
apiInstance.packageTypetoBundlesDelete(bundleID, packageTypeID, (error, data, response) => {
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
 **bundleID** | **String**| The BundleID | 
 **packageTypeID** | **String**| The PackageTypeID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## packageTypetoBundlesGet

> APIPagedResponseUpdateSystemModelsPackageTypeIDtoBundle packageTypetoBundlesGet(opts)

Get all of the Package Type to Bundle Relationships.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypetoBundlesApi();
let opts = {
  'bundleID': "bundleID_example", // String | Optional. Filter by BundleID.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.packageTypetoBundlesGet(opts, (error, data, response) => {
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
 **bundleID** | **String**| Optional. Filter by BundleID. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsPackageTypeIDtoBundle**](APIPagedResponseUpdateSystemModelsPackageTypeIDtoBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## packageTypetoBundlesPost

> packageTypetoBundlesPost(updateSystemModelsPackageTypeIDtoBundle)

Add a new Package Type ID to Bundle Relationship.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypetoBundlesApi();
let updateSystemModelsPackageTypeIDtoBundle = new AgcoApi.UpdateSystemModelsPackageTypeIDtoBundle(); // UpdateSystemModelsPackageTypeIDtoBundle | The PackageTypeToBundle to add.
apiInstance.packageTypetoBundlesPost(updateSystemModelsPackageTypeIDtoBundle, (error, data, response) => {
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
 **updateSystemModelsPackageTypeIDtoBundle** | [**UpdateSystemModelsPackageTypeIDtoBundle**](UpdateSystemModelsPackageTypeIDtoBundle.md)| The PackageTypeToBundle to add. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## packageTypetoBundlesPut

> packageTypetoBundlesPut(updateSystemModelsPackageTypeIDtoBundle)

Update a Package Type ID to Bundle Relationship.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PackageTypetoBundlesApi();
let updateSystemModelsPackageTypeIDtoBundle = new AgcoApi.UpdateSystemModelsPackageTypeIDtoBundle(); // UpdateSystemModelsPackageTypeIDtoBundle | The PackageTypeToBundle to update.
apiInstance.packageTypetoBundlesPut(updateSystemModelsPackageTypeIDtoBundle, (error, data, response) => {
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
 **updateSystemModelsPackageTypeIDtoBundle** | [**UpdateSystemModelsPackageTypeIDtoBundle**](UpdateSystemModelsPackageTypeIDtoBundle.md)| The PackageTypeToBundle to update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

