# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**streamingLocatorsCreate**](DefaultApi.md#streamingLocatorsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators/{streamingLocatorName} | Create a Streaming Locator |
| [**streamingLocatorsDelete**](DefaultApi.md#streamingLocatorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators/{streamingLocatorName} | Delete a Streaming Locator |
| [**streamingLocatorsGet**](DefaultApi.md#streamingLocatorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators/{streamingLocatorName} | Get a Streaming Locator |
| [**streamingLocatorsList**](DefaultApi.md#streamingLocatorsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators | List Streaming Locators |
| [**streamingLocatorsListContentKeys**](DefaultApi.md#streamingLocatorsListContentKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators/{streamingLocatorName}/listContentKeys | List Content Keys |
| [**streamingLocatorsListPaths**](DefaultApi.md#streamingLocatorsListPaths) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators/{streamingLocatorName}/listPaths | List Paths |
| [**streamingPoliciesCreate**](DefaultApi.md#streamingPoliciesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingPolicies/{streamingPolicyName} | Create a Streaming Policy |
| [**streamingPoliciesDelete**](DefaultApi.md#streamingPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingPolicies/{streamingPolicyName} | Delete a Streaming Policy |
| [**streamingPoliciesGet**](DefaultApi.md#streamingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingPolicies/{streamingPolicyName} | Get a Streaming Policy |
| [**streamingPoliciesList**](DefaultApi.md#streamingPoliciesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingPolicies | List Streaming Policies |


<a id="streamingLocatorsCreate"></a>
# **streamingLocatorsCreate**
> StreamingLocator streamingLocatorsCreate(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion, parameters)

Create a Streaming Locator

Create a Streaming Locator in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingLocatorName = "streamingLocatorName_example"; // String | The Streaming Locator name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    StreamingLocator parameters = new StreamingLocator(); // StreamingLocator | The request parameters
    try {
      StreamingLocator result = apiInstance.streamingLocatorsCreate(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#streamingLocatorsCreate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingLocatorName** | **String**| The Streaming Locator name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**StreamingLocator**](StreamingLocator.md)| The request parameters | |

### Return type

[**StreamingLocator**](StreamingLocator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | Detailed error information. |  -  |

<a id="streamingLocatorsDelete"></a>
# **streamingLocatorsDelete**
> streamingLocatorsDelete(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion)

Delete a Streaming Locator

Deletes a Streaming Locator in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingLocatorName = "streamingLocatorName_example"; // String | The Streaming Locator name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.streamingLocatorsDelete(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#streamingLocatorsDelete");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingLocatorName** | **String**| The Streaming Locator name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |
| **0** | Detailed error information. |  -  |

<a id="streamingLocatorsGet"></a>
# **streamingLocatorsGet**
> StreamingLocator streamingLocatorsGet(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion)

Get a Streaming Locator

Get the details of a Streaming Locator in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingLocatorName = "streamingLocatorName_example"; // String | The Streaming Locator name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      StreamingLocator result = apiInstance.streamingLocatorsGet(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#streamingLocatorsGet");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingLocatorName** | **String**| The Streaming Locator name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**StreamingLocator**](StreamingLocator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NotFound |  -  |
| **0** | Detailed error information. |  -  |

<a id="streamingLocatorsList"></a>
# **streamingLocatorsList**
> StreamingLocatorCollection streamingLocatorsList(subscriptionId, resourceGroupName, accountName, apiVersion, $filter, $top, $orderby)

List Streaming Locators

Lists the Streaming Locators in the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Restricts the set of items returned.
    Integer $top = 56; // Integer | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    String $orderby = "$orderby_example"; // String | Specifies the key by which the result collection should be ordered.
    try {
      StreamingLocatorCollection result = apiInstance.streamingLocatorsList(subscriptionId, resourceGroupName, accountName, apiVersion, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#streamingLocatorsList");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **$filter** | **String**| Restricts the set of items returned. | [optional] |
| **$top** | **Integer**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] |
| **$orderby** | **String**| Specifies the key by which the result collection should be ordered. | [optional] |

### Return type

[**StreamingLocatorCollection**](StreamingLocatorCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="streamingLocatorsListContentKeys"></a>
# **streamingLocatorsListContentKeys**
> ListContentKeysResponse streamingLocatorsListContentKeys(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion)

List Content Keys

List Content Keys used by this Streaming Locator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingLocatorName = "streamingLocatorName_example"; // String | The Streaming Locator name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      ListContentKeysResponse result = apiInstance.streamingLocatorsListContentKeys(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#streamingLocatorsListContentKeys");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingLocatorName** | **String**| The Streaming Locator name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**ListContentKeysResponse**](ListContentKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="streamingLocatorsListPaths"></a>
# **streamingLocatorsListPaths**
> ListPathsResponse streamingLocatorsListPaths(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion)

List Paths

List Paths supported by this Streaming Locator

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingLocatorName = "streamingLocatorName_example"; // String | The Streaming Locator name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      ListPathsResponse result = apiInstance.streamingLocatorsListPaths(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#streamingLocatorsListPaths");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingLocatorName** | **String**| The Streaming Locator name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**ListPathsResponse**](ListPathsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="streamingPoliciesCreate"></a>
# **streamingPoliciesCreate**
> StreamingPolicy streamingPoliciesCreate(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion, parameters)

Create a Streaming Policy

Create a Streaming Policy in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingPolicyName = "streamingPolicyName_example"; // String | The Streaming Policy name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    StreamingPolicy parameters = new StreamingPolicy(); // StreamingPolicy | The request parameters
    try {
      StreamingPolicy result = apiInstance.streamingPoliciesCreate(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#streamingPoliciesCreate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingPolicyName** | **String**| The Streaming Policy name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**StreamingPolicy**](StreamingPolicy.md)| The request parameters | |

### Return type

[**StreamingPolicy**](StreamingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | Detailed error information. |  -  |

<a id="streamingPoliciesDelete"></a>
# **streamingPoliciesDelete**
> streamingPoliciesDelete(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion)

Delete a Streaming Policy

Deletes a Streaming Policy in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingPolicyName = "streamingPolicyName_example"; // String | The Streaming Policy name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.streamingPoliciesDelete(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#streamingPoliciesDelete");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingPolicyName** | **String**| The Streaming Policy name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |
| **0** | Detailed error information. |  -  |

<a id="streamingPoliciesGet"></a>
# **streamingPoliciesGet**
> StreamingPolicy streamingPoliciesGet(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion)

Get a Streaming Policy

Get the details of a Streaming Policy in the Media Services account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String streamingPolicyName = "streamingPolicyName_example"; // String | The Streaming Policy name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      StreamingPolicy result = apiInstance.streamingPoliciesGet(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#streamingPoliciesGet");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **streamingPolicyName** | **String**| The Streaming Policy name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**StreamingPolicy**](StreamingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NotFound |  -  |
| **0** | Detailed error information. |  -  |

<a id="streamingPoliciesList"></a>
# **streamingPoliciesList**
> StreamingPolicyCollection streamingPoliciesList(subscriptionId, resourceGroupName, accountName, apiVersion, $filter, $top, $orderby)

List Streaming Policies

Lists the Streaming Policies in the account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Restricts the set of items returned.
    Integer $top = 56; // Integer | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    String $orderby = "$orderby_example"; // String | Specifies the key by which the result collection should be ordered.
    try {
      StreamingPolicyCollection result = apiInstance.streamingPoliciesList(subscriptionId, resourceGroupName, accountName, apiVersion, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#streamingPoliciesList");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **$filter** | **String**| Restricts the set of items returned. | [optional] |
| **$top** | **Integer**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] |
| **$orderby** | **String**| Specifies the key by which the result collection should be ordered. | [optional] |

### Return type

[**StreamingPolicyCollection**](StreamingPolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

