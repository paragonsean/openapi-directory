# ConfigHistoryApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryConfigurationHistoryUpdates**](ConfigHistoryApi.md#queryConfigurationHistoryUpdates) | **GET** /config/history/list_updates | View a list of filtered configuration updates |
| [**retrieveConfigurationValues**](ConfigHistoryApi.md#retrieveConfigurationValues) | **GET** /config/history/ondate | View a list of configurations and their values on a given date |


<a id="queryConfigurationHistoryUpdates"></a>
# **queryConfigurationHistoryUpdates**
> ConfigurationUpdateSummaryListResponse queryConfigurationHistoryUpdates(limit, offset, apiUser, nodeId, namespace, name, source, afterTime, beforeTime)

View a list of filtered configuration updates

View a list of cluster configuration options that have updated within a specified time window.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ConfigHistoryApi apiInstance = new ConfigHistoryApi(defaultClient);
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Ignore these many matches in the beginning.
    String apiUser = "apiUser_example"; // String | The username of the account. Applies a filter to the configuration updates performed by the specified username.
    String nodeId = "nodeId_example"; // String | The node ID. Applies a filter to the configuration updates for the specified node. When no node_id is specified, the filter shows both local and cluster-wide configurations. Specify 'cluster' for filtering out cluster-wide configuration updates.
    String namespace = "namespace_example"; // String | The configuration namespace. Applies a filter to the configuration updates for the specified namespace.
    String name = "name_example"; // String | Name of the configuration. Applies a filter to the configuration updates for the specified configuration name.
    String source = "Unknown"; // String | Source for configuration updates. Applies a filter to the configuration updates for the specified source.
    OffsetDateTime afterTime = OffsetDateTime.now(); // OffsetDateTime | The earliest time configuration history is needed. Applies a filter that only shows configuration updates after the specified time.
    OffsetDateTime beforeTime = OffsetDateTime.now(); // OffsetDateTime | The latest time configuration history is needed. Applies filter to display only configuration updates prior to the specified time. The default value is the current time.
    try {
      ConfigurationUpdateSummaryListResponse result = apiInstance.queryConfigurationHistoryUpdates(limit, offset, apiUser, nodeId, namespace, name, source, afterTime, beforeTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigHistoryApi#queryConfigurationHistoryUpdates");
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
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Ignore these many matches in the beginning. | [optional] |
| **apiUser** | **String**| The username of the account. Applies a filter to the configuration updates performed by the specified username. | [optional] |
| **nodeId** | **String**| The node ID. Applies a filter to the configuration updates for the specified node. When no node_id is specified, the filter shows both local and cluster-wide configurations. Specify &#39;cluster&#39; for filtering out cluster-wide configuration updates. | [optional] |
| **namespace** | **String**| The configuration namespace. Applies a filter to the configuration updates for the specified namespace. | [optional] |
| **name** | **String**| Name of the configuration. Applies a filter to the configuration updates for the specified configuration name. | [optional] |
| **source** | **String**| Source for configuration updates. Applies a filter to the configuration updates for the specified source. | [optional] [enum: Unknown, CustomerApi, Upgrade, ResetNode, Software, Init] |
| **afterTime** | **OffsetDateTime**| The earliest time configuration history is needed. Applies a filter that only shows configuration updates after the specified time. | [optional] |
| **beforeTime** | **OffsetDateTime**| The latest time configuration history is needed. Applies filter to display only configuration updates prior to the specified time. The default value is the current time. | [optional] |

### Return type

[**ConfigurationUpdateSummaryListResponse**](ConfigurationUpdateSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A summary of configuration updates that satisfy the filters in place. |  -  |

<a id="retrieveConfigurationValues"></a>
# **retrieveConfigurationValues**
> ConfigurationSummaryListResponse retrieveConfigurationValues(namespace, onDate, limit, offset, nodeId, name)

View a list of configurations and their values on a given date

View a list of configurations and their values on a given date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ConfigHistoryApi apiInstance = new ConfigHistoryApi(defaultClient);
    String namespace = "namespace_example"; // String | The configuration namespace. Applies a filter to the configuration updates for the specified namespace.
    OffsetDateTime onDate = OffsetDateTime.now(); // OffsetDateTime | The timestamp for which to retrieve configuration values.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Ignore these many matches in the beginning.
    String nodeId = "nodeId_example"; // String | The name of the node that require configuration values. Applies a filter specific to the name of node. When no node_id is specified, the filter shows both local and cluster-wide configurations.
    String name = "name_example"; // String | The name of the configuration option. Applies a filter to the configuration updates for the specified option.
    try {
      ConfigurationSummaryListResponse result = apiInstance.retrieveConfigurationValues(namespace, onDate, limit, offset, nodeId, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigHistoryApi#retrieveConfigurationValues");
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
| **namespace** | **String**| The configuration namespace. Applies a filter to the configuration updates for the specified namespace. | |
| **onDate** | **OffsetDateTime**| The timestamp for which to retrieve configuration values. | |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Ignore these many matches in the beginning. | [optional] |
| **nodeId** | **String**| The name of the node that require configuration values. Applies a filter specific to the name of node. When no node_id is specified, the filter shows both local and cluster-wide configurations. | [optional] |
| **name** | **String**| The name of the configuration option. Applies a filter to the configuration updates for the specified option. | [optional] |

### Return type

[**ConfigurationSummaryListResponse**](ConfigurationSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the values of configuration options, as of a specified timestamp, that match the filters in place. |  -  |

