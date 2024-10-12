# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentKeyPoliciesCreateOrUpdate**](DefaultApi.md#contentKeyPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName} | Create or update an Content Key Policy |
| [**contentKeyPoliciesDelete**](DefaultApi.md#contentKeyPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName} | Delete a Content Key Policy |
| [**contentKeyPoliciesGet**](DefaultApi.md#contentKeyPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName} | Get a Content Key Policy |
| [**contentKeyPoliciesGetPolicyPropertiesWithSecrets**](DefaultApi.md#contentKeyPoliciesGetPolicyPropertiesWithSecrets) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}/getPolicyPropertiesWithSecrets | Get a Content Key Policy with secrets |
| [**contentKeyPoliciesList**](DefaultApi.md#contentKeyPoliciesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies | List Content Key Policies |
| [**contentKeyPoliciesUpdate**](DefaultApi.md#contentKeyPoliciesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName} | Update a Content Key Policy |


<a id="contentKeyPoliciesCreateOrUpdate"></a>
# **contentKeyPoliciesCreateOrUpdate**
> ContentKeyPolicy contentKeyPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, parameters)

Create or update an Content Key Policy

Create or update a Content Key Policy in the Media Services account

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
    String contentKeyPolicyName = "contentKeyPolicyName_example"; // String | The Content Key Policy name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    ContentKeyPolicy parameters = new ContentKeyPolicy(); // ContentKeyPolicy | The request parameters
    try {
      ContentKeyPolicy result = apiInstance.contentKeyPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#contentKeyPoliciesCreateOrUpdate");
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
| **contentKeyPolicyName** | **String**| The Content Key Policy name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**ContentKeyPolicy**](ContentKeyPolicy.md)| The request parameters | |

### Return type

[**ContentKeyPolicy**](ContentKeyPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Detailed error information. |  -  |

<a id="contentKeyPoliciesDelete"></a>
# **contentKeyPoliciesDelete**
> contentKeyPoliciesDelete(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion)

Delete a Content Key Policy

Deletes a Content Key Policy in the Media Services account

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
    String contentKeyPolicyName = "contentKeyPolicyName_example"; // String | The Content Key Policy name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.contentKeyPoliciesDelete(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#contentKeyPoliciesDelete");
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
| **contentKeyPolicyName** | **String**| The Content Key Policy name. | |
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

<a id="contentKeyPoliciesGet"></a>
# **contentKeyPoliciesGet**
> ContentKeyPolicy contentKeyPoliciesGet(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion)

Get a Content Key Policy

Get the details of a Content Key Policy in the Media Services account

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
    String contentKeyPolicyName = "contentKeyPolicyName_example"; // String | The Content Key Policy name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      ContentKeyPolicy result = apiInstance.contentKeyPoliciesGet(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#contentKeyPoliciesGet");
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
| **contentKeyPolicyName** | **String**| The Content Key Policy name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**ContentKeyPolicy**](ContentKeyPolicy.md)

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

<a id="contentKeyPoliciesGetPolicyPropertiesWithSecrets"></a>
# **contentKeyPoliciesGetPolicyPropertiesWithSecrets**
> ContentKeyPolicyProperties contentKeyPoliciesGetPolicyPropertiesWithSecrets(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion)

Get a Content Key Policy with secrets

Get a Content Key Policy including secret values

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
    String contentKeyPolicyName = "contentKeyPolicyName_example"; // String | The Content Key Policy name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      ContentKeyPolicyProperties result = apiInstance.contentKeyPoliciesGetPolicyPropertiesWithSecrets(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#contentKeyPoliciesGetPolicyPropertiesWithSecrets");
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
| **contentKeyPolicyName** | **String**| The Content Key Policy name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**ContentKeyPolicyProperties**](ContentKeyPolicyProperties.md)

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

<a id="contentKeyPoliciesList"></a>
# **contentKeyPoliciesList**
> ContentKeyPolicyCollection contentKeyPoliciesList(subscriptionId, resourceGroupName, accountName, apiVersion, $filter, $top, $orderby)

List Content Key Policies

Lists the Content Key Policies in the account

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
      ContentKeyPolicyCollection result = apiInstance.contentKeyPoliciesList(subscriptionId, resourceGroupName, accountName, apiVersion, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#contentKeyPoliciesList");
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

[**ContentKeyPolicyCollection**](ContentKeyPolicyCollection.md)

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

<a id="contentKeyPoliciesUpdate"></a>
# **contentKeyPoliciesUpdate**
> ContentKeyPolicy contentKeyPoliciesUpdate(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, parameters)

Update a Content Key Policy

Updates an existing Content Key Policy in the Media Services account

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
    String contentKeyPolicyName = "contentKeyPolicyName_example"; // String | The Content Key Policy name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    ContentKeyPolicy parameters = new ContentKeyPolicy(); // ContentKeyPolicy | The request parameters
    try {
      ContentKeyPolicy result = apiInstance.contentKeyPoliciesUpdate(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#contentKeyPoliciesUpdate");
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
| **contentKeyPolicyName** | **String**| The Content Key Policy name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**ContentKeyPolicy**](ContentKeyPolicy.md)| The request parameters | |

### Return type

[**ContentKeyPolicy**](ContentKeyPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

