# CloudPrivateCatalogProducer.CatalogsApi

All URIs are relative to *https://cloudprivatecatalogproducer.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudprivatecatalogproducerCatalogsAssociationsCreate**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsAssociationsCreate) | **POST** /v1beta1/{parent}/associations | 
[**cloudprivatecatalogproducerCatalogsAssociationsList**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsAssociationsList) | **GET** /v1beta1/{parent}/associations | 
[**cloudprivatecatalogproducerCatalogsCreate**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsCreate) | **POST** /v1beta1/catalogs | 
[**cloudprivatecatalogproducerCatalogsGetIamPolicy**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsGetIamPolicy) | **GET** /v1beta1/{resource}:getIamPolicy | 
[**cloudprivatecatalogproducerCatalogsList**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsList) | **GET** /v1beta1/catalogs | 
[**cloudprivatecatalogproducerCatalogsProductsCopy**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsProductsCopy) | **POST** /v1beta1/{name}:copy | 
[**cloudprivatecatalogproducerCatalogsProductsCreate**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsProductsCreate) | **POST** /v1beta1/{parent}/products | 
[**cloudprivatecatalogproducerCatalogsProductsIconsUpload**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsProductsIconsUpload) | **POST** /v1beta1/{product}/icons:upload | 
[**cloudprivatecatalogproducerCatalogsProductsList**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsProductsList) | **GET** /v1beta1/{parent}/products | 
[**cloudprivatecatalogproducerCatalogsProductsVersionsCreate**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsProductsVersionsCreate) | **POST** /v1beta1/{parent}/versions | 
[**cloudprivatecatalogproducerCatalogsProductsVersionsDelete**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsProductsVersionsDelete) | **DELETE** /v1beta1/{name} | 
[**cloudprivatecatalogproducerCatalogsProductsVersionsGet**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsProductsVersionsGet) | **GET** /v1beta1/{name} | 
[**cloudprivatecatalogproducerCatalogsProductsVersionsList**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsProductsVersionsList) | **GET** /v1beta1/{parent}/versions | 
[**cloudprivatecatalogproducerCatalogsProductsVersionsPatch**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsProductsVersionsPatch) | **PATCH** /v1beta1/{name} | 
[**cloudprivatecatalogproducerCatalogsSetIamPolicy**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsSetIamPolicy) | **POST** /v1beta1/{resource}:setIamPolicy | 
[**cloudprivatecatalogproducerCatalogsTestIamPermissions**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsTestIamPermissions) | **POST** /v1beta1/{resource}:testIamPermissions | 
[**cloudprivatecatalogproducerCatalogsUndelete**](CatalogsApi.md#cloudprivatecatalogproducerCatalogsUndelete) | **POST** /v1beta1/{name}:undelete | 



## cloudprivatecatalogproducerCatalogsAssociationsCreate

> GoogleCloudPrivatecatalogproducerV1beta1Association cloudprivatecatalogproducerCatalogsAssociationsCreate(parent, opts)



Creates an Association instance under a given Catalog.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let parent = "parent_example"; // String | The `Catalog` resource's name.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'googleCloudPrivatecatalogproducerV1beta1CreateAssociationRequest': new CloudPrivateCatalogProducer.GoogleCloudPrivatecatalogproducerV1beta1CreateAssociationRequest() // GoogleCloudPrivatecatalogproducerV1beta1CreateAssociationRequest | 
};
apiInstance.cloudprivatecatalogproducerCatalogsAssociationsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The &#x60;Catalog&#x60; resource&#39;s name. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **googleCloudPrivatecatalogproducerV1beta1CreateAssociationRequest** | [**GoogleCloudPrivatecatalogproducerV1beta1CreateAssociationRequest**](GoogleCloudPrivatecatalogproducerV1beta1CreateAssociationRequest.md)|  | [optional] 

### Return type

[**GoogleCloudPrivatecatalogproducerV1beta1Association**](GoogleCloudPrivatecatalogproducerV1beta1Association.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsAssociationsList

> GoogleCloudPrivatecatalogproducerV1beta1ListAssociationsResponse cloudprivatecatalogproducerCatalogsAssociationsList(parent, opts)



Lists all Association resources under a catalog.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let parent = "parent_example"; // String | The resource name of the `Catalog` whose `Associations` are being retrieved. In the format `catalogs/<catalog>`.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'pageSize': 56, // Number | The maximum number of catalog associations to return.
  'pageToken': "pageToken_example" // String | A pagination token returned from the previous call to `ListAssociations`.
};
apiInstance.cloudprivatecatalogproducerCatalogsAssociationsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the &#x60;Catalog&#x60; whose &#x60;Associations&#x60; are being retrieved. In the format &#x60;catalogs/&lt;catalog&gt;&#x60;. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **pageSize** | **Number**| The maximum number of catalog associations to return. | [optional] 
 **pageToken** | **String**| A pagination token returned from the previous call to &#x60;ListAssociations&#x60;. | [optional] 

### Return type

[**GoogleCloudPrivatecatalogproducerV1beta1ListAssociationsResponse**](GoogleCloudPrivatecatalogproducerV1beta1ListAssociationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsCreate

> GoogleLongrunningOperation cloudprivatecatalogproducerCatalogsCreate(opts)



Creates a new Catalog resource.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'googleCloudPrivatecatalogproducerV1beta1Catalog': new CloudPrivateCatalogProducer.GoogleCloudPrivatecatalogproducerV1beta1Catalog() // GoogleCloudPrivatecatalogproducerV1beta1Catalog | 
};
apiInstance.cloudprivatecatalogproducerCatalogsCreate(opts, (error, data, response) => {
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
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **googleCloudPrivatecatalogproducerV1beta1Catalog** | [**GoogleCloudPrivatecatalogproducerV1beta1Catalog**](GoogleCloudPrivatecatalogproducerV1beta1Catalog.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsGetIamPolicy

> GoogleIamV1Policy cloudprivatecatalogproducerCatalogsGetIamPolicy(resource, opts)



Gets IAM policy for the specified Catalog.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'optionsRequestedPolicyVersion': 56 // Number | Optional. The policy format version to be returned.  Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected.  Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset.
};
apiInstance.cloudprivatecatalogproducerCatalogsGetIamPolicy(resource, opts, (error, data, response) => {
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
 **resource** | **String**| REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **optionsRequestedPolicyVersion** | **Number**| Optional. The policy format version to be returned.  Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected.  Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset. | [optional] 

### Return type

[**GoogleIamV1Policy**](GoogleIamV1Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsList

> GoogleCloudPrivatecatalogproducerV1beta1ListCatalogsResponse cloudprivatecatalogproducerCatalogsList(opts)



Lists Catalog resources that the producer has access to, within the scope of the parent resource.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'pageSize': 56, // Number | The maximum number of catalogs to return.
  'pageToken': "pageToken_example", // String | A pagination token returned from a previous call to ListCatalogs that indicates where this listing should continue from. This field is optional.
  'parent': "parent_example" // String | The resource name of the parent resource.
};
apiInstance.cloudprivatecatalogproducerCatalogsList(opts, (error, data, response) => {
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
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **pageSize** | **Number**| The maximum number of catalogs to return. | [optional] 
 **pageToken** | **String**| A pagination token returned from a previous call to ListCatalogs that indicates where this listing should continue from. This field is optional. | [optional] 
 **parent** | **String**| The resource name of the parent resource. | [optional] 

### Return type

[**GoogleCloudPrivatecatalogproducerV1beta1ListCatalogsResponse**](GoogleCloudPrivatecatalogproducerV1beta1ListCatalogsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsProductsCopy

> GoogleLongrunningOperation cloudprivatecatalogproducerCatalogsProductsCopy(name, opts)



Copies a Product under another Catalog.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let name = "name_example"; // String | The resource name of the current product that is copied from.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'googleCloudPrivatecatalogproducerV1beta1CopyProductRequest': new CloudPrivateCatalogProducer.GoogleCloudPrivatecatalogproducerV1beta1CopyProductRequest() // GoogleCloudPrivatecatalogproducerV1beta1CopyProductRequest | 
};
apiInstance.cloudprivatecatalogproducerCatalogsProductsCopy(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the current product that is copied from. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **googleCloudPrivatecatalogproducerV1beta1CopyProductRequest** | [**GoogleCloudPrivatecatalogproducerV1beta1CopyProductRequest**](GoogleCloudPrivatecatalogproducerV1beta1CopyProductRequest.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsProductsCreate

> GoogleCloudPrivatecatalogproducerV1beta1Product cloudprivatecatalogproducerCatalogsProductsCreate(parent, opts)



Creates a Product instance under a given Catalog.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let parent = "parent_example"; // String | The catalog name of the new product's parent.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'googleCloudPrivatecatalogproducerV1beta1Product': new CloudPrivateCatalogProducer.GoogleCloudPrivatecatalogproducerV1beta1Product() // GoogleCloudPrivatecatalogproducerV1beta1Product | 
};
apiInstance.cloudprivatecatalogproducerCatalogsProductsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The catalog name of the new product&#39;s parent. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **googleCloudPrivatecatalogproducerV1beta1Product** | [**GoogleCloudPrivatecatalogproducerV1beta1Product**](GoogleCloudPrivatecatalogproducerV1beta1Product.md)|  | [optional] 

### Return type

[**GoogleCloudPrivatecatalogproducerV1beta1Product**](GoogleCloudPrivatecatalogproducerV1beta1Product.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsProductsIconsUpload

> Object cloudprivatecatalogproducerCatalogsProductsIconsUpload(product, opts)



Creates an Icon instance under a given Product. If Product only has a default icon, a new Icon instance is created and associated with the given Product. If Product already has a non-default icon, the action creates a new Icon instance, associates the newly created Icon with the given Product and deletes the old icon.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let product = "product_example"; // String | The resource name of the product.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'googleCloudPrivatecatalogproducerV1beta1UploadIconRequest': new CloudPrivateCatalogProducer.GoogleCloudPrivatecatalogproducerV1beta1UploadIconRequest() // GoogleCloudPrivatecatalogproducerV1beta1UploadIconRequest | 
};
apiInstance.cloudprivatecatalogproducerCatalogsProductsIconsUpload(product, opts, (error, data, response) => {
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
 **product** | **String**| The resource name of the product. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **googleCloudPrivatecatalogproducerV1beta1UploadIconRequest** | [**GoogleCloudPrivatecatalogproducerV1beta1UploadIconRequest**](GoogleCloudPrivatecatalogproducerV1beta1UploadIconRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsProductsList

> GoogleCloudPrivatecatalogproducerV1beta1ListProductsResponse cloudprivatecatalogproducerCatalogsProductsList(parent, opts)



Lists Product resources that the producer has access to, within the scope of the parent catalog.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let parent = "parent_example"; // String | The resource name of the parent resource.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'filter': "filter_example", // String | A filter expression used to restrict the returned results based upon properties of the product.
  'pageSize': 56, // Number | The maximum number of products to return.
  'pageToken': "pageToken_example" // String | A pagination token returned from a previous call to ListProducts that indicates where this listing should continue from. This field is optional.
};
apiInstance.cloudprivatecatalogproducerCatalogsProductsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the parent resource. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **filter** | **String**| A filter expression used to restrict the returned results based upon properties of the product. | [optional] 
 **pageSize** | **Number**| The maximum number of products to return. | [optional] 
 **pageToken** | **String**| A pagination token returned from a previous call to ListProducts that indicates where this listing should continue from. This field is optional. | [optional] 

### Return type

[**GoogleCloudPrivatecatalogproducerV1beta1ListProductsResponse**](GoogleCloudPrivatecatalogproducerV1beta1ListProductsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsProductsVersionsCreate

> GoogleLongrunningOperation cloudprivatecatalogproducerCatalogsProductsVersionsCreate(parent, opts)



Creates a Version instance under a given Product.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let parent = "parent_example"; // String | The product name of the new version's parent.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'googleCloudPrivatecatalogproducerV1beta1Version': new CloudPrivateCatalogProducer.GoogleCloudPrivatecatalogproducerV1beta1Version() // GoogleCloudPrivatecatalogproducerV1beta1Version | 
};
apiInstance.cloudprivatecatalogproducerCatalogsProductsVersionsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The product name of the new version&#39;s parent. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **googleCloudPrivatecatalogproducerV1beta1Version** | [**GoogleCloudPrivatecatalogproducerV1beta1Version**](GoogleCloudPrivatecatalogproducerV1beta1Version.md)|  | [optional] 

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsProductsVersionsDelete

> Object cloudprivatecatalogproducerCatalogsProductsVersionsDelete(name, opts)



Hard deletes a Version.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let name = "name_example"; // String | The resource name of the version.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'force': true // Boolean | Forces deletion of the `Catalog` and its `Association` resources. If the `Catalog` is still associated with other resources and force is not set to true, then the operation fails.
};
apiInstance.cloudprivatecatalogproducerCatalogsProductsVersionsDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the version. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **force** | **Boolean**| Forces deletion of the &#x60;Catalog&#x60; and its &#x60;Association&#x60; resources. If the &#x60;Catalog&#x60; is still associated with other resources and force is not set to true, then the operation fails. | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsProductsVersionsGet

> GoogleCloudPrivatecatalogproducerV1beta1Version cloudprivatecatalogproducerCatalogsProductsVersionsGet(name, opts)



Returns the requested Version resource.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let name = "name_example"; // String | The resource name of the version.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example" // String | JSONP
};
apiInstance.cloudprivatecatalogproducerCatalogsProductsVersionsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the version. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 

### Return type

[**GoogleCloudPrivatecatalogproducerV1beta1Version**](GoogleCloudPrivatecatalogproducerV1beta1Version.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsProductsVersionsList

> GoogleCloudPrivatecatalogproducerV1beta1ListVersionsResponse cloudprivatecatalogproducerCatalogsProductsVersionsList(parent, opts)



Lists Version resources that the producer has access to, within the scope of the parent Product.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let parent = "parent_example"; // String | The resource name of the parent resource.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'pageSize': 56, // Number | The maximum number of versions to return.
  'pageToken': "pageToken_example" // String | A pagination token returned from a previous call to ListVersions that indicates where this listing should continue from. This field is optional.
};
apiInstance.cloudprivatecatalogproducerCatalogsProductsVersionsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the parent resource. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **pageSize** | **Number**| The maximum number of versions to return. | [optional] 
 **pageToken** | **String**| A pagination token returned from a previous call to ListVersions that indicates where this listing should continue from. This field is optional. | [optional] 

### Return type

[**GoogleCloudPrivatecatalogproducerV1beta1ListVersionsResponse**](GoogleCloudPrivatecatalogproducerV1beta1ListVersionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsProductsVersionsPatch

> GoogleCloudPrivatecatalogproducerV1beta1Version cloudprivatecatalogproducerCatalogsProductsVersionsPatch(name, opts)



Updates a specific Version resource.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let name = "name_example"; // String | Required. The resource name of the version, in the format `catalogs/{catalog_id}/products/{product_id}/versions/a-z*[a-z0-9]'.  A unique identifier for the version under a product, which can't be changed after the version is created. The final segment of the name must between 1 and 63 characters in length.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'updateMask': "updateMask_example", // String | Field mask that controls which fields of the version should be updated.
  'googleCloudPrivatecatalogproducerV1beta1Version': new CloudPrivateCatalogProducer.GoogleCloudPrivatecatalogproducerV1beta1Version() // GoogleCloudPrivatecatalogproducerV1beta1Version | 
};
apiInstance.cloudprivatecatalogproducerCatalogsProductsVersionsPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The resource name of the version, in the format &#x60;catalogs/{catalog_id}/products/{product_id}/versions/a-z*[a-z0-9]&#39;.  A unique identifier for the version under a product, which can&#39;t be changed after the version is created. The final segment of the name must between 1 and 63 characters in length. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **updateMask** | **String**| Field mask that controls which fields of the version should be updated. | [optional] 
 **googleCloudPrivatecatalogproducerV1beta1Version** | [**GoogleCloudPrivatecatalogproducerV1beta1Version**](GoogleCloudPrivatecatalogproducerV1beta1Version.md)|  | [optional] 

### Return type

[**GoogleCloudPrivatecatalogproducerV1beta1Version**](GoogleCloudPrivatecatalogproducerV1beta1Version.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsSetIamPolicy

> GoogleIamV1Policy cloudprivatecatalogproducerCatalogsSetIamPolicy(resource, opts)



Sets the IAM policy for the specified Catalog.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'googleIamV1SetIamPolicyRequest': new CloudPrivateCatalogProducer.GoogleIamV1SetIamPolicyRequest() // GoogleIamV1SetIamPolicyRequest | 
};
apiInstance.cloudprivatecatalogproducerCatalogsSetIamPolicy(resource, opts, (error, data, response) => {
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
 **resource** | **String**| REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **googleIamV1SetIamPolicyRequest** | [**GoogleIamV1SetIamPolicyRequest**](GoogleIamV1SetIamPolicyRequest.md)|  | [optional] 

### Return type

[**GoogleIamV1Policy**](GoogleIamV1Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsTestIamPermissions

> GoogleIamV1TestIamPermissionsResponse cloudprivatecatalogproducerCatalogsTestIamPermissions(resource, opts)



Tests the IAM permissions for the specified Catalog.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'googleIamV1TestIamPermissionsRequest': new CloudPrivateCatalogProducer.GoogleIamV1TestIamPermissionsRequest() // GoogleIamV1TestIamPermissionsRequest | 
};
apiInstance.cloudprivatecatalogproducerCatalogsTestIamPermissions(resource, opts, (error, data, response) => {
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
 **resource** | **String**| REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **googleIamV1TestIamPermissionsRequest** | [**GoogleIamV1TestIamPermissionsRequest**](GoogleIamV1TestIamPermissionsRequest.md)|  | [optional] 

### Return type

[**GoogleIamV1TestIamPermissionsResponse**](GoogleIamV1TestIamPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## cloudprivatecatalogproducerCatalogsUndelete

> GoogleCloudPrivatecatalogproducerV1beta1Catalog cloudprivatecatalogproducerCatalogsUndelete(name, opts)



Undeletes a deleted Catalog and all resources under it.

### Example

```javascript
import CloudPrivateCatalogProducer from 'cloud_private_catalog_producer';
let defaultClient = CloudPrivateCatalogProducer.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudPrivateCatalogProducer.CatalogsApi();
let name = "name_example"; // String | The resource name of the catalog.
let opts = {
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'body': {key: null} // Object | 
};
apiInstance.cloudprivatecatalogproducerCatalogsUndelete(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the catalog. | 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **body** | **Object**|  | [optional] 

### Return type

[**GoogleCloudPrivatecatalogproducerV1beta1Catalog**](GoogleCloudPrivatecatalogproducerV1beta1Catalog.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

