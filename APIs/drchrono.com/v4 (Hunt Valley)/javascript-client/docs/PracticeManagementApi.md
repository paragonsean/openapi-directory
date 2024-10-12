# OpenapiJsClient.PracticeManagementApi

All URIs are relative to *https://app.drchrono.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventoryCategoriesList**](PracticeManagementApi.md#inventoryCategoriesList) | **GET** /api/inventory_categories | 
[**inventoryCategoriesRead**](PracticeManagementApi.md#inventoryCategoriesRead) | **GET** /api/inventory_categories/{id} | 
[**inventoryVaccinesCreate**](PracticeManagementApi.md#inventoryVaccinesCreate) | **POST** /api/inventory_vaccines | 
[**inventoryVaccinesList**](PracticeManagementApi.md#inventoryVaccinesList) | **GET** /api/inventory_vaccines | 
[**inventoryVaccinesRead**](PracticeManagementApi.md#inventoryVaccinesRead) | **GET** /api/inventory_vaccines/{id} | 
[**messagesCreate**](PracticeManagementApi.md#messagesCreate) | **POST** /api/messages | 
[**messagesDelete**](PracticeManagementApi.md#messagesDelete) | **DELETE** /api/messages/{id} | 
[**messagesList**](PracticeManagementApi.md#messagesList) | **GET** /api/messages | 
[**messagesPartialUpdate**](PracticeManagementApi.md#messagesPartialUpdate) | **PATCH** /api/messages/{id} | 
[**messagesRead**](PracticeManagementApi.md#messagesRead) | **GET** /api/messages/{id} | 
[**messagesUpdate**](PracticeManagementApi.md#messagesUpdate) | **PUT** /api/messages/{id} | 
[**officesAddExamRoom**](PracticeManagementApi.md#officesAddExamRoom) | **POST** /api/offices/{id}/add_exam_room | 
[**officesList**](PracticeManagementApi.md#officesList) | **GET** /api/offices | 
[**officesPartialUpdate**](PracticeManagementApi.md#officesPartialUpdate) | **PATCH** /api/offices/{id} | 
[**officesRead**](PracticeManagementApi.md#officesRead) | **GET** /api/offices/{id} | 
[**officesUpdate**](PracticeManagementApi.md#officesUpdate) | **PUT** /api/offices/{id} | 
[**taskCategoriesCreate**](PracticeManagementApi.md#taskCategoriesCreate) | **POST** /api/task_categories | 
[**taskCategoriesList**](PracticeManagementApi.md#taskCategoriesList) | **GET** /api/task_categories | 
[**taskCategoriesPartialUpdate**](PracticeManagementApi.md#taskCategoriesPartialUpdate) | **PATCH** /api/task_categories/{id} | 
[**taskCategoriesRead**](PracticeManagementApi.md#taskCategoriesRead) | **GET** /api/task_categories/{id} | 
[**taskCategoriesUpdate**](PracticeManagementApi.md#taskCategoriesUpdate) | **PUT** /api/task_categories/{id} | 
[**taskNotesCreate**](PracticeManagementApi.md#taskNotesCreate) | **POST** /api/task_notes | 
[**taskNotesList**](PracticeManagementApi.md#taskNotesList) | **GET** /api/task_notes | 
[**taskNotesPartialUpdate**](PracticeManagementApi.md#taskNotesPartialUpdate) | **PATCH** /api/task_notes/{id} | 
[**taskNotesRead**](PracticeManagementApi.md#taskNotesRead) | **GET** /api/task_notes/{id} | 
[**taskNotesUpdate**](PracticeManagementApi.md#taskNotesUpdate) | **PUT** /api/task_notes/{id} | 
[**taskStatusesCreate**](PracticeManagementApi.md#taskStatusesCreate) | **POST** /api/task_statuses | 
[**taskStatusesList**](PracticeManagementApi.md#taskStatusesList) | **GET** /api/task_statuses | 
[**taskStatusesPartialUpdate**](PracticeManagementApi.md#taskStatusesPartialUpdate) | **PATCH** /api/task_statuses/{id} | 
[**taskStatusesRead**](PracticeManagementApi.md#taskStatusesRead) | **GET** /api/task_statuses/{id} | 
[**taskStatusesUpdate**](PracticeManagementApi.md#taskStatusesUpdate) | **PUT** /api/task_statuses/{id} | 
[**taskTemplatesCreate**](PracticeManagementApi.md#taskTemplatesCreate) | **POST** /api/task_templates | 
[**taskTemplatesList**](PracticeManagementApi.md#taskTemplatesList) | **GET** /api/task_templates | 
[**taskTemplatesPartialUpdate**](PracticeManagementApi.md#taskTemplatesPartialUpdate) | **PATCH** /api/task_templates/{id} | 
[**taskTemplatesRead**](PracticeManagementApi.md#taskTemplatesRead) | **GET** /api/task_templates/{id} | 
[**taskTemplatesUpdate**](PracticeManagementApi.md#taskTemplatesUpdate) | **PUT** /api/task_templates/{id} | 
[**tasksCreate**](PracticeManagementApi.md#tasksCreate) | **POST** /api/tasks | 
[**tasksList**](PracticeManagementApi.md#tasksList) | **GET** /api/tasks | 
[**tasksPartialUpdate**](PracticeManagementApi.md#tasksPartialUpdate) | **PATCH** /api/tasks/{id} | 
[**tasksRead**](PracticeManagementApi.md#tasksRead) | **GET** /api/tasks/{id} | 
[**tasksUpdate**](PracticeManagementApi.md#tasksUpdate) | **PUT** /api/tasks/{id} | 



## inventoryCategoriesList

> InventoryCategoriesList200Response inventoryCategoriesList(opts)



Retrieve or search inventory categories

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'since': "since_example", // String | 
  'doctor': 56 // Number | 
};
apiInstance.inventoryCategoriesList(opts, (error, data, response) => {
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
 **doctor** | **Number**|  | [optional] 

### Return type

[**InventoryCategoriesList200Response**](InventoryCategoriesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## inventoryCategoriesRead

> InventoryCategory inventoryCategoriesRead(id, opts)



Retrieve an existing inventory category

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example", // String | 
  'doctor': 56 // Number | 
};
apiInstance.inventoryCategoriesRead(id, opts, (error, data, response) => {
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
 **doctor** | **Number**|  | [optional] 

### Return type

[**InventoryCategory**](InventoryCategory.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## inventoryVaccinesCreate

> InventoryVaccine inventoryVaccinesCreate(opts)



Create vaccine inventory

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'status': "status_example", // String | 
  'cvxCode': "cvxCode_example", // String | 
  'since': "since_example", // String | 
  'doctor': 56 // Number | 
};
apiInstance.inventoryVaccinesCreate(opts, (error, data, response) => {
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
 **status** | **String**|  | [optional] 
 **cvxCode** | **String**|  | [optional] 
 **since** | **String**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**InventoryVaccine**](InventoryVaccine.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## inventoryVaccinesList

> InventoryVaccinesList200Response inventoryVaccinesList(opts)



Retrieve or search vaccine inventories

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'status': "status_example", // String | 
  'cvxCode': "cvxCode_example", // String | 
  'since': "since_example", // String | 
  'doctor': 56 // Number | 
};
apiInstance.inventoryVaccinesList(opts, (error, data, response) => {
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
 **status** | **String**|  | [optional] 
 **cvxCode** | **String**|  | [optional] 
 **since** | **String**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**InventoryVaccinesList200Response**](InventoryVaccinesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## inventoryVaccinesRead

> InventoryVaccine inventoryVaccinesRead(id, opts)



Retrieve an existing vaccine inventory

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'status': "status_example", // String | 
  'cvxCode': "cvxCode_example", // String | 
  'since': "since_example", // String | 
  'doctor': 56 // Number | 
};
apiInstance.inventoryVaccinesRead(id, opts, (error, data, response) => {
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
 **status** | **String**|  | [optional] 
 **cvxCode** | **String**|  | [optional] 
 **since** | **String**|  | [optional] 
 **doctor** | **Number**|  | [optional] 

### Return type

[**InventoryVaccine**](InventoryVaccine.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## messagesCreate

> DoctorMessage messagesCreate(opts)



Create messages in doctor&#39;s message center

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'patient': 56, // Number | 
  'doctor': 56, // Number | 
  'responsibleUser': 56, // Number | 
  'updatedSince': "updatedSince_example", // String | 
  'receivedSince': "receivedSince_example", // String | 
  'owner': 56, // Number | 
  'type': "type_example" // String | 
};
apiInstance.messagesCreate(opts, (error, data, response) => {
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
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **responsibleUser** | **Number**|  | [optional] 
 **updatedSince** | **String**|  | [optional] 
 **receivedSince** | **String**|  | [optional] 
 **owner** | **Number**|  | [optional] 
 **type** | **String**|  | [optional] 

### Return type

[**DoctorMessage**](DoctorMessage.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## messagesDelete

> messagesDelete(id, opts)



Delete an existing message in doctor&#39;s message center

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'patient': 56, // Number | 
  'doctor': 56, // Number | 
  'responsibleUser': 56, // Number | 
  'updatedSince': "updatedSince_example", // String | 
  'receivedSince': "receivedSince_example", // String | 
  'owner': 56, // Number | 
  'type': "type_example" // String | 
};
apiInstance.messagesDelete(id, opts, (error, data, response) => {
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
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **responsibleUser** | **Number**|  | [optional] 
 **updatedSince** | **String**|  | [optional] 
 **receivedSince** | **String**|  | [optional] 
 **owner** | **Number**|  | [optional] 
 **type** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## messagesList

> MessagesList200Response messagesList(opts)



Retrieve or search messages in doctor&#39;s message center

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'patient': 56, // Number | 
  'doctor': 56, // Number | 
  'responsibleUser': 56, // Number | 
  'updatedSince': "updatedSince_example", // String | 
  'receivedSince': "receivedSince_example", // String | 
  'owner': 56, // Number | 
  'type': "type_example" // String | 
};
apiInstance.messagesList(opts, (error, data, response) => {
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
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **responsibleUser** | **Number**|  | [optional] 
 **updatedSince** | **String**|  | [optional] 
 **receivedSince** | **String**|  | [optional] 
 **owner** | **Number**|  | [optional] 
 **type** | **String**|  | [optional] 

### Return type

[**MessagesList200Response**](MessagesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## messagesPartialUpdate

> messagesPartialUpdate(id, opts)



Update an existing message in doctor&#39;s message center

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'patient': 56, // Number | 
  'doctor': 56, // Number | 
  'responsibleUser': 56, // Number | 
  'updatedSince': "updatedSince_example", // String | 
  'receivedSince': "receivedSince_example", // String | 
  'owner': 56, // Number | 
  'type': "type_example" // String | 
};
apiInstance.messagesPartialUpdate(id, opts, (error, data, response) => {
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
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **responsibleUser** | **Number**|  | [optional] 
 **updatedSince** | **String**|  | [optional] 
 **receivedSince** | **String**|  | [optional] 
 **owner** | **Number**|  | [optional] 
 **type** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## messagesRead

> DoctorMessage messagesRead(id, opts)



Retrieve an existing message in doctor&#39;s message center

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'patient': 56, // Number | 
  'doctor': 56, // Number | 
  'responsibleUser': 56, // Number | 
  'updatedSince': "updatedSince_example", // String | 
  'receivedSince': "receivedSince_example", // String | 
  'owner': 56, // Number | 
  'type': "type_example" // String | 
};
apiInstance.messagesRead(id, opts, (error, data, response) => {
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
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **responsibleUser** | **Number**|  | [optional] 
 **updatedSince** | **String**|  | [optional] 
 **receivedSince** | **String**|  | [optional] 
 **owner** | **Number**|  | [optional] 
 **type** | **String**|  | [optional] 

### Return type

[**DoctorMessage**](DoctorMessage.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## messagesUpdate

> messagesUpdate(id, opts)



Update an existing message in doctor&#39;s message center

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'patient': 56, // Number | 
  'doctor': 56, // Number | 
  'responsibleUser': 56, // Number | 
  'updatedSince': "updatedSince_example", // String | 
  'receivedSince': "receivedSince_example", // String | 
  'owner': 56, // Number | 
  'type': "type_example" // String | 
};
apiInstance.messagesUpdate(id, opts, (error, data, response) => {
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
 **patient** | **Number**|  | [optional] 
 **doctor** | **Number**|  | [optional] 
 **responsibleUser** | **Number**|  | [optional] 
 **updatedSince** | **String**|  | [optional] 
 **receivedSince** | **String**|  | [optional] 
 **owner** | **Number**|  | [optional] 
 **type** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## officesAddExamRoom

> Office officesAddExamRoom(id, opts)



Add an exam room to the office

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'doctor': 56 // Number | 
};
apiInstance.officesAddExamRoom(id, opts, (error, data, response) => {
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

[**Office**](Office.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## officesList

> OfficesList200Response officesList(opts)



Retrieve or search offices

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'doctor': 56 // Number | 
};
apiInstance.officesList(opts, (error, data, response) => {
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

[**OfficesList200Response**](OfficesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## officesPartialUpdate

> officesPartialUpdate(id, opts)



Update an existing office

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'doctor': 56 // Number | 
};
apiInstance.officesPartialUpdate(id, opts, (error, data, response) => {
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
 **doctor** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## officesRead

> Office officesRead(id, opts)



Retrieve an existing office

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'doctor': 56 // Number | 
};
apiInstance.officesRead(id, opts, (error, data, response) => {
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

[**Office**](Office.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## officesUpdate

> officesUpdate(id, opts)



Update an existing office

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'doctor': 56 // Number | 
};
apiInstance.officesUpdate(id, opts, (error, data, response) => {
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
 **doctor** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## taskCategoriesCreate

> TaskCategory taskCategoriesCreate(opts)



Create a task category

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'since': "since_example" // String | 
};
apiInstance.taskCategoriesCreate(opts, (error, data, response) => {
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

### Return type

[**TaskCategory**](TaskCategory.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskCategoriesList

> TaskCategoriesList200Response taskCategoriesList(opts)



Retrieve or search task categories

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'since': "since_example" // String | 
};
apiInstance.taskCategoriesList(opts, (error, data, response) => {
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

### Return type

[**TaskCategoriesList200Response**](TaskCategoriesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskCategoriesPartialUpdate

> taskCategoriesPartialUpdate(id, opts)



Update an existing task category

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example" // String | 
};
apiInstance.taskCategoriesPartialUpdate(id, opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## taskCategoriesRead

> TaskCategory taskCategoriesRead(id, opts)



Retrieve an existing task category

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example" // String | 
};
apiInstance.taskCategoriesRead(id, opts, (error, data, response) => {
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

### Return type

[**TaskCategory**](TaskCategory.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskCategoriesUpdate

> taskCategoriesUpdate(id, opts)



Update an existing task category

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example" // String | 
};
apiInstance.taskCategoriesUpdate(id, opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## taskNotesCreate

> TaskNote taskNotesCreate(opts)



Create a task note

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'task': 56, // Number | 
  'since': "since_example" // String | 
};
apiInstance.taskNotesCreate(opts, (error, data, response) => {
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
 **task** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 

### Return type

[**TaskNote**](TaskNote.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskNotesList

> TaskNotesList200Response taskNotesList(opts)



Retrieve or search task notes

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'task': 56, // Number | 
  'since': "since_example" // String | 
};
apiInstance.taskNotesList(opts, (error, data, response) => {
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
 **task** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 

### Return type

[**TaskNotesList200Response**](TaskNotesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskNotesPartialUpdate

> taskNotesPartialUpdate(id, opts)



Update an existing task note

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'task': 56, // Number | 
  'since': "since_example" // String | 
};
apiInstance.taskNotesPartialUpdate(id, opts, (error, data, response) => {
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
 **task** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## taskNotesRead

> TaskNote taskNotesRead(id, opts)



Retrieve an existing task note

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'task': 56, // Number | 
  'since': "since_example" // String | 
};
apiInstance.taskNotesRead(id, opts, (error, data, response) => {
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
 **task** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 

### Return type

[**TaskNote**](TaskNote.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskNotesUpdate

> taskNotesUpdate(id, opts)



Update an existing task note

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'task': 56, // Number | 
  'since': "since_example" // String | 
};
apiInstance.taskNotesUpdate(id, opts, (error, data, response) => {
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
 **task** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## taskStatusesCreate

> TaskStatus taskStatusesCreate(opts)



Create a task status

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'since': "since_example" // String | 
};
apiInstance.taskStatusesCreate(opts, (error, data, response) => {
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

### Return type

[**TaskStatus**](TaskStatus.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskStatusesList

> TaskStatusesList200Response taskStatusesList(opts)



Retrieve or search task statuses

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'since': "since_example" // String | 
};
apiInstance.taskStatusesList(opts, (error, data, response) => {
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

### Return type

[**TaskStatusesList200Response**](TaskStatusesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskStatusesPartialUpdate

> taskStatusesPartialUpdate(id, opts)



Update an existing task status

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example" // String | 
};
apiInstance.taskStatusesPartialUpdate(id, opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## taskStatusesRead

> TaskStatus taskStatusesRead(id, opts)



Retrieve an existing task status

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example" // String | 
};
apiInstance.taskStatusesRead(id, opts, (error, data, response) => {
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

### Return type

[**TaskStatus**](TaskStatus.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskStatusesUpdate

> taskStatusesUpdate(id, opts)



Update an existing task status

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'since': "since_example" // String | 
};
apiInstance.taskStatusesUpdate(id, opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## taskTemplatesCreate

> TaskTemplate taskTemplatesCreate(opts)



Create a task template

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'assigneeUser': 56, // Number | 
  'status': 56, // Number | 
  'assigneeGroup': 56, // Number | 
  'since': "since_example", // String | 
  'category': 56 // Number | 
};
apiInstance.taskTemplatesCreate(opts, (error, data, response) => {
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
 **assigneeUser** | **Number**|  | [optional] 
 **status** | **Number**|  | [optional] 
 **assigneeGroup** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **category** | **Number**|  | [optional] 

### Return type

[**TaskTemplate**](TaskTemplate.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskTemplatesList

> TaskTemplatesList200Response taskTemplatesList(opts)



Retrieve or search task templates

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'assigneeUser': 56, // Number | 
  'status': 56, // Number | 
  'assigneeGroup': 56, // Number | 
  'since': "since_example", // String | 
  'category': 56 // Number | 
};
apiInstance.taskTemplatesList(opts, (error, data, response) => {
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
 **assigneeUser** | **Number**|  | [optional] 
 **status** | **Number**|  | [optional] 
 **assigneeGroup** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **category** | **Number**|  | [optional] 

### Return type

[**TaskTemplatesList200Response**](TaskTemplatesList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskTemplatesPartialUpdate

> taskTemplatesPartialUpdate(id, opts)



Update an existing task template

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'assigneeUser': 56, // Number | 
  'status': 56, // Number | 
  'assigneeGroup': 56, // Number | 
  'since': "since_example", // String | 
  'category': 56 // Number | 
};
apiInstance.taskTemplatesPartialUpdate(id, opts, (error, data, response) => {
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
 **assigneeUser** | **Number**|  | [optional] 
 **status** | **Number**|  | [optional] 
 **assigneeGroup** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **category** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## taskTemplatesRead

> TaskTemplate taskTemplatesRead(id, opts)



Retrieve an existing task template

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'assigneeUser': 56, // Number | 
  'status': 56, // Number | 
  'assigneeGroup': 56, // Number | 
  'since': "since_example", // String | 
  'category': 56 // Number | 
};
apiInstance.taskTemplatesRead(id, opts, (error, data, response) => {
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
 **assigneeUser** | **Number**|  | [optional] 
 **status** | **Number**|  | [optional] 
 **assigneeGroup** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **category** | **Number**|  | [optional] 

### Return type

[**TaskTemplate**](TaskTemplate.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taskTemplatesUpdate

> taskTemplatesUpdate(id, opts)



Update an existing task template

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'assigneeUser': 56, // Number | 
  'status': 56, // Number | 
  'assigneeGroup': 56, // Number | 
  'since': "since_example", // String | 
  'category': 56 // Number | 
};
apiInstance.taskTemplatesUpdate(id, opts, (error, data, response) => {
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
 **assigneeUser** | **Number**|  | [optional] 
 **status** | **Number**|  | [optional] 
 **assigneeGroup** | **Number**|  | [optional] 
 **since** | **String**|  | [optional] 
 **category** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tasksCreate

> Task tasksCreate(opts)



Create a task

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'status': 56, // Number | 
  'category': 56, // Number | 
  'dueAtDate': "dueAtDate_example", // String | 
  'dueAtUnknown': "dueAtUnknown_example", // String | 
  'since': "since_example", // String | 
  'dueAtSince': "dueAtSince_example", // String | 
  'assigneeUser': 56, // Number | 
  'assigneeGroup': 56, // Number | 
  'dueAtRange': "dueAtRange_example" // String | 
};
apiInstance.tasksCreate(opts, (error, data, response) => {
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
 **status** | **Number**|  | [optional] 
 **category** | **Number**|  | [optional] 
 **dueAtDate** | **String**|  | [optional] 
 **dueAtUnknown** | **String**|  | [optional] 
 **since** | **String**|  | [optional] 
 **dueAtSince** | **String**|  | [optional] 
 **assigneeUser** | **Number**|  | [optional] 
 **assigneeGroup** | **Number**|  | [optional] 
 **dueAtRange** | **String**|  | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksList

> TasksList200Response tasksList(opts)



Retrieve or search tasks

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'pageSize': 56, // Number | 
  'status': 56, // Number | 
  'category': 56, // Number | 
  'dueAtDate': "dueAtDate_example", // String | 
  'dueAtUnknown': "dueAtUnknown_example", // String | 
  'since': "since_example", // String | 
  'dueAtSince': "dueAtSince_example", // String | 
  'assigneeUser': 56, // Number | 
  'assigneeGroup': 56, // Number | 
  'dueAtRange': "dueAtRange_example" // String | 
};
apiInstance.tasksList(opts, (error, data, response) => {
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
 **status** | **Number**|  | [optional] 
 **category** | **Number**|  | [optional] 
 **dueAtDate** | **String**|  | [optional] 
 **dueAtUnknown** | **String**|  | [optional] 
 **since** | **String**|  | [optional] 
 **dueAtSince** | **String**|  | [optional] 
 **assigneeUser** | **Number**|  | [optional] 
 **assigneeGroup** | **Number**|  | [optional] 
 **dueAtRange** | **String**|  | [optional] 

### Return type

[**TasksList200Response**](TasksList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksPartialUpdate

> tasksPartialUpdate(id, opts)



Update an existing task

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'status': 56, // Number | 
  'category': 56, // Number | 
  'dueAtDate': "dueAtDate_example", // String | 
  'dueAtUnknown': "dueAtUnknown_example", // String | 
  'since': "since_example", // String | 
  'dueAtSince': "dueAtSince_example", // String | 
  'assigneeUser': 56, // Number | 
  'assigneeGroup': 56, // Number | 
  'dueAtRange': "dueAtRange_example" // String | 
};
apiInstance.tasksPartialUpdate(id, opts, (error, data, response) => {
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
 **status** | **Number**|  | [optional] 
 **category** | **Number**|  | [optional] 
 **dueAtDate** | **String**|  | [optional] 
 **dueAtUnknown** | **String**|  | [optional] 
 **since** | **String**|  | [optional] 
 **dueAtSince** | **String**|  | [optional] 
 **assigneeUser** | **Number**|  | [optional] 
 **assigneeGroup** | **Number**|  | [optional] 
 **dueAtRange** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tasksRead

> Task tasksRead(id, opts)



Retrieve an existing task

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'status': 56, // Number | 
  'category': 56, // Number | 
  'dueAtDate': "dueAtDate_example", // String | 
  'dueAtUnknown': "dueAtUnknown_example", // String | 
  'since': "since_example", // String | 
  'dueAtSince': "dueAtSince_example", // String | 
  'assigneeUser': 56, // Number | 
  'assigneeGroup': 56, // Number | 
  'dueAtRange': "dueAtRange_example" // String | 
};
apiInstance.tasksRead(id, opts, (error, data, response) => {
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
 **status** | **Number**|  | [optional] 
 **category** | **Number**|  | [optional] 
 **dueAtDate** | **String**|  | [optional] 
 **dueAtUnknown** | **String**|  | [optional] 
 **since** | **String**|  | [optional] 
 **dueAtSince** | **String**|  | [optional] 
 **assigneeUser** | **Number**|  | [optional] 
 **assigneeGroup** | **Number**|  | [optional] 
 **dueAtRange** | **String**|  | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksUpdate

> tasksUpdate(id, opts)



Update an existing task

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';
let defaultClient = OpenapiJsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: drchrono_oauth2
let drchrono_oauth2 = defaultClient.authentications['drchrono_oauth2'];
drchrono_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OpenapiJsClient.PracticeManagementApi();
let id = "id_example"; // String | 
let opts = {
  'status': 56, // Number | 
  'category': 56, // Number | 
  'dueAtDate': "dueAtDate_example", // String | 
  'dueAtUnknown': "dueAtUnknown_example", // String | 
  'since': "since_example", // String | 
  'dueAtSince': "dueAtSince_example", // String | 
  'assigneeUser': 56, // Number | 
  'assigneeGroup': 56, // Number | 
  'dueAtRange': "dueAtRange_example" // String | 
};
apiInstance.tasksUpdate(id, opts, (error, data, response) => {
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
 **status** | **Number**|  | [optional] 
 **category** | **Number**|  | [optional] 
 **dueAtDate** | **String**|  | [optional] 
 **dueAtUnknown** | **String**|  | [optional] 
 **since** | **String**|  | [optional] 
 **dueAtSince** | **String**|  | [optional] 
 **assigneeUser** | **Number**|  | [optional] 
 **assigneeGroup** | **Number**|  | [optional] 
 **dueAtRange** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

