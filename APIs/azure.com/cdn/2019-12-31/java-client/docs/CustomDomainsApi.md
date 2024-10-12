# CustomDomainsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customDomainsCreate**](CustomDomainsApi.md#customDomainsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName} |  |
| [**customDomainsDelete**](CustomDomainsApi.md#customDomainsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName} |  |
| [**customDomainsDisableCustomHttps**](CustomDomainsApi.md#customDomainsDisableCustomHttps) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName}/disableCustomHttps |  |
| [**customDomainsEnableCustomHttps**](CustomDomainsApi.md#customDomainsEnableCustomHttps) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName}/enableCustomHttps |  |
| [**customDomainsGet**](CustomDomainsApi.md#customDomainsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName} |  |
| [**customDomainsListByEndpoint**](CustomDomainsApi.md#customDomainsListByEndpoint) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains |  |


<a id="customDomainsCreate"></a>
# **customDomainsCreate**
> CustomDomain customDomainsCreate(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, customDomainProperties)



Creates a new custom domain within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    CustomDomainParameters customDomainProperties = new CustomDomainParameters(); // CustomDomainParameters | Properties required to create a new custom domain.
    try {
      CustomDomain result = apiInstance.customDomainsCreate(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, customDomainProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsCreate");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **customDomainName** | **String**| Name of the custom domain within an endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **customDomainProperties** | [**CustomDomainParameters**](CustomDomainParameters.md)| Properties required to create a new custom domain. | |

### Return type

[**CustomDomain**](CustomDomain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. The request has been fulfilled and a new custom domain has been created. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="customDomainsDelete"></a>
# **customDomainsDelete**
> customDomainsDelete(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion)



Deletes an existing custom domain within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      apiInstance.customDomainsDelete(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsDelete");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **customDomainName** | **String**| Name of the custom domain within an endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

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
| **204** | No Content. The request has been accepted but the custom domain was not found |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="customDomainsDisableCustomHttps"></a>
# **customDomainsDisableCustomHttps**
> customDomainsDisableCustomHttps(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion)



Disable https delivery of the custom domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      apiInstance.customDomainsDisableCustomHttps(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsDisableCustomHttps");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **customDomainName** | **String**| Name of the custom domain within an endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

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
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="customDomainsEnableCustomHttps"></a>
# **customDomainsEnableCustomHttps**
> customDomainsEnableCustomHttps(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, customDomainHttpsParameters)



Enable https delivery of the custom domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    CustomDomainHttpsParameters customDomainHttpsParameters = new CustomDomainHttpsParameters(); // CustomDomainHttpsParameters | The configuration specifying how to enable HTTPS for the custom domain - using CDN managed certificate or user's own certificate. If not specified, enabling ssl uses CDN managed certificate by default.
    try {
      apiInstance.customDomainsEnableCustomHttps(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, customDomainHttpsParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsEnableCustomHttps");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **customDomainName** | **String**| Name of the custom domain within an endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **customDomainHttpsParameters** | [**CustomDomainHttpsParameters**](CustomDomainHttpsParameters.md)| The configuration specifying how to enable HTTPS for the custom domain - using CDN managed certificate or user&#39;s own certificate. If not specified, enabling ssl uses CDN managed certificate by default. | [optional] |

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
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="customDomainsGet"></a>
# **customDomainsGet**
> CustomDomain customDomainsGet(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion)



Gets an existing custom domain within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      CustomDomain result = apiInstance.customDomainsGet(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsGet");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **customDomainName** | **String**| Name of the custom domain within an endpoint. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

### Return type

[**CustomDomain**](CustomDomain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="customDomainsListByEndpoint"></a>
# **customDomainsListByEndpoint**
> CustomDomainListResult customDomainsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Lists all of the existing custom domains within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      CustomDomainListResult result = apiInstance.customDomainsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsListByEndpoint");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

### Return type

[**CustomDomainListResult**](CustomDomainListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

