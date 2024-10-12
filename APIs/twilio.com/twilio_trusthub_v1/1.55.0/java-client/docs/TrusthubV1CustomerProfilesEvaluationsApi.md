# TrusthubV1CustomerProfilesEvaluationsApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomerProfileEvaluation**](TrusthubV1CustomerProfilesEvaluationsApi.md#createCustomerProfileEvaluation) | **POST** /v1/CustomerProfiles/{CustomerProfileSid}/Evaluations |  |
| [**fetchCustomerProfileEvaluation**](TrusthubV1CustomerProfilesEvaluationsApi.md#fetchCustomerProfileEvaluation) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/Evaluations/{Sid} |  |
| [**listCustomerProfileEvaluation**](TrusthubV1CustomerProfilesEvaluationsApi.md#listCustomerProfileEvaluation) | **GET** /v1/CustomerProfiles/{CustomerProfileSid}/Evaluations |  |


<a id="createCustomerProfileEvaluation"></a>
# **createCustomerProfileEvaluation**
> TrusthubV1CustomerProfileCustomerProfileEvaluation createCustomerProfileEvaluation(customerProfileSid, policySid)



Create a new Evaluation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesEvaluationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesEvaluationsApi apiInstance = new TrusthubV1CustomerProfilesEvaluationsApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    String policySid = "policySid_example"; // String | The unique string of a policy that is associated to the customer_profile resource.
    try {
      TrusthubV1CustomerProfileCustomerProfileEvaluation result = apiInstance.createCustomerProfileEvaluation(customerProfileSid, policySid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesEvaluationsApi#createCustomerProfileEvaluation");
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
| **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | |
| **policySid** | **String**| The unique string of a policy that is associated to the customer_profile resource. | |

### Return type

[**TrusthubV1CustomerProfileCustomerProfileEvaluation**](TrusthubV1CustomerProfileCustomerProfileEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchCustomerProfileEvaluation"></a>
# **fetchCustomerProfileEvaluation**
> TrusthubV1CustomerProfileCustomerProfileEvaluation fetchCustomerProfileEvaluation(customerProfileSid, sid)



Fetch specific Evaluation Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesEvaluationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesEvaluationsApi apiInstance = new TrusthubV1CustomerProfilesEvaluationsApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the customer_profile resource.
    String sid = "sid_example"; // String | The unique string that identifies the Evaluation resource.
    try {
      TrusthubV1CustomerProfileCustomerProfileEvaluation result = apiInstance.fetchCustomerProfileEvaluation(customerProfileSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesEvaluationsApi#fetchCustomerProfileEvaluation");
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
| **customerProfileSid** | **String**| The unique string that we created to identify the customer_profile resource. | |
| **sid** | **String**| The unique string that identifies the Evaluation resource. | |

### Return type

[**TrusthubV1CustomerProfileCustomerProfileEvaluation**](TrusthubV1CustomerProfileCustomerProfileEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listCustomerProfileEvaluation"></a>
# **listCustomerProfileEvaluation**
> ListCustomerProfileEvaluationResponse listCustomerProfileEvaluation(customerProfileSid, pageSize, page, pageToken)



Retrieve a list of Evaluations associated to the customer_profile resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1CustomerProfilesEvaluationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1CustomerProfilesEvaluationsApi apiInstance = new TrusthubV1CustomerProfilesEvaluationsApi(defaultClient);
    String customerProfileSid = "customerProfileSid_example"; // String | The unique string that we created to identify the CustomerProfile resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCustomerProfileEvaluationResponse result = apiInstance.listCustomerProfileEvaluation(customerProfileSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1CustomerProfilesEvaluationsApi#listCustomerProfileEvaluation");
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
| **customerProfileSid** | **String**| The unique string that we created to identify the CustomerProfile resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListCustomerProfileEvaluationResponse**](ListCustomerProfileEvaluationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

