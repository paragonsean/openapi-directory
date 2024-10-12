# ErrorsApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**errorsAppBuildsList**](ErrorsApi.md#errorsAppBuildsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/availableAppBuilds |  |
| [**errorsAvailableVersions**](ErrorsApi.md#errorsAvailableVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/available_versions |  |
| [**errorsCountsPerDay**](ErrorsApi.md#errorsCountsPerDay) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorCountsPerDay |  |
| [**errorsDeleteError**](ErrorsApi.md#errorsDeleteError) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId} |  |
| [**errorsErrorAttachmentLocation**](ErrorsApi.md#errorsErrorAttachmentLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/attachments/{attachmentId}/location |  |
| [**errorsErrorAttachmentText**](ErrorsApi.md#errorsErrorAttachmentText) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/attachments/{attachmentId}/text |  |
| [**errorsErrorAttachments**](ErrorsApi.md#errorsErrorAttachments) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/attachments |  |
| [**errorsErrorDownload**](ErrorsApi.md#errorsErrorDownload) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId}/download |  |
| [**errorsErrorFreeDevicePercentages**](ErrorsApi.md#errorsErrorFreeDevicePercentages) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorfreeDevicePercentages |  |
| [**errorsErrorGroupsSearch**](ErrorsApi.md#errorsErrorGroupsSearch) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/search |  |
| [**errorsErrorLocation**](ErrorsApi.md#errorsErrorLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId}/location |  |
| [**errorsErrorSearch**](ErrorsApi.md#errorsErrorSearch) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/search |  |
| [**errorsErrorStackTrace**](ErrorsApi.md#errorsErrorStackTrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId}/stacktrace |  |
| [**errorsGetErrorDetails**](ErrorsApi.md#errorsGetErrorDetails) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/{errorId} |  |
| [**errorsGetRetentionSettings**](ErrorsApi.md#errorsGetRetentionSettings) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/retention_settings | gets the retention settings in days |
| [**errorsGroupCountsPerDay**](ErrorsApi.md#errorsGroupCountsPerDay) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errorCountsPerDay |  |
| [**errorsGroupDetails**](ErrorsApi.md#errorsGroupDetails) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId} |  |
| [**errorsGroupErrorFreeDevicePercentages**](ErrorsApi.md#errorsGroupErrorFreeDevicePercentages) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errorfreeDevicePercentages |  |
| [**errorsGroupErrorStackTrace**](ErrorsApi.md#errorsGroupErrorStackTrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/stacktrace |  |
| [**errorsGroupList**](ErrorsApi.md#errorsGroupList) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups |  |
| [**errorsGroupModelCounts**](ErrorsApi.md#errorsGroupModelCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/models |  |
| [**errorsGroupOperatingSystemCounts**](ErrorsApi.md#errorsGroupOperatingSystemCounts) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/operatingSystems |  |
| [**errorsLatestErrorDetails**](ErrorsApi.md#errorsLatestErrorDetails) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors/latest |  |
| [**errorsListForGroup**](ErrorsApi.md#errorsListForGroup) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId}/errors |  |
| [**errorsListSessionLogs**](ErrorsApi.md#errorsListSessionLogs) | **GET** /v0.1/apps/{owner_name}/{app_name}/errors/{errorId}/sessionLogs |  |
| [**errorsUpdateState**](ErrorsApi.md#errorsUpdateState) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/errors/errorGroups/{errorGroupId} |  |


<a id="errorsAppBuildsList"></a>
# **errorsAppBuildsList**
> ErrorsAppBuildsList200Response errorsAppBuildsList(version, start, ownerName, appName, end, $top, errorType)



List of app builds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String version = "version_example"; // String | 
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results till the max number.)
    String errorType = "all"; // String | Type of error (handled vs unhandled), including All
    try {
      ErrorsAppBuildsList200Response result = apiInstance.errorsAppBuildsList(version, start, ownerName, appName, end, $top, errorType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsAppBuildsList");
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
| **version** | **String**|  | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format | [optional] |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30] |
| **errorType** | **String**| Type of error (handled vs unhandled), including All | [optional] [enum: all, unhandledError, handledError] |

### Return type

[**ErrorsAppBuildsList200Response**](ErrorsAppBuildsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of App builds |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsAvailableVersions"></a>
# **errorsAvailableVersions**
> ErrorsAvailableVersions200Response errorsAvailableVersions(start, ownerName, appName, end, $top, $skip, $filter, $inlinecount, errorType)



Get all available versions in the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results till the max number.)
    Long $skip = 0L; // Long | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
    String $filter = "$filter_example"; // String | A filter as specified in https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md#97-filtering.
    String $inlinecount = "allpages"; // String | Controls whether or not to include a count of all the items across all pages.
    String errorType = "all"; // String | Type of error (handled vs unhandled), including All
    try {
      ErrorsAvailableVersions200Response result = apiInstance.errorsAvailableVersions(start, ownerName, appName, end, $top, $skip, $filter, $inlinecount, errorType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsAvailableVersions");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format | [optional] |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30] |
| **$skip** | **Long**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] [default to 0] |
| **$filter** | **String**| A filter as specified in https://github.com/Microsoft/api-guidelines/blob/master/Guidelines.md#97-filtering. | [optional] |
| **$inlinecount** | **String**| Controls whether or not to include a count of all the items across all pages. | [optional] [default to none] [enum: allpages, none] |
| **errorType** | **String**| Type of error (handled vs unhandled), including All | [optional] [enum: all, unhandledError, handledError] |

### Return type

[**ErrorsAvailableVersions200Response**](ErrorsAvailableVersions200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of available versions in the time range. |  -  |
| **0** | Error code with reason. |  -  |

<a id="errorsCountsPerDay"></a>
# **errorsCountsPerDay**
> ErrorsCountsPerDay200Response errorsCountsPerDay(start, ownerName, appName, version, end, appBuild, errorType)



Count of crashes or errors by day in the time range based the selected versions. If SingleErrorTypeParameter is not provided, defaults to handlederror.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String version = "version_example"; // String | 
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format
    String appBuild = "appBuild_example"; // String | app build
    String errorType = "unhandledError"; // String | Type of error (handled vs unhandled), excluding All
    try {
      ErrorsCountsPerDay200Response result = apiInstance.errorsCountsPerDay(start, ownerName, appName, version, end, appBuild, errorType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsCountsPerDay");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **version** | **String**|  | [optional] |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format | [optional] |
| **appBuild** | **String**| app build | [optional] |
| **errorType** | **String**| Type of error (handled vs unhandled), excluding All | [optional] [enum: unhandledError, handledError] |

### Return type

[**ErrorsCountsPerDay200Response**](ErrorsCountsPerDay200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of crashes or errors by day in the time range, and total over the entire time range. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsDeleteError"></a>
# **errorsDeleteError**
> ErrorsDeleteError200Response errorsDeleteError(errorGroupId, errorId, ownerName, appName)



Delete a specific error and related attachments and blobs for an app. Searchable data will not be deleted immediately and may take up to 30 days.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String errorId = "errorId_example"; // String | The id of the error
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ErrorsDeleteError200Response result = apiInstance.errorsDeleteError(errorGroupId, errorId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsDeleteError");
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
| **errorGroupId** | **String**| The id of the error group | |
| **errorId** | **String**| The id of the error | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ErrorsDeleteError200Response**](ErrorsDeleteError200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsErrorAttachmentLocation"></a>
# **errorsErrorAttachmentLocation**
> ErrorsErrorLocation200Response errorsErrorAttachmentLocation(errorId, attachmentId, ownerName, appName)



Error attachment location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorId = "errorId_example"; // String | The id of the error
    String attachmentId = "attachmentId_example"; // String | Error attachment id.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ErrorsErrorLocation200Response result = apiInstance.errorsErrorAttachmentLocation(errorId, attachmentId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsErrorAttachmentLocation");
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
| **errorId** | **String**| The id of the error | |
| **attachmentId** | **String**| Error attachment id. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ErrorsErrorLocation200Response**](ErrorsErrorLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Error attachment location. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsErrorAttachmentText"></a>
# **errorsErrorAttachmentText**
> ErrorsErrorAttachmentText200Response errorsErrorAttachmentText(errorId, attachmentId, ownerName, appName)



Error attachment text.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorId = "errorId_example"; // String | The id of the error
    String attachmentId = "attachmentId_example"; // String | Error attachment id.
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ErrorsErrorAttachmentText200Response result = apiInstance.errorsErrorAttachmentText(errorId, attachmentId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsErrorAttachmentText");
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
| **errorId** | **String**| The id of the error | |
| **attachmentId** | **String**| Error attachment id. | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ErrorsErrorAttachmentText200Response**](ErrorsErrorAttachmentText200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Error attachment text. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsErrorAttachments"></a>
# **errorsErrorAttachments**
> List&lt;ErrorsErrorAttachments200ResponseInner&gt; errorsErrorAttachments(errorId, ownerName, appName)



List error attachments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorId = "errorId_example"; // String | The id of the error
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<ErrorsErrorAttachments200ResponseInner> result = apiInstance.errorsErrorAttachments(errorId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsErrorAttachments");
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
| **errorId** | **String**| The id of the error | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;ErrorsErrorAttachments200ResponseInner&gt;**](ErrorsErrorAttachments200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of error attachments. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsErrorDownload"></a>
# **errorsErrorDownload**
> Object errorsErrorDownload(errorGroupId, errorId, ownerName, appName, format)



Download details for a specific error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String errorId = "errorId_example"; // String | The id of the error
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String format = "json"; // String | the format of the crash log
    try {
      Object result = apiInstance.errorsErrorDownload(errorGroupId, errorId, ownerName, appName, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsErrorDownload");
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
| **errorGroupId** | **String**| The id of the error group | |
| **errorId** | **String**| The id of the error | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **format** | **String**| the format of the crash log | [optional] [enum: json, txt] |

### Return type

**Object**

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Error details. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsErrorFreeDevicePercentages"></a>
# **errorsErrorFreeDevicePercentages**
> ErrorsGroupErrorFreeDevicePercentages200Response errorsErrorFreeDevicePercentages(start, ownerName, appName, end, versions, appBuild, errorType)



Percentage of error-free devices by day in the time range based on the selected versions. If SingleErrorTypeParameter is not provided, defaults to handlederror. API will return -1 if crash devices is greater than active devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format
    List<String> versions = Arrays.asList(); // List<String> | 
    String appBuild = "appBuild_example"; // String | app build
    String errorType = "unhandledError"; // String | Type of error (handled vs unhandled), excluding All
    try {
      ErrorsGroupErrorFreeDevicePercentages200Response result = apiInstance.errorsErrorFreeDevicePercentages(start, ownerName, appName, end, versions, appBuild, errorType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsErrorFreeDevicePercentages");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format | [optional] |
| **versions** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **appBuild** | **String**| app build | [optional] |
| **errorType** | **String**| Type of error (handled vs unhandled), excluding All | [optional] [enum: unhandledError, handledError] |

### Return type

[**ErrorsGroupErrorFreeDevicePercentages200Response**](ErrorsGroupErrorFreeDevicePercentages200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Percentage of error-free devices by day in the time range and overall percentage of the entire time range. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsErrorGroupsSearch"></a>
# **errorsErrorGroupsSearch**
> ErrorsErrorGroupsSearch200Response errorsErrorGroupsSearch(ownerName, appName, filter, q, order, sort, $top, $skip)



Error groups list based on search parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String filter = "filter_example"; // String | A filter as specified in OData notation
    String q = "q_example"; // String | A query string
    String order = "desc"; // String | It controls the order of sorting
    String sort = "matchingReportsCount"; // String | It controls the sort based on specified field
    Long $top = 100L; // Long | The maximum number of results to return
    Long $skip = 0L; // Long | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
    try {
      ErrorsErrorGroupsSearch200Response result = apiInstance.errorsErrorGroupsSearch(ownerName, appName, filter, q, order, sort, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsErrorGroupsSearch");
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
| **filter** | **String**| A filter as specified in OData notation | [optional] |
| **q** | **String**| A query string | [optional] |
| **order** | **String**| It controls the order of sorting | [optional] [default to desc] [enum: desc, asc] |
| **sort** | **String**| It controls the sort based on specified field | [optional] [default to matchingReportsCount] [enum: matchingReportsCount, exceptionClassName, exceptionMessage, exceptionMethod, lastOccurrence] |
| **$top** | **Long**| The maximum number of results to return | [optional] [default to 100] |
| **$skip** | **Long**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] [default to 0] |

### Return type

[**ErrorsErrorGroupsSearch200Response**](ErrorsErrorGroupsSearch200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of error groups |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsErrorLocation"></a>
# **errorsErrorLocation**
> ErrorsErrorLocation200Response errorsErrorLocation(errorGroupId, errorId, ownerName, appName)



Error location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String errorId = "errorId_example"; // String | The id of the error
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ErrorsErrorLocation200Response result = apiInstance.errorsErrorLocation(errorGroupId, errorId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsErrorLocation");
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
| **errorGroupId** | **String**| The id of the error group | |
| **errorId** | **String**| The id of the error | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ErrorsErrorLocation200Response**](ErrorsErrorLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Error location. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsErrorSearch"></a>
# **errorsErrorSearch**
> ErrorsErrorSearch200Response errorsErrorSearch(ownerName, appName, filter, q, order, sort, $top, $skip)



Errors list based on search parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String filter = "filter_example"; // String | A filter as specified in OData notation
    String q = "q_example"; // String | A query string
    String order = "desc"; // String | It controls the order of sorting
    String sort = "timestamp"; // String | It controls the sort based on specified field
    Long $top = 100L; // Long | The maximum number of results to return
    Long $skip = 0L; // Long | The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination.
    try {
      ErrorsErrorSearch200Response result = apiInstance.errorsErrorSearch(ownerName, appName, filter, q, order, sort, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsErrorSearch");
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
| **filter** | **String**| A filter as specified in OData notation | [optional] |
| **q** | **String**| A query string | [optional] |
| **order** | **String**| It controls the order of sorting | [optional] [default to desc] [enum: desc, asc] |
| **sort** | **String**| It controls the sort based on specified field | [optional] [default to timestamp] [enum: timestamp, errorGroupId, exceptionClassName, exceptionFile, exceptionLine, exceptionMessage, exceptionMethod, deviceName, osVersion, userId] |
| **$top** | **Long**| The maximum number of results to return | [optional] [default to 100] |
| **$skip** | **Long**| The offset (starting at 0) of the first result to return. This parameter along with limit is used to perform pagination. | [optional] [default to 0] |

### Return type

[**ErrorsErrorSearch200Response**](ErrorsErrorSearch200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of errors |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsErrorStackTrace"></a>
# **errorsErrorStackTrace**
> DiagnosticsStackTrace errorsErrorStackTrace(errorGroupId, errorId, ownerName, appName)



Error Stacktrace details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String errorId = "errorId_example"; // String | The id of the error
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      DiagnosticsStackTrace result = apiInstance.errorsErrorStackTrace(errorGroupId, errorId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsErrorStackTrace");
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
| **errorGroupId** | **String**| The id of the error group | |
| **errorId** | **String**| The id of the error | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**DiagnosticsStackTrace**](DiagnosticsStackTrace.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Error stacktrace details. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsGetErrorDetails"></a>
# **errorsGetErrorDetails**
> ErrorsLatestErrorDetails200Response errorsGetErrorDetails(errorGroupId, errorId, ownerName, appName)



Error details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String errorId = "errorId_example"; // String | The id of the error
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ErrorsLatestErrorDetails200Response result = apiInstance.errorsGetErrorDetails(errorGroupId, errorId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsGetErrorDetails");
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
| **errorGroupId** | **String**| The id of the error group | |
| **errorId** | **String**| The id of the error | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ErrorsLatestErrorDetails200Response**](ErrorsLatestErrorDetails200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Error details. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsGetRetentionSettings"></a>
# **errorsGetRetentionSettings**
> ErrorsGetRetentionSettings200Response errorsGetRetentionSettings(ownerName, appName)

gets the retention settings in days

gets the retention settings in days

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ErrorsGetRetentionSettings200Response result = apiInstance.errorsGetRetentionSettings(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsGetRetentionSettings");
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

[**ErrorsGetRetentionSettings200Response**](ErrorsGetRetentionSettings200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error code with reason. |  -  |

<a id="errorsGroupCountsPerDay"></a>
# **errorsGroupCountsPerDay**
> ErrorsCountsPerDay200Response errorsGroupCountsPerDay(errorGroupId, start, ownerName, appName, version, end)



Count of errors by day in the time range of the selected error group with selected version

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String version = "version_example"; // String | 
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format
    try {
      ErrorsCountsPerDay200Response result = apiInstance.errorsGroupCountsPerDay(errorGroupId, start, ownerName, appName, version, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsGroupCountsPerDay");
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
| **errorGroupId** | **String**| The id of the error group | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **version** | **String**|  | [optional] |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format | [optional] |

### Return type

[**ErrorsCountsPerDay200Response**](ErrorsCountsPerDay200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of errors by day in the time range and total errors over the time range. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsGroupDetails"></a>
# **errorsGroupDetails**
> ErrorsGroupDetails200Response errorsGroupDetails(errorGroupId, ownerName, appName)



Error group details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ErrorsGroupDetails200Response result = apiInstance.errorsGroupDetails(errorGroupId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsGroupDetails");
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
| **errorGroupId** | **String**| The id of the error group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ErrorsGroupDetails200Response**](ErrorsGroupDetails200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Error group details |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsGroupErrorFreeDevicePercentages"></a>
# **errorsGroupErrorFreeDevicePercentages**
> ErrorsGroupErrorFreeDevicePercentages200Response errorsGroupErrorFreeDevicePercentages(errorGroupId, start, ownerName, appName, end)



Percentage of error-free devices by day in the time range. Api will return -1 if crash devices is greater than active devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format
    try {
      ErrorsGroupErrorFreeDevicePercentages200Response result = apiInstance.errorsGroupErrorFreeDevicePercentages(errorGroupId, start, ownerName, appName, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsGroupErrorFreeDevicePercentages");
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
| **errorGroupId** | **String**| The id of the error group | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format | [optional] |

### Return type

[**ErrorsGroupErrorFreeDevicePercentages200Response**](ErrorsGroupErrorFreeDevicePercentages200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Percentage of error-free devices by day in the time range and overall percentage of the time range. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsGroupErrorStackTrace"></a>
# **errorsGroupErrorStackTrace**
> DiagnosticsStackTrace errorsGroupErrorStackTrace(errorGroupId, ownerName, appName)



Gets the stack trace for the error group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      DiagnosticsStackTrace result = apiInstance.errorsGroupErrorStackTrace(errorGroupId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsGroupErrorStackTrace");
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
| **errorGroupId** | **String**| The id of the error group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**DiagnosticsStackTrace**](DiagnosticsStackTrace.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the stack trace for the error group. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsGroupList"></a>
# **errorsGroupList**
> ErrorsGroupList200Response errorsGroupList(start, ownerName, appName, version, appBuild, groupState, end, $orderby, $top, errorType)



List of error groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String version = "version_example"; // String | 
    String appBuild = "appBuild_example"; // String | app build
    String groupState = "groupState_example"; // String | 
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format
    String $orderby = "count desc"; // String | controls the sorting order and sorting based on which column
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results till the max number.)
    String errorType = "all"; // String | Type of error (handled vs unhandled), including All
    try {
      ErrorsGroupList200Response result = apiInstance.errorsGroupList(start, ownerName, appName, version, appBuild, groupState, end, $orderby, $top, errorType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsGroupList");
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
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **version** | **String**|  | [optional] |
| **appBuild** | **String**| app build | [optional] |
| **groupState** | **String**|  | [optional] |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format | [optional] |
| **$orderby** | **String**| controls the sorting order and sorting based on which column | [optional] [default to count desc] |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30] |
| **errorType** | **String**| Type of error (handled vs unhandled), including All | [optional] [enum: all, unhandledError, handledError] |

### Return type

[**ErrorsGroupList200Response**](ErrorsGroupList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of error groups |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsGroupModelCounts"></a>
# **errorsGroupModelCounts**
> ErrorsGroupModelCounts200Response errorsGroupModelCounts(errorGroupId, ownerName, appName, $top)



Top models of the selected error group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results till the max number.)
    try {
      ErrorsGroupModelCounts200Response result = apiInstance.errorsGroupModelCounts(errorGroupId, ownerName, appName, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsGroupModelCounts");
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
| **errorGroupId** | **String**| The id of the error group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30] |

### Return type

[**ErrorsGroupModelCounts200Response**](ErrorsGroupModelCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Top Models with percentage in descending order |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsGroupOperatingSystemCounts"></a>
# **errorsGroupOperatingSystemCounts**
> ErrorsGroupOperatingSystemCounts200Response errorsGroupOperatingSystemCounts(errorGroupId, ownerName, appName, $top)



Top OSes of the selected error group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results till the max number.)
    try {
      ErrorsGroupOperatingSystemCounts200Response result = apiInstance.errorsGroupOperatingSystemCounts(errorGroupId, ownerName, appName, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsGroupOperatingSystemCounts");
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
| **errorGroupId** | **String**| The id of the error group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30] |

### Return type

[**ErrorsGroupOperatingSystemCounts200Response**](ErrorsGroupOperatingSystemCounts200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Top OSes with percentage in descending order |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsLatestErrorDetails"></a>
# **errorsLatestErrorDetails**
> ErrorsLatestErrorDetails200Response errorsLatestErrorDetails(errorGroupId, ownerName, appName)



Latest error details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      ErrorsLatestErrorDetails200Response result = apiInstance.errorsLatestErrorDetails(errorGroupId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsLatestErrorDetails");
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
| **errorGroupId** | **String**| The id of the error group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**ErrorsLatestErrorDetails200Response**](ErrorsLatestErrorDetails200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Latest error details. |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsListForGroup"></a>
# **errorsListForGroup**
> ErrorsListForGroup200Response errorsListForGroup(errorGroupId, start, ownerName, appName, end, $top, model, os)



Get all errors for group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | Start date time in data in ISO 8601 date time format
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | Last date time in data in ISO 8601 date time format
    Long $top = 30L; // Long | The maximum number of results to return. (0 will fetch all results till the max number.)
    String model = "model_example"; // String | 
    String os = "os_example"; // String | 
    try {
      ErrorsListForGroup200Response result = apiInstance.errorsListForGroup(errorGroupId, start, ownerName, appName, end, $top, model, os);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsListForGroup");
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
| **errorGroupId** | **String**| The id of the error group | |
| **start** | **OffsetDateTime**| Start date time in data in ISO 8601 date time format | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **end** | **OffsetDateTime**| Last date time in data in ISO 8601 date time format | [optional] |
| **$top** | **Long**| The maximum number of results to return. (0 will fetch all results till the max number.) | [optional] [default to 30] |
| **model** | **String**|  | [optional] |
| **os** | **String**|  | [optional] |

### Return type

[**ErrorsListForGroup200Response**](ErrorsListForGroup200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get all errors for group |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsListSessionLogs"></a>
# **errorsListSessionLogs**
> ErrorsListSessionLogs200Response errorsListSessionLogs(errorId, ownerName, appName, date)



Get session logs by error ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorId = "errorId_example"; // String | The id of the error
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime date = OffsetDateTime.now(); // OffsetDateTime | Date of data requested
    try {
      ErrorsListSessionLogs200Response result = apiInstance.errorsListSessionLogs(errorId, ownerName, appName, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsListSessionLogs");
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
| **errorId** | **String**| The id of the error | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **date** | **OffsetDateTime**| Date of data requested | [optional] |

### Return type

[**ErrorsListSessionLogs200Response**](ErrorsListSessionLogs200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session logs of specific error |  -  |
| **0** | Error code with reason |  -  |

<a id="errorsUpdateState"></a>
# **errorsUpdateState**
> ErrorsGroupDetails200Response errorsUpdateState(errorGroupId, ownerName, appName, errorsUpdateStateRequest)



Update error group state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ErrorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    ErrorsApi apiInstance = new ErrorsApi(defaultClient);
    String errorGroupId = "errorGroupId_example"; // String | The id of the error group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    ErrorsUpdateStateRequest errorsUpdateStateRequest = new ErrorsUpdateStateRequest(); // ErrorsUpdateStateRequest | The state of the error group
    try {
      ErrorsGroupDetails200Response result = apiInstance.errorsUpdateState(errorGroupId, ownerName, appName, errorsUpdateStateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ErrorsApi#errorsUpdateState");
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
| **errorGroupId** | **String**| The id of the error group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **errorsUpdateStateRequest** | [**ErrorsUpdateStateRequest**](ErrorsUpdateStateRequest.md)| The state of the error group | |

### Return type

[**ErrorsGroupDetails200Response**](ErrorsGroupDetails200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Error group details |  -  |
| **0** | Error code with reason |  -  |

