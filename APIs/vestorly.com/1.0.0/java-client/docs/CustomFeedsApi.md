# CustomFeedsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomFeed**](CustomFeedsApi.md#createCustomFeed) | **POST** /custom_feeds |  |
| [**deleteCustomFeed**](CustomFeedsApi.md#deleteCustomFeed) | **DELETE** /custom_feeds/{id} |  |
| [**duplicateCustomFeed**](CustomFeedsApi.md#duplicateCustomFeed) | **POST** /custom_feeds/{id}/duplicates |  |
| [**findCustomFeedByID**](CustomFeedsApi.md#findCustomFeedByID) | **GET** /custom_feeds/{id} |  |
| [**findCustomFeeds**](CustomFeedsApi.md#findCustomFeeds) | **GET** /custom_feeds |  |
| [**updateCategoryById**](CustomFeedsApi.md#updateCategoryById) | **PUT** /custom_feeds/{id} |  |


<a id="createCustomFeed"></a>
# **createCustomFeed**
> CustomFeedresponse createCustomFeed(vestorlyAuth, customFeed, accessToken)



Creates a new Category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedsApi apiInstance = new CustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    CustomFeedInput customFeed = new CustomFeedInput(); // CustomFeedInput | Category to add
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeedresponse result = apiInstance.createCustomFeed(vestorlyAuth, customFeed, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedsApi#createCustomFeed");
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
| **customFeed** | [**CustomFeedInput**](CustomFeedInput.md)| Category to add | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**CustomFeedresponse**](CustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom Feed response |  -  |

<a id="deleteCustomFeed"></a>
# **deleteCustomFeed**
> CustomFeedresponse deleteCustomFeed(vestorlyAuth, id, accessToken)



Deletes a new Category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedsApi apiInstance = new CustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | id of category to delete
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeedresponse result = apiInstance.deleteCustomFeed(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedsApi#deleteCustomFeed");
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
| **id** | **String**| id of category to delete | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**CustomFeedresponse**](CustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom Feed response |  -  |

<a id="duplicateCustomFeed"></a>
# **duplicateCustomFeed**
> CustomFeedresponse duplicateCustomFeed(vestorlyAuth, id, accessToken)



Duplicates Category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedsApi apiInstance = new CustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | id of category to duplicate
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeedresponse result = apiInstance.duplicateCustomFeed(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedsApi#duplicateCustomFeed");
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
| **id** | **String**| id of category to duplicate | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**CustomFeedresponse**](CustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom Feed response |  -  |

<a id="findCustomFeedByID"></a>
# **findCustomFeedByID**
> CustomFeedresponse findCustomFeedByID(vestorlyAuth, id, accessToken)



Returns a single Category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedsApi apiInstance = new CustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | Custom Feed Id to fetch
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeedresponse result = apiInstance.findCustomFeedByID(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedsApi#findCustomFeedByID");
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
| **id** | **String**| Custom Feed Id to fetch | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**CustomFeedresponse**](CustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom Feed response |  -  |

<a id="findCustomFeeds"></a>
# **findCustomFeeds**
> CustomFeeds findCustomFeeds(vestorlyAuth, accessToken)



Returns all Categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedsApi apiInstance = new CustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeeds result = apiInstance.findCustomFeeds(vestorlyAuth, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedsApi#findCustomFeeds");
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

[**CustomFeeds**](CustomFeeds.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="updateCategoryById"></a>
# **updateCategoryById**
> CustomFeedresponse updateCategoryById(vestorlyAuth, id, customFeed, accessToken)



Updates a Category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedsApi apiInstance = new CustomFeedsApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | id of category to update
    CustomFeedInput customFeed = new CustomFeedInput(); // CustomFeedInput | Category to add
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeedresponse result = apiInstance.updateCategoryById(vestorlyAuth, id, customFeed, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedsApi#updateCategoryById");
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
| **id** | **String**| id of category to update | |
| **customFeed** | [**CustomFeedInput**](CustomFeedInput.md)| Category to add | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**CustomFeedresponse**](CustomFeedresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom Feed response |  -  |

