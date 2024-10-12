# TrusthubV1TrustProductsEvaluationsApi

All URIs are relative to *https://trusthub.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTrustProductEvaluation**](TrusthubV1TrustProductsEvaluationsApi.md#createTrustProductEvaluation) | **POST** /v1/TrustProducts/{TrustProductSid}/Evaluations |  |
| [**fetchTrustProductEvaluation**](TrusthubV1TrustProductsEvaluationsApi.md#fetchTrustProductEvaluation) | **GET** /v1/TrustProducts/{TrustProductSid}/Evaluations/{Sid} |  |
| [**listTrustProductEvaluation**](TrusthubV1TrustProductsEvaluationsApi.md#listTrustProductEvaluation) | **GET** /v1/TrustProducts/{TrustProductSid}/Evaluations |  |


<a id="createTrustProductEvaluation"></a>
# **createTrustProductEvaluation**
> TrusthubV1TrustProductTrustProductEvaluation createTrustProductEvaluation(trustProductSid, policySid)



Create a new Evaluation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsEvaluationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsEvaluationsApi apiInstance = new TrusthubV1TrustProductsEvaluationsApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the trust_product resource.
    String policySid = "policySid_example"; // String | The unique string of a policy that is associated to the customer_profile resource.
    try {
      TrusthubV1TrustProductTrustProductEvaluation result = apiInstance.createTrustProductEvaluation(trustProductSid, policySid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsEvaluationsApi#createTrustProductEvaluation");
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
| **trustProductSid** | **String**| The unique string that we created to identify the trust_product resource. | |
| **policySid** | **String**| The unique string of a policy that is associated to the customer_profile resource. | |

### Return type

[**TrusthubV1TrustProductTrustProductEvaluation**](TrusthubV1TrustProductTrustProductEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchTrustProductEvaluation"></a>
# **fetchTrustProductEvaluation**
> TrusthubV1TrustProductTrustProductEvaluation fetchTrustProductEvaluation(trustProductSid, sid)



Fetch specific Evaluation Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsEvaluationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsEvaluationsApi apiInstance = new TrusthubV1TrustProductsEvaluationsApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the trust_product resource.
    String sid = "sid_example"; // String | The unique string that identifies the Evaluation resource.
    try {
      TrusthubV1TrustProductTrustProductEvaluation result = apiInstance.fetchTrustProductEvaluation(trustProductSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsEvaluationsApi#fetchTrustProductEvaluation");
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
| **trustProductSid** | **String**| The unique string that we created to identify the trust_product resource. | |
| **sid** | **String**| The unique string that identifies the Evaluation resource. | |

### Return type

[**TrusthubV1TrustProductTrustProductEvaluation**](TrusthubV1TrustProductTrustProductEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTrustProductEvaluation"></a>
# **listTrustProductEvaluation**
> ListTrustProductEvaluationResponse listTrustProductEvaluation(trustProductSid, pageSize, page, pageToken)



Retrieve a list of Evaluations associated to the trust_product resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrusthubV1TrustProductsEvaluationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trusthub.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrusthubV1TrustProductsEvaluationsApi apiInstance = new TrusthubV1TrustProductsEvaluationsApi(defaultClient);
    String trustProductSid = "trustProductSid_example"; // String | The unique string that we created to identify the trust_product resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTrustProductEvaluationResponse result = apiInstance.listTrustProductEvaluation(trustProductSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrusthubV1TrustProductsEvaluationsApi#listTrustProductEvaluation");
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
| **trustProductSid** | **String**| The unique string that we created to identify the trust_product resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTrustProductEvaluationResponse**](ListTrustProductEvaluationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

