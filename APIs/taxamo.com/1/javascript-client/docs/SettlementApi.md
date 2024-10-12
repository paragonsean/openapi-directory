# Taxamo.SettlementApi

All URIs are relative to *https://api.taxamo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDetailedRefunds**](SettlementApi.md#getDetailedRefunds) | **GET** /api/v1/settlement/detailed_refunds | Detailed refunds
[**getRefunds**](SettlementApi.md#getRefunds) | **GET** /api/v1/settlement/refunds | Fetch refunds
[**getSettlement**](SettlementApi.md#getSettlement) | **GET** /api/v1/settlement/{quarter} | Fetch settlement
[**getSettlementSummary**](SettlementApi.md#getSettlementSummary) | **GET** /api/v1/settlement/summary/{quarter} | Fetch summary



## getDetailedRefunds

> GetDetailedRefundsOut getDetailedRefunds(opts)

Detailed refunds

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.SettlementApi();
let opts = {
  'format': "format_example", // String | Output format. 'json' or 'csv'. Default value is 'json'
  'countryCodes': "countryCodes_example", // String | Comma separated list of 2-letter country codes
  'dateFrom': "dateFrom_example", // String | Take only refunds issued at or after the date. Format: yyyy-MM-dd
  'dateTo': "dateTo_example", // String | Take only refunds issued at or before the date. Format: yyyy-MM-dd
  'limit': 3.4, // Number | Limit (no more than 1000, defaults to 100).
  'offset': 3.4 // Number | Offset. Defaults to 0
};
apiInstance.getDetailedRefunds(opts, (error, data, response) => {
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
 **format** | **String**| Output format. &#39;json&#39; or &#39;csv&#39;. Default value is &#39;json&#39; | [optional] 
 **countryCodes** | **String**| Comma separated list of 2-letter country codes | [optional] 
 **dateFrom** | **String**| Take only refunds issued at or after the date. Format: yyyy-MM-dd | [optional] 
 **dateTo** | **String**| Take only refunds issued at or before the date. Format: yyyy-MM-dd | [optional] 
 **limit** | **Number**| Limit (no more than 1000, defaults to 100). | [optional] 
 **offset** | **Number**| Offset. Defaults to 0 | [optional] 

### Return type

[**GetDetailedRefundsOut**](GetDetailedRefundsOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRefunds

> GetRefundsOut getRefunds(dateFrom, opts)

Fetch refunds

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.SettlementApi();
let dateFrom = "dateFrom_example"; // String | Take only refunds issued at or after the date. Format: yyyy-MM-dd
let opts = {
  'format': "format_example", // String | Output format. 'csv' value is accepted as well
  'mossCountryCode': "mossCountryCode_example", // String | MOSS country code, used to determine currency. If ommited, merchant default setting is used.
  'taxRegion': "taxRegion_example" // String | Tax region key, defaults to EU for backwards compatibility.
};
apiInstance.getRefunds(dateFrom, opts, (error, data, response) => {
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
 **dateFrom** | **String**| Take only refunds issued at or after the date. Format: yyyy-MM-dd | 
 **format** | **String**| Output format. &#39;csv&#39; value is accepted as well | [optional] 
 **mossCountryCode** | **String**| MOSS country code, used to determine currency. If ommited, merchant default setting is used. | [optional] 
 **taxRegion** | **String**| Tax region key, defaults to EU for backwards compatibility. | [optional] 

### Return type

[**GetRefundsOut**](GetRefundsOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSettlement

> GetSettlementOut getSettlement(quarter, opts)

Fetch settlement

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.SettlementApi();
let quarter = "quarter_example"; // String | Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to 'range'.
let opts = {
  'mossTaxId': "mossTaxId_example", // String | MOSS-assigned tax ID - if not provided, merchant's national tax number will be used. Deprecated, please use tax-id.
  'currencyCode': "currencyCode_example", // String | ISO 3-letter currency code, e.g. EUR or USD. If provided, all amounts will be coerced for this currency. Defaults to region's currency code.
  'endMonth': "endMonth_example", // String | Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
  'taxId': "taxId_example", // String | MOSS-assigned tax ID - if not provided, merchant's national tax number will be used. Deprecated, please use tax-id.
  'refundDateKindOverride': "refundDateKindOverride_example", // String | Set to 'order_date' to show only refunds for the transactions in the selected reporting period. Set to 'refund_timestamp' to show refunds that were created in the selected reporting period. Do not set to use the default region's setting.
  'startMonth': "startMonth_example", // String | Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
  'mossCountryCode': "mossCountryCode_example", // String | MOSS country code, used to determine currency/region. If ommited, merchant default setting is used. Deprecated: please use tax-country-code.
  'format': "format_example", // String | Output format. 'csv' value is accepted as well
  'taxCountryCode': "taxCountryCode_example" // String | Tax entity country code, used to determine currency/region. 
};
apiInstance.getSettlement(quarter, opts, (error, data, response) => {
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
 **quarter** | **String**| Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to &#39;range&#39;. | 
 **mossTaxId** | **String**| MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. Deprecated, please use tax-id. | [optional] 
 **currencyCode** | **String**| ISO 3-letter currency code, e.g. EUR or USD. If provided, all amounts will be coerced for this currency. Defaults to region&#39;s currency code. | [optional] 
 **endMonth** | **String**| Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided. | [optional] 
 **taxId** | **String**| MOSS-assigned tax ID - if not provided, merchant&#39;s national tax number will be used. Deprecated, please use tax-id. | [optional] 
 **refundDateKindOverride** | **String**| Set to &#39;order_date&#39; to show only refunds for the transactions in the selected reporting period. Set to &#39;refund_timestamp&#39; to show refunds that were created in the selected reporting period. Do not set to use the default region&#39;s setting. | [optional] 
 **startMonth** | **String**| Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided. | [optional] 
 **mossCountryCode** | **String**| MOSS country code, used to determine currency/region. If ommited, merchant default setting is used. Deprecated: please use tax-country-code. | [optional] 
 **format** | **String**| Output format. &#39;csv&#39; value is accepted as well | [optional] 
 **taxCountryCode** | **String**| Tax entity country code, used to determine currency/region.  | [optional] 

### Return type

[**GetSettlementOut**](GetSettlementOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSettlementSummary

> GetSettlementSummaryOut getSettlementSummary(quarter, opts)

Fetch summary

### Example

```javascript
import Taxamo from 'taxamo';

let apiInstance = new Taxamo.SettlementApi();
let quarter = "quarter_example"; // String | Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to 'range'.
let opts = {
  'mossCountryCode': "mossCountryCode_example", // String | MOSS country code, used to determine currency. If ommited, merchant default setting is used.
  'taxRegion': "taxRegion_example", // String | Tax region key
  'startMonth': "startMonth_example", // String | Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
  'endMonth': "endMonth_example" // String | Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
};
apiInstance.getSettlementSummary(quarter, opts, (error, data, response) => {
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
 **quarter** | **String**| Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to &#39;range&#39;. | 
 **mossCountryCode** | **String**| MOSS country code, used to determine currency. If ommited, merchant default setting is used. | [optional] 
 **taxRegion** | **String**| Tax region key | [optional] 
 **startMonth** | **String**| Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided. | [optional] 
 **endMonth** | **String**| Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided. | [optional] 

### Return type

[**GetSettlementSummaryOut**](GetSettlementSummaryOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

