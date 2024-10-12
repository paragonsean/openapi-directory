# NumbersV2SupportingDocumentTypeApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchSupportingDocumentType**](NumbersV2SupportingDocumentTypeApi.md#fetchSupportingDocumentType) | **GET** /v2/RegulatoryCompliance/SupportingDocumentTypes/{Sid} |  |
| [**listSupportingDocumentType**](NumbersV2SupportingDocumentTypeApi.md#listSupportingDocumentType) | **GET** /v2/RegulatoryCompliance/SupportingDocumentTypes |  |


<a id="fetchSupportingDocumentType"></a>
# **fetchSupportingDocumentType**
> NumbersV2RegulatoryComplianceSupportingDocumentType fetchSupportingDocumentType(sid)



Fetch a specific Supporting Document Type Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2SupportingDocumentTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2SupportingDocumentTypeApi apiInstance = new NumbersV2SupportingDocumentTypeApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that identifies the Supporting Document Type resource.
    try {
      NumbersV2RegulatoryComplianceSupportingDocumentType result = apiInstance.fetchSupportingDocumentType(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2SupportingDocumentTypeApi#fetchSupportingDocumentType");
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
| **sid** | **String**| The unique string that identifies the Supporting Document Type resource. | |

### Return type

[**NumbersV2RegulatoryComplianceSupportingDocumentType**](NumbersV2RegulatoryComplianceSupportingDocumentType.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSupportingDocumentType"></a>
# **listSupportingDocumentType**
> ListSupportingDocumentTypeResponse listSupportingDocumentType(pageSize, page, pageToken)



Retrieve a list of all Supporting Document Types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2SupportingDocumentTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2SupportingDocumentTypeApi apiInstance = new NumbersV2SupportingDocumentTypeApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSupportingDocumentTypeResponse result = apiInstance.listSupportingDocumentType(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2SupportingDocumentTypeApi#listSupportingDocumentType");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSupportingDocumentTypeResponse**](ListSupportingDocumentTypeResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

