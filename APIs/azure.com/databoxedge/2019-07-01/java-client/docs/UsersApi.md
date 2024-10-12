# UsersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersCreateOrUpdate**](UsersApi.md#usersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/users/{name} |  |
| [**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/users/{name} |  |
| [**usersGet**](UsersApi.md#usersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/users/{name} |  |
| [**usersListByDataBoxEdgeDevice**](UsersApi.md#usersListByDataBoxEdgeDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/users |  |


<a id="usersCreateOrUpdate"></a>
# **usersCreateOrUpdate**
> User usersCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, user)



Creates a new user or updates an existing user&#39;s information on a Data Box Edge/Data Box Gateway device.

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
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The user name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    User user = new User(); // User | The user details.
    try {
      User result = apiInstance.usersCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, user);
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
| **deviceName** | **String**| The device name. | |
| **name** | **String**| The user name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |
| **user** | [**User**](User.md)| The user details. | |

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
| **200** | Successfully created or updated the user. |  -  |
| **202** | Accepted the request to create or update the user. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="usersDelete"></a>
# **usersDelete**
> usersDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Deletes the user on a databox edge/gateway device.

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
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The user name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.usersDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
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
| **deviceName** | **String**| The device name. | |
| **name** | **String**| The user name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | Successfully deleted the user. |  -  |
| **202** | Accepted the request to delete the user. |  -  |
| **204** | The user is already deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="usersGet"></a>
# **usersGet**
> User usersGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Gets the properties of the specified user.

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
    String deviceName = "deviceName_example"; // String | The device name.
    String name = "name_example"; // String | The user name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      User result = apiInstance.usersGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion);
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
| **deviceName** | **String**| The device name. | |
| **name** | **String**| The user name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | The user details. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="usersListByDataBoxEdgeDevice"></a>
# **usersListByDataBoxEdgeDevice**
> UserList usersListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion)



Gets all the users registered on a Data Box Edge/Data Box Gateway device.

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
    String deviceName = "deviceName_example"; // String | The device name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      UserList result = apiInstance.usersListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersListByDataBoxEdgeDevice");
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
| **deviceName** | **String**| The device name. | |
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**UserList**](UserList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of all users on the device. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

