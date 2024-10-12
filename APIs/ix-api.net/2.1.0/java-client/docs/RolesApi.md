# RolesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rolesList**](RolesApi.md#rolesList) | **GET** /roles |  |
| [**rolesRead**](RolesApi.md#rolesRead) | **GET** /roles/{id} |  |


<a id="rolesList"></a>
# **rolesList**
> List&lt;Role&gt; rolesList(id, name, contact)



List all roles available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String name = "name_example"; // String | Filter by name
    String contact = "contact_example"; // String | Filter by contact
    try {
      List<Role> result = apiInstance.rolesList(id, name, contact);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#rolesList");
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
| **name** | **String**| Filter by name | [optional] |
| **contact** | **String**| Filter by contact | [optional] |

### Return type

[**List&lt;Role&gt;**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: A role for a contact |  -  |
| **401** | Authentication |  -  |

<a id="rolesRead"></a>
# **rolesRead**
> Role rolesRead(id, id2, name)



Get a single &#x60;Role&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String id = "id_example"; // String | Get by id
    List<String> id2 = Arrays.asList(); // List<String> | Filter by id
    String name = "name_example"; // String | Filter by name
    try {
      Role result = apiInstance.rolesRead(id, id2, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#rolesRead");
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
| **id** | **String**| Get by id | |
| **id2** | [**List&lt;String&gt;**](String.md)| Filter by id | [optional] |
| **name** | **String**| Filter by name | [optional] |

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A role for a contact |  -  |
| **401** | Authentication |  -  |

