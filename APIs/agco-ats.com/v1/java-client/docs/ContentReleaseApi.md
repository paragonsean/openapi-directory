# ContentReleaseApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2ContentReleasesContentReleaseIdGet**](ContentReleaseApi.md#apiV2ContentReleasesContentReleaseIdGet) | **GET** /api/v2/ContentReleases/{ContentReleaseId} | Get a Content Release Version by ID |
| [**contentReleaseDeleteContentReleaseVersionn**](ContentReleaseApi.md#contentReleaseDeleteContentReleaseVersionn) | **DELETE** /api/v2/ContentReleases/{ContentReleaseId} | Delete a ContentReleaseVersion |
| [**contentReleaseGetContentReleaseVersion**](ContentReleaseApi.md#contentReleaseGetContentReleaseVersion) | **GET** /api/v2/ContentReleases | Get ContentReleaseVersion |
| [**contentReleasePostContentRelease**](ContentReleaseApi.md#contentReleasePostContentRelease) | **POST** /api/v2/ContentReleases | Create a ContentReleaseVersion |
| [**contentReleasePutContentDefinition**](ContentReleaseApi.md#contentReleasePutContentDefinition) | **PUT** /api/v2/ContentReleases/{ContentReleaseId} | Update a ContentReleaseVersion |


<a id="apiV2ContentReleasesContentReleaseIdGet"></a>
# **apiV2ContentReleasesContentReleaseIdGet**
> ContentSubmissionSharedBusinessEntitiesContentReleaseVersion apiV2ContentReleasesContentReleaseIdGet(contentReleaseId)

Get a Content Release Version by ID

Gets a ContentReleaseVersion by ID. When successful, the response is the requested ContentReleaseVersion.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentReleaseApi apiInstance = new ContentReleaseApi(defaultClient);
    Integer contentReleaseId = 56; // Integer | The ID of the ContentReleaseVersion to get.
    try {
      ContentSubmissionSharedBusinessEntitiesContentReleaseVersion result = apiInstance.apiV2ContentReleasesContentReleaseIdGet(contentReleaseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentReleaseApi#apiV2ContentReleasesContentReleaseIdGet");
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
| **contentReleaseId** | **Integer**| The ID of the ContentReleaseVersion to get. | |

### Return type

[**ContentSubmissionSharedBusinessEntitiesContentReleaseVersion**](ContentSubmissionSharedBusinessEntitiesContentReleaseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="contentReleaseDeleteContentReleaseVersionn"></a>
# **contentReleaseDeleteContentReleaseVersionn**
> contentReleaseDeleteContentReleaseVersionn(contentReleaseId)

Delete a ContentReleaseVersion

Deletes an ContentReleaseVersion. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentReleaseApi apiInstance = new ContentReleaseApi(defaultClient);
    Integer contentReleaseId = 56; // Integer | The ID of the ContentReleaseVersion to delete
    try {
      apiInstance.contentReleaseDeleteContentReleaseVersionn(contentReleaseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentReleaseApi#contentReleaseDeleteContentReleaseVersionn");
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
| **contentReleaseId** | **Integer**| The ID of the ContentReleaseVersion to delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="contentReleaseGetContentReleaseVersion"></a>
# **contentReleaseGetContentReleaseVersion**
> APIPagedResponseContentSubmissionSharedBusinessEntitiesContentReleaseVersion contentReleaseGetContentReleaseVersion(limit, offset, deleted, releaseID, userId, contentDefinitionID, version)

Get ContentReleaseVersion

Gets a collection of ContentReleaseVersion. When successful, the response is a PagedResponse of ContentReleaseVersion.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentReleaseApi apiInstance = new ContentReleaseApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    Boolean deleted = true; // Boolean | Optional. Filter by deleted.
    Integer releaseID = 56; // Integer | Optional. Filter by releaseID.
    Integer userId = 56; // Integer | Optional. Filter by UserID.
    Integer contentDefinitionID = 56; // Integer | Optional. Filter by ContentDefinitionID.
    Integer version = 56; // Integer | Optional. Filter by Version.
    try {
      APIPagedResponseContentSubmissionSharedBusinessEntitiesContentReleaseVersion result = apiInstance.contentReleaseGetContentReleaseVersion(limit, offset, deleted, releaseID, userId, contentDefinitionID, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentReleaseApi#contentReleaseGetContentReleaseVersion");
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
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **deleted** | **Boolean**| Optional. Filter by deleted. | [optional] |
| **releaseID** | **Integer**| Optional. Filter by releaseID. | [optional] |
| **userId** | **Integer**| Optional. Filter by UserID. | [optional] |
| **contentDefinitionID** | **Integer**| Optional. Filter by ContentDefinitionID. | [optional] |
| **version** | **Integer**| Optional. Filter by Version. | [optional] |

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesContentReleaseVersion**](APIPagedResponseContentSubmissionSharedBusinessEntitiesContentReleaseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="contentReleasePostContentRelease"></a>
# **contentReleasePostContentRelease**
> Integer contentReleasePostContentRelease(contentSubmissionSharedBusinessEntitiesContentReleaseVersion)

Create a ContentReleaseVersion

Creates a ContentReleaseVersion.  The body of the POST is the ContentReleaseVersion to create.              The ContentReleaseId will be assigned on creation of the Job.  When successful, the response              is the contentReleaseId.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentReleaseApi apiInstance = new ContentReleaseApi(defaultClient);
    ContentSubmissionSharedBusinessEntitiesContentReleaseVersion contentSubmissionSharedBusinessEntitiesContentReleaseVersion = new ContentSubmissionSharedBusinessEntitiesContentReleaseVersion(); // ContentSubmissionSharedBusinessEntitiesContentReleaseVersion | The ContentReleaseVersion to create.
    try {
      Integer result = apiInstance.contentReleasePostContentRelease(contentSubmissionSharedBusinessEntitiesContentReleaseVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentReleaseApi#contentReleasePostContentRelease");
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
| **contentSubmissionSharedBusinessEntitiesContentReleaseVersion** | [**ContentSubmissionSharedBusinessEntitiesContentReleaseVersion**](ContentSubmissionSharedBusinessEntitiesContentReleaseVersion.md)| The ContentReleaseVersion to create. | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="contentReleasePutContentDefinition"></a>
# **contentReleasePutContentDefinition**
> contentReleasePutContentDefinition(contentReleaseId, contentSubmissionSharedBusinessEntitiesContentReleaseVersion)

Update a ContentReleaseVersion

Updates a ContentReleaseVersion.  The body of the PUT is the updated ContentReleaseVersion.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ContentReleaseApi apiInstance = new ContentReleaseApi(defaultClient);
    Integer contentReleaseId = 56; // Integer | The ID of the ContentReleaseVersion to update
    ContentSubmissionSharedBusinessEntitiesContentReleaseVersion contentSubmissionSharedBusinessEntitiesContentReleaseVersion = new ContentSubmissionSharedBusinessEntitiesContentReleaseVersion(); // ContentSubmissionSharedBusinessEntitiesContentReleaseVersion | The updated ContentReleaseVersion
    try {
      apiInstance.contentReleasePutContentDefinition(contentReleaseId, contentSubmissionSharedBusinessEntitiesContentReleaseVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentReleaseApi#contentReleasePutContentDefinition");
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
| **contentReleaseId** | **Integer**| The ID of the ContentReleaseVersion to update | |
| **contentSubmissionSharedBusinessEntitiesContentReleaseVersion** | [**ContentSubmissionSharedBusinessEntitiesContentReleaseVersion**](ContentSubmissionSharedBusinessEntitiesContentReleaseVersion.md)| The updated ContentReleaseVersion | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

