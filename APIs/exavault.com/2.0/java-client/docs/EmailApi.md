# EmailApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendReferralEmail**](EmailApi.md#sendReferralEmail) | **POST** /email/referral | Send referral email to a given address |
| [**sendWelcomeEmail**](EmailApi.md#sendWelcomeEmail) | **POST** /email/welcome/{username} | Resend welcome email to specific user |


<a id="sendReferralEmail"></a>
# **sendReferralEmail**
> EmptyResponse sendReferralEmail(evApiKey, evAccessToken, sendReferralEmailRequestBody)

Send referral email to a given address

Invite a friend to sign up for a free trial of ExaVault. Send a [referral](/lp/referafriend/) email to an email address. If the recipient signs up for ExaVault, we&#39;ll apply a credit to your account for the referral. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    EmailApi apiInstance = new EmailApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    SendReferralEmailRequestBody sendReferralEmailRequestBody = new SendReferralEmailRequestBody(); // SendReferralEmailRequestBody | 
    try {
      EmptyResponse result = apiInstance.sendReferralEmail(evApiKey, evAccessToken, sendReferralEmailRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#sendReferralEmail");
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
| **sendReferralEmailRequestBody** | [**SendReferralEmailRequestBody**](SendReferralEmailRequestBody.md)|  | [optional] |

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Operation |  -  |

<a id="sendWelcomeEmail"></a>
# **sendWelcomeEmail**
> EmptyResponse sendWelcomeEmail(evApiKey, evAccessToken, username)

Resend welcome email to specific user

Send a welcome email to a user. The contents of the welcome email can be set by [PATCH /accounts](#operation/updateAccount).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    EmailApi apiInstance = new EmailApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String username = "exampleuser"; // String | A username to send the welcome email to.
    try {
      EmptyResponse result = apiInstance.sendWelcomeEmail(evApiKey, evAccessToken, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailApi#sendWelcomeEmail");
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
| **username** | **String**| A username to send the welcome email to. | |

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

