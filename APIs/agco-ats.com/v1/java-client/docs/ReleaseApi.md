# ReleaseApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**releaseDeleteReleaseBundle**](ReleaseApi.md#releaseDeleteReleaseBundle) | **DELETE** /api/v2/Releases/{ReleaseId}/Bundle/{BundleId} | Deletes the association between a release and a bundle. |
| [**releaseGetRelease**](ReleaseApi.md#releaseGetRelease) | **GET** /api/v2/Releases/{ReleaseId} | Get a  Release by ID |
| [**releaseGetReleases**](ReleaseApi.md#releaseGetReleases) | **GET** /api/v2/Releases | Get Release |
| [**releasePostRelease**](ReleaseApi.md#releasePostRelease) | **POST** /api/v2/Releases | Create a Release |
| [**releasePostReleaseBundle**](ReleaseApi.md#releasePostReleaseBundle) | **POST** /api/v2/Releases/{ReleaseId}/Bundle/{BundleId} | Associates the release with a bundle. |
| [**releasePutContentDefinition**](ReleaseApi.md#releasePutContentDefinition) | **PUT** /api/v2/Releases/{releaseId} | Update a Release |


<a id="releaseDeleteReleaseBundle"></a>
# **releaseDeleteReleaseBundle**
> releaseDeleteReleaseBundle(releaseId, bundleId)

Deletes the association between a release and a bundle.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReleaseApi apiInstance = new ReleaseApi(defaultClient);
    Integer releaseId = 56; // Integer | The release identifier.
    String bundleId = "bundleId_example"; // String | The bundle identifier.
    try {
      apiInstance.releaseDeleteReleaseBundle(releaseId, bundleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleaseApi#releaseDeleteReleaseBundle");
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
| **releaseId** | **Integer**| The release identifier. | |
| **bundleId** | **String**| The bundle identifier. | |

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

<a id="releaseGetRelease"></a>
# **releaseGetRelease**
> ContentSubmissionSharedBusinessEntitiesRelease releaseGetRelease(releaseId)

Get a  Release by ID

Gets a Release by ID. When successful, the response is the requested Release.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReleaseApi apiInstance = new ReleaseApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the Release to get.
    try {
      ContentSubmissionSharedBusinessEntitiesRelease result = apiInstance.releaseGetRelease(releaseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleaseApi#releaseGetRelease");
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
| **releaseId** | **Integer**| The ID of the Release to get. | |

### Return type

[**ContentSubmissionSharedBusinessEntitiesRelease**](ContentSubmissionSharedBusinessEntitiesRelease.md)

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

<a id="releaseGetReleases"></a>
# **releaseGetReleases**
> APIPagedResponseContentSubmissionSharedBusinessEntitiesRelease releaseGetReleases(limit, offset, visible, bundleID)

Get Release

Gets a collection of Release. When successful, the response is a PagedResponse of Release.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReleaseApi apiInstance = new ReleaseApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    Boolean visible = true; // Boolean | Optional. Filter by visible.
    String bundleID = "bundleID_example"; // String | Optional. Filter by BundleID.
    try {
      APIPagedResponseContentSubmissionSharedBusinessEntitiesRelease result = apiInstance.releaseGetReleases(limit, offset, visible, bundleID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleaseApi#releaseGetReleases");
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
| **visible** | **Boolean**| Optional. Filter by visible. | [optional] |
| **bundleID** | **String**| Optional. Filter by BundleID. | [optional] |

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesRelease**](APIPagedResponseContentSubmissionSharedBusinessEntitiesRelease.md)

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

<a id="releasePostRelease"></a>
# **releasePostRelease**
> Integer releasePostRelease(contentSubmissionSharedBusinessEntitiesRelease)

Create a Release

Creates a Release.  The body of the POST is the Release to create.              The ReleaseId will be assigned on creation of the Job.  When successful, the response              is the Release Id.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReleaseApi apiInstance = new ReleaseApi(defaultClient);
    ContentSubmissionSharedBusinessEntitiesRelease contentSubmissionSharedBusinessEntitiesRelease = new ContentSubmissionSharedBusinessEntitiesRelease(); // ContentSubmissionSharedBusinessEntitiesRelease | The Release to create.
    try {
      Integer result = apiInstance.releasePostRelease(contentSubmissionSharedBusinessEntitiesRelease);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleaseApi#releasePostRelease");
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
| **contentSubmissionSharedBusinessEntitiesRelease** | [**ContentSubmissionSharedBusinessEntitiesRelease**](ContentSubmissionSharedBusinessEntitiesRelease.md)| The Release to create. | |

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

<a id="releasePostReleaseBundle"></a>
# **releasePostReleaseBundle**
> releasePostReleaseBundle(releaseId, bundleId)

Associates the release with a bundle.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReleaseApi apiInstance = new ReleaseApi(defaultClient);
    Integer releaseId = 56; // Integer | The release identifier.
    String bundleId = "bundleId_example"; // String | The bundle identifier.
    try {
      apiInstance.releasePostReleaseBundle(releaseId, bundleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleaseApi#releasePostReleaseBundle");
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
| **releaseId** | **Integer**| The release identifier. | |
| **bundleId** | **String**| The bundle identifier. | |

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

<a id="releasePutContentDefinition"></a>
# **releasePutContentDefinition**
> releasePutContentDefinition(releaseId, contentSubmissionSharedBusinessEntitiesRelease)

Update a Release

Updates a Release.  The body of the PUT is the updated Release.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReleaseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReleaseApi apiInstance = new ReleaseApi(defaultClient);
    Integer releaseId = 56; // Integer | The ID of the Release to update
    ContentSubmissionSharedBusinessEntitiesRelease contentSubmissionSharedBusinessEntitiesRelease = new ContentSubmissionSharedBusinessEntitiesRelease(); // ContentSubmissionSharedBusinessEntitiesRelease | The updated Release
    try {
      apiInstance.releasePutContentDefinition(releaseId, contentSubmissionSharedBusinessEntitiesRelease);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReleaseApi#releasePutContentDefinition");
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
| **releaseId** | **Integer**| The ID of the Release to update | |
| **contentSubmissionSharedBusinessEntitiesRelease** | [**ContentSubmissionSharedBusinessEntitiesRelease**](ContentSubmissionSharedBusinessEntitiesRelease.md)| The updated Release | |

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

