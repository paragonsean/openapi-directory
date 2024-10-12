# DomainsIndexApi.InfoApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getApiInfoItem**](InfoApi.md#getApiInfoItem) | **GET** /info/api | 
[**getStatisticsCollection**](InfoApi.md#getStatisticsCollection) | **GET** /info/stat/ | Returns overall stagtistics
[**getStatisticsItem**](InfoApi.md#getStatisticsItem) | **GET** /info/stat/{zone} | Returns statistics for specific zone
[**infoTldGet**](InfoApi.md#infoTldGet) | **GET** /info/tld/ | Returns overall Tld info
[**infoTldZoneGet**](InfoApi.md#infoTldZoneGet) | **GET** /info/tld/{zone} | Returns statistics for specific zone



## getApiInfoItem

> APIKeyInfo getApiInfoItem(opts)



### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.InfoApi();
let opts = {
  'apiKey': "apiKey_example" // String | API key
};
apiInstance.getApiInfoItem(opts, (error, data, response) => {
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
 **apiKey** | **String**| API key | [optional] 

### Return type

[**APIKeyInfo**](APIKeyInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStatisticsCollection

> [ZoneStats] getStatisticsCollection(opts)

Returns overall stagtistics

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.InfoApi();
let opts = {
  'page': "page_example", // String | Search page to request
  'limit': 50 // Number | Results per page
};
apiInstance.getStatisticsCollection(opts, (error, data, response) => {
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
 **page** | **String**| Search page to request | [optional] 
 **limit** | **Number**| Results per page | [optional] [default to 50]

### Return type

[**[ZoneStats]**](ZoneStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStatisticsItem

> ZoneStats getStatisticsItem(zone, opts)

Returns statistics for specific zone

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.InfoApi();
let zone = "zone_example"; // String | 
let opts = {
  'page': "page_example", // String | Search page to request
  'limit': 50 // Number | Results per page
};
apiInstance.getStatisticsItem(zone, opts, (error, data, response) => {
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
 **zone** | **String**|  | 
 **page** | **String**| Search page to request | [optional] 
 **limit** | **Number**| Results per page | [optional] [default to 50]

### Return type

[**ZoneStats**](ZoneStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## infoTldGet

> [ZoneInfo] infoTldGet()

Returns overall Tld info

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.InfoApi();
apiInstance.infoTldGet((error, data, response) => {
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

[**[ZoneInfo]**](ZoneInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## infoTldZoneGet

> ZoneInfo infoTldZoneGet(zone, opts)

Returns statistics for specific zone

### Example

```javascript
import DomainsIndexApi from 'domains_index_api';

let apiInstance = new DomainsIndexApi.InfoApi();
let zone = "zone_example"; // String | 
let opts = {
  'page': "page_example", // String | Search page to request
  'limit': 50 // Number | Results per page
};
apiInstance.infoTldZoneGet(zone, opts, (error, data, response) => {
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
 **zone** | **String**|  | 
 **page** | **String**| Search page to request | [optional] 
 **limit** | **Number**| Results per page | [optional] [default to 50]

### Return type

[**ZoneInfo**](ZoneInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

