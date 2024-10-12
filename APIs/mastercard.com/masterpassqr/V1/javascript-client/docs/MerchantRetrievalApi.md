# SendPersonToMerchant.MerchantRetrievalApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMerchantTransferById**](MerchantRetrievalApi.md#getMerchantTransferById) | **GET** /send/#env/v1/partners/{partnerId}/merchant/transfers/{transferId} | Purpose of this service is to retrieve the Transfer resource associated with the specified transfer-id.
[**getMerchantTransferByRef**](MerchantRetrievalApi.md#getMerchantTransferByRef) | **GET** /send/#env/v1/partners/{partnerId}/merchant/transfers | Purpose of this service is to retrieve the Transfer resource associated with a specified transfer_reference value.



## getMerchantTransferById

> MerchantTransfer54Wrapper getMerchantTransferById(partnerId, transferId)

Purpose of this service is to retrieve the Transfer resource associated with the specified transfer-id.

Purpose of this service is to retrieve the Transfer resource associated with the specified transfer-id.

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.MerchantRetrievalApi();
let partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
let transferId = "transferId_example"; // String | Path Param - Valid transfer id
apiInstance.getMerchantTransferById(partnerId, transferId, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | 
 **transferId** | **String**| Path Param - Valid transfer id | 

### Return type

[**MerchantTransfer54Wrapper**](MerchantTransfer54Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getMerchantTransferByRef

> MerchantTransfers69Wrapper getMerchantTransferByRef(partnerId, ref)

Purpose of this service is to retrieve the Transfer resource associated with a specified transfer_reference value.

Purpose of this service is to retrieve the Transfer resource associated with a specified transfer_reference value.

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.MerchantRetrievalApi();
let partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
let ref = "ref_example"; // String | Query Param - Is the client specified transfer reference when initiating the transfer. Allowable characters are alphanumeric and * , - . _ ~. Details- 6-40 Example- DEF123456
apiInstance.getMerchantTransferByRef(partnerId, ref, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | 
 **ref** | **String**| Query Param - Is the client specified transfer reference when initiating the transfer. Allowable characters are alphanumeric and * , - . _ ~. Details- 6-40 Example- DEF123456 | 

### Return type

[**MerchantTransfers69Wrapper**](MerchantTransfers69Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

