# BotApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**botsCreate**](BotApi.md#botsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName} |  |
| [**botsDelete**](BotApi.md#botsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName} |  |
| [**botsGet**](BotApi.md#botsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName} |  |
| [**botsGetCheckNameAvailability**](BotApi.md#botsGetCheckNameAvailability) | **POST** /providers/Microsoft.BotService/checkNameAvailability |  |
| [**botsList**](BotApi.md#botsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.BotService/botServices |  |
| [**botsListByResourceGroup**](BotApi.md#botsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices |  |
| [**botsUpdate**](BotApi.md#botsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName} |  |


<a id="botsCreate"></a>
# **botsCreate**
> Bot botsCreate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters)



Creates a Bot Service. Bot Service is a resource group wide resource type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotApi apiInstance = new BotApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    Bot parameters = new Bot(); // Bot | The parameters to provide for the created bot.
    try {
      Bot result = apiInstance.botsCreate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotApi#botsCreate");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **parameters** | [**Bot**](Bot.md)| The parameters to provide for the created bot. | |

### Return type

[**Bot**](Bot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created successfully or already existed, the service should return 200 (OK). |  -  |
| **201** | If resource is created successfully, the service should return 201 (Created). Execution to continue asynchronously. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="botsDelete"></a>
# **botsDelete**
> botsDelete(resourceGroupName, resourceName, apiVersion, subscriptionId)



Deletes a Bot Service from the resource group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotApi apiInstance = new BotApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      apiInstance.botsDelete(resourceGroupName, resourceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotApi#botsDelete");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

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
| **200** | A 200 (OK) should be returned if the object exists and was deleted successfully; |  -  |
| **204** | a 204 (NoContent) should be used if the resource does not exist and the request is well formed. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="botsGet"></a>
# **botsGet**
> Bot botsGet(resourceGroupName, resourceName, apiVersion, subscriptionId)



Returns a BotService specified by the parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotApi apiInstance = new BotApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      Bot result = apiInstance.botsGet(resourceGroupName, resourceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotApi#botsGet");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**Bot**](Bot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully.  |  -  |
| **0** | Error response describing why the operation failed. If the resource group *or* resource does not exist, 404 (NotFound) should be returned. |  -  |

<a id="botsGetCheckNameAvailability"></a>
# **botsGetCheckNameAvailability**
> CheckNameAvailabilityResponseBody botsGetCheckNameAvailability(apiVersion, parameters)



Check whether a bot name is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotApi apiInstance = new BotApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    CheckNameAvailabilityRequestBody parameters = new CheckNameAvailabilityRequestBody(); // CheckNameAvailabilityRequestBody | The request body parameters to provide for the check name availability request
    try {
      CheckNameAvailabilityResponseBody result = apiInstance.botsGetCheckNameAvailability(apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotApi#botsGetCheckNameAvailability");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**CheckNameAvailabilityRequestBody**](CheckNameAvailabilityRequestBody.md)| The request body parameters to provide for the check name availability request | |

### Return type

[**CheckNameAvailabilityResponseBody**](CheckNameAvailabilityResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully. For other errors (e.g. internal errors) use the appropriate HTTP error code. The nextLink field is expected to point to the URL the client should use to fetch the next page (per server side paging). This matches the OData guidelines for paged responses. If a resource provider does not support paging, it should return the same body but leave nextLink empty for future compatibility. For a detailed explanation of each field in the response body, please refer to the request body description in the PUT resource section.  |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="botsList"></a>
# **botsList**
> BotResponseList botsList(apiVersion, subscriptionId)



Returns all the resources of a particular type belonging to a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotApi apiInstance = new BotApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      BotResponseList result = apiInstance.botsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotApi#botsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**BotResponseList**](BotResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully. For other errors (e.g. internal errors) use the appropriate HTTP error code. The nextLink field is expected to point to the URL the client should use to fetch the next page (per server side paging). This matches the OData guidelines for paged responses. If a resource provider does not support paging, it should return the same body but leave nextLink empty for future compatibility. For a detailed explanation of each field in the response body, please refer to the request body description in the PUT resource section.  |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="botsListByResourceGroup"></a>
# **botsListByResourceGroup**
> BotResponseList botsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Returns all the resources of a particular type belonging to a resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotApi apiInstance = new BotApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      BotResponseList result = apiInstance.botsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotApi#botsListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**BotResponseList**](BotResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully. For other errors (e.g. internal errors) use the appropriate HTTP error code. The nextLink field is expected to point to the URL the client should use to fetch the next page (per server side paging). This matches the OData guidelines for paged responses here. If a resource provider does not support paging, it should return the same body (JSON object with “value” property) but omit nextLink entirely (or set to null, *not* empty string) for future compatibility. The nextLink should be implemented using following query parameters: · skipToken: opaque token that allows the resource provider to skip resources already enumerated. This value is defined and returned by the RP after first request via nextLink. · top: the optional client query parameter which defines the maximum number of records to be returned by the server. Implementation details: · NextLink may include all the query parameters (specifically OData $filter) used by the client in the first query.  · Server may return less records than requested with nextLink. Returning zero records with NextLink is an acceptable response.  Clients must fetch records until the nextLink is not returned back / null. Clients should never rely on number of returned records to determinate if pagination is completed. |  -  |
| **0** | Error response describing why the operation failed. If the resource group does not exist, 404 (NotFound) will be returned. |  -  |

<a id="botsUpdate"></a>
# **botsUpdate**
> Bot botsUpdate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters)



Updates a Bot Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotApi apiInstance = new BotApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    Bot parameters = new Bot(); // Bot | The parameters to provide for the created bot.
    try {
      Bot result = apiInstance.botsUpdate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotApi#botsUpdate");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **parameters** | [**Bot**](Bot.md)| The parameters to provide for the created bot. | |

### Return type

[**Bot**](Bot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully.  |  -  |
| **201** | If resource is updated successfully, the service should return 201 (Created). Execution to continue asynchronously. |  -  |
| **0** | Error response describing why the operation failed. If the resource group *or* resource does not exist, 404 (NotFound) should be returned. |  -  |

