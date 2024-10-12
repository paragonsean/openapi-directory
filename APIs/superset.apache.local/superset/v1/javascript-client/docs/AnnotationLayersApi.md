# Superset.AnnotationLayersApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annotationLayerDelete**](AnnotationLayersApi.md#annotationLayerDelete) | **DELETE** /annotation_layer/ | 
[**annotationLayerGet**](AnnotationLayersApi.md#annotationLayerGet) | **GET** /annotation_layer/ | 
[**annotationLayerInfoGet**](AnnotationLayersApi.md#annotationLayerInfoGet) | **GET** /annotation_layer/_info | 
[**annotationLayerPkAnnotationAnnotationIdDelete**](AnnotationLayersApi.md#annotationLayerPkAnnotationAnnotationIdDelete) | **DELETE** /annotation_layer/{pk}/annotation/{annotation_id} | 
[**annotationLayerPkAnnotationAnnotationIdGet**](AnnotationLayersApi.md#annotationLayerPkAnnotationAnnotationIdGet) | **GET** /annotation_layer/{pk}/annotation/{annotation_id} | 
[**annotationLayerPkAnnotationAnnotationIdPut**](AnnotationLayersApi.md#annotationLayerPkAnnotationAnnotationIdPut) | **PUT** /annotation_layer/{pk}/annotation/{annotation_id} | 
[**annotationLayerPkAnnotationDelete**](AnnotationLayersApi.md#annotationLayerPkAnnotationDelete) | **DELETE** /annotation_layer/{pk}/annotation/ | 
[**annotationLayerPkAnnotationGet**](AnnotationLayersApi.md#annotationLayerPkAnnotationGet) | **GET** /annotation_layer/{pk}/annotation/ | 
[**annotationLayerPkAnnotationPost**](AnnotationLayersApi.md#annotationLayerPkAnnotationPost) | **POST** /annotation_layer/{pk}/annotation/ | 
[**annotationLayerPkDelete**](AnnotationLayersApi.md#annotationLayerPkDelete) | **DELETE** /annotation_layer/{pk} | 
[**annotationLayerPkGet**](AnnotationLayersApi.md#annotationLayerPkGet) | **GET** /annotation_layer/{pk} | 
[**annotationLayerPkPut**](AnnotationLayersApi.md#annotationLayerPkPut) | **PUT** /annotation_layer/{pk} | 
[**annotationLayerPost**](AnnotationLayersApi.md#annotationLayerPost) | **POST** /annotation_layer/ | 
[**annotationLayerRelatedColumnNameGet**](AnnotationLayersApi.md#annotationLayerRelatedColumnNameGet) | **GET** /annotation_layer/related/{column_name} | 



## annotationLayerDelete

> AnnotationLayerGet400Response annotationLayerDelete(opts)



Deletes multiple annotation layers in a bulk operation.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.annotationLayerDelete(opts, (error, data, response) => {
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
 **q** | [**[Number]**](Number.md)|  | [optional] 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## annotationLayerGet

> AnnotationLayerGet200Response annotationLayerGet(opts)



Get a list of Annotation layers, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.annotationLayerGet(opts, (error, data, response) => {
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
 **q** | [**GetListSchema**](.md)|  | [optional] 

### Return type

[**AnnotationLayerGet200Response**](AnnotationLayerGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## annotationLayerInfoGet

> AnnotationLayerInfoGet200Response annotationLayerInfoGet(opts)



Get metadata information about this API resource

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let opts = {
  'q': new Superset.GetInfoSchema() // GetInfoSchema | 
};
apiInstance.annotationLayerInfoGet(opts, (error, data, response) => {
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
 **q** | [**GetInfoSchema**](.md)|  | [optional] 

### Return type

[**AnnotationLayerInfoGet200Response**](AnnotationLayerInfoGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## annotationLayerPkAnnotationAnnotationIdDelete

> AnnotationLayerGet400Response annotationLayerPkAnnotationAnnotationIdDelete(pk, annotationId)



Delete Annotation layer

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let pk = 56; // Number | The annotation layer pk for this annotation
let annotationId = 56; // Number | The annotation pk for this annotation
apiInstance.annotationLayerPkAnnotationAnnotationIdDelete(pk, annotationId, (error, data, response) => {
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
 **pk** | **Number**| The annotation layer pk for this annotation | 
 **annotationId** | **Number**| The annotation pk for this annotation | 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## annotationLayerPkAnnotationAnnotationIdGet

> AnnotationLayerPkAnnotationAnnotationIdGet200Response annotationLayerPkAnnotationAnnotationIdGet(pk, annotationId, opts)



Get an Annotation layer

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let pk = 56; // Number | The annotation layer pk for this annotation
let annotationId = 56; // Number | The annotation pk
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.annotationLayerPkAnnotationAnnotationIdGet(pk, annotationId, opts, (error, data, response) => {
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
 **pk** | **Number**| The annotation layer pk for this annotation | 
 **annotationId** | **Number**| The annotation pk | 
 **q** | [**GetItemSchema**](.md)|  | [optional] 

### Return type

[**AnnotationLayerPkAnnotationAnnotationIdGet200Response**](AnnotationLayerPkAnnotationAnnotationIdGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## annotationLayerPkAnnotationAnnotationIdPut

> AnnotationLayerPkAnnotationAnnotationIdPut200Response annotationLayerPkAnnotationAnnotationIdPut(pk, annotationId, annotationRestApiPut)



Update an Annotation layer

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let pk = 56; // Number | The annotation layer pk for this annotation
let annotationId = 56; // Number | The annotation pk for this annotation
let annotationRestApiPut = new Superset.AnnotationRestApiPut(); // AnnotationRestApiPut | Annotation schema
apiInstance.annotationLayerPkAnnotationAnnotationIdPut(pk, annotationId, annotationRestApiPut, (error, data, response) => {
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
 **pk** | **Number**| The annotation layer pk for this annotation | 
 **annotationId** | **Number**| The annotation pk for this annotation | 
 **annotationRestApiPut** | [**AnnotationRestApiPut**](AnnotationRestApiPut.md)| Annotation schema | 

### Return type

[**AnnotationLayerPkAnnotationAnnotationIdPut200Response**](AnnotationLayerPkAnnotationAnnotationIdPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## annotationLayerPkAnnotationDelete

> AnnotationLayerGet400Response annotationLayerPkAnnotationDelete(pk, opts)



Deletes multiple annotation in a bulk operation.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let pk = 56; // Number | The annotation layer pk for this annotation
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.annotationLayerPkAnnotationDelete(pk, opts, (error, data, response) => {
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
 **pk** | **Number**| The annotation layer pk for this annotation | 
 **q** | [**[Number]**](Number.md)|  | [optional] 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## annotationLayerPkAnnotationGet

> AnnotationLayerPkAnnotationGet200Response annotationLayerPkAnnotationGet(pk, opts)



Get a list of Annotation layers, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let pk = 56; // Number | The annotation layer id for this annotation
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.annotationLayerPkAnnotationGet(pk, opts, (error, data, response) => {
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
 **pk** | **Number**| The annotation layer id for this annotation | 
 **q** | [**GetListSchema**](.md)|  | [optional] 

### Return type

[**AnnotationLayerPkAnnotationGet200Response**](AnnotationLayerPkAnnotationGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## annotationLayerPkAnnotationPost

> AnnotationLayerPkAnnotationPost201Response annotationLayerPkAnnotationPost(pk, annotationRestApiPost)



Create an Annotation layer

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let pk = 56; // Number | The annotation layer pk for this annotation
let annotationRestApiPost = new Superset.AnnotationRestApiPost(); // AnnotationRestApiPost | Annotation schema
apiInstance.annotationLayerPkAnnotationPost(pk, annotationRestApiPost, (error, data, response) => {
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
 **pk** | **Number**| The annotation layer pk for this annotation | 
 **annotationRestApiPost** | [**AnnotationRestApiPost**](AnnotationRestApiPost.md)| Annotation schema | 

### Return type

[**AnnotationLayerPkAnnotationPost201Response**](AnnotationLayerPkAnnotationPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## annotationLayerPkDelete

> AnnotationLayerGet400Response annotationLayerPkDelete(pk)



Delete Annotation layer

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let pk = 56; // Number | The annotation layer pk for this annotation
apiInstance.annotationLayerPkDelete(pk, (error, data, response) => {
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
 **pk** | **Number**| The annotation layer pk for this annotation | 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## annotationLayerPkGet

> AnnotationLayerPkGet200Response annotationLayerPkGet(pk, opts)



Get an Annotation layer

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let pk = 56; // Number | 
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.annotationLayerPkGet(pk, opts, (error, data, response) => {
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
 **pk** | **Number**|  | 
 **q** | [**GetItemSchema**](.md)|  | [optional] 

### Return type

[**AnnotationLayerPkGet200Response**](AnnotationLayerPkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## annotationLayerPkPut

> AnnotationLayerPkPut200Response annotationLayerPkPut(pk, annotationLayerRestApiPut)



Update an Annotation layer

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let pk = 56; // Number | The annotation layer pk for this annotation
let annotationLayerRestApiPut = new Superset.AnnotationLayerRestApiPut(); // AnnotationLayerRestApiPut | Annotation schema
apiInstance.annotationLayerPkPut(pk, annotationLayerRestApiPut, (error, data, response) => {
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
 **pk** | **Number**| The annotation layer pk for this annotation | 
 **annotationLayerRestApiPut** | [**AnnotationLayerRestApiPut**](AnnotationLayerRestApiPut.md)| Annotation schema | 

### Return type

[**AnnotationLayerPkPut200Response**](AnnotationLayerPkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## annotationLayerPost

> AnnotationLayerPost201Response annotationLayerPost(annotationLayerRestApiPost)



Create an Annotation layer

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let annotationLayerRestApiPost = new Superset.AnnotationLayerRestApiPost(); // AnnotationLayerRestApiPost | Annotation Layer schema
apiInstance.annotationLayerPost(annotationLayerRestApiPost, (error, data, response) => {
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
 **annotationLayerRestApiPost** | [**AnnotationLayerRestApiPost**](AnnotationLayerRestApiPost.md)| Annotation Layer schema | 

### Return type

[**AnnotationLayerPost201Response**](AnnotationLayerPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## annotationLayerRelatedColumnNameGet

> RelatedResponseSchema annotationLayerRelatedColumnNameGet(columnName, opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.AnnotationLayersApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.annotationLayerRelatedColumnNameGet(columnName, opts, (error, data, response) => {
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
 **columnName** | **String**|  | 
 **q** | [**GetRelatedSchema**](.md)|  | [optional] 

### Return type

[**RelatedResponseSchema**](RelatedResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

