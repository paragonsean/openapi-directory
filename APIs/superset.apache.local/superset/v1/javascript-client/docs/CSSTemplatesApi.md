# Superset.CSSTemplatesApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cssTemplateDelete**](CSSTemplatesApi.md#cssTemplateDelete) | **DELETE** /css_template/ | 
[**cssTemplateGet**](CSSTemplatesApi.md#cssTemplateGet) | **GET** /css_template/ | 
[**cssTemplateInfoGet**](CSSTemplatesApi.md#cssTemplateInfoGet) | **GET** /css_template/_info | 
[**cssTemplatePkDelete**](CSSTemplatesApi.md#cssTemplatePkDelete) | **DELETE** /css_template/{pk} | 
[**cssTemplatePkGet**](CSSTemplatesApi.md#cssTemplatePkGet) | **GET** /css_template/{pk} | 
[**cssTemplatePkPut**](CSSTemplatesApi.md#cssTemplatePkPut) | **PUT** /css_template/{pk} | 
[**cssTemplatePost**](CSSTemplatesApi.md#cssTemplatePost) | **POST** /css_template/ | 
[**cssTemplateRelatedColumnNameGet**](CSSTemplatesApi.md#cssTemplateRelatedColumnNameGet) | **GET** /css_template/related/{column_name} | 



## cssTemplateDelete

> AnnotationLayerGet400Response cssTemplateDelete(opts)



Deletes multiple css templates in a bulk operation.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.CSSTemplatesApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.cssTemplateDelete(opts, (error, data, response) => {
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


## cssTemplateGet

> CssTemplateGet200Response cssTemplateGet(opts)



Get a list of CSS templates, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.CSSTemplatesApi();
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.cssTemplateGet(opts, (error, data, response) => {
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

[**CssTemplateGet200Response**](CssTemplateGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cssTemplateInfoGet

> AnnotationLayerInfoGet200Response cssTemplateInfoGet(opts)



Get metadata information about this API resource

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.CSSTemplatesApi();
let opts = {
  'q': new Superset.GetInfoSchema() // GetInfoSchema | 
};
apiInstance.cssTemplateInfoGet(opts, (error, data, response) => {
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


## cssTemplatePkDelete

> AnnotationLayerGet400Response cssTemplatePkDelete(pk)



Delete CSS template

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.CSSTemplatesApi();
let pk = 56; // Number | 
apiInstance.cssTemplatePkDelete(pk, (error, data, response) => {
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

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cssTemplatePkGet

> CssTemplatePkGet200Response cssTemplatePkGet(pk, opts)



Get a CSS template

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.CSSTemplatesApi();
let pk = 56; // Number | 
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.cssTemplatePkGet(pk, opts, (error, data, response) => {
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

[**CssTemplatePkGet200Response**](CssTemplatePkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cssTemplatePkPut

> CssTemplatePkPut200Response cssTemplatePkPut(pk, cssTemplateRestApiPut)



Update a CSS template

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.CSSTemplatesApi();
let pk = 56; // Number | 
let cssTemplateRestApiPut = new Superset.CssTemplateRestApiPut(); // CssTemplateRestApiPut | Model schema
apiInstance.cssTemplatePkPut(pk, cssTemplateRestApiPut, (error, data, response) => {
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
 **cssTemplateRestApiPut** | [**CssTemplateRestApiPut**](CssTemplateRestApiPut.md)| Model schema | 

### Return type

[**CssTemplatePkPut200Response**](CssTemplatePkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cssTemplatePost

> CssTemplatePost201Response cssTemplatePost(cssTemplateRestApiPost)



Create a CSS template

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.CSSTemplatesApi();
let cssTemplateRestApiPost = new Superset.CssTemplateRestApiPost(); // CssTemplateRestApiPost | Model schema
apiInstance.cssTemplatePost(cssTemplateRestApiPost, (error, data, response) => {
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
 **cssTemplateRestApiPost** | [**CssTemplateRestApiPost**](CssTemplateRestApiPost.md)| Model schema | 

### Return type

[**CssTemplatePost201Response**](CssTemplatePost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cssTemplateRelatedColumnNameGet

> RelatedResponseSchema cssTemplateRelatedColumnNameGet(columnName, opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.CSSTemplatesApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.cssTemplateRelatedColumnNameGet(columnName, opts, (error, data, response) => {
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

