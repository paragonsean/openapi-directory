# SourcesApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSource**](SourcesApi.md#createSource) | **POST** /sources |  |
| [**findSources**](SourcesApi.md#findSources) | **GET** /sources |  |
| [**getSourceByID**](SourcesApi.md#getSourceByID) | **GET** /sources/{id} |  |
| [**updateSourceByID**](SourcesApi.md#updateSourceByID) | **PUT** /sources/{id} |  |


<a id="createSource"></a>
# **createSource**
> Sourceresponse createSource(vestorlyAuth, source, accessToken)



Create source

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    SourceInput source = new SourceInput(); // SourceInput | Source
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Sourceresponse result = apiInstance.createSource(vestorlyAuth, source, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#createSource");
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
| **source** | [**SourceInput**](SourceInput.md)| Source | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Sourceresponse**](Sourceresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | source response |  -  |

<a id="findSources"></a>
# **findSources**
> Sources findSources(vestorlyAuth, accessToken)



Returns all sources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Sources result = apiInstance.findSources(vestorlyAuth, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#findSources");
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

[**Sources**](Sources.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | source response |  -  |

<a id="getSourceByID"></a>
# **getSourceByID**
> Sourceresponse getSourceByID(vestorlyAuth, id, accessToken)



Get Source By ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | ID of source to fetch
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Sourceresponse result = apiInstance.getSourceByID(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#getSourceByID");
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
| **id** | **String**| ID of source to fetch | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Sourceresponse**](Sourceresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | source response |  -  |

<a id="updateSourceByID"></a>
# **updateSourceByID**
> Sourceresponse updateSourceByID(vestorlyAuth, id, source, accessToken)



Update Source By ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    SourcesApi apiInstance = new SourcesApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | ID of source to fetch
    SourceInput source = new SourceInput(); // SourceInput | Source
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Sourceresponse result = apiInstance.updateSourceByID(vestorlyAuth, id, source, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourcesApi#updateSourceByID");
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
| **id** | **String**| ID of source to fetch | |
| **source** | [**SourceInput**](SourceInput.md)| Source | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Sourceresponse**](Sourceresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | source response |  -  |

