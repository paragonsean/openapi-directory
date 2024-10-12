# AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**landlordControllerCreateMaintenancePreference**](LandlordControllerApi.md#landlordControllerCreateMaintenancePreference) | **POST** /v2/customer/{shortName}/landlord/tenancy/maintenance/preference | Post tenancy maintenance preferences:-
[**landlordControllerGetAccounts**](LandlordControllerApi.md#landlordControllerGetAccounts) | **GET** /v2/customer/{shortName}/landlord/accounting | Get the accounting details for the landlord.
[**landlordControllerGetDocument**](LandlordControllerApi.md#landlordControllerGetDocument) | **GET** /v2/customer/{shortName}/landlord/document | Download a Document
[**landlordControllerGetInvetoryReport**](LandlordControllerApi.md#landlordControllerGetInvetoryReport) | **GET** /v2/customer/{shortName}/landlord/inventory | Generate a Inventory PDF for a tenancy
[**landlordControllerGetInvoice**](LandlordControllerApi.md#landlordControllerGetInvoice) | **GET** /v2/customer/{shortName}/landlord/invoice | Get an invoice pdf belonging to the landlord.
[**landlordControllerGetLandlordCrmEntries**](LandlordControllerApi.md#landlordControllerGetLandlordCrmEntries) | **GET** /v2/customer/{shortName}/landlord/landlordcrmentries | Retrieve landlord&#39;s CRM ID
[**landlordControllerGetMaintenanceJobs**](LandlordControllerApi.md#landlordControllerGetMaintenanceJobs) | **GET** /v2/customer/{shortName}/landlord/maintenance | Get Active maintenance jobs.
[**landlordControllerGetProfitLossReport**](LandlordControllerApi.md#landlordControllerGetProfitLossReport) | **GET** /v2/customer/{shortName}/landlord/profitloss | Generate a Profit and Loss Report
[**landlordControllerGetRentArrears**](LandlordControllerApi.md#landlordControllerGetRentArrears) | **GET** /v2/customer/{shortName}/landlord/rentarrears | Rent Arrears
[**landlordControllerGetSASReport**](LandlordControllerApi.md#landlordControllerGetSASReport) | **GET** /v2/customer/{shortName}/landlord/sas | Generate a Self Assessment Tax Report
[**landlordControllerGetSettings**](LandlordControllerApi.md#landlordControllerGetSettings) | **GET** /v2/customer/{shortName}/landlord/settings | Get contact details of all linked landlords.
[**landlordControllerGetSummaryDetails**](LandlordControllerApi.md#landlordControllerGetSummaryDetails) | **GET** /v2/customer/{shortName}/landlord/summary | Get the summary details for the landlord.
[**landlordControllerGetTenancy**](LandlordControllerApi.md#landlordControllerGetTenancy) | **GET** /v2/customer/{shortName}/landlord/tenancy | Get tenancy details.
[**landlordControllerGetTenancyAgreementReport**](LandlordControllerApi.md#landlordControllerGetTenancyAgreementReport) | **GET** /v2/customer/{shortName}/landlord/tenancyagreement | Generate a Tenancy Agreement Copy (PDF)



## landlordControllerCreateMaintenancePreference

> String landlordControllerCreateMaintenancePreference(shortName, token, tenancyID, name, notes)

Post tenancy maintenance preferences:-

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
let tenancyID = "tenancyID_example"; // String | The Tenancy ID
let name = "name_example"; // String | Name of the maintenance preference to add
let notes = "notes_example"; // String | Notes of the maintenance preference to add
apiInstance.landlordControllerCreateMaintenancePreference(shortName, token, tenancyID, name, notes, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 
 **tenancyID** | **String**| The Tenancy ID | 
 **name** | **String**| Name of the maintenance preference to add | 
 **notes** | **String**| Notes of the maintenance preference to add | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## landlordControllerGetAccounts

> LandlordAccountingModel landlordControllerGetAccounts(shortName, token)

Get the accounting details for the landlord.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
apiInstance.landlordControllerGetAccounts(shortName, token, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 

### Return type

[**LandlordAccountingModel**](LandlordAccountingModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## landlordControllerGetDocument

> Object landlordControllerGetDocument(shortName, token, ID)

Download a Document

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
let ID = "ID_example"; // String | The Document ID
apiInstance.landlordControllerGetDocument(shortName, token, ID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 
 **ID** | **String**| The Document ID | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## landlordControllerGetInvetoryReport

> Object landlordControllerGetInvetoryReport(shortName, token, tenancyID)

Generate a Inventory PDF for a tenancy

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
let tenancyID = "tenancyID_example"; // String | The Tenancy ID
apiInstance.landlordControllerGetInvetoryReport(shortName, token, tenancyID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 
 **tenancyID** | **String**| The Tenancy ID | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## landlordControllerGetInvoice

> Object landlordControllerGetInvoice(shortName, token, invoiceID)

Get an invoice pdf belonging to the landlord.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
let invoiceID = "invoiceID_example"; // String | The invoice ID to load.
apiInstance.landlordControllerGetInvoice(shortName, token, invoiceID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 
 **invoiceID** | **String**| The invoice ID to load. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## landlordControllerGetLandlordCrmEntries

> [LandlordCrmEntry] landlordControllerGetLandlordCrmEntries(shortName, token)

Retrieve landlord&#39;s CRM ID

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
apiInstance.landlordControllerGetLandlordCrmEntries(shortName, token, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 

### Return type

[**[LandlordCrmEntry]**](LandlordCrmEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## landlordControllerGetMaintenanceJobs

> LandlordMaintenanceModel landlordControllerGetMaintenanceJobs(shortName, token)

Get Active maintenance jobs.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
apiInstance.landlordControllerGetMaintenanceJobs(shortName, token, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 

### Return type

[**LandlordMaintenanceModel**](LandlordMaintenanceModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## landlordControllerGetProfitLossReport

> LandlordProfitLossModel landlordControllerGetProfitLossReport(shortName, token)

Generate a Profit and Loss Report

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
apiInstance.landlordControllerGetProfitLossReport(shortName, token, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 

### Return type

[**LandlordProfitLossModel**](LandlordProfitLossModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## landlordControllerGetRentArrears

> LandlordRentArrearsModel landlordControllerGetRentArrears(shortName, token)

Rent Arrears

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
apiInstance.landlordControllerGetRentArrears(shortName, token, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 

### Return type

[**LandlordRentArrearsModel**](LandlordRentArrearsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## landlordControllerGetSASReport

> Object landlordControllerGetSASReport(shortName, token, yearEnd)

Generate a Self Assessment Tax Report

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
let yearEnd = 56; // Number | The Tax Year End.
apiInstance.landlordControllerGetSASReport(shortName, token, yearEnd, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 
 **yearEnd** | **Number**| The Tax Year End. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## landlordControllerGetSettings

> LandlordSettingsModel landlordControllerGetSettings(shortName, token)

Get contact details of all linked landlords.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
apiInstance.landlordControllerGetSettings(shortName, token, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 

### Return type

[**LandlordSettingsModel**](LandlordSettingsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## landlordControllerGetSummaryDetails

> LandlordSummaryModel landlordControllerGetSummaryDetails(shortName, token)

Get the summary details for the landlord.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
apiInstance.landlordControllerGetSummaryDetails(shortName, token, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 

### Return type

[**LandlordSummaryModel**](LandlordSummaryModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## landlordControllerGetTenancy

> LandlordTenancyModel landlordControllerGetTenancy(shortName, token, tenancyID)

Get tenancy details.

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
let tenancyID = "tenancyID_example"; // String | The Tenancy ID
apiInstance.landlordControllerGetTenancy(shortName, token, tenancyID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 
 **tenancyID** | **String**| The Tenancy ID | 

### Return type

[**LandlordTenancyModel**](LandlordTenancyModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## landlordControllerGetTenancyAgreementReport

> Object landlordControllerGetTenancyAgreementReport(shortName, token, tenancyID)

Generate a Tenancy Agreement Copy (PDF)

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.LandlordControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let token = "token_example"; // String | The login token returned from the /session POST call
let tenancyID = "tenancyID_example"; // String | The Tenancy ID
apiInstance.landlordControllerGetTenancyAgreementReport(shortName, token, tenancyID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **token** | **String**| The login token returned from the /session POST call | 
 **tenancyID** | **String**| The Tenancy ID | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

