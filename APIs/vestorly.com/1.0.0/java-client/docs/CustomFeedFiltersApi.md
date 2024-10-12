# CustomFeedFiltersApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomFeedFilter**](CustomFeedFiltersApi.md#createCustomFeedFilter) | **POST** /custom_feed_filters |  |
| [**deleteCustomFeedFilter**](CustomFeedFiltersApi.md#deleteCustomFeedFilter) | **DELETE** /custom_feed_filters/{id} |  |
| [**findCustomFeedFilterByID**](CustomFeedFiltersApi.md#findCustomFeedFilterByID) | **GET** /custom_feed_filters/{id} |  |
| [**findCustomFeedFilters**](CustomFeedFiltersApi.md#findCustomFeedFilters) | **GET** /custom_feed_filters |  |
| [**updateCustomFeedFilterById**](CustomFeedFiltersApi.md#updateCustomFeedFilterById) | **PUT** /custom_feed_filters/{id} |  |


<a id="createCustomFeedFilter"></a>
# **createCustomFeedFilter**
> CustomFeedFilterresponse createCustomFeedFilter(vestorlyAuth, customFeedFilter, accessToken)



Creates a new Category filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedFiltersApi apiInstance = new CustomFeedFiltersApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    CustomFeedFilterInput customFeedFilter = new CustomFeedFilterInput(); // CustomFeedFilterInput | Category filter to add
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeedFilterresponse result = apiInstance.createCustomFeedFilter(vestorlyAuth, customFeedFilter, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedFiltersApi#createCustomFeedFilter");
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
| **customFeedFilter** | [**CustomFeedFilterInput**](CustomFeedFilterInput.md)| Category filter to add | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**CustomFeedFilterresponse**](CustomFeedFilterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom Feed Filter response |  -  |

<a id="deleteCustomFeedFilter"></a>
# **deleteCustomFeedFilter**
> CustomFeedFilterresponse deleteCustomFeedFilter(vestorlyAuth, id, accessToken)



Deletes the Category&#39;s filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedFiltersApi apiInstance = new CustomFeedFiltersApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | id of category filter to delete
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeedFilterresponse result = apiInstance.deleteCustomFeedFilter(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedFiltersApi#deleteCustomFeedFilter");
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
| **id** | **String**| id of category filter to delete | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**CustomFeedFilterresponse**](CustomFeedFilterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom Feed Filter response |  -  |

<a id="findCustomFeedFilterByID"></a>
# **findCustomFeedFilterByID**
> CustomFeedFilterresponse findCustomFeedFilterByID(vestorlyAuth, id, accessToken)



Returns a single Category&#39;s filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedFiltersApi apiInstance = new CustomFeedFiltersApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | Custom Feed Filter Id to fetch
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeedFilterresponse result = apiInstance.findCustomFeedFilterByID(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedFiltersApi#findCustomFeedFilterByID");
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
| **id** | **String**| Custom Feed Filter Id to fetch | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**CustomFeedFilterresponse**](CustomFeedFilterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom Feed Filter response |  -  |

<a id="findCustomFeedFilters"></a>
# **findCustomFeedFilters**
> CustomFeedFilters findCustomFeedFilters(vestorlyAuth, accessToken)



Returns all Categorie&#39;s filters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedFiltersApi apiInstance = new CustomFeedFiltersApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeedFilters result = apiInstance.findCustomFeedFilters(vestorlyAuth, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedFiltersApi#findCustomFeedFilters");
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

[**CustomFeedFilters**](CustomFeedFilters.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="updateCustomFeedFilterById"></a>
# **updateCustomFeedFilterById**
> CustomFeedFilterresponse updateCustomFeedFilterById(vestorlyAuth, id, customFeedFilter, accessToken)



Updates a Category Feed Filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFeedFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    CustomFeedFiltersApi apiInstance = new CustomFeedFiltersApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | id of category filter to update
    CustomFeedFilterInput customFeedFilter = new CustomFeedFilterInput(); // CustomFeedFilterInput | Category filter to add
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      CustomFeedFilterresponse result = apiInstance.updateCustomFeedFilterById(vestorlyAuth, id, customFeedFilter, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFeedFiltersApi#updateCustomFeedFilterById");
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
| **id** | **String**| id of category filter to update | |
| **customFeedFilter** | [**CustomFeedFilterInput**](CustomFeedFilterInput.md)| Category filter to add | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**CustomFeedFilterresponse**](CustomFeedFilterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Custom Feed Filter response |  -  |

