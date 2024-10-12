# DetailedZipCodeInformationApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getzipcodeinfo**](DetailedZipCodeInformationApi.md#getzipcodeinfo) | **GET** /getzipcodeinfo | Gets detailed zip code information |


<a id="getzipcodeinfo"></a>
# **getzipcodeinfo**
> Getzipcodeinfo200Response getzipcodeinfo(license, zip)

Gets detailed zip code information

For a given zip code, detailed information is returned, including city, state, latitude, longitude, area size, and various population demographics, including income, age, and presence of farming data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DetailedZipCodeInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    DetailedZipCodeInformationApi apiInstance = new DetailedZipCodeInformationApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String zip = "zip_example"; // String | Zip code to retrieve detailed information
    try {
      Getzipcodeinfo200Response result = apiInstance.getzipcodeinfo(license, zip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DetailedZipCodeInformationApi#getzipcodeinfo");
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
| **zip** | **String**| Zip code to retrieve detailed information | |

### Return type

[**Getzipcodeinfo200Response**](Getzipcodeinfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Zip code detailed code information |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **404** | zip code not found |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

