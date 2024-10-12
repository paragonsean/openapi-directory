# CustomizerApi

All URIs are relative to *https://api.handwrytten.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomCard**](CustomizerApi.md#createCustomCard) | **POST** /cards/createCustomCard | Create a new custom card |
| [**fontsListForCustomizer**](CustomizerApi.md#fontsListForCustomizer) | **GET** /fonts/listForCustomizer | Lists fonts available for use with the card customizer |
| [**uploadCustomLogo**](CustomizerApi.md#uploadCustomLogo) | **POST** /cards/uploadCustomLogo | upload logo or cover image for card |


<a id="createCustomCard"></a>
# **createCustomCard**
> List&lt;Card&gt; createCustomCard(body)

Create a new custom card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomizerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    CustomizerApi apiInstance = new CustomizerApi(defaultClient);
    CreateCustomCardRequest body = new CreateCustomCardRequest(); // CreateCustomCardRequest | additional parameters
    try {
      List<Card> result = apiInstance.createCustomCard(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomizerApi#createCustomCard");
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
| **body** | [**CreateCustomCardRequest**](CreateCustomCardRequest.md)| additional parameters | |

### Return type

[**List&lt;Card&gt;**](Card.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="fontsListForCustomizer"></a>
# **fontsListForCustomizer**
> List&lt;FontForCustomizer&gt; fontsListForCustomizer()

Lists fonts available for use with the card customizer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomizerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    CustomizerApi apiInstance = new CustomizerApi(defaultClient);
    try {
      List<FontForCustomizer> result = apiInstance.fontsListForCustomizer();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomizerApi#fontsListForCustomizer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;FontForCustomizer&gt;**](FontForCustomizer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="uploadCustomLogo"></a>
# **uploadCustomLogo**
> UploadCustomLogo200Response uploadCustomLogo(_file, type, uid)

upload logo or cover image for card

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomizerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    CustomizerApi apiInstance = new CustomizerApi(defaultClient);
    File _file = new File("/path/to/file"); // File | upload images for customc cards
    String type = "type_example"; // String | set to cover or header
    String uid = "uid_example"; // String | uid of the user
    try {
      UploadCustomLogo200Response result = apiInstance.uploadCustomLogo(_file, type, uid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomizerApi#uploadCustomLogo");
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
| **_file** | **File**| upload images for customc cards | |
| **type** | **String**| set to cover or header | |
| **uid** | **String**| uid of the user | |

### Return type

[**UploadCustomLogo200Response**](UploadCustomLogo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

