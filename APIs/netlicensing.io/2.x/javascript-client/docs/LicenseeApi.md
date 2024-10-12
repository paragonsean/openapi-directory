# Labs64NetLicensingResTfulApiTestCenter.LicenseeApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLicensee**](LicenseeApi.md#createLicensee) | **POST** /licensee | Create Licensee
[**deleteLicensee**](LicenseeApi.md#deleteLicensee) | **DELETE** /licensee/{licenseeNumber} | Delete Licensee
[**getLicensee**](LicenseeApi.md#getLicensee) | **GET** /licensee/{licenseeNumber} | Get Licensee
[**listLicensees**](LicenseeApi.md#listLicensees) | **GET** /licensee | List Licensees
[**transferLicenses**](LicenseeApi.md#transferLicenses) | **POST** /licensee/{licenseeNumber}/transfer | Transfer Licenses
[**updateLicensee**](LicenseeApi.md#updateLicensee) | **POST** /licensee/{licenseeNumber} | Update Licensee
[**validateLicensee**](LicenseeApi.md#validateLicensee) | **POST** /licensee/{licenseeNumber}/validate | Validate Licensee



## createLicensee

> Netlicensing createLicensee(active, productNumber, opts)

Create Licensee

Creates a new Licensee

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseeApi();
let active = true; // Boolean | If set to 'false', the Licensee is disabled. Licensee can not obtain new Licenses, and validation is disabled
let productNumber = "productNumber_example"; // String | 'productNumber' to assign new Licensee object
let opts = {
  'markedForTransfer': true, // Boolean | Mark Licensee for transfer.
  'name': "name_example", // String | 
  'number': "number_example" // String | Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee
};
apiInstance.createLicensee(active, productNumber, opts, (error, data, response) => {
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
 **active** | **Boolean**| If set to &#39;false&#39;, the Licensee is disabled. Licensee can not obtain new Licenses, and validation is disabled | 
 **productNumber** | **String**| &#39;productNumber&#39; to assign new Licensee object | 
 **markedForTransfer** | **Boolean**| Mark Licensee for transfer. | [optional] 
 **name** | **String**|  | [optional] 
 **number** | **String**| Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## deleteLicensee

> Netlicensing deleteLicensee(licenseeNumber, opts)

Delete Licensee

Delete a Licensee by &#39;number&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseeApi();
let licenseeNumber = "licenseeNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Licensee.
let opts = {
  'forceCascade': true // Boolean | Force object deletion and all descendants.
};
apiInstance.deleteLicensee(licenseeNumber, opts, (error, data, response) => {
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
 **licenseeNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Licensee. | 
 **forceCascade** | **Boolean**| Force object deletion and all descendants. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getLicensee

> Netlicensing getLicensee(licenseeNumber)

Get Licensee

Return a Licensee by &#39;licenseeNumber&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseeApi();
let licenseeNumber = "licenseeNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee.
apiInstance.getLicensee(licenseeNumber, (error, data, response) => {
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
 **licenseeNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee. | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listLicensees

> [Netlicensing] listLicensees()

List Licensees

Return a list of all Licensees for the current Vendor

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseeApi();
apiInstance.listLicensees((error, data, response) => {
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


## transferLicenses

> Netlicensing transferLicenses(licenseeNumber, sourceLicenseeNumber)

Transfer Licenses

Licenses transfer between Licensees

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseeApi();
let licenseeNumber = "licenseeNumber_example"; // String | Licensee number with a maximum length of 1000 characters
let sourceLicenseeNumber = "sourceLicenseeNumber_example"; // String | Licensee number which Licenses to be transferred
apiInstance.transferLicenses(licenseeNumber, sourceLicenseeNumber, (error, data, response) => {
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
 **licenseeNumber** | **String**| Licensee number with a maximum length of 1000 characters | 
 **sourceLicenseeNumber** | **String**| Licensee number which Licenses to be transferred | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## updateLicensee

> Netlicensing updateLicensee(licenseeNumber, opts)

Update Licensee

Sets the provided properties to a Licensee. Return an updated Licensee

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseeApi();
let licenseeNumber = "licenseeNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee.
let opts = {
  'active': true, // Boolean | If set to 'false', the Licensee is disabled. Licensee can not obtain new Licenses, and validation is disabled
  'markedForTransfer': true, // Boolean | Mark Licensee for transfer.
  'name': "name_example", // String | 
  'number': "number_example" // String | New Licensee number (update).
};
apiInstance.updateLicensee(licenseeNumber, opts, (error, data, response) => {
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
 **licenseeNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Licensee. Vendor can assign this number when creating a Licensee or let NetLicensing generate one. Read-only after creation of the first License for the Licensee. | 
 **active** | **Boolean**| If set to &#39;false&#39;, the Licensee is disabled. Licensee can not obtain new Licenses, and validation is disabled | [optional] 
 **markedForTransfer** | **Boolean**| Mark Licensee for transfer. | [optional] 
 **name** | **String**|  | [optional] 
 **number** | **String**| New Licensee number (update). | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## validateLicensee

> Netlicensing validateLicensee(licenseeNumber, opts)

Validate Licensee

Validates active Licenses of the Licensee

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseeApi();
let licenseeNumber = "licenseeNumber_example"; // String | Licensee number with a maximum length of 1000 characters
let opts = {
  'action': "action_example", // String | 'Floating' licensing model: check-out or check-in session action, to allocate or return it from/to the pool of available sessions
  'licenseeName': "licenseeName_example", // String | Human-readable name for the auto-created Licensee (will be set as custom Licensee property)
  'nodeSecret': "nodeSecret_example", // String | 'Node-Locked' licensing model: specifies unique secret
  'productModuleNumber': "productModuleNumber_example", // String | 'Node-Locked' licensing model: product module number
  'productNumber': "productNumber_example", // String | Product number, must be provided when 'Licensee auto-create' is enabled (see also Product JavaDoc). Identifies the Product to which new Licensee should be added
  'sessionId': "sessionId_example" // String | 'Floating' licensing model: specifies unique session identifier
};
apiInstance.validateLicensee(licenseeNumber, opts, (error, data, response) => {
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
 **licenseeNumber** | **String**| Licensee number with a maximum length of 1000 characters | 
 **action** | **String**| &#39;Floating&#39; licensing model: check-out or check-in session action, to allocate or return it from/to the pool of available sessions | [optional] 
 **licenseeName** | **String**| Human-readable name for the auto-created Licensee (will be set as custom Licensee property) | [optional] 
 **nodeSecret** | **String**| &#39;Node-Locked&#39; licensing model: specifies unique secret | [optional] 
 **productModuleNumber** | **String**| &#39;Node-Locked&#39; licensing model: product module number | [optional] 
 **productNumber** | **String**| Product number, must be provided when &#39;Licensee auto-create&#39; is enabled (see also Product JavaDoc). Identifies the Product to which new Licensee should be added | [optional] 
 **sessionId** | **String**| &#39;Floating&#39; licensing model: specifies unique session identifier | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

