# AgcoApi.LicenseActivationsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licenseActivationsPost**](LicenseActivationsApi.md#licenseActivationsPost) | **POST** /api/v2/LicenseActivations | Create a license activation.
[**licenseActivationsPostRegisterEDTLite**](LicenseActivationsApi.md#licenseActivationsPostRegisterEDTLite) | **POST** /api/v2/LicenseActivations/RegisterEDTLite | Register an EDT Lite with the Server
[**licenseActivationsPut**](LicenseActivationsApi.md#licenseActivationsPut) | **PUT** /api/v2/LicenseActivations/{ID} | Update a license activiation.
[**licenseActivationsPutConfirm**](LicenseActivationsApi.md#licenseActivationsPutConfirm) | **PUT** /api/v2/LicenseActivations/{ID}/Confirm | Confirm that the client has applied the updated license.



## licenseActivationsPost

> DealerDBModelsLicenseActivation licenseActivationsPost(dealerDBModelsLicenseActivationCreate)

Create a license activation.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LicenseActivationsApi();
let dealerDBModelsLicenseActivationCreate = new AgcoApi.DealerDBModelsLicenseActivationCreate(); // DealerDBModelsLicenseActivationCreate | The data required for creating the license.
apiInstance.licenseActivationsPost(dealerDBModelsLicenseActivationCreate, (error, data, response) => {
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
 **dealerDBModelsLicenseActivationCreate** | [**DealerDBModelsLicenseActivationCreate**](DealerDBModelsLicenseActivationCreate.md)| The data required for creating the license. | 

### Return type

[**DealerDBModelsLicenseActivation**](DealerDBModelsLicenseActivation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## licenseActivationsPostRegisterEDTLite

> Boolean licenseActivationsPostRegisterEDTLite(dealerDBModelsEDTLiteRegistration)

Register an EDT Lite with the Server

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LicenseActivationsApi();
let dealerDBModelsEDTLiteRegistration = new AgcoApi.DealerDBModelsEDTLiteRegistration(); // DealerDBModelsEDTLiteRegistration | The information required for registration.
apiInstance.licenseActivationsPostRegisterEDTLite(dealerDBModelsEDTLiteRegistration, (error, data, response) => {
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
 **dealerDBModelsEDTLiteRegistration** | [**DealerDBModelsEDTLiteRegistration**](DealerDBModelsEDTLiteRegistration.md)| The information required for registration. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## licenseActivationsPut

> DealerDBModelsLicenseActivation licenseActivationsPut(ID, dealerDBModelsLicenseActivationUpdate)

Update a license activiation.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LicenseActivationsApi();
let ID = "ID_example"; // String | The ID of the license.
let dealerDBModelsLicenseActivationUpdate = new AgcoApi.DealerDBModelsLicenseActivationUpdate(); // DealerDBModelsLicenseActivationUpdate | The data required for updating the license.
apiInstance.licenseActivationsPut(ID, dealerDBModelsLicenseActivationUpdate, (error, data, response) => {
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
 **ID** | **String**| The ID of the license. | 
 **dealerDBModelsLicenseActivationUpdate** | [**DealerDBModelsLicenseActivationUpdate**](DealerDBModelsLicenseActivationUpdate.md)| The data required for updating the license. | 

### Return type

[**DealerDBModelsLicenseActivation**](DealerDBModelsLicenseActivation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## licenseActivationsPutConfirm

> licenseActivationsPutConfirm(ID, dealerDBModelsLicenseActivationConfirm)

Confirm that the client has applied the updated license.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LicenseActivationsApi();
let ID = "ID_example"; // String | The ID of the license
let dealerDBModelsLicenseActivationConfirm = new AgcoApi.DealerDBModelsLicenseActivationConfirm(); // DealerDBModelsLicenseActivationConfirm | The license data.
apiInstance.licenseActivationsPutConfirm(ID, dealerDBModelsLicenseActivationConfirm, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ID** | **String**| The ID of the license | 
 **dealerDBModelsLicenseActivationConfirm** | [**DealerDBModelsLicenseActivationConfirm**](DealerDBModelsLicenseActivationConfirm.md)| The license data. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

