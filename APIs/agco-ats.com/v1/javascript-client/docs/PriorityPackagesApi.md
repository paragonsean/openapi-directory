# AgcoApi.PriorityPackagesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**priorityPackagesDeletePriorityPackages**](PriorityPackagesApi.md#priorityPackagesDeletePriorityPackages) | **DELETE** /api/v2/PriorityPackages/{ID} | Delete a Priority Package for a Client.
[**priorityPackagesGetPriorityPackage**](PriorityPackagesApi.md#priorityPackagesGetPriorityPackage) | **GET** /api/v2/PriorityPackages/{ID} | Get a Priority Packages for a Client.
[**priorityPackagesGetPriorityPackages**](PriorityPackagesApi.md#priorityPackagesGetPriorityPackages) | **GET** /api/v2/PriorityPackages | Get a list of Priority Packages by Client.
[**priorityPackagesPostPriorityPackages**](PriorityPackagesApi.md#priorityPackagesPostPriorityPackages) | **POST** /api/v2/PriorityPackages | Add a Priority Package for a Client.



## priorityPackagesDeletePriorityPackages

> priorityPackagesDeletePriorityPackages(ID)

Delete a Priority Package for a Client.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PriorityPackagesApi();
let ID = "ID_example"; // String | The Priority Package ID
apiInstance.priorityPackagesDeletePriorityPackages(ID, (error, data, response) => {
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
 **ID** | **String**| The Priority Package ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## priorityPackagesGetPriorityPackage

> UpdateSystemModelsPriorityPackage priorityPackagesGetPriorityPackage(ID)

Get a Priority Packages for a Client.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PriorityPackagesApi();
let ID = "ID_example"; // String | The Priority Package ID
apiInstance.priorityPackagesGetPriorityPackage(ID, (error, data, response) => {
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
 **ID** | **String**| The Priority Package ID | 

### Return type

[**UpdateSystemModelsPriorityPackage**](UpdateSystemModelsPriorityPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## priorityPackagesGetPriorityPackages

> APIPagedResponseUpdateSystemModelsPriorityPackage priorityPackagesGetPriorityPackages(opts)

Get a list of Priority Packages by Client.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PriorityPackagesApi();
let opts = {
  'clientID': "clientID_example", // String | Optional. Filter priority packages by ClientID.
  'status': "status_example", // String | Optional. Filter returned packages by status. By default only active packages will be returned.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.priorityPackagesGetPriorityPackages(opts, (error, data, response) => {
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
 **clientID** | **String**| Optional. Filter priority packages by ClientID. | [optional] 
 **status** | **String**| Optional. Filter returned packages by status. By default only active packages will be returned. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsPriorityPackage**](APIPagedResponseUpdateSystemModelsPriorityPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## priorityPackagesPostPriorityPackages

> String priorityPackagesPostPriorityPackages(updateSystemModelsPriorityPackage)

Add a Priority Package for a Client.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.PriorityPackagesApi();
let updateSystemModelsPriorityPackage = new AgcoApi.UpdateSystemModelsPriorityPackage(); // UpdateSystemModelsPriorityPackage | The PriorityPackage to add
apiInstance.priorityPackagesPostPriorityPackages(updateSystemModelsPriorityPackage, (error, data, response) => {
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
 **updateSystemModelsPriorityPackage** | [**UpdateSystemModelsPriorityPackage**](UpdateSystemModelsPriorityPackage.md)| The PriorityPackage to add | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

