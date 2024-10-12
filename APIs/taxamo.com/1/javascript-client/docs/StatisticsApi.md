# Taxamo.StatisticsApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDailySettlementStats**](StatisticsApi.md#getDailySettlementStats) | **GET** /api/v1/stats/settlement/daily | Settlement stats over time
[**getSettlementStatsByCountry**](StatisticsApi.md#getSettlementStatsByCountry) | **GET** /api/v1/stats/settlement/by_country | Settlement by country
[**getSettlementStatsByTaxationType**](StatisticsApi.md#getSettlementStatsByTaxationType) | **GET** /api/v1/stats/settlement/by_taxation_type | Settlement by tax type
[**getTransactionsStats**](StatisticsApi.md#getTransactionsStats) | **GET** /api/v1/stats/transactions | Transaction stats
[**getTransactionsStatsByCountry**](StatisticsApi.md#getTransactionsStatsByCountry) | **GET** /api/v1/stats/transactions/by_country | Settlement by country



## getDailySettlementStats

> GetDailySettlementStatsOut getDailySettlementStats(interval, dateFrom, dateTo)

Settlement stats over time

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.StatisticsApi();
let interval = "interval_example"; // String | Interval type - day, week, month.
let dateFrom = "dateFrom_example"; // String | Date from in yyyy-MM format.
let dateTo = "dateTo_example"; // String | Date to in yyyy-MM format.
apiInstance.getDailySettlementStats(interval, dateFrom, dateTo, (error, data, response) => {
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
 **interval** | **String**| Interval type - day, week, month. | 
 **dateFrom** | **String**| Date from in yyyy-MM format. | 
 **dateTo** | **String**| Date to in yyyy-MM format. | 

### Return type

[**GetDailySettlementStatsOut**](GetDailySettlementStatsOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSettlementStatsByCountry

> GetSettlementStatsByCountryOut getSettlementStatsByCountry(dateFrom, dateTo)

Settlement by country

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.StatisticsApi();
let dateFrom = "dateFrom_example"; // String | Date from in yyyy-MM format.
let dateTo = "dateTo_example"; // String | Date to in yyyy-MM format.
apiInstance.getSettlementStatsByCountry(dateFrom, dateTo, (error, data, response) => {
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
 **dateFrom** | **String**| Date from in yyyy-MM format. | 
 **dateTo** | **String**| Date to in yyyy-MM format. | 

### Return type

[**GetSettlementStatsByCountryOut**](GetSettlementStatsByCountryOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSettlementStatsByTaxationType

> GetSettlementStatsByTaxationTypeOut getSettlementStatsByTaxationType(dateFrom, dateTo)

Settlement by tax type

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.StatisticsApi();
let dateFrom = "dateFrom_example"; // String | Date from in yyyy-MM format.
let dateTo = "dateTo_example"; // String | Date to in yyyy-MM format.
apiInstance.getSettlementStatsByTaxationType(dateFrom, dateTo, (error, data, response) => {
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
 **dateFrom** | **String**| Date from in yyyy-MM format. | 
 **dateTo** | **String**| Date to in yyyy-MM format. | 

### Return type

[**GetSettlementStatsByTaxationTypeOut**](GetSettlementStatsByTaxationTypeOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionsStats

> GetTransactionsStatsOut getTransactionsStats(dateFrom, dateTo, opts)

Transaction stats

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.StatisticsApi();
let dateFrom = "dateFrom_example"; // String | Date from in yyyy-MM format.
let dateTo = "dateTo_example"; // String | Date to in yyyy-MM format.
let opts = {
  'interval': "interval_example" // String | Interval. Accepted values are 'day', 'week' and 'month'.
};
apiInstance.getTransactionsStats(dateFrom, dateTo, opts, (error, data, response) => {
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
 **dateFrom** | **String**| Date from in yyyy-MM format. | 
 **dateTo** | **String**| Date to in yyyy-MM format. | 
 **interval** | **String**| Interval. Accepted values are &#39;day&#39;, &#39;week&#39; and &#39;month&#39;. | [optional] 

### Return type

[**GetTransactionsStatsOut**](GetTransactionsStatsOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionsStatsByCountry

> GetTransactionsStatsByCountryOut getTransactionsStatsByCountry(dateFrom, dateTo, opts)

Settlement by country

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.StatisticsApi();
let dateFrom = "dateFrom_example"; // String | Date from in yyyy-MM format.
let dateTo = "dateTo_example"; // String | Date to in yyyy-MM format.
let opts = {
  'globalCurrencyCode': "globalCurrencyCode_example" // String | Global currency code to use for conversion - in addition to country's currency if rate is available. Conversion is indicative and based on most-recent rate from ECB.
};
apiInstance.getTransactionsStatsByCountry(dateFrom, dateTo, opts, (error, data, response) => {
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
 **dateFrom** | **String**| Date from in yyyy-MM format. | 
 **dateTo** | **String**| Date to in yyyy-MM format. | 
 **globalCurrencyCode** | **String**| Global currency code to use for conversion - in addition to country&#39;s currency if rate is available. Conversion is indicative and based on most-recent rate from ECB. | [optional] 

### Return type

[**GetTransactionsStatsByCountryOut**](GetTransactionsStatsByCountryOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

