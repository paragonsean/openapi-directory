# PersonalisedNetworksApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**myNetworksFollowsDelete**](PersonalisedNetworksApi.md#myNetworksFollowsDelete) | **DELETE** /my/networks/follows | Unfollow network |
| [**myNetworksFollowsGet**](PersonalisedNetworksApi.md#myNetworksFollowsGet) | **GET** /my/networks/follows | List of followed networks |
| [**myNetworksFollowsPost**](PersonalisedNetworksApi.md#myNetworksFollowsPost) | **POST** /my/networks/follows | Follow network |


<a id="myNetworksFollowsDelete"></a>
# **myNetworksFollowsDelete**
> myNetworksFollowsDelete(authorization, xAPIKey, body, offset, limit)

Unfollow network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalisedNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PersonalisedNetworksApi apiInstance = new PersonalisedNetworksApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Body3 body = new Body3(); // Body3 | 
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      apiInstance.myNetworksFollowsDelete(authorization, xAPIKey, body, offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalisedNetworksApi#myNetworksFollowsDelete");
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
| **body** | [**Body3**](Body3.md)|  | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

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

<a id="myNetworksFollowsGet"></a>
# **myNetworksFollowsGet**
> PersonalisedNetworksResponse myNetworksFollowsGet(authorization, xAPIKey, offset, limit)

List of followed networks

List of followed networks for a given user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalisedNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PersonalisedNetworksApi apiInstance = new PersonalisedNetworksApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      PersonalisedNetworksResponse result = apiInstance.myNetworksFollowsGet(authorization, xAPIKey, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalisedNetworksApi#myNetworksFollowsGet");
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

[**PersonalisedNetworksResponse**](PersonalisedNetworksResponse.md)

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

<a id="myNetworksFollowsPost"></a>
# **myNetworksFollowsPost**
> myNetworksFollowsPost(authorization, xAPIKey, body, offset, limit)

Follow network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonalisedNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    PersonalisedNetworksApi apiInstance = new PersonalisedNetworksApi(defaultClient);
    String authorization = "Bearer OAUTH_TOKEN"; // String | Bearer OAUTH_TOKEN
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Body2 body = new Body2(); // Body2 | 
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    try {
      apiInstance.myNetworksFollowsPost(authorization, xAPIKey, body, offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonalisedNetworksApi#myNetworksFollowsPost");
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
| **body** | [**Body2**](Body2.md)|  | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |

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

