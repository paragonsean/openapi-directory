# AgcoApi.VouchersApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2VouchersVoucherCodeGet**](VouchersApi.md#apiV2VouchersVoucherCodeGet) | **GET** /api/v2/Vouchers/{VoucherCode} | Get a voucher
[**vouchersDelete**](VouchersApi.md#vouchersDelete) | **DELETE** /api/v2/Vouchers/{VoucherCode} | Delete a voucher
[**vouchersGet**](VouchersApi.md#vouchersGet) | **GET** /api/v2/Vouchers | Gets a list of vouchers
[**vouchersGetVoucherHistory**](VouchersApi.md#vouchersGetVoucherHistory) | **GET** /api/v2/Vouchers/{VoucherCode}/VoucherHistory | Get a voucher&#39;s history.
[**vouchersPost**](VouchersApi.md#vouchersPost) | **POST** /api/v2/Vouchers | Create a voucher
[**vouchersPut**](VouchersApi.md#vouchersPut) | **PUT** /api/v2/Vouchers/{VoucherCode} | Update a voucher



## apiV2VouchersVoucherCodeGet

> DealerDBModelsVoucher apiV2VouchersVoucherCodeGet(voucherCode, opts)

Get a voucher

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.VouchersApi();
let voucherCode = "voucherCode_example"; // String | The voucher code of the voucher to get.
let opts = {
  'deleted': "deleted_example" // String | Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.
};
apiInstance.apiV2VouchersVoucherCodeGet(voucherCode, opts, (error, data, response) => {
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
 **voucherCode** | **String**| The voucher code of the voucher to get. | 
 **deleted** | **String**| Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned. | [optional] 

### Return type

[**DealerDBModelsVoucher**](DealerDBModelsVoucher.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## vouchersDelete

> vouchersDelete(voucherCode)

Delete a voucher

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.VouchersApi();
let voucherCode = "voucherCode_example"; // String | The voucher code of the voucher to delete.
apiInstance.vouchersDelete(voucherCode, (error, data, response) => {
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
 **voucherCode** | **String**| The voucher code of the voucher to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vouchersGet

> APIPagedResponseDealerDBModelsVoucher vouchersGet(opts)

Gets a list of vouchers

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.VouchersApi();
let opts = {
  'type': "type_example", // String | Optional. Filter vouchers by Type
  'dealerCode': "dealerCode_example", // String | Optional. Filter vouchers by DealerCode
  'licenseTo': "licenseTo_example", // String | Optional. Filter vouchers by LicenseTo. Wildcard supported (*).
  'purpose': "purpose_example", // String | Optional. Filter vouchers by Purpose. Wildcard supported (*).
  'orderNumber': "orderNumber_example", // String | Optional. Filter vouchers by OrderNumber
  'email': "email_example", // String | Optional. Filter vouchers by Email. Wildcard supported (*).
  'modifiedBy': "modifiedBy_example", // String | Optional. Filter vouchers by ModifiedBy
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Filter vouchers by CreatedDate
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Filter vouchers by CreatedDate
  'punchedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Filter vouchers by PunchedDate
  'punchedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Filter vouchers by PunchedDate
  'punched': true, // Boolean | Optional. Filter vouchers by Punched status
  'expirationAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Filter vouchers by ExpirationDate
  'expirationBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Filter vouchers by ExpirationDate
  'deleted': "deleted_example", // String | Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.vouchersGet(opts, (error, data, response) => {
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
 **type** | **String**| Optional. Filter vouchers by Type | [optional] 
 **dealerCode** | **String**| Optional. Filter vouchers by DealerCode | [optional] 
 **licenseTo** | **String**| Optional. Filter vouchers by LicenseTo. Wildcard supported (*). | [optional] 
 **purpose** | **String**| Optional. Filter vouchers by Purpose. Wildcard supported (*). | [optional] 
 **orderNumber** | **String**| Optional. Filter vouchers by OrderNumber | [optional] 
 **email** | **String**| Optional. Filter vouchers by Email. Wildcard supported (*). | [optional] 
 **modifiedBy** | **String**| Optional. Filter vouchers by ModifiedBy | [optional] 
 **createdAfter** | **Date**| Optional. Filter vouchers by CreatedDate | [optional] 
 **createdBefore** | **Date**| Optional. Filter vouchers by CreatedDate | [optional] 
 **punchedAfter** | **Date**| Optional. Filter vouchers by PunchedDate | [optional] 
 **punchedBefore** | **Date**| Optional. Filter vouchers by PunchedDate | [optional] 
 **punched** | **Boolean**| Optional. Filter vouchers by Punched status | [optional] 
 **expirationAfter** | **Date**| Optional. Filter vouchers by ExpirationDate | [optional] 
 **expirationBefore** | **Date**| Optional. Filter vouchers by ExpirationDate | [optional] 
 **deleted** | **String**| Optional. Filter vouchers by Deleted state. By default only vouchers that are not deleted are returned. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseDealerDBModelsVoucher**](APIPagedResponseDealerDBModelsVoucher.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## vouchersGetVoucherHistory

> APIPagedResponseDealerDBModelsVoucherHistory vouchersGetVoucherHistory(voucherCode, opts)

Get a voucher&#39;s history.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.VouchersApi();
let voucherCode = "voucherCode_example"; // String | The voucher code to get history for.
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.vouchersGetVoucherHistory(voucherCode, opts, (error, data, response) => {
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
 **voucherCode** | **String**| The voucher code to get history for. | 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseDealerDBModelsVoucherHistory**](APIPagedResponseDealerDBModelsVoucherHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## vouchersPost

> String vouchersPost(dealerDBModelsVoucher)

Create a voucher

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.VouchersApi();
let dealerDBModelsVoucher = new AgcoApi.DealerDBModelsVoucher(); // DealerDBModelsVoucher | The voucher to add.
apiInstance.vouchersPost(dealerDBModelsVoucher, (error, data, response) => {
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
 **dealerDBModelsVoucher** | [**DealerDBModelsVoucher**](DealerDBModelsVoucher.md)| The voucher to add. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## vouchersPut

> vouchersPut(voucherCode, dealerDBModelsVoucher)

Update a voucher

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.VouchersApi();
let voucherCode = "voucherCode_example"; // String | The voucher code of the voucher to update.
let dealerDBModelsVoucher = new AgcoApi.DealerDBModelsVoucher(); // DealerDBModelsVoucher | The updated voucher.
apiInstance.vouchersPut(voucherCode, dealerDBModelsVoucher, (error, data, response) => {
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
 **voucherCode** | **String**| The voucher code of the voucher to update. | 
 **dealerDBModelsVoucher** | [**DealerDBModelsVoucher**](DealerDBModelsVoucher.md)| The updated voucher. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined

