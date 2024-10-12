# Tradeworks.StrategiesApi

All URIs are relative to *http://devui.magick.nu/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStrategiesStrategyIdStrategyId**](StrategiesApi.md#getStrategiesStrategyIdStrategyId) | **GET** /strategies/strategyId/{strategyId} | Get Strategy by ID
[**getStrategiesTemplates**](StrategiesApi.md#getStrategiesTemplates) | **GET** /strategies/templates | Get all Template Strategies



## getStrategiesStrategyIdStrategyId

> getStrategiesStrategyIdStrategyId(strategyId)

Get Strategy by ID

### Example

```javascript
import Tradeworks from 'tradeworks';

let apiInstance = new Tradeworks.StrategiesApi();
let strategyId = "strategyId_example"; // String | 
apiInstance.getStrategiesStrategyIdStrategyId(strategyId, (error, data, response) => {
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
 **strategyId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getStrategiesTemplates

> getStrategiesTemplates()

Get all Template Strategies

### Example

```javascript
import Tradeworks from 'tradeworks';

let apiInstance = new Tradeworks.StrategiesApi();
apiInstance.getStrategiesTemplates((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

