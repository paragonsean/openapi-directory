# IoTSecuritySolutionsAnalyticsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts/{aggregatedAlertName}/dismiss |  |
| [**ioTSecuritySolutionsAnalyticsAggregatedAlertGet**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsAggregatedAlertGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts/{aggregatedAlertName} |  |
| [**ioTSecuritySolutionsAnalyticsAggregatedAlertsList**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsAggregatedAlertsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedAlerts |  |
| [**ioTSecuritySolutionsAnalyticsGetAll**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsGetAll) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels |  |
| [**ioTSecuritySolutionsAnalyticsGetDefault**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsGetDefault) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default |  |
| [**ioTSecuritySolutionsAnalyticsRecommendationGet**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsRecommendationGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedRecommendations/{aggregatedRecommendationName} |  |
| [**ioTSecuritySolutionsAnalyticsRecommendationsList**](IoTSecuritySolutionsAnalyticsApi.md#ioTSecuritySolutionsAnalyticsRecommendationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/iotSecuritySolutions/{solutionName}/analyticsModels/default/aggregatedRecommendations |  |


<a id="ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss"></a>
# **ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss**
> ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName)



Security Analytics of a security solution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTSecuritySolutionsAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTSecuritySolutionsAnalyticsApi apiInstance = new IoTSecuritySolutionsAnalyticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The solution manager name
    String aggregatedAlertName = "aggregatedAlertName_example"; // String | Identifier of the aggregated alert
    try {
      apiInstance.ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTSecuritySolutionsAnalyticsApi#ioTSecuritySolutionsAnalyticsAggregatedAlertDismiss");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **solutionName** | **String**| The solution manager name | |
| **aggregatedAlertName** | **String**| Identifier of the aggregated alert | |

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
| **200** | Dismissed |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ioTSecuritySolutionsAnalyticsAggregatedAlertGet"></a>
# **ioTSecuritySolutionsAnalyticsAggregatedAlertGet**
> IoTSecurityAggregatedAlert ioTSecuritySolutionsAnalyticsAggregatedAlertGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName)



Security Analytics of a security solution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTSecuritySolutionsAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTSecuritySolutionsAnalyticsApi apiInstance = new IoTSecuritySolutionsAnalyticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The solution manager name
    String aggregatedAlertName = "aggregatedAlertName_example"; // String | Identifier of the aggregated alert
    try {
      IoTSecurityAggregatedAlert result = apiInstance.ioTSecuritySolutionsAnalyticsAggregatedAlertGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedAlertName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTSecuritySolutionsAnalyticsApi#ioTSecuritySolutionsAnalyticsAggregatedAlertGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **solutionName** | **String**| The solution manager name | |
| **aggregatedAlertName** | **String**| Identifier of the aggregated alert | |

### Return type

[**IoTSecurityAggregatedAlert**](IoTSecurityAggregatedAlert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ioTSecuritySolutionsAnalyticsAggregatedAlertsList"></a>
# **ioTSecuritySolutionsAnalyticsAggregatedAlertsList**
> IoTSecurityAggregatedAlertList ioTSecuritySolutionsAnalyticsAggregatedAlertsList(apiVersion, subscriptionId, resourceGroupName, solutionName, $top)



Security Analytics of a security solution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTSecuritySolutionsAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTSecuritySolutionsAnalyticsApi apiInstance = new IoTSecuritySolutionsAnalyticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The solution manager name
    Integer $top = 56; // Integer | The number of results to retrieve.
    try {
      IoTSecurityAggregatedAlertList result = apiInstance.ioTSecuritySolutionsAnalyticsAggregatedAlertsList(apiVersion, subscriptionId, resourceGroupName, solutionName, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTSecuritySolutionsAnalyticsApi#ioTSecuritySolutionsAnalyticsAggregatedAlertsList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **solutionName** | **String**| The solution manager name | |
| **$top** | **Integer**| The number of results to retrieve. | [optional] |

### Return type

[**IoTSecurityAggregatedAlertList**](IoTSecurityAggregatedAlertList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ioTSecuritySolutionsAnalyticsGetAll"></a>
# **ioTSecuritySolutionsAnalyticsGetAll**
> IoTSecuritySolutionAnalyticsModelList ioTSecuritySolutionsAnalyticsGetAll(apiVersion, subscriptionId, resourceGroupName, solutionName)



Security Analytics of a security solution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTSecuritySolutionsAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTSecuritySolutionsAnalyticsApi apiInstance = new IoTSecuritySolutionsAnalyticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The solution manager name
    try {
      IoTSecuritySolutionAnalyticsModelList result = apiInstance.ioTSecuritySolutionsAnalyticsGetAll(apiVersion, subscriptionId, resourceGroupName, solutionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTSecuritySolutionsAnalyticsApi#ioTSecuritySolutionsAnalyticsGetAll");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **solutionName** | **String**| The solution manager name | |

### Return type

[**IoTSecuritySolutionAnalyticsModelList**](IoTSecuritySolutionAnalyticsModelList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ioTSecuritySolutionsAnalyticsGetDefault"></a>
# **ioTSecuritySolutionsAnalyticsGetDefault**
> IoTSecuritySolutionAnalyticsModel ioTSecuritySolutionsAnalyticsGetDefault(apiVersion, subscriptionId, resourceGroupName, solutionName)



Security Analytics of a security solution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTSecuritySolutionsAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTSecuritySolutionsAnalyticsApi apiInstance = new IoTSecuritySolutionsAnalyticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The solution manager name
    try {
      IoTSecuritySolutionAnalyticsModel result = apiInstance.ioTSecuritySolutionsAnalyticsGetDefault(apiVersion, subscriptionId, resourceGroupName, solutionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTSecuritySolutionsAnalyticsApi#ioTSecuritySolutionsAnalyticsGetDefault");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **solutionName** | **String**| The solution manager name | |

### Return type

[**IoTSecuritySolutionAnalyticsModel**](IoTSecuritySolutionAnalyticsModel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ioTSecuritySolutionsAnalyticsRecommendationGet"></a>
# **ioTSecuritySolutionsAnalyticsRecommendationGet**
> IoTSecurityAggregatedRecommendation ioTSecuritySolutionsAnalyticsRecommendationGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedRecommendationName)



Security Analytics of a security solution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTSecuritySolutionsAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTSecuritySolutionsAnalyticsApi apiInstance = new IoTSecuritySolutionsAnalyticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The solution manager name
    String aggregatedRecommendationName = "aggregatedRecommendationName_example"; // String | Identifier of the aggregated recommendation
    try {
      IoTSecurityAggregatedRecommendation result = apiInstance.ioTSecuritySolutionsAnalyticsRecommendationGet(apiVersion, subscriptionId, resourceGroupName, solutionName, aggregatedRecommendationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTSecuritySolutionsAnalyticsApi#ioTSecuritySolutionsAnalyticsRecommendationGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **solutionName** | **String**| The solution manager name | |
| **aggregatedRecommendationName** | **String**| Identifier of the aggregated recommendation | |

### Return type

[**IoTSecurityAggregatedRecommendation**](IoTSecurityAggregatedRecommendation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ioTSecuritySolutionsAnalyticsRecommendationsList"></a>
# **ioTSecuritySolutionsAnalyticsRecommendationsList**
> IoTSecurityAggregatedRecommendationList ioTSecuritySolutionsAnalyticsRecommendationsList(apiVersion, subscriptionId, resourceGroupName, solutionName, $top)



Security Analytics of a security solution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IoTSecuritySolutionsAnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IoTSecuritySolutionsAnalyticsApi apiInstance = new IoTSecuritySolutionsAnalyticsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String solutionName = "solutionName_example"; // String | The solution manager name
    Integer $top = 56; // Integer | The number of results to retrieve.
    try {
      IoTSecurityAggregatedRecommendationList result = apiInstance.ioTSecuritySolutionsAnalyticsRecommendationsList(apiVersion, subscriptionId, resourceGroupName, solutionName, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IoTSecuritySolutionsAnalyticsApi#ioTSecuritySolutionsAnalyticsRecommendationsList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **solutionName** | **String**| The solution manager name | |
| **$top** | **Integer**| The number of results to retrieve. | [optional] |

### Return type

[**IoTSecurityAggregatedRecommendationList**](IoTSecurityAggregatedRecommendationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

