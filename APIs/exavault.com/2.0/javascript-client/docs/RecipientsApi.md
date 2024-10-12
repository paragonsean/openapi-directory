# ExaVault.RecipientsApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resendInvitationsForShare**](RecipientsApi.md#resendInvitationsForShare) | **POST** /recipients/shares/invites/{shareId} | Resend invitations to share recipients



## resendInvitationsForShare

> ShareRecipientsResponse resendInvitationsForShare(evApiKey, evAccessToken, shareId, opts)

Resend invitations to share recipients

Resend invitations to one or all recipients attached to specified share. The most recent message that was sent for the share will be re-used for this email.  You can use [GET /shares/{id}](#operation/getShareById) to view the recipient list and message history for a share. Use [PATCH /shares/{id}](#operation/updateShareById) to add or remove recipients.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.RecipientsApi();
let evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let shareId = 56; // Number | ID of the share to resend invites for.
let opts = {
  'resendInvitationsRequestBody': {"recipientId":0} // ResendInvitationsRequestBody | 
};
apiInstance.resendInvitationsForShare(evApiKey, evAccessToken, shareId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evApiKey** | **String**| API Key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **shareId** | **Number**| ID of the share to resend invites for. | 
 **resendInvitationsRequestBody** | [**ResendInvitationsRequestBody**](ResendInvitationsRequestBody.md)|  | [optional] 

### Return type

[**ShareRecipientsResponse**](ShareRecipientsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

