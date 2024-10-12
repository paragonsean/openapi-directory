# ReturnsIdTrackingNumbersApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rmaTrackManagementV1AddTrackPost**](ReturnsIdTrackingNumbersApi.md#rmaTrackManagementV1AddTrackPost) | **POST** /V1/returns/{id}/tracking-numbers | returns/{id}/tracking-numbers |
| [**rmaTrackManagementV1GetTracksGet**](ReturnsIdTrackingNumbersApi.md#rmaTrackManagementV1GetTracksGet) | **GET** /V1/returns/{id}/tracking-numbers | returns/{id}/tracking-numbers |


<a id="rmaTrackManagementV1AddTrackPost"></a>
# **rmaTrackManagementV1AddTrackPost**
> Boolean rmaTrackManagementV1AddTrackPost(id, rmaTrackManagementV1AddTrackPostRequest)

returns/{id}/tracking-numbers

Add track

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsIdTrackingNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsIdTrackingNumbersApi apiInstance = new ReturnsIdTrackingNumbersApi(defaultClient);
    Integer id = 56; // Integer | 
    RmaTrackManagementV1AddTrackPostRequest rmaTrackManagementV1AddTrackPostRequest = new RmaTrackManagementV1AddTrackPostRequest(); // RmaTrackManagementV1AddTrackPostRequest | 
    try {
      Boolean result = apiInstance.rmaTrackManagementV1AddTrackPost(id, rmaTrackManagementV1AddTrackPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsIdTrackingNumbersApi#rmaTrackManagementV1AddTrackPost");
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
| **id** | **Integer**|  | |
| **rmaTrackManagementV1AddTrackPostRequest** | [**RmaTrackManagementV1AddTrackPostRequest**](RmaTrackManagementV1AddTrackPostRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="rmaTrackManagementV1GetTracksGet"></a>
# **rmaTrackManagementV1GetTracksGet**
> RmaDataTrackSearchResultInterface rmaTrackManagementV1GetTracksGet(id)

returns/{id}/tracking-numbers

Get track list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsIdTrackingNumbersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsIdTrackingNumbersApi apiInstance = new ReturnsIdTrackingNumbersApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      RmaDataTrackSearchResultInterface result = apiInstance.rmaTrackManagementV1GetTracksGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsIdTrackingNumbersApi#rmaTrackManagementV1GetTracksGet");
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
| **id** | **Integer**|  | |

### Return type

[**RmaDataTrackSearchResultInterface**](RmaDataTrackSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

