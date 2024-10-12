# EveMarketerMarketstatApi.MarketstatApi

All URIs are relative to *https://api.evemarketer.com/ec*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketstatGet**](MarketstatApi.md#marketstatGet) | **GET** /marketstat | XML Marketstat
[**marketstatJsonGet**](MarketstatApi.md#marketstatJsonGet) | **GET** /marketstat/json | JSON Marketstat
[**marketstatJsonPost**](MarketstatApi.md#marketstatJsonPost) | **POST** /marketstat/json | JSON Marketstat
[**marketstatPost**](MarketstatApi.md#marketstatPost) | **POST** /marketstat | XML Marketstat



## marketstatGet

> ExecAPI marketstatGet(typeid, opts)

XML Marketstat

### Example

```javascript
import EveMarketerMarketstatApi from 'eve_marketer_marketstat_api';

let apiInstance = new EveMarketerMarketstatApi.MarketstatApi();
let typeid = [null]; // [Number] | TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid=34&typeid=35 or typeid=34,35 
let opts = {
  'regionlimit': 56, // Number | Limit the statistics to a single region.
  'usesystem': 56 // Number | Limit the statistics to a single solar system.
};
apiInstance.marketstatGet(typeid, opts, (error, data, response) => {
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
 **typeid** | [**[Number]**](Number.md)| TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35  | 
 **regionlimit** | **Number**| Limit the statistics to a single region. | [optional] 
 **usesystem** | **Number**| Limit the statistics to a single solar system. | [optional] 

### Return type

[**ExecAPI**](ExecAPI.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## marketstatJsonGet

> [Type] marketstatJsonGet(typeid, opts)

JSON Marketstat

### Example

```javascript
import EveMarketerMarketstatApi from 'eve_marketer_marketstat_api';

let apiInstance = new EveMarketerMarketstatApi.MarketstatApi();
let typeid = [null]; // [Number] | TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid=34&typeid=35 or typeid=34,35 
let opts = {
  'regionlimit': 56, // Number | Limit the statistics to a single region.
  'usesystem': 56 // Number | Limit the statistics to a single region.
};
apiInstance.marketstatJsonGet(typeid, opts, (error, data, response) => {
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
 **typeid** | [**[Number]**](Number.md)| TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35  | 
 **regionlimit** | **Number**| Limit the statistics to a single region. | [optional] 
 **usesystem** | **Number**| Limit the statistics to a single region. | [optional] 

### Return type

[**[Type]**](Type.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## marketstatJsonPost

> [Type] marketstatJsonPost(typeid, opts)

JSON Marketstat

### Example

```javascript
import EveMarketerMarketstatApi from 'eve_marketer_marketstat_api';

let apiInstance = new EveMarketerMarketstatApi.MarketstatApi();
let typeid = [null]; // [Number] | TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid=34&typeid=35 or typeid=34,35 
let opts = {
  'regionlimit': 56, // Number | Limit the statistics to a single region.
  'usesystem': 56 // Number | Limit the statistics to a single region.
};
apiInstance.marketstatJsonPost(typeid, opts, (error, data, response) => {
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
 **typeid** | [**[Number]**](Number.md)| TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35  | 
 **regionlimit** | **Number**| Limit the statistics to a single region. | [optional] 
 **usesystem** | **Number**| Limit the statistics to a single region. | [optional] 

### Return type

[**[Type]**](Type.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## marketstatPost

> ExecAPI marketstatPost(typeid, opts)

XML Marketstat

### Example

```javascript
import EveMarketerMarketstatApi from 'eve_marketer_marketstat_api';

let apiInstance = new EveMarketerMarketstatApi.MarketstatApi();
let typeid = [null]; // [Number] | TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid=34&typeid=35 or typeid=34,35 
let opts = {
  'regionlimit': 56, // Number | Limit the statistics to a single region.
  'usesystem': 56 // Number | Limit the statistics to a single solar system.
};
apiInstance.marketstatPost(typeid, opts, (error, data, response) => {
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
 **typeid** | [**[Number]**](Number.md)| TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35  | 
 **regionlimit** | **Number**| Limit the statistics to a single region. | [optional] 
 **usesystem** | **Number**| Limit the statistics to a single solar system. | [optional] 

### Return type

[**ExecAPI**](ExecAPI.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/xml

