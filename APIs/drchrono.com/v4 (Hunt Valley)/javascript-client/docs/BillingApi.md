# OpenapiJsClient.BillingApi

All URIs are relative to *https://app.drchrono.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingProfilesList**](BillingApi.md#billingProfilesList) | **GET** /api/billing_profiles | 
[**billingProfilesRead**](BillingApi.md#billingProfilesRead) | **GET** /api/billing_profiles/{id} | 
[**commLogsCreate**](BillingApi.md#commLogsCreate) | **POST** /api/comm_logs | 
[**commLogsList**](BillingApi.md#commLogsList) | **GET** /api/comm_logs | 
[**commLogsPartialUpdate**](BillingApi.md#commLogsPartialUpdate) | **PATCH** /api/comm_logs/{id} | 
[**commLogsRead**](BillingApi.md#commLogsRead) | **GET** /api/comm_logs/{id} | 
[**commLogsUpdate**](BillingApi.md#commLogsUpdate) | **PUT** /api/comm_logs/{id} | 
[**customInsurancePlanNamesList**](BillingApi.md#customInsurancePlanNamesList) | **GET** /api/custom_insurance_plan_names | 
[**customInsurancePlanNamesRead**](BillingApi.md#customInsurancePlanNamesRead) | **GET** /api/custom_insurance_plan_names/{id} | 
[**eligibilityChecksList**](BillingApi.md#eligibilityChecksList) | **GET** /api/eligibility_checks | 
[**eligibilityChecksRead**](BillingApi.md#eligibilityChecksRead) | **GET** /api/eligibility_checks/{id} | 
[**lineItemsCreate**](BillingApi.md#lineItemsCreate) | **POST** /api/line_items | 
[**lineItemsDelete**](BillingApi.md#lineItemsDelete) | **DELETE** /api/line_items/{id} | 
[**lineItemsList**](BillingApi.md#lineItemsList) | **GET** /api/line_items | 
[**lineItemsPartialUpdate**](BillingApi.md#lineItemsPartialUpdate) | **PATCH** /api/line_items/{id} | 
[**lineItemsRead**](BillingApi.md#lineItemsRead) | **GET** /api/line_items/{id} | 
[**lineItemsUpdate**](BillingApi.md#lineItemsUpdate) | **PUT** /api/line_items/{id} | 
[**patientPaymentLogList**](BillingApi.md#patientPaymentLogList) | **GET** /api/patient_payment_log | 
[**patientPaymentLogRead**](BillingApi.md#patientPaymentLogRead) | **GET** /api/patient_payment_log/{id} | 
[**patientPaymentsCreate**](BillingApi.md#patientPaymentsCreate) | **POST** /api/patient_payments | 
[**patientPaymentsList**](BillingApi.md#patientPaymentsList) | **GET** /api/patient_payments | 
[**patientPaymentsRead**](BillingApi.md#patientPaymentsRead) | **GET** /api/patient_payments/{id} | 
[**proceduresList**](BillingApi.md#proceduresList) | **GET** /api/procedures | 
[**proceduresRead**](BillingApi.md#proceduresRead) | **GET** /api/procedures/{id} | 
[**transactionsList**](BillingApi.md#transactionsList) | **GET** /api/transactions | 
[**transactionsRead**](BillingApi.md#transactionsRead) | **GET** /api/transactions/{id} | 



## billingProfilesList

> BillingProfilesList200Response billingProfilesList(opts)



Retrieve or search billing profiles

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.billingProfilesList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**BillingProfilesList200Response**](BillingProfilesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingProfilesRead

> BillingProfile billingProfilesRead(id, opts)



Retrieve an existing billing profiles

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'doctor': 56 // Number | 
};
apiInstance.billingProfilesRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **doctor** | **Number**|  | [optional] 

### Return type

[**BillingProfile**](BillingProfile.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commLogsCreate

> PhoneCallLog commLogsCreate(opts)



Create communication (phone call) logs

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'since': "since_example", // String | 
  'patient': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.commLogsCreate(opts, (error, data, response) => {
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
 **since** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**PhoneCallLog**](PhoneCallLog.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commLogsList

> CommLogsList200Response commLogsList(opts)



Retrieve or search communicatioin (phone call) logs

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'since': "since_example", // String | 
  'patient': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.commLogsList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**CommLogsList200Response**](CommLogsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commLogsPartialUpdate

> commLogsPartialUpdate(id, opts)



Update an existing communication (phone call) logs

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example", // String | 
  'patient': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.commLogsPartialUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **since** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## commLogsRead

> PhoneCallLog commLogsRead(id, opts)



Retrieve an existing communication (phone call) logs

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example", // String | 
  'patient': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.commLogsRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **since** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**PhoneCallLog**](PhoneCallLog.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commLogsUpdate

> commLogsUpdate(id, opts)



Update an existing communication (phone call) logs

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example", // String | 
  'patient': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.commLogsUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **since** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## customInsurancePlanNamesList

> CustomInsurancePlanNamesList200Response customInsurancePlanNamesList(opts)



Retrieve or search custom insurance plan names

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'since': "since_example", // String | 
  'user': 56, // Number | 
  'name': "name_example", // String | 
  'doctor': 56 // Number | 
};
apiInstance.customInsurancePlanNamesList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **user** | **Number**|  | [optional] 
 **name** | **String**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**CustomInsurancePlanNamesList200Response**](CustomInsurancePlanNamesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customInsurancePlanNamesRead

> CustomInsurancePlanName customInsurancePlanNamesRead(id, opts)



Retrieve an existing custom insurance plan name

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example", // String | 
  'user': 56, // Number | 
  'name': "name_example", // String | 
  'doctor': 56 // Number | 
};
apiInstance.customInsurancePlanNamesRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **since** | **String**|  | [optional] 
 **user** | **Number**|  | [optional] 
 **name** | **String**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**CustomInsurancePlanName**](CustomInsurancePlanName.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eligibilityChecksList

> EligibilityChecksList200Response eligibilityChecksList(opts)



Retrieve or search past eligibility checks for patient

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'appointment': 56, // Number | 
  'appointmentDate': "appointmentDate_example", // String | 
  'doctor': 56, // Number | 
  'queryDateRange': "queryDateRange_example", // String | 
  'appointmentDateRange': "appointmentDateRange_example", // String | 
  'queryDate': "queryDate_example", // String | 
  'patient': 56 // Number | 
};
apiInstance.eligibilityChecksList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **appointmentDate** | **String**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **queryDateRange** | **String**|  | [optional] 
 **appointmentDateRange** | **String**|  | [optional] 
 **queryDate** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 

### Return type

[**EligibilityChecksList200Response**](EligibilityChecksList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eligibilityChecksRead

> Coverage eligibilityChecksRead(id, opts)



Retrieve an existing past eligibility check

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'appointment': 56, // Number | 
  'appointmentDate': "appointmentDate_example", // String | 
  'doctor': 56, // Number | 
  'queryDateRange': "queryDateRange_example", // String | 
  'appointmentDateRange': "appointmentDateRange_example", // String | 
  'queryDate': "queryDate_example", // String | 
  'patient': 56 // Number | 
};
apiInstance.eligibilityChecksRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **appointment** | **Number**|  | [optional] 
 **appointmentDate** | **String**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **queryDateRange** | **String**|  | [optional] 
 **appointmentDateRange** | **String**|  | [optional] 
 **queryDate** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 

### Return type

[**Coverage**](Coverage.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lineItemsCreate

> BillingLineItem lineItemsCreate(opts)



Create billing line item for appointments

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'postedDate': "postedDate_example", // String | 
  'patient': 56, // Number | 
  'office': 56, // Number | 
  'doctor': 56, // Number | 
  'since': "since_example", // String | 
  'appointment': 56, // Number | 
  'serviceDate': "serviceDate_example" // String | 
};
apiInstance.lineItemsCreate(opts, (error, data, response) => {
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
 **postedDate** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **office** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **serviceDate** | **String**|  | [optional] 

### Return type

[**BillingLineItem**](BillingLineItem.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lineItemsDelete

> lineItemsDelete(id, opts)



### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'postedDate': "postedDate_example", // String | 
  'patient': 56, // Number | 
  'office': 56, // Number | 
  'doctor': 56, // Number | 
  'since': "since_example", // String | 
  'appointment': 56, // Number | 
  'serviceDate': "serviceDate_example" // String | 
};
apiInstance.lineItemsDelete(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **postedDate** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **office** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **serviceDate** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## lineItemsList

> LineItemsList200Response lineItemsList(opts)



Retrieve or search billing line items

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'postedDate': "postedDate_example", // String | 
  'patient': 56, // Number | 
  'office': 56, // Number | 
  'doctor': 56, // Number | 
  'since': "since_example", // String | 
  'appointment': 56, // Number | 
  'serviceDate': "serviceDate_example" // String | 
};
apiInstance.lineItemsList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **postedDate** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **office** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **serviceDate** | **String**|  | [optional] 

### Return type

[**LineItemsList200Response**](LineItemsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lineItemsPartialUpdate

> lineItemsPartialUpdate(id, opts)



### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'postedDate': "postedDate_example", // String | 
  'patient': 56, // Number | 
  'office': 56, // Number | 
  'doctor': 56, // Number | 
  'since': "since_example", // String | 
  'appointment': 56, // Number | 
  'serviceDate': "serviceDate_example" // String | 
};
apiInstance.lineItemsPartialUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **postedDate** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **office** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **serviceDate** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## lineItemsRead

> BillingLineItem lineItemsRead(id, opts)



Retrieve an existing billing line item

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'postedDate': "postedDate_example", // String | 
  'patient': 56, // Number | 
  'office': 56, // Number | 
  'doctor': 56, // Number | 
  'since': "since_example", // String | 
  'appointment': 56, // Number | 
  'serviceDate': "serviceDate_example" // String | 
};
apiInstance.lineItemsRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **postedDate** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **office** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **serviceDate** | **String**|  | [optional] 

### Return type

[**BillingLineItem**](BillingLineItem.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lineItemsUpdate

> lineItemsUpdate(id, opts)



### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'postedDate': "postedDate_example", // String | 
  'patient': 56, // Number | 
  'office': 56, // Number | 
  'doctor': 56, // Number | 
  'since': "since_example", // String | 
  'appointment': 56, // Number | 
  'serviceDate': "serviceDate_example" // String | 
};
apiInstance.lineItemsUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **postedDate** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **office** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **serviceDate** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## patientPaymentLogList

> PatientPaymentLogList200Response patientPaymentLogList(opts)



Retrieve or search patient payment logs

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'since': "since_example", // String | 
  'office': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.patientPaymentLogList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **office** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**PatientPaymentLogList200Response**](PatientPaymentLogList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patientPaymentLogRead

> CashPaymentLog patientPaymentLogRead(id, opts)



Retrieve an existing patient payment log

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example", // String | 
  'office': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.patientPaymentLogRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **since** | **String**|  | [optional] 
 **office** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**CashPaymentLog**](CashPaymentLog.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patientPaymentsCreate

> CashPayment patientPaymentsCreate(opts)



Create patient payment

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'since': "since_example", // String | 
  'patient': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.patientPaymentsCreate(opts, (error, data, response) => {
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
 **since** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**CashPayment**](CashPayment.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patientPaymentsList

> PatientPaymentsList200Response patientPaymentsList(opts)



Retrieve or search patient payments

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'since': "since_example", // String | 
  'patient': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.patientPaymentsList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**PatientPaymentsList200Response**](PatientPaymentsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patientPaymentsRead

> CashPayment patientPaymentsRead(id, opts)



Retrieve an existing patient payment

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example", // String | 
  'patient': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.patientPaymentsRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **since** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**CashPayment**](CashPayment.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proceduresList

> LineItemsList200Response proceduresList(opts)



### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'muDate': "muDate_example", // String | 
  'patient': 56, // Number | 
  'doctor': 56, // Number | 
  'muDateRange': "muDateRange_example", // String | 
  'appointment': 56, // Number | 
  'serviceDate': "serviceDate_example" // String | 
};
apiInstance.proceduresList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **muDate** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **muDateRange** | **String**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **serviceDate** | **String**|  | [optional] 

### Return type

[**LineItemsList200Response**](LineItemsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proceduresRead

> BillingLineItem proceduresRead(id, opts)



### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'muDate': "muDate_example", // String | 
  'patient': 56, // Number | 
  'doctor': 56, // Number | 
  'muDateRange': "muDateRange_example", // String | 
  'appointment': 56, // Number | 
  'serviceDate': "serviceDate_example" // String | 
};
apiInstance.proceduresRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **muDate** | **String**|  | [optional] 
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **muDateRange** | **String**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **serviceDate** | **String**|  | [optional] 

### Return type

[**BillingLineItem**](BillingLineItem.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsList

> TransactionsList200Response transactionsList(opts)



Retrieve or search insurance transactions associated with billing line items

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'lineItem': 56, // Number | 
  'postedDate': "postedDate_example", // String | 
  'appointment': 56, // Number | 
  'since': "since_example", // String | 
  'doctor': 56 // Number | 
};
apiInstance.transactionsList(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 
 **lineItem** | **Number**|  | [optional] 
 **postedDate** | **String**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**TransactionsList200Response**](TransactionsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsRead

> LineItemTransaction transactionsRead(id, opts)



Retrieve an existing insurance transaction

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.BillingApi();
let id = "id_example"; // String | 
let opts = {
  'lineItem': 56, // Number | 
  'postedDate': "postedDate_example", // String | 
  'appointment': 56, // Number | 
  'since': "since_example", // String | 
  'doctor': 56 // Number | 
};
apiInstance.transactionsRead(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **lineItem** | **Number**|  | [optional] 
 **postedDate** | **String**|  | [optional] 
 **appointment** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**LineItemTransaction**](LineItemTransaction.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

