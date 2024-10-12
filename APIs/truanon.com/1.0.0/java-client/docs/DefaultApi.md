# DefaultApi

All URIs are relative to *https://staging.truanon.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProfile**](DefaultApi.md#getProfile) | **GET** /api/get_profile | Get Profile |
| [**getToken**](DefaultApi.md#getToken) | **GET** /api/request_token | Get Token |


<a id="getProfile"></a>
# **getProfile**
> getProfile(id, service)

Get Profile

get_profile Private API: Request confirmed profile data for your unique member ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.truanon.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "{{your-member-id}}"; // String | This is your unique username or member ID
    String service = "{{service-identifier}}"; // String | The service name given to you by TruAnon
    try {
      apiInstance.getProfile(id, service);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProfile");
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
| **id** | **String**| This is your unique username or member ID | [optional] |
| **service** | **String**| The service name given to you by TruAnon | [optional] |

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
| **200** |  |  -  |

<a id="getToken"></a>
# **getToken**
> getToken(id, service)

Get Token

request_token Private API: Request a Proof token to let the member confirm in a popup interface          {\&quot;id\&quot;:\&quot;qjgblv72bzzio\&quot;,\&quot;type\&quot;:\&quot;Proof\&quot;,\&quot;active\&quot;:true,\&quot;name\&quot;:\&quot;New Proof\&quot;}  Step 2. Create a verifyProfile Public Web link: Use the Proof token id as the token argument in your public URL used to open a new target popup. This activity is where members may confirm immediately.              https://staging.truanon.com/verifyProfile?id&#x3D;john_doe&amp;service&#x3D;securecannabisalliance&amp;token&#x3D;qjgblv72bzzio

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://staging.truanon.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "{{your-member-id}}"; // String | This is your unique username or member ID
    String service = "{{service-identifier}}"; // String | The service name given to you by TruAnon
    try {
      apiInstance.getToken(id, service);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getToken");
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
| **id** | **String**| This is your unique username or member ID | [optional] |
| **service** | **String**| The service name given to you by TruAnon | [optional] |

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
| **200** |  |  -  |

