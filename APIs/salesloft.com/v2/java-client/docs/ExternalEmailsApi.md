# ExternalEmailsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2ExternalEmailsJsonPost**](ExternalEmailsApi.md#v2ExternalEmailsJsonPost) | **POST** /v2/external_emails.json | Create an External Email |


<a id="v2ExternalEmailsJsonPost"></a>
# **v2ExternalEmailsJsonPost**
> ExternalEmail v2ExternalEmailsJsonPost(mailbox, raw)

Create an External Email

Creates an external email object. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalEmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    ExternalEmailsApi apiInstance = new ExternalEmailsApi(defaultClient);
    String mailbox = "mailbox_example"; // String | Email address of mailbox email was sent to
    String raw = "raw_example"; // String | Base64 encoded MIME email content
    try {
      ExternalEmail result = apiInstance.v2ExternalEmailsJsonPost(mailbox, raw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalEmailsApi#v2ExternalEmailsJsonPost");
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
| **mailbox** | **String**| Email address of mailbox email was sent to | |
| **raw** | **String**| Base64 encoded MIME email content | |

### Return type

[**ExternalEmail**](ExternalEmail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |

