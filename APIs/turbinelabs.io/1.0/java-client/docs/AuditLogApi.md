# AuditLogApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changelogAdhocGet**](AuditLogApi.md#changelogAdhocGet) | **GET** /changelog/adhoc | Allows an arbitrary filter to be specified and applied to the org\\&#39;s change log. |
| [**changelogClusterGraphClusterKeyGet**](AuditLogApi.md#changelogClusterGraphClusterKeyGet) | **GET** /changelog/cluster-graph/{clusterKey} | get changes related to the indicated cluster |
| [**changelogDomainGraphDomainKeyGet**](AuditLogApi.md#changelogDomainGraphDomainKeyGet) | **GET** /changelog/domain-graph/{domainKey} | get changes related to the indicated domain |
| [**changelogRouteGraphRouteKeyGet**](AuditLogApi.md#changelogRouteGraphRouteKeyGet) | **GET** /changelog/route-graph/{routeKey} | get changes related to the indicated route |
| [**changelogSharedRulesGraphSharedRulesKeyGet**](AuditLogApi.md#changelogSharedRulesGraphSharedRulesKeyGet) | **GET** /changelog/shared-rules-graph/{sharedRulesKey} | get changes related to the indicated SharedRules |
| [**changelogZoneZoneKeyGet**](AuditLogApi.md#changelogZoneZoneKeyGet) | **GET** /changelog/zone/{zoneKey} | get changes in a specified zone |


<a id="changelogAdhocGet"></a>
# **changelogAdhocGet**
> PaginatedChangeDescriptions changelogAdhocGet(filter)

Allows an arbitrary filter to be specified and applied to the org\\&#39;s change log.

Perform an adhoc query against the change log for your org. The filter is a JSON encoded FilterSum as defined in this file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AuditLogApi apiInstance = new AuditLogApi(defaultClient);
    String filter = "filter_example"; // String | Encoded FilterSums representing the query you would like to execute. See object definition for details.
    try {
      PaginatedChangeDescriptions result = apiInstance.changelogAdhocGet(filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogApi#changelogAdhocGet");
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
| **filter** | **String**| Encoded FilterSums representing the query you would like to execute. See object definition for details. | [optional] |

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of changes that meet the provided filter. |  -  |
| **0** | Unexpected error |  -  |

<a id="changelogClusterGraphClusterKeyGet"></a>
# **changelogClusterGraphClusterKeyGet**
> PaginatedChangeDescriptions changelogClusterGraphClusterKeyGet(clusterKey, start, end, maxResults, refId, direction)

get changes related to the indicated cluster

Gets all changes to a cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AuditLogApi apiInstance = new AuditLogApi(defaultClient);
    String clusterKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the cluster key to see an audit log for
    BigDecimal start = new BigDecimal(78); // BigDecimal | The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    BigDecimal end = new BigDecimal(78); // BigDecimal | The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    BigDecimal maxResults = new BigDecimal(78); // BigDecimal | Determines how many ChangeDescription object should be returned to the calling code. 
    String refId = "refId_example"; // String | When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
    String direction = "before"; // String | If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
    try {
      PaginatedChangeDescriptions result = apiInstance.changelogClusterGraphClusterKeyGet(clusterKey, start, end, maxResults, refId, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogApi#changelogClusterGraphClusterKeyGet");
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
| **clusterKey** | **String**| the cluster key to see an audit log for | |
| **start** | **BigDecimal**| The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] |
| **end** | **BigDecimal**| The end of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] |
| **maxResults** | **BigDecimal**| Determines how many ChangeDescription object should be returned to the calling code.  | [optional] |
| **refId** | **String**| When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument).  | [optional] |
| **direction** | **String**| If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID.  | [optional] [enum: before, after] |

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of changes occurring during the requested window. |  -  |
| **0** | Unexpected error |  -  |

<a id="changelogDomainGraphDomainKeyGet"></a>
# **changelogDomainGraphDomainKeyGet**
> PaginatedChangeDescriptions changelogDomainGraphDomainKeyGet(domainKey, start, end, maxResults, refId, direction)

get changes related to the indicated domain

Gets all changes to a domain, the proxies that front the specified domain, routes within that domain, the shared rules of each route, the clusters connected via route or shared rules. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AuditLogApi apiInstance = new AuditLogApi(defaultClient);
    String domainKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the domain key to see an audit log for
    BigDecimal start = new BigDecimal(78); // BigDecimal | The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    BigDecimal end = new BigDecimal(78); // BigDecimal | The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    BigDecimal maxResults = new BigDecimal(78); // BigDecimal | Determines how many ChangeDescription object should be returned to the calling code. 
    String refId = "refId_example"; // String | When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
    String direction = "before"; // String | If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
    try {
      PaginatedChangeDescriptions result = apiInstance.changelogDomainGraphDomainKeyGet(domainKey, start, end, maxResults, refId, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogApi#changelogDomainGraphDomainKeyGet");
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
| **domainKey** | **String**| the domain key to see an audit log for | |
| **start** | **BigDecimal**| The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] |
| **end** | **BigDecimal**| The end of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] |
| **maxResults** | **BigDecimal**| Determines how many ChangeDescription object should be returned to the calling code.  | [optional] |
| **refId** | **String**| When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument).  | [optional] |
| **direction** | **String**| If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID.  | [optional] [enum: before, after] |

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of changes occurring during the requested window. |  -  |
| **0** | Unexpected error |  -  |

<a id="changelogRouteGraphRouteKeyGet"></a>
# **changelogRouteGraphRouteKeyGet**
> PaginatedChangeDescriptions changelogRouteGraphRouteKeyGet(routeKey, start, end, maxResults, refId, direction)

get changes related to the indicated route

Gets all changes to a route, the domains associated with it, the shared rules it references, and the clusters connected to it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AuditLogApi apiInstance = new AuditLogApi(defaultClient);
    String routeKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the route key to see an audit log for
    BigDecimal start = new BigDecimal(78); // BigDecimal | The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    BigDecimal end = new BigDecimal(78); // BigDecimal | The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    BigDecimal maxResults = new BigDecimal(78); // BigDecimal | Determines how many ChangeDescription object should be returned to the calling code. 
    String refId = "refId_example"; // String | When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
    String direction = "before"; // String | If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
    try {
      PaginatedChangeDescriptions result = apiInstance.changelogRouteGraphRouteKeyGet(routeKey, start, end, maxResults, refId, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogApi#changelogRouteGraphRouteKeyGet");
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
| **routeKey** | **String**| the route key to see an audit log for | |
| **start** | **BigDecimal**| The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] |
| **end** | **BigDecimal**| The end of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] |
| **maxResults** | **BigDecimal**| Determines how many ChangeDescription object should be returned to the calling code.  | [optional] |
| **refId** | **String**| When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument).  | [optional] |
| **direction** | **String**| If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID.  | [optional] [enum: before, after] |

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of changes occurring during the requested window. |  -  |
| **0** | Unexpected error |  -  |

<a id="changelogSharedRulesGraphSharedRulesKeyGet"></a>
# **changelogSharedRulesGraphSharedRulesKeyGet**
> PaginatedChangeDescriptions changelogSharedRulesGraphSharedRulesKeyGet(sharedRulesKey, start, end, maxResults, refId, direction)

get changes related to the indicated SharedRules

Gets all changes associated with set of Shared Rules; the domains using it and the clusters referenced by it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AuditLogApi apiInstance = new AuditLogApi(defaultClient);
    String sharedRulesKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the shared rules key to see an audit log for
    BigDecimal start = new BigDecimal(78); // BigDecimal | The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    BigDecimal end = new BigDecimal(78); // BigDecimal | The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    BigDecimal maxResults = new BigDecimal(78); // BigDecimal | Determines how many ChangeDescription object should be returned to the calling code. 
    String refId = "refId_example"; // String | When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
    String direction = "before"; // String | If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
    try {
      PaginatedChangeDescriptions result = apiInstance.changelogSharedRulesGraphSharedRulesKeyGet(sharedRulesKey, start, end, maxResults, refId, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogApi#changelogSharedRulesGraphSharedRulesKeyGet");
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
| **sharedRulesKey** | **String**| the shared rules key to see an audit log for | |
| **start** | **BigDecimal**| The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] |
| **end** | **BigDecimal**| The end of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] |
| **maxResults** | **BigDecimal**| Determines how many ChangeDescription object should be returned to the calling code.  | [optional] |
| **refId** | **String**| When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument).  | [optional] |
| **direction** | **String**| If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID.  | [optional] [enum: before, after] |

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of changes occurring during the requested window. |  -  |
| **0** | Unexpected error |  -  |

<a id="changelogZoneZoneKeyGet"></a>
# **changelogZoneZoneKeyGet**
> PaginatedChangeDescriptions changelogZoneZoneKeyGet(zoneKey, start, end, maxResults, refId, direction)

get changes in a specified zone

Retrieve all changes in the specified zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AuditLogApi apiInstance = new AuditLogApi(defaultClient);
    String zoneKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the zone key to see an audit log for
    BigDecimal start = new BigDecimal(78); // BigDecimal | The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    BigDecimal end = new BigDecimal(78); // BigDecimal | The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    BigDecimal maxResults = new BigDecimal(78); // BigDecimal | Determines how many ChangeDescription object should be returned to the calling code. 
    String refId = "refId_example"; // String | When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
    String direction = "before"; // String | If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
    try {
      PaginatedChangeDescriptions result = apiInstance.changelogZoneZoneKeyGet(zoneKey, start, end, maxResults, refId, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogApi#changelogZoneZoneKeyGet");
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
| **zoneKey** | **String**| the zone key to see an audit log for | |
| **start** | **BigDecimal**| The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] |
| **end** | **BigDecimal**| The end of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] |
| **maxResults** | **BigDecimal**| Determines how many ChangeDescription object should be returned to the calling code.  | [optional] |
| **refId** | **String**| When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument).  | [optional] |
| **direction** | **String**| If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID.  | [optional] [enum: before, after] |

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of changes occurring during the requested window. |  -  |
| **0** | Unexpected error |  -  |

