# RegistrationAssignmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registrationAssignmentsCreateOrUpdate**](RegistrationAssignmentsApi.md#registrationAssignmentsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.ManagedServices/registrationAssignments/{registrationAssignmentId} |  |
| [**registrationAssignmentsDelete**](RegistrationAssignmentsApi.md#registrationAssignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.ManagedServices/registrationAssignments/{registrationAssignmentId} |  |
| [**registrationAssignmentsGet**](RegistrationAssignmentsApi.md#registrationAssignmentsGet) | **GET** /{scope}/providers/Microsoft.ManagedServices/registrationAssignments/{registrationAssignmentId} |  |
| [**registrationAssignmentsList**](RegistrationAssignmentsApi.md#registrationAssignmentsList) | **GET** /{scope}/providers/Microsoft.ManagedServices/registrationAssignments |  |


<a id="registrationAssignmentsCreateOrUpdate"></a>
# **registrationAssignmentsCreateOrUpdate**
> RegistrationAssignment registrationAssignmentsCreateOrUpdate(scope, registrationAssignmentId, apiVersion, requestBody)



Creates or updates a registration assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationAssignmentsApi apiInstance = new RegistrationAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | Scope of the resource.
    String registrationAssignmentId = "registrationAssignmentId_example"; // String | Guid of the registration assignment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    RegistrationAssignment requestBody = new RegistrationAssignment(); // RegistrationAssignment | The parameters required to create new registration assignment.
    try {
      RegistrationAssignment result = apiInstance.registrationAssignmentsCreateOrUpdate(scope, registrationAssignmentId, apiVersion, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationAssignmentsApi#registrationAssignmentsCreateOrUpdate");
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
| **scope** | **String**| Scope of the resource. | |
| **registrationAssignmentId** | **String**| Guid of the registration assignment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **requestBody** | [**RegistrationAssignment**](RegistrationAssignment.md)| The parameters required to create new registration assignment. | |

### Return type

[**RegistrationAssignment**](RegistrationAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok - Returns information about the updated registration assignment. |  -  |
| **201** | Created - Returns information about the created registration assignment. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="registrationAssignmentsDelete"></a>
# **registrationAssignmentsDelete**
> registrationAssignmentsDelete(scope, registrationAssignmentId, apiVersion)



Deletes the specified registration assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationAssignmentsApi apiInstance = new RegistrationAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | Scope of the resource.
    String registrationAssignmentId = "registrationAssignmentId_example"; // String | Guid of the registration assignment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    try {
      apiInstance.registrationAssignmentsDelete(scope, registrationAssignmentId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationAssignmentsApi#registrationAssignmentsDelete");
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
| **scope** | **String**| Scope of the resource. | |
| **registrationAssignmentId** | **String**| Guid of the registration assignment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - The registration assignment is deleted. |  -  |
| **202** | Accepted - The registration assignment deletion operation is accepted. |  -  |
| **204** | No Content- The registration assignment does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="registrationAssignmentsGet"></a>
# **registrationAssignmentsGet**
> RegistrationAssignment registrationAssignmentsGet(scope, registrationAssignmentId, apiVersion, $expandRegistrationDefinition)



Gets the details of specified registration assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationAssignmentsApi apiInstance = new RegistrationAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | Scope of the resource.
    String registrationAssignmentId = "registrationAssignmentId_example"; // String | Guid of the registration assignment.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    Boolean $expandRegistrationDefinition = true; // Boolean | Tells whether to return registration definition details also along with registration assignment details.
    try {
      RegistrationAssignment result = apiInstance.registrationAssignmentsGet(scope, registrationAssignmentId, apiVersion, $expandRegistrationDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationAssignmentsApi#registrationAssignmentsGet");
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
| **scope** | **String**| Scope of the resource. | |
| **registrationAssignmentId** | **String**| Guid of the registration assignment. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$expandRegistrationDefinition** | **Boolean**| Tells whether to return registration definition details also along with registration assignment details. | [optional] |

### Return type

[**RegistrationAssignment**](RegistrationAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns the registration assignment. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="registrationAssignmentsList"></a>
# **registrationAssignmentsList**
> RegistrationAssignmentList registrationAssignmentsList(scope, apiVersion, $expandRegistrationDefinition)



Gets a list of the registration assignments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegistrationAssignmentsApi apiInstance = new RegistrationAssignmentsApi(defaultClient);
    String scope = "scope_example"; // String | Scope of the resource.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    Boolean $expandRegistrationDefinition = true; // Boolean | Tells whether to return registration definition details also along with registration assignment details.
    try {
      RegistrationAssignmentList result = apiInstance.registrationAssignmentsList(scope, apiVersion, $expandRegistrationDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationAssignmentsApi#registrationAssignmentsList");
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
| **scope** | **String**| Scope of the resource. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$expandRegistrationDefinition** | **Boolean**| Tells whether to return registration definition details also along with registration assignment details. | [optional] |

### Return type

[**RegistrationAssignmentList**](RegistrationAssignmentList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns a list of the registration assignments. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

