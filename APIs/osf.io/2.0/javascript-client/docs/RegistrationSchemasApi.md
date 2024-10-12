# OsfApiv2Documentation.RegistrationSchemasApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registrationSchemaRead**](RegistrationSchemasApi.md#registrationSchemaRead) | **GET** /schemas/registrations/{registration_schema_id} | Retrieve a Registration Schema
[**registrationSchemasList**](RegistrationSchemasApi.md#registrationSchemasList) | **GET** /schemas/registrations/ | Retrieve a list of Registration Schemas



## registrationSchemaRead

> RegistrationSchema registrationSchemaRead(registrationSchemaId)

Retrieve a Registration Schema

Retrieves the details of a given Registration Schema. Registration Schemas defines the desired supplemental information that should accompany be included in a Registration. Registration Schemas are Read-only to API users. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.RegistrationSchemasApi();
let registrationSchemaId = "registrationSchemaId_example"; // String | The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.
apiInstance.registrationSchemaRead(registrationSchemaId, (error, data, response) => {
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
 **registrationSchemaId** | **String**| The unique identifier of the Registration Schema example &#x60;6176c9d45e01f100091d4f94&#x60;. | 

### Return type

[**RegistrationSchema**](RegistrationSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## registrationSchemasList

> RegistrationSchema registrationSchemasList()

Retrieve a list of Registration Schemas

Retrieve a paginated list of all active Registration Schemas. Registration Schemas describe the supplemental questions that accompany a registration. Registration Schemas are read-only for API users. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;data&#x60; key contains an array of 10 Registration Schemas. Each resource in the array is a separate Registration Schemas object. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.RegistrationSchemasApi();
apiInstance.registrationSchemasList((error, data, response) => {
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

[**RegistrationSchema**](RegistrationSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

