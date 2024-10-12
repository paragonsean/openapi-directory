# UsersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersCreateOrUpdate**](UsersApi.md#usersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName} |  |
| [**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName} |  |
| [**usersGet**](UsersApi.md#usersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName} |  |
| [**usersList**](UsersApi.md#usersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users |  |
| [**usersUpdate**](UsersApi.md#usersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/users/{userName} |  |


<a id="usersCreateOrUpdate"></a>
# **usersCreateOrUpdate**
> User usersCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, user)



Create or replace an existing User.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    User user = new User(); // User | The User registered to a lab
    try {
      User result = apiInstance.usersCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **user** | [**User**](User.md)| The User registered to a lab | |

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | BadRequest |  -  |

<a id="usersDelete"></a>
# **usersDelete**
> usersDelete(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion)



Delete user. This operation can take a while to complete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      apiInstance.usersDelete(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersDelete");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

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
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="usersGet"></a>
# **usersGet**
> User usersGet(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, $expand)



Get user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=email)'
    try {
      User result = apiInstance.usersGet(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;email)&#39; | [optional] |

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="usersList"></a>
# **usersList**
> ResponseWithContinuationUser usersList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, $expand, $filter, $top, $orderby)



List users in a given lab.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2018-10-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=email)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation.
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation.
    try {
      ResponseWithContinuationUser result = apiInstance.usersList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;email)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] |

### Return type

[**ResponseWithContinuationUser**](ResponseWithContinuationUser.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="usersUpdate"></a>
# **usersUpdate**
> User usersUpdate(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, user)



Modify properties of users.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labAccountName = "labAccountName_example"; // String | The name of the lab Account.
    String labName = "labName_example"; // String | The name of the lab.
    String userName = "userName_example"; // String | The name of the user.
    String apiVersion = "2018-10-15"; // String | Client API version.
    UserFragment user = new UserFragment(); // UserFragment | The User registered to a lab
    try {
      User result = apiInstance.usersUpdate(subscriptionId, resourceGroupName, labAccountName, labName, userName, apiVersion, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labAccountName** | **String**| The name of the lab Account. | |
| **labName** | **String**| The name of the lab. | |
| **userName** | **String**| The name of the user. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |
| **user** | [**UserFragment**](UserFragment.md)| The User registered to a lab | |

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

