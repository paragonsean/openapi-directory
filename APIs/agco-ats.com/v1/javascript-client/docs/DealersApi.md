# AgcoApi.DealersApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dealersGetDealerbyDealerCode**](DealersApi.md#dealersGetDealerbyDealerCode) | **GET** /api/v2/Dealers/{DealerCode} | Lookup a dealer using a dealer code.
[**dealersGetDealers**](DealersApi.md#dealersGetDealers) | **GET** /api/v2/Dealers | Get a list of dealers.



## dealersGetDealerbyDealerCode

> DealerDBModelsDealer dealersGetDealerbyDealerCode(dealerCode)

Lookup a dealer using a dealer code.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.DealersApi();
let dealerCode = "dealerCode_example"; // String | The Dealer Code to Search for
apiInstance.dealersGetDealerbyDealerCode(dealerCode, (error, data, response) => {
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
 **dealerCode** | **String**| The Dealer Code to Search for | 

### Return type

[**DealerDBModelsDealer**](DealerDBModelsDealer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## dealersGetDealers

> APIPagedResponseDealerDBModelsDealer dealersGetDealers(opts)

Get a list of dealers.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.DealersApi();
let opts = {
  'brand': "brand_example", // String | The brand to filter by.
  'shippingCountry': "shippingCountry_example", // String | The country to filter by.
  'dealerName': "dealerName_example", // String | The partial Dealer Name to filter by. Wildcard supported (*).
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.dealersGetDealers(opts, (error, data, response) => {
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
 **brand** | **String**| The brand to filter by. | [optional] 
 **shippingCountry** | **String**| The country to filter by. | [optional] 
 **dealerName** | **String**| The partial Dealer Name to filter by. Wildcard supported (*). | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseDealerDBModelsDealer**](APIPagedResponseDealerDBModelsDealer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

