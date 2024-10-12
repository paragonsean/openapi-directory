# AreaCodeInformationApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getareacode**](AreaCodeInformationApi.md#getareacode) | **GET** /getareacode | Gets telephone area code information |


<a id="getareacode"></a>
# **getareacode**
> Getareacode200Response getareacode(license, areacode)

Gets telephone area code information

Gets telephone area code information for a given area code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AreaCodeInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    AreaCodeInformationApi apiInstance = new AreaCodeInformationApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String areacode = "areacode_example"; // String | Telephone area code to retrieve area code information
    try {
      Getareacode200Response result = apiInstance.getareacode(license, areacode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AreaCodeInformationApi#getareacode");
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
| **areacode** | **String**| Telephone area code to retrieve area code information | |

### Return type

[**Getareacode200Response**](Getareacode200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Telephone area code information |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **404** | area code not found |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

