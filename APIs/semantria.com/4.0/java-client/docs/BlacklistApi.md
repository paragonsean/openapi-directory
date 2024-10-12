# BlacklistApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addBlacklist**](BlacklistApi.md#addBlacklist) | **POST** /blacklist.{content_type} | Add items to blacklist |
| [**deleteBlacklistItems**](BlacklistApi.md#deleteBlacklistItems) | **DELETE** /blacklist.{content_type} | Remove items from blacklist |
| [**getBlacklist**](BlacklistApi.md#getBlacklist) | **GET** /blacklist.{content_type} | Retrieve blacklisted items |
| [**updateBlacklist**](BlacklistApi.md#updateBlacklist) | **PUT** /blacklist.{content_type} | Update items in blacklist |


<a id="addBlacklist"></a>
# **addBlacklist**
> List&lt;BlacklistItemResponseVersion&gt; addBlacklist(contentType, blacklistedItems, configId)

Add items to blacklist

This method adds new unique items to the backlist on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlacklistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    BlacklistApi apiInstance = new BlacklistApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object blacklistedItems = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration blacklist linked to.
    try {
      List<BlacklistItemResponseVersion> result = apiInstance.addBlacklist(contentType, blacklistedItems, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlacklistApi#addBlacklist");
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
| **contentType** | **String**|  | |
| **blacklistedItems** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration blacklist linked to. | [optional] |

### Return type

[**List&lt;BlacklistItemResponseVersion&gt;**](BlacklistItemResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Number of allowed blacklisted items per configuration achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="deleteBlacklistItems"></a>
# **deleteBlacklistItems**
> deleteBlacklistItems(contentType, blacklistedItemIDs, configId)

Remove items from blacklist

This method removes certain blacklisted items by their values on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlacklistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    BlacklistApi apiInstance = new BlacklistApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    List<String> blacklistedItemIDs = Arrays.asList(); // List<String> | List of unique blacklisted item identifiers (string).
    String configId = "configId_example"; // String | Identifier of configuration blacklist items linked to.
    try {
      apiInstance.deleteBlacklistItems(contentType, blacklistedItemIDs, configId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlacklistApi#deleteBlacklistItems");
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
| **contentType** | **String**|  | |
| **blacklistedItemIDs** | [**List&lt;String&gt;**](String.md)| List of unique blacklisted item identifiers (string). | |
| **configId** | **String**| Identifier of configuration blacklist items linked to. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **403** | Forbidden. Server responds if client tries to remove primary configuration. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="getBlacklist"></a>
# **getBlacklist**
> List&lt;BlacklistItemResponseVersion&gt; getBlacklist(contentType, configId)

Retrieve blacklisted items

This method retrieves all backlisted items available on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlacklistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    BlacklistApi apiInstance = new BlacklistApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration blacklist linked to.
    try {
      List<BlacklistItemResponseVersion> result = apiInstance.getBlacklist(contentType, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlacklistApi#getBlacklist");
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
| **contentType** | **String**|  | |
| **configId** | **String**| Identifier of configuration blacklist linked to. | [optional] |

### Return type

[**List&lt;BlacklistItemResponseVersion&gt;**](BlacklistItemResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with the blacklist. |  -  |
| **202** | Client request accepted, no blacklist found. Server responds with empty body. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="updateBlacklist"></a>
# **updateBlacklist**
> List&lt;BlacklistItemResponseVersion&gt; updateBlacklist(contentType, blacklistedItems, configId)

Update items in blacklist

This method updates existing items by unique IDs in the backlist on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlacklistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    BlacklistApi apiInstance = new BlacklistApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object blacklistedItems = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration blacklist linked to.
    try {
      List<BlacklistItemResponseVersion> result = apiInstance.updateBlacklist(contentType, blacklistedItems, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlacklistApi#updateBlacklist");
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
| **contentType** | **String**|  | |
| **blacklistedItems** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration blacklist linked to. | [optional] |

### Return type

[**List&lt;BlacklistItemResponseVersion&gt;**](BlacklistItemResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Number of allowed blacklisted items per configuration achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

