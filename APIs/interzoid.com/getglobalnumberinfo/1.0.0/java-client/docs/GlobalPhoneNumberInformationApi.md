# GlobalPhoneNumberInformationApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getglobalnumberinfo**](GlobalPhoneNumberInformationApi.md#getglobalnumberinfo) | **GET** /getglobalnumberinfo | Get demographic information for a global telephone number |


<a id="getglobalnumberinfo"></a>
# **getglobalnumberinfo**
> Getglobalnumberinfo200Response getglobalnumberinfo(license, intlnumber)

Get demographic information for a global telephone number

Get demographic information for a global telephone number, including city and country information, primary languages spoken, and mobile device identification.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GlobalPhoneNumberInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    GlobalPhoneNumberInformationApi apiInstance = new GlobalPhoneNumberInformationApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String intlnumber = "intlnumber_example"; // String | International number (with country code) to retrieve information for
    try {
      Getglobalnumberinfo200Response result = apiInstance.getglobalnumberinfo(license, intlnumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GlobalPhoneNumberInformationApi#getglobalnumberinfo");
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
| **intlnumber** | **String**| International number (with country code) to retrieve information for | |

### Return type

[**Getglobalnumberinfo200Response**](Getglobalnumberinfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Global telephone demographic information |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **404** | telephone number not found |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

