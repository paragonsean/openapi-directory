# Labs64NetLicensingResTfulApiTestCenter.LicenseTemplateApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createLicenseTemplate**](LicenseTemplateApi.md#createLicenseTemplate) | **POST** /licensetemplate | Create License Template
[**deleteLicenseTemplate**](LicenseTemplateApi.md#deleteLicenseTemplate) | **DELETE** /licensetemplate/{licenseTemplateNumber} | Delete License Template
[**getLicenseTemplate**](LicenseTemplateApi.md#getLicenseTemplate) | **GET** /licensetemplate/{licenseTemplateNumber} | Get License Template
[**listLicenseTemplates**](LicenseTemplateApi.md#listLicenseTemplates) | **GET** /licensetemplate | List License Templates
[**updateLicenseTemplate**](LicenseTemplateApi.md#updateLicenseTemplate) | **POST** /licensetemplate/{licenseTemplateNumber} | Update License Template



## createLicenseTemplate

> Netlicensing createLicenseTemplate(active, licenseType, name, productModuleNumber, opts)

Create License Template

Creates a new License Template

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseTemplateApi();
let active = true; // Boolean | If set to 'false', the License Template is disabled. Licensee can not obtain any new Licenses off this License Template.
let licenseType = "licenseType_example"; // String | Type of Licenses created from this License Template. Supported types: FEATURE, TIMEVOLUME, FLOATING, QUANTITY
let name = "name_example"; // String | License Template name to create License Template object
let productModuleNumber = "productModuleNumber_example"; // String | Number of Product Module to create License Template object
let opts = {
  'automatic': true, // Boolean | If set to 'true', every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0.
  'currency': "currency_example", // String | Specifies currency for the License price. Check data types to discover which currencies are supported.
  'hidden': true, // Boolean | If set to 'true', this License Template is not shown in NetLicensing Shop as offered for purchase.
  'hideLicenses': true, // Boolean | If set to 'true', Licenses from this License Template are not visible to the end customer, but participate in validation.
  'maxSessions': "maxSessions_example", // String | Mandatory for 'FLOATING' License Type.
  'number': "number_example", // String | Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template.
  'price': 3.4, // Number | Price for the License. If >0, it must always be accompanied by the currency specification.
  'quantity': "quantity_example", // String | Mandatory for 'Pay-per-Use' and 'Node-Locked' License Model.
  'quota': "quota_example", // String | Mandatory for 'Quota' License Model.
  'timeVolume': "timeVolume_example", // String | Mandatory for 'TIMEVOLUME' License Type.
  'timeVolumePeriod': "timeVolumePeriod_example" // String | For 'TIMEVOLUME' License Type.
};
apiInstance.createLicenseTemplate(active, licenseType, name, productModuleNumber, opts, (error, data, response) => {
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
 **active** | **Boolean**| If set to &#39;false&#39;, the License Template is disabled. Licensee can not obtain any new Licenses off this License Template. | 
 **licenseType** | **String**| Type of Licenses created from this License Template. Supported types: FEATURE, TIMEVOLUME, FLOATING, QUANTITY | 
 **name** | **String**| License Template name to create License Template object | 
 **productModuleNumber** | **String**| Number of Product Module to create License Template object | 
 **automatic** | **Boolean**| If set to &#39;true&#39;, every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0. | [optional] 
 **currency** | **String**| Specifies currency for the License price. Check data types to discover which currencies are supported. | [optional] 
 **hidden** | **Boolean**| If set to &#39;true&#39;, this License Template is not shown in NetLicensing Shop as offered for purchase. | [optional] 
 **hideLicenses** | **Boolean**| If set to &#39;true&#39;, Licenses from this License Template are not visible to the end customer, but participate in validation. | [optional] 
 **maxSessions** | **String**| Mandatory for &#39;FLOATING&#39; License Type. | [optional] 
 **number** | **String**| Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template. | [optional] 
 **price** | **Number**| Price for the License. If &gt;0, it must always be accompanied by the currency specification. | [optional] 
 **quantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; and &#39;Node-Locked&#39; License Model. | [optional] 
 **quota** | **String**| Mandatory for &#39;Quota&#39; License Model. | [optional] 
 **timeVolume** | **String**| Mandatory for &#39;TIMEVOLUME&#39; License Type. | [optional] 
 **timeVolumePeriod** | **String**| For &#39;TIMEVOLUME&#39; License Type. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## deleteLicenseTemplate

> Netlicensing deleteLicenseTemplate(licenseTemplateNumber, opts)

Delete License Template

Delete a License Template by &#39;number&#39;.

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseTemplateApi();
let licenseTemplateNumber = "licenseTemplateNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the License Template.
let opts = {
  'forceCascade': true // Boolean | Force object deletion and all descendants.
};
apiInstance.deleteLicenseTemplate(licenseTemplateNumber, opts, (error, data, response) => {
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
 **licenseTemplateNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the License Template. | 
 **forceCascade** | **Boolean**| Force object deletion and all descendants. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getLicenseTemplate

> Netlicensing getLicenseTemplate(licenseTemplateNumber)

Get License Template

Return a License Template by &#39;licenseTemplateNumber&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseTemplateApi();
let licenseTemplateNumber = "licenseTemplateNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template.
apiInstance.getLicenseTemplate(licenseTemplateNumber, (error, data, response) => {
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
 **licenseTemplateNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template. | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listLicenseTemplates

> [Netlicensing] listLicenseTemplates()

List License Templates

Return a list of all License Templates for the current Vendor

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseTemplateApi();
apiInstance.listLicenseTemplates((error, data, response) => {
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


## updateLicenseTemplate

> Netlicensing updateLicenseTemplate(licenseTemplateNumber, opts)

Update License Template

Sets the provided properties to a License Template. Return an updated License Template

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.LicenseTemplateApi();
let licenseTemplateNumber = "licenseTemplateNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template.
let opts = {
  'active': true, // Boolean | If set to 'false', the License Template is disabled. Licensee can not obtain any new Licenses off this License Template.
  'automatic': true, // Boolean | If set to 'true', every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0.
  'currency': "currency_example", // String | Specifies currency for the License price. Check data types to discover which currencies are supported.
  'hidden': true, // Boolean | If set to 'true', this License Template is not shown in NetLicensing Shop as offered for purchase.
  'hideLicenses': true, // Boolean | If set to 'true', Licenses from this License Template are not visible to the end customer, but participate in validation.
  'licenseType': "licenseType_example", // String | Type of Licenses created from this License Template. Supported types: FEATURE, TIMEVOLUME, FLOATING, QUANTITY
  'maxSessions': "maxSessions_example", // String | Mandatory for 'FLOATING' License Type.
  'name': "name_example", // String | Name for the Licensed item
  'number': "number_example", // String | New License Template number (update).
  'price': 3.4, // Number | Price for the License. If >0, it must always be accompanied by the currency specification.
  'quantity': "quantity_example", // String | Mandatory for 'Pay-per-Use' and 'Node-Locked' License Model.
  'quota': "quota_example", // String | Mandatory for 'Quota' License Model.
  'timeVolume': "timeVolume_example", // String | Mandatory for 'TIMEVOLUME' License Type.
  'timeVolumePeriod': "timeVolumePeriod_example" // String | For 'TIMEVOLUME' License Type.
};
apiInstance.updateLicenseTemplate(licenseTemplateNumber, opts, (error, data, response) => {
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
 **licenseTemplateNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template. | 
 **active** | **Boolean**| If set to &#39;false&#39;, the License Template is disabled. Licensee can not obtain any new Licenses off this License Template. | [optional] 
 **automatic** | **Boolean**| If set to &#39;true&#39;, every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0. | [optional] 
 **currency** | **String**| Specifies currency for the License price. Check data types to discover which currencies are supported. | [optional] 
 **hidden** | **Boolean**| If set to &#39;true&#39;, this License Template is not shown in NetLicensing Shop as offered for purchase. | [optional] 
 **hideLicenses** | **Boolean**| If set to &#39;true&#39;, Licenses from this License Template are not visible to the end customer, but participate in validation. | [optional] 
 **licenseType** | **String**| Type of Licenses created from this License Template. Supported types: FEATURE, TIMEVOLUME, FLOATING, QUANTITY | [optional] 
 **maxSessions** | **String**| Mandatory for &#39;FLOATING&#39; License Type. | [optional] 
 **name** | **String**| Name for the Licensed item | [optional] 
 **number** | **String**| New License Template number (update). | [optional] 
 **price** | **Number**| Price for the License. If &gt;0, it must always be accompanied by the currency specification. | [optional] 
 **quantity** | **String**| Mandatory for &#39;Pay-per-Use&#39; and &#39;Node-Locked&#39; License Model. | [optional] 
 **quota** | **String**| Mandatory for &#39;Quota&#39; License Model. | [optional] 
 **timeVolume** | **String**| Mandatory for &#39;TIMEVOLUME&#39; License Type. | [optional] 
 **timeVolumePeriod** | **String**| For &#39;TIMEVOLUME&#39; License Type. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

