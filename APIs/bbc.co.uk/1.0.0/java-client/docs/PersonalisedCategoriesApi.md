# PersonalisedCategoriesApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**myCategoriesFollowsDelete**](PersonalisedCategoriesApi.md#myCategoriesFollowsDelete) | **DELETE** /my/categories/follows | Unfollow category |
| [**myCategoriesFollowsGet**](PersonalisedCategoriesApi.md#myCategoriesFollowsGet) | **GET** /my/categories/follows | List of followed categories |
| [**myCategoriesFollowsPost**](PersonalisedCategoriesApi.md#myCategoriesFollowsPost) | **POST** /my/categories/follows | Follow category |


<a id="myCategoriesFollowsDelete"></a>
# **myCategoriesFollowsDelete**
> myCategoriesFollowsDelete(authorization, xAPIKey, body)

Unfollow category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalisedCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PersonalisedCategoriesApi apiInstance = new PersonalisedCategoriesApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Body1 body = new Body1(); // Body1 | 
    try {
      apiInstance.myCategoriesFollowsDelete(authorization, xAPIKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalisedCategoriesApi#myCategoriesFollowsDelete");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**Body1**](Body1.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request successfully sent to UAS. |  -  |
| **400** | The request was malformed. |  -  |
| **401** | There was an error with the supplied &#x60;Authorization&#x60; header. |  -  |

<a id="myCategoriesFollowsGet"></a>
# **myCategoriesFollowsGet**
> PersonalisedCategoriesResponse myCategoriesFollowsGet(authorization, xAPIKey, offset, limit)

List of followed categories

List of followed categories for a given user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalisedCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PersonalisedCategoriesApi apiInstance = new PersonalisedCategoriesApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      PersonalisedCategoriesResponse result = apiInstance.myCategoriesFollowsGet(authorization, xAPIKey, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalisedCategoriesApi#myCategoriesFollowsGet");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAPIKey** | **String**| API_KEY | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

### Return type

[**PersonalisedCategoriesResponse**](PersonalisedCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="myCategoriesFollowsPost"></a>
# **myCategoriesFollowsPost**
> myCategoriesFollowsPost(authorization, xAPIKey, body)

Follow category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalisedCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PersonalisedCategoriesApi apiInstance = new PersonalisedCategoriesApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Body body = new Body(); // Body | 
    try {
      apiInstance.myCategoriesFollowsPost(authorization, xAPIKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalisedCategoriesApi#myCategoriesFollowsPost");
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
| **authorization** | **String**| Bearer OAUTH_TOKEN | [default to Bearer OAUTH_TOKEN] |
| **xAPIKey** | **String**| API_KEY | |
| **body** | [**Body**](Body.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request successfully sent to UAS. |  -  |
| **400** | The request was malformed. |  -  |
| **401** | There was an error with the supplied &#x60;Authorization&#x60; header. |  -  |

