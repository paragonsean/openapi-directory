# V1EmployeesApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEmployee**](V1EmployeesApi.md#createEmployee) | **POST** /v1/me/employees | CreateEmployee |
| [**createEmployeeRole**](V1EmployeesApi.md#createEmployeeRole) | **POST** /v1/me/roles | CreateEmployeeRole |
| [**listEmployeeRoles**](V1EmployeesApi.md#listEmployeeRoles) | **GET** /v1/me/roles | ListEmployeeRoles |
| [**listEmployees**](V1EmployeesApi.md#listEmployees) | **GET** /v1/me/employees | ListEmployees |
| [**retrieveEmployee**](V1EmployeesApi.md#retrieveEmployee) | **GET** /v1/me/employees/{employee_id} | RetrieveEmployee |
| [**retrieveEmployeeRole**](V1EmployeesApi.md#retrieveEmployeeRole) | **GET** /v1/me/roles/{role_id} | RetrieveEmployeeRole |
| [**updateEmployee**](V1EmployeesApi.md#updateEmployee) | **PUT** /v1/me/employees/{employee_id} | UpdateEmployee |
| [**updateEmployeeRole**](V1EmployeesApi.md#updateEmployeeRole) | **PUT** /v1/me/roles/{role_id} | UpdateEmployeeRole |


<a id="createEmployee"></a>
# **createEmployee**
> V1Employee createEmployee(v1Employee)

CreateEmployee

 Use the CreateEmployee endpoint to add an employee to a Square account. Employees created with the Connect API have an initial status of &#x60;INACTIVE&#x60;. Inactive employees cannot sign in to Square Point of Sale until they are activated from the Square Dashboard. Employee status cannot be changed with the Connect API.  Employee entities cannot be deleted. To disable employee profiles, set the employee&#39;s status to &lt;code&gt;INACTIVE&lt;/code&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EmployeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1EmployeesApi apiInstance = new V1EmployeesApi(defaultClient);
    V1Employee v1Employee = new V1Employee(); // V1Employee | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      V1Employee result = apiInstance.createEmployee(v1Employee);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EmployeesApi#createEmployee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **v1Employee** | [**V1Employee**](V1Employee.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="createEmployeeRole"></a>
# **createEmployeeRole**
> V1EmployeeRole createEmployeeRole(v1EmployeeRole)

CreateEmployeeRole

Creates an employee role you can then assign to employees.  Square accounts can include any number of roles that can be assigned to employees. These roles define the actions and permissions granted to an employee with that role. For example, an employee with a \&quot;Shift Manager\&quot; role might be able to issue refunds in Square Point of Sale, whereas an employee with a \&quot;Clerk\&quot; role might not.  Roles are assigned with the [V1UpdateEmployee](https://developer.squareup.com/reference/square_2021-08-18/v1-employees-api/update-employee-role) endpoint. An employee can have only one role at a time.  If an employee has no role, they have none of the permissions associated with roles. All employees can accept payments with Square Point of Sale.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EmployeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1EmployeesApi apiInstance = new V1EmployeesApi(defaultClient);
    V1EmployeeRole v1EmployeeRole = new V1EmployeeRole(); // V1EmployeeRole | An EmployeeRole object with a name and permissions, and an optional owner flag.
    try {
      V1EmployeeRole result = apiInstance.createEmployeeRole(v1EmployeeRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EmployeesApi#createEmployeeRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **v1EmployeeRole** | [**V1EmployeeRole**](V1EmployeeRole.md)| An EmployeeRole object with a name and permissions, and an optional owner flag. | |

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listEmployeeRoles"></a>
# **listEmployeeRoles**
> List&lt;V1EmployeeRole&gt; listEmployeeRoles(order, limit, batchToken)

ListEmployeeRoles

Provides summary information for all of a business&#39;s employee roles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EmployeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1EmployeesApi apiInstance = new V1EmployeesApi(defaultClient);
    String order = "order_example"; // String | The order in which employees are listed in the response, based on their created_at field.Default value: ASC
    Integer limit = 56; // Integer | The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.
    String batchToken = "batchToken_example"; // String | A pagination cursor to retrieve the next set of results for your original query to the endpoint.
    try {
      List<V1EmployeeRole> result = apiInstance.listEmployeeRoles(order, limit, batchToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EmployeesApi#listEmployeeRoles");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **order** | **String**| The order in which employees are listed in the response, based on their created_at field.Default value: ASC | [optional] |
| **limit** | **Integer**| The maximum integer number of employee entities to return in a single response. Default 100, maximum 200. | [optional] |
| **batchToken** | **String**| A pagination cursor to retrieve the next set of results for your original query to the endpoint. | [optional] |

### Return type

[**List&lt;V1EmployeeRole&gt;**](V1EmployeeRole.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listEmployees"></a>
# **listEmployees**
> List&lt;V1Employee&gt; listEmployees(order, beginUpdatedAt, endUpdatedAt, beginCreatedAt, endCreatedAt, status, externalId, limit, batchToken)

ListEmployees

Provides summary information for all of a business&#39;s employees.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EmployeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1EmployeesApi apiInstance = new V1EmployeesApi(defaultClient);
    String order = "order_example"; // String | The order in which employees are listed in the response, based on their created_at field.      Default value: ASC
    String beginUpdatedAt = "beginUpdatedAt_example"; // String | If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format
    String endUpdatedAt = "endUpdatedAt_example"; // String | If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format.
    String beginCreatedAt = "beginCreatedAt_example"; // String | If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format.
    String endCreatedAt = "endCreatedAt_example"; // String | If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format.
    String status = "status_example"; // String | If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE).
    String externalId = "externalId_example"; // String | If provided, the endpoint returns only employee entities with the specified external_id.
    Integer limit = 56; // Integer | The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.
    String batchToken = "batchToken_example"; // String | A pagination cursor to retrieve the next set of results for your original query to the endpoint.
    try {
      List<V1Employee> result = apiInstance.listEmployees(order, beginUpdatedAt, endUpdatedAt, beginCreatedAt, endCreatedAt, status, externalId, limit, batchToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EmployeesApi#listEmployees");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **order** | **String**| The order in which employees are listed in the response, based on their created_at field.      Default value: ASC | [optional] |
| **beginUpdatedAt** | **String**| If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format | [optional] |
| **endUpdatedAt** | **String**| If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format. | [optional] |
| **beginCreatedAt** | **String**| If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format. | [optional] |
| **endCreatedAt** | **String**| If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format. | [optional] |
| **status** | **String**| If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE). | [optional] |
| **externalId** | **String**| If provided, the endpoint returns only employee entities with the specified external_id. | [optional] |
| **limit** | **Integer**| The maximum integer number of employee entities to return in a single response. Default 100, maximum 200. | [optional] |
| **batchToken** | **String**| A pagination cursor to retrieve the next set of results for your original query to the endpoint. | [optional] |

### Return type

[**List&lt;V1Employee&gt;**](V1Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveEmployee"></a>
# **retrieveEmployee**
> V1Employee retrieveEmployee(employeeId)

RetrieveEmployee

Provides the details for a single employee.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EmployeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1EmployeesApi apiInstance = new V1EmployeesApi(defaultClient);
    String employeeId = "employeeId_example"; // String | The employee's ID.
    try {
      V1Employee result = apiInstance.retrieveEmployee(employeeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EmployeesApi#retrieveEmployee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **employeeId** | **String**| The employee&#39;s ID. | |

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveEmployeeRole"></a>
# **retrieveEmployeeRole**
> V1EmployeeRole retrieveEmployeeRole(roleId)

RetrieveEmployeeRole

Provides the details for a single employee role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EmployeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1EmployeesApi apiInstance = new V1EmployeesApi(defaultClient);
    String roleId = "roleId_example"; // String | The role's ID.
    try {
      V1EmployeeRole result = apiInstance.retrieveEmployeeRole(roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EmployeesApi#retrieveEmployeeRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **roleId** | **String**| The role&#39;s ID. | |

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateEmployee"></a>
# **updateEmployee**
> V1Employee updateEmployee(employeeId, v1Employee)

UpdateEmployee



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EmployeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1EmployeesApi apiInstance = new V1EmployeesApi(defaultClient);
    String employeeId = "employeeId_example"; // String | The ID of the role to modify.
    V1Employee v1Employee = new V1Employee(); // V1Employee | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      V1Employee result = apiInstance.updateEmployee(employeeId, v1Employee);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EmployeesApi#updateEmployee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **employeeId** | **String**| The ID of the role to modify. | |
| **v1Employee** | [**V1Employee**](V1Employee.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**V1Employee**](V1Employee.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateEmployeeRole"></a>
# **updateEmployeeRole**
> V1EmployeeRole updateEmployeeRole(roleId, v1EmployeeRole)

UpdateEmployeeRole

Modifies the details of an employee role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1EmployeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1EmployeesApi apiInstance = new V1EmployeesApi(defaultClient);
    String roleId = "roleId_example"; // String | The ID of the role to modify.
    V1EmployeeRole v1EmployeeRole = new V1EmployeeRole(); // V1EmployeeRole | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      V1EmployeeRole result = apiInstance.updateEmployeeRole(roleId, v1EmployeeRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1EmployeesApi#updateEmployeeRole");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **roleId** | **String**| The ID of the role to modify. | |
| **v1EmployeeRole** | [**V1EmployeeRole**](V1EmployeeRole.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**V1EmployeeRole**](V1EmployeeRole.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

