# BillbeeApi.ProvisioningApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**automaticProvisioningCreateAccount**](ProvisioningApi.md#automaticProvisioningCreateAccount) | **POST** /api/v1/automaticprovision/createaccount | Creates a new Billbee user account with the data passed
[**automaticProvisioningTermsInfo**](ProvisioningApi.md#automaticProvisioningTermsInfo) | **GET** /api/v1/automaticprovision/termsinfo | Returns infos about Billbee terms and conditions



## automaticProvisioningCreateAccount

> Object automaticProvisioningCreateAccount(rechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer)

Creates a new Billbee user account with the data passed

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProvisioningApi();
let rechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer = new BillbeeApi.RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer(); // RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer | 
apiInstance.automaticProvisioningCreateAccount(rechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer, (error, data, response) => {
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
 **rechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer** | [**RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer**](RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, text/json


## automaticProvisioningTermsInfo

> Object automaticProvisioningTermsInfo()

Returns infos about Billbee terms and conditions

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProvisioningApi();
apiInstance.automaticProvisioningTermsInfo((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

