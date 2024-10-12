# YodleeCoreApis.HoldingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssetClassificationList**](HoldingsApi.md#getAssetClassificationList) | **GET** /holdings/assetClassificationList | Get Asset Classification List
[**getHoldingTypeList**](HoldingsApi.md#getHoldingTypeList) | **GET** /holdings/holdingTypeList | Get Holding Type List
[**getHoldings**](HoldingsApi.md#getHoldings) | **GET** /holdings | Get Holdings
[**getSecurities**](HoldingsApi.md#getSecurities) | **GET** /holdings/securities | Get Security Details



## getAssetClassificationList

> HoldingAssetClassificationListResponse getAssetClassificationList()

Get Asset Classification List

The get asset classifications list service is used to get the supported asset classifications. &lt;br&gt;The response includes different classification types like assetClass, country, sector, style, etc. and the values corresponding to each type.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.HoldingsApi();
apiInstance.getAssetClassificationList((error, data, response) => {
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

[**HoldingAssetClassificationListResponse**](HoldingAssetClassificationListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getHoldingTypeList

> HoldingTypeListResponse getHoldingTypeList()

Get Holding Type List

The get holding types list service is used to get the supported holding types.&lt;br&gt;The response includes different holding types such as future, moneyMarketFund, stock, etc. and it returns the supported holding types &lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.HoldingsApi();
apiInstance.getHoldingTypeList((error, data, response) => {
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

[**HoldingTypeListResponse**](HoldingTypeListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getHoldings

> HoldingResponse getHoldings(opts)

Get Holdings

The get holdings service is used to get the list of holdings of a user.&lt;br&gt;Supported holding types can be employeeStockOption, moneyMarketFund, bond, etc. and is obtained using get holding type list service. &lt;br&gt;Asset classifications for the holdings need to be requested through the \&quot;include\&quot; parameter.&lt;br&gt;Asset classification information for holdings are not available by default, as it is a premium feature.&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.HoldingsApi();
let opts = {
  'accountId': "accountId_example", // String | Comma separated accountId
  'assetClassificationClassificationType': "assetClassificationClassificationType_example", // String | e.g. Country, Sector, etc.
  'classificationValue': "classificationValue_example", // String | e.g. US
  'include': "include_example", // String | assetClassification
  'providerAccountId': "providerAccountId_example" // String | providerAccountId
};
apiInstance.getHoldings(opts, (error, data, response) => {
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
 **accountId** | **String**| Comma separated accountId | [optional] 
 **assetClassificationClassificationType** | **String**| e.g. Country, Sector, etc. | [optional] 
 **classificationValue** | **String**| e.g. US | [optional] 
 **include** | **String**| assetClassification | [optional] 
 **providerAccountId** | **String**| providerAccountId | [optional] 

### Return type

[**HoldingResponse**](HoldingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## getSecurities

> HoldingSecuritiesResponse getSecurities(opts)

Get Security Details

The get security details service is used to get all the security information for the holdings&lt;br&gt;

### Example

```javascript
import YodleeCoreApis from 'yodlee_core_apis';

let apiInstance = new YodleeCoreApis.HoldingsApi();
let opts = {
  'holdingId': "holdingId_example" // String | Comma separated holdingId
};
apiInstance.getSecurities(opts, (error, data, response) => {
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
 **holdingId** | **String**| Comma separated holdingId | [optional] 

### Return type

[**HoldingSecuritiesResponse**](HoldingSecuritiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

