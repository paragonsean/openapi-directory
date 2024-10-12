# LanguagePredictionApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**intentMultipart**](LanguagePredictionApi.md#intentMultipart) | **POST** /v2/language/intent | Prediction for Intent |
| [**sentimentMultipart**](LanguagePredictionApi.md#sentimentMultipart) | **POST** /v2/language/sentiment | Prediction for Sentiment |


<a id="intentMultipart"></a>
# **intentMultipart**
> IntentPredictResponse intentMultipart(intentPredictRequest)

Prediction for Intent

Returns an intent prediction for the given string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguagePredictionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguagePredictionApi apiInstance = new LanguagePredictionApi(defaultClient);
    IntentPredictRequest intentPredictRequest = new IntentPredictRequest(); // IntentPredictRequest | 
    try {
      IntentPredictResponse result = apiInstance.intentMultipart(intentPredictRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguagePredictionApi#intentMultipart");
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
| **intentPredictRequest** | [**IntentPredictRequest**](IntentPredictRequest.md)|  | [optional] |

### Return type

[**IntentPredictResponse**](IntentPredictResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prediction Result |  -  |
| **429** | Exceed usage limitation |  -  |

<a id="sentimentMultipart"></a>
# **sentimentMultipart**
> SentimentPredictResponse sentimentMultipart(sentimentPredictRequest)

Prediction for Sentiment

Returns a sentiment prediction for the given string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguagePredictionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguagePredictionApi apiInstance = new LanguagePredictionApi(defaultClient);
    SentimentPredictRequest sentimentPredictRequest = new SentimentPredictRequest(); // SentimentPredictRequest | 
    try {
      SentimentPredictResponse result = apiInstance.sentimentMultipart(sentimentPredictRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguagePredictionApi#sentimentMultipart");
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
| **sentimentPredictRequest** | [**SentimentPredictRequest**](SentimentPredictRequest.md)|  | [optional] |

### Return type

[**SentimentPredictResponse**](SentimentPredictResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prediction Result |  -  |

