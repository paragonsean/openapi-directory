# SeldonExternalApi.InternalApi

All URIs are relative to *http://seldon.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate**](InternalApi.md#aggregate) | **GET** /aggregate | 
[**aggregate2**](InternalApi.md#aggregate2) | **POST** /aggregate | 
[**route**](InternalApi.md#route) | **POST** /route | 
[**route2**](InternalApi.md#route2) | **GET** /route | 
[**sendFeedback**](InternalApi.md#sendFeedback) | **POST** /send-feedback | 
[**sendFeedback2**](InternalApi.md#sendFeedback2) | **GET** /send-feedback | 
[**transformInput**](InternalApi.md#transformInput) | **POST** /transform-input | 
[**transformInput2**](InternalApi.md#transformInput2) | **GET** /transform-input | 
[**transformInput3**](InternalApi.md#transformInput3) | **POST** /predict | 
[**transformInput4**](InternalApi.md#transformInput4) | **GET** /predict | 
[**transformOutput**](InternalApi.md#transformOutput) | **POST** /transform-output | 
[**transformOutput2**](InternalApi.md#transformOutput2) | **GET** /transform-output | 



## aggregate

> SeldonMessage aggregate(body)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let body = new SeldonExternalApi.SeldonMessageList(); // SeldonMessageList | 
apiInstance.aggregate(body, (error, data, response) => {
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
 **body** | [**SeldonMessageList**](.md)|  | 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aggregate2

> SeldonMessage aggregate2(opts)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let opts = {
  'json': new SeldonExternalApi.SeldonMessageList() // SeldonMessageList | 
};
apiInstance.aggregate2(opts, (error, data, response) => {
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
 **json** | [**SeldonMessageList**](SeldonMessageList.md)|  | [optional] 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## route

> SeldonMessage route(opts)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let opts = {
  'json': new SeldonExternalApi.SeldonMessage() // SeldonMessage | 
};
apiInstance.route(opts, (error, data, response) => {
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
 **json** | [**SeldonMessage**](SeldonMessage.md)|  | [optional] 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## route2

> SeldonMessage route2(json)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let json = new SeldonExternalApi.SeldonMessage(); // SeldonMessage | 
apiInstance.route2(json, (error, data, response) => {
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
 **json** | [**SeldonMessage**](.md)|  | 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendFeedback

> SeldonMessage sendFeedback(opts)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let opts = {
  'json': new SeldonExternalApi.Feedback() // Feedback | 
};
apiInstance.sendFeedback(opts, (error, data, response) => {
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
 **json** | [**Feedback**](Feedback.md)|  | [optional] 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## sendFeedback2

> SeldonMessage sendFeedback2(json)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let json = new SeldonExternalApi.Feedback(); // Feedback | 
apiInstance.sendFeedback2(json, (error, data, response) => {
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
 **json** | [**Feedback**](.md)|  | 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transformInput

> SeldonMessage transformInput(opts)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let opts = {
  'json': new SeldonExternalApi.SeldonMessage() // SeldonMessage | 
};
apiInstance.transformInput(opts, (error, data, response) => {
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
 **json** | [**SeldonMessage**](SeldonMessage.md)|  | [optional] 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## transformInput2

> SeldonMessage transformInput2(json)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let json = new SeldonExternalApi.SeldonMessage(); // SeldonMessage | 
apiInstance.transformInput2(json, (error, data, response) => {
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
 **json** | [**SeldonMessage**](.md)|  | 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transformInput3

> SeldonMessage transformInput3(opts)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let opts = {
  'json': new SeldonExternalApi.SeldonMessage() // SeldonMessage | 
};
apiInstance.transformInput3(opts, (error, data, response) => {
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
 **json** | [**SeldonMessage**](SeldonMessage.md)|  | [optional] 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## transformInput4

> SeldonMessage transformInput4(json)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let json = new SeldonExternalApi.SeldonMessage(); // SeldonMessage | 
apiInstance.transformInput4(json, (error, data, response) => {
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
 **json** | [**SeldonMessage**](.md)|  | 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transformOutput

> SeldonMessage transformOutput(opts)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let opts = {
  'json': new SeldonExternalApi.SeldonMessage() // SeldonMessage | 
};
apiInstance.transformOutput(opts, (error, data, response) => {
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
 **json** | [**SeldonMessage**](SeldonMessage.md)|  | [optional] 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## transformOutput2

> SeldonMessage transformOutput2(json)



### Example

```javascript
import SeldonExternalApi from 'seldon_external_api';

let apiInstance = new SeldonExternalApi.InternalApi();
let json = new SeldonExternalApi.SeldonMessage(); // SeldonMessage | 
apiInstance.transformOutput2(json, (error, data, response) => {
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
 **json** | [**SeldonMessage**](.md)|  | 

### Return type

[**SeldonMessage**](SeldonMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

