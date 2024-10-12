# PublicApi.WindowsHostingsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getWindowsHosting**](WindowsHostingsApi.md#getWindowsHosting) | **GET** /windowshostings/{domainName} | Windows hosting detail
[**getWindowsHostings**](WindowsHostingsApi.md#getWindowsHostings) | **GET** /windowshostings | Overview of windows hostings



## getWindowsHosting

> WindowsHostingDetail getWindowsHosting(domainName, domainName2)

Windows hosting detail

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.WindowsHostingsApi();
let domainName = "domainName_example"; // String | The Windows hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
apiInstance.getWindowsHosting(domainName, domainName2, (error, data, response) => {
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
 **domainName** | **String**| The Windows hosting domain name. | 
 **domainName2** | **String**| Automatically added | 

### Return type

[**WindowsHostingDetail**](WindowsHostingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWindowsHostings

> [WindowsHosting] getWindowsHostings(opts)

Overview of windows hostings

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.WindowsHostingsApi();
let opts = {
  'skip': 56, // Number | The number of items to skip in the resultset.
  'take': 56 // Number | The number of items to return in the resultset. The returned count can be equal or less than this number.
};
apiInstance.getWindowsHostings(opts, (error, data, response) => {
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
 **skip** | **Number**| The number of items to skip in the resultset. | [optional] 
 **take** | **Number**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] 

### Return type

[**[WindowsHosting]**](WindowsHosting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

