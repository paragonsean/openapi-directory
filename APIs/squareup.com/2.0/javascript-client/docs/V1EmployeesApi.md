# SquareConnectApi.V1EmployeesApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEmployee**](V1EmployeesApi.md#createEmployee) | **POST** /v1/me/employees | CreateEmployee
[**createEmployeeRole**](V1EmployeesApi.md#createEmployeeRole) | **POST** /v1/me/roles | CreateEmployeeRole
[**listEmployeeRoles**](V1EmployeesApi.md#listEmployeeRoles) | **GET** /v1/me/roles | ListEmployeeRoles
[**listEmployees**](V1EmployeesApi.md#listEmployees) | **GET** /v1/me/employees | ListEmployees
[**retrieveEmployee**](V1EmployeesApi.md#retrieveEmployee) | **GET** /v1/me/employees/{employee_id} | RetrieveEmployee
[**retrieveEmployeeRole**](V1EmployeesApi.md#retrieveEmployeeRole) | **GET** /v1/me/roles/{role_id} | RetrieveEmployeeRole
[**updateEmployee**](V1EmployeesApi.md#updateEmployee) | **PUT** /v1/me/employees/{employee_id} | UpdateEmployee
[**updateEmployeeRole**](V1EmployeesApi.md#updateEmployeeRole) | **PUT** /v1/me/roles/{role_id} | UpdateEmployeeRole



## createEmployee

> V1Employee createEmployee(v1Employee)

CreateEmployee

 Use the CreateEmployee endpoint to add an employee to a Square account. Employees created with the Connect API have an initial status of &#x60;INACTIVE&#x60;. Inactive employees cannot sign in to Square Point of Sale until they are activated from the Square Dashboard. Employee status cannot be changed with the Connect API.  Employee entities cannot be deleted. To disable employee profiles, set the employee&#39;s status to &lt;code&gt;INACTIVE&lt;/code&gt;

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.V1EmployeesApi();
let v1Employee = new SquareConnectApi.V1Employee(); // V1Employee | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createEmployee(v1Employee, (error, data, response) => {
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
 **v1Employee** | [**V1Employee**](V1Employee.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEmployeeRole

> V1EmployeeRole createEmployeeRole(v1EmployeeRole)

CreateEmployeeRole

Creates an employee role you can then assign to employees.  Square accounts can include any number of roles that can be assigned to employees. These roles define the actions and permissions granted to an employee with that role. For example, an employee with a \&quot;Shift Manager\&quot; role might be able to issue refunds in Square Point of Sale, whereas an employee with a \&quot;Clerk\&quot; role might not.  Roles are assigned with the [V1UpdateEmployee](https://developer.squareup.com/reference/square_2021-08-18/v1-employees-api/update-employee-role) endpoint. An employee can have only one role at a time.  If an employee has no role, they have none of the permissions associated with roles. All employees can accept payments with Square Point of Sale.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.V1EmployeesApi();
let v1EmployeeRole = new SquareConnectApi.V1EmployeeRole(); // V1EmployeeRole | An EmployeeRole object with a name and permissions, and an optional owner flag.
apiInstance.createEmployeeRole(v1EmployeeRole, (error, data, response) => {
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
 **v1EmployeeRole** | [**V1EmployeeRole**](V1EmployeeRole.md)| An EmployeeRole object with a name and permissions, and an optional owner flag. | 

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listEmployeeRoles

> [V1EmployeeRole] listEmployeeRoles(opts)

ListEmployeeRoles

Provides summary information for all of a business&#39;s employee roles.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.V1EmployeesApi();
let opts = {
  'order': "order_example", // String | The order in which employees are listed in the response, based on their created_at field.Default value: ASC
  'limit': 56, // Number | The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.
  'batchToken': "batchToken_example" // String | A pagination cursor to retrieve the next set of results for your original query to the endpoint.
};
apiInstance.listEmployeeRoles(opts, (error, data, response) => {
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
 **order** | **String**| The order in which employees are listed in the response, based on their created_at field.Default value: ASC | [optional] 
 **limit** | **Number**| The maximum integer number of employee entities to return in a single response. Default 100, maximum 200. | [optional] 
 **batchToken** | **String**| A pagination cursor to retrieve the next set of results for your original query to the endpoint. | [optional] 

### Return type

[**[V1EmployeeRole]**](V1EmployeeRole.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEmployees

> [V1Employee] listEmployees(opts)

ListEmployees

Provides summary information for all of a business&#39;s employees.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.V1EmployeesApi();
let opts = {
  'order': "order_example", // String | The order in which employees are listed in the response, based on their created_at field.      Default value: ASC
  'beginUpdatedAt': "beginUpdatedAt_example", // String | If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format
  'endUpdatedAt': "endUpdatedAt_example", // String | If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format.
  'beginCreatedAt': "beginCreatedAt_example", // String | If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format.
  'endCreatedAt': "endCreatedAt_example", // String | If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format.
  'status': "status_example", // String | If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE).
  'externalId': "externalId_example", // String | If provided, the endpoint returns only employee entities with the specified external_id.
  'limit': 56, // Number | The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.
  'batchToken': "batchToken_example" // String | A pagination cursor to retrieve the next set of results for your original query to the endpoint.
};
apiInstance.listEmployees(opts, (error, data, response) => {
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
 **order** | **String**| The order in which employees are listed in the response, based on their created_at field.      Default value: ASC | [optional] 
 **beginUpdatedAt** | **String**| If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format | [optional] 
 **endUpdatedAt** | **String**| If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format. | [optional] 
 **beginCreatedAt** | **String**| If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format. | [optional] 
 **endCreatedAt** | **String**| If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format. | [optional] 
 **status** | **String**| If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE). | [optional] 
 **externalId** | **String**| If provided, the endpoint returns only employee entities with the specified external_id. | [optional] 
 **limit** | **Number**| The maximum integer number of employee entities to return in a single response. Default 100, maximum 200. | [optional] 
 **batchToken** | **String**| A pagination cursor to retrieve the next set of results for your original query to the endpoint. | [optional] 

### Return type

[**[V1Employee]**](V1Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveEmployee

> V1Employee retrieveEmployee(employeeId)

RetrieveEmployee

Provides the details for a single employee.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.V1EmployeesApi();
let employeeId = "employeeId_example"; // String | The employee's ID.
apiInstance.retrieveEmployee(employeeId, (error, data, response) => {
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
 **employeeId** | **String**| The employee&#39;s ID. | 

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveEmployeeRole

> V1EmployeeRole retrieveEmployeeRole(roleId)

RetrieveEmployeeRole

Provides the details for a single employee role.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.V1EmployeesApi();
let roleId = "roleId_example"; // String | The role's ID.
apiInstance.retrieveEmployeeRole(roleId, (error, data, response) => {
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
 **roleId** | **String**| The role&#39;s ID. | 

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateEmployee

> V1Employee updateEmployee(employeeId, v1Employee)

UpdateEmployee



### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.V1EmployeesApi();
let employeeId = "employeeId_example"; // String | The ID of the role to modify.
let v1Employee = new SquareConnectApi.V1Employee(); // V1Employee | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateEmployee(employeeId, v1Employee, (error, data, response) => {
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
 **employeeId** | **String**| The ID of the role to modify. | 
 **v1Employee** | [**V1Employee**](V1Employee.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEmployeeRole

> V1EmployeeRole updateEmployeeRole(roleId, v1EmployeeRole)

UpdateEmployeeRole

Modifies the details of an employee role.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.V1EmployeesApi();
let roleId = "roleId_example"; // String | The ID of the role to modify.
let v1EmployeeRole = new SquareConnectApi.V1EmployeeRole(); // V1EmployeeRole | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateEmployeeRole(roleId, v1EmployeeRole, (error, data, response) => {
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
 **roleId** | **String**| The ID of the role to modify. | 
 **v1EmployeeRole** | [**V1EmployeeRole**](V1EmployeeRole.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

