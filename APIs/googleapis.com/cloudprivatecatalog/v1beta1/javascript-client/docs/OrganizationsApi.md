# CloudPrivateCatalog.OrganizationsApi

All URIs are relative to *https://cloudprivatecatalog.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudprivatecatalogOrganizationsCatalogsSearch**](OrganizationsApi.md#cloudprivatecatalogOrganizationsCatalogsSearch) | **GET** /v1beta1/{resource}/catalogs:search | 
[**cloudprivatecatalogOrganizationsProductsSearch**](OrganizationsApi.md#cloudprivatecatalogOrganizationsProductsSearch) | **GET** /v1beta1/{resource}/products:search | 
[**cloudprivatecatalogOrganizationsVersionsSearch**](OrganizationsApi.md#cloudprivatecatalogOrganizationsVersionsSearch) | **GET** /v1beta1/{resource}/versions:search | 



## cloudprivatecatalogOrganizationsCatalogsSearch

> GoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse cloudprivatecatalogOrganizationsCatalogsSearch(resource, opts)



Search Catalog resources that consumers have access to, within the scope of the consumer cloud resource hierarchy context.

### Example

```javascript
import CloudPrivateCatalog from 'cloud_private_catalog';
let defaultClient = CloudPrivateCatalog.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalog.OrganizationsApi();
let resource = "resource_example"; // String | Required. The name of the resource context. It can be in following formats:  * `projects/{project_id}` * `folders/{folder_id}` * `organizations/{organization_id}`
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of entries that are requested.
  'pageToken': "pageToken_example", // String | A pagination token returned from a previous call to SearchCatalogs that indicates where this listing should continue from. This field is optional.
  'query': "query_example" // String | The query to filter the catalogs. The supported queries are:  * Get a single catalog: `name=catalogs/{catalog_id}`
};
apiInstance.cloudprivatecatalogOrganizationsCatalogsSearch(resource, opts, (error, data, response) => {
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
 **resource** | **String**| Required. The name of the resource context. It can be in following formats:  * &#x60;projects/{project_id}&#x60; * &#x60;folders/{folder_id}&#x60; * &#x60;organizations/{organization_id}&#x60; | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of entries that are requested. | [optional] 
 **pageToken** | **String**| A pagination token returned from a previous call to SearchCatalogs that indicates where this listing should continue from. This field is optional. | [optional] 
 **query** | **String**| The query to filter the catalogs. The supported queries are:  * Get a single catalog: &#x60;name&#x3D;catalogs/{catalog_id}&#x60; | [optional] 

### Return type

[**GoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse**](GoogleCloudPrivatecatalogV1beta1SearchCatalogsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## cloudprivatecatalogOrganizationsProductsSearch

> GoogleCloudPrivatecatalogV1beta1SearchProductsResponse cloudprivatecatalogOrganizationsProductsSearch(resource, opts)



Search Product resources that consumers have access to, within the scope of the consumer cloud resource hierarchy context.

### Example

```javascript
import CloudPrivateCatalog from 'cloud_private_catalog';
let defaultClient = CloudPrivateCatalog.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalog.OrganizationsApi();
let resource = "resource_example"; // String | Required. The name of the resource context. See SearchCatalogsRequest.resource for details.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of entries that are requested.
  'pageToken': "pageToken_example", // String | A pagination token returned from a previous call to SearchProducts that indicates where this listing should continue from. This field is optional.
  'query': "query_example" // String | The query to filter the products.  The supported queries are: * List products of all catalogs: empty * List products under a catalog: `parent=catalogs/{catalog_id}` * Get a product by name: `name=catalogs/{catalog_id}/products/{product_id}`
};
apiInstance.cloudprivatecatalogOrganizationsProductsSearch(resource, opts, (error, data, response) => {
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
 **resource** | **String**| Required. The name of the resource context. See SearchCatalogsRequest.resource for details. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of entries that are requested. | [optional] 
 **pageToken** | **String**| A pagination token returned from a previous call to SearchProducts that indicates where this listing should continue from. This field is optional. | [optional] 
 **query** | **String**| The query to filter the products.  The supported queries are: * List products of all catalogs: empty * List products under a catalog: &#x60;parent&#x3D;catalogs/{catalog_id}&#x60; * Get a product by name: &#x60;name&#x3D;catalogs/{catalog_id}/products/{product_id}&#x60; | [optional] 

### Return type

[**GoogleCloudPrivatecatalogV1beta1SearchProductsResponse**](GoogleCloudPrivatecatalogV1beta1SearchProductsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## cloudprivatecatalogOrganizationsVersionsSearch

> GoogleCloudPrivatecatalogV1beta1SearchVersionsResponse cloudprivatecatalogOrganizationsVersionsSearch(resource, opts)



Search Version resources that consumers have access to, within the scope of the consumer cloud resource hierarchy context.

### Example

```javascript
import CloudPrivateCatalog from 'cloud_private_catalog';
let defaultClient = CloudPrivateCatalog.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalog.OrganizationsApi();
let resource = "resource_example"; // String | Required. The name of the resource context. See SearchCatalogsRequest.resource for details.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of entries that are requested.
  'pageToken': "pageToken_example", // String | A pagination token returned from a previous call to SearchVersions that indicates where this listing should continue from. This field is optional.
  'query': "query_example" // String | The query to filter the versions. Required.  The supported queries are: * List versions under a product: `parent=catalogs/{catalog_id}/products/{product_id}` * Get a version by name: `name=catalogs/{catalog_id}/products/{product_id}/versions/{version_id}`
};
apiInstance.cloudprivatecatalogOrganizationsVersionsSearch(resource, opts, (error, data, response) => {
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
 **resource** | **String**| Required. The name of the resource context. See SearchCatalogsRequest.resource for details. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of entries that are requested. | [optional] 
 **pageToken** | **String**| A pagination token returned from a previous call to SearchVersions that indicates where this listing should continue from. This field is optional. | [optional] 
 **query** | **String**| The query to filter the versions. Required.  The supported queries are: * List versions under a product: &#x60;parent&#x3D;catalogs/{catalog_id}/products/{product_id}&#x60; * Get a version by name: &#x60;name&#x3D;catalogs/{catalog_id}/products/{product_id}/versions/{version_id}&#x60; | [optional] 

### Return type

[**GoogleCloudPrivatecatalogV1beta1SearchVersionsResponse**](GoogleCloudPrivatecatalogV1beta1SearchVersionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

