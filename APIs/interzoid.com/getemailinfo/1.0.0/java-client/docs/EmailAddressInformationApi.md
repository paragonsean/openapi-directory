# EmailAddressInformationApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getemailinfo**](EmailAddressInformationApi.md#getemailinfo) | **GET** /getemailinfo | Gets email validation information for an email address |


<a id="getemailinfo"></a>
# **getemailinfo**
> Getemailinfo200Response getemailinfo(license, email)

Gets email validation information for an email address

Get email validation information and other demographics for an email address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailAddressInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    EmailAddressInformationApi apiInstance = new EmailAddressInformationApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String email = "email_example"; // String | Email address to retrieve validation information
    try {
      Getemailinfo200Response result = apiInstance.getemailinfo(license, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailAddressInformationApi#getemailinfo");
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
| **email** | **String**| Email address to retrieve validation information | |

### Return type

[**Getemailinfo200Response**](Getemailinfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Email validation and demographic information |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **404** | email address not valid |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

