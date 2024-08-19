# SeveraPublicRestApiDocumentation.CustomersReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addressesGetAddress**](CustomersReadApi.md#addressesGetAddress) | **GET** /v1/addresses/{guid} | Get address by ID.
[**addressesGetAddresses**](CustomersReadApi.md#addressesGetAddresses) | **GET** /v1/addresses | Get the addresses.
[**addressesGetContactAddress**](CustomersReadApi.md#addressesGetContactAddress) | **GET** /v1/contactpersons/{contactGuid}/addresses | Get contact person&#39;s address
[**addressesGetCustomerAddresses**](CustomersReadApi.md#addressesGetCustomerAddresses) | **GET** /v1/customers/{customerGuid}/addresses | Get customer&#39;s addresses
[**contactCommunicationsGetCommunication**](CustomersReadApi.md#contactCommunicationsGetCommunication) | **GET** /v1/contactcommunications/{guid} | Get contact communication by ID.
[**contactCommunicationsGetCommunications**](CustomersReadApi.md#contactCommunicationsGetCommunications) | **GET** /v1/contactcommunications | Get all contact communications.
[**contactCommunicationsGetCommunications2**](CustomersReadApi.md#contactCommunicationsGetCommunications2) | **GET** /v1/contacts/{contactGuid}/contactcommunications | Get all communications for a contact.
[**contactsGetContact**](CustomersReadApi.md#contactsGetContact) | **GET** /v1/contactpersons/{guid} | Get contact by ID.
[**contactsGetContacts**](CustomersReadApi.md#contactsGetContacts) | **GET** /v1/contactpersons | Get all the contact persons.
[**contactsGetCustomerContacts**](CustomersReadApi.md#contactsGetCustomerContacts) | **GET** /v1/customers/{customerGuid}/contactpersons | Get the contact persons for a customer.
[**customerCountrySettingsGetCustomerCountrySettings**](CustomersReadApi.md#customerCountrySettingsGetCustomerCountrySettings) | **GET** /v1/customers/{customerGuid}/customercountrysettings | Get all the country settings for a customer.
[**customerCustomValuesGetCustomerCustomValue**](CustomersReadApi.md#customerCustomValuesGetCustomerCustomValue) | **GET** /v1/customers/customvalues/{guid} | Get customer custom value by ID.
[**customerCustomValuesGetCustomerCustomValues**](CustomersReadApi.md#customerCustomValuesGetCustomerCustomValues) | **GET** /v1/customers/{customerGuid}/customvalues | Get the customer custom values.
[**customerMarketSegmentsGetAllCustomerMarketSegments**](CustomersReadApi.md#customerMarketSegmentsGetAllCustomerMarketSegments) | **GET** /v1/customermarketsegments | Get all Customer Market Segments.
[**customerMarketSegmentsGetCustomerMarketSegment**](CustomersReadApi.md#customerMarketSegmentsGetCustomerMarketSegment) | **GET** /v1/customermarketsegments/{guid} | Get the customer market segment.
[**customerMarketSegmentsGetCustomerMarketSegments**](CustomersReadApi.md#customerMarketSegmentsGetCustomerMarketSegments) | **GET** /v1/customers/{customerGuid}/customermarketsegments | Get the Market Segments for a customer.
[**customersGetCustomer**](CustomersReadApi.md#customersGetCustomer) | **GET** /v1/customers/{guid} | Get customer by GUID.
[**customersGetCustomers**](CustomersReadApi.md#customersGetCustomers) | **GET** /v1/customers | Get all the customers
[**keywordsGetContactKeywords**](CustomersReadApi.md#keywordsGetContactKeywords) | **GET** /v1/contacts/{contactGuid}/keywords | Get all the keywords for contact.
[**salesNotesGetAllCustomerSalesNotes_0**](CustomersReadApi.md#salesNotesGetAllCustomerSalesNotes_0) | **GET** /v1/customers/{customerGuid}/salesnotes | Get the sales notes by customer guid.
[**salesNotesGetCustomerSalesNote**](CustomersReadApi.md#salesNotesGetCustomerSalesNote) | **GET** /v1/customersalesnotes/{guid} | Get customer sales note by ID.
[**salesNotesGetCustomerSalesNotes**](CustomersReadApi.md#salesNotesGetCustomerSalesNotes) | **GET** /v1/customers/{customerGuid}/customersalesnotes | Get the customer sales notes.



## addressesGetAddress

> AddressModel addressesGetAddress(guid)

Get address by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let guid = "guid_example"; // String | GUID used to get the address.
apiInstance.addressesGetAddress(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the address. | 

### Return type

[**AddressModel**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addressesGetAddresses

> [AddressModel] addressesGetAddresses(opts)

Get the addresses.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get addresses that have been added or changed after this date time (greater or equal).
};
apiInstance.addressesGetAddresses(opts, (error, data, response) => {
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
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **changedSince** | **Date**| Optional: Get addresses that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[AddressModel]**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addressesGetContactAddress

> [AddressModel] addressesGetContactAddress(contactGuid)

Get contact person&#39;s address

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let contactGuid = "contactGuid_example"; // String | ID for the contact person
apiInstance.addressesGetContactAddress(contactGuid, (error, data, response) => {
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
 **contactGuid** | **String**| ID for the contact person | 

### Return type

[**[AddressModel]**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addressesGetCustomerAddresses

> [AddressModel] addressesGetCustomerAddresses(customerGuid, opts)

Get customer&#39;s addresses

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let customerGuid = "customerGuid_example"; // String | ID for the customer.
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'calculateRowCount': false // Boolean | Optional: Calculate total number of rows.
};
apiInstance.addressesGetCustomerAddresses(customerGuid, opts, (error, data, response) => {
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
 **customerGuid** | **String**| ID for the customer. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]

### Return type

[**[AddressModel]**](AddressModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactCommunicationsGetCommunication

> ContactCommunicationModel contactCommunicationsGetCommunication(guid)

Get contact communication by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let guid = "guid_example"; // String | GUID used to get the contact communication.
apiInstance.contactCommunicationsGetCommunication(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the contact communication. | 

### Return type

[**ContactCommunicationModel**](ContactCommunicationModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactCommunicationsGetCommunications

> [ContactCommunicationModel] contactCommunicationsGetCommunications(opts)

Get all contact communications.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all contact communications, if given as true return only active contact communications, if given as false returns only inactive contact communications.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from contact communication value.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get contact communications that have been added or changed after this date time (greater or equal).
};
apiInstance.contactCommunicationsGetCommunications(opts, (error, data, response) => {
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
 **active** | **Boolean**| If not given, return all contact communications, if given as true return only active contact communications, if given as false returns only inactive contact communications. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from contact communication value. | [optional] [default to &#39;&#39;]
 **changedSince** | **Date**| Optional: Get contact communications that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ContactCommunicationModel]**](ContactCommunicationModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactCommunicationsGetCommunications2

> [ContactCommunicationModel] contactCommunicationsGetCommunications2(contactGuid, opts)

Get all communications for a contact.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let contactGuid = "contactGuid_example"; // String | Whose communications are requested.
let opts = {
  'active': true // Boolean | If not given, return all contact communications, if given as true return only active contact communications, if given as false returns only inactive contact communications.
};
apiInstance.contactCommunicationsGetCommunications2(contactGuid, opts, (error, data, response) => {
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
 **contactGuid** | **String**| Whose communications are requested. | 
 **active** | **Boolean**| If not given, return all contact communications, if given as true return only active contact communications, if given as false returns only inactive contact communications. | [optional] 

### Return type

[**[ContactCommunicationModel]**](ContactCommunicationModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsGetContact

> ContactModel contactsGetContact(guid)

Get contact by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let guid = "guid_example"; // String | GUID used to get the contact.
apiInstance.contactsGetContact(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the contact. | 

### Return type

[**ContactModel**](ContactModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsGetContacts

> [ContactModel] contactsGetContacts(opts)

Get all the contact persons.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let opts = {
  'active': true, // Boolean | If not given, return all Contact persons, if given as true return only active Contact persons, if given as false returns only inactive Contact persons.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from contact person's name or communication method (i.e. phone number or email address).
  'searchCriterias': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndObject()], // [KeyValuePairOfStringAndObject] | Optional: Search criterias.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()], // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=FirstName&sortings[0].value=Desc &sortings[1].key=LastName&sortings[1].value=Asc\".
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get contact persons that have been added or changed after this date time (greater or equal).
};
apiInstance.contactsGetContacts(opts, (error, data, response) => {
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
 **active** | **Boolean**| If not given, return all Contact persons, if given as true return only active Contact persons, if given as false returns only inactive Contact persons. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from contact person&#39;s name or communication method (i.e. phone number or email address). | [optional] [default to &#39;&#39;]
 **searchCriterias** | [**[KeyValuePairOfStringAndObject]**](KeyValuePairOfStringAndObject.md)| Optional: Search criterias. | [optional] 
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;FirstName&amp;sortings[0].value&#x3D;Desc &amp;sortings[1].key&#x3D;LastName&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 
 **changedSince** | **Date**| Optional: Get contact persons that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ContactModel]**](ContactModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contactsGetCustomerContacts

> [ContactModel] contactsGetCustomerContacts(customerGuid, opts)

Get the contact persons for a customer.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let customerGuid = "customerGuid_example"; // String | Customer guid used to get the contact persons.
let opts = {
  'active': true, // Boolean | If not given, return all Contact persons, if given as true return only active Contact persons, if given as false returns only inactive Contact persons.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''" // String | Optional: Text to search from contact person's name or communication method (i.e. phone number or email address).
};
apiInstance.contactsGetCustomerContacts(customerGuid, opts, (error, data, response) => {
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
 **customerGuid** | **String**| Customer guid used to get the contact persons. | 
 **active** | **Boolean**| If not given, return all Contact persons, if given as true return only active Contact persons, if given as false returns only inactive Contact persons. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from contact person&#39;s name or communication method (i.e. phone number or email address). | [optional] [default to &#39;&#39;]

### Return type

[**[ContactModel]**](ContactModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCountrySettingsGetCustomerCountrySettings

> [CustomerCountrySettingsOutputModel] customerCountrySettingsGetCustomerCountrySettings(customerGuid)

Get all the country settings for a customer.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let customerGuid = "customerGuid_example"; // String | GUID of the customer.
apiInstance.customerCountrySettingsGetCustomerCountrySettings(customerGuid, (error, data, response) => {
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
 **customerGuid** | **String**| GUID of the customer. | 

### Return type

[**[CustomerCountrySettingsOutputModel]**](CustomerCountrySettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCustomValuesGetCustomerCustomValue

> CustomerCustomValueModel customerCustomValuesGetCustomerCustomValue(guid)

Get customer custom value by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let guid = "guid_example"; // String | Id used to get the customer custom value.
apiInstance.customerCustomValuesGetCustomerCustomValue(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the customer custom value. | 

### Return type

[**CustomerCustomValueModel**](CustomerCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCustomValuesGetCustomerCustomValues

> [CustomerCustomValueModel] customerCustomValuesGetCustomerCustomValues(customerGuid, opts)

Get the customer custom values.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let customerGuid = "customerGuid_example"; // String | ID of the customer.
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'active': true, // Boolean | Optional: Get only values of active or inactive customer custom properties.
  'target': ["null"], // [String] | List of target for which to get the values.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
};
apiInstance.customerCustomValuesGetCustomerCustomValues(customerGuid, opts, (error, data, response) => {
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
 **customerGuid** | **String**| ID of the customer. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **active** | **Boolean**| Optional: Get only values of active or inactive customer custom properties. | [optional] 
 **target** | [**[String]**](String.md)| List of target for which to get the values. | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[CustomerCustomValueModel]**](CustomerCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerMarketSegmentsGetAllCustomerMarketSegments

> [CustomerMarketSegmentModel] customerMarketSegmentsGetAllCustomerMarketSegments(opts)

Get all Customer Market Segments.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from customer market segment name.
  'parentMarketSegmentGuid': "parentMarketSegmentGuid_example", // String | Optional: Fetches all children of a parent based on parent market segment guid.
  'includeParentLevel': true // Boolean | Optional: Returns only child segments when false. Has no effect if parentMarketSegmentGuid parameter is defined. Default = true.
};
apiInstance.customerMarketSegmentsGetAllCustomerMarketSegments(opts, (error, data, response) => {
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
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from customer market segment name. | [optional] [default to &#39;&#39;]
 **parentMarketSegmentGuid** | **String**| Optional: Fetches all children of a parent based on parent market segment guid. | [optional] 
 **includeParentLevel** | **Boolean**| Optional: Returns only child segments when false. Has no effect if parentMarketSegmentGuid parameter is defined. Default &#x3D; true. | [optional] [default to true]

### Return type

[**[CustomerMarketSegmentModel]**](CustomerMarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerMarketSegmentsGetCustomerMarketSegment

> CustomerMarketSegmentModel customerMarketSegmentsGetCustomerMarketSegment(guid)

Get the customer market segment.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let guid = "guid_example"; // String | Customer market segment guid.
apiInstance.customerMarketSegmentsGetCustomerMarketSegment(guid, (error, data, response) => {
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
 **guid** | **String**| Customer market segment guid. | 

### Return type

[**CustomerMarketSegmentModel**](CustomerMarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerMarketSegmentsGetCustomerMarketSegments

> [CustomerMarketSegmentModel] customerMarketSegmentsGetCustomerMarketSegments(customerGuid, opts)

Get the Market Segments for a customer.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let customerGuid = "customerGuid_example"; // String | ID of the customer.
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'includeMarketSegmentsFromRegistry': false // Boolean | Optional: Return also the markets segments that are not in use for the customer.
};
apiInstance.customerMarketSegmentsGetCustomerMarketSegments(customerGuid, opts, (error, data, response) => {
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
 **customerGuid** | **String**| ID of the customer. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **includeMarketSegmentsFromRegistry** | **Boolean**| Optional: Return also the markets segments that are not in use for the customer. | [optional] [default to false]

### Return type

[**[CustomerMarketSegmentModel]**](CustomerMarketSegmentModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersGetCustomer

> CustomerModel customersGetCustomer(guid)

Get customer by GUID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let guid = "guid_example"; // String | ID used to get the customer.
apiInstance.customersGetCustomer(guid, (error, data, response) => {
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
 **guid** | **String**| ID used to get the customer. | 

### Return type

[**CustomerModel**](CustomerModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersGetCustomers

> [CustomerModel] customersGetCustomers(opts)

Get all the customers

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | 
  'rowCount': 56, // Number | Optional: How many rows to fetch.
  'isActive': true, // Boolean | If not given, return all Customers, if given as true return only active Customers, if given as false returns only inactive Customers.
  'customerOwnerGuids': ["null"], // [String] | Optional: List of customer owner ids to search for. Default all.
  'isInternal': true, // Boolean | Optional: When true returns only internal customer
  'numbers': [null], // [Number] | Optional: List of customer numbers.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get customers that have been added or changed after this date time (greater or equal).
  'emailAddresses': ["null"], // [String] | Optional: Get customers where email address matches to any provided email address
  'customerNames': ["null"] // [String] | Optional: Get customers where customer name matches to any provided customer name
};
apiInstance.customersGetCustomers(opts, (error, data, response) => {
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
 **pageToken** | **String**|  | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch. | [optional] 
 **isActive** | **Boolean**| If not given, return all Customers, if given as true return only active Customers, if given as false returns only inactive Customers. | [optional] 
 **customerOwnerGuids** | [**[String]**](String.md)| Optional: List of customer owner ids to search for. Default all. | [optional] 
 **isInternal** | **Boolean**| Optional: When true returns only internal customer | [optional] 
 **numbers** | [**[Number]**](Number.md)| Optional: List of customer numbers. | [optional] 
 **changedSince** | **Date**| Optional: Get customers that have been added or changed after this date time (greater or equal). | [optional] 
 **emailAddresses** | [**[String]**](String.md)| Optional: Get customers where email address matches to any provided email address | [optional] 
 **customerNames** | [**[String]**](String.md)| Optional: Get customers where customer name matches to any provided customer name | [optional] 

### Return type

[**[CustomerModel]**](CustomerModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keywordsGetContactKeywords

> [KeywordModel] keywordsGetContactKeywords(contactGuid, opts)

Get all the keywords for contact.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let contactGuid = "contactGuid_example"; // String | ID of the user whose keywords are requested.
let opts = {
  'active': true, // Boolean | If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Keyword&sortings[0].value=Desc\".
};
apiInstance.keywordsGetContactKeywords(contactGuid, opts, (error, data, response) => {
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
 **contactGuid** | **String**| ID of the user whose keywords are requested. | 
 **active** | **Boolean**| If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords. | [optional] 
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] 

### Return type

[**[KeywordModel]**](KeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesNotesGetAllCustomerSalesNotes_0

> [SalesNoteOutputModel] salesNotesGetAllCustomerSalesNotes_0(customerGuid, opts)

Get the sales notes by customer guid.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let customerGuid = "customerGuid_example"; // String | Customer guid used to get the notes.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get sales notes that have been added or changed after this date time (greater or equal).
};
apiInstance.salesNotesGetAllCustomerSalesNotes_0(customerGuid, opts, (error, data, response) => {
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
 **customerGuid** | **String**| Customer guid used to get the notes. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get sales notes that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[SalesNoteOutputModel]**](SalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesNotesGetCustomerSalesNote

> CustomerSalesNoteOutputModel salesNotesGetCustomerSalesNote(guid)

Get customer sales note by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let guid = "guid_example"; // String | GUID used to get the customer sales note.
apiInstance.salesNotesGetCustomerSalesNote(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the customer sales note. | 

### Return type

[**CustomerSalesNoteOutputModel**](CustomerSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesNotesGetCustomerSalesNotes

> [CustomerSalesNoteOutputModel] salesNotesGetCustomerSalesNotes(customerGuid, opts)

Get the customer sales notes.

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

let apiInstance = new SeveraPublicRestApiDocumentation.CustomersReadApi();
let customerGuid = "customerGuid_example"; // String | Customer guid used to get the notes.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get sales notes that have been added or changed after this date time (greater or equal).
};
apiInstance.salesNotesGetCustomerSalesNotes(customerGuid, opts, (error, data, response) => {
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
 **customerGuid** | **String**| Customer guid used to get the notes. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get sales notes that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[CustomerSalesNoteOutputModel]**](CustomerSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

