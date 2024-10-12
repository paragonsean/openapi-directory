# SampleResponseApi

All URIs are relative to *https://api.hubapi.com/crm/v3/extensions/cards*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCrmV3ExtensionsCardsSampleResponse**](SampleResponseApi.md#getCrmV3ExtensionsCardsSampleResponse) | **GET** /sample-response | Get sample card detail response |


<a id="getCrmV3ExtensionsCardsSampleResponse"></a>
# **getCrmV3ExtensionsCardsSampleResponse**
> IntegratorCardPayloadResponse getCrmV3ExtensionsCardsSampleResponse()

Get sample card detail response

Returns an example card detail response. This is the payload with displayed details for a card that will be shown to a user. An app should send this in response to the data fetch request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SampleResponseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hubapi.com/crm/v3/extensions/cards");

    SampleResponseApi apiInstance = new SampleResponseApi(defaultClient);
    try {
      IntegratorCardPayloadResponse result = apiInstance.getCrmV3ExtensionsCardsSampleResponse();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SampleResponseApi#getCrmV3ExtensionsCardsSampleResponse");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IntegratorCardPayloadResponse**](IntegratorCardPayloadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | An error occurred. |  -  |

