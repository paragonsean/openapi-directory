# AgcoApi.LicensesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2LicensesIDGet**](LicensesApi.md#apiV2LicensesIDGet) | **GET** /api/v2/Licenses/{ID} | Get a license.
[**licensesGet**](LicensesApi.md#licensesGet) | **GET** /api/v2/Licenses | Gets a list of licenses with the specified criteria.



## apiV2LicensesIDGet

> DealerDBModelsLicense apiV2LicensesIDGet(ID)

Get a license.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LicensesApi();
let ID = "ID_example"; // String | The ID of the license to get.
apiInstance.apiV2LicensesIDGet(ID, (error, data, response) => {
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
 **ID** | **String**| The ID of the license to get. | 

### Return type

[**DealerDBModelsLicense**](DealerDBModelsLicense.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## licensesGet

> APIPagedResponseDealerDBModelsLicense licensesGet(opts)

Gets a list of licenses with the specified criteria.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LicensesApi();
let opts = {
  'voucherCode': "voucherCode_example", // String | Optional. Filter by VoucherCode
  'dealerCode': "dealerCode_example", // String | Optional. Filter by DealerCode
  'status': "status_example", // String | Optional. Filter by Status.  By default only active licenses will be returned.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.licensesGet(opts, (error, data, response) => {
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
 **voucherCode** | **String**| Optional. Filter by VoucherCode | [optional] 
 **dealerCode** | **String**| Optional. Filter by DealerCode | [optional] 
 **status** | **String**| Optional. Filter by Status.  By default only active licenses will be returned. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseDealerDBModelsLicense**](APIPagedResponseDealerDBModelsLicense.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

