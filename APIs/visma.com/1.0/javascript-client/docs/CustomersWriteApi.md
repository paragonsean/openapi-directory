# SeveraPublicRestApiDocumentation.CustomersWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addressesPatchAddress**](CustomersWriteApi.md#addressesPatchAddress) | **PATCH** /v1/addresses/{guid} | Update (Patch) an address or a part of it.
[**addressesPostCustomerAddress**](CustomersWriteApi.md#addressesPostCustomerAddress) | **POST** /v1/customers/{customerGuid}/addresses | Insert an address.
[**contactCommunicationsPatchContactCommunication**](CustomersWriteApi.md#contactCommunicationsPatchContactCommunication) | **PATCH** /v1/contactcommunications/{guid} | Update (Patch) a contact&#39;s communication or a part of it.
[**contactCommunicationsPostContactCommunication**](CustomersWriteApi.md#contactCommunicationsPostContactCommunication) | **POST** /v1/contactcommunications | Insert a communication for a contact.
[**contactsPatchContact**](CustomersWriteApi.md#contactsPatchContact) | **PATCH** /v1/contactpersons/{guid} | Update (Patch) an contact or a part of it.
[**contactsPostContact**](CustomersWriteApi.md#contactsPostContact) | **POST** /v1/contactpersons | Insert a contact.
[**customerCountrySettingsPatchCustomerCountrySettings**](CustomersWriteApi.md#customerCountrySettingsPatchCustomerCountrySettings) | **PATCH** /v1/customercountrysettings/{guid} | Update (Patch) a customer country setting.
[**customerCountrySettingsPostCustomerCountrySettings**](CustomersWriteApi.md#customerCountrySettingsPostCustomerCountrySettings) | **POST** /v1/customercountrysettings | Insert a customer country setting.
[**customerCustomValuesPatchCustomerCustomValue**](CustomersWriteApi.md#customerCustomValuesPatchCustomerCustomValue) | **PATCH** /v1/customers/customvalues/{guid} | Update (Patch) a customer custom value or a part of it.
[**customerCustomValuesPostCustomerCustomValue**](CustomersWriteApi.md#customerCustomValuesPostCustomerCustomValue) | **POST** /v1/customers/customvalues | Insert a customer custom value.
[**customerMarketSegmentsPostCustomerMarketSegment**](CustomersWriteApi.md#customerMarketSegmentsPostCustomerMarketSegment) | **POST** /v1/customermarketsegments | Add a market segment for customer.
[**customersPatchCustomer**](CustomersWriteApi.md#customersPatchCustomer) | **PATCH** /v1/customers/{guid} | Update (Patch) an customer or a part of it.
[**customersPostCustomer**](CustomersWriteApi.md#customersPostCustomer) | **POST** /v1/customers | Insert a customer.
[**keywordsLinkKeywordToContact**](CustomersWriteApi.md#keywordsLinkKeywordToContact) | **POST** /v1/contacts/{contactGuid}/keywords/{guid} | Link existing keyword to contact
[**salesNotesPatchCustomerSalesNote**](CustomersWriteApi.md#salesNotesPatchCustomerSalesNote) | **PATCH** /v1/customersalesnotes/{guid} | Update (Patch) a customer sales note or a part of it.
[**salesNotesPostCustomerSalesNotes**](CustomersWriteApi.md#salesNotesPostCustomerSalesNotes) | **POST** /v1/customersalesnotes | Insert a customer sales note.



## addressesPatchAddress

> [AddressModel] addressesPatchAddress(guid, opts)

Update (Patch) an address or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let guid = "guid_example"; // String | ID of the address.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of AddressModel.
};
apiInstance.addressesPatchAddress(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the address. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of AddressModel. | [optional] 

### Return type

[**[AddressModel]**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addressesPostCustomerAddress

> AddressModel addressesPostCustomerAddress(customerGuid, opts)

Insert an address.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let customerGuid = "customerGuid_example"; // String | ID of the customer to add the address for.
let opts = {
  'addressModel': new SeveraPublicRestApiDocumentation.AddressModel() // AddressModel | AddressModel.
};
apiInstance.addressesPostCustomerAddress(customerGuid, opts, (error, data, response) => {
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
 **customerGuid** | **String**| ID of the customer to add the address for. | 
 **addressModel** | [**AddressModel**](AddressModel.md)| AddressModel. | [optional] 

### Return type

[**AddressModel**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contactCommunicationsPatchContactCommunication

> ContactCommunicationModel contactCommunicationsPatchContactCommunication(guid, opts)

Update (Patch) a contact&#39;s communication or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let guid = "guid_example"; // String | ID of the contact's communication.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of ContactCommunicationModel.
};
apiInstance.contactCommunicationsPatchContactCommunication(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the contact&#39;s communication. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of ContactCommunicationModel. | [optional] 

### Return type

[**ContactCommunicationModel**](ContactCommunicationModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contactCommunicationsPostContactCommunication

> ContactCommunicationModel contactCommunicationsPostContactCommunication(opts)

Insert a communication for a contact.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let opts = {
  'contactCommunicationModel': new SeveraPublicRestApiDocumentation.ContactCommunicationModel() // ContactCommunicationModel | ContactCommunicationModel.
};
apiInstance.contactCommunicationsPostContactCommunication(opts, (error, data, response) => {
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
 **contactCommunicationModel** | [**ContactCommunicationModel**](ContactCommunicationModel.md)| ContactCommunicationModel. | [optional] 

### Return type

[**ContactCommunicationModel**](ContactCommunicationModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contactsPatchContact

> [ContactModel] contactsPatchContact(guid, opts)

Update (Patch) an contact or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let guid = "guid_example"; // String | ID of the contact.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ContactModel.
};
apiInstance.contactsPatchContact(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the contact. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ContactModel. | [optional] 

### Return type

[**[ContactModel]**](ContactModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contactsPostContact

> ContactModel contactsPostContact(opts)

Insert a contact.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let opts = {
  'contactModel': new SeveraPublicRestApiDocumentation.ContactModel() // ContactModel | ContactModel.
};
apiInstance.contactsPostContact(opts, (error, data, response) => {
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
 **contactModel** | [**ContactModel**](ContactModel.md)| ContactModel. | [optional] 

### Return type

[**ContactModel**](ContactModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerCountrySettingsPatchCustomerCountrySettings

> [CustomerCountrySettingsOutputModel] customerCountrySettingsPatchCustomerCountrySettings(guid, opts)

Update (Patch) a customer country setting.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let guid = "guid_example"; // String | ID of the customer country setting.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of CustomerCountrySettingsModel.
};
apiInstance.customerCountrySettingsPatchCustomerCountrySettings(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the customer country setting. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of CustomerCountrySettingsModel. | [optional] 

### Return type

[**[CustomerCountrySettingsOutputModel]**](CustomerCountrySettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerCountrySettingsPostCustomerCountrySettings

> CustomerCountrySettingsOutputModel customerCountrySettingsPostCustomerCountrySettings(opts)

Insert a customer country setting.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let opts = {
  'customerCountrySettingsInputModel': new SeveraPublicRestApiDocumentation.CustomerCountrySettingsInputModel() // CustomerCountrySettingsInputModel | CustomerCountrySettingsModel.
};
apiInstance.customerCountrySettingsPostCustomerCountrySettings(opts, (error, data, response) => {
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
 **customerCountrySettingsInputModel** | [**CustomerCountrySettingsInputModel**](CustomerCountrySettingsInputModel.md)| CustomerCountrySettingsModel. | [optional] 

### Return type

[**CustomerCountrySettingsOutputModel**](CustomerCountrySettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerCustomValuesPatchCustomerCustomValue

> [CustomerCustomValueModel] customerCustomValuesPatchCustomerCustomValue(guid, opts)

Update (Patch) a customer custom value or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let guid = "guid_example"; // String | ID of the customer custom value Can also be comma separate list of IDs to patch multiple customer custom values with one call. When multiple IDs are given, returns model which has list of succeeded customer custom values and list of errors.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of CustomerCustomValueModel.
};
apiInstance.customerCustomValuesPatchCustomerCustomValue(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the customer custom value Can also be comma separate list of IDs to patch multiple customer custom values with one call. When multiple IDs are given, returns model which has list of succeeded customer custom values and list of errors. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of CustomerCustomValueModel. | [optional] 

### Return type

[**[CustomerCustomValueModel]**](CustomerCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerCustomValuesPostCustomerCustomValue

> [CustomerCustomValueModel] customerCustomValuesPostCustomerCustomValue(opts)

Insert a customer custom value.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let opts = {
  'customerCustomValueModel': new SeveraPublicRestApiDocumentation.CustomerCustomValueModel() // CustomerCustomValueModel | CustomerCustomValueModel.
};
apiInstance.customerCustomValuesPostCustomerCustomValue(opts, (error, data, response) => {
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
 **customerCustomValueModel** | [**CustomerCustomValueModel**](CustomerCustomValueModel.md)| CustomerCustomValueModel. | [optional] 

### Return type

[**[CustomerCustomValueModel]**](CustomerCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerMarketSegmentsPostCustomerMarketSegment

> CustomerMarketSegmentModel customerMarketSegmentsPostCustomerMarketSegment(opts)

Add a market segment for customer.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let opts = {
  'customerMarketSegmentModel': new SeveraPublicRestApiDocumentation.CustomerMarketSegmentModel() // CustomerMarketSegmentModel | CustomerMarketSegmentModel.
};
apiInstance.customerMarketSegmentsPostCustomerMarketSegment(opts, (error, data, response) => {
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
 **customerMarketSegmentModel** | [**CustomerMarketSegmentModel**](CustomerMarketSegmentModel.md)| CustomerMarketSegmentModel. | [optional] 

### Return type

[**CustomerMarketSegmentModel**](CustomerMarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customersPatchCustomer

> [CustomerModel] customersPatchCustomer(guid, opts)

Update (Patch) an customer or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let guid = "guid_example"; // String | ID of the customer.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of CustomerModel.
};
apiInstance.customersPatchCustomer(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the customer. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of CustomerModel. | [optional] 

### Return type

[**[CustomerModel]**](CustomerModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customersPostCustomer

> CustomerModel customersPostCustomer(opts)

Insert a customer.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let opts = {
  'customerModel': new SeveraPublicRestApiDocumentation.CustomerModel() // CustomerModel | CustomerModel.
};
apiInstance.customersPostCustomer(opts, (error, data, response) => {
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
 **customerModel** | [**CustomerModel**](CustomerModel.md)| CustomerModel. | [optional] 

### Return type

[**CustomerModel**](CustomerModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## keywordsLinkKeywordToContact

> ContactKeywordModel keywordsLinkKeywordToContact(contactGuid, guid)

Link existing keyword to contact

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let contactGuid = "contactGuid_example"; // String | 
let guid = "guid_example"; // String | 
apiInstance.keywordsLinkKeywordToContact(contactGuid, guid, (error, data, response) => {
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
 **contactGuid** | **String**|  | 
 **guid** | **String**|  | 

### Return type

[**ContactKeywordModel**](ContactKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesNotesPatchCustomerSalesNote

> [CustomerSalesNoteOutputModel] salesNotesPatchCustomerSalesNote(guid, opts)

Update (Patch) a customer sales note or a part of it.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let guid = "guid_example"; // String | ID of the customer sales note.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of customer sales note model.
};
apiInstance.salesNotesPatchCustomerSalesNote(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the customer sales note. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of customer sales note model. | [optional] 

### Return type

[**[CustomerSalesNoteOutputModel]**](CustomerSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesNotesPostCustomerSalesNotes

> CustomerSalesNoteOutputModel salesNotesPostCustomerSalesNotes(opts)

Insert a customer sales note.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersWriteApi();
let opts = {
  'customerSalesNoteInputModel': new SeveraPublicRestApiDocumentation.CustomerSalesNoteInputModel() // CustomerSalesNoteInputModel | SalesNoteOutputModel
};
apiInstance.salesNotesPostCustomerSalesNotes(opts, (error, data, response) => {
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
 **customerSalesNoteInputModel** | [**CustomerSalesNoteInputModel**](CustomerSalesNoteInputModel.md)| SalesNoteOutputModel | [optional] 

### Return type

[**CustomerSalesNoteOutputModel**](CustomerSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

