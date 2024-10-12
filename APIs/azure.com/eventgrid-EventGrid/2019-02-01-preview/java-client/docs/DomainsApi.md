# DomainsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**domainsCreateOrUpdate**](DomainsApi.md#domainsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName} | Create or update a domain |
| [**domainsDelete**](DomainsApi.md#domainsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName} | Delete a domain |
| [**domainsGet**](DomainsApi.md#domainsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName} | Get a domain |
| [**domainsListByResourceGroup**](DomainsApi.md#domainsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains | List domains under a resource group |
| [**domainsListBySubscription**](DomainsApi.md#domainsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EventGrid/domains | List domains under an Azure subscription |
| [**domainsListSharedAccessKeys**](DomainsApi.md#domainsListSharedAccessKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/listKeys | List keys for a domain |
| [**domainsRegenerateKey**](DomainsApi.md#domainsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/regenerateKey | Regenerate key for a domain |
| [**domainsUpdate**](DomainsApi.md#domainsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName} | Update a domain |


<a id="domainsCreateOrUpdate"></a>
# **domainsCreateOrUpdate**
> Domain domainsCreateOrUpdate(subscriptionId, resourceGroupName, domainName, apiVersion, domainInfo)

Create or update a domain

Asynchronously creates or updates a new domain with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Name of the domain
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    Domain domainInfo = new Domain(); // Domain | Domain information
    try {
      Domain result = apiInstance.domainsCreateOrUpdate(subscriptionId, resourceGroupName, domainName, apiVersion, domainInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **domainName** | **String**| Name of the domain | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **domainInfo** | [**Domain**](Domain.md)| Domain information | |

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="domainsDelete"></a>
# **domainsDelete**
> domainsDelete(subscriptionId, resourceGroupName, domainName, apiVersion)

Delete a domain

Delete existing domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Name of the domain
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.domainsDelete(subscriptionId, resourceGroupName, domainName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsDelete");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **domainName** | **String**| Name of the domain | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 404 Not Found.   * 500 Internal Server Error. |  -  |

<a id="domainsGet"></a>
# **domainsGet**
> Domain domainsGet(subscriptionId, resourceGroupName, domainName, apiVersion)

Get a domain

Get properties of a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Name of the domain
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      Domain result = apiInstance.domainsGet(subscriptionId, resourceGroupName, domainName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **domainName** | **String**| Name of the domain | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="domainsListByResourceGroup"></a>
# **domainsListByResourceGroup**
> DomainsListResult domainsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top)

List domains under a resource group

List all the domains under a resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    try {
      DomainsListResult result = apiInstance.domainsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsListByResourceGroup");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |

### Return type

[**DomainsListResult**](DomainsListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="domainsListBySubscription"></a>
# **domainsListBySubscription**
> DomainsListResult domainsListBySubscription(subscriptionId, apiVersion, $filter, $top)

List domains under an Azure subscription

List all the domains under an Azure subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Filter the results using OData syntax.
    Integer $top = 56; // Integer | The number of results to return.
    try {
      DomainsListResult result = apiInstance.domainsListBySubscription(subscriptionId, apiVersion, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsListBySubscription");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| Filter the results using OData syntax. | [optional] |
| **$top** | **Integer**| The number of results to return. | [optional] |

### Return type

[**DomainsListResult**](DomainsListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="domainsListSharedAccessKeys"></a>
# **domainsListSharedAccessKeys**
> DomainSharedAccessKeys domainsListSharedAccessKeys(subscriptionId, resourceGroupName, domainName, apiVersion)

List keys for a domain

List the two keys used to publish to a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Name of the domain
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      DomainSharedAccessKeys result = apiInstance.domainsListSharedAccessKeys(subscriptionId, resourceGroupName, domainName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsListSharedAccessKeys");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **domainName** | **String**| Name of the domain | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**DomainSharedAccessKeys**](DomainSharedAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="domainsRegenerateKey"></a>
# **domainsRegenerateKey**
> DomainSharedAccessKeys domainsRegenerateKey(subscriptionId, resourceGroupName, domainName, apiVersion, regenerateKeyRequest)

Regenerate key for a domain

Regenerate a shared access key for a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Name of the domain
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    DomainRegenerateKeyRequest regenerateKeyRequest = new DomainRegenerateKeyRequest(); // DomainRegenerateKeyRequest | Request body to regenerate key
    try {
      DomainSharedAccessKeys result = apiInstance.domainsRegenerateKey(subscriptionId, resourceGroupName, domainName, apiVersion, regenerateKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsRegenerateKey");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **domainName** | **String**| Name of the domain | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **regenerateKeyRequest** | [**DomainRegenerateKeyRequest**](DomainRegenerateKeyRequest.md)| Request body to regenerate key | |

### Return type

[**DomainSharedAccessKeys**](DomainSharedAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="domainsUpdate"></a>
# **domainsUpdate**
> Domain domainsUpdate(subscriptionId, resourceGroupName, domainName, apiVersion, domainUpdateParameters)

Update a domain

Asynchronously updates a domain with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Name of the domain
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    DomainUpdateParameters domainUpdateParameters = new DomainUpdateParameters(); // DomainUpdateParameters | Domain update information
    try {
      Domain result = apiInstance.domainsUpdate(subscriptionId, resourceGroupName, domainName, apiVersion, domainUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsUpdate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. | |
| **domainName** | **String**| Name of the domain | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **domainUpdateParameters** | [**DomainUpdateParameters**](DomainUpdateParameters.md)| Domain update information | |

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Domain update request accepted. |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

