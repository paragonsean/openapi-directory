# NumbersV2EvaluationApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEvaluation**](NumbersV2EvaluationApi.md#createEvaluation) | **POST** /v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations |  |
| [**fetchEvaluation**](NumbersV2EvaluationApi.md#fetchEvaluation) | **GET** /v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations/{Sid} |  |
| [**listEvaluation**](NumbersV2EvaluationApi.md#listEvaluation) | **GET** /v2/RegulatoryCompliance/Bundles/{BundleSid}/Evaluations |  |


<a id="createEvaluation"></a>
# **createEvaluation**
> NumbersV2RegulatoryComplianceBundleEvaluation createEvaluation(bundleSid)



Creates an evaluation for a bundle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2EvaluationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2EvaluationApi apiInstance = new NumbersV2EvaluationApi(defaultClient);
    String bundleSid = "bundleSid_example"; // String | The unique string that identifies the Bundle resource.
    try {
      NumbersV2RegulatoryComplianceBundleEvaluation result = apiInstance.createEvaluation(bundleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2EvaluationApi#createEvaluation");
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
| **bundleSid** | **String**| The unique string that identifies the Bundle resource. | |

### Return type

[**NumbersV2RegulatoryComplianceBundleEvaluation**](NumbersV2RegulatoryComplianceBundleEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchEvaluation"></a>
# **fetchEvaluation**
> NumbersV2RegulatoryComplianceBundleEvaluation fetchEvaluation(bundleSid, sid)



Fetch specific Evaluation Instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2EvaluationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2EvaluationApi apiInstance = new NumbersV2EvaluationApi(defaultClient);
    String bundleSid = "bundleSid_example"; // String | The unique string that we created to identify the Bundle resource.
    String sid = "sid_example"; // String | The unique string that identifies the Evaluation resource.
    try {
      NumbersV2RegulatoryComplianceBundleEvaluation result = apiInstance.fetchEvaluation(bundleSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2EvaluationApi#fetchEvaluation");
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
| **bundleSid** | **String**| The unique string that we created to identify the Bundle resource. | |
| **sid** | **String**| The unique string that identifies the Evaluation resource. | |

### Return type

[**NumbersV2RegulatoryComplianceBundleEvaluation**](NumbersV2RegulatoryComplianceBundleEvaluation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listEvaluation"></a>
# **listEvaluation**
> ListEvaluationResponse listEvaluation(bundleSid, pageSize, page, pageToken)



Retrieve a list of Evaluations associated to the Bundle resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV2EvaluationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV2EvaluationApi apiInstance = new NumbersV2EvaluationApi(defaultClient);
    String bundleSid = "bundleSid_example"; // String | The unique string that identifies the Bundle resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListEvaluationResponse result = apiInstance.listEvaluation(bundleSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV2EvaluationApi#listEvaluation");
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
| **bundleSid** | **String**| The unique string that identifies the Bundle resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListEvaluationResponse**](ListEvaluationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

