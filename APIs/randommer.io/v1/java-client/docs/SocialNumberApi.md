# SocialNumberApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiSocialNumberGet**](SocialNumberApi.md#apiSocialNumberGet) | **GET** /api/SocialNumber | Generate a social security number |
| [**apiSocialNumberPost**](SocialNumberApi.md#apiSocialNumberPost) | **POST** /api/SocialNumber | Validate VAT/identity numbers |


<a id="apiSocialNumberGet"></a>
# **apiSocialNumberGet**
> apiSocialNumberGet(xApiKey)

Generate a social security number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SocialNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SocialNumberApi apiInstance = new SocialNumberApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiSocialNumberGet(xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SocialNumberApi#apiSocialNumberGet");
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
| **xApiKey** | **String**| Enter your key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiSocialNumberPost"></a>
# **apiSocialNumberPost**
> apiSocialNumberPost(idType, numberValidation, xApiKey)

Validate VAT/identity numbers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SocialNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SocialNumberApi apiInstance = new SocialNumberApi(defaultClient);
    IdType idType = IdType.fromValue("VAT"); // IdType | 
    NumberValidation numberValidation = new NumberValidation(); // NumberValidation | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiSocialNumberPost(idType, numberValidation, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SocialNumberApi#apiSocialNumberPost");
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
| **idType** | [**IdType**](.md)|  | [enum: VAT, SSN] |
| **numberValidation** | [**NumberValidation**](NumberValidation.md)|  | |
| **xApiKey** | **String**| Enter your key | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

