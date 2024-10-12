# IpQualityScoreApi.MaliciousUrlScannerApi

All URIs are relative to *https://ipqualityscore.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maliciousUrlScanner**](MaliciousUrlScannerApi.md#maliciousUrlScanner) | **GET** /json/url/{YOUR_API_KEY_HERE}/{URL_HERE} | Malicious URL Scanner



## maliciousUrlScanner

> MaliciousUrlScanner200Response maliciousUrlScanner(YOUR_API_KEY_HERE, URL_HERE)

Malicious URL Scanner

Malicious URL Scanner

### Example

```javascript
import IpQualityScoreApi from 'ip_quality_score_api';

let apiInstance = new IpQualityScoreApi.MaliciousUrlScannerApi();
let YOUR_API_KEY_HERE = "asd24#sdfs322#"; // String | (Required) YOUR_API_KEY_HERE
let URL_HERE = "https%3A%2F%2Fgoogle.com"; // String | (Required) URL_HERE
apiInstance.maliciousUrlScanner(YOUR_API_KEY_HERE, URL_HERE, (error, data, response) => {
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
 **YOUR_API_KEY_HERE** | **String**| (Required) YOUR_API_KEY_HERE | 
 **URL_HERE** | **String**| (Required) URL_HERE | 

### Return type

[**MaliciousUrlScanner200Response**](MaliciousUrlScanner200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

