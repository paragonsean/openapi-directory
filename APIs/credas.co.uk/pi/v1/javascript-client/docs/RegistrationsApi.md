# CredasApi.RegistrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addInstantRegistration**](RegistrationsApi.md#addInstantRegistration) | **POST** /api/registrations/instant | Creates new registration record, adds an ID document and optional selfie image in one go.
[**addRegistration**](RegistrationsApi.md#addRegistration) | **POST** /api/registrations | Creates new registration.
[**apiRegistrationsIdPdfExportSectionsGet**](RegistrationsApi.md#apiRegistrationsIdPdfExportSectionsGet) | **GET** /api/registrations/{id}/pdf-export-sections | Returns a PDF report for a given registration containing specified sections
[**checkSubmittedIdDocuments**](RegistrationsApi.md#checkSubmittedIdDocuments) | **GET** /api/registrations/{id}/check-submitted-id-documents | Checks if submitted documents are sufficient to complete registration.
[**getRegistrationPdfExport**](RegistrationsApi.md#getRegistrationPdfExport) | **GET** /api/registrations/{id}/pdf-export | Returns PDF export for a given registration.
[**getRegistrationSearch**](RegistrationsApi.md#getRegistrationSearch) | **GET** /api/registrations/search | Gets paged registration list by search criteria or nothing if there are no matching fields.  Optional parameters may be appended to the query string.  Maximum page size is 50.
[**getRegistrationSettings**](RegistrationsApi.md#getRegistrationSettings) | **GET** /api/registrations/{id}/settings | Gets registration settings or nothing if there are no settings associated with the registration.
[**getRegistrationSummariesByReferenceId**](RegistrationsApi.md#getRegistrationSummariesByReferenceId) | **GET** /api/registrations/referenceid/{referenceId}/summary | Finds registrations by the ReferenceId.
[**getRegistrationSummary**](RegistrationsApi.md#getRegistrationSummary) | **GET** /api/registrations/{id}/summary | Finds a registration by the Id.
[**getRegistrationSummaryByRegCode**](RegistrationsApi.md#getRegistrationSummaryByRegCode) | **GET** /api/registrations/regcode/{regCode}/summary | Finds a registration by the RegCode.
[**getRegistrationSupportedIdDocuments**](RegistrationsApi.md#getRegistrationSupportedIdDocuments) | **GET** /api/registrations/{id}/supported-id-documents | Get a list of supported id document for the specified registration id.
[**getShareCodePdfExport**](RegistrationsApi.md#getShareCodePdfExport) | **GET** /api/registrations/{id}/pdf-settlement-status | Returns settlement status PDF (Share Code) for a given registration.
[**overrideCheckStatus**](RegistrationsApi.md#overrideCheckStatus) | **PUT** /api/registrations/{id}/override-check-status | Sets an override for a specific check on the registration.
[**resendInvitation**](RegistrationsApi.md#resendInvitation) | **POST** /api/registrations/{id}/resend-invitation | Resends any invitation for the specified registration.
[**updateContactDetails**](RegistrationsApi.md#updateContactDetails) | **PUT** /api/registrations/{id}/contact-details | Updates a registration&#39;s contact details.
[**updateRegistrationSettings**](RegistrationsApi.md#updateRegistrationSettings) | **PUT** /api/registrations/{id}/settings | Updates registration settings.
[**updateRegistrationStatus**](RegistrationsApi.md#updateRegistrationStatus) | **PUT** /api/registrations/{id}/status | Updates the status of the registration to one specified in the request.



## addInstantRegistration

> CredasApiModelsRegistrationsAddInstantRegistrationResponse addInstantRegistration(apikey, opts)

Creates new registration record, adds an ID document and optional selfie image in one go.

It&#39;s designed to provide a quick integration path for external systems which capture these details.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsRegistrationsAddInstantRegistrationRequest': new CredasApi.CredasApiModelsRegistrationsAddInstantRegistrationRequest() // CredasApiModelsRegistrationsAddInstantRegistrationRequest | The Credas.Api.Models.Registrations.AddInstantRegistrationRequest object containing required data.
};
apiInstance.addInstantRegistration(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsRegistrationsAddInstantRegistrationRequest** | [**CredasApiModelsRegistrationsAddInstantRegistrationRequest**](CredasApiModelsRegistrationsAddInstantRegistrationRequest.md)| The Credas.Api.Models.Registrations.AddInstantRegistrationRequest object containing required data. | [optional] 

### Return type

[**CredasApiModelsRegistrationsAddInstantRegistrationResponse**](CredasApiModelsRegistrationsAddInstantRegistrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## addRegistration

> CredasApiModelsRegistrationsAddRegistrationResponse addRegistration(apikey, opts)

Creates new registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsRegistrationsAddRegistrationRequest': new CredasApi.CredasApiModelsRegistrationsAddRegistrationRequest() // CredasApiModelsRegistrationsAddRegistrationRequest | Object containing registration details.
};
apiInstance.addRegistration(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsRegistrationsAddRegistrationRequest** | [**CredasApiModelsRegistrationsAddRegistrationRequest**](CredasApiModelsRegistrationsAddRegistrationRequest.md)| Object containing registration details. | [optional] 

### Return type

[**CredasApiModelsRegistrationsAddRegistrationResponse**](CredasApiModelsRegistrationsAddRegistrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## apiRegistrationsIdPdfExportSectionsGet

> Blob apiRegistrationsIdPdfExportSectionsGet(id, apikey, opts)

Returns a PDF report for a given registration containing specified sections

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'comments': true, // Boolean | 
  'contactDetails': true, // Boolean | 
  'standardChecks': true, // Boolean | 
  'pepSanctionChecks': true, // Boolean | 
  'proofOfOwnership': true, // Boolean | 
  'bankAccountCheck': true, // Boolean | 
  'creditStatusCheck': true, // Boolean | 
  'liveness': true, // Boolean | 
  'excludeSelfie': true, // Boolean | 
  'excludeIDDocuments': true, // Boolean | 
  'dIATFSection': true // Boolean | 
};
apiInstance.apiRegistrationsIdPdfExportSectionsGet(id, apikey, opts, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 
 **comments** | **Boolean**|  | [optional] 
 **contactDetails** | **Boolean**|  | [optional] 
 **standardChecks** | **Boolean**|  | [optional] 
 **pepSanctionChecks** | **Boolean**|  | [optional] 
 **proofOfOwnership** | **Boolean**|  | [optional] 
 **bankAccountCheck** | **Boolean**|  | [optional] 
 **creditStatusCheck** | **Boolean**|  | [optional] 
 **liveness** | **Boolean**|  | [optional] 
 **excludeSelfie** | **Boolean**|  | [optional] 
 **excludeIDDocuments** | **Boolean**|  | [optional] 
 **dIATFSection** | **Boolean**|  | [optional] 

### Return type

**Blob**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## checkSubmittedIdDocuments

> CredasApiModelsRegistrationsCheckSubmittedIdDocumentsResponse checkSubmittedIdDocuments(id, apikey)

Checks if submitted documents are sufficient to complete registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.checkSubmittedIdDocuments(id, apikey, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**CredasApiModelsRegistrationsCheckSubmittedIdDocumentsResponse**](CredasApiModelsRegistrationsCheckSubmittedIdDocumentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getRegistrationPdfExport

> Blob getRegistrationPdfExport(id, apikey)

Returns PDF export for a given registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getRegistrationPdfExport(id, apikey, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

**Blob**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getRegistrationSearch

> CredasApiModelsRegistrationsPagedRegistrationSummary getRegistrationSearch(apikey, opts)

Gets paged registration list by search criteria or nothing if there are no matching fields.  Optional parameters may be appended to the query string.  Maximum page size is 50.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'pageNum': 0, // Number | Zero-based page number to retrieve.
  'pageSize': 50, // Number | Number of records to return on each request (Maximum value is 50).
  'forename': "forename_example", // String | Search by forename.
  'surname': "surname_example", // String | Search by surname.
  'email': "email_example", // String | Search by user email.
  'dob': "dob_example" // String | Date of birth in (yyyy-MM-dd) format
};
apiInstance.getRegistrationSearch(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| ApiKey supplied. | 
 **pageNum** | **Number**| Zero-based page number to retrieve. | [optional] [default to 0]
 **pageSize** | **Number**| Number of records to return on each request (Maximum value is 50). | [optional] [default to 50]
 **forename** | **String**| Search by forename. | [optional] 
 **surname** | **String**| Search by surname. | [optional] 
 **email** | **String**| Search by user email. | [optional] 
 **dob** | **String**| Date of birth in (yyyy-MM-dd) format | [optional] 

### Return type

[**CredasApiModelsRegistrationsPagedRegistrationSummary**](CredasApiModelsRegistrationsPagedRegistrationSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getRegistrationSettings

> getRegistrationSettings(id, apikey)

Gets registration settings or nothing if there are no settings associated with the registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getRegistrationSettings(id, apikey, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getRegistrationSummariesByReferenceId

> [CredasApiModelsRegistrationsRegistrationSummary] getRegistrationSummariesByReferenceId(referenceId, apikey)

Finds registrations by the ReferenceId.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let referenceId = "referenceId_example"; // String | ReferenceId - from external system to match Registrations on.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getRegistrationSummariesByReferenceId(referenceId, apikey, (error, data, response) => {
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
 **referenceId** | **String**| ReferenceId - from external system to match Registrations on. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**[CredasApiModelsRegistrationsRegistrationSummary]**](CredasApiModelsRegistrationsRegistrationSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getRegistrationSummary

> CredasApiModelsRegistrationsRegistrationSummary getRegistrationSummary(id, apikey)

Finds a registration by the Id.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getRegistrationSummary(id, apikey, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**CredasApiModelsRegistrationsRegistrationSummary**](CredasApiModelsRegistrationsRegistrationSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getRegistrationSummaryByRegCode

> CredasApiModelsRegistrationsRegistrationSummary getRegistrationSummaryByRegCode(regCode, apikey)

Finds a registration by the RegCode.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let regCode = "regCode_example"; // String | RegCode - short unique identifier.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getRegistrationSummaryByRegCode(regCode, apikey, (error, data, response) => {
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
 **regCode** | **String**| RegCode - short unique identifier. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**CredasApiModelsRegistrationsRegistrationSummary**](CredasApiModelsRegistrationsRegistrationSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getRegistrationSupportedIdDocuments

> CredasApiModelsRegistrationsSupportedIdDocument getRegistrationSupportedIdDocuments(id, apikey)

Get a list of supported id document for the specified registration id.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getRegistrationSupportedIdDocuments(id, apikey, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

[**CredasApiModelsRegistrationsSupportedIdDocument**](CredasApiModelsRegistrationsSupportedIdDocument.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## getShareCodePdfExport

> Blob getShareCodePdfExport(id, apikey)

Returns settlement status PDF (Share Code) for a given registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.getShareCodePdfExport(id, apikey, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

**Blob**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## overrideCheckStatus

> overrideCheckStatus(id, apikey, opts)

Sets an override for a specific check on the registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsStatusOverridesOverrideCheckStatusRequest': new CredasApi.CredasApiModelsStatusOverridesOverrideCheckStatusRequest() // CredasApiModelsStatusOverridesOverrideCheckStatusRequest | Request data.
};
apiInstance.overrideCheckStatus(id, apikey, opts, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsStatusOverridesOverrideCheckStatusRequest** | [**CredasApiModelsStatusOverridesOverrideCheckStatusRequest**](CredasApiModelsStatusOverridesOverrideCheckStatusRequest.md)| Request data. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## resendInvitation

> resendInvitation(id, apikey)

Resends any invitation for the specified registration.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
apiInstance.resendInvitation(id, apikey, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## updateContactDetails

> updateContactDetails(id, apikey, opts)

Updates a registration&#39;s contact details.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsRegistrationsUpdateContactDetailsRequest': new CredasApi.CredasApiModelsRegistrationsUpdateContactDetailsRequest() // CredasApiModelsRegistrationsUpdateContactDetailsRequest | Object containing contact details.
};
apiInstance.updateContactDetails(id, apikey, opts, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsRegistrationsUpdateContactDetailsRequest** | [**CredasApiModelsRegistrationsUpdateContactDetailsRequest**](CredasApiModelsRegistrationsUpdateContactDetailsRequest.md)| Object containing contact details. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## updateRegistrationSettings

> updateRegistrationSettings(id, apikey, opts)

Updates registration settings.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsRegistrationsRegistrationSettings': new CredasApi.CredasApiModelsRegistrationsRegistrationSettings() // CredasApiModelsRegistrationsRegistrationSettings | Object containing registration settings.
};
apiInstance.updateRegistrationSettings(id, apikey, opts, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsRegistrationsRegistrationSettings** | [**CredasApiModelsRegistrationsRegistrationSettings**](CredasApiModelsRegistrationsRegistrationSettings.md)| Object containing registration settings. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## updateRegistrationStatus

> updateRegistrationStatus(id, apikey, opts)

Updates the status of the registration to one specified in the request.

### Example

```javascript
import CredasApi from 'credas_api';

let apiInstance = new CredasApi.RegistrationsApi();
let id = "id_example"; // String | Id of the registration.
let apikey = "apikey_example"; // String | ApiKey supplied.
let opts = {
  'credasApiModelsRegistrationsUpdateRegistrationStatusRequest': new CredasApi.CredasApiModelsRegistrationsUpdateRegistrationStatusRequest() // CredasApiModelsRegistrationsUpdateRegistrationStatusRequest | Request object containing the details.
};
apiInstance.updateRegistrationStatus(id, apikey, opts, (error, data, response) => {
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
 **id** | **String**| Id of the registration. | 
 **apikey** | **String**| ApiKey supplied. | 
 **credasApiModelsRegistrationsUpdateRegistrationStatusRequest** | [**CredasApiModelsRegistrationsUpdateRegistrationStatusRequest**](CredasApiModelsRegistrationsUpdateRegistrationStatusRequest.md)| Request object containing the details. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

