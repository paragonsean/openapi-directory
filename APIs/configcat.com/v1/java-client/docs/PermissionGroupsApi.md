# PermissionGroupsApi

All URIs are relative to *https://api.configcat.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPermissionGroup**](PermissionGroupsApi.md#createPermissionGroup) | **POST** /v1/products/{productId}/permissions | Create Permission Group |
| [**deletePermissionGroup**](PermissionGroupsApi.md#deletePermissionGroup) | **DELETE** /v1/permissions/{permissionGroupId} | Delete Permission Group |
| [**getPermissionGroup**](PermissionGroupsApi.md#getPermissionGroup) | **GET** /v1/permissions/{permissionGroupId} | Get Permission Group |
| [**getPermissionGroups**](PermissionGroupsApi.md#getPermissionGroups) | **GET** /v1/products/{productId}/permissions | List Permission Groups |
| [**updatePermissionGroup**](PermissionGroupsApi.md#updatePermissionGroup) | **PUT** /v1/permissions/{permissionGroupId} | Update Permission Group |


<a id="createPermissionGroup"></a>
# **createPermissionGroup**
> PermissionGroupModelHaljson createPermissionGroup(productId, createPermissionGroupRequest)

Create Permission Group

This endpoint creates a new Permission Group in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    PermissionGroupsApi apiInstance = new PermissionGroupsApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | The identifier of the Product.
    CreatePermissionGroupRequest createPermissionGroupRequest = new CreatePermissionGroupRequest(); // CreatePermissionGroupRequest | 
    try {
      PermissionGroupModelHaljson result = apiInstance.createPermissionGroup(productId, createPermissionGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionGroupsApi#createPermissionGroup");
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
| **productId** | **UUID**| The identifier of the Product. | |
| **createPermissionGroupRequest** | [**CreatePermissionGroupRequest**](CreatePermissionGroupRequest.md)|  | |

### Return type

[**PermissionGroupModelHaljson**](PermissionGroupModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | When the creation was successful. |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="deletePermissionGroup"></a>
# **deletePermissionGroup**
> deletePermissionGroup(permissionGroupId)

Delete Permission Group

This endpoint removes a Permission Group identified by the &#x60;permissionGroupId&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    PermissionGroupsApi apiInstance = new PermissionGroupsApi(defaultClient);
    Long permissionGroupId = 56L; // Long | The identifier of the Permission Group.
    try {
      apiInstance.deletePermissionGroup(permissionGroupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionGroupsApi#deletePermissionGroup");
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
| **permissionGroupId** | **Long**| The identifier of the Permission Group. | |

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | When the delete was successful. |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="getPermissionGroup"></a>
# **getPermissionGroup**
> PermissionGroupModelHaljson getPermissionGroup(permissionGroupId)

Get Permission Group

This endpoint returns the metadata of a Permission Group  identified by the &#x60;permissionGroupId&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    PermissionGroupsApi apiInstance = new PermissionGroupsApi(defaultClient);
    Long permissionGroupId = 56L; // Long | The identifier of the Permission Group.
    try {
      PermissionGroupModelHaljson result = apiInstance.getPermissionGroup(permissionGroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionGroupsApi#getPermissionGroup");
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
| **permissionGroupId** | **Long**| The identifier of the Permission Group. | |

### Return type

[**PermissionGroupModelHaljson**](PermissionGroupModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | When everything is ok, the permission group data returned. |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="getPermissionGroups"></a>
# **getPermissionGroups**
> List&lt;PermissionGroupModelHaljson&gt; getPermissionGroups(productId)

List Permission Groups

This endpoint returns the list of the Permission Groups that belongs to the given Product identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    PermissionGroupsApi apiInstance = new PermissionGroupsApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | The identifier of the Product.
    try {
      List<PermissionGroupModelHaljson> result = apiInstance.getPermissionGroups(productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionGroupsApi#getPermissionGroups");
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
| **productId** | **UUID**| The identifier of the Product. | |

### Return type

[**List&lt;PermissionGroupModelHaljson&gt;**](PermissionGroupModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="updatePermissionGroup"></a>
# **updatePermissionGroup**
> PermissionGroupModelHaljson updatePermissionGroup(permissionGroupId, updatePermissionGroupRequest)

Update Permission Group

This endpoint updates a Permission Group identified by the &#x60;permissionGroupId&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    PermissionGroupsApi apiInstance = new PermissionGroupsApi(defaultClient);
    Long permissionGroupId = 56L; // Long | The identifier of the Permission Group.
    UpdatePermissionGroupRequest updatePermissionGroupRequest = new UpdatePermissionGroupRequest(); // UpdatePermissionGroupRequest | 
    try {
      PermissionGroupModelHaljson result = apiInstance.updatePermissionGroup(permissionGroupId, updatePermissionGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionGroupsApi#updatePermissionGroup");
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
| **permissionGroupId** | **Long**| The identifier of the Permission Group. | |
| **updatePermissionGroupRequest** | [**UpdatePermissionGroupRequest**](UpdatePermissionGroupRequest.md)|  | |

### Return type

[**PermissionGroupModelHaljson**](PermissionGroupModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

