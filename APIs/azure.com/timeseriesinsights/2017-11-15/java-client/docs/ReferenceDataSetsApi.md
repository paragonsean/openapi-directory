# ReferenceDataSetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**referenceDataSetsCreateOrUpdate**](ReferenceDataSetsApi.md#referenceDataSetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName} |  |
| [**referenceDataSetsDelete**](ReferenceDataSetsApi.md#referenceDataSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName} |  |
| [**referenceDataSetsGet**](ReferenceDataSetsApi.md#referenceDataSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName} |  |
| [**referenceDataSetsListByEnvironment**](ReferenceDataSetsApi.md#referenceDataSetsListByEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets |  |
| [**referenceDataSetsUpdate**](ReferenceDataSetsApi.md#referenceDataSetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}/referenceDataSets/{referenceDataSetName} |  |


<a id="referenceDataSetsCreateOrUpdate"></a>
# **referenceDataSetsCreateOrUpdate**
> ReferenceDataSetResource referenceDataSetsCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion, parameters)



Create or update a reference data set in the specified environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataSetsApi apiInstance = new ReferenceDataSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String referenceDataSetName = "referenceDataSetName_example"; // String | Name of the reference data set.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    ReferenceDataSetCreateOrUpdateParameters parameters = new ReferenceDataSetCreateOrUpdateParameters(); // ReferenceDataSetCreateOrUpdateParameters | Parameters for creating a reference data set.
    try {
      ReferenceDataSetResource result = apiInstance.referenceDataSetsCreateOrUpdate(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataSetsApi#referenceDataSetsCreateOrUpdate");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | |
| **referenceDataSetName** | **String**| Name of the reference data set. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**ReferenceDataSetCreateOrUpdateParameters**](ReferenceDataSetCreateOrUpdateParameters.md)| Parameters for creating a reference data set. | |

### Return type

[**ReferenceDataSetResource**](ReferenceDataSetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The existing reference data set definition was successfully updated. |  -  |
| **201** | The reference data set was successfully created. |  -  |
| **0** | HTTP 400 (Bad Request): The given reference data set request body is invalid; See the error code and message in the response for details. |  -  |

<a id="referenceDataSetsDelete"></a>
# **referenceDataSetsDelete**
> referenceDataSetsDelete(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion)



Deletes the reference data set with the specified name in the specified subscription, resource group, and environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataSetsApi apiInstance = new ReferenceDataSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String referenceDataSetName = "referenceDataSetName_example"; // String | The name of the Time Series Insights reference data set associated with the specified environment.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.referenceDataSetsDelete(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataSetsApi#referenceDataSetsDelete");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | |
| **referenceDataSetName** | **String**| The name of the Time Series Insights reference data set associated with the specified environment. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

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
| **200** | The reference data set was successfully deleted. |  -  |
| **204** | The reference data set was successfully deleted. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, environment, or reference data set could not be found. |  -  |

<a id="referenceDataSetsGet"></a>
# **referenceDataSetsGet**
> ReferenceDataSetResource referenceDataSetsGet(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion)



Gets the reference data set with the specified name in the specified environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataSetsApi apiInstance = new ReferenceDataSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String referenceDataSetName = "referenceDataSetName_example"; // String | The name of the Time Series Insights reference data set associated with the specified environment.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      ReferenceDataSetResource result = apiInstance.referenceDataSetsGet(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataSetsApi#referenceDataSetsGet");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | |
| **referenceDataSetName** | **String**| The name of the Time Series Insights reference data set associated with the specified environment. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**ReferenceDataSetResource**](ReferenceDataSetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The reference data set definition was successfully retrieved and is in the response. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, environment, or reference data set could not be found. |  -  |

<a id="referenceDataSetsListByEnvironment"></a>
# **referenceDataSetsListByEnvironment**
> ReferenceDataSetListResponse referenceDataSetsListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion)



Lists all the available reference data sets associated with the subscription and within the specified resource group and environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataSetsApi apiInstance = new ReferenceDataSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      ReferenceDataSetListResponse result = apiInstance.referenceDataSetsListByEnvironment(subscriptionId, resourceGroupName, environmentName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataSetsApi#referenceDataSetsListByEnvironment");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**ReferenceDataSetListResponse**](ReferenceDataSetListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reference data sets returned successfully. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, or environment could not be found. |  -  |

<a id="referenceDataSetsUpdate"></a>
# **referenceDataSetsUpdate**
> ReferenceDataSetResource referenceDataSetsUpdate(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion, referenceDataSetUpdateParameters)



Updates the reference data set with the specified name in the specified subscription, resource group, and environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataSetsApi apiInstance = new ReferenceDataSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String environmentName = "environmentName_example"; // String | The name of the Time Series Insights environment associated with the specified resource group.
    String referenceDataSetName = "referenceDataSetName_example"; // String | The name of the Time Series Insights reference data set associated with the specified environment.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    ReferenceDataSetUpdateParameters referenceDataSetUpdateParameters = new ReferenceDataSetUpdateParameters(); // ReferenceDataSetUpdateParameters | Request object that contains the updated information for the reference data set.
    try {
      ReferenceDataSetResource result = apiInstance.referenceDataSetsUpdate(subscriptionId, resourceGroupName, environmentName, referenceDataSetName, apiVersion, referenceDataSetUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataSetsApi#referenceDataSetsUpdate");
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
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **environmentName** | **String**| The name of the Time Series Insights environment associated with the specified resource group. | |
| **referenceDataSetName** | **String**| The name of the Time Series Insights reference data set associated with the specified environment. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **referenceDataSetUpdateParameters** | [**ReferenceDataSetUpdateParameters**](ReferenceDataSetUpdateParameters.md)| Request object that contains the updated information for the reference data set. | |

### Return type

[**ReferenceDataSetResource**](ReferenceDataSetResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The reference data set definition was successfully updated and is in the response. |  -  |
| **0** | HTTP 404 (Not Found): The subscription, resource group, environment, or reference data set could not be found. |  -  |

