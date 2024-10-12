# AssignmentOperationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignmentOperationsGet**](AssignmentOperationsApi.md#assignmentOperationsGet) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName}/assignmentOperations/{assignmentOperationName} |  |
| [**assignmentOperationsList**](AssignmentOperationsApi.md#assignmentOperationsList) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName}/assignmentOperations |  |


<a id="assignmentOperationsGet"></a>
# **assignmentOperationsGet**
> AssignmentOperation assignmentOperationsGet(apiVersion, scope, assignmentName, assignmentOperationName)



Get a blueprint assignment operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssignmentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssignmentOperationsApi apiInstance = new AssignmentOperationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String assignmentName = "assignmentName_example"; // String | Name of the blueprint assignment.
    String assignmentOperationName = "assignmentOperationName_example"; // String | Name of the blueprint assignment operation.
    try {
      AssignmentOperation result = apiInstance.assignmentOperationsGet(apiVersion, scope, assignmentName, assignmentOperationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssignmentOperationsApi#assignmentOperationsGet");
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
| **assignmentOperationName** | **String**| Name of the blueprint assignment operation. | |

### Return type

[**AssignmentOperation**](AssignmentOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- blueprint assignment operation retrieved. |  -  |

<a id="assignmentOperationsList"></a>
# **assignmentOperationsList**
> AssignmentOperationList assignmentOperationsList(apiVersion, scope, assignmentName)



List operations for given blueprint assignment within a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssignmentOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AssignmentOperationsApi apiInstance = new AssignmentOperationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
    String assignmentName = "assignmentName_example"; // String | Name of the blueprint assignment.
    try {
      AssignmentOperationList result = apiInstance.assignmentOperationsList(apiVersion, scope, assignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssignmentOperationsApi#assignmentOperationsList");
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

[**AssignmentOperationList**](AssignmentOperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- all blueprint assignment operations retrieved. |  -  |

