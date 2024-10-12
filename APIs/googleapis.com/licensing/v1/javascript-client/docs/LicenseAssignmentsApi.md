# EnterpriseLicenseManagerApi.LicenseAssignmentsApi

All URIs are relative to *https://licensing.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licensingLicenseAssignmentsDelete**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsDelete) | **DELETE** /apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId} | 
[**licensingLicenseAssignmentsGet**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsGet) | **GET** /apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId} | 
[**licensingLicenseAssignmentsInsert**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsInsert) | **POST** /apps/licensing/v1/product/{productId}/sku/{skuId}/user | 
[**licensingLicenseAssignmentsListForProduct**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsListForProduct) | **GET** /apps/licensing/v1/product/{productId}/users | 
[**licensingLicenseAssignmentsListForProductAndSku**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsListForProductAndSku) | **GET** /apps/licensing/v1/product/{productId}/sku/{skuId}/users | 
[**licensingLicenseAssignmentsPatch**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsPatch) | **PATCH** /apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId} | 
[**licensingLicenseAssignmentsUpdate**](LicenseAssignmentsApi.md#licensingLicenseAssignmentsUpdate) | **PUT** /apps/licensing/v1/product/{productId}/sku/{skuId}/user/{userId} | 



## licensingLicenseAssignmentsDelete

> Object licensingLicenseAssignmentsDelete(productId, skuId, userId, opts)



Revoke a license.

### Example

```javascript
import EnterpriseLicenseManagerApi from 'enterprise_license_manager_api';
let defaultClient = EnterpriseLicenseManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnterpriseLicenseManagerApi.LicenseAssignmentsApi();
let productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
let skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
let userId = "userId_example"; // String | The user's current primary email address. If the user's email address changes, use the new email address in your API requests. Since a `userId` is subject to change, do not use a `userId` value as a key for persistent data. This key could break if the current user's email address changes. If the `userId` is suspended, the license status changes.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.licensingLicenseAssignmentsDelete(productId, skuId, userId, opts, (error, data, response) => {
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
 **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | 
 **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | 
 **userId** | **String**| The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licensingLicenseAssignmentsGet

> LicenseAssignment licensingLicenseAssignmentsGet(productId, skuId, userId, opts)



Get a specific user&#39;s license by product SKU.

### Example

```javascript
import EnterpriseLicenseManagerApi from 'enterprise_license_manager_api';
let defaultClient = EnterpriseLicenseManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnterpriseLicenseManagerApi.LicenseAssignmentsApi();
let productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
let skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
let userId = "userId_example"; // String | The user's current primary email address. If the user's email address changes, use the new email address in your API requests. Since a `userId` is subject to change, do not use a `userId` value as a key for persistent data. This key could break if the current user's email address changes. If the `userId` is suspended, the license status changes.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.licensingLicenseAssignmentsGet(productId, skuId, userId, opts, (error, data, response) => {
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
 **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | 
 **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | 
 **userId** | **String**| The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**LicenseAssignment**](LicenseAssignment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licensingLicenseAssignmentsInsert

> LicenseAssignment licensingLicenseAssignmentsInsert(productId, skuId, opts)



Assign a license.

### Example

```javascript
import EnterpriseLicenseManagerApi from 'enterprise_license_manager_api';
let defaultClient = EnterpriseLicenseManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnterpriseLicenseManagerApi.LicenseAssignmentsApi();
let productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
let skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'licenseAssignmentInsert': new EnterpriseLicenseManagerApi.LicenseAssignmentInsert() // LicenseAssignmentInsert | 
};
apiInstance.licensingLicenseAssignmentsInsert(productId, skuId, opts, (error, data, response) => {
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
 **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | 
 **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **licenseAssignmentInsert** | [**LicenseAssignmentInsert**](LicenseAssignmentInsert.md)|  | [optional] 

### Return type

[**LicenseAssignment**](LicenseAssignment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## licensingLicenseAssignmentsListForProduct

> LicenseAssignmentList licensingLicenseAssignmentsListForProduct(productId, customerId, opts)



List all users assigned licenses for a specific product SKU.

### Example

```javascript
import EnterpriseLicenseManagerApi from 'enterprise_license_manager_api';
let defaultClient = EnterpriseLicenseManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnterpriseLicenseManagerApi.LicenseAssignmentsApi();
let productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
let customerId = "customerId_example"; // String | The customer's unique ID as defined in the Admin console, such as `C00000000`. If the customer is suspended, the server returns an error.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'maxResults': 56, // Number | The `maxResults` query string determines how many entries are returned on each page of a large response. This is an optional parameter. The value must be a positive number.
  'pageToken': "pageToken_example" // String | Token to fetch the next page of data. The `maxResults` query string is related to the `pageToken` since `maxResults` determines how many entries are returned on each page. This is an optional query string. If not specified, the server returns the first page.
};
apiInstance.licensingLicenseAssignmentsListForProduct(productId, customerId, opts, (error, data, response) => {
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
 **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | 
 **customerId** | **String**| The customer&#39;s unique ID as defined in the Admin console, such as &#x60;C00000000&#x60;. If the customer is suspended, the server returns an error. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **maxResults** | **Number**| The &#x60;maxResults&#x60; query string determines how many entries are returned on each page of a large response. This is an optional parameter. The value must be a positive number. | [optional] 
 **pageToken** | **String**| Token to fetch the next page of data. The &#x60;maxResults&#x60; query string is related to the &#x60;pageToken&#x60; since &#x60;maxResults&#x60; determines how many entries are returned on each page. This is an optional query string. If not specified, the server returns the first page. | [optional] 

### Return type

[**LicenseAssignmentList**](LicenseAssignmentList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licensingLicenseAssignmentsListForProductAndSku

> LicenseAssignmentList licensingLicenseAssignmentsListForProductAndSku(productId, skuId, customerId, opts)



List all users assigned licenses for a specific product SKU.

### Example

```javascript
import EnterpriseLicenseManagerApi from 'enterprise_license_manager_api';
let defaultClient = EnterpriseLicenseManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnterpriseLicenseManagerApi.LicenseAssignmentsApi();
let productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
let skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
let customerId = "customerId_example"; // String | The customer's unique ID as defined in the Admin console, such as `C00000000`. If the customer is suspended, the server returns an error.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'maxResults': 56, // Number | The `maxResults` query string determines how many entries are returned on each page of a large response. This is an optional parameter. The value must be a positive number.
  'pageToken': "pageToken_example" // String | Token to fetch the next page of data. The `maxResults` query string is related to the `pageToken` since `maxResults` determines how many entries are returned on each page. This is an optional query string. If not specified, the server returns the first page.
};
apiInstance.licensingLicenseAssignmentsListForProductAndSku(productId, skuId, customerId, opts, (error, data, response) => {
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
 **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | 
 **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | 
 **customerId** | **String**| The customer&#39;s unique ID as defined in the Admin console, such as &#x60;C00000000&#x60;. If the customer is suspended, the server returns an error. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **maxResults** | **Number**| The &#x60;maxResults&#x60; query string determines how many entries are returned on each page of a large response. This is an optional parameter. The value must be a positive number. | [optional] 
 **pageToken** | **String**| Token to fetch the next page of data. The &#x60;maxResults&#x60; query string is related to the &#x60;pageToken&#x60; since &#x60;maxResults&#x60; determines how many entries are returned on each page. This is an optional query string. If not specified, the server returns the first page. | [optional] 

### Return type

[**LicenseAssignmentList**](LicenseAssignmentList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## licensingLicenseAssignmentsPatch

> LicenseAssignment licensingLicenseAssignmentsPatch(productId, skuId, userId, opts)



Reassign a user&#39;s product SKU with a different SKU in the same product. This method supports patch semantics.

### Example

```javascript
import EnterpriseLicenseManagerApi from 'enterprise_license_manager_api';
let defaultClient = EnterpriseLicenseManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnterpriseLicenseManagerApi.LicenseAssignmentsApi();
let productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
let skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
let userId = "userId_example"; // String | The user's current primary email address. If the user's email address changes, use the new email address in your API requests. Since a `userId` is subject to change, do not use a `userId` value as a key for persistent data. This key could break if the current user's email address changes. If the `userId` is suspended, the license status changes.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'licenseAssignment': new EnterpriseLicenseManagerApi.LicenseAssignment() // LicenseAssignment | 
};
apiInstance.licensingLicenseAssignmentsPatch(productId, skuId, userId, opts, (error, data, response) => {
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
 **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | 
 **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | 
 **userId** | **String**| The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **licenseAssignment** | [**LicenseAssignment**](LicenseAssignment.md)|  | [optional] 

### Return type

[**LicenseAssignment**](LicenseAssignment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## licensingLicenseAssignmentsUpdate

> LicenseAssignment licensingLicenseAssignmentsUpdate(productId, skuId, userId, opts)



Reassign a user&#39;s product SKU with a different SKU in the same product.

### Example

```javascript
import EnterpriseLicenseManagerApi from 'enterprise_license_manager_api';
let defaultClient = EnterpriseLicenseManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnterpriseLicenseManagerApi.LicenseAssignmentsApi();
let productId = "productId_example"; // String | A product's unique identifier. For more information about products in this version of the API, see Products and SKUs.
let skuId = "skuId_example"; // String | A product SKU's unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs.
let userId = "userId_example"; // String | The user's current primary email address. If the user's email address changes, use the new email address in your API requests. Since a `userId` is subject to change, do not use a `userId` value as a key for persistent data. This key could break if the current user's email address changes. If the `userId` is suspended, the license status changes.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'licenseAssignment': new EnterpriseLicenseManagerApi.LicenseAssignment() // LicenseAssignment | 
};
apiInstance.licensingLicenseAssignmentsUpdate(productId, skuId, userId, opts, (error, data, response) => {
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
 **productId** | **String**| A product&#39;s unique identifier. For more information about products in this version of the API, see Products and SKUs. | 
 **skuId** | **String**| A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. | 
 **userId** | **String**| The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **licenseAssignment** | [**LicenseAssignment**](LicenseAssignment.md)|  | [optional] 

### Return type

[**LicenseAssignment**](LicenseAssignment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

