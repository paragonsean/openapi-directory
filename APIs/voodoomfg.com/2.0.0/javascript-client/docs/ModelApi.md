# VoodooManufacturing3DPrintApi.ModelApi

All URIs are relative to */api/2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modelGet**](ModelApi.md#modelGet) | **GET** /model | Retrieve the models you&#39;ve created. 
[**modelModelIdGet**](ModelApi.md#modelModelIdGet) | **GET** /model/{model_id} | Retrieve a previously created model by its id. 
[**modelPost**](ModelApi.md#modelPost) | **POST** /model | Models represent 3D design files that you&#39;d like to produce. Creating models is generally the first step in creating an order. 
[**modelQuoteAttrsGet**](ModelApi.md#modelQuoteAttrsGet) | **GET** /model/quote_attrs | Get a quote for a model with the given attributes. 
[**modelQuoteGet**](ModelApi.md#modelQuoteGet) | **GET** /model/quote | Get a quote a given model id. 



## modelGet

> [Model] modelGet()

Retrieve the models you&#39;ve created. 

Lists all of the models you&#39;ve created. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.ModelApi();
apiInstance.modelGet((error, data, response) => {
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

[**[Model]**](Model.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelModelIdGet

> Model modelModelIdGet(modelId)

Retrieve a previously created model by its id. 

In cases where you&#39;re ordering models you&#39;ve created previously, you can fetch a specific model by its id. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.ModelApi();
let modelId = 56; // Number | 
apiInstance.modelModelIdGet(modelId, (error, data, response) => {
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
 **modelId** | **Number**|  | 

### Return type

[**Model**](Model.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelPost

> Model modelPost(body)

Models represent 3D design files that you&#39;d like to produce. Creating models is generally the first step in creating an order. 

Downloads the model data from the URL specified by file_url and saves it as a model. As a part of the model upload process, the file is run through a program that repairs the mesh (closing holes, flipping inverted normals, etc). In some cases, this may alter the geometry of your model. If you&#39;re noticing bad results for your created models, you might consider repairing your files before submitting them. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.ModelApi();
let body = new VoodooManufacturing3DPrintApi.CreateModelBody(); // CreateModelBody | 
apiInstance.modelPost(body, (error, data, response) => {
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
 **body** | [**CreateModelBody**](CreateModelBody.md)|  | 

### Return type

[**Model**](Model.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelQuoteAttrsGet

> ModelQuote modelQuoteAttrsGet(x, y, z, volume, surfaceArea, materialId, quantity, units, opts)

Get a quote for a model with the given attributes. 

This endpoint will provide a quote for a model matching the submitted parameters. Note that this quote may be different than the quote provided by /model/quote in the case that your attribute calculations differ from the ones used by Voodoo Manufacturing. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.ModelApi();
let x = 3.4; // Number | The calculated unitless x dimension of this model's bounding box.
let y = 3.4; // Number | The calculated unitless y dimension of this model's bounding box.
let z = 3.4; // Number | The calculated unitless z dimension of this model's bounding box.
let volume = 3.4; // Number | The calculated unitless volume of the model.
let surfaceArea = 3.4; // Number | The calculated unitless surface area of the model.
let materialId = 3.4; // Number | The unique id of the desired material.
let quantity = 3.4; // Number | The number of units in this quote.
let units = "units_example"; // String | The units of the model file. Either \"mm\", \"cm\", or \"in\". The correct value to pass here depends on which design program you're using. Defaults to \"mm\".
let opts = {
  'optionsOrientation': true // Boolean | Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you're not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation.
};
apiInstance.modelQuoteAttrsGet(x, y, z, volume, surfaceArea, materialId, quantity, units, opts, (error, data, response) => {
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
 **x** | **Number**| The calculated unitless x dimension of this model&#39;s bounding box. | 
 **y** | **Number**| The calculated unitless y dimension of this model&#39;s bounding box. | 
 **z** | **Number**| The calculated unitless z dimension of this model&#39;s bounding box. | 
 **volume** | **Number**| The calculated unitless volume of the model. | 
 **surfaceArea** | **Number**| The calculated unitless surface area of the model. | 
 **materialId** | **Number**| The unique id of the desired material. | 
 **quantity** | **Number**| The number of units in this quote. | 
 **units** | **String**| The units of the model file. Either \&quot;mm\&quot;, \&quot;cm\&quot;, or \&quot;in\&quot;. The correct value to pass here depends on which design program you&#39;re using. Defaults to \&quot;mm\&quot;. | 
 **optionsOrientation** | **Boolean**| Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you&#39;re not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation. | [optional] 

### Return type

[**ModelQuote**](ModelQuote.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelQuoteGet

> ModelQuote modelQuoteGet(modelId, materialId, quantity, units, opts)

Get a quote a given model id. 

Calculates a quote for the given model in the given material and quantity. This endpoint required that you&#39;ve already uploaded the model to our servers -- to get a quote for a model you haven&#39;t yet uploaded, you can try /model/quote_attrs. 

### Example

```javascript
import VoodooManufacturing3DPrintApi from 'voodoo_manufacturing_3_d_print_api';
let defaultClient = VoodooManufacturing3DPrintApi.ApiClient.instance;
// Configure API key authorization: Voodoo Manufacturing API Key
let Voodoo Manufacturing API Key = defaultClient.authentications['Voodoo Manufacturing API Key'];
Voodoo Manufacturing API Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Voodoo Manufacturing API Key.apiKeyPrefix = 'Token';

let apiInstance = new VoodooManufacturing3DPrintApi.ModelApi();
let modelId = 56; // Number | The unique id of the model you'd like to quote.
let materialId = 3.4; // Number | The unique id of the desired material.
let quantity = 3.4; // Number | The number of units in this quote.
let units = "units_example"; // String | The units of the model file. Either \"mm\", \"cm\", or \"in\". The correct value to pass here depends on which design program you're using. Defaults to \"mm\".
let opts = {
  'optionsOrientation': true // Boolean | Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you're not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation.
};
apiInstance.modelQuoteGet(modelId, materialId, quantity, units, opts, (error, data, response) => {
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
 **modelId** | **Number**| The unique id of the model you&#39;d like to quote. | 
 **materialId** | **Number**| The unique id of the desired material. | 
 **quantity** | **Number**| The number of units in this quote. | 
 **units** | **String**| The units of the model file. Either \&quot;mm\&quot;, \&quot;cm\&quot;, or \&quot;in\&quot;. The correct value to pass here depends on which design program you&#39;re using. Defaults to \&quot;mm\&quot;. | 
 **optionsOrientation** | **Boolean**| Indicates whether or not this model needs to be oriented prior to printing. If your model is already oriented for 3D printing, you can omit this flag (or set it to false) and it will not be re-oriented prior to printing. If true, it will be re-oriented prior to printing. If you&#39;re not sure if your model is oriented, you should set this flag to true. There is an additional charge for orientation. | [optional] 

### Return type

[**ModelQuote**](ModelQuote.md)

### Authorization

[Voodoo Manufacturing API Key](../README.md#Voodoo Manufacturing API Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

