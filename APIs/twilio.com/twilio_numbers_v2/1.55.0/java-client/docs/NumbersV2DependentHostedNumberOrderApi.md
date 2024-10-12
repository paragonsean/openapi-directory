# NumbersV2DependentHostedNumberOrderApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listDependentHostedNumberOrder**](NumbersV2DependentHostedNumberOrderApi.md#listDependentHostedNumberOrder) | **GET** /v2/HostedNumber/AuthorizationDocuments/{SigningDocumentSid}/DependentHostedNumberOrders |  |


<a id="listDependentHostedNumberOrder"></a>
# **listDependentHostedNumberOrder**
> ListDependentHostedNumberOrderResponse listDependentHostedNumberOrder(signingDocumentSid, status, phoneNumber, incomingPhoneNumberSid, friendlyName, pageSize, page, pageToken)



Retrieve a list of dependent HostedNumberOrders belonging to the AuthorizationDocument.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2DependentHostedNumberOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2DependentHostedNumberOrderApi apiInstance = new NumbersV2DependentHostedNumberOrderApi(defaultClient);
    String signingDocumentSid = "signingDocumentSid_example"; // String | A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder.
    DependentHostedNumberOrderEnumStatus status = DependentHostedNumberOrderEnumStatus.fromValue("received"); // DependentHostedNumberOrderEnumStatus | Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
    String phoneNumber = "phoneNumber_example"; // String | An E164 formatted phone number hosted by this HostedNumberOrder.
    String incomingPhoneNumberSid = "incomingPhoneNumberSid_example"; // String | A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
    String friendlyName = "friendlyName_example"; // String | A human readable description of this resource, up to 128 characters.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDependentHostedNumberOrderResponse result = apiInstance.listDependentHostedNumberOrder(signingDocumentSid, status, phoneNumber, incomingPhoneNumberSid, friendlyName, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2DependentHostedNumberOrderApi#listDependentHostedNumberOrder");
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
| **signingDocumentSid** | **String**| A 34 character string that uniquely identifies the LOA document associated with this HostedNumberOrder. | |
| **status** | **DependentHostedNumberOrderEnumStatus**| Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses. | [optional] [enum: received, verified, pending-loa, carrier-processing, completed, failed, action-required] |
| **phoneNumber** | **String**| An E164 formatted phone number hosted by this HostedNumberOrder. | [optional] |
| **incomingPhoneNumberSid** | **String**| A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder. | [optional] |
| **friendlyName** | **String**| A human readable description of this resource, up to 128 characters. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDependentHostedNumberOrderResponse**](ListDependentHostedNumberOrderResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

