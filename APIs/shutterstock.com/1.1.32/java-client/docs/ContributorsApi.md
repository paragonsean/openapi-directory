# ContributorsApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getContributor**](ContributorsApi.md#getContributor) | **GET** /v2/contributors/{contributor_id} | Get details about a single contributor |
| [**getContributorCollectionItems**](ContributorsApi.md#getContributorCollectionItems) | **GET** /v2/contributors/{contributor_id}/collections/{id}/items | Get the items in contributors&#39; collections |
| [**getContributorCollections**](ContributorsApi.md#getContributorCollections) | **GET** /v2/contributors/{contributor_id}/collections/{id} | Get details about contributors&#39; collections |
| [**getContributorCollectionsList**](ContributorsApi.md#getContributorCollectionsList) | **GET** /v2/contributors/{contributor_id}/collections | List contributors&#39; collections |
| [**getContributorList**](ContributorsApi.md#getContributorList) | **GET** /v2/contributors | Get details about multiple contributors |


<a id="getContributor"></a>
# **getContributor**
> ContributorProfile getContributor(contributorId)

Get details about a single contributor

This endpoint shows information about a single contributor, including contributor type, equipment they use, and other attributes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ContributorsApi apiInstance = new ContributorsApi(defaultClient);
    String contributorId = "1653538"; // String | Contributor ID
    try {
      ContributorProfile result = apiInstance.getContributor(contributorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributorsApi#getContributor");
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
| **contributorId** | **String**| Contributor ID | |

### Return type

[**ContributorProfile**](ContributorProfile.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="getContributorCollectionItems"></a>
# **getContributorCollectionItems**
> CollectionItemDataList getContributorCollectionItems(contributorId, id, page, perPage, sort)

Get the items in contributors&#39; collections

This endpoint lists the IDs of items in a contributor&#39;s collection and the date that each was added.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ContributorsApi apiInstance = new ContributorsApi(defaultClient);
    String contributorId = "800506"; // String | Contributor ID
    String id = "1991678"; // String | Collection ID that belongs to the contributor
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String sort = "newest"; // String | Sort order
    try {
      CollectionItemDataList result = apiInstance.getContributorCollectionItems(contributorId, id, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributorsApi#getContributorCollectionItems");
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
| **contributorId** | **String**| Contributor ID | |
| **id** | **String**| Collection ID that belongs to the contributor | |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **sort** | **String**| Sort order | [optional] [enum: newest, oldest] |

### Return type

[**CollectionItemDataList**](CollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Set not found |  -  |

<a id="getContributorCollections"></a>
# **getContributorCollections**
> Collection getContributorCollections(contributorId, id)

Get details about contributors&#39; collections

This endpoint gets more detailed information about a contributor&#39;s collection, including its cover image, timestamps for its creation, and most recent update. To get the items in collections, use GET /v2/contributors/{contributor_id}/collections/{id}/items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ContributorsApi apiInstance = new ContributorsApi(defaultClient);
    String contributorId = "800506"; // String | Contributor ID
    String id = "1991678"; // String | Collection ID that belongs to the contributor
    try {
      Collection result = apiInstance.getContributorCollections(contributorId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributorsApi#getContributorCollections");
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
| **contributorId** | **String**| Contributor ID | |
| **id** | **String**| Collection ID that belongs to the contributor | |

### Return type

[**Collection**](Collection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Set not found |  -  |

<a id="getContributorCollectionsList"></a>
# **getContributorCollectionsList**
> CollectionDataList getContributorCollectionsList(contributorId, sort)

List contributors&#39; collections

This endpoint lists collections based on contributor ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ContributorsApi apiInstance = new ContributorsApi(defaultClient);
    String contributorId = "800506"; // String | Contributor ID
    String sort = "newest"; // String | Sort order
    try {
      CollectionDataList result = apiInstance.getContributorCollectionsList(contributorId, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributorsApi#getContributorCollectionsList");
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
| **contributorId** | **String**| Contributor ID | |
| **sort** | **String**| Sort order | [optional] [enum: newest, last_updated, item_count] |

### Return type

[**CollectionDataList**](CollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Contributor not found |  -  |

<a id="getContributorList"></a>
# **getContributorList**
> ContributorProfileDataList getContributorList(id)

Get details about multiple contributors

This endpoint lists information about one or more contributors, including contributor type, equipment they use and other attributes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContributorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ContributorsApi apiInstance = new ContributorsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | One or more contributor IDs
    try {
      ContributorProfileDataList result = apiInstance.getContributorList(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContributorsApi#getContributorList");
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
| **id** | [**List&lt;String&gt;**](String.md)| One or more contributor IDs | |

### Return type

[**ContributorProfileDataList**](ContributorProfileDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

