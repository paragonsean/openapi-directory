# AttachmentsApi

All URIs are relative to *https://api.bulksms.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rmmPreSignAttachmentPost**](AttachmentsApi.md#rmmPreSignAttachmentPost) | **POST** /rmm/pre-sign-attachment | Upload an attachment via a signed URL |


<a id="rmmPreSignAttachmentPost"></a>
# **rmmPreSignAttachmentPost**
> PreSignInfo rmmPreSignAttachmentPost(preSignRequest)

Upload an attachment via a signed URL

When composing an SMS, you can add SMS attachments by adding a URL to your text. When the recipient clicks on the URL, the attached file will be downloaded and opened on their mobile device.    The best way to do this is to store the file on a web server you own and use that URL in the SMS text. This URL will be easily recognisable to your message recipient and ties your message back to your brand or company.   If that’s not possible, you can use BulkSMS storage to keep the files that you want to attach to your SMS. These files will be deleted after 30 days as per our fair use policy.    We recommend you keep this file size below 20 MB, as larger files may be deleted without warning.   To use the BulkSMS storage, follow these three steps:  **Step 1**: Use your BulkSMS credentials (or your API Token) to request a pre-signed URL.  This is what this &#x60;pre-sign-attachment&#x60; method is for.  It returns a PreSignInfo object that you will use in the other two steps.  **Step 2**: Upload the file using a standard HTTP &#x60;PUT&#x60; request. For your &#x60;PUT&#x60; request, use the value of &#x60;putURL&#x60; from the PreSignInfo object as the request address.  You also have to add the entries from the &#x60;fields&#x60; property (of the PreSignInfo object) to the headers of your &#39;PUT&#39; request. You send the file content as the body of the &#x60;PUT&#x60; request.  **Step 3**: Now you can use the value of &#x60;fetchURL&#x60; from the PreSignInfo object in the body of your SMS messages and send those using the usual messaging API (described elsewhere in this document).  If you send the same file to many recipients, it is safe to use the same URL for all of them.  If you need to, take a closer look at the example program (on the right-hand side) to get a better idea of how to implement this process. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bulksms.com/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AttachmentsApi apiInstance = new AttachmentsApi(defaultClient);
    PreSignRequest preSignRequest = new PreSignRequest(); // PreSignRequest | Describes the file to upload
    try {
      PreSignInfo result = apiInstance.rmmPreSignAttachmentPost(preSignRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachmentsApi#rmmPreSignAttachmentPost");
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
| **preSignRequest** | [**PreSignRequest**](PreSignRequest.md)| Describes the file to upload | |

### Return type

[**PreSignInfo**](PreSignInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A PreSignInfo object |  -  |

