# FeaturesApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFeatures**](FeaturesApi.md#getFeatures) | **GET** /features.{content_type} | Retrieve supported features |


<a id="getFeatures"></a>
# **getFeatures**
> List&lt;Feature&gt; getFeatures(contentType, language)

Retrieve supported features

This method returns list of supported features per languages supported by Semantria API. Let the users know about API capabilities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeaturesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    FeaturesApi apiInstance = new FeaturesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String language = "language_example"; // String | Filter features by specified language
    try {
      List<Feature> result = apiInstance.getFeatures(contentType, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeaturesApi#getFeatures");
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
| **contentType** | **String**|  | |
| **language** | **String**| Filter features by specified language | [optional] |

### Return type

[**List&lt;Feature&gt;**](Feature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with subscription details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

