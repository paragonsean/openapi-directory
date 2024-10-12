# DomainsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**domainsCreateOrUpdateDomain**](DomainsApi.md#domainsCreateOrUpdateDomain) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Creates a domain |
| [**domainsDeleteDomain**](DomainsApi.md#domainsDeleteDomain) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Deletes a domain |
| [**domainsGetDomain**](DomainsApi.md#domainsGetDomain) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Gets details of a domain |
| [**domainsGetDomainOperation**](DomainsApi.md#domainsGetDomainOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName}/operationresults/{operationId} | Retrieves the latest status of a domain purchase operation |
| [**domainsGetDomains**](DomainsApi.md#domainsGetDomains) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains | Lists domains under a resource group |
| [**domainsUpdateDomain**](DomainsApi.md#domainsUpdateDomain) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DomainRegistration/domains/{domainName} | Creates a domain |


<a id="domainsCreateOrUpdateDomain"></a>
# **domainsCreateOrUpdateDomain**
> Domain domainsCreateOrUpdateDomain(resourceGroupName, domainName, subscriptionId, apiVersion, domain)

Creates a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | &gt;Name of the resource group
    String domainName = "domainName_example"; // String | Name of the domain
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Domain domain = new Domain(); // Domain | Domain registration information
    try {
      Domain result = apiInstance.domainsCreateOrUpdateDomain(resourceGroupName, domainName, subscriptionId, apiVersion, domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsCreateOrUpdateDomain");
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
| **resourceGroupName** | **String**| &amp;gt;Name of the resource group | |
| **domainName** | **String**| Name of the domain | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **domain** | [**Domain**](Domain.md)| Domain registration information | |

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domain purchase was successful |  -  |
| **202** | Domain purchase is in progress |  -  |

<a id="domainsDeleteDomain"></a>
# **domainsDeleteDomain**
> Object domainsDeleteDomain(resourceGroupName, domainName, subscriptionId, apiVersion, forceHardDeleteDomain)

Deletes a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String domainName = "domainName_example"; // String | Name of the domain
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean forceHardDeleteDomain = true; // Boolean | If true then the domain will be deleted immediately instead of after 24 hours
    try {
      Object result = apiInstance.domainsDeleteDomain(resourceGroupName, domainName, subscriptionId, apiVersion, forceHardDeleteDomain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsDeleteDomain");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **domainName** | **String**| Name of the domain | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **forceHardDeleteDomain** | **Boolean**| If true then the domain will be deleted immediately instead of after 24 hours | [optional] |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Domain does not exist in Azure database probably because it has already been deleted |  -  |

<a id="domainsGetDomain"></a>
# **domainsGetDomain**
> Domain domainsGetDomain(resourceGroupName, domainName, subscriptionId, apiVersion)

Gets details of a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String domainName = "domainName_example"; // String | Name of the domain
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Domain result = apiInstance.domainsGetDomain(resourceGroupName, domainName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsGetDomain");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **domainName** | **String**| Name of the domain | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="domainsGetDomainOperation"></a>
# **domainsGetDomainOperation**
> Domain domainsGetDomainOperation(resourceGroupName, domainName, operationId, subscriptionId, apiVersion)

Retrieves the latest status of a domain purchase operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String domainName = "domainName_example"; // String | Name of the domain
    String operationId = "operationId_example"; // String | Domain purchase operation Id
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Domain result = apiInstance.domainsGetDomainOperation(resourceGroupName, domainName, operationId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsGetDomainOperation");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **domainName** | **String**| Name of the domain | |
| **operationId** | **String**| Domain purchase operation Id | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domain purchase was successful |  -  |
| **202** | Domain purchase is in progress |  -  |
| **500** | Domain purchase request failed |  -  |

<a id="domainsGetDomains"></a>
# **domainsGetDomains**
> DomainCollection domainsGetDomains(resourceGroupName, subscriptionId, apiVersion)

Lists domains under a resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DomainCollection result = apiInstance.domainsGetDomains(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsGetDomains");
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
| **resourceGroupName** | **String**| Name of the resource group | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DomainCollection**](DomainCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="domainsUpdateDomain"></a>
# **domainsUpdateDomain**
> Domain domainsUpdateDomain(resourceGroupName, domainName, subscriptionId, apiVersion, domain)

Creates a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | &gt;Name of the resource group
    String domainName = "domainName_example"; // String | Name of the domain
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Domain domain = new Domain(); // Domain | Domain registration information
    try {
      Domain result = apiInstance.domainsUpdateDomain(resourceGroupName, domainName, subscriptionId, apiVersion, domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsUpdateDomain");
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
| **resourceGroupName** | **String**| &amp;gt;Name of the resource group | |
| **domainName** | **String**| Name of the domain | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **domain** | [**Domain**](Domain.md)| Domain registration information | |

### Return type

[**Domain**](Domain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Domain purchase was successful |  -  |
| **202** | Domain purchase is in progress |  -  |

