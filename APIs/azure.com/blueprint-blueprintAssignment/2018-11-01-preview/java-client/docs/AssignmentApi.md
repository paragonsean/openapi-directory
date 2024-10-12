# AssignmentApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignmentsCreateOrUpdate**](AssignmentApi.md#assignmentsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName} |  |
| [**assignmentsDelete**](AssignmentApi.md#assignmentsDelete) | **DELETE** /{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName} |  |
| [**assignmentsGet**](AssignmentApi.md#assignmentsGet) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName} |  |
| [**assignmentsList**](AssignmentApi.md#assignmentsList) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprintAssignments |  |


<a id="assignmentsCreateOrUpdate"></a>
# **assignmentsCreateOrUpdate**
> Assignment assignmentsCreateOrUpdate(apiVersion, scope, assignmentName, assignment)



Create or update a blueprint assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssignmentApi apiInstance = new AssignmentApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String assignmentName = "assignmentName_example"; // String | Name of the blueprint assignment.
    Assignment assignment = new Assignment(); // Assignment | Blueprint assignment object to save.
    try {
      Assignment result = apiInstance.assignmentsCreateOrUpdate(apiVersion, scope, assignmentName, assignment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssignmentApi#assignmentsCreateOrUpdate");
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |
| **assignmentName** | **String**| Name of the blueprint assignment. | |
| **assignment** | [**Assignment**](Assignment.md)| Blueprint assignment object to save. | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created -- blueprint assignment saved. |  -  |

<a id="assignmentsDelete"></a>
# **assignmentsDelete**
> Assignment assignmentsDelete(apiVersion, scope, assignmentName)



Delete a blueprint assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssignmentApi apiInstance = new AssignmentApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String assignmentName = "assignmentName_example"; // String | Name of the blueprint assignment.
    try {
      Assignment result = apiInstance.assignmentsDelete(apiVersion, scope, assignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssignmentApi#assignmentsDelete");
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |
| **assignmentName** | **String**| Name of the blueprint assignment. | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | OK -- blueprint assignment deleted. |  -  |
| **204** | No Content |  -  |

<a id="assignmentsGet"></a>
# **assignmentsGet**
> Assignment assignmentsGet(apiVersion, scope, assignmentName)



Get a blueprint assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssignmentApi apiInstance = new AssignmentApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String assignmentName = "assignmentName_example"; // String | Name of the blueprint assignment.
    try {
      Assignment result = apiInstance.assignmentsGet(apiVersion, scope, assignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssignmentApi#assignmentsGet");
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |
| **assignmentName** | **String**| Name of the blueprint assignment. | |

### Return type

[**Assignment**](Assignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- blueprint assignment retrieved. |  -  |

<a id="assignmentsList"></a>
# **assignmentsList**
> AssignmentList assignmentsList(apiVersion, scope)



List blueprint assignments within a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssignmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssignmentApi apiInstance = new AssignmentApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    try {
      AssignmentList result = apiInstance.assignmentsList(apiVersion, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssignmentApi#assignmentsList");
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
| **apiVersion** | **String**| Client API Version. | |
| **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | |

### Return type

[**AssignmentList**](AssignmentList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- all blueprint assignments retrieved. |  -  |

