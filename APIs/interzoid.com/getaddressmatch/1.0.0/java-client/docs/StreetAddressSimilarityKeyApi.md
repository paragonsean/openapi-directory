# StreetAddressSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getaddressmatch**](StreetAddressSimilarityKeyApi.md#getaddressmatch) | **GET** /getaddressmatch | Gets a similarity key for matching purposes for address data |


<a id="getaddressmatch"></a>
# **getaddressmatch**
> Getaddressmatch200Response getaddressmatch(license, address)

Gets a similarity key for matching purposes for address data

Gets a similarity key for matching purposes for street address data 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StreetAddressSimilarityKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    StreetAddressSimilarityKeyApi apiInstance = new StreetAddressSimilarityKeyApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String address = "address_example"; // String | Address from which to generate similarity key
    try {
      Getaddressmatch200Response result = apiInstance.getaddressmatch(license, address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StreetAddressSimilarityKeyApi#getaddressmatch");
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
| **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | |
| **address** | **String**| Address from which to generate similarity key | |

### Return type

[**Getaddressmatch200Response**](Getaddressmatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated similarity key for address data |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

