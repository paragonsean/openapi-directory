# SeedCustomFeedsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSeedCustomFeed**](SeedCustomFeedsApi.md#createSeedCustomFeed) | **POST** /seed_custom_feeds |  |
| [**deleteSeedCustomFeed**](SeedCustomFeedsApi.md#deleteSeedCustomFeed) | **DELETE** /seed_custom_feeds/{id} |  |
| [**findSeedCustomFeedByID**](SeedCustomFeedsApi.md#findSeedCustomFeedByID) | **GET** /seed_custom_feeds/{id} |  |
| [**findSeedCustomFeeds**](SeedCustomFeedsApi.md#findSeedCustomFeeds) | **GET** /seed_custom_feeds |  |
| [**updateSeedCustomFeedById**](SeedCustomFeedsApi.md#updateSeedCustomFeedById) | **PUT** /seed_custom_feeds/{id} |  |


<a id="createSeedCustomFeed"></a>
# **createSeedCustomFeed**
> SeedCustomFeedresponse createSeedCustomFeed(vestorlyAuth, seedCustomFeed, accessToken)



Creates a new Category Keyword

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeedCustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    SeedCustomFeedsApi apiInstance = new SeedCustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    SeedCustomFeedInput seedCustomFeed = new SeedCustomFeedInput(); // SeedCustomFeedInput | Category to add
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      SeedCustomFeedresponse result = apiInstance.createSeedCustomFeed(vestorlyAuth, seedCustomFeed, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeedCustomFeedsApi#createSeedCustomFeed");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **seedCustomFeed** | [**SeedCustomFeedInput**](SeedCustomFeedInput.md)| Category to add | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**SeedCustomFeedresponse**](SeedCustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Seed Custom Feed response |  -  |

<a id="deleteSeedCustomFeed"></a>
# **deleteSeedCustomFeed**
> SeedCustomFeedresponse deleteSeedCustomFeed(vestorlyAuth, id, accessToken)



Deletes a Category keywords

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeedCustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    SeedCustomFeedsApi apiInstance = new SeedCustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | id of seed category to delete
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      SeedCustomFeedresponse result = apiInstance.deleteSeedCustomFeed(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeedCustomFeedsApi#deleteSeedCustomFeed");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **id** | **String**| id of seed category to delete | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**SeedCustomFeedresponse**](SeedCustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Seed Custom Feed response |  -  |

<a id="findSeedCustomFeedByID"></a>
# **findSeedCustomFeedByID**
> SeedCustomFeedresponse findSeedCustomFeedByID(vestorlyAuth, id, accessToken)



Returns a single Category keyword

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeedCustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    SeedCustomFeedsApi apiInstance = new SeedCustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | Seed Custom Feed Id to fetch
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      SeedCustomFeedresponse result = apiInstance.findSeedCustomFeedByID(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeedCustomFeedsApi#findSeedCustomFeedByID");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **id** | **String**| Seed Custom Feed Id to fetch | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**SeedCustomFeedresponse**](SeedCustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Seed Custom Feed response |  -  |

<a id="findSeedCustomFeeds"></a>
# **findSeedCustomFeeds**
> SeedCustomFeeds findSeedCustomFeeds(vestorlyAuth, accessToken)



Returns all Categories keywords

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeedCustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    SeedCustomFeedsApi apiInstance = new SeedCustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      SeedCustomFeeds result = apiInstance.findSeedCustomFeeds(vestorlyAuth, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeedCustomFeedsApi#findSeedCustomFeeds");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**SeedCustomFeeds**](SeedCustomFeeds.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="updateSeedCustomFeedById"></a>
# **updateSeedCustomFeedById**
> SeedCustomFeedresponse updateSeedCustomFeedById(vestorlyAuth, id, seedCustomFeed, accessToken)



Updates a Category keywords

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeedCustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    SeedCustomFeedsApi apiInstance = new SeedCustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | id of seed category to update
    SeedCustomFeedInput seedCustomFeed = new SeedCustomFeedInput(); // SeedCustomFeedInput | Category keywords to add
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      SeedCustomFeedresponse result = apiInstance.updateSeedCustomFeedById(vestorlyAuth, id, seedCustomFeed, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeedCustomFeedsApi#updateSeedCustomFeedById");
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
| **vestorlyAuth** | **String**| Vestorly Auth Token | |
| **id** | **String**| id of seed category to update | |
| **seedCustomFeed** | [**SeedCustomFeedInput**](SeedCustomFeedInput.md)| Category keywords to add | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**SeedCustomFeedresponse**](SeedCustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Seed Custom Feed response |  -  |

