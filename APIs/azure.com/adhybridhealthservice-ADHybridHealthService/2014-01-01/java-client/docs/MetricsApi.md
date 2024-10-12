# MetricsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceGetMetrics**](MetricsApi.md#serviceGetMetrics) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metrics/{metricName}/groups/{groupName} |  |
| [**serviceMembersGetConnectorMetadata**](MetricsApi.md#serviceMembersGetConnectorMetadata) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/metrics/{metricName} |  |
| [**serviceMembersGetMetrics**](MetricsApi.md#serviceMembersGetMetrics) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/metrics/{metricName}/groups/{groupName} |  |
| [**servicesGetMetricMetadata**](MetricsApi.md#servicesGetMetricMetadata) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metricmetadata/{metricName} |  |
| [**servicesGetMetricMetadataForGroup**](MetricsApi.md#servicesGetMetricMetadataForGroup) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metricmetadata/{metricName}/groups/{groupName} |  |
| [**servicesListMetricMetadata**](MetricsApi.md#servicesListMetricMetadata) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metricmetadata |  |
| [**servicesListMetricsAverage**](MetricsApi.md#servicesListMetricsAverage) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metrics/{metricName}/groups/{groupName}/average |  |
| [**servicesListMetricsSum**](MetricsApi.md#servicesListMetricsSum) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metrics/{metricName}/groups/{groupName}/sum |  |


<a id="serviceGetMetrics"></a>
# **serviceGetMetrics**
> MetricSets serviceGetMetrics(serviceName, metricName, groupName, apiVersion, groupKey, fromDate, toDate)



Gets the server related metrics for a given metric and group combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String groupName = "groupName_example"; // String | The group name
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String groupKey = "groupKey_example"; // String | The group key
    OffsetDateTime fromDate = OffsetDateTime.now(); // OffsetDateTime | The start date.
    OffsetDateTime toDate = OffsetDateTime.now(); // OffsetDateTime | The end date.
    try {
      MetricSets result = apiInstance.serviceGetMetrics(serviceName, metricName, groupName, apiVersion, groupKey, fromDate, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#serviceGetMetrics");
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
| **serviceName** | **String**| The name of the service. | |
| **metricName** | **String**| The metric name | |
| **groupName** | **String**| The group name | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **groupKey** | **String**| The group key | [optional] |
| **fromDate** | **OffsetDateTime**| The start date. | [optional] |
| **toDate** | **OffsetDateTime**| The end date. | [optional] |

### Return type

[**MetricSets**](MetricSets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric sets for a given service. |  -  |

<a id="serviceMembersGetConnectorMetadata"></a>
# **serviceMembersGetConnectorMetadata**
> ConnectorMetadata serviceMembersGetConnectorMetadata(serviceName, serviceMemberId, metricName, apiVersion)



Gets the list of connectors and run profile names.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The service member id.
    String metricName = "metricName_example"; // String | The name of the metric.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ConnectorMetadata result = apiInstance.serviceMembersGetConnectorMetadata(serviceName, serviceMemberId, metricName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#serviceMembersGetConnectorMetadata");
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
| **serviceName** | **String**| The name of the service. | |
| **serviceMemberId** | **UUID**| The service member id. | |
| **metricName** | **String**| The name of the metric. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**ConnectorMetadata**](ConnectorMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the list of connectors and run profile names for the given service and service member. |  -  |

<a id="serviceMembersGetMetrics"></a>
# **serviceMembersGetMetrics**
> MetricSets serviceMembersGetMetrics(serviceName, metricName, groupName, serviceMemberId, apiVersion, groupKey, fromDate, toDate)



Gets the server related metrics for a given metric and group combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String groupName = "groupName_example"; // String | The group name
    UUID serviceMemberId = UUID.randomUUID(); // UUID | The server id.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String groupKey = "groupKey_example"; // String | The group key
    OffsetDateTime fromDate = OffsetDateTime.now(); // OffsetDateTime | The start date.
    OffsetDateTime toDate = OffsetDateTime.now(); // OffsetDateTime | The end date.
    try {
      MetricSets result = apiInstance.serviceMembersGetMetrics(serviceName, metricName, groupName, serviceMemberId, apiVersion, groupKey, fromDate, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#serviceMembersGetMetrics");
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
| **serviceName** | **String**| The name of the service. | |
| **metricName** | **String**| The metric name | |
| **groupName** | **String**| The group name | |
| **serviceMemberId** | **UUID**| The server id. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **groupKey** | **String**| The group key | [optional] |
| **fromDate** | **OffsetDateTime**| The start date. | [optional] |
| **toDate** | **OffsetDateTime**| The end date. | [optional] |

### Return type

[**MetricSets**](MetricSets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of metric sets for a given metric. |  -  |

<a id="servicesGetMetricMetadata"></a>
# **servicesGetMetricMetadata**
> MetricMetadata servicesGetMetricMetadata(serviceName, metricName, apiVersion)



Gets the service related metrics information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      MetricMetadata result = apiInstance.servicesGetMetricMetadata(serviceName, metricName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#servicesGetMetricMetadata");
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
| **serviceName** | **String**| The name of the service. | |
| **metricName** | **String**| The metric name | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**MetricMetadata**](MetricMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric metadata for a given metric. |  -  |

<a id="servicesGetMetricMetadataForGroup"></a>
# **servicesGetMetricMetadataForGroup**
> MetricSets servicesGetMetricMetadataForGroup(serviceName, metricName, groupName, apiVersion, groupKey, fromDate, toDate)



Gets the service related metrics for a given metric and group combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String groupName = "groupName_example"; // String | The group name
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String groupKey = "groupKey_example"; // String | The group key
    OffsetDateTime fromDate = OffsetDateTime.now(); // OffsetDateTime | The start date.
    OffsetDateTime toDate = OffsetDateTime.now(); // OffsetDateTime | The end date.
    try {
      MetricSets result = apiInstance.servicesGetMetricMetadataForGroup(serviceName, metricName, groupName, apiVersion, groupKey, fromDate, toDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#servicesGetMetricMetadataForGroup");
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
| **serviceName** | **String**| The name of the service. | |
| **metricName** | **String**| The metric name | |
| **groupName** | **String**| The group name | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **groupKey** | **String**| The group key | [optional] |
| **fromDate** | **OffsetDateTime**| The start date. | [optional] |
| **toDate** | **OffsetDateTime**| The end date. | [optional] |

### Return type

[**MetricSets**](MetricSets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The metric sets for a given service and group. |  -  |

<a id="servicesListMetricMetadata"></a>
# **servicesListMetricMetadata**
> MetricMetadataList servicesListMetricMetadata(serviceName, apiVersion, $filter, perfCounter)



Gets the service related metrics information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The metric metadata property filter to apply.
    Boolean perfCounter = true; // Boolean | Indicates if only performance counter metrics are requested.
    try {
      MetricMetadataList result = apiInstance.servicesListMetricMetadata(serviceName, apiVersion, $filter, perfCounter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#servicesListMetricMetadata");
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
| **serviceName** | **String**| The name of the service. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The metric metadata property filter to apply. | [optional] |
| **perfCounter** | **Boolean**| Indicates if only performance counter metrics are requested. | [optional] |

### Return type

[**MetricMetadataList**](MetricMetadataList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of metric metadata for a given service. |  -  |

<a id="servicesListMetricsAverage"></a>
# **servicesListMetricsAverage**
> Metrics servicesListMetricsAverage(serviceName, metricName, groupName, apiVersion)



Gets the average of the metric values for a given metric and group combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String groupName = "groupName_example"; // String | The group name
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Metrics result = apiInstance.servicesListMetricsAverage(serviceName, metricName, groupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#servicesListMetricsAverage");
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
| **serviceName** | **String**| The name of the service. | |
| **metricName** | **String**| The metric name | |
| **groupName** | **String**| The group name | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of average metrics for a given service. |  -  |

<a id="servicesListMetricsSum"></a>
# **servicesListMetricsSum**
> Metrics servicesListMetricsSum(serviceName, metricName, groupName, apiVersion)



Gets the sum of the metric values for a given metric and group combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String serviceName = "serviceName_example"; // String | The name of the service.
    String metricName = "metricName_example"; // String | The metric name
    String groupName = "groupName_example"; // String | The group name
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      Metrics result = apiInstance.servicesListMetricsSum(serviceName, metricName, groupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#servicesListMetricsSum");
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
| **serviceName** | **String**| The name of the service. | |
| **metricName** | **String**| The metric name | |
| **groupName** | **String**| The group name | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**Metrics**](Metrics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of metrics for a given service. |  -  |

