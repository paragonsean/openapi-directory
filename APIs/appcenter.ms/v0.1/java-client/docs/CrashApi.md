# CrashApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**crashGroupsGet**](CrashApi.md#crashGroupsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id} |  |
| [**crashGroupsGetStacktrace**](CrashApi.md#crashGroupsGetStacktrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/stacktrace |  |
| [**crashGroupsList**](CrashApi.md#crashGroupsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups |  |
| [**crashGroupsUpdate**](CrashApi.md#crashGroupsUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id} |  |
| [**crashesDelete**](CrashApi.md#crashesDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id} |  |
| [**crashesGet**](CrashApi.md#crashesGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id} |  |
| [**crashesGetAppCrashesInfo**](CrashApi.md#crashesGetAppCrashesInfo) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes_info |  |
| [**crashesGetAppVersions**](CrashApi.md#crashesGetAppVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/versions |  |
| [**crashesGetCrashAttachmentLocation**](CrashApi.md#crashesGetCrashAttachmentLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments/{attachment_id}/location |  |
| [**crashesGetCrashTextAttachmentContent**](CrashApi.md#crashesGetCrashTextAttachmentContent) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments/{attachment_id}/text |  |
| [**crashesGetNativeCrash**](CrashApi.md#crashesGetNativeCrash) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/native |  |
| [**crashesGetNativeCrashDownload**](CrashApi.md#crashesGetNativeCrashDownload) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/native/download |  |
| [**crashesGetRawCrashLocation**](CrashApi.md#crashesGetRawCrashLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/raw/location |  |
| [**crashesGetStacktrace**](CrashApi.md#crashesGetStacktrace) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes/{crash_id}/stacktrace |  |
| [**crashesList**](CrashApi.md#crashesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/crash_groups/{crash_group_id}/crashes |  |
| [**crashesListAttachments**](CrashApi.md#crashesListAttachments) | **GET** /v0.1/apps/{owner_name}/{app_name}/crashes/{crash_id}/attachments |  |
| [**missingSymbolGroupsGet**](CrashApi.md#missingSymbolGroupsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups/{symbol_group_id} | Gets missing symbol crash group by its id |
| [**missingSymbolGroupsInfo**](CrashApi.md#missingSymbolGroupsInfo) | **GET** /v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups_info | Gets application level statistics for all missing symbol groups |
| [**missingSymbolGroupsList**](CrashApi.md#missingSymbolGroupsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/diagnostics/symbol_groups | Gets top N (ordered by crash count) of crash groups by missing symbol |
| [**symbolUploadsComplete**](CrashApi.md#symbolUploadsComplete) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id} |  |
| [**symbolUploadsCreate**](CrashApi.md#symbolUploadsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads |  |
| [**symbolUploadsDelete**](CrashApi.md#symbolUploadsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id} |  |
| [**symbolUploadsGet**](CrashApi.md#symbolUploadsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id} |  |
| [**symbolUploadsGetLocation**](CrashApi.md#symbolUploadsGetLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads/{symbol_upload_id}/location |  |
| [**symbolUploadsList**](CrashApi.md#symbolUploadsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbol_uploads |  |
| [**symbolsGet**](CrashApi.md#symbolsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id} |  |
| [**symbolsGetLocation**](CrashApi.md#symbolsGetLocation) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/location |  |
| [**symbolsGetStatus**](CrashApi.md#symbolsGetStatus) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/status |  |
| [**symbolsIgnore**](CrashApi.md#symbolsIgnore) | **POST** /v0.1/apps/{owner_name}/{app_name}/symbols/{symbol_id}/ignore |  |
| [**symbolsList**](CrashApi.md#symbolsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/symbols |  |


<a id="crashGroupsGet"></a>
# **crashGroupsGet**
> CrashGroupsList200ResponseCrashGroupsInner crashGroupsGet(crashGroupId, ownerName, appName)



Gets a specific group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | id of a specific group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      CrashGroupsList200ResponseCrashGroupsInner result = apiInstance.crashGroupsGet(crashGroupId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashGroupsGet");
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
| **crashGroupId** | **String**| id of a specific group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**CrashGroupsList200ResponseCrashGroupsInner**](CrashGroupsList200ResponseCrashGroupsInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashGroupsGetStacktrace"></a>
# **crashGroupsGetStacktrace**
> Stacktrace crashGroupsGetStacktrace(crashGroupId, ownerName, appName, groupingOnly)



Gets a stacktrace for a specific crash.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | id of a specific group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean groupingOnly = false; // Boolean | true if the stacktrace should be only the relevant thread / exception. Default is false
    try {
      Stacktrace result = apiInstance.crashGroupsGetStacktrace(crashGroupId, ownerName, appName, groupingOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashGroupsGetStacktrace");
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
| **crashGroupId** | **String**| id of a specific group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **groupingOnly** | **Boolean**| true if the stacktrace should be only the relevant thread / exception. Default is false | [optional] [default to false] |

### Return type

[**Stacktrace**](Stacktrace.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashGroupsList"></a>
# **crashGroupsList**
> CrashGroupsList200Response crashGroupsList(ownerName, appName, lastOccurrenceFrom, lastOccurrenceTo, appVersion, groupType, groupStatus, groupTextSearch, $orderby, continuationToken)



Gets a list of crash groups and whether the list contains all available groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    OffsetDateTime lastOccurrenceFrom = OffsetDateTime.now(); // OffsetDateTime | Earliest date when the last time a crash occured in a crash group
    OffsetDateTime lastOccurrenceTo = OffsetDateTime.now(); // OffsetDateTime | Latest date when the last time a crash occured in a crash group
    String appVersion = "appVersion_example"; // String | version
    String groupType = "GroupType1"; // String | 
    String groupStatus = "open"; // String | 
    String groupTextSearch = "groupTextSearch_example"; // String | A freetext search that matches in crash, crash types, crash stack_traces and crash user
    String $orderby = "last_occurrence asc"; // String | the OData-like $orderby argument
    String continuationToken = "continuationToken_example"; // String | Cassandra request continuation token. The token is used for pagination.
    try {
      CrashGroupsList200Response result = apiInstance.crashGroupsList(ownerName, appName, lastOccurrenceFrom, lastOccurrenceTo, appVersion, groupType, groupStatus, groupTextSearch, $orderby, continuationToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashGroupsList");
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
| **lastOccurrenceFrom** | **OffsetDateTime**| Earliest date when the last time a crash occured in a crash group | [optional] |
| **lastOccurrenceTo** | **OffsetDateTime**| Latest date when the last time a crash occured in a crash group | [optional] |
| **appVersion** | **String**| version | [optional] |
| **groupType** | **String**|  | [optional] [enum: GroupType1, GroupType2] |
| **groupStatus** | **String**|  | [optional] [enum: open, closed, ignored] |
| **groupTextSearch** | **String**| A freetext search that matches in crash, crash types, crash stack_traces and crash user | [optional] |
| **$orderby** | **String**| the OData-like $orderby argument | [optional] [default to last_occurrence desc] [enum: last_occurrence asc, last_occurrence desc, count asc, count desc, display_id asc, display_id desc, impacted_users asc, impacted_users desc] |
| **continuationToken** | **String**| Cassandra request continuation token. The token is used for pagination. | [optional] |

### Return type

[**CrashGroupsList200Response**](CrashGroupsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashGroupsUpdate"></a>
# **crashGroupsUpdate**
> CrashGroupsList200ResponseCrashGroupsInner crashGroupsUpdate(crashGroupId, ownerName, appName, crashGroupsUpdateRequest)



Updates a group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | id of a specific group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    CrashGroupsUpdateRequest crashGroupsUpdateRequest = new CrashGroupsUpdateRequest(); // CrashGroupsUpdateRequest | Group change object. All fields are optional and only provided fields will get updated.
    try {
      CrashGroupsList200ResponseCrashGroupsInner result = apiInstance.crashGroupsUpdate(crashGroupId, ownerName, appName, crashGroupsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashGroupsUpdate");
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
| **crashGroupId** | **String**| id of a specific group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **crashGroupsUpdateRequest** | [**CrashGroupsUpdateRequest**](CrashGroupsUpdateRequest.md)| Group change object. All fields are optional and only provided fields will get updated. | |

### Return type

[**CrashGroupsList200ResponseCrashGroupsInner**](CrashGroupsList200ResponseCrashGroupsInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesDelete"></a>
# **crashesDelete**
> CrashesDelete200Response crashesDelete(crashGroupId, crashId, ownerName, appName, retentionDelete)



Delete a specific crash and related attachments and blobs for an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | id of a specific group
    String crashId = "crashId_example"; // String | id of a specific crash
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean retentionDelete = false; // Boolean | true in that case if the method should skip update counts
    try {
      CrashesDelete200Response result = apiInstance.crashesDelete(crashGroupId, crashId, ownerName, appName, retentionDelete);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesDelete");
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
| **crashGroupId** | **String**| id of a specific group | |
| **crashId** | **String**| id of a specific crash | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **retentionDelete** | **Boolean**| true in that case if the method should skip update counts | [optional] [default to false] |

### Return type

[**CrashesDelete200Response**](CrashesDelete200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesGet"></a>
# **crashesGet**
> Crash crashesGet(crashGroupId, crashId, ownerName, appName, includeReport, includeLog, includeDetails, includeStacktrace, groupingOnly)



Gets a specific crash for an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | id of a specific group
    String crashId = "crashId_example"; // String | id of a specific crash
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean includeReport = false; // Boolean | true if the crash should include the raw crash report. Default is false
    Boolean includeLog = false; // Boolean | true if the crash should include the custom log report. Default is false
    Boolean includeDetails = false; // Boolean | true if the crash should include in depth crash details
    Boolean includeStacktrace = false; // Boolean | true if the crash should include the stacktrace information
    Boolean groupingOnly = false; // Boolean | true if the stacktrace should be only the relevant thread / exception. Default is false
    try {
      Crash result = apiInstance.crashesGet(crashGroupId, crashId, ownerName, appName, includeReport, includeLog, includeDetails, includeStacktrace, groupingOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesGet");
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
| **crashGroupId** | **String**| id of a specific group | |
| **crashId** | **String**| id of a specific crash | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **includeReport** | **Boolean**| true if the crash should include the raw crash report. Default is false | [optional] [default to false] |
| **includeLog** | **Boolean**| true if the crash should include the custom log report. Default is false | [optional] [default to false] |
| **includeDetails** | **Boolean**| true if the crash should include in depth crash details | [optional] [default to false] |
| **includeStacktrace** | **Boolean**| true if the crash should include the stacktrace information | [optional] [default to false] |
| **groupingOnly** | **Boolean**| true if the stacktrace should be only the relevant thread / exception. Default is false | [optional] [default to false] |

### Return type

[**Crash**](Crash.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | Error |  -  |

<a id="crashesGetAppCrashesInfo"></a>
# **crashesGetAppCrashesInfo**
> CrashesGetAppCrashesInfo200Response crashesGetAppCrashesInfo(ownerName, appName)



Gets whether the application has any crashes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      CrashesGetAppCrashesInfo200Response result = apiInstance.crashesGetAppCrashesInfo(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesGetAppCrashesInfo");
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

[**CrashesGetAppCrashesInfo200Response**](CrashesGetAppCrashesInfo200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesGetAppVersions"></a>
# **crashesGetAppVersions**
> List&lt;CrashesGetAppVersions200ResponseInner&gt; crashesGetAppVersions(ownerName, appName)



Gets a list of application versions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<CrashesGetAppVersions200ResponseInner> result = apiInstance.crashesGetAppVersions(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesGetAppVersions");
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

[**List&lt;CrashesGetAppVersions200ResponseInner&gt;**](CrashesGetAppVersions200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesGetCrashAttachmentLocation"></a>
# **crashesGetCrashAttachmentLocation**
> CrashesGetCrashAttachmentLocation200Response crashesGetCrashAttachmentLocation(crashId, attachmentId, ownerName, appName)



Gets the URI location to download crash attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashId = "crashId_example"; // String | id of a specific crash
    String attachmentId = "attachmentId_example"; // String | attachment id
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      CrashesGetCrashAttachmentLocation200Response result = apiInstance.crashesGetCrashAttachmentLocation(crashId, attachmentId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesGetCrashAttachmentLocation");
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
| **crashId** | **String**| id of a specific crash | |
| **attachmentId** | **String**| attachment id | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**CrashesGetCrashAttachmentLocation200Response**](CrashesGetCrashAttachmentLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesGetCrashTextAttachmentContent"></a>
# **crashesGetCrashTextAttachmentContent**
> String crashesGetCrashTextAttachmentContent(crashId, attachmentId, ownerName, appName)



Gets content of the text attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashId = "crashId_example"; // String | id of a specific crash
    String attachmentId = "attachmentId_example"; // String | attachment id
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      String result = apiInstance.crashesGetCrashTextAttachmentContent(crashId, attachmentId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesGetCrashTextAttachmentContent");
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
| **crashId** | **String**| id of a specific crash | |
| **attachmentId** | **String**| attachment id | |
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
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesGetNativeCrash"></a>
# **crashesGetNativeCrash**
> String crashesGetNativeCrash(crashGroupId, crashId, ownerName, appName)



Gets the native log of a specific crash.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | id of a specific group
    String crashId = "crashId_example"; // String | id of a specific crash
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      String result = apiInstance.crashesGetNativeCrash(crashGroupId, crashId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesGetNativeCrash");
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
| **crashGroupId** | **String**| id of a specific group | |
| **crashId** | **String**| id of a specific crash | |
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
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesGetNativeCrashDownload"></a>
# **crashesGetNativeCrashDownload**
> String crashesGetNativeCrashDownload(crashGroupId, crashId, ownerName, appName)



Gets the native log of a specific crash as a text attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | id of a specific group
    String crashId = "crashId_example"; // String | id of a specific crash
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      String result = apiInstance.crashesGetNativeCrashDownload(crashGroupId, crashId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesGetNativeCrashDownload");
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
| **crashGroupId** | **String**| id of a specific group | |
| **crashId** | **String**| id of a specific crash | |
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
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesGetRawCrashLocation"></a>
# **crashesGetRawCrashLocation**
> CrashesGetRawCrashLocation200Response crashesGetRawCrashLocation(crashGroupId, crashId, ownerName, appName)



Gets the URI location to download json of a specific crash.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | id of a specific group
    String crashId = "crashId_example"; // String | id of a specific crash
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      CrashesGetRawCrashLocation200Response result = apiInstance.crashesGetRawCrashLocation(crashGroupId, crashId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesGetRawCrashLocation");
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
| **crashGroupId** | **String**| id of a specific group | |
| **crashId** | **String**| id of a specific crash | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**CrashesGetRawCrashLocation200Response**](CrashesGetRawCrashLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesGetStacktrace"></a>
# **crashesGetStacktrace**
> Stacktrace crashesGetStacktrace(crashGroupId, crashId, ownerName, appName, groupingOnly)



Gets a stacktrace for a specific crash.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | id of a specific group
    String crashId = "crashId_example"; // String | id of a specific crash
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean groupingOnly = false; // Boolean | true if the stacktrace should be only the relevant thread / exception. Default is false
    try {
      Stacktrace result = apiInstance.crashesGetStacktrace(crashGroupId, crashId, ownerName, appName, groupingOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesGetStacktrace");
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
| **crashGroupId** | **String**| id of a specific group | |
| **crashId** | **String**| id of a specific crash | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **groupingOnly** | **Boolean**| true if the stacktrace should be only the relevant thread / exception. Default is false | [optional] [default to false] |

### Return type

[**Stacktrace**](Stacktrace.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesList"></a>
# **crashesList**
> List&lt;Crash&gt; crashesList(crashGroupId, ownerName, appName, includeReport, includeLog, dateFrom, dateTo, appVersion, errorType)



Gets all crashes of a group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashGroupId = "crashGroupId_example"; // String | id of a specific group
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Boolean includeReport = false; // Boolean | true if the crash should include the raw crash report. Default is false
    Boolean includeLog = false; // Boolean | true if the crash should include the custom log report. Default is false
    OffsetDateTime dateFrom = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime dateTo = OffsetDateTime.now(); // OffsetDateTime | 
    String appVersion = "appVersion_example"; // String | version
    String errorType = "CrashingErrors"; // String | 
    try {
      List<Crash> result = apiInstance.crashesList(crashGroupId, ownerName, appName, includeReport, includeLog, dateFrom, dateTo, appVersion, errorType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesList");
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
| **crashGroupId** | **String**| id of a specific group | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **includeReport** | **Boolean**| true if the crash should include the raw crash report. Default is false | [optional] [default to false] |
| **includeLog** | **Boolean**| true if the crash should include the custom log report. Default is false | [optional] [default to false] |
| **dateFrom** | **OffsetDateTime**|  | [optional] |
| **dateTo** | **OffsetDateTime**|  | [optional] |
| **appVersion** | **String**| version | [optional] |
| **errorType** | **String**|  | [optional] [enum: CrashingErrors, HandledErrors] |

### Return type

[**List&lt;Crash&gt;**](Crash.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="crashesListAttachments"></a>
# **crashesListAttachments**
> List&lt;CrashesListAttachments200ResponseInner&gt; crashesListAttachments(crashId, ownerName, appName)



Gets all attachments for a specific crash.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String crashId = "crashId_example"; // String | id of a specific crash
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<CrashesListAttachments200ResponseInner> result = apiInstance.crashesListAttachments(crashId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#crashesListAttachments");
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
| **crashId** | **String**| id of a specific crash | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;CrashesListAttachments200ResponseInner&gt;**](CrashesListAttachments200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="missingSymbolGroupsGet"></a>
# **missingSymbolGroupsGet**
> MissingSymbolGroupsList200Response missingSymbolGroupsGet(symbolGroupId, ownerName, appName)

Gets missing symbol crash group by its id

Gets missing symbol crash group by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String symbolGroupId = "symbolGroupId_example"; // String | missing symbol crash group id
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      MissingSymbolGroupsList200Response result = apiInstance.missingSymbolGroupsGet(symbolGroupId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#missingSymbolGroupsGet");
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
| **symbolGroupId** | **String**| missing symbol crash group id | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**MissingSymbolGroupsList200Response**](MissingSymbolGroupsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="missingSymbolGroupsInfo"></a>
# **missingSymbolGroupsInfo**
> MissingSymbolGroupsInfo200Response missingSymbolGroupsInfo(ownerName, appName)

Gets application level statistics for all missing symbol groups

Gets application level statistics for all missing symbol groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      MissingSymbolGroupsInfo200Response result = apiInstance.missingSymbolGroupsInfo(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#missingSymbolGroupsInfo");
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

[**MissingSymbolGroupsInfo200Response**](MissingSymbolGroupsInfo200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="missingSymbolGroupsList"></a>
# **missingSymbolGroupsList**
> MissingSymbolGroupsList200Response missingSymbolGroupsList(top, ownerName, appName)

Gets top N (ordered by crash count) of crash groups by missing symbol

Gets top N (ordered by crash count) of crash groups by missing symbol

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    Integer top = 56; // Integer | top N elements
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      MissingSymbolGroupsList200Response result = apiInstance.missingSymbolGroupsList(top, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#missingSymbolGroupsList");
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
| **top** | **Integer**| top N elements | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**MissingSymbolGroupsList200Response**](MissingSymbolGroupsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="symbolUploadsComplete"></a>
# **symbolUploadsComplete**
> SymbolUploadsList200ResponseInner symbolUploadsComplete(symbolUploadId, ownerName, appName, symbolUploadsCompleteRequest)



Commits or aborts the symbol upload process for a new set of symbols for the specified application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String symbolUploadId = "symbolUploadId_example"; // String | The ID of the symbol upload
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    SymbolUploadsCompleteRequest symbolUploadsCompleteRequest = new SymbolUploadsCompleteRequest(); // SymbolUploadsCompleteRequest | The symbol information
    try {
      SymbolUploadsList200ResponseInner result = apiInstance.symbolUploadsComplete(symbolUploadId, ownerName, appName, symbolUploadsCompleteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolUploadsComplete");
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
| **symbolUploadId** | **String**| The ID of the symbol upload | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **symbolUploadsCompleteRequest** | [**SymbolUploadsCompleteRequest**](SymbolUploadsCompleteRequest.md)| The symbol information | |

### Return type

[**SymbolUploadsList200ResponseInner**](SymbolUploadsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **403** | Unauthorized |  -  |
| **500** | Internal error |  -  |

<a id="symbolUploadsCreate"></a>
# **symbolUploadsCreate**
> SymbolUploadsCreate200Response symbolUploadsCreate(ownerName, appName, symbolUploadsCreateRequest)



Begins the symbol upload process for a new set of symbols for the specified application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    SymbolUploadsCreateRequest symbolUploadsCreateRequest = new SymbolUploadsCreateRequest(); // SymbolUploadsCreateRequest | The symbol information
    try {
      SymbolUploadsCreate200Response result = apiInstance.symbolUploadsCreate(ownerName, appName, symbolUploadsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolUploadsCreate");
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
| **symbolUploadsCreateRequest** | [**SymbolUploadsCreateRequest**](SymbolUploadsCreateRequest.md)| The symbol information | |

### Return type

[**SymbolUploadsCreate200Response**](SymbolUploadsCreate200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **403** | Unauthorized |  -  |
| **500** | Internal error |  -  |

<a id="symbolUploadsDelete"></a>
# **symbolUploadsDelete**
> SymbolUploadsList200ResponseInner symbolUploadsDelete(symbolUploadId, ownerName, appName)



Deletes a symbol upload by id for the specified application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String symbolUploadId = "symbolUploadId_example"; // String | The ID of the symbol upload
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      SymbolUploadsList200ResponseInner result = apiInstance.symbolUploadsDelete(symbolUploadId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolUploadsDelete");
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
| **symbolUploadId** | **String**| The ID of the symbol upload | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**SymbolUploadsList200ResponseInner**](SymbolUploadsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal error |  -  |

<a id="symbolUploadsGet"></a>
# **symbolUploadsGet**
> SymbolUploadsList200ResponseInner symbolUploadsGet(symbolUploadId, ownerName, appName)



Gets a symbol upload by id for the specified application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String symbolUploadId = "symbolUploadId_example"; // String | The ID of the symbol upload
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      SymbolUploadsList200ResponseInner result = apiInstance.symbolUploadsGet(symbolUploadId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolUploadsGet");
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
| **symbolUploadId** | **String**| The ID of the symbol upload | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**SymbolUploadsList200ResponseInner**](SymbolUploadsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal error |  -  |

<a id="symbolUploadsGetLocation"></a>
# **symbolUploadsGetLocation**
> SymbolUploadsGetLocation200Response symbolUploadsGetLocation(symbolUploadId, ownerName, appName)



Gets the URL to download the symbol upload

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String symbolUploadId = "symbolUploadId_example"; // String | The ID of the symbol upload
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      SymbolUploadsGetLocation200Response result = apiInstance.symbolUploadsGetLocation(symbolUploadId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolUploadsGetLocation");
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
| **symbolUploadId** | **String**| The ID of the symbol upload | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**SymbolUploadsGetLocation200Response**](SymbolUploadsGetLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal error |  -  |

<a id="symbolUploadsList"></a>
# **symbolUploadsList**
> List&lt;SymbolUploadsList200ResponseInner&gt; symbolUploadsList(ownerName, appName, top, status, symbolType)



Gets a list of all uploads for the specified application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Long top = 30L; // Long | The maximum number of results to return.
    String status = "all"; // String | Filter results by the current status of a symbol upload: * all: all states in the symbol upload process. Includes created, aborted, committed, processing, indexed and failed states * uploaded: all states after package is uploaded. Includes committed, processing, indexed and failed states * processed: symbol upload processing is completed. Includes indexed and failed states. 
    String symbolType = "AndroidProguard"; // String | The type of symbols
    try {
      List<SymbolUploadsList200ResponseInner> result = apiInstance.symbolUploadsList(ownerName, appName, top, status, symbolType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolUploadsList");
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
| **top** | **Long**| The maximum number of results to return. | [optional] [default to 30] |
| **status** | **String**| Filter results by the current status of a symbol upload: * all: all states in the symbol upload process. Includes created, aborted, committed, processing, indexed and failed states * uploaded: all states after package is uploaded. Includes committed, processing, indexed and failed states * processed: symbol upload processing is completed. Includes indexed and failed states.  | [optional] [enum: all, uploaded, processed] |
| **symbolType** | **String**| The type of symbols | [optional] [enum: AndroidProguard, Apple, Breakpad, JavaScript, UWP] |

### Return type

[**List&lt;SymbolUploadsList200ResponseInner&gt;**](SymbolUploadsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Unauthorized |  -  |
| **500** | Internal error |  -  |

<a id="symbolsGet"></a>
# **symbolsGet**
> SymbolsList200ResponseInner symbolsGet(symbolId, ownerName, appName)



Returns a particular symbol by id (uuid) for the provided application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String symbolId = "symbolId_example"; // String | The ID of the symbol (uuid of the symbol)
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      SymbolsList200ResponseInner result = apiInstance.symbolsGet(symbolId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolsGet");
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
| **symbolId** | **String**| The ID of the symbol (uuid of the symbol) | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**SymbolsList200ResponseInner**](SymbolsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal error |  -  |

<a id="symbolsGetLocation"></a>
# **symbolsGetLocation**
> SymbolsGetLocation200Response symbolsGetLocation(symbolId, ownerName, appName)



Gets the URL to download the symbol

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String symbolId = "symbolId_example"; // String | The ID of the symbol (uuid of the symbol)
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      SymbolsGetLocation200Response result = apiInstance.symbolsGetLocation(symbolId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolsGetLocation");
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
| **symbolId** | **String**| The ID of the symbol (uuid of the symbol) | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**SymbolsGetLocation200Response**](SymbolsGetLocation200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal error |  -  |

<a id="symbolsGetStatus"></a>
# **symbolsGetStatus**
> SymbolsGetStatus200Response symbolsGetStatus(symbolId, ownerName, appName)



Returns a particular symbol by id (uuid) for the provided application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String symbolId = "symbolId_example"; // String | The ID of the symbol (uuid of the symbol)
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      SymbolsGetStatus200Response result = apiInstance.symbolsGetStatus(symbolId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolsGetStatus");
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
| **symbolId** | **String**| The ID of the symbol (uuid of the symbol) | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**SymbolsGetStatus200Response**](SymbolsGetStatus200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal error |  -  |

<a id="symbolsIgnore"></a>
# **symbolsIgnore**
> SymbolsList200ResponseInner symbolsIgnore(symbolId, ownerName, appName)



Marks a symbol by id (uuid) as ignored

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String symbolId = "symbolId_example"; // String | The ID of the symbol (uuid of the symbol)
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      SymbolsList200ResponseInner result = apiInstance.symbolsIgnore(symbolId, ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolsIgnore");
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
| **symbolId** | **String**| The ID of the symbol (uuid of the symbol) | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**SymbolsList200ResponseInner**](SymbolsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **500** | Internal error |  -  |

<a id="symbolsList"></a>
# **symbolsList**
> List&lt;SymbolsList200ResponseInner&gt; symbolsList(ownerName, appName)



Returns the list of all symbols for the provided application

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrashApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    CrashApi apiInstance = new CrashApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<SymbolsList200ResponseInner> result = apiInstance.symbolsList(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrashApi#symbolsList");
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

[**List&lt;SymbolsList200ResponseInner&gt;**](SymbolsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Unauthorized |  -  |
| **500** | Internal error |  -  |

