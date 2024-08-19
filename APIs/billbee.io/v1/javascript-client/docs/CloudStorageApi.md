# BillbeeApi.CloudStorageApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudStorageApiGetList**](CloudStorageApi.md#cloudStorageApiGetList) | **GET** /api/v1/cloudstorages | Gets a list of all connected cloud storage devices



## cloudStorageApiGetList

> RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel cloudStorageApiGetList()

Gets a list of all connected cloud storage devices

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CloudStorageApi();
apiInstance.cloudStorageApiGetList((error, data, response) => {
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

[**RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel**](RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

