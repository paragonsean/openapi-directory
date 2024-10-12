# Labs64NetLicensingResTfulApiTestCenter.LicenseApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLicense**](LicenseApi.md#createLicense) | **POST** /license | Create License
[**deleteLicense**](LicenseApi.md#deleteLicense) | **DELETE** /license/{licenseNumber} | Delete License
[**getLicense**](LicenseApi.md#getLicense) | **GET** /license/{licenseNumber} | Get License
[**listLicenses**](LicenseApi.md#listLicenses) | **GET** /license | List Licenses
[**updateLicense**](LicenseApi.md#updateLicense) | **POST** /license/{licenseNumber} | Update License



## createLicense

> Netlicensing createLicense(active, licenseTemplateNumber, licenseeNumber, opts)

Create License

Creates a new License

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseApi();
let active = true; // Boolean | 
let licenseTemplateNumber = "licenseTemplateNumber_example"; // String | 
let licenseeNumber = "licenseeNumber_example"; // String | 
let opts = {
  'currency': "currency_example", // String | Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation
  'hidden': true, // Boolean | If set to 'true', this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly
  'name': "name_example", // String | Name for the Licensed item. Set from License Template on creation, if not specified explicitly.
  'number': "number_example", // String | 
  'parentfeature': "parentfeature_example", // String | Mandatory for 'TIMEVOLUME' License Type and 'RENTAL' licensing model
  'price': 3.4, // Number | Price for the License. If >0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation
  'quantity': "quantity_example", // String | Mandatory for 'Pay-per-Use' License Model.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Mandatory for 'TIMEVOLUME' License Type.
  'timeVolume': "timeVolume_example", // String | Mandatory for 'TIMEVOLUME' License Type.
  'timeVolumePeriod': "timeVolumePeriod_example", // String | For 'TIMEVOLUME' License Type.
  'usedQuantity': "usedQuantity_example" // String | Mandatory for 'Pay-per-Use' License Model.
};
apiInstance.createLicense(active, licenseTemplateNumber, licenseeNumber, opts, (error, data, response) => {
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
 **active** | **Boolean**|  | 
 **licenseTemplateNumber** | **String**|  | 
 **licenseeNumber** | **String**|  | 
 **currency** | **String**| Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation | [optional] 
 **hidden** | **Boolean**| If set to &#39;true&#39;, this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly | [optional] 
 **name** | **String**| Name for the Licensed item. Set from License Template on creation, if not specified explicitly. | [optional] 
 **number** | **String**|  | [optional] 
 **parentfeature** | **String**| Mandatory for &#39;TIMEVOLUME&#39; License Type and &#39;RENTAL&#39; licensing model | [optional] 
 **price** | **Number**| Price for the License. If &gt;0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation | [optional] 
 **quantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; License Model. | [optional] 
 **startDate** | **Date**| Mandatory for &#39;TIMEVOLUME&#39; License Type. | [optional] 
 **timeVolume** | **String**| Mandatory for &#39;TIMEVOLUME&#39; License Type. | [optional] 
 **timeVolumePeriod** | **String**| For &#39;TIMEVOLUME&#39; License Type. | [optional] 
 **usedQuantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; License Model. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## deleteLicense

> Netlicensing deleteLicense(licenseNumber)

Delete License

Delete License by a &#39;licenseNumber&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseApi();
let licenseNumber = "licenseNumber_example"; // String | Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
apiInstance.deleteLicense(licenseNumber, (error, data, response) => {
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
 **licenseNumber** | **String**| Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed. | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getLicense

> Netlicensing getLicense(licenseNumber)

Get License

Get License by a &#39;licenseNumber&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseApi();
let licenseNumber = "licenseNumber_example"; // String | Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
apiInstance.getLicense(licenseNumber, (error, data, response) => {
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
 **licenseNumber** | **String**| Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed. | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listLicenses

> [Netlicensing] listLicenses()

List Licenses

Return a list of all Licenses for the current Vendor

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseApi();
apiInstance.listLicenses((error, data, response) => {
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


## updateLicense

> Netlicensing updateLicense(licenseNumber, opts)

Update License

Update License by a &#39;licenseNumber&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseApi();
let licenseNumber = "licenseNumber_example"; // String | Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
let opts = {
  'active': true, // Boolean | 
  'currency': "currency_example", // String | Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation
  'hidden': true, // Boolean | If set to 'true', this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly
  'name': "name_example", // String | Name for the Licensed item. Set from License Template on creation, if not specified explicitly.
  'number': "number_example", // String | Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed.
  'parentfeature': "parentfeature_example", // String | 
  'price': 3.4, // Number | Price for the License. If > 0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation
  'quantity': "quantity_example", // String | Mandatory for 'Pay-per-Use' License Model.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | For 'TIMEVOLUME' License type
  'timeVolume': "timeVolume_example", // String | Mandatory for 'TIMEVOLUME' License Type.
  'timeVolumePeriod': "timeVolumePeriod_example", // String | For 'TIMEVOLUME' License Type.
  'usedQuantity': "usedQuantity_example" // String | Mandatory for 'Pay-per-Use' License Model.
};
apiInstance.updateLicense(licenseNumber, opts, (error, data, response) => {
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
 **licenseNumber** | **String**| Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed. | 
 **active** | **Boolean**|  | [optional] 
 **currency** | **String**| Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation | [optional] 
 **hidden** | **Boolean**| If set to &#39;true&#39;, this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly | [optional] 
 **name** | **String**| Name for the Licensed item. Set from License Template on creation, if not specified explicitly. | [optional] 
 **number** | **String**| Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed. | [optional] 
 **parentfeature** | **String**|  | [optional] 
 **price** | **Number**| Price for the License. If &gt; 0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation | [optional] 
 **quantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; License Model. | [optional] 
 **startDate** | **Date**| For &#39;TIMEVOLUME&#39; License type | [optional] 
 **timeVolume** | **String**| Mandatory for &#39;TIMEVOLUME&#39; License Type. | [optional] 
 **timeVolumePeriod** | **String**| For &#39;TIMEVOLUME&#39; License Type. | [optional] 
 **usedQuantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; License Model. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

