# JumpsellerApi.PartnersApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**partnersStoresJsonGet**](PartnersApi.md#partnersStoresJsonGet) | **GET** /partners/stores.json | Retrieve statistics.
[**storeCheckStatusJsonGet**](PartnersApi.md#storeCheckStatusJsonGet) | **GET** /store/check_status.json | Retrive store creation status.
[**storeCreateJsonPost**](PartnersApi.md#storeCreateJsonPost) | **POST** /store/create.json | Create a Partnered Store



## partnersStoresJsonGet

> [Type] partnersStoresJsonGet(partnerCode, authToken, from, to, opts)

Retrieve statistics.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PartnersApi();
let partnerCode = "partnerCode_example"; // String | Partner code.
let authToken = "authToken_example"; // String | Partner authentication token.
let from = "from_example"; // String | Statistics start date. Should be in format 'Y-m-d'.
let to = "to_example"; // String | Statistics end date. Should be in format 'Y-m-d'.
let opts = {
  'page': 1 // Number | List page
};
apiInstance.partnersStoresJsonGet(partnerCode, authToken, from, to, opts, (error, data, response) => {
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
 **partnerCode** | **String**| Partner code. | 
 **authToken** | **String**| Partner authentication token. | 
 **from** | **String**| Statistics start date. Should be in format &#39;Y-m-d&#39;. | 
 **to** | **String**| Statistics end date. Should be in format &#39;Y-m-d&#39;. | 
 **page** | **Number**| List page | [optional] [default to 1]

### Return type

[**[Type]**](Type.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeCheckStatusJsonGet

> StoreCheckStatusJsonGet200Response storeCheckStatusJsonGet(partnerCode, authToken, storeCode, opts)

Retrive store creation status.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PartnersApi();
let partnerCode = "partnerCode_example"; // String | Partner code.
let authToken = "authToken_example"; // String | Partner authentication token.
let storeCode = "storeCode_example"; // String | Store Code
let opts = {
  'locale': "'en'" // String | ISO 3166-2 code of the language used in the response messages.
};
apiInstance.storeCheckStatusJsonGet(partnerCode, authToken, storeCode, opts, (error, data, response) => {
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
 **partnerCode** | **String**| Partner code. | 
 **authToken** | **String**| Partner authentication token. | 
 **storeCode** | **String**| Store Code | 
 **locale** | **String**| ISO 3166-2 code of the language used in the response messages. | [optional] [default to &#39;en&#39;]

### Return type

[**StoreCheckStatusJsonGet200Response**](StoreCheckStatusJsonGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storeCreateJsonPost

> PartnerStoreCode storeCreateJsonPost(partnerCode, authToken, partnerStoreCreate)

Create a Partnered Store

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PartnersApi();
let partnerCode = "partnerCode_example"; // String | Partner code.
let authToken = "authToken_example"; // String | Partner authentication token.
let partnerStoreCreate = new JumpsellerApi.PartnerStoreCreate(); // PartnerStoreCreate | New partnered Store parameters.
apiInstance.storeCreateJsonPost(partnerCode, authToken, partnerStoreCreate, (error, data, response) => {
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
 **partnerCode** | **String**| Partner code. | 
 **authToken** | **String**| Partner authentication token. | 
 **partnerStoreCreate** | [**PartnerStoreCreate**](PartnerStoreCreate.md)| New partnered Store parameters. | 

### Return type

[**PartnerStoreCode**](PartnerStoreCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

