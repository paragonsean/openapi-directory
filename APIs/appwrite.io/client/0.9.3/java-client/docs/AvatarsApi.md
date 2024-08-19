# AvatarsApi

All URIs are relative to *https://appwrite.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**avatarsGetBrowser**](AvatarsApi.md#avatarsGetBrowser) | **GET** /avatars/browsers/{code} | Get Browser Icon |
| [**avatarsGetCreditCard**](AvatarsApi.md#avatarsGetCreditCard) | **GET** /avatars/credit-cards/{code} | Get Credit Card Icon |
| [**avatarsGetFavicon**](AvatarsApi.md#avatarsGetFavicon) | **GET** /avatars/favicon | Get Favicon |
| [**avatarsGetFlag**](AvatarsApi.md#avatarsGetFlag) | **GET** /avatars/flags/{code} | Get Country Flag |
| [**avatarsGetImage**](AvatarsApi.md#avatarsGetImage) | **GET** /avatars/image | Get Image from URL |
| [**avatarsGetInitials**](AvatarsApi.md#avatarsGetInitials) | **GET** /avatars/initials | Get User Initials |
| [**avatarsGetQR**](AvatarsApi.md#avatarsGetQR) | **GET** /avatars/qr | Get QR Code |


<a id="avatarsGetBrowser"></a>
# **avatarsGetBrowser**
> avatarsGetBrowser(code, width, height, quality)

Get Browser Icon

You can use this endpoint to show different browser icons to your users. The code argument receives the browser code as it appears in your user /account/sessions endpoint. Use width, height and quality arguments to change the output settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvatarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AvatarsApi apiInstance = new AvatarsApi(defaultClient);
    String code = "code_example"; // String | Browser Code.
    Integer width = 100; // Integer | Image width. Pass an integer between 0 to 2000. Defaults to 100.
    Integer height = 100; // Integer | Image height. Pass an integer between 0 to 2000. Defaults to 100.
    Integer quality = 100; // Integer | Image quality. Pass an integer between 0 to 100. Defaults to 100.
    try {
      apiInstance.avatarsGetBrowser(code, width, height, quality);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvatarsApi#avatarsGetBrowser");
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
| **code** | **String**| Browser Code. | |
| **width** | **Integer**| Image width. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100] |
| **height** | **Integer**| Image height. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100] |
| **quality** | **Integer**| Image quality. Pass an integer between 0 to 100. Defaults to 100. | [optional] [default to 100] |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image |  -  |

<a id="avatarsGetCreditCard"></a>
# **avatarsGetCreditCard**
> avatarsGetCreditCard(code, width, height, quality)

Get Credit Card Icon

The credit card endpoint will return you the icon of the credit card provider you need. Use width, height and quality arguments to change the output settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvatarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AvatarsApi apiInstance = new AvatarsApi(defaultClient);
    String code = "code_example"; // String | Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro.
    Integer width = 100; // Integer | Image width. Pass an integer between 0 to 2000. Defaults to 100.
    Integer height = 100; // Integer | Image height. Pass an integer between 0 to 2000. Defaults to 100.
    Integer quality = 100; // Integer | Image quality. Pass an integer between 0 to 100. Defaults to 100.
    try {
      apiInstance.avatarsGetCreditCard(code, width, height, quality);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvatarsApi#avatarsGetCreditCard");
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
| **code** | **String**| Credit Card Code. Possible values: amex, argencard, cabal, censosud, diners, discover, elo, hipercard, jcb, mastercard, naranja, targeta-shopping, union-china-pay, visa, mir, maestro. | |
| **width** | **Integer**| Image width. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100] |
| **height** | **Integer**| Image height. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100] |
| **quality** | **Integer**| Image quality. Pass an integer between 0 to 100. Defaults to 100. | [optional] [default to 100] |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image |  -  |

<a id="avatarsGetFavicon"></a>
# **avatarsGetFavicon**
> avatarsGetFavicon(url)

Get Favicon

Use this endpoint to fetch the favorite icon (AKA favicon) of any remote website URL. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvatarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AvatarsApi apiInstance = new AvatarsApi(defaultClient);
    String url = "url_example"; // String | Website URL which you want to fetch the favicon from.
    try {
      apiInstance.avatarsGetFavicon(url);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvatarsApi#avatarsGetFavicon");
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
| **url** | **String**| Website URL which you want to fetch the favicon from. | |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image |  -  |

<a id="avatarsGetFlag"></a>
# **avatarsGetFlag**
> avatarsGetFlag(code, width, height, quality)

Get Country Flag

You can use this endpoint to show different country flags icons to your users. The code argument receives the 2 letter country code. Use width, height and quality arguments to change the output settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvatarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AvatarsApi apiInstance = new AvatarsApi(defaultClient);
    String code = "code_example"; // String | Country Code. ISO Alpha-2 country code format.
    Integer width = 100; // Integer | Image width. Pass an integer between 0 to 2000. Defaults to 100.
    Integer height = 100; // Integer | Image height. Pass an integer between 0 to 2000. Defaults to 100.
    Integer quality = 100; // Integer | Image quality. Pass an integer between 0 to 100. Defaults to 100.
    try {
      apiInstance.avatarsGetFlag(code, width, height, quality);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvatarsApi#avatarsGetFlag");
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
| **code** | **String**| Country Code. ISO Alpha-2 country code format. | |
| **width** | **Integer**| Image width. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100] |
| **height** | **Integer**| Image height. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 100] |
| **quality** | **Integer**| Image quality. Pass an integer between 0 to 100. Defaults to 100. | [optional] [default to 100] |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image |  -  |

<a id="avatarsGetImage"></a>
# **avatarsGetImage**
> avatarsGetImage(url, width, height)

Get Image from URL

Use this endpoint to fetch a remote image URL and crop it to any image size you want. This endpoint is very useful if you need to crop and display remote images in your app or in case you want to make sure a 3rd party image is properly served using a TLS protocol.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvatarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AvatarsApi apiInstance = new AvatarsApi(defaultClient);
    String url = "url_example"; // String | Image URL which you want to crop.
    Integer width = 400; // Integer | Resize preview image width, Pass an integer between 0 to 2000.
    Integer height = 400; // Integer | Resize preview image height, Pass an integer between 0 to 2000.
    try {
      apiInstance.avatarsGetImage(url, width, height);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvatarsApi#avatarsGetImage");
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
| **url** | **String**| Image URL which you want to crop. | |
| **width** | **Integer**| Resize preview image width, Pass an integer between 0 to 2000. | [optional] [default to 400] |
| **height** | **Integer**| Resize preview image height, Pass an integer between 0 to 2000. | [optional] [default to 400] |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image |  -  |

<a id="avatarsGetInitials"></a>
# **avatarsGetInitials**
> avatarsGetInitials(name, width, height, color, background)

Get User Initials

Use this endpoint to show your user initials avatar icon on your website or app. By default, this route will try to print your logged-in user name or email initials. You can also overwrite the user name if you pass the &#39;name&#39; parameter. If no name is given and no user is logged, an empty avatar will be returned.  You can use the color and background params to change the avatar colors. By default, a random theme will be selected. The random theme will persist for the user&#39;s initials when reloading the same theme will always return for the same initials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvatarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AvatarsApi apiInstance = new AvatarsApi(defaultClient);
    String name = ""; // String | Full Name. When empty, current user name or email will be used. Max length: 128 chars.
    Integer width = 500; // Integer | Image width. Pass an integer between 0 to 2000. Defaults to 100.
    Integer height = 500; // Integer | Image height. Pass an integer between 0 to 2000. Defaults to 100.
    String color = ""; // String | Changes text color. By default a random color will be picked and stay will persistent to the given name.
    String background = ""; // String | Changes background color. By default a random color will be picked and stay will persistent to the given name.
    try {
      apiInstance.avatarsGetInitials(name, width, height, color, background);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvatarsApi#avatarsGetInitials");
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
| **name** | **String**| Full Name. When empty, current user name or email will be used. Max length: 128 chars. | [optional] [default to ] |
| **width** | **Integer**| Image width. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 500] |
| **height** | **Integer**| Image height. Pass an integer between 0 to 2000. Defaults to 100. | [optional] [default to 500] |
| **color** | **String**| Changes text color. By default a random color will be picked and stay will persistent to the given name. | [optional] [default to ] |
| **background** | **String**| Changes background color. By default a random color will be picked and stay will persistent to the given name. | [optional] [default to ] |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image |  -  |

<a id="avatarsGetQR"></a>
# **avatarsGetQR**
> avatarsGetQR(text, size, margin, download)

Get QR Code

Converts a given plain text to a QR code image. You can use the query parameters to change the size and style of the resulting image.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvatarsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://appwrite.io/v1");
    
    // Configure API key authorization: Project
    ApiKeyAuth Project = (ApiKeyAuth) defaultClient.getAuthentication("Project");
    Project.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Project.setApiKeyPrefix("Token");

    // Configure API key authorization: JWT
    ApiKeyAuth JWT = (ApiKeyAuth) defaultClient.getAuthentication("JWT");
    JWT.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //JWT.setApiKeyPrefix("Token");

    AvatarsApi apiInstance = new AvatarsApi(defaultClient);
    String text = "text_example"; // String | Plain text to be converted to QR code image.
    Integer size = 400; // Integer | QR code size. Pass an integer between 0 to 1000. Defaults to 400.
    Integer margin = 1; // Integer | Margin from edge. Pass an integer between 0 to 10. Defaults to 1.
    Boolean download = false; // Boolean | Return resulting image with 'Content-Disposition: attachment ' headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0.
    try {
      apiInstance.avatarsGetQR(text, size, margin, download);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvatarsApi#avatarsGetQR");
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
| **text** | **String**| Plain text to be converted to QR code image. | |
| **size** | **Integer**| QR code size. Pass an integer between 0 to 1000. Defaults to 400. | [optional] [default to 400] |
| **margin** | **Integer**| Margin from edge. Pass an integer between 0 to 10. Defaults to 1. | [optional] [default to 1] |
| **download** | **Boolean**| Return resulting image with &#39;Content-Disposition: attachment &#39; headers for the browser to start downloading it. Pass 0 for no header, or 1 for otherwise. Default value is set to 0. | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Image |  -  |

