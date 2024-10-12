# RandommerApi.NameApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiNameBrandNamePost**](NameApi.md#apiNameBrandNamePost) | **POST** /api/Name/BrandName | Generate brand name suggestions
[**apiNameBusinessNamePost**](NameApi.md#apiNameBusinessNamePost) | **POST** /api/Name/BusinessName | Get business names for a specific culture
[**apiNameCulturesGet**](NameApi.md#apiNameCulturesGet) | **GET** /api/Name/Cultures | Get available cultures
[**apiNameGet**](NameApi.md#apiNameGet) | **GET** /api/Name | Get name
[**apiNameSuggestionsGet**](NameApi.md#apiNameSuggestionsGet) | **GET** /api/Name/Suggestions | Get business name suggestions



## apiNameBrandNamePost

> apiNameBrandNamePost(startingWords, opts)

Generate brand name suggestions

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.NameApi();
let startingWords = "startingWords_example"; // String | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiNameBrandNamePost(startingWords, opts, (error, data, response) => {
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
 **startingWords** | **String**|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiNameBusinessNamePost

> apiNameBusinessNamePost(number, opts)

Get business names for a specific culture

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.NameApi();
let number = 56; // Number | 
let opts = {
  'cultureCode': "'en_US'", // String | 
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiNameBusinessNamePost(number, opts, (error, data, response) => {
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
 **number** | **Number**|  | 
 **cultureCode** | **String**|  | [optional] [default to &#39;en_US&#39;]
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiNameCulturesGet

> apiNameCulturesGet(opts)

Get available cultures

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.NameApi();
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiNameCulturesGet(opts, (error, data, response) => {
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
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiNameGet

> apiNameGet(nameType, quantity, opts)

Get name

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.NameApi();
let nameType = new RandommerApi.NameType(); // NameType | 
let quantity = 56; // Number | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiNameGet(nameType, quantity, opts, (error, data, response) => {
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
 **nameType** | [**NameType**](.md)|  | 
 **quantity** | **Number**|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiNameSuggestionsGet

> apiNameSuggestionsGet(startingWords, opts)

Get business name suggestions

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.NameApi();
let startingWords = "startingWords_example"; // String | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiNameSuggestionsGet(startingWords, opts, (error, data, response) => {
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
 **startingWords** | **String**|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

