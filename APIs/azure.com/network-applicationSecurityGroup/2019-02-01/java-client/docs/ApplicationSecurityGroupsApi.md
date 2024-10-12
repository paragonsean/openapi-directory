# ApplicationSecurityGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationSecurityGroupsCreateOrUpdate**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups/{applicationSecurityGroupName} |  |
| [**applicationSecurityGroupsDelete**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups/{applicationSecurityGroupName} |  |
| [**applicationSecurityGroupsGet**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups/{applicationSecurityGroupName} |  |
| [**applicationSecurityGroupsList**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups |  |
| [**applicationSecurityGroupsListAll**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationSecurityGroups |  |
| [**applicationSecurityGroupsUpdateTags**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups/{applicationSecurityGroupName} |  |


<a id="applicationSecurityGroupsCreateOrUpdate"></a>
# **applicationSecurityGroupsCreateOrUpdate**
> ApplicationSecurityGroup applicationSecurityGroupsCreateOrUpdate(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId, parameters)



Creates or updates an application security group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationSecurityGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationSecurityGroupsApi apiInstance = new ApplicationSecurityGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationSecurityGroupName = "applicationSecurityGroupName_example"; // String | The name of the application security group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApplicationSecurityGroup parameters = new ApplicationSecurityGroup(); // ApplicationSecurityGroup | Parameters supplied to the create or update ApplicationSecurityGroup operation.
    try {
      ApplicationSecurityGroup result = apiInstance.applicationSecurityGroupsCreateOrUpdate(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationSecurityGroupsApi#applicationSecurityGroupsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **applicationSecurityGroupName** | **String**| The name of the application security group. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApplicationSecurityGroup**](ApplicationSecurityGroup.md)| Parameters supplied to the create or update ApplicationSecurityGroup operation. | |

### Return type

[**ApplicationSecurityGroup**](ApplicationSecurityGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting application security group resource. |  -  |
| **201** | Create successful. The operation returns the resulting application security group resource. |  -  |

<a id="applicationSecurityGroupsDelete"></a>
# **applicationSecurityGroupsDelete**
> applicationSecurityGroupsDelete(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId)



Deletes the specified application security group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationSecurityGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationSecurityGroupsApi apiInstance = new ApplicationSecurityGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationSecurityGroupName = "applicationSecurityGroupName_example"; // String | The name of the application security group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.applicationSecurityGroupsDelete(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationSecurityGroupsApi#applicationSecurityGroupsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **applicationSecurityGroupName** | **String**| The name of the application security group. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Request successful. Resource does not exist. |  -  |

<a id="applicationSecurityGroupsGet"></a>
# **applicationSecurityGroupsGet**
> ApplicationSecurityGroup applicationSecurityGroupsGet(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId)



Gets information about the specified application security group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationSecurityGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationSecurityGroupsApi apiInstance = new ApplicationSecurityGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationSecurityGroupName = "applicationSecurityGroupName_example"; // String | The name of the application security group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApplicationSecurityGroup result = apiInstance.applicationSecurityGroupsGet(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationSecurityGroupsApi#applicationSecurityGroupsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **applicationSecurityGroupName** | **String**| The name of the application security group. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApplicationSecurityGroup**](ApplicationSecurityGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the specified application security group resource. |  -  |

<a id="applicationSecurityGroupsList"></a>
# **applicationSecurityGroupsList**
> ApplicationSecurityGroupListResult applicationSecurityGroupsList(resourceGroupName, apiVersion, subscriptionId)



Gets all the application security groups in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationSecurityGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationSecurityGroupsApi apiInstance = new ApplicationSecurityGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApplicationSecurityGroupListResult result = apiInstance.applicationSecurityGroupsList(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationSecurityGroupsApi#applicationSecurityGroupsList");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApplicationSecurityGroupListResult**](ApplicationSecurityGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of application security group resources. |  -  |

<a id="applicationSecurityGroupsListAll"></a>
# **applicationSecurityGroupsListAll**
> ApplicationSecurityGroupListResult applicationSecurityGroupsListAll(apiVersion, subscriptionId)



Gets all application security groups in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationSecurityGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationSecurityGroupsApi apiInstance = new ApplicationSecurityGroupsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApplicationSecurityGroupListResult result = apiInstance.applicationSecurityGroupsListAll(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationSecurityGroupsApi#applicationSecurityGroupsListAll");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApplicationSecurityGroupListResult**](ApplicationSecurityGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of application security group resources. |  -  |

<a id="applicationSecurityGroupsUpdateTags"></a>
# **applicationSecurityGroupsUpdateTags**
> ApplicationSecurityGroup applicationSecurityGroupsUpdateTags(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId, parameters)



Updates an application security group&#39;s tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationSecurityGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationSecurityGroupsApi apiInstance = new ApplicationSecurityGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String applicationSecurityGroupName = "applicationSecurityGroupName_example"; // String | The name of the application security group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApplicationSecurityGroupsUpdateTagsRequest parameters = new ApplicationSecurityGroupsUpdateTagsRequest(); // ApplicationSecurityGroupsUpdateTagsRequest | Parameters supplied to update application security group tags.
    try {
      ApplicationSecurityGroup result = apiInstance.applicationSecurityGroupsUpdateTags(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationSecurityGroupsApi#applicationSecurityGroupsUpdateTags");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **applicationSecurityGroupName** | **String**| The name of the application security group. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApplicationSecurityGroupsUpdateTagsRequest**](ApplicationSecurityGroupsUpdateTagsRequest.md)| Parameters supplied to update application security group tags. | |

### Return type

[**ApplicationSecurityGroup**](ApplicationSecurityGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ApplicationSecurityGroup resource. |  -  |

