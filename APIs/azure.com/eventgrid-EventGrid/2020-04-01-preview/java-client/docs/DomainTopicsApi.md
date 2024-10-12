# DomainTopicsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**domainTopicsCreateOrUpdate**](DomainTopicsApi.md#domainTopicsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{domainTopicName} | Create or update a domain topic. |
| [**domainTopicsDelete**](DomainTopicsApi.md#domainTopicsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{domainTopicName} | Delete a domain topic. |
| [**domainTopicsGet**](DomainTopicsApi.md#domainTopicsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics/{domainTopicName} | Get a domain topic. |
| [**domainTopicsListByDomain**](DomainTopicsApi.md#domainTopicsListByDomain) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/domains/{domainName}/topics | List domain topics. |


<a id="domainTopicsCreateOrUpdate"></a>
# **domainTopicsCreateOrUpdate**
> DomainTopic domainTopicsCreateOrUpdate(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion)

Create or update a domain topic.

Asynchronously creates or updates a new domain topic with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainTopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainTopicsApi apiInstance = new DomainTopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Name of the domain.
    String domainTopicName = "domainTopicName_example"; // String | Name of the domain topic.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      DomainTopic result = apiInstance.domainTopicsCreateOrUpdate(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainTopicsApi#domainTopicsCreateOrUpdate");
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
| **domainName** | **String**| Name of the domain. | |
| **domainTopicName** | **String**| Name of the domain topic. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**DomainTopic**](DomainTopic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | *** Error Responses: ***   * 400 Bad Request.   * 500 Internal Server Error. |  -  |

<a id="domainTopicsDelete"></a>
# **domainTopicsDelete**
> domainTopicsDelete(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion)

Delete a domain topic.

Delete existing domain topic.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainTopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainTopicsApi apiInstance = new DomainTopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Name of the domain.
    String domainTopicName = "domainTopicName_example"; // String | Name of the domain topic.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.domainTopicsDelete(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainTopicsApi#domainTopicsDelete");
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
| **domainName** | **String**| Name of the domain. | |
| **domainTopicName** | **String**| Name of the domain topic. | |
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

<a id="domainTopicsGet"></a>
# **domainTopicsGet**
> DomainTopic domainTopicsGet(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion)

Get a domain topic.

Get properties of a domain topic.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainTopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainTopicsApi apiInstance = new DomainTopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Name of the domain.
    String domainTopicName = "domainTopicName_example"; // String | Name of the topic.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      DomainTopic result = apiInstance.domainTopicsGet(subscriptionId, resourceGroupName, domainName, domainTopicName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainTopicsApi#domainTopicsGet");
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
| **domainName** | **String**| Name of the domain. | |
| **domainTopicName** | **String**| Name of the topic. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**DomainTopic**](DomainTopic.md)

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

<a id="domainTopicsListByDomain"></a>
# **domainTopicsListByDomain**
> DomainTopicsListResult domainTopicsListByDomain(subscriptionId, resourceGroupName, domainName, apiVersion, $filter, $top)

List domain topics.

List all the topics in a domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainTopicsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DomainTopicsApi apiInstance = new DomainTopicsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription.
    String domainName = "domainName_example"; // String | Domain name.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The query used to filter the search results using OData syntax. Filtering is permitted on the 'name' property only and with limited number of OData operations. These operations are: the 'contains' function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter=contains(namE, 'PATTERN') and name ne 'PATTERN-1'. The following is not a valid filter example: $filter=location eq 'westus'.
    Integer $top = 56; // Integer | The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page.
    try {
      DomainTopicsListResult result = apiInstance.domainTopicsListByDomain(subscriptionId, resourceGroupName, domainName, apiVersion, $filter, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainTopicsApi#domainTopicsListByDomain");
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
| **domainName** | **String**| Domain name. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| The query used to filter the search results using OData syntax. Filtering is permitted on the &#39;name&#39; property only and with limited number of OData operations. These operations are: the &#39;contains&#39; function as well as the following logical operations: not, and, or, eq (for equal), and ne (for not equal). No arithmetic operations are supported. The following is a valid filter example: $filter&#x3D;contains(namE, &#39;PATTERN&#39;) and name ne &#39;PATTERN-1&#39;. The following is not a valid filter example: $filter&#x3D;location eq &#39;westus&#39;. | [optional] |
| **$top** | **Integer**| The number of results to return per page for the list operation. Valid range for top parameter is 1 to 100. If not specified, the default number of results to be returned is 20 items per page. | [optional] |

### Return type

[**DomainTopicsListResult**](DomainTopicsListResult.md)

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

