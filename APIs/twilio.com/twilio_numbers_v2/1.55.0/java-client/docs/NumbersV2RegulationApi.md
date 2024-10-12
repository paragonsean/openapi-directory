# NumbersV2RegulationApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchRegulation**](NumbersV2RegulationApi.md#fetchRegulation) | **GET** /v2/RegulatoryCompliance/Regulations/{Sid} |  |
| [**listRegulation**](NumbersV2RegulationApi.md#listRegulation) | **GET** /v2/RegulatoryCompliance/Regulations |  |


<a id="fetchRegulation"></a>
# **fetchRegulation**
> NumbersV2RegulatoryComplianceRegulation fetchRegulation(sid)



Fetch specific Regulation Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2RegulationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2RegulationApi apiInstance = new NumbersV2RegulationApi(defaultClient);
    String sid = "sid_example"; // String | The unique string that identifies the Regulation resource.
    try {
      NumbersV2RegulatoryComplianceRegulation result = apiInstance.fetchRegulation(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2RegulationApi#fetchRegulation");
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
| **sid** | **String**| The unique string that identifies the Regulation resource. | |

### Return type

[**NumbersV2RegulatoryComplianceRegulation**](NumbersV2RegulatoryComplianceRegulation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRegulation"></a>
# **listRegulation**
> ListRegulationResponse listRegulation(endUserType, isoCountry, numberType, pageSize, page, pageToken)



Retrieve a list of all Regulations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2RegulationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2RegulationApi apiInstance = new NumbersV2RegulationApi(defaultClient);
    RegulationEnumEndUserType endUserType = RegulationEnumEndUserType.fromValue("individual"); // RegulationEnumEndUserType | The type of End User the regulation requires - can be `individual` or `business`.
    String isoCountry = "isoCountry_example"; // String | The ISO country code of the phone number's country.
    String numberType = "numberType_example"; // String | The type of phone number that the regulatory requiremnt is restricting.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRegulationResponse result = apiInstance.listRegulation(endUserType, isoCountry, numberType, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2RegulationApi#listRegulation");
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
| **endUserType** | **RegulationEnumEndUserType**| The type of End User the regulation requires - can be &#x60;individual&#x60; or &#x60;business&#x60;. | [optional] [enum: individual, business] |
| **isoCountry** | **String**| The ISO country code of the phone number&#39;s country. | [optional] |
| **numberType** | **String**| The type of phone number that the regulatory requiremnt is restricting. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRegulationResponse**](ListRegulationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

