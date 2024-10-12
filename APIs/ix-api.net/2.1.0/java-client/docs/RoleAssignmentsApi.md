# RoleAssignmentsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**roleAssignmentsCreate**](RoleAssignmentsApi.md#roleAssignmentsCreate) | **POST** /role-assignments |  |
| [**roleAssignmentsDestroy**](RoleAssignmentsApi.md#roleAssignmentsDestroy) | **DELETE** /role-assignments/{assignment_id} |  |
| [**roleAssignmentsList**](RoleAssignmentsApi.md#roleAssignmentsList) | **GET** /role-assignments |  |
| [**roleAssignmentsRead**](RoleAssignmentsApi.md#roleAssignmentsRead) | **GET** /role-assignments/{assignment_id} |  |


<a id="roleAssignmentsCreate"></a>
# **roleAssignmentsCreate**
> RoleAssignment roleAssignmentsCreate(roleAssignmentRequest)



Assign a &#x60;Role&#x60; to a &#x60;Contact&#x60;.  The contact needs to have all fields filled, which the role requires. If this is not the case a &#x60;400&#x60; &#x60;UnableToFulfill&#x60; will be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    RoleAssignmentRequest roleAssignmentRequest = new RoleAssignmentRequest(); // RoleAssignmentRequest | A role assignment request
    try {
      RoleAssignment result = apiInstance.roleAssignmentsCreate(roleAssignmentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsCreate");
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
| **roleAssignmentRequest** | [**RoleAssignmentRequest**](RoleAssignmentRequest.md)| A role assignment request | [optional] |

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A role assignment for a contact |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="roleAssignmentsDestroy"></a>
# **roleAssignmentsDestroy**
> RoleAssignment roleAssignmentsDestroy(assignmentId)



Remove a role assignment from a contact.  If the contact is still in use with a given role required, this will yield an &#x60;UnableToFulfill&#x60; error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String assignmentId = "assignmentId_example"; // String | Get by assignment_id
    try {
      RoleAssignment result = apiInstance.roleAssignmentsDestroy(assignmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsDestroy");
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
| **assignmentId** | **String**| Get by assignment_id | |

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A role assignment for a contact |  -  |
| **400** | UnableToFulfill |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

<a id="roleAssignmentsList"></a>
# **roleAssignmentsList**
> List&lt;RoleAssignment&gt; roleAssignmentsList(id, contact, role)



List all role assignments for a contact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String contact = "contact_example"; // String | Filter by contact
    String role = "role_example"; // String | Filter by role
    try {
      List<RoleAssignment> result = apiInstance.roleAssignmentsList(id, contact, role);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsList");
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
| **id** | [**List&lt;String&gt;**](String.md)| Filter by id | [optional] |
| **contact** | **String**| Filter by contact | [optional] |
| **role** | **String**| Filter by role | [optional] |

### Return type

[**List&lt;RoleAssignment&gt;**](RoleAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: A role assignment for a contact |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="roleAssignmentsRead"></a>
# **roleAssignmentsRead**
> RoleAssignment roleAssignmentsRead(assignmentId)



Get a role assignment for a contact.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RoleAssignmentsApi apiInstance = new RoleAssignmentsApi(defaultClient);
    String assignmentId = "assignmentId_example"; // String | Get by assignment_id
    try {
      RoleAssignment result = apiInstance.roleAssignmentsRead(assignmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleAssignmentsApi#roleAssignmentsRead");
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
| **assignmentId** | **String**| Get by assignment_id | |

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A role assignment for a contact |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

