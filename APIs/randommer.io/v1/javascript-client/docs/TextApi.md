# RandommerApi.TextApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTextHumanizePost**](TextApi.md#apiTextHumanizePost) | **POST** /api/Text/Humanize | Humanize text
[**apiTextLoremIpsumGet**](TextApi.md#apiTextLoremIpsumGet) | **GET** /api/Text/LoremIpsum | Generate lorem ipsum
[**apiTextPasswordGet**](TextApi.md#apiTextPasswordGet) | **GET** /api/Text/Password | Generate password
[**apiTextReviewPost**](TextApi.md#apiTextReviewPost) | **POST** /api/Text/Review | Get reviews (max quantity&#x3D;500)
[**apiTextTransformPost**](TextApi.md#apiTextTransformPost) | **POST** /api/Text/Transform | Transform text



## apiTextHumanizePost

> apiTextHumanizePost(textDto, opts)

Humanize text

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.TextApi();
let textDto = new RandommerApi.TextDto(); // TextDto | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiTextHumanizePost(textDto, opts, (error, data, response) => {
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
 **textDto** | [**TextDto**](TextDto.md)|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined


## apiTextLoremIpsumGet

> apiTextLoremIpsumGet(loremType, type, number, opts)

Generate lorem ipsum

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.TextApi();
let loremType = new RandommerApi.LoremType(); // LoremType | 
let type = new RandommerApi.TextType(); // TextType | 
let number = 56; // Number | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiTextLoremIpsumGet(loremType, type, number, opts, (error, data, response) => {
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
 **loremType** | [**LoremType**](.md)|  | 
 **type** | [**TextType**](.md)|  | 
 **number** | **Number**|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTextPasswordGet

> apiTextPasswordGet(length, hasDigits, hasUppercase, hasSpecial, opts)

Generate password

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.TextApi();
let length = 56; // Number | 
let hasDigits = true; // Boolean | 
let hasUppercase = true; // Boolean | 
let hasSpecial = true; // Boolean | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiTextPasswordGet(length, hasDigits, hasUppercase, hasSpecial, opts, (error, data, response) => {
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
 **length** | **Number**|  | 
 **hasDigits** | **Boolean**|  | 
 **hasUppercase** | **Boolean**|  | 
 **hasSpecial** | **Boolean**|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTextReviewPost

> apiTextReviewPost(product, quantity, opts)

Get reviews (max quantity&#x3D;500)

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.TextApi();
let product = "product_example"; // String | 
let quantity = 56; // Number | 
let opts = {
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiTextReviewPost(product, quantity, opts, (error, data, response) => {
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
 **product** | **String**|  | 
 **quantity** | **Number**|  | 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTextTransformPost

> apiTextTransformPost(textActionType, textDto, opts)

Transform text

### Example

```javascript
import RandommerApi from 'randommer_api';

let apiInstance = new RandommerApi.TextApi();
let textActionType = new RandommerApi.TextActionType(); // TextActionType | 
let textDto = new RandommerApi.TextDto(); // TextDto | 
let opts = {
  'caseType': new RandommerApi.CaseType(), // CaseType | 
  'find': "find_example", // String | 
  'replace': "replace_example", // String | 
  'xApiKey': "xApiKey_example" // String | Enter your key
};
apiInstance.apiTextTransformPost(textActionType, textDto, opts, (error, data, response) => {
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
 **textActionType** | [**TextActionType**](.md)|  | 
 **textDto** | [**TextDto**](TextDto.md)|  | 
 **caseType** | [**CaseType**](.md)|  | [optional] 
 **find** | **String**|  | [optional] 
 **replace** | **String**|  | [optional] 
 **xApiKey** | **String**| Enter your key | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined

