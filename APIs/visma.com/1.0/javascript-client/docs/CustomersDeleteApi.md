# SeveraPublicRestApiDocumentation.CustomersDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addressesDeleteAddress**](CustomersDeleteApi.md#addressesDeleteAddress) | **DELETE** /v1/addresses/{guid} | Delete an address.
[**contactCommunicationsDeleteContactCommunication**](CustomersDeleteApi.md#contactCommunicationsDeleteContactCommunication) | **DELETE** /v1/contactcommunications/{guid} | Deletes contact&#39;s communication.
[**contactsDeleteContact**](CustomersDeleteApi.md#contactsDeleteContact) | **DELETE** /v1/contactpersons/{guid} | Deletes a contact.
[**customerCountrySettingsDeleteCustomerCountrySetting**](CustomersDeleteApi.md#customerCountrySettingsDeleteCustomerCountrySetting) | **DELETE** /v1/customercountrysettings/{guid} | Deletes a customer country setting.
[**customerCustomValuesDeleteCustomerCustomValue**](CustomersDeleteApi.md#customerCustomValuesDeleteCustomerCustomValue) | **DELETE** /v1/customers/customvalues/{guid} | Deletes a customer custom value.
[**customerMarketSegmentsDeleteCustomerMarketSegment**](CustomersDeleteApi.md#customerMarketSegmentsDeleteCustomerMarketSegment) | **DELETE** /v1/customermarketsegments/{guid} | Deletes a customer market segment.
[**customersDeleteCustomer**](CustomersDeleteApi.md#customersDeleteCustomer) | **DELETE** /v1/customers/{guid} | Deletes a customer.
[**keywordsDeleteContactKeyword**](CustomersDeleteApi.md#keywordsDeleteContactKeyword) | **DELETE** /v1/contacts/{contactGuid}/keywords/{guid} | Delete a keyword from the contact
[**salesNotesDeleteCustomerSalesNote**](CustomersDeleteApi.md#salesNotesDeleteCustomerSalesNote) | **DELETE** /v1/customersalesnotes/{guid} | Deletes a customer sales note.



## addressesDeleteAddress

> addressesDeleteAddress(guid)

Delete an address.

Returns: No Content (204) if succeeded. Not found (404) if address can&#39;t be found.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersDeleteApi();
let guid = "guid_example"; // String | ID for the address to delete.
apiInstance.addressesDeleteAddress(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the address to delete. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactCommunicationsDeleteContactCommunication

> contactCommunicationsDeleteContactCommunication(guid)

Deletes contact&#39;s communication.

Returns: No Content (204) if succeeded.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the contact's communication.
apiInstance.contactCommunicationsDeleteContactCommunication(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the contact&#39;s communication. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsDeleteContact

> contactsDeleteContact(guid)

Deletes a contact.

Returns: No Content (204) if succeeded.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the contact.
apiInstance.contactsDeleteContact(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the contact. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCountrySettingsDeleteCustomerCountrySetting

> customerCountrySettingsDeleteCustomerCountrySetting(guid)

Deletes a customer country setting.

Returns: No Content (204) if succeeded. Not found (404) if customer country setting can&#39;t be found.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the customer country setting.
apiInstance.customerCountrySettingsDeleteCustomerCountrySetting(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the customer country setting. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCustomValuesDeleteCustomerCustomValue

> customerCustomValuesDeleteCustomerCustomValue(guid)

Deletes a customer custom value.

Returns: No Content (204) if succeeded.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the customer custom value.
apiInstance.customerCustomValuesDeleteCustomerCustomValue(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the customer custom value. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerMarketSegmentsDeleteCustomerMarketSegment

> customerMarketSegmentsDeleteCustomerMarketSegment(guid)

Deletes a customer market segment.

Returns: No Content (204) if succeeded. Not found (404) if customer market segment can&#39;t be found.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersDeleteApi();
let guid = "guid_example"; // String | ID for the customer market segment to delete.
apiInstance.customerMarketSegmentsDeleteCustomerMarketSegment(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the customer market segment to delete. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersDeleteCustomer

> customersDeleteCustomer(guid)

Deletes a customer.

Returns: No Content (204) if succeeded.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the customer.
apiInstance.customersDeleteCustomer(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the customer. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keywordsDeleteContactKeyword

> keywordsDeleteContactKeyword(contactGuid, guid)

Delete a keyword from the contact

Returns: No Content (204) if succeeded. Not found (404) if the keyword or the link can&#39;t be found.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersDeleteApi();
let contactGuid = "contactGuid_example"; // String | 
let guid = "guid_example"; // String | 
apiInstance.keywordsDeleteContactKeyword(contactGuid, guid, (error, data, response) => {
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
 **contactGuid** | **String**|  | 
 **guid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesNotesDeleteCustomerSalesNote

> salesNotesDeleteCustomerSalesNote(guid)

Deletes a customer sales note.

Returns: No Content (204) if succeeded. OK (200) if note has child notes and can&#39;t be deleted. It is marked as IsDeleted &#x3D; true. Not found (404) if note can&#39;t be found.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the customer sales note.
apiInstance.salesNotesDeleteCustomerSalesNote(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the customer sales note. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

