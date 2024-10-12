# AssignmentApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignmentsCreateOrUpdate**](AssignmentApi.md#assignmentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName} |  |
| [**assignmentsDelete**](AssignmentApi.md#assignmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName} |  |
| [**assignmentsGet**](AssignmentApi.md#assignmentsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Blueprint/blueprintAssignments/{assignmentName} |  |
| [**assignmentsList**](AssignmentApi.md#assignmentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Blueprint/blueprintAssignments |  |


<a id="assignmentsCreateOrUpdate"></a>
# **assignmentsCreateOrUpdate**
> Assignment assignmentsCreateOrUpdate(apiVersion, subscriptionId, assignmentName, assignment)



Create or update a Blueprint assignment.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | azure subscriptionId, which we assign the blueprint to.
    String assignmentName = "assignmentName_example"; // String | name of the assignment.
    Assignment assignment = new Assignment(); // Assignment | assignment object to save.
    try {
      Assignment result = apiInstance.assignmentsCreateOrUpdate(apiVersion, subscriptionId, assignmentName, assignment);
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| azure subscriptionId, which we assign the blueprint to. | |
| **assignmentName** | **String**| name of the assignment. | |
| **assignment** | [**Assignment**](Assignment.md)| assignment object to save. | |

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
| **201** | Created - Blueprint assignment saved |  -  |

<a id="assignmentsDelete"></a>
# **assignmentsDelete**
> Assignment assignmentsDelete(apiVersion, subscriptionId, assignmentName)



Delete a Blueprint assignment.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | azure subscriptionId, which we assign the blueprint to.
    String assignmentName = "assignmentName_example"; // String | name of the assignment.
    try {
      Assignment result = apiInstance.assignmentsDelete(apiVersion, subscriptionId, assignmentName);
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| azure subscriptionId, which we assign the blueprint to. | |
| **assignmentName** | **String**| name of the assignment. | |

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
| **202** | OK - Blueprint assignment deleted. |  -  |
| **204** | no content |  -  |

<a id="assignmentsGet"></a>
# **assignmentsGet**
> Assignment assignmentsGet(apiVersion, subscriptionId, assignmentName)



Get a Blueprint assignment.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | azure subscriptionId, which we assign the blueprint to.
    String assignmentName = "assignmentName_example"; // String | name of the assignment.
    try {
      Assignment result = apiInstance.assignmentsGet(apiVersion, subscriptionId, assignmentName);
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| azure subscriptionId, which we assign the blueprint to. | |
| **assignmentName** | **String**| name of the assignment. | |

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
| **200** | OK - Blueprint assignment retrieved. |  -  |

<a id="assignmentsList"></a>
# **assignmentsList**
> AssignmentList assignmentsList(apiVersion, subscriptionId)



List Blueprint assignments within a subscription.

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
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | azure subscriptionId, which we assign the blueprint to.
    try {
      AssignmentList result = apiInstance.assignmentsList(apiVersion, subscriptionId);
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| azure subscriptionId, which we assign the blueprint to. | |

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
| **200** | OK - all Blueprint assignment retrieved. |  -  |

