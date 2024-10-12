# VerifyV2FormApi

All URIs are relative to *https://verify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchForm**](VerifyV2FormApi.md#fetchForm) | **GET** /v2/Forms/{FormType} |  |


<a id="fetchForm"></a>
# **fetchForm**
> VerifyV2Form fetchForm(formType)



Fetch the forms for a specific Form Type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2FormApi apiInstance = new VerifyV2FormApi(defaultClient);
    FormEnumFormTypes formType = FormEnumFormTypes.fromValue("form-push"); // FormEnumFormTypes | The Type of this Form. Currently only `form-push` is supported.
    try {
      VerifyV2Form result = apiInstance.fetchForm(formType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2FormApi#fetchForm");
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
| **formType** | **FormEnumFormTypes**| The Type of this Form. Currently only &#x60;form-push&#x60; is supported. | [enum: form-push] |

### Return type

[**VerifyV2Form**](VerifyV2Form.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

