# AnalyticsApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyticsAudienceNameExists**](AnalyticsApi.md#analyticsAudienceNameExists) | **HEAD** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} |  |
| [**analyticsCrashCounts**](AnalyticsApi.md#analyticsCrashCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_counts | Available for UWP apps only. |
| [**analyticsCrashFreeDevicePercentages**](AnalyticsApi.md#analyticsCrashFreeDevicePercentages) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crashfree_device_percentages |  |
| [**analyticsCrashGroupCounts**](AnalyticsApi.md#analyticsCrashGroupCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/crash_counts | Available for UWP apps only. |
| [**analyticsCrashGroupModelCounts**](AnalyticsApi.md#analyticsCrashGroupModelCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/models | Available for UWP apps only. |
| [**analyticsCrashGroupOperatingSystemCounts**](AnalyticsApi.md#analyticsCrashGroupOperatingSystemCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/operating_systems | Available for UWP apps only. |
| [**analyticsCrashGroupTotals**](AnalyticsApi.md#analyticsCrashGroupTotals) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups/{crash_group_id}/overall | Available for UWP apps only. |
| [**analyticsCrashGroupsTotals**](AnalyticsApi.md#analyticsCrashGroupsTotals) | **POST** /v0.1/apps/{owner_name}/{app_name}/analytics/crash_groups |  |
| [**analyticsCreateOrUpdateAudience**](AnalyticsApi.md#analyticsCreateOrUpdateAudience) | **PUT** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} |  |
| [**analyticsDeleteAudience**](AnalyticsApi.md#analyticsDeleteAudience) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} |  |
| [**analyticsDeviceCounts**](AnalyticsApi.md#analyticsDeviceCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/active_device_counts |  |
| [**analyticsDistributionReleaseCounts**](AnalyticsApi.md#analyticsDistributionReleaseCounts) | **POST** /v0.1/apps/{owner_name}/{app_name}/analytics/distribution/release_counts |  |
| [**analyticsEventCount**](AnalyticsApi.md#analyticsEventCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/event_count |  |
| [**analyticsEventDeviceCount**](AnalyticsApi.md#analyticsEventDeviceCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/device_count |  |
| [**analyticsEventPerDeviceCount**](AnalyticsApi.md#analyticsEventPerDeviceCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/count_per_device |  |
| [**analyticsEventPerSessionCount**](AnalyticsApi.md#analyticsEventPerSessionCount) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/count_per_session |  |
| [**analyticsEventProperties**](AnalyticsApi.md#analyticsEventProperties) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/properties |  |
| [**analyticsEventPropertyCounts**](AnalyticsApi.md#analyticsEventPropertyCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name}/properties/{event_property_name}/counts |  |
| [**analyticsEvents**](AnalyticsApi.md#analyticsEvents) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/events |  |
| [**analyticsEventsDelete**](AnalyticsApi.md#analyticsEventsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/analytics/events/{event_name} |  |
| [**analyticsEventsDeleteLogs**](AnalyticsApi.md#analyticsEventsDeleteLogs) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/analytics/event_logs/{event_name} |  |
| [**analyticsGenericLogFlow**](AnalyticsApi.md#analyticsGenericLogFlow) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/generic_log_flow |  |
| [**analyticsGetAudience**](AnalyticsApi.md#analyticsGetAudience) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/{audience_name} |  |
| [**analyticsLanguageCounts**](AnalyticsApi.md#analyticsLanguageCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/languages |  |
| [**analyticsListAudiences**](AnalyticsApi.md#analyticsListAudiences) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences |  |
| [**analyticsListCustomProperties**](AnalyticsApi.md#analyticsListCustomProperties) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/custom_properties |  |
| [**analyticsListDeviceProperties**](AnalyticsApi.md#analyticsListDeviceProperties) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/device_properties |  |
| [**analyticsListDevicePropertyValues**](AnalyticsApi.md#analyticsListDevicePropertyValues) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/metadata/device_properties/{property_name}/values |  |
| [**analyticsLogFlow**](AnalyticsApi.md#analyticsLogFlow) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/log_flow |  |
| [**analyticsModelCounts**](AnalyticsApi.md#analyticsModelCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/models |  |
| [**analyticsOperatingSystemCounts**](AnalyticsApi.md#analyticsOperatingSystemCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/oses |  |
| [**analyticsPerDeviceCounts**](AnalyticsApi.md#analyticsPerDeviceCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/sessions_per_device |  |
| [**analyticsPlaceCounts**](AnalyticsApi.md#analyticsPlaceCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/places |  |
| [**analyticsSessionCounts**](AnalyticsApi.md#analyticsSessionCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/session_counts |  |
| [**analyticsSessionDurationsDistribution**](AnalyticsApi.md#analyticsSessionDurationsDistribution) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/session_durations_distribution |  |
| [**analyticsTestAudience**](AnalyticsApi.md#analyticsTestAudience) | **POST** /v0.1/apps/{owner_name}/{app_name}/analytics/audiences/definition/test |  |
| [**analyticsVersions**](AnalyticsApi.md#analyticsVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/analytics/versions |  |
| [**appBlockLogs**](AnalyticsApi.md#appBlockLogs) | **PUT** /v0.1/apps/{owner_name}/{app_name}/devices/block_logs |  |
| [**crashesListSessionLogs**](AnalyticsApi.md#crashesListSessionLogs) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/session_logs |  |
| [**devicesBlockLogs**](AnalyticsApi.md#devicesBlockLogs) | **PUT** /v0.1/apps/{owner_name}/{app_name}/devices/block_logs/{install_id} |  |


<a id="analyticsAudienceNameExists"></a>
# **analyticsAudienceNameExists**
> analyticsAudienceNameExists(audienceName, ownerName, appName)



Returns whether audience definition exists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String audienceName = "audienceName_example"; // String | The name of the audience
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.analyticsAudienceNameExists(audienceName, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsAudienceNameExists");
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
| **audienceName** | **String**| The name of the audience | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Audiences exists. |  -  |
| **404** | Audiences does not exist. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsCrashCounts"></a>
# **analyticsCrashCounts**
> AnalyticsCrashCounts200Response analyticsCrashCounts(start, ownerName, appName, end, versions)

Available for UWP apps only.

Count of crashes by day in the time range based the selected versions. Available for UWP apps only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsCrashCounts200Response result = apiInstance.analyticsCrashCounts(start, ownerName, appName, end, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsCrashCounts");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsCrashCounts200Response**](AnalyticsCrashCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of crashes by day in the time range and total crashes over the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsCrashFreeDevicePercentages"></a>
# **analyticsCrashFreeDevicePercentages**
> AnalyticsCrashFreeDevicePercentages200Response analyticsCrashFreeDevicePercentages(start, version, ownerName, appName, end)



Percentage of crash-free device by day in the time range based on the selected versions. Api will return -1 if crash devices is greater than active devices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String version = "version_example"; // String | 
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    try {
      AnalyticsCrashFreeDevicePercentages200Response result = apiInstance.analyticsCrashFreeDevicePercentages(start, version, ownerName, appName, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsCrashFreeDevicePercentages");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **version** | **String**|  | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |

### Return type

[**AnalyticsCrashFreeDevicePercentages200Response**](AnalyticsCrashFreeDevicePercentages200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Percentage of crash-free devices by day in the time range and overall percentage of the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsCrashGroupCounts"></a>
# **analyticsCrashGroupCounts**
> AnalyticsCrashCounts200Response analyticsCrashGroupCounts(crashGroupId, version, start, ownerName, appName, end)

Available for UWP apps only.

Count of crashes by day in the time range of the selected crash group with selected version. Available for UWP apps only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | The id of the crash group.
    String version = "version_example"; // String | 
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    try {
      AnalyticsCrashCounts200Response result = apiInstance.analyticsCrashGroupCounts(crashGroupId, version, start, ownerName, appName, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsCrashGroupCounts");
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
| **crashGroupId** | **String**| The id of the crash group. | |
| **version** | **String**|  | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |

### Return type

[**AnalyticsCrashCounts200Response**](AnalyticsCrashCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of crashes by day in the time range and total crashes over the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsCrashGroupModelCounts"></a>
# **analyticsCrashGroupModelCounts**
> AnalyticsCrashGroupModelCounts200Response analyticsCrashGroupModelCounts(crashGroupId, version, ownerName, appName, $top)

Available for UWP apps only.

Top models of the selected crash group with selected version. Available for UWP apps only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | The id of the crash group.
    String version = "version_example"; // String | 
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results)
    try {
      AnalyticsCrashGroupModelCounts200Response result = apiInstance.analyticsCrashGroupModelCounts(crashGroupId, version, ownerName, appName, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsCrashGroupModelCounts");
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
| **crashGroupId** | **String**| The id of the crash group. | |
| **version** | **String**|  | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30] |

### Return type

[**AnalyticsCrashGroupModelCounts200Response**](AnalyticsCrashGroupModelCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Top models with percentage in descending order. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsCrashGroupOperatingSystemCounts"></a>
# **analyticsCrashGroupOperatingSystemCounts**
> AnalyticsCrashGroupOperatingSystemCounts200Response analyticsCrashGroupOperatingSystemCounts(crashGroupId, version, ownerName, appName, $top)

Available for UWP apps only.

Top OSes of the selected crash group with selected version. Available for UWP apps only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | The id of the crash group.
    String version = "version_example"; // String | 
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results)
    try {
      AnalyticsCrashGroupOperatingSystemCounts200Response result = apiInstance.analyticsCrashGroupOperatingSystemCounts(crashGroupId, version, ownerName, appName, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsCrashGroupOperatingSystemCounts");
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
| **crashGroupId** | **String**| The id of the crash group. | |
| **version** | **String**|  | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30] |

### Return type

[**AnalyticsCrashGroupOperatingSystemCounts200Response**](AnalyticsCrashGroupOperatingSystemCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Top OSes with percentage in descending order. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsCrashGroupTotals"></a>
# **analyticsCrashGroupTotals**
> AnalyticsCrashGroupsTotals200ResponseInnerOverall analyticsCrashGroupTotals(crashGroupId, version, ownerName, appName)

Available for UWP apps only.

Overall crashes and affected users count of the selected crash group with selected version. Available for UWP apps only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | The id of the crash group.
    String version = "version_example"; // String | 
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      AnalyticsCrashGroupsTotals200ResponseInnerOverall result = apiInstance.analyticsCrashGroupTotals(crashGroupId, version, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsCrashGroupTotals");
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
| **crashGroupId** | **String**| The id of the crash group. | |
| **version** | **String**|  | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**AnalyticsCrashGroupsTotals200ResponseInnerOverall**](AnalyticsCrashGroupsTotals200ResponseInnerOverall.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Overall crashes and affected users count. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsCrashGroupsTotals"></a>
# **analyticsCrashGroupsTotals**
> List&lt;AnalyticsCrashGroupsTotals200ResponseInner&gt; analyticsCrashGroupsTotals(ownerName, appName, analyticsCrashGroupsTotalsRequest)



Overall crashes and affected users count of the selected crash groups with selected versions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    AnalyticsCrashGroupsTotalsRequest analyticsCrashGroupsTotalsRequest = new AnalyticsCrashGroupsTotalsRequest(); // AnalyticsCrashGroupsTotalsRequest | 
    try {
      List<AnalyticsCrashGroupsTotals200ResponseInner> result = apiInstance.analyticsCrashGroupsTotals(ownerName, appName, analyticsCrashGroupsTotalsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsCrashGroupsTotals");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **analyticsCrashGroupsTotalsRequest** | [**AnalyticsCrashGroupsTotalsRequest**](AnalyticsCrashGroupsTotalsRequest.md)|  | |

### Return type

[**List&lt;AnalyticsCrashGroupsTotals200ResponseInner&gt;**](AnalyticsCrashGroupsTotals200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Overall crashes and affected users count for all selected crash groups. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsCreateOrUpdateAudience"></a>
# **analyticsCreateOrUpdateAudience**
> AnalyticsGetAudience200Response analyticsCreateOrUpdateAudience(audienceName, ownerName, appName, analyticsTestAudienceRequest)



Creates or updates audience definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String audienceName = "audienceName_example"; // String | The name of the audience
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    AnalyticsTestAudienceRequest analyticsTestAudienceRequest = new AnalyticsTestAudienceRequest(); // AnalyticsTestAudienceRequest | Audience definition
    try {
      AnalyticsGetAudience200Response result = apiInstance.analyticsCreateOrUpdateAudience(audienceName, ownerName, appName, analyticsTestAudienceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsCreateOrUpdateAudience");
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
| **audienceName** | **String**| The name of the audience | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **analyticsTestAudienceRequest** | [**AnalyticsTestAudienceRequest**](AnalyticsTestAudienceRequest.md)| Audience definition | |

### Return type

[**AnalyticsGetAudience200Response**](AnalyticsGetAudience200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated audiences definition. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsDeleteAudience"></a>
# **analyticsDeleteAudience**
> analyticsDeleteAudience(audienceName, ownerName, appName)



Deletes audience definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String audienceName = "audienceName_example"; // String | The name of the audience
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.analyticsDeleteAudience(audienceName, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsDeleteAudience");
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
| **audienceName** | **String**| The name of the audience | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Audiences exists. |  -  |
| **404** | Audiences does not exist. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsDeviceCounts"></a>
# **analyticsDeviceCounts**
> AnalyticsDeviceCounts200Response analyticsDeviceCounts(start, ownerName, appName, end, versions, appBuild)



Count of active devices by interval in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    String appBuild = "appBuild_example"; // String | Application build number. If build number is specified than multiple versions are not allowed.
    try {
      AnalyticsDeviceCounts200Response result = apiInstance.analyticsDeviceCounts(start, ownerName, appName, end, versions, appBuild);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsDeviceCounts");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |
| **appBuild** | **String**| Application build number. If build number is specified than multiple versions are not allowed. | [optional] |

### Return type

[**AnalyticsDeviceCounts200Response**](AnalyticsDeviceCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of active devices by interval in the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsDistributionReleaseCounts"></a>
# **analyticsDistributionReleaseCounts**
> AnalyticsDistributionReleaseCounts200Response analyticsDistributionReleaseCounts(ownerName, appName, analyticsDistributionReleaseCountsRequest)



Count of total downloads for the provided distribution releases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    AnalyticsDistributionReleaseCountsRequest analyticsDistributionReleaseCountsRequest = new AnalyticsDistributionReleaseCountsRequest(); // AnalyticsDistributionReleaseCountsRequest | The releases to retrieve.
    try {
      AnalyticsDistributionReleaseCounts200Response result = apiInstance.analyticsDistributionReleaseCounts(ownerName, appName, analyticsDistributionReleaseCountsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsDistributionReleaseCounts");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **analyticsDistributionReleaseCountsRequest** | [**AnalyticsDistributionReleaseCountsRequest**](AnalyticsDistributionReleaseCountsRequest.md)| The releases to retrieve. | |

### Return type

[**AnalyticsDistributionReleaseCounts200Response**](AnalyticsDistributionReleaseCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of total downloads for the provided distribution release(s). |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsEventCount"></a>
# **analyticsEventCount**
> AnalyticsEventCount200Response analyticsEventCount(eventName, start, ownerName, appName, end, versions)



Count of events by interval in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String eventName = "eventName_example"; // String | The id of the event.
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsEventCount200Response result = apiInstance.analyticsEventCount(eventName, start, ownerName, appName, end, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsEventCount");
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
| **eventName** | **String**| The id of the event. | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsEventCount200Response**](AnalyticsEventCount200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of events by interval in the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsEventDeviceCount"></a>
# **analyticsEventDeviceCount**
> AnalyticsEventDeviceCount200Response analyticsEventDeviceCount(eventName, start, ownerName, appName, end, versions)



Count of devices for an event by interval in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String eventName = "eventName_example"; // String | The id of the event.
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsEventDeviceCount200Response result = apiInstance.analyticsEventDeviceCount(eventName, start, ownerName, appName, end, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsEventDeviceCount");
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
| **eventName** | **String**| The id of the event. | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsEventDeviceCount200Response**](AnalyticsEventDeviceCount200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of devices for an event by interval in the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsEventPerDeviceCount"></a>
# **analyticsEventPerDeviceCount**
> AnalyticsEventPerDeviceCount200Response analyticsEventPerDeviceCount(eventName, start, ownerName, appName, end, versions)



Count of events per device by interval in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String eventName = "eventName_example"; // String | The id of the event.
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsEventPerDeviceCount200Response result = apiInstance.analyticsEventPerDeviceCount(eventName, start, ownerName, appName, end, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsEventPerDeviceCount");
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
| **eventName** | **String**| The id of the event. | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsEventPerDeviceCount200Response**](AnalyticsEventPerDeviceCount200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of events per device by interval in the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsEventPerSessionCount"></a>
# **analyticsEventPerSessionCount**
> AnalyticsEventPerSessionCount200Response analyticsEventPerSessionCount(eventName, start, ownerName, appName, end, versions)



Count of events per session by interval in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String eventName = "eventName_example"; // String | The id of the event.
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsEventPerSessionCount200Response result = apiInstance.analyticsEventPerSessionCount(eventName, start, ownerName, appName, end, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsEventPerSessionCount");
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
| **eventName** | **String**| The id of the event. | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsEventPerSessionCount200Response**](AnalyticsEventPerSessionCount200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of events per session by interval in the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsEventProperties"></a>
# **analyticsEventProperties**
> AnalyticsEventProperties200Response analyticsEventProperties(eventName, ownerName, appName)



Event properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String eventName = "eventName_example"; // String | The id of the event.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      AnalyticsEventProperties200Response result = apiInstance.analyticsEventProperties(eventName, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsEventProperties");
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
| **eventName** | **String**| The id of the event. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**AnalyticsEventProperties200Response**](AnalyticsEventProperties200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event properties. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsEventPropertyCounts"></a>
# **analyticsEventPropertyCounts**
> AnalyticsEventPropertyCounts200Response analyticsEventPropertyCounts(eventName, eventPropertyName, start, ownerName, appName, end, versions, $top)



Event properties value counts during the time range in descending order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String eventName = "eventName_example"; // String | The id of the event.
    String eventPropertyName = "eventPropertyName_example"; // String | The id of the event property.
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    Long $top = 10L; // Long | The number of property values to return. Set to 0 in order to fetch all results available.
    try {
      AnalyticsEventPropertyCounts200Response result = apiInstance.analyticsEventPropertyCounts(eventName, eventPropertyName, start, ownerName, appName, end, versions, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsEventPropertyCounts");
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
| **eventName** | **String**| The id of the event. | |
| **eventPropertyName** | **String**| The id of the event property. | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |
| **$top** | **Long**| The number of property values to return. Set to 0 in order to fetch all results available. | [optional] [default to 10] |

### Return type

[**AnalyticsEventPropertyCounts200Response**](AnalyticsEventPropertyCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event properties value counts during the time range in descending order. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsEvents"></a>
# **analyticsEvents**
> AnalyticsEvents200Response analyticsEvents(start, ownerName, appName, end, versions, eventName, $top, $skip, $inlinecount, $orderby)



Count of active events in the time range ordered by event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    List<String> eventName = Arrays.asList(); // List<String> | To select the specific events.
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results)
    Long $skip = 0L; // Long | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
    String $inlinecount = "allpages"; // String | Controls whether or not to include a count of all the items across all pages.
    String $orderby = "count desc"; // String | controls the sorting order and sorting based on which column
    try {
      AnalyticsEvents200Response result = apiInstance.analyticsEvents(start, ownerName, appName, end, versions, eventName, $top, $skip, $inlinecount, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsEvents");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |
| **eventName** | [**List&lt;String&gt;**](String.md)| To select the specific events. | [optional] |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30] |
| **$skip** | **Long**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] [default to 0] |
| **$inlinecount** | **String**| Controls whether or not to include a count of all the items across all pages. | [optional] [default to none] [enum: allpages, none] |
| **$orderby** | **String**| controls the sorting order and sorting based on which column | [optional] [default to count desc] |

### Return type

[**AnalyticsEvents200Response**](AnalyticsEvents200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of active events in the time range ordered by event. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsEventsDelete"></a>
# **analyticsEventsDelete**
> analyticsEventsDelete(eventName, ownerName, appName)



Delete the set of Events with the specified event names.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String eventName = "eventName_example"; // String | The id of the event.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.analyticsEventsDelete(eventName, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsEventsDelete");
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
| **eventName** | **String**| The id of the event. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event successfully deleted. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsEventsDeleteLogs"></a>
# **analyticsEventsDeleteLogs**
> analyticsEventsDeleteLogs(eventName, ownerName, appName)



Delete the set of Events with the specified event names.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String eventName = "eventName_example"; // String | The id of the event.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.analyticsEventsDeleteLogs(eventName, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsEventsDeleteLogs");
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
| **eventName** | **String**| The id of the event. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event successfully deleted. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsGenericLogFlow"></a>
# **analyticsGenericLogFlow**
> AnalyticsGenericLogFlow200Response analyticsGenericLogFlow(ownerName, appName, start)



Logs received between the specified start time and the current time. The API will return a maximum of 100 logs per call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone.
    try {
      AnalyticsGenericLogFlow200Response result = apiInstance.analyticsGenericLogFlow(ownerName, appName, start);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsGenericLogFlow");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone. | [optional] |

### Return type

[**AnalyticsGenericLogFlow200Response**](AnalyticsGenericLogFlow200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of logs for the requested time range. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsGetAudience"></a>
# **analyticsGetAudience**
> AnalyticsGetAudience200Response analyticsGetAudience(audienceName, ownerName, appName)



Gets audience definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String audienceName = "audienceName_example"; // String | The name of the audience
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      AnalyticsGetAudience200Response result = apiInstance.analyticsGetAudience(audienceName, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsGetAudience");
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
| **audienceName** | **String**| The name of the audience | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**AnalyticsGetAudience200Response**](AnalyticsGetAudience200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Audiences definition. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsLanguageCounts"></a>
# **analyticsLanguageCounts**
> AnalyticsLanguageCounts200Response analyticsLanguageCounts(start, ownerName, appName, end, $top, versions)



Languages in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results)
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsLanguageCounts200Response result = apiInstance.analyticsLanguageCounts(start, ownerName, appName, end, $top, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsLanguageCounts");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsLanguageCounts200Response**](AnalyticsLanguageCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Languages with count during the time range in descending order. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsListAudiences"></a>
# **analyticsListAudiences**
> AnalyticsListAudiences200Response analyticsListAudiences(ownerName, appName, includeDisabled)



Get list of audiences.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean includeDisabled = true; // Boolean | Include disabled audience definitions
    try {
      AnalyticsListAudiences200Response result = apiInstance.analyticsListAudiences(ownerName, appName, includeDisabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsListAudiences");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **includeDisabled** | **Boolean**| Include disabled audience definitions | [optional] |

### Return type

[**AnalyticsListAudiences200Response**](AnalyticsListAudiences200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of audiences. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsListCustomProperties"></a>
# **analyticsListCustomProperties**
> AnalyticsListCustomProperties200Response analyticsListCustomProperties(ownerName, appName)



Get list of custom properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      AnalyticsListCustomProperties200Response result = apiInstance.analyticsListCustomProperties(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsListCustomProperties");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**AnalyticsListCustomProperties200Response**](AnalyticsListCustomProperties200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of device properties. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsListDeviceProperties"></a>
# **analyticsListDeviceProperties**
> AnalyticsListCustomProperties200Response analyticsListDeviceProperties(ownerName, appName)



Get list of device properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      AnalyticsListCustomProperties200Response result = apiInstance.analyticsListDeviceProperties(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsListDeviceProperties");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**AnalyticsListCustomProperties200Response**](AnalyticsListCustomProperties200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of device properties. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsListDevicePropertyValues"></a>
# **analyticsListDevicePropertyValues**
> AnalyticsListDevicePropertyValues200Response analyticsListDevicePropertyValues(propertyName, ownerName, appName, contains)



Get list of device property values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String propertyName = "propertyName_example"; // String | Device property
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String contains = "contains_example"; // String | Contains string
    try {
      AnalyticsListDevicePropertyValues200Response result = apiInstance.analyticsListDevicePropertyValues(propertyName, ownerName, appName, contains);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsListDevicePropertyValues");
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
| **propertyName** | **String**| Device property | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **contains** | **String**| Contains string | [optional] |

### Return type

[**AnalyticsListDevicePropertyValues200Response**](AnalyticsListDevicePropertyValues200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of supported device property values. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsLogFlow"></a>
# **analyticsLogFlow**
> AnalyticsLogFlow200Response analyticsLogFlow(ownerName, appName, start)



Logs received between the specified start time and the current time. The API will return a maximum of 100 logs per call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone.
    try {
      AnalyticsLogFlow200Response result = apiInstance.analyticsLogFlow(ownerName, appName, start);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsLogFlow");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. It must be within the current day in the UTC timezone. The default value is the start time of the current day in UTC timezone. | [optional] |

### Return type

[**AnalyticsLogFlow200Response**](AnalyticsLogFlow200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of logs for the requested time range. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsModelCounts"></a>
# **analyticsModelCounts**
> AnalyticsModelCounts200Response analyticsModelCounts(start, ownerName, appName, end, $top, versions)



Models in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results)
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsModelCounts200Response result = apiInstance.analyticsModelCounts(start, ownerName, appName, end, $top, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsModelCounts");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsModelCounts200Response**](AnalyticsModelCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Models with count during the time range in descending order. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsOperatingSystemCounts"></a>
# **analyticsOperatingSystemCounts**
> AnalyticsOperatingSystemCounts200Response analyticsOperatingSystemCounts(start, ownerName, appName, end, $top, versions)



OSes in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results)
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsOperatingSystemCounts200Response result = apiInstance.analyticsOperatingSystemCounts(start, ownerName, appName, end, $top, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsOperatingSystemCounts");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsOperatingSystemCounts200Response**](AnalyticsOperatingSystemCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OSes with count during the time range in descending order. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsPerDeviceCounts"></a>
# **analyticsPerDeviceCounts**
> AnalyticsPerDeviceCounts200Response analyticsPerDeviceCounts(start, ownerName, appName, end, versions)



Count of sessions per device in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsPerDeviceCounts200Response result = apiInstance.analyticsPerDeviceCounts(start, ownerName, appName, end, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsPerDeviceCounts");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsPerDeviceCounts200Response**](AnalyticsPerDeviceCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of sessions per device in the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsPlaceCounts"></a>
# **analyticsPlaceCounts**
> AnalyticsPlaceCounts200Response analyticsPlaceCounts(start, ownerName, appName, end, $top, versions)



Places in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results)
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsPlaceCounts200Response result = apiInstance.analyticsPlaceCounts(start, ownerName, appName, end, $top, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsPlaceCounts");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsPlaceCounts200Response**](AnalyticsPlaceCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Places with count during the time range in descending order. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsSessionCounts"></a>
# **analyticsSessionCounts**
> List&lt;AnalyticsDeviceCounts200ResponseDailyInner&gt; analyticsSessionCounts(start, ownerName, appName, end, versions)



Count of sessions in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      List<AnalyticsDeviceCounts200ResponseDailyInner> result = apiInstance.analyticsSessionCounts(start, ownerName, appName, end, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsSessionCounts");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**List&lt;AnalyticsDeviceCounts200ResponseDailyInner&gt;**](AnalyticsDeviceCounts200ResponseDailyInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of sessions in the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsSessionDurationsDistribution"></a>
# **analyticsSessionDurationsDistribution**
> AnalyticsSessionDurationsDistribution200Response analyticsSessionDurationsDistribution(start, ownerName, appName, end, versions)



Gets session duration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsSessionDurationsDistribution200Response result = apiInstance.analyticsSessionDurationsDistribution(start, ownerName, appName, end, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsSessionDurationsDistribution");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsSessionDurationsDistribution200Response**](AnalyticsSessionDurationsDistribution200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of  session durations for requested time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="analyticsTestAudience"></a>
# **analyticsTestAudience**
> AnalyticsTestAudience200Response analyticsTestAudience(ownerName, appName, analyticsTestAudienceRequest)



Tests audience definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    AnalyticsTestAudienceRequest analyticsTestAudienceRequest = new AnalyticsTestAudienceRequest(); // AnalyticsTestAudienceRequest | Audience definition
    try {
      AnalyticsTestAudience200Response result = apiInstance.analyticsTestAudience(ownerName, appName, analyticsTestAudienceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsTestAudience");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **analyticsTestAudienceRequest** | [**AnalyticsTestAudienceRequest**](AnalyticsTestAudienceRequest.md)| Audience definition | |

### Return type

[**AnalyticsTestAudience200Response**](AnalyticsTestAudience200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tests audience definition. |  -  |
| **0** | Error code with reason |  -  |

<a id="analyticsVersions"></a>
# **analyticsVersions**
> AnalyticsVersions200Response analyticsVersions(start, ownerName, appName, end, $top, versions)



Count of active versions in the time range ordered by version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format.
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results)
    List<String> versions = Arrays.asList(); // List<String> | To select specific application versions
    try {
      AnalyticsVersions200Response result = apiInstance.analyticsVersions(start, ownerName, appName, end, $top, versions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analyticsVersions");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format. | [optional] |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results) | [optional] [default to 30] |
| **versions** | [**List&lt;String&gt;**](String.md)| To select specific application versions | [optional] |

### Return type

[**AnalyticsVersions200Response**](AnalyticsVersions200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of active versions in the time range ordered by version. |  -  |
| **0** | Error code with reason. |  -  |

<a id="appBlockLogs"></a>
# **appBlockLogs**
> String appBlockLogs(ownerName, appName)



**Warning, this operation is not reversible.**   A successful call to this API will permanently stop ingesting any logs received via SDK by app_id, and cannot be restored. We advise caution when using this API, it is designed to permanently disable an app_id. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      String result = apiInstance.appBlockLogs(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#appBlockLogs");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

**String**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Operation successful |  -  |

<a id="crashesListSessionLogs"></a>
# **crashesListSessionLogs**
> CrashesListSessionLogs200Response crashesListSessionLogs(crashId, ownerName, appName, date)



Get session logs by crash ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String crashId = "crashId_example"; // String | The id of the a crash
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime date = OffsetDateTime.now(); // OffsetDateTime | Date of data requested
    try {
      CrashesListSessionLogs200Response result = apiInstance.crashesListSessionLogs(crashId, ownerName, appName, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#crashesListSessionLogs");
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
| **crashId** | **String**| The id of the a crash | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **date** | **OffsetDateTime**| Date of data requested | [optional] |

### Return type

[**CrashesListSessionLogs200Response**](CrashesListSessionLogs200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session logs of specific crash |  -  |
| **0** | Error code with reason |  -  |

<a id="devicesBlockLogs"></a>
# **devicesBlockLogs**
> String devicesBlockLogs(installId, ownerName, appName)



**Warning, this operation is not reversible.**   A successful call to this API will permanently stop ingesting any logs received via SDK for the given installation ID, and cannot be restored. We advise caution when using this API, it is designed to permanently disable collection from a specific installation of the app on a device, usually following the request from a user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String installId = "installId_example"; // String | The id of the device
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      String result = apiInstance.devicesBlockLogs(installId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#devicesBlockLogs");
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
| **installId** | **String**| The id of the device | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

**String**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Operation successful |  -  |

