# MasterCardBinTableListing.BINTableListingServiceApi

All URIs are relative to *https://api.mastercard.com/fraud/mtf/bintable/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**binlistingGet**](BINTableListingServiceApi.md#binlistingGet) | **GET** /binlisting | BIN Table Listing file



## binlistingGet

> BinTableResponse binlistingGet()

BIN Table Listing file

REST service will retrieve and return the BIN Table file to Merchants.

### Example

```javascript
import MasterCardBinTableListing from 'master_card_bin_table_listing';

let apiInstance = new MasterCardBinTableListing.BINTableListingServiceApi();
apiInstance.binlistingGet((error, data, response) => {
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

[**BinTableResponse**](BinTableResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

