# HandwryttenApi.CustomizerApi

All URIs are relative to *https://api.handwrytten.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomCard**](CustomizerApi.md#createCustomCard) | **POST** /cards/createCustomCard | Create a new custom card
[**fontsListForCustomizer**](CustomizerApi.md#fontsListForCustomizer) | **GET** /fonts/listForCustomizer | Lists fonts available for use with the card customizer
[**uploadCustomLogo**](CustomizerApi.md#uploadCustomLogo) | **POST** /cards/uploadCustomLogo | upload logo or cover image for card



## createCustomCard

> [Card] createCustomCard(body)

Create a new custom card

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.CustomizerApi();
let body = new HandwryttenApi.CreateCustomCardRequest(); // CreateCustomCardRequest | additional parameters
apiInstance.createCustomCard(body, (error, data, response) => {
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
 **body** | [**CreateCustomCardRequest**](CreateCustomCardRequest.md)| additional parameters | 

### Return type

[**[Card]**](Card.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fontsListForCustomizer

> [FontForCustomizer] fontsListForCustomizer()

Lists fonts available for use with the card customizer

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.CustomizerApi();
apiInstance.fontsListForCustomizer((error, data, response) => {
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

[**[FontForCustomizer]**](FontForCustomizer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadCustomLogo

> UploadCustomLogo200Response uploadCustomLogo(file, type, uid)

upload logo or cover image for card

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.CustomizerApi();
let file = "/path/to/file"; // File | upload images for customc cards
let type = "type_example"; // String | set to cover or header
let uid = "uid_example"; // String | uid of the user
apiInstance.uploadCustomLogo(file, type, uid, (error, data, response) => {
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
 **file** | **File**| upload images for customc cards | 
 **type** | **String**| set to cover or header | 
 **uid** | **String**| uid of the user | 

### Return type

[**UploadCustomLogo200Response**](UploadCustomLogo200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

