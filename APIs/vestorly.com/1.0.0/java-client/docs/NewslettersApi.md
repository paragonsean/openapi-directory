# NewslettersApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findNewsletters**](NewslettersApi.md#findNewsletters) | **GET** /newsletters |  |
| [**getNewsletterByID**](NewslettersApi.md#getNewsletterByID) | **GET** /newsletters/{id} |  |
| [**updateNewsletterByID**](NewslettersApi.md#updateNewsletterByID) | **PUT** /newsletters/{id} |  |


<a id="findNewsletters"></a>
# **findNewsletters**
> Newsletters findNewsletters(vestorlyAuth, accessToken)



Returns all newsletters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NewslettersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    NewslettersApi apiInstance = new NewslettersApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Newsletters result = apiInstance.findNewsletters(vestorlyAuth, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NewslettersApi#findNewsletters");
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

[**Newsletters**](Newsletters.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newsletter response |  -  |

<a id="getNewsletterByID"></a>
# **getNewsletterByID**
> Newsletterresponse getNewsletterByID(vestorlyAuth, id, accessToken)



Get a newsletter by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NewslettersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    NewslettersApi apiInstance = new NewslettersApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | Mongo ID of event to get
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Newsletterresponse result = apiInstance.getNewsletterByID(vestorlyAuth, id, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NewslettersApi#getNewsletterByID");
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
| **id** | **String**| Mongo ID of event to get | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Newsletterresponse**](Newsletterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newsletter response |  -  |

<a id="updateNewsletterByID"></a>
# **updateNewsletterByID**
> Newsletterresponse updateNewsletterByID(vestorlyAuth, id, newsletter, accessToken)



Updates a newsletter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NewslettersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.vestorly.com/api/v2");
    
    // Configure OAuth2 access token for authorization: access_token
    OAuth access_token = (OAuth) defaultClient.getAuthentication("access_token");
    access_token.setAccessToken("YOUR ACCESS TOKEN");

    NewslettersApi apiInstance = new NewslettersApi(defaultClient);
    String vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
    String id = "id_example"; // String | Mongo ID of event to update
    NewsletterInput newsletter = new NewsletterInput(); // NewsletterInput | Newsletter
    String accessToken = "accessToken_example"; // String | OAuth Token
    try {
      Newsletterresponse result = apiInstance.updateNewsletterByID(vestorlyAuth, id, newsletter, accessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NewslettersApi#updateNewsletterByID");
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
| **id** | **String**| Mongo ID of event to update | |
| **newsletter** | [**NewsletterInput**](NewsletterInput.md)| Newsletter | |
| **accessToken** | **String**| OAuth Token | [optional] |

### Return type

[**Newsletterresponse**](Newsletterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Newsletter response |  -  |

