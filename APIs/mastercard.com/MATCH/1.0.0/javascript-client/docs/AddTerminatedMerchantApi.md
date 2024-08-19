# MatchApi.AddTerminatedMerchantApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fraudMerchantV3AddMerchantPost**](AddTerminatedMerchantApi.md#fraudMerchantV3AddMerchantPost) | **POST** /fraud/merchant/v3/add-merchant | Used by Acquirers to add a terminated a merchant in the MATCH system. Merchant information, and up to five principal owners per merchant, can be provided by an acquiring bank as part of the listing.



## fraudMerchantV3AddMerchantPost

> AddTerminatedMerchantResponseSchema fraudMerchantV3AddMerchantPost(addTerminatedMerchantRequestSchema)

Used by Acquirers to add a terminated a merchant in the MATCH system. Merchant information, and up to five principal owners per merchant, can be provided by an acquiring bank as part of the listing.

Used by Acquirers to add a terminated a merchant in the MATCH system. Merchant information, and up to five principal owners per merchant, can be provided by an acquiring bank as part of the listing. 

### Example

```javascript
import MatchApi from 'match_api';

let apiInstance = new MatchApi.AddTerminatedMerchantApi();
let addTerminatedMerchantRequestSchema = new MatchApi.AddTerminatedMerchantRequestSchema(); // AddTerminatedMerchantRequestSchema | Body of the Add Terminated Merchant Request
apiInstance.fraudMerchantV3AddMerchantPost(addTerminatedMerchantRequestSchema, (error, data, response) => {
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
 **addTerminatedMerchantRequestSchema** | [**AddTerminatedMerchantRequestSchema**](AddTerminatedMerchantRequestSchema.md)| Body of the Add Terminated Merchant Request | 

### Return type

[**AddTerminatedMerchantResponseSchema**](AddTerminatedMerchantResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

