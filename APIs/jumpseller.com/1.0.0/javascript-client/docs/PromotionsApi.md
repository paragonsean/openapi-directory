# JumpsellerApi.PromotionsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**promotionsIdJsonDelete**](PromotionsApi.md#promotionsIdJsonDelete) | **DELETE** /promotions/{id}.json | Delete an existing Promotion.
[**promotionsIdJsonGet**](PromotionsApi.md#promotionsIdJsonGet) | **GET** /promotions/{id}.json | Retrieve a single Promotion.
[**promotionsIdJsonPut**](PromotionsApi.md#promotionsIdJsonPut) | **PUT** /promotions/{id}.json | Update a Promotion.
[**promotionsJsonGet**](PromotionsApi.md#promotionsJsonGet) | **GET** /promotions.json | Retrieve all Promotions.
[**promotionsJsonPost**](PromotionsApi.md#promotionsJsonPost) | **POST** /promotions.json | Create a new Promotion.



## promotionsIdJsonDelete

> String promotionsIdJsonDelete(login, authtoken, id)

Delete an existing Promotion.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PromotionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Promotion
apiInstance.promotionsIdJsonDelete(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Promotion | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## promotionsIdJsonGet

> Promotion promotionsIdJsonGet(login, authtoken, id)

Retrieve a single Promotion.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PromotionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Promotion
apiInstance.promotionsIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Promotion | 

### Return type

[**Promotion**](Promotion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## promotionsIdJsonPut

> Promotion promotionsIdJsonPut(login, authtoken, id, promotionEdit)

Update a Promotion.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PromotionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Promotion
let promotionEdit = new JumpsellerApi.PromotionEdit(); // PromotionEdit | Promotion parameters.
apiInstance.promotionsIdJsonPut(login, authtoken, id, promotionEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Promotion | 
 **promotionEdit** | [**PromotionEdit**](PromotionEdit.md)| Promotion parameters. | 

### Return type

[**Promotion**](Promotion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## promotionsJsonGet

> [Promotion] promotionsJsonGet(login, authtoken, opts)

Retrieve all Promotions.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PromotionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let opts = {
  'limit': 56, // Number | Promotions' list restriction (default: 50 | max: 200).
  'page': 56 // Number | Promotions' list page (default: 1).
};
apiInstance.promotionsJsonGet(login, authtoken, opts, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **limit** | **Number**| Promotions&#39; list restriction (default: 50 | max: 200). | [optional] 
 **page** | **Number**| Promotions&#39; list page (default: 1). | [optional] 

### Return type

[**[Promotion]**](Promotion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## promotionsJsonPost

> Promotion promotionsJsonPost(login, authtoken, promotionEdit)

Create a new Promotion.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PromotionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let promotionEdit = new JumpsellerApi.PromotionEdit(); // PromotionEdit | Promotion parameters.
apiInstance.promotionsJsonPost(login, authtoken, promotionEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **promotionEdit** | [**PromotionEdit**](PromotionEdit.md)| Promotion parameters. | 

### Return type

[**Promotion**](Promotion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

