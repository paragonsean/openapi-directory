# CheckoutApi.CustomDataApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**removesinglecustomfieldvalue**](CustomDataApi.md#removesinglecustomfieldvalue) | **DELETE** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName} | Remove single custom field value
[**setMultipleCustomFieldValues**](CustomDataApi.md#setMultipleCustomFieldValues) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId} | Set multiple custom field values
[**setSingleCustomFieldValue**](CustomDataApi.md#setSingleCustomFieldValue) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName} | Set single custom field value



## removesinglecustomfieldvalue

> removesinglecustomfieldvalue(contentType, accept, orderFormId, appId, appFieldName)

Remove single custom field value

Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can be removed by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    You also need to iform the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, also passed through the URL) whose value you want to remove.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.CustomDataApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let orderFormId = "orderFormId_example"; // String | The ID of the orderForm from which you want to remove the custom field value.
let appId = "appId_example"; // String | ID of the app created through the Update orderForm Configuration endpoint.
let appFieldName = "appFieldName_example"; // String | Name of the app's field created through the Update orderForm Configuration endpoint and which will be deleted.
apiInstance.removesinglecustomfieldvalue(contentType, accept, orderFormId, appId, appFieldName, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **orderFormId** | **String**| The ID of the orderForm from which you want to remove the custom field value. | 
 **appId** | **String**| ID of the app created through the Update orderForm Configuration endpoint. | 
 **appFieldName** | **String**| Name of the app&#39;s field created through the Update orderForm Configuration endpoint and which will be deleted. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setMultipleCustomFieldValues

> Object setMultipleCustomFieldValues(orderFormId, contentType, accept, appId, requestBody)

Set multiple custom field values

Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference/configuration#updateorderformconfiguration) request. The values of these custom fields can then be updated by this request.    To do that, you need to inform the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, for each field created in this app (&#x60;appFieldName&#x60;) you will inform a value (&#x60;appFieldValue&#x60;).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.CustomDataApi();
let orderFormId = "orderFormId_example"; // String | ID of the orderForm that will receive the new custom field values.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let appId = "appId_example"; // String | ID of the app created with the configuration API.
let requestBody = {key: null}; // {String: Object} | 
apiInstance.setMultipleCustomFieldValues(orderFormId, contentType, accept, appId, requestBody, (error, data, response) => {
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
 **orderFormId** | **String**| ID of the orderForm that will receive the new custom field values. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **appId** | **String**| ID of the app created with the configuration API. | 
 **requestBody** | [**{String: Object}**](Object.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setSingleCustomFieldValue

> setSingleCustomFieldValue(orderFormId, appId, appFieldName, contentType, accept, setsinglecustomfieldvalueRequest)

Set single custom field value

Your account may create &#x60;apps&#x60;, which contain custom fields, through the [Update orderForm configuration](https://developers.vtex.com/reference#updateorderformconfiguration) request. The value of a specific custom field can then be updated by this request.    To do that, you need to inform in the URL the ID of the app you created with the configuration API (&#x60;appId&#x60;).    In the body of the request, you will inform the new value (&#x60;appFieldValue&#x60;, passed through the body) of the specific field created in this app (identified by the &#x60;appFieldName&#x60; parameter, passed through the URL).    The [orderForm](https://developers.vtex.com/docs/guides/orderform-fields) is the data structure which represents a shopping cart and contains all information pertaining to it. Hence, the &#x60;orderFormId&#x60; is the identification code of a given cart.

### Example

```javascript
import CheckoutApi from 'checkout_api';

let apiInstance = new CheckoutApi.CustomDataApi();
let orderFormId = "orderFormId_example"; // String | The ID of the orderForm whose custom field's value you want to change.
let appId = "appId_example"; // String | ID of the app created through the Update orderForm Configuration endpoint.
let appFieldName = "appFieldName_example"; // String | Name of the app's field created through the Update orderForm Configuration endpoint.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let setsinglecustomfieldvalueRequest = {"value":"{{appFieldValue}}"}; // SetsinglecustomfieldvalueRequest | 
apiInstance.setSingleCustomFieldValue(orderFormId, appId, appFieldName, contentType, accept, setsinglecustomfieldvalueRequest, (error, data, response) => {
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
 **orderFormId** | **String**| The ID of the orderForm whose custom field&#39;s value you want to change. | 
 **appId** | **String**| ID of the app created through the Update orderForm Configuration endpoint. | 
 **appFieldName** | **String**| Name of the app&#39;s field created through the Update orderForm Configuration endpoint. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **setsinglecustomfieldvalueRequest** | [**SetsinglecustomfieldvalueRequest**](SetsinglecustomfieldvalueRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

