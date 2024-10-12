# AddShortlinkApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addShortlink**](AddShortlinkApi.md#addShortlink) | **POST** /shortlink | add a shortlink |


<a id="addShortlink"></a>
# **addShortlink**
> ShortlinkResponse addShortlink(shortlinkRequest)

add a shortlink

add a shortlink

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddShortlinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    AddShortlinkApi apiInstance = new AddShortlinkApi(defaultClient);
    ShortlinkRequest shortlinkRequest = new ShortlinkRequest(); // ShortlinkRequest | add sub account request
    try {
      ShortlinkResponse result = apiInstance.addShortlink(shortlinkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddShortlinkApi#addShortlink");
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
| **shortlinkRequest** | [**ShortlinkRequest**](ShortlinkRequest.md)| add sub account request | |

### Return type

[**ShortlinkResponse**](ShortlinkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, exemple1

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reponse OK |  -  |
| **400** | Dysfonctionnement |  -  |

