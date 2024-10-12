# EmployeesApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2EmployeesGet**](EmployeesApi.md#v2EmployeesGet) | **GET** /v2/employees | ListEmployees |
| [**v2EmployeesIdGet**](EmployeesApi.md#v2EmployeesIdGet) | **GET** /v2/employees/{id} | RetrieveEmployee |


<a id="v2EmployeesGet"></a>
# **v2EmployeesGet**
> ListEmployeesResponse v2EmployeesGet(locationId, status, limit, cursor)

ListEmployees



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmployeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EmployeesApi apiInstance = new EmployeesApi(defaultClient);
    String locationId = "locationId_example"; // String | 
    String status = "status_example"; // String | Specifies the EmployeeStatus to filter the employee by.
    Integer limit = 56; // Integer | The number of employees to be returned on each page.
    String cursor = "cursor_example"; // String | The token required to retrieve the specified page of results.
    try {
      ListEmployeesResponse result = apiInstance.v2EmployeesGet(locationId, status, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeesApi#v2EmployeesGet");
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
| **locationId** | **String**|  | [optional] |
| **status** | **String**| Specifies the EmployeeStatus to filter the employee by. | [optional] |
| **limit** | **Integer**| The number of employees to be returned on each page. | [optional] |
| **cursor** | **String**| The token required to retrieve the specified page of results. | [optional] |

### Return type

[**ListEmployeesResponse**](ListEmployeesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2EmployeesIdGet"></a>
# **v2EmployeesIdGet**
> RetrieveEmployeeResponse v2EmployeesIdGet(id)

RetrieveEmployee



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmployeesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EmployeesApi apiInstance = new EmployeesApi(defaultClient);
    String id = "id_example"; // String | UUID for the employee that was requested.
    try {
      RetrieveEmployeeResponse result = apiInstance.v2EmployeesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeesApi#v2EmployeesIdGet");
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
| **id** | **String**| UUID for the employee that was requested. | |

### Return type

[**RetrieveEmployeeResponse**](RetrieveEmployeeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

