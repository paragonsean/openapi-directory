# Superset.DashboardsApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dashboardDelete**](DashboardsApi.md#dashboardDelete) | **DELETE** /dashboard/ | 
[**dashboardExportGet**](DashboardsApi.md#dashboardExportGet) | **GET** /dashboard/export/ | 
[**dashboardFavoriteStatusGet**](DashboardsApi.md#dashboardFavoriteStatusGet) | **GET** /dashboard/favorite_status/ | 
[**dashboardGet**](DashboardsApi.md#dashboardGet) | **GET** /dashboard/ | 
[**dashboardIdOrSlugChartsGet**](DashboardsApi.md#dashboardIdOrSlugChartsGet) | **GET** /dashboard/{id_or_slug}/charts | 
[**dashboardIdOrSlugDatasetsGet**](DashboardsApi.md#dashboardIdOrSlugDatasetsGet) | **GET** /dashboard/{id_or_slug}/datasets | 
[**dashboardIdOrSlugGet**](DashboardsApi.md#dashboardIdOrSlugGet) | **GET** /dashboard/{id_or_slug} | 
[**dashboardImportPost**](DashboardsApi.md#dashboardImportPost) | **POST** /dashboard/import/ | 
[**dashboardInfoGet**](DashboardsApi.md#dashboardInfoGet) | **GET** /dashboard/_info | 
[**dashboardPkDelete**](DashboardsApi.md#dashboardPkDelete) | **DELETE** /dashboard/{pk} | 
[**dashboardPkPut**](DashboardsApi.md#dashboardPkPut) | **PUT** /dashboard/{pk} | 
[**dashboardPkThumbnailDigestGet**](DashboardsApi.md#dashboardPkThumbnailDigestGet) | **GET** /dashboard/{pk}/thumbnail/{digest}/ | 
[**dashboardPost**](DashboardsApi.md#dashboardPost) | **POST** /dashboard/ | 
[**dashboardRelatedColumnNameGet**](DashboardsApi.md#dashboardRelatedColumnNameGet) | **GET** /dashboard/related/{column_name} | 



## dashboardDelete

> AnnotationLayerGet400Response dashboardDelete(opts)



Deletes multiple Dashboards in a bulk operation.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.dashboardDelete(opts, (error, data, response) => {
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


## dashboardExportGet

> String dashboardExportGet(opts)



Exports multiple Dashboards and downloads them as YAML files.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.dashboardExportGet(opts, (error, data, response) => {
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

**String**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json


## dashboardFavoriteStatusGet

> GetFavStarIdsSchema dashboardFavoriteStatusGet(opts)



Check favorited dashboards for current user

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.dashboardFavoriteStatusGet(opts, (error, data, response) => {
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

[**GetFavStarIdsSchema**](GetFavStarIdsSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dashboardGet

> DashboardGet200Response dashboardGet(opts)



Get a list of dashboards, use Rison or JSON query parameters for filtering, sorting, pagination and  for selecting specific columns and metadata.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.dashboardGet(opts, (error, data, response) => {
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

[**DashboardGet200Response**](DashboardGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dashboardIdOrSlugChartsGet

> DashboardIdOrSlugChartsGet200Response dashboardIdOrSlugChartsGet(idOrSlug)



Get the chart definitions for a given dashboard

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let idOrSlug = "idOrSlug_example"; // String | 
apiInstance.dashboardIdOrSlugChartsGet(idOrSlug, (error, data, response) => {
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
 **idOrSlug** | **String**|  | 

### Return type

[**DashboardIdOrSlugChartsGet200Response**](DashboardIdOrSlugChartsGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dashboardIdOrSlugDatasetsGet

> DashboardIdOrSlugDatasetsGet200Response dashboardIdOrSlugDatasetsGet(idOrSlug)



Returns a list of a dashboard&#39;s datasets. Each dataset includes only the information necessary to render the dashboard&#39;s charts.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let idOrSlug = "idOrSlug_example"; // String | Either the id of the dashboard, or its slug
apiInstance.dashboardIdOrSlugDatasetsGet(idOrSlug, (error, data, response) => {
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
 **idOrSlug** | **String**| Either the id of the dashboard, or its slug | 

### Return type

[**DashboardIdOrSlugDatasetsGet200Response**](DashboardIdOrSlugDatasetsGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dashboardIdOrSlugGet

> DashboardIdOrSlugGet200Response dashboardIdOrSlugGet(idOrSlug)



Get a dashboard detail information.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let idOrSlug = "idOrSlug_example"; // String | Either the id of the dashboard, or its slug
apiInstance.dashboardIdOrSlugGet(idOrSlug, (error, data, response) => {
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
 **idOrSlug** | **String**| Either the id of the dashboard, or its slug | 

### Return type

[**DashboardIdOrSlugGet200Response**](DashboardIdOrSlugGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dashboardImportPost

> AnnotationLayerGet400Response dashboardImportPost(opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let opts = {
  'formData': "/path/to/file", // File | upload file (ZIP or JSON)
  'overwrite': true, // Boolean | overwrite existing databases?
  'passwords': "passwords_example" // String | JSON map of passwords for each file
};
apiInstance.dashboardImportPost(opts, (error, data, response) => {
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
 **formData** | **File**| upload file (ZIP or JSON) | [optional] 
 **overwrite** | **Boolean**| overwrite existing databases? | [optional] 
 **passwords** | **String**| JSON map of passwords for each file | [optional] 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## dashboardInfoGet

> AnnotationLayerInfoGet200Response dashboardInfoGet(opts)



Several metadata information about dashboard API endpoints.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let opts = {
  'q': new Superset.GetInfoSchema() // GetInfoSchema | 
};
apiInstance.dashboardInfoGet(opts, (error, data, response) => {
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


## dashboardPkDelete

> AnnotationLayerGet400Response dashboardPkDelete(pk)



Deletes a Dashboard.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let pk = 56; // Number | 
apiInstance.dashboardPkDelete(pk, (error, data, response) => {
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


## dashboardPkPut

> DashboardPkPut200Response dashboardPkPut(pk, dashboardRestApiPut)



Changes a Dashboard.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let pk = 56; // Number | 
let dashboardRestApiPut = new Superset.DashboardRestApiPut(); // DashboardRestApiPut | Dashboard schema
apiInstance.dashboardPkPut(pk, dashboardRestApiPut, (error, data, response) => {
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
 **dashboardRestApiPut** | [**DashboardRestApiPut**](DashboardRestApiPut.md)| Dashboard schema | 

### Return type

[**DashboardPkPut200Response**](DashboardPkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dashboardPkThumbnailDigestGet

> File dashboardPkThumbnailDigestGet(pk, digest, opts)



Compute async or get already computed dashboard thumbnail from cache.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let pk = 56; // Number | 
let digest = "digest_example"; // String | A hex digest that makes this dashboard unique
let opts = {
  'q': new Superset.ThumbnailQuerySchema() // ThumbnailQuerySchema | 
};
apiInstance.dashboardPkThumbnailDigestGet(pk, digest, opts, (error, data, response) => {
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
 **digest** | **String**| A hex digest that makes this dashboard unique | 
 **q** | [**ThumbnailQuerySchema**](.md)|  | [optional] 

### Return type

**File**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json


## dashboardPost

> DashboardPost201Response dashboardPost(dashboardRestApiPost)



Create a new Dashboard.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let dashboardRestApiPost = new Superset.DashboardRestApiPost(); // DashboardRestApiPost | Dashboard schema
apiInstance.dashboardPost(dashboardRestApiPost, (error, data, response) => {
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
 **dashboardRestApiPost** | [**DashboardRestApiPost**](DashboardRestApiPost.md)| Dashboard schema | 

### Return type

[**DashboardPost201Response**](DashboardPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dashboardRelatedColumnNameGet

> RelatedResponseSchema dashboardRelatedColumnNameGet(columnName, opts)



Get a list of all possible owners for a dashboard.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DashboardsApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.dashboardRelatedColumnNameGet(columnName, opts, (error, data, response) => {
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

