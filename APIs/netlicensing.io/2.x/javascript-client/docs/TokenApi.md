# Labs64NetLicensingResTfulApiTestCenter.TokenApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createToken**](TokenApi.md#createToken) | **POST** /token | Create token
[**deleteToken**](TokenApi.md#deleteToken) | **DELETE** /token/{tokenNumber} | Delete token
[**getToken**](TokenApi.md#getToken) | **GET** /token/{tokenNumber} | Get token
[**listTokens**](TokenApi.md#listTokens) | **GET** /token | List Tokens



## createToken

> Netlicensing createToken(tokenType, opts)

Create token

Create token by &#39;tokenType&#39; and additional token parameters

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.TokenApi();
let tokenType = "tokenType_example"; // String | Token type to be generated
let opts = {
  'action': "action_example", // String | For <i>type=ACTION</i> only; defines token action to be perfromed
  'apiKeyRole': "apiKeyRole_example", // String | For <i>tokenType=APIKEY</i> only (default: ROLE_APIKEY_LICENSEE); defines token RoleID
  'cancelURL': "cancelURL_example", // String | For <i>tokenType=SHOP</i> only; take customers to this URL when they cancel their checkout
  'cancelURLTitle': "cancelURLTitle_example", // String | For <i>tokenType=SHOP</i> only; shop link title for cancel checkout process
  'licenseTemplateNumber': "licenseTemplateNumber_example", // String | For <i>tokenType=SHOP</i> only; identifies LicenseTemplate that will be assigned to the shop token
  'licenseeNumber': "licenseeNumber_example", // String | For <i>tokenType=SHOP</i> or <i>type=ACTION</i> only (mandatory); identifies Licensee that will be assigned to the shop token
  'predefinedShoppingItem': "predefinedShoppingItem_example", // String | For <i>tokenType=SHOP</i> only; identifies Shopping Item name that will be shown to the customer
  'privateKey': "privateKey_example", // String | For <i>tokenType=APIKEY</i> only (optional); defines PrivateKey to be used with the validate method<br/><strong>Please Note:</strong> PrivateKey need to be provided as one line without spaces
  'productNumber': "productNumber_example", // String | For <i>tokenType=SHOP</i> only (mandatory); identifies Product that will be assigned to the shop token
  'successURL': "successURL_example", // String | For <i>tokenType=SHOP</i> only; take customers to this URL when they finish checkout
  'successURLTitle': "successURLTitle_example", // String | For <i>tokenType=SHOP</i> only; shop link title for successful checkout process
  'type': "type_example" // String | For <i>tokenType=DEFAULT</i> only; action type to be set
};
apiInstance.createToken(tokenType, opts, (error, data, response) => {
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
 **tokenType** | **String**| Token type to be generated | 
 **action** | **String**| For &lt;i&gt;type&#x3D;ACTION&lt;/i&gt; only; defines token action to be perfromed | [optional] 
 **apiKeyRole** | **String**| For &lt;i&gt;tokenType&#x3D;APIKEY&lt;/i&gt; only (default: ROLE_APIKEY_LICENSEE); defines token RoleID | [optional] 
 **cancelURL** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; take customers to this URL when they cancel their checkout | [optional] 
 **cancelURLTitle** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; shop link title for cancel checkout process | [optional] 
 **licenseTemplateNumber** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; identifies LicenseTemplate that will be assigned to the shop token | [optional] 
 **licenseeNumber** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; or &lt;i&gt;type&#x3D;ACTION&lt;/i&gt; only (mandatory); identifies Licensee that will be assigned to the shop token | [optional] 
 **predefinedShoppingItem** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; identifies Shopping Item name that will be shown to the customer | [optional] 
 **privateKey** | **String**| For &lt;i&gt;tokenType&#x3D;APIKEY&lt;/i&gt; only (optional); defines PrivateKey to be used with the validate method&lt;br/&gt;&lt;strong&gt;Please Note:&lt;/strong&gt; PrivateKey need to be provided as one line without spaces | [optional] 
 **productNumber** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only (mandatory); identifies Product that will be assigned to the shop token | [optional] 
 **successURL** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; take customers to this URL when they finish checkout | [optional] 
 **successURLTitle** | **String**| For &lt;i&gt;tokenType&#x3D;SHOP&lt;/i&gt; only; shop link title for successful checkout process | [optional] 
 **type** | **String**| For &lt;i&gt;tokenType&#x3D;DEFAULT&lt;/i&gt; only; action type to be set | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## deleteToken

> Netlicensing deleteToken(tokenNumber)

Delete token

Delete a token by &#39;number&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.TokenApi();
let tokenNumber = "tokenNumber_example"; // String | Token number
apiInstance.deleteToken(tokenNumber, (error, data, response) => {
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
 **tokenNumber** | **String**| Token number | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getToken

> Netlicensing getToken(tokenNumber)

Get token

Return a token by &#39;tokenNumber&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.TokenApi();
let tokenNumber = "tokenNumber_example"; // String | Token number
apiInstance.getToken(tokenNumber, (error, data, response) => {
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
 **tokenNumber** | **String**| Token number | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listTokens

> [Netlicensing] listTokens()

List Tokens

Return a list of all tokens for the current Vendor

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.TokenApi();
apiInstance.listTokens((error, data, response) => {
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

[**[Netlicensing]**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

