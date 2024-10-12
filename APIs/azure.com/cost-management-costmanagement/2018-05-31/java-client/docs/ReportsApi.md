# ReportsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportConfigCreateOrUpdate**](ReportsApi.md#reportConfigCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} |  |
| [**reportConfigCreateOrUpdateByResourceGroupName**](ReportsApi.md#reportConfigCreateOrUpdateByResourceGroupName) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} |  |
| [**reportConfigDelete**](ReportsApi.md#reportConfigDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} |  |
| [**reportConfigDeleteByResourceGroupName**](ReportsApi.md#reportConfigDeleteByResourceGroupName) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} |  |
| [**reportConfigGet**](ReportsApi.md#reportConfigGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} |  |
| [**reportConfigGetByResourceGroupName**](ReportsApi.md#reportConfigGetByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} |  |
| [**reportConfigList**](ReportsApi.md#reportConfigList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reportconfigs |  |
| [**reportConfigListByResourceGroupName**](ReportsApi.md#reportConfigListByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reportconfigs |  |


<a id="reportConfigCreateOrUpdate"></a>
# **reportConfigCreateOrUpdate**
> ReportConfig reportConfigCreateOrUpdate(apiVersion, subscriptionId, reportConfigName, parameters)



The operation to create or update a report config. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String reportConfigName = "reportConfigName_example"; // String | Report Config Name.
    ReportConfig parameters = new ReportConfig(); // ReportConfig | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      ReportConfig result = apiInstance.reportConfigCreateOrUpdate(apiVersion, subscriptionId, reportConfigName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportConfigCreateOrUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **reportConfigName** | **String**| Report Config Name. | |
| **parameters** | [**ReportConfig**](ReportConfig.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | |

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportConfigCreateOrUpdateByResourceGroupName"></a>
# **reportConfigCreateOrUpdateByResourceGroupName**
> ReportConfig reportConfigCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName, parameters)



The operation to create or update a report config. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String reportConfigName = "reportConfigName_example"; // String | Report Config Name.
    ReportConfig parameters = new ReportConfig(); // ReportConfig | Parameters supplied to the CreateOrUpdate Report Config operation.
    try {
      ReportConfig result = apiInstance.reportConfigCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportConfigCreateOrUpdateByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **reportConfigName** | **String**| Report Config Name. | |
| **parameters** | [**ReportConfig**](ReportConfig.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | |

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportConfigDelete"></a>
# **reportConfigDelete**
> reportConfigDelete(apiVersion, subscriptionId, reportConfigName)



The operation to delete a report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String reportConfigName = "reportConfigName_example"; // String | Report Config Name.
    try {
      apiInstance.reportConfigDelete(apiVersion, subscriptionId, reportConfigName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportConfigDelete");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **reportConfigName** | **String**| Report Config Name. | |

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
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportConfigDeleteByResourceGroupName"></a>
# **reportConfigDeleteByResourceGroupName**
> reportConfigDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName)



The operation to delete a report config.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String reportConfigName = "reportConfigName_example"; // String | Report Config Name.
    try {
      apiInstance.reportConfigDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportConfigDeleteByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **reportConfigName** | **String**| Report Config Name. | |

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
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportConfigGet"></a>
# **reportConfigGet**
> ReportConfig reportConfigGet(apiVersion, subscriptionId, reportConfigName)



Gets the report config for a subscription by report config name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String reportConfigName = "reportConfigName_example"; // String | Report Config Name.
    try {
      ReportConfig result = apiInstance.reportConfigGet(apiVersion, subscriptionId, reportConfigName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportConfigGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **reportConfigName** | **String**| Report Config Name. | |

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportConfigGetByResourceGroupName"></a>
# **reportConfigGetByResourceGroupName**
> ReportConfig reportConfigGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName)



Gets the report config for a resource group under a subscription by report config name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    String reportConfigName = "reportConfigName_example"; // String | Report Config Name.
    try {
      ReportConfig result = apiInstance.reportConfigGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportConfigGetByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |
| **reportConfigName** | **String**| Report Config Name. | |

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportConfigList"></a>
# **reportConfigList**
> ReportConfigListResult reportConfigList(apiVersion, subscriptionId)



Lists all report configs for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      ReportConfigListResult result = apiInstance.reportConfigList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportConfigList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**ReportConfigListResult**](ReportConfigListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="reportConfigListByResourceGroupName"></a>
# **reportConfigListByResourceGroupName**
> ReportConfigListResult reportConfigListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName)



Lists all report configs for a resource group under a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
    try {
      ReportConfigListResult result = apiInstance.reportConfigListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportConfigListByResourceGroupName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **resourceGroupName** | **String**| Azure Resource Group Name. | |

### Return type

[**ReportConfigListResult**](ReportConfigListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

