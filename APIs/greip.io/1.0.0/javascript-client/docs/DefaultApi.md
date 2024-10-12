# GreipApi.DefaultApi

All URIs are relative to *https://gregeoip.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aSNLookupGet**](DefaultApi.md#aSNLookupGet) | **GET** /ASNLookup | 
[**bINLookupGet**](DefaultApi.md#bINLookupGet) | **GET** /BINLookup | 
[**badWordsGet**](DefaultApi.md#badWordsGet) | **GET** /badWords | 
[**bulkLookupGet**](DefaultApi.md#bulkLookupGet) | **GET** /BulkLookup | 
[**countryGet**](DefaultApi.md#countryGet) | **GET** /Country | 
[**geoIPGet**](DefaultApi.md#geoIPGet) | **GET** /GeoIP | 
[**iPLookupGet**](DefaultApi.md#iPLookupGet) | **GET** /IPLookup | 
[**validateEmailGet**](DefaultApi.md#validateEmailGet) | **GET** /validateEmail | 
[**validatePhoneGet**](DefaultApi.md#validatePhoneGet) | **GET** /validatePhone | 



## aSNLookupGet

> aSNLookupGet(key, asn, opts)



ASNLookup endpoint: This method helps you lookup any AS Number. It returns the type, organisation details, routes, etc.

### Example

```javascript
import GreipApi from 'greip_api';

let apiInstance = new GreipApi.DefaultApi();
let key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
let asn = "15169"; // String | The AS Number you want to lookup
let opts = {
  'isList': "false", // String | Set this to true if you want to list all routes of both IPv4 and IPv6.
  'format': "JSON" // String | Sets the format of the API response. JSON is the default format.
};
apiInstance.aSNLookupGet(key, asn, opts, (error, data, response) => {
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
 **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | 
 **asn** | **String**| The AS Number you want to lookup | 
 **isList** | **String**| Set this to true if you want to list all routes of both IPv4 and IPv6. | [optional] 
 **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bINLookupGet

> bINLookupGet(key, bin, opts)



This method helps you validate any BIN/IIN number and retrieve the full details related to the bank, brand, type, scheme, country, etc.

### Example

```javascript
import GreipApi from 'greip_api';

let apiInstance = new GreipApi.DefaultApi();
let key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
let bin = "489022"; // String | The BIN/IIN you want to lookup/validate.
let opts = {
  'format': "JSON" // String | Sets the format of the API response. JSON is the default format.
};
apiInstance.bINLookupGet(key, bin, opts, (error, data, response) => {
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
 **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | 
 **bin** | **String**| The BIN/IIN you want to lookup/validate. | 
 **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## badWordsGet

> badWordsGet(key, text, opts)



badWords endpoint: Detects whether user inputs contain profanity or not.

### Example

```javascript
import GreipApi from 'greip_api';

let apiInstance = new GreipApi.DefaultApi();
let key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
let text = "This is a sample text without profanity!"; // String | The text you want to check.
let opts = {
  'listBadWords': "false", // String | Set to `yes` to list the bad-words as an Array.
  'scoreOnly': "false", // String | Set to `yes` to return only the score of the text and whether it's safe or not.
  'format': "JSON" // String | Sets the format of the API response. JSON is the default format.
};
apiInstance.badWordsGet(key, text, opts, (error, data, response) => {
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
 **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | 
 **text** | **String**| The text you want to check. | 
 **listBadWords** | **String**| Set to &#x60;yes&#x60; to list the bad-words as an Array. | [optional] 
 **scoreOnly** | **String**| Set to &#x60;yes&#x60; to return only the score of the text and whether it&#39;s safe or not. | [optional] 
 **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## bulkLookupGet

> bulkLookupGet(key, ips, opts)



BulkLookup endpoint: Returns the geolocation data of multiple IP Addresses.

### Example

```javascript
import GreipApi from 'greip_api';

let apiInstance = new GreipApi.DefaultApi();
let key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
let ips = "1.1.1.1"; // String | The IP Addresses you want to lookup. It's a CSV (Comma Separated Values)
let opts = {
  'params': "currency", // String | The modules you want to use of the request. It's a CSV (Comma Separated Values)
  'lang': "AR", // String | Used to inform the API to retrieve the response in your native language.
  'format': "JSON" // String | Sets the format of the API response. JSON is the default format.
};
apiInstance.bulkLookupGet(key, ips, opts, (error, data, response) => {
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
 **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | 
 **ips** | **String**| The IP Addresses you want to lookup. It&#39;s a CSV (Comma Separated Values) | 
 **params** | **String**| The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values) | [optional] 
 **lang** | **String**| Used to inform the API to retrieve the response in your native language. | [optional] 
 **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## countryGet

> countryGet(key, countryCode, opts)



Country endpoint: Returns the information of a specific country by passing the &#x60;countrCode&#x60;.

### Example

```javascript
import GreipApi from 'greip_api';

let apiInstance = new GreipApi.DefaultApi();
let key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
let countryCode = "PS"; // String | The Country Code of the country you want to fetch it's data.
let opts = {
  'params': "language", // String | The modules you want to use of the request. It's a CSV (Comma Separated Values)
  'lang': "AR", // String | Used to inform the API to retrieve the response in your native language.
  'format': "JSON" // String | Sets the format of the API response. JSON is the default format.
};
apiInstance.countryGet(key, countryCode, opts, (error, data, response) => {
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
 **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | 
 **countryCode** | **String**| The Country Code of the country you want to fetch it&#39;s data. | 
 **params** | **String**| The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values) | [optional] 
 **lang** | **String**| Used to inform the API to retrieve the response in your native language. | [optional] 
 **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## geoIPGet

> geoIPGet(key, opts)



Returns the geolocation data of the visitor.

### Example

```javascript
import GreipApi from 'greip_api';

let apiInstance = new GreipApi.DefaultApi();
let key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
let opts = {
  'params': "currency", // String | The modules you want to use of the request. It's a CSV (Comma Separated Values)
  'lang': "AR", // String | Used to inform the API to retrieve the response in your native language.
  'format': "JSON" // String | Sets the format of the API response. JSON is the default format.
};
apiInstance.geoIPGet(key, opts, (error, data, response) => {
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
 **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | 
 **params** | **String**| The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values) | [optional] 
 **lang** | **String**| Used to inform the API to retrieve the response in your native language. | [optional] 
 **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## iPLookupGet

> iPLookupGet(key, ip, opts)



Returns the geolocation data of a specific IP Address.

### Example

```javascript
import GreipApi from 'greip_api';

let apiInstance = new GreipApi.DefaultApi();
let key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
let ip = "1.1.1.1"; // String | The IP Address you want to lookup.
let opts = {
  'params': "currency", // String | The modules you want to use of the request. It's a CSV (Comma Separated Values)
  'lang': "AR", // String | Used to inform the API to retrieve the response in your native language.
  'format': "JSON" // String | Sets the format of the API response. JSON is the default format.
};
apiInstance.iPLookupGet(key, ip, opts, (error, data, response) => {
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
 **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | 
 **ip** | **String**| The IP Address you want to lookup. | 
 **params** | **String**| The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values) | [optional] 
 **lang** | **String**| Used to inform the API to retrieve the response in your native language. | [optional] 
 **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## validateEmailGet

> validateEmailGet(key, email, opts)



This method can be used as an extra-layer of your system for validating email addresses.

### Example

```javascript
import GreipApi from 'greip_api';

let apiInstance = new GreipApi.DefaultApi();
let key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
let email = "name@domain.com"; // String | The Email Address you want to validate.
let opts = {
  'format': "JSON" // String | Sets the format of the API response. JSON is the default format.
};
apiInstance.validateEmailGet(key, email, opts, (error, data, response) => {
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
 **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | 
 **email** | **String**| The Email Address you want to validate. | 
 **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## validatePhoneGet

> validatePhoneGet(key, phone, countryCode, opts)



This method can be used as an extra-layer of your system for validating phone numbers.

### Example

```javascript
import GreipApi from 'greip_api';

let apiInstance = new GreipApi.DefaultApi();
let key = "2517bc4fc3f790e8f09bc808bb63b899"; // String | Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don't have an account yet, please create new account first.
let phone = "1234567890"; // String | The Phone Number you want to validate.
let countryCode = "US"; // String | The ISO 3166-1 alpha-2 format of the country code of the phone number.
let opts = {
  'format': "JSON" // String | Sets the format of the API response. JSON is the default format.
};
apiInstance.validatePhoneGet(key, phone, countryCode, opts, (error, data, response) => {
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
 **key** | **String**| Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first. | 
 **phone** | **String**| The Phone Number you want to validate. | 
 **countryCode** | **String**| The ISO 3166-1 alpha-2 format of the country code of the phone number. | 
 **format** | **String**| Sets the format of the API response. JSON is the default format. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

