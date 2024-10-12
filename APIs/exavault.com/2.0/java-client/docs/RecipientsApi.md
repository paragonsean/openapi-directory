# RecipientsApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resendInvitationsForShare**](RecipientsApi.md#resendInvitationsForShare) | **POST** /recipients/shares/invites/{shareId} | Resend invitations to share recipients |


<a id="resendInvitationsForShare"></a>
# **resendInvitationsForShare**
> ShareRecipientsResponse resendInvitationsForShare(evApiKey, evAccessToken, shareId, resendInvitationsRequestBody)

Resend invitations to share recipients

Resend invitations to one or all recipients attached to specified share. The most recent message that was sent for the share will be re-used for this email.  You can use [GET /shares/{id}](#operation/getShareById) to view the recipient list and message history for a share. Use [PATCH /shares/{id}](#operation/updateShareById) to add or remove recipients.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecipientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    RecipientsApi apiInstance = new RecipientsApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    Integer shareId = 56; // Integer | ID of the share to resend invites for.
    ResendInvitationsRequestBody resendInvitationsRequestBody = new ResendInvitationsRequestBody(); // ResendInvitationsRequestBody | 
    try {
      ShareRecipientsResponse result = apiInstance.resendInvitationsForShare(evApiKey, evAccessToken, shareId, resendInvitationsRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecipientsApi#resendInvitationsForShare");
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
| **evApiKey** | **String**| API Key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **shareId** | **Integer**| ID of the share to resend invites for. | |
| **resendInvitationsRequestBody** | [**ResendInvitationsRequestBody**](ResendInvitationsRequestBody.md)|  | [optional] |

### Return type

[**ShareRecipientsResponse**](ShareRecipientsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

