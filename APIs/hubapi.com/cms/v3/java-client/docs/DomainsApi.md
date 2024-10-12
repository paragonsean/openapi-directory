# DomainsApi

All URIs are relative to *https://api.hubapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCmsV3DomainsDomainIdGetById**](DomainsApi.md#getCmsV3DomainsDomainIdGetById) | **GET** /cms/v3/domains/{domainId} | Get a single domain |
| [**getCmsV3DomainsGetPage**](DomainsApi.md#getCmsV3DomainsGetPage) | **GET** /cms/v3/domains/ | Get current domains |


<a id="getCmsV3DomainsDomainIdGetById"></a>
# **getCmsV3DomainsDomainIdGetById**
> Domain getCmsV3DomainsDomainIdGetById(domainId)

Get a single domain

Returns a single domains with the id specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps
    ApiKeyAuth private_apps = (ApiKeyAuth) defaultClient.getAuthentication("private_apps");
    private_apps.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domainId = "domainId_example"; // String | The unique ID of the domain.
    try {
      Domain result = apiInstance.getCmsV3DomainsDomainIdGetById(domainId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getCmsV3DomainsDomainIdGetById");
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
| **domainId** | **String**| The unique ID of the domain. | |

### Return type

[**Domain**](Domain.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy), [oauth2](../README.md#oauth2), [private_apps](../README.md#private_apps)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

<a id="getCmsV3DomainsGetPage"></a>
# **getCmsV3DomainsGetPage**
> CollectionResponseWithTotalDomainForwardPaging getCmsV3DomainsGetPage(createdAt, createdAfter, createdBefore, updatedAt, updatedAfter, updatedBefore, sort, after, limit, archived)

Get current domains

Returns all existing domains that have been created. Results can be limited and filtered by creation or updated date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com");
    
    // Configure OAuth2 access token for authorization: oauth2_legacy
    OAuth oauth2_legacy = (OAuth) defaultClient.getAuthentication("oauth2_legacy");
    oauth2_legacy.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps_legacy
    ApiKeyAuth private_apps_legacy = (ApiKeyAuth) defaultClient.getAuthentication("private_apps_legacy");
    private_apps_legacy.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps_legacy.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: private_apps
    ApiKeyAuth private_apps = (ApiKeyAuth) defaultClient.getAuthentication("private_apps");
    private_apps.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //private_apps.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    OffsetDateTime createdAt = OffsetDateTime.now(); // OffsetDateTime | Only return domains created at this date.
    OffsetDateTime createdAfter = OffsetDateTime.now(); // OffsetDateTime | Only return domains created after this date.
    OffsetDateTime createdBefore = OffsetDateTime.now(); // OffsetDateTime | Only return domains created before this date.
    OffsetDateTime updatedAt = OffsetDateTime.now(); // OffsetDateTime | Only return domains updated at this date.
    OffsetDateTime updatedAfter = OffsetDateTime.now(); // OffsetDateTime | Only return domains updated after this date.
    OffsetDateTime updatedBefore = OffsetDateTime.now(); // OffsetDateTime | Only return domains updated before this date.
    List<String> sort = Arrays.asList(); // List<String> | 
    String after = "after_example"; // String | The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
    Integer limit = 56; // Integer | Maximum number of results per page.
    Boolean archived = true; // Boolean | Whether to return only results that have been archived.
    try {
      CollectionResponseWithTotalDomainForwardPaging result = apiInstance.getCmsV3DomainsGetPage(createdAt, createdAfter, createdBefore, updatedAt, updatedAfter, updatedBefore, sort, after, limit, archived);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getCmsV3DomainsGetPage");
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
| **createdAt** | **OffsetDateTime**| Only return domains created at this date. | [optional] |
| **createdAfter** | **OffsetDateTime**| Only return domains created after this date. | [optional] |
| **createdBefore** | **OffsetDateTime**| Only return domains created before this date. | [optional] |
| **updatedAt** | **OffsetDateTime**| Only return domains updated at this date. | [optional] |
| **updatedAfter** | **OffsetDateTime**| Only return domains updated after this date. | [optional] |
| **updatedBefore** | **OffsetDateTime**| Only return domains updated before this date. | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **after** | **String**| The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results. | [optional] |
| **limit** | **Integer**| Maximum number of results per page. | [optional] |
| **archived** | **Boolean**| Whether to return only results that have been archived. | [optional] |

### Return type

[**CollectionResponseWithTotalDomainForwardPaging**](CollectionResponseWithTotalDomainForwardPaging.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy), [oauth2](../README.md#oauth2), [private_apps](../README.md#private_apps)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

