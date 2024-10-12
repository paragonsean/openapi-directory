# WorldTimeApi.DefaultApi

All URIs are relative to *http://worldtimeapi.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipGet**](DefaultApi.md#ipGet) | **GET** /ip | request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.
[**ipIpv4Get**](DefaultApi.md#ipIpv4Get) | **GET** /ip/{ipv4} | request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.
[**ipIpv4TxtGet**](DefaultApi.md#ipIpv4TxtGet) | **GET** /ip/{ipv4}.txt | request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.
[**ipTxtGet**](DefaultApi.md#ipTxtGet) | **GET** /ip.txt | request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.
[**timezoneAreaGet**](DefaultApi.md#timezoneAreaGet) | **GET** /timezone/{area} | a listing of all timezones available for that area.
[**timezoneAreaLocationGet**](DefaultApi.md#timezoneAreaLocationGet) | **GET** /timezone/{area}/{location} | request the current time for a timezone.
[**timezoneAreaLocationRegionGet**](DefaultApi.md#timezoneAreaLocationRegionGet) | **GET** /timezone/{area}/{location}/{region} | request the current time for a timezone.
[**timezoneAreaLocationRegionTxtGet**](DefaultApi.md#timezoneAreaLocationRegionTxtGet) | **GET** /timezone/{area}/{location}/{region}.txt | request the current time for a timezone.
[**timezoneAreaLocationTxtGet**](DefaultApi.md#timezoneAreaLocationTxtGet) | **GET** /timezone/{area}/{location}.txt | request the current time for a timezone.
[**timezoneAreaTxtGet**](DefaultApi.md#timezoneAreaTxtGet) | **GET** /timezone/{area}.txt | a listing of all timezones available for that area.
[**timezoneGet**](DefaultApi.md#timezoneGet) | **GET** /timezone | a listing of all timezones.
[**timezoneTxtGet**](DefaultApi.md#timezoneTxtGet) | **GET** /timezone.txt | a listing of all timezones.



## ipGet

> DateTimeJsonResponse ipGet()

request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
apiInstance.ipGet((error, data, response) => {
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

[**DateTimeJsonResponse**](DateTimeJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipIpv4Get

> DateTimeJsonResponse ipIpv4Get(ipv4)

request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
let ipv4 = "ipv4_example"; // String | 
apiInstance.ipIpv4Get(ipv4, (error, data, response) => {
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
 **ipv4** | **String**|  | 

### Return type

[**DateTimeJsonResponse**](DateTimeJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ipIpv4TxtGet

> String ipIpv4TxtGet(ipv4)

request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
let ipv4 = "ipv4_example"; // String | 
apiInstance.ipIpv4TxtGet(ipv4, (error, data, response) => {
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
 **ipv4** | **String**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## ipTxtGet

> String ipTxtGet()

request the current time based on the ip of the request. note: this is a \&quot;best guess\&quot; obtained from open-source data.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
apiInstance.ipTxtGet((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## timezoneAreaGet

> [String] timezoneAreaGet(area)

a listing of all timezones available for that area.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
let area = "area_example"; // String | 
apiInstance.timezoneAreaGet(area, (error, data, response) => {
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
 **area** | **String**|  | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timezoneAreaLocationGet

> DateTimeJsonResponse timezoneAreaLocationGet(area, location)

request the current time for a timezone.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
let area = "area_example"; // String | 
let location = "location_example"; // String | 
apiInstance.timezoneAreaLocationGet(area, location, (error, data, response) => {
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
 **area** | **String**|  | 
 **location** | **String**|  | 

### Return type

[**DateTimeJsonResponse**](DateTimeJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timezoneAreaLocationRegionGet

> DateTimeJsonResponse timezoneAreaLocationRegionGet(area, location, region)

request the current time for a timezone.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
let area = "area_example"; // String | 
let location = "location_example"; // String | 
let region = "region_example"; // String | 
apiInstance.timezoneAreaLocationRegionGet(area, location, region, (error, data, response) => {
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
 **area** | **String**|  | 
 **location** | **String**|  | 
 **region** | **String**|  | 

### Return type

[**DateTimeJsonResponse**](DateTimeJsonResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timezoneAreaLocationRegionTxtGet

> String timezoneAreaLocationRegionTxtGet(area, location, region)

request the current time for a timezone.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
let area = "area_example"; // String | 
let location = "location_example"; // String | 
let region = "region_example"; // String | 
apiInstance.timezoneAreaLocationRegionTxtGet(area, location, region, (error, data, response) => {
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
 **area** | **String**|  | 
 **location** | **String**|  | 
 **region** | **String**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## timezoneAreaLocationTxtGet

> String timezoneAreaLocationTxtGet(area, location)

request the current time for a timezone.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
let area = "area_example"; // String | 
let location = "location_example"; // String | 
apiInstance.timezoneAreaLocationTxtGet(area, location, (error, data, response) => {
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
 **area** | **String**|  | 
 **location** | **String**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## timezoneAreaTxtGet

> String timezoneAreaTxtGet(area)

a listing of all timezones available for that area.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
let area = "area_example"; // String | 
apiInstance.timezoneAreaTxtGet(area, (error, data, response) => {
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
 **area** | **String**|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## timezoneGet

> [String] timezoneGet()

a listing of all timezones.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
apiInstance.timezoneGet((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timezoneTxtGet

> String timezoneTxtGet()

a listing of all timezones.

### Example

```javascript
import WorldTimeApi from 'world_time_api';

let apiInstance = new WorldTimeApi.DefaultApi();
apiInstance.timezoneTxtGet((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

