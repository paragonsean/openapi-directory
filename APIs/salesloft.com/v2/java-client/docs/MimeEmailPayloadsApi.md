# MimeEmailPayloadsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2MimeEmailPayloadsIdJsonGet**](MimeEmailPayloadsApi.md#v2MimeEmailPayloadsIdJsonGet) | **GET** /v2/mime_email_payloads/{id}.json | Fetch the MIME content for email |


<a id="v2MimeEmailPayloadsIdJsonGet"></a>
# **v2MimeEmailPayloadsIdJsonGet**
> MimeEmailPayload v2MimeEmailPayloadsIdJsonGet(id)

Fetch the MIME content for email

Fetch the MIME content for email. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MimeEmailPayloadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    MimeEmailPayloadsApi apiInstance = new MimeEmailPayloadsApi(defaultClient);
    String id = "id_example"; // String | ID of Email
    try {
      MimeEmailPayload result = apiInstance.v2MimeEmailPayloadsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MimeEmailPayloadsApi#v2MimeEmailPayloadsIdJsonGet");
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
| **id** | **String**| ID of Email | |

### Return type

[**MimeEmailPayload**](MimeEmailPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

