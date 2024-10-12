# FrontDoorsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**endpointsPurgeContent**](FrontDoorsApi.md#endpointsPurgeContent) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/purge |  |
| [**frontDoorsCreateOrUpdate**](FrontDoorsApi.md#frontDoorsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName} |  |
| [**frontDoorsDelete**](FrontDoorsApi.md#frontDoorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName} |  |
| [**frontDoorsGet**](FrontDoorsApi.md#frontDoorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName} |  |
| [**frontDoorsList**](FrontDoorsApi.md#frontDoorsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/frontDoors |  |
| [**frontDoorsListByResourceGroup**](FrontDoorsApi.md#frontDoorsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors |  |
| [**frontDoorsValidateCustomDomain**](FrontDoorsApi.md#frontDoorsValidateCustomDomain) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/validateCustomDomain |  |
| [**frontendEndpointsDisableHttps**](FrontDoorsApi.md#frontendEndpointsDisableHttps) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}/disableHttps |  |
| [**frontendEndpointsEnableHttps**](FrontDoorsApi.md#frontendEndpointsEnableHttps) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}/enableHttps |  |
| [**frontendEndpointsGet**](FrontDoorsApi.md#frontendEndpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName} |  |
| [**frontendEndpointsListByFrontDoor**](FrontDoorsApi.md#frontendEndpointsListByFrontDoor) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints |  |
| [**rulesEnginesCreateOrUpdate**](FrontDoorsApi.md#rulesEnginesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/rulesEngines/{rulesEngineName} |  |
| [**rulesEnginesDelete**](FrontDoorsApi.md#rulesEnginesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/rulesEngines/{rulesEngineName} |  |
| [**rulesEnginesGet**](FrontDoorsApi.md#rulesEnginesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/rulesEngines/{rulesEngineName} |  |
| [**rulesEnginesListByFrontDoor**](FrontDoorsApi.md#rulesEnginesListByFrontDoor) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/rulesEngines |  |


<a id="endpointsPurgeContent"></a>
# **endpointsPurgeContent**
> endpointsPurgeContent(subscriptionId, resourceGroupName, frontDoorName, apiVersion, contentFilePaths)



Removes a content from Front Door.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    PurgeParameters contentFilePaths = new PurgeParameters(); // PurgeParameters | The path to the content to be purged. Path can be a full URL, e.g. '/pictures/city.png' which removes a single file, or a directory with a wildcard, e.g. '/pictures/_*' which removes all folders and files in the directory.
    try {
      apiInstance.endpointsPurgeContent(subscriptionId, resourceGroupName, frontDoorName, apiVersion, contentFilePaths);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#endpointsPurgeContent");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **apiVersion** | **String**| Client API version. | |
| **contentFilePaths** | [**PurgeParameters**](PurgeParameters.md)| The path to the content to be purged. Path can be a full URL, e.g. &#39;/pictures/city.png&#39; which removes a single file, or a directory with a wildcard, e.g. &#39;/pictures/_*&#39; which removes all folders and files in the directory. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="frontDoorsCreateOrUpdate"></a>
# **frontDoorsCreateOrUpdate**
> FrontDoor frontDoorsCreateOrUpdate(subscriptionId, resourceGroupName, frontDoorName, apiVersion, frontDoorParameters)



Creates a new Front Door with a Front Door name under the specified subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    FrontDoor frontDoorParameters = new FrontDoor(); // FrontDoor | Front Door properties needed to create a new Front Door.
    try {
      FrontDoor result = apiInstance.frontDoorsCreateOrUpdate(subscriptionId, resourceGroupName, frontDoorName, apiVersion, frontDoorParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#frontDoorsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **apiVersion** | **String**| Client API version. | |
| **frontDoorParameters** | [**FrontDoor**](FrontDoor.md)| Front Door properties needed to create a new Front Door. | |

### Return type

[**FrontDoor**](FrontDoor.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. The request has been fulfilled and a new Front Door has been created. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="frontDoorsDelete"></a>
# **frontDoorsDelete**
> frontDoorsDelete(subscriptionId, resourceGroupName, frontDoorName, apiVersion)



Deletes an existing Front Door with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.frontDoorsDelete(subscriptionId, resourceGroupName, frontDoorName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#frontDoorsDelete");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **apiVersion** | **String**| Client API version. | |

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
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **204** | No Content. The request has been accepted but the Front Door was not found. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="frontDoorsGet"></a>
# **frontDoorsGet**
> FrontDoor frontDoorsGet(subscriptionId, resourceGroupName, frontDoorName, apiVersion)



Gets a Front Door with the specified Front Door name under the specified subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      FrontDoor result = apiInstance.frontDoorsGet(subscriptionId, resourceGroupName, frontDoorName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#frontDoorsGet");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**FrontDoor**](FrontDoor.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="frontDoorsList"></a>
# **frontDoorsList**
> FrontDoorListResult frontDoorsList(subscriptionId, apiVersion)



Lists all of the Front Doors within an Azure subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      FrontDoorListResult result = apiInstance.frontDoorsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#frontDoorsList");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**FrontDoorListResult**](FrontDoorListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="frontDoorsListByResourceGroup"></a>
# **frontDoorsListByResourceGroup**
> FrontDoorListResult frontDoorsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all of the Front Doors within a resource group under a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      FrontDoorListResult result = apiInstance.frontDoorsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#frontDoorsListByResourceGroup");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**FrontDoorListResult**](FrontDoorListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="frontDoorsValidateCustomDomain"></a>
# **frontDoorsValidateCustomDomain**
> ValidateCustomDomainOutput frontDoorsValidateCustomDomain(subscriptionId, resourceGroupName, frontDoorName, apiVersion, customDomainProperties)



Validates the custom domain mapping to ensure it maps to the correct Front Door endpoint in DNS.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    ValidateCustomDomainInput customDomainProperties = new ValidateCustomDomainInput(); // ValidateCustomDomainInput | Custom domain to be validated.
    try {
      ValidateCustomDomainOutput result = apiInstance.frontDoorsValidateCustomDomain(subscriptionId, resourceGroupName, frontDoorName, apiVersion, customDomainProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#frontDoorsValidateCustomDomain");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **apiVersion** | **String**| Client API version. | |
| **customDomainProperties** | [**ValidateCustomDomainInput**](ValidateCustomDomainInput.md)| Custom domain to be validated. | |

### Return type

[**ValidateCustomDomainOutput**](ValidateCustomDomainOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="frontendEndpointsDisableHttps"></a>
# **frontendEndpointsDisableHttps**
> frontendEndpointsDisableHttps(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion)



Disables a frontendEndpoint for HTTPS traffic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String frontendEndpointName = "frontendEndpointName_example"; // String | Name of the Frontend endpoint which is unique within the Front Door.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.frontendEndpointsDisableHttps(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#frontendEndpointsDisableHttps");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **frontendEndpointName** | **String**| Name of the Frontend endpoint which is unique within the Front Door. | |
| **apiVersion** | **String**| Client API version. | |

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
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="frontendEndpointsEnableHttps"></a>
# **frontendEndpointsEnableHttps**
> frontendEndpointsEnableHttps(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion, customHttpsConfiguration)



Enables a frontendEndpoint for HTTPS traffic

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String frontendEndpointName = "frontendEndpointName_example"; // String | Name of the Frontend endpoint which is unique within the Front Door.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    CustomHttpsConfiguration customHttpsConfiguration = new CustomHttpsConfiguration(); // CustomHttpsConfiguration | The configuration specifying how to enable HTTPS
    try {
      apiInstance.frontendEndpointsEnableHttps(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion, customHttpsConfiguration);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#frontendEndpointsEnableHttps");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **frontendEndpointName** | **String**| Name of the Frontend endpoint which is unique within the Front Door. | |
| **apiVersion** | **String**| Client API version. | |
| **customHttpsConfiguration** | [**CustomHttpsConfiguration**](CustomHttpsConfiguration.md)| The configuration specifying how to enable HTTPS | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="frontendEndpointsGet"></a>
# **frontendEndpointsGet**
> FrontendEndpoint frontendEndpointsGet(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion)



Gets a Frontend endpoint with the specified name within the specified Front Door.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String frontendEndpointName = "frontendEndpointName_example"; // String | Name of the Frontend endpoint which is unique within the Front Door.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      FrontendEndpoint result = apiInstance.frontendEndpointsGet(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#frontendEndpointsGet");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **frontendEndpointName** | **String**| Name of the Frontend endpoint which is unique within the Front Door. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**FrontendEndpoint**](FrontendEndpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="frontendEndpointsListByFrontDoor"></a>
# **frontendEndpointsListByFrontDoor**
> FrontendEndpointsListResult frontendEndpointsListByFrontDoor(subscriptionId, resourceGroupName, frontDoorName, apiVersion)



Lists all of the frontend endpoints within a Front Door.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      FrontendEndpointsListResult result = apiInstance.frontendEndpointsListByFrontDoor(subscriptionId, resourceGroupName, frontDoorName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#frontendEndpointsListByFrontDoor");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**FrontendEndpointsListResult**](FrontendEndpointsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="rulesEnginesCreateOrUpdate"></a>
# **rulesEnginesCreateOrUpdate**
> RulesEngine rulesEnginesCreateOrUpdate(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion, rulesEngineParameters)



Creates a new Rules Engine Configuration with the specified name within the specified Front Door.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String rulesEngineName = "rulesEngineName_example"; // String | Name of the Rules Engine which is unique within the Front Door.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    RulesEngine rulesEngineParameters = new RulesEngine(); // RulesEngine | Rules Engine Configuration properties needed to create a new Rules Engine Configuration.
    try {
      RulesEngine result = apiInstance.rulesEnginesCreateOrUpdate(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion, rulesEngineParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#rulesEnginesCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **rulesEngineName** | **String**| Name of the Rules Engine which is unique within the Front Door. | |
| **apiVersion** | **String**| Client API version. | |
| **rulesEngineParameters** | [**RulesEngine**](RulesEngine.md)| Rules Engine Configuration properties needed to create a new Rules Engine Configuration. | |

### Return type

[**RulesEngine**](RulesEngine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. The request has been fulfilled and a new RulesEngine has been created. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="rulesEnginesDelete"></a>
# **rulesEnginesDelete**
> rulesEnginesDelete(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion)



Deletes an existing Rules Engine Configuration with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String rulesEngineName = "rulesEngineName_example"; // String | Name of the Rules Engine which is unique within the Front Door.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.rulesEnginesDelete(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#rulesEnginesDelete");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **rulesEngineName** | **String**| Name of the Rules Engine which is unique within the Front Door. | |
| **apiVersion** | **String**| Client API version. | |

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
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **204** | No Content. The request has been accepted but the Rules Engine Configuration was not found. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="rulesEnginesGet"></a>
# **rulesEnginesGet**
> RulesEngine rulesEnginesGet(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion)



Gets a Rules Engine Configuration with the specified name within the specified Front Door.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String rulesEngineName = "rulesEngineName_example"; // String | Name of the Rules Engine which is unique within the Front Door.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      RulesEngine result = apiInstance.rulesEnginesGet(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#rulesEnginesGet");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **rulesEngineName** | **String**| Name of the Rules Engine which is unique within the Front Door. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**RulesEngine**](RulesEngine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

<a id="rulesEnginesListByFrontDoor"></a>
# **rulesEnginesListByFrontDoor**
> RulesEngineListResult rulesEnginesListByFrontDoor(subscriptionId, resourceGroupName, frontDoorName, apiVersion)



Lists all of the Rules Engine Configurations within a Front Door.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FrontDoorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FrontDoorsApi apiInstance = new FrontDoorsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      RulesEngineListResult result = apiInstance.rulesEnginesListByFrontDoor(subscriptionId, resourceGroupName, frontDoorName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FrontDoorsApi#rulesEnginesListByFrontDoor");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **frontDoorName** | **String**| Name of the Front Door which is globally unique. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**RulesEngineListResult**](RulesEngineListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Front Door error response describing why the operation failed. |  -  |

