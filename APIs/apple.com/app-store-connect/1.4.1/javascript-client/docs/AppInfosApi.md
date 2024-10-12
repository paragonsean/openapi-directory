# AppStoreConnectApi.AppInfosApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appInfosAgeRatingDeclarationGetToOneRelated**](AppInfosApi.md#appInfosAgeRatingDeclarationGetToOneRelated) | **GET** /v1/appInfos/{id}/ageRatingDeclaration | 
[**appInfosAppInfoLocalizationsGetToManyRelated**](AppInfosApi.md#appInfosAppInfoLocalizationsGetToManyRelated) | **GET** /v1/appInfos/{id}/appInfoLocalizations | 
[**appInfosGetInstance**](AppInfosApi.md#appInfosGetInstance) | **GET** /v1/appInfos/{id} | 
[**appInfosPrimaryCategoryGetToOneRelated**](AppInfosApi.md#appInfosPrimaryCategoryGetToOneRelated) | **GET** /v1/appInfos/{id}/primaryCategory | 
[**appInfosPrimarySubcategoryOneGetToOneRelated**](AppInfosApi.md#appInfosPrimarySubcategoryOneGetToOneRelated) | **GET** /v1/appInfos/{id}/primarySubcategoryOne | 
[**appInfosPrimarySubcategoryTwoGetToOneRelated**](AppInfosApi.md#appInfosPrimarySubcategoryTwoGetToOneRelated) | **GET** /v1/appInfos/{id}/primarySubcategoryTwo | 
[**appInfosSecondaryCategoryGetToOneRelated**](AppInfosApi.md#appInfosSecondaryCategoryGetToOneRelated) | **GET** /v1/appInfos/{id}/secondaryCategory | 
[**appInfosSecondarySubcategoryOneGetToOneRelated**](AppInfosApi.md#appInfosSecondarySubcategoryOneGetToOneRelated) | **GET** /v1/appInfos/{id}/secondarySubcategoryOne | 
[**appInfosSecondarySubcategoryTwoGetToOneRelated**](AppInfosApi.md#appInfosSecondarySubcategoryTwoGetToOneRelated) | **GET** /v1/appInfos/{id}/secondarySubcategoryTwo | 
[**appInfosUpdateInstance**](AppInfosApi.md#appInfosUpdateInstance) | **PATCH** /v1/appInfos/{id} | 



## appInfosAgeRatingDeclarationGetToOneRelated

> AgeRatingDeclarationResponse appInfosAgeRatingDeclarationGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppInfosApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAgeRatingDeclarations': ["null"] // [String] | the fields to include for returned resources of type ageRatingDeclarations
};
apiInstance.appInfosAgeRatingDeclarationGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAgeRatingDeclarations** | [**[String]**](String.md)| the fields to include for returned resources of type ageRatingDeclarations | [optional] 

### Return type

[**AgeRatingDeclarationResponse**](AgeRatingDeclarationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInfosAppInfoLocalizationsGetToManyRelated

> AppInfoLocalizationsResponse appInfosAppInfoLocalizationsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppInfosApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'filterLocale': ["null"], // [String] | filter by attribute 'locale'
  'fieldsAppInfos': ["null"], // [String] | the fields to include for returned resources of type appInfos
  'fieldsAppInfoLocalizations': ["null"], // [String] | the fields to include for returned resources of type appInfoLocalizations
  'limit': 56, // Number | maximum resources per page
  'include': ["null"] // [String] | comma-separated list of relationships to include
};
apiInstance.appInfosAppInfoLocalizationsGetToManyRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **filterLocale** | [**[String]**](String.md)| filter by attribute &#39;locale&#39; | [optional] 
 **fieldsAppInfos** | [**[String]**](String.md)| the fields to include for returned resources of type appInfos | [optional] 
 **fieldsAppInfoLocalizations** | [**[String]**](String.md)| the fields to include for returned resources of type appInfoLocalizations | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 

### Return type

[**AppInfoLocalizationsResponse**](AppInfoLocalizationsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInfosGetInstance

> AppInfoResponse appInfosGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppInfosApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppInfos': ["null"], // [String] | the fields to include for returned resources of type appInfos
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsAgeRatingDeclarations': ["null"], // [String] | the fields to include for returned resources of type ageRatingDeclarations
  'fieldsAppCategories': ["null"], // [String] | the fields to include for returned resources of type appCategories
  'fieldsAppInfoLocalizations': ["null"], // [String] | the fields to include for returned resources of type appInfoLocalizations
  'limitAppInfoLocalizations': 56 // Number | maximum number of related appInfoLocalizations returned (when they are included)
};
apiInstance.appInfosGetInstance(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppInfos** | [**[String]**](String.md)| the fields to include for returned resources of type appInfos | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsAgeRatingDeclarations** | [**[String]**](String.md)| the fields to include for returned resources of type ageRatingDeclarations | [optional] 
 **fieldsAppCategories** | [**[String]**](String.md)| the fields to include for returned resources of type appCategories | [optional] 
 **fieldsAppInfoLocalizations** | [**[String]**](String.md)| the fields to include for returned resources of type appInfoLocalizations | [optional] 
 **limitAppInfoLocalizations** | **Number**| maximum number of related appInfoLocalizations returned (when they are included) | [optional] 

### Return type

[**AppInfoResponse**](AppInfoResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInfosPrimaryCategoryGetToOneRelated

> AppCategoryResponse appInfosPrimaryCategoryGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppInfosApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppCategories': ["null"] // [String] | the fields to include for returned resources of type appCategories
};
apiInstance.appInfosPrimaryCategoryGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppCategories** | [**[String]**](String.md)| the fields to include for returned resources of type appCategories | [optional] 

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInfosPrimarySubcategoryOneGetToOneRelated

> AppCategoryResponse appInfosPrimarySubcategoryOneGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppInfosApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppCategories': ["null"] // [String] | the fields to include for returned resources of type appCategories
};
apiInstance.appInfosPrimarySubcategoryOneGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppCategories** | [**[String]**](String.md)| the fields to include for returned resources of type appCategories | [optional] 

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInfosPrimarySubcategoryTwoGetToOneRelated

> AppCategoryResponse appInfosPrimarySubcategoryTwoGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppInfosApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppCategories': ["null"] // [String] | the fields to include for returned resources of type appCategories
};
apiInstance.appInfosPrimarySubcategoryTwoGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppCategories** | [**[String]**](String.md)| the fields to include for returned resources of type appCategories | [optional] 

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInfosSecondaryCategoryGetToOneRelated

> AppCategoryResponse appInfosSecondaryCategoryGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppInfosApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppCategories': ["null"] // [String] | the fields to include for returned resources of type appCategories
};
apiInstance.appInfosSecondaryCategoryGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppCategories** | [**[String]**](String.md)| the fields to include for returned resources of type appCategories | [optional] 

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInfosSecondarySubcategoryOneGetToOneRelated

> AppCategoryResponse appInfosSecondarySubcategoryOneGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppInfosApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppCategories': ["null"] // [String] | the fields to include for returned resources of type appCategories
};
apiInstance.appInfosSecondarySubcategoryOneGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppCategories** | [**[String]**](String.md)| the fields to include for returned resources of type appCategories | [optional] 

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInfosSecondarySubcategoryTwoGetToOneRelated

> AppCategoryResponse appInfosSecondarySubcategoryTwoGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppInfosApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppCategories': ["null"] // [String] | the fields to include for returned resources of type appCategories
};
apiInstance.appInfosSecondarySubcategoryTwoGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppCategories** | [**[String]**](String.md)| the fields to include for returned resources of type appCategories | [optional] 

### Return type

[**AppCategoryResponse**](AppCategoryResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appInfosUpdateInstance

> AppInfoResponse appInfosUpdateInstance(id, appInfoUpdateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppInfosApi();
let id = "id_example"; // String | the id of the requested resource
let appInfoUpdateRequest = new AppStoreConnectApi.AppInfoUpdateRequest(); // AppInfoUpdateRequest | AppInfo representation
apiInstance.appInfosUpdateInstance(id, appInfoUpdateRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **appInfoUpdateRequest** | [**AppInfoUpdateRequest**](AppInfoUpdateRequest.md)| AppInfo representation | 

### Return type

[**AppInfoResponse**](AppInfoResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

