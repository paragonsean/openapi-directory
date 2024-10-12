# UserContentDefinitionsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userContentDefinitionsDeleteUserContentDefinition**](UserContentDefinitionsApi.md#userContentDefinitionsDeleteUserContentDefinition) | **DELETE** /api/v2/UserContentDefinitions/{userContentDefinitionID} | Delete a UserContentDefinition |
| [**userContentDefinitionsGetUserContentDefinition**](UserContentDefinitionsApi.md#userContentDefinitionsGetUserContentDefinition) | **GET** /api/v2/UserContentDefinitions/{userContentDefinitionID} | Get a UserContentDefinition by ID |
| [**userContentDefinitionsGetUserContentDefinitions**](UserContentDefinitionsApi.md#userContentDefinitionsGetUserContentDefinitions) | **GET** /api/v2/UserContentDefinitions | Get UserContentDefinitions |
| [**userContentDefinitionsPostUserContentDefinition**](UserContentDefinitionsApi.md#userContentDefinitionsPostUserContentDefinition) | **POST** /api/v2/UserContentDefinitions | Create a UserContentDefinition |


<a id="userContentDefinitionsDeleteUserContentDefinition"></a>
# **userContentDefinitionsDeleteUserContentDefinition**
> userContentDefinitionsDeleteUserContentDefinition(userContentDefinitionID)

Delete a UserContentDefinition

Deletes an UserContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserContentDefinitionsApi apiInstance = new UserContentDefinitionsApi(defaultClient);
    Integer userContentDefinitionID = 56; // Integer | The ID of the UserContentDefinition to delete
    try {
      apiInstance.userContentDefinitionsDeleteUserContentDefinition(userContentDefinitionID);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContentDefinitionsApi#userContentDefinitionsDeleteUserContentDefinition");
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
| **userContentDefinitionID** | **Integer**| The ID of the UserContentDefinition to delete | |

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

<a id="userContentDefinitionsGetUserContentDefinition"></a>
# **userContentDefinitionsGetUserContentDefinition**
> ContentSubmissionSharedBusinessEntitiesUserContentDefinition userContentDefinitionsGetUserContentDefinition(userContentDefinitionID)

Get a UserContentDefinition by ID

Gets a UserContentDefinition by ID. When successful, the response is the requested UserContentDefinition.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserContentDefinitionsApi apiInstance = new UserContentDefinitionsApi(defaultClient);
    Integer userContentDefinitionID = 56; // Integer | The ID of the UserContentDefinition to get.
    try {
      ContentSubmissionSharedBusinessEntitiesUserContentDefinition result = apiInstance.userContentDefinitionsGetUserContentDefinition(userContentDefinitionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContentDefinitionsApi#userContentDefinitionsGetUserContentDefinition");
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
| **userContentDefinitionID** | **Integer**| The ID of the UserContentDefinition to get. | |

### Return type

[**ContentSubmissionSharedBusinessEntitiesUserContentDefinition**](ContentSubmissionSharedBusinessEntitiesUserContentDefinition.md)

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

<a id="userContentDefinitionsGetUserContentDefinitions"></a>
# **userContentDefinitionsGetUserContentDefinitions**
> APIPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition userContentDefinitionsGetUserContentDefinitions(limit, offset, userID, contentDefinitionID)

Get UserContentDefinitions

Gets a collection of UserContentDefinitions. When successful, the response is a PagedResponse of UserContentDefinitions.              If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserContentDefinitionsApi apiInstance = new UserContentDefinitionsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    Integer userID = 56; // Integer | Optional. Filter by UserID.
    Integer contentDefinitionID = 56; // Integer | Optional. Filter by ContentDefinitionID
    try {
      APIPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition result = apiInstance.userContentDefinitionsGetUserContentDefinitions(limit, offset, userID, contentDefinitionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContentDefinitionsApi#userContentDefinitionsGetUserContentDefinitions");
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
| **userID** | **Integer**| Optional. Filter by UserID. | [optional] |
| **contentDefinitionID** | **Integer**| Optional. Filter by ContentDefinitionID | [optional] |

### Return type

[**APIPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition**](APIPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition.md)

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

<a id="userContentDefinitionsPostUserContentDefinition"></a>
# **userContentDefinitionsPostUserContentDefinition**
> Integer userContentDefinitionsPostUserContentDefinition(contentSubmissionSharedBusinessEntitiesUserContentDefinition)

Create a UserContentDefinition

Creates a UserContentDefinition.  The body of the POST is the UserContentDefinition to create.              The UserContentDefinitionID will be assigned on creation of the Job.  When successful, the response              is the UserContentDefinitionID.  If unsuccessful, an appropriate ApiError is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserContentDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserContentDefinitionsApi apiInstance = new UserContentDefinitionsApi(defaultClient);
    ContentSubmissionSharedBusinessEntitiesUserContentDefinition contentSubmissionSharedBusinessEntitiesUserContentDefinition = new ContentSubmissionSharedBusinessEntitiesUserContentDefinition(); // ContentSubmissionSharedBusinessEntitiesUserContentDefinition | The UserContentDefinition to create.
    try {
      Integer result = apiInstance.userContentDefinitionsPostUserContentDefinition(contentSubmissionSharedBusinessEntitiesUserContentDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserContentDefinitionsApi#userContentDefinitionsPostUserContentDefinition");
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
| **contentSubmissionSharedBusinessEntitiesUserContentDefinition** | [**ContentSubmissionSharedBusinessEntitiesUserContentDefinition**](ContentSubmissionSharedBusinessEntitiesUserContentDefinition.md)| The UserContentDefinition to create. | |

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

