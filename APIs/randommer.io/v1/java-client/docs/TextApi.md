# TextApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiTextHumanizePost**](TextApi.md#apiTextHumanizePost) | **POST** /api/Text/Humanize | Humanize text |
| [**apiTextLoremIpsumGet**](TextApi.md#apiTextLoremIpsumGet) | **GET** /api/Text/LoremIpsum | Generate lorem ipsum |
| [**apiTextPasswordGet**](TextApi.md#apiTextPasswordGet) | **GET** /api/Text/Password | Generate password |
| [**apiTextReviewPost**](TextApi.md#apiTextReviewPost) | **POST** /api/Text/Review | Get reviews (max quantity&#x3D;500) |
| [**apiTextTransformPost**](TextApi.md#apiTextTransformPost) | **POST** /api/Text/Transform | Transform text |


<a id="apiTextHumanizePost"></a>
# **apiTextHumanizePost**
> apiTextHumanizePost(textDto, xApiKey)

Humanize text

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TextApi apiInstance = new TextApi(defaultClient);
    TextDto textDto = new TextDto(); // TextDto | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiTextHumanizePost(textDto, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextApi#apiTextHumanizePost");
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
| **textDto** | [**TextDto**](TextDto.md)|  | |
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

<a id="apiTextLoremIpsumGet"></a>
# **apiTextLoremIpsumGet**
> apiTextLoremIpsumGet(loremType, type, number, xApiKey)

Generate lorem ipsum

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TextApi apiInstance = new TextApi(defaultClient);
    LoremType loremType = LoremType.fromValue("normal"); // LoremType | 
    TextType type = TextType.fromValue("paragraphs"); // TextType | 
    Integer number = 56; // Integer | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiTextLoremIpsumGet(loremType, type, number, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextApi#apiTextLoremIpsumGet");
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
| **loremType** | [**LoremType**](.md)|  | [enum: normal, business] |
| **type** | [**TextType**](.md)|  | [enum: paragraphs, words] |
| **number** | **Integer**|  | |
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

<a id="apiTextPasswordGet"></a>
# **apiTextPasswordGet**
> apiTextPasswordGet(length, hasDigits, hasUppercase, hasSpecial, xApiKey)

Generate password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TextApi apiInstance = new TextApi(defaultClient);
    Integer length = 56; // Integer | 
    Boolean hasDigits = true; // Boolean | 
    Boolean hasUppercase = true; // Boolean | 
    Boolean hasSpecial = true; // Boolean | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiTextPasswordGet(length, hasDigits, hasUppercase, hasSpecial, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextApi#apiTextPasswordGet");
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
| **length** | **Integer**|  | |
| **hasDigits** | **Boolean**|  | |
| **hasUppercase** | **Boolean**|  | |
| **hasSpecial** | **Boolean**|  | |
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

<a id="apiTextReviewPost"></a>
# **apiTextReviewPost**
> apiTextReviewPost(product, quantity, xApiKey)

Get reviews (max quantity&#x3D;500)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TextApi apiInstance = new TextApi(defaultClient);
    String product = "product_example"; // String | 
    Integer quantity = 56; // Integer | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiTextReviewPost(product, quantity, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextApi#apiTextReviewPost");
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
| **product** | **String**|  | |
| **quantity** | **Integer**|  | |
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

<a id="apiTextTransformPost"></a>
# **apiTextTransformPost**
> apiTextTransformPost(textActionType, textDto, caseType, find, replace, xApiKey)

Transform text

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TextApi apiInstance = new TextApi(defaultClient);
    TextActionType textActionType = TextActionType.fromValue("Transform"); // TextActionType | 
    TextDto textDto = new TextDto(); // TextDto | 
    CaseType caseType = CaseType.fromValue("LowerCase"); // CaseType | 
    String find = "find_example"; // String | 
    String replace = "replace_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiTextTransformPost(textActionType, textDto, caseType, find, replace, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling TextApi#apiTextTransformPost");
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
| **textActionType** | [**TextActionType**](.md)|  | [enum: Transform, Replace] |
| **textDto** | [**TextDto**](TextDto.md)|  | |
| **caseType** | [**CaseType**](.md)|  | [optional] [enum: LowerCase, UpperCase, SentenceCase, TitleCase] |
| **find** | **String**|  | [optional] |
| **replace** | **String**|  | [optional] |
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

