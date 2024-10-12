# DatabaseLogReportApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryLogReport**](DatabaseLogReportApi.md#queryLogReport) | **GET** /database/log_report | Get the database log backup delay information |
| [**queryReportProperties**](DatabaseLogReportApi.md#queryReportProperties) | **GET** /database/log_report/defaults | Get the database log backup report properties |
| [**updateReportProperties**](DatabaseLogReportApi.md#updateReportProperties) | **PATCH** /database/log_report/defaults | Update the database log backup report properties |


<a id="queryLogReport"></a>
# **queryLogReport**
> DbLogReportSummaryListResponse queryLogReport(effectiveSlaDomainId, name, databaseType, location, logBackupDelay, limit, offset, sortBy, sortOrder)

Get the database log backup delay information

Get the database log backup delay information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseLogReportApi;

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

    DatabaseLogReportApi apiInstance = new DatabaseLogReportApi(defaultClient);
    String effectiveSlaDomainId = "effectiveSlaDomainId_example"; // String | Filter by effective SLA domain.
    String name = "name_example"; // String | Filter by the database name substring.
    String databaseType = "databaseType_example"; // String | Filter by the database type.
    String location = "location_example"; // String | Filter by the database location.
    Integer logBackupDelay = 56; // Integer | Filter by the database log backup delay in seconds, greater than this value.
    Integer limit = 56; // Integer | Limit the number of matches returned.
    Integer offset = 56; // Integer | Integer specifying the number of initial matches to ignore.
    String sortBy = "effectiveSlaDomainName"; // String | Specifies the attribute to use while sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      DbLogReportSummaryListResponse result = apiInstance.queryLogReport(effectiveSlaDomainId, name, databaseType, location, logBackupDelay, limit, offset, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseLogReportApi#queryLogReport");
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
| **effectiveSlaDomainId** | **String**| Filter by effective SLA domain. | [optional] |
| **name** | **String**| Filter by the database name substring. | [optional] |
| **databaseType** | **String**| Filter by the database type. | [optional] |
| **location** | **String**| Filter by the database location. | [optional] |
| **logBackupDelay** | **Integer**| Filter by the database log backup delay in seconds, greater than this value. | [optional] |
| **limit** | **Integer**| Limit the number of matches returned. | [optional] |
| **offset** | **Integer**| Integer specifying the number of initial matches to ignore. | [optional] |
| **sortBy** | **String**| Specifies the attribute to use while sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order. | [optional] [enum: effectiveSlaDomainName, name, location, databaseType, logBackupFrequency, lastSnapshotTime, latestRecoveryTime, logBackupDelay] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |

### Return type

[**DbLogReportSummaryListResponse**](DbLogReportSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the query was successful, Returns the array of DbLogReportSummary objects. |  -  |

<a id="queryReportProperties"></a>
# **queryReportProperties**
> DbLogReportProperties queryReportProperties()

Get the database log backup report properties

Get the properties for the database (SQL and Oracle) log backup delay email notification creation. The properties are logDelayThresholdInMin and logDelayNotificationFrequencyInMin.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseLogReportApi;

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

    DatabaseLogReportApi apiInstance = new DatabaseLogReportApi(defaultClient);
    try {
      DbLogReportProperties result = apiInstance.queryReportProperties();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseLogReportApi#queryReportProperties");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DbLogReportProperties**](DbLogReportProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the current properties of logDelayThresholdInMin and logDelayNotificationFrequencyInMin. |  -  |

<a id="updateReportProperties"></a>
# **updateReportProperties**
> DbLogReportProperties updateReportProperties(dbLogReportPropertiesUpdate)

Update the database log backup report properties

Update the properties for the database (SQL and Oracle) log backup delay email notification creation. The properties are logDelayThresholdInMin and logDelayNotificationFrequencyInMin.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseLogReportApi;

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

    DatabaseLogReportApi apiInstance = new DatabaseLogReportApi(defaultClient);
    DbLogReportPropertiesUpdate dbLogReportPropertiesUpdate = new DbLogReportPropertiesUpdate(); // DbLogReportPropertiesUpdate | Updated report properties.
    try {
      DbLogReportProperties result = apiInstance.updateReportProperties(dbLogReportPropertiesUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseLogReportApi#updateReportProperties");
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
| **dbLogReportPropertiesUpdate** | [**DbLogReportPropertiesUpdate**](DbLogReportPropertiesUpdate.md)| Updated report properties. | |

### Return type

[**DbLogReportProperties**](DbLogReportProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the updated properties of logDelayThresholdInMin and logDelayNotificationFrequencyInMin. |  -  |

