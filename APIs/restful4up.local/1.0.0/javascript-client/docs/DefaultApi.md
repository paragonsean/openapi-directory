# ResTful4Up.DefaultApi

All URIs are relative to *http://restful4up.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applyYaraRules**](DefaultApi.md#applyYaraRules) | **POST** /apply-yara-rules | 
[**clean**](DefaultApi.md#clean) | **HEAD** /clean | 
[**emulationOutput**](DefaultApi.md#emulationOutput) | **POST** /emulation-output | 
[**generatePartialYaraRule**](DefaultApi.md#generatePartialYaraRule) | **POST** /generate-partial-yara-rules | 
[**unpack**](DefaultApi.md#unpack) | **POST** /unpack | 



## applyYaraRules

> ApplyYaraRules200Response applyYaraRules(file, rules, opts)



apply given YARA rules to the given executable. (upto 10 rules)

### Example

```javascript
import ResTful4Up from 'res_tful4_up';

let apiInstance = new ResTful4Up.DefaultApi();
let file = "/path/to/file"; // File | file
let rules = ["null"]; // [String] | 
let opts = {
  'isUnpackingRequired': "isUnpackingRequired_example" // String | 
};
apiInstance.applyYaraRules(file, rules, opts, (error, data, response) => {
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
 **file** | **File**| file | 
 **rules** | [**[String]**](String.md)|  | 
 **isUnpackingRequired** | **String**|  | [optional] 

### Return type

[**ApplyYaraRules200Response**](ApplyYaraRules200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## clean

> clean()



clean up the uploaded files

### Example

```javascript
import ResTful4Up from 'res_tful4_up';

let apiInstance = new ResTful4Up.DefaultApi();
apiInstance.clean((error, data, response) => {
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
- **Accept**: */*


## emulationOutput

> EmulationOutput200Response emulationOutput(file)



try to get the emulation output after unpacking the file

### Example

```javascript
import ResTful4Up from 'res_tful4_up';

let apiInstance = new ResTful4Up.DefaultApi();
let file = "/path/to/file"; // File | file
apiInstance.emulationOutput(file, (error, data, response) => {
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
 **file** | **File**| file | 

### Return type

[**EmulationOutput200Response**](EmulationOutput200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## generatePartialYaraRule

> GeneratePartialYaraRule200Response generatePartialYaraRule(file, opts)



generate partial YARA rules for give executable. (Rule without the condition section)

### Example

```javascript
import ResTful4Up from 'res_tful4_up';

let apiInstance = new ResTful4Up.DefaultApi();
let file = "/path/to/file"; // File | file
let opts = {
  'isUnpackingRequired': "isUnpackingRequired_example", // String | 
  'minimumStringLength': "minimumStringLength_example", // String | 
  'stringsToIgnore': ["null"] // [String] | 
};
apiInstance.generatePartialYaraRule(file, opts, (error, data, response) => {
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
 **file** | **File**| file | 
 **isUnpackingRequired** | **String**|  | [optional] 
 **minimumStringLength** | **String**|  | [optional] 
 **stringsToIgnore** | [**[String]**](String.md)|  | [optional] 

### Return type

[**GeneratePartialYaraRule200Response**](GeneratePartialYaraRule200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## unpack

> File unpack(file)



try to unpack the given file

### Example

```javascript
import ResTful4Up from 'res_tful4_up';

let apiInstance = new ResTful4Up.DefaultApi();
let file = "/path/to/file"; // File | file
apiInstance.unpack(file, (error, data, response) => {
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
 **file** | **File**| file | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*

