# QrCodeApi

All URIs are relative to *https://api.fungenerators.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**qrcodeBusinessCardGet**](QrCodeApi.md#qrcodeBusinessCardGet) | **GET** /qrcode/business_card |  |
| [**qrcodeDecodePost**](QrCodeApi.md#qrcodeDecodePost) | **POST** /qrcode/decode |  |
| [**qrcodeEmailGet**](QrCodeApi.md#qrcodeEmailGet) | **GET** /qrcode/email |  |
| [**qrcodePhoneGet**](QrCodeApi.md#qrcodePhoneGet) | **GET** /qrcode/phone |  |
| [**qrcodeRawGet**](QrCodeApi.md#qrcodeRawGet) | **GET** /qrcode/raw |  |
| [**qrcodeSkypeGet**](QrCodeApi.md#qrcodeSkypeGet) | **GET** /qrcode/skype |  |
| [**qrcodeSmsGet**](QrCodeApi.md#qrcodeSmsGet) | **GET** /qrcode/sms |  |
| [**qrcodeTextGet**](QrCodeApi.md#qrcodeTextGet) | **GET** /qrcode/text |  |
| [**qrcodeUrlGet**](QrCodeApi.md#qrcodeUrlGet) | **GET** /qrcode/url |  |


<a id="qrcodeBusinessCardGet"></a>
# **qrcodeBusinessCardGet**
> qrcodeBusinessCardGet(firstname, lastname, email, middlename, company, phoneWork, phoneHome, phoneCell, street1, street2, city, zip, state, country, format)



Get a QR Code image for a business card aka VCARD

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    QrCodeApi apiInstance = new QrCodeApi(defaultClient);
    String firstname = "firstname_example"; // String | First Name
    String lastname = "lastname_example"; // String | Last Name
    String email = "email_example"; // String | Email id
    String middlename = "middlename_example"; // String | Middle Name
    String company = "company_example"; // String | Company Name
    String phoneWork = "phoneWork_example"; // String | Work Phone Number
    String phoneHome = "phoneHome_example"; // String | Home Phone Number
    String phoneCell = "phoneCell_example"; // String | Cell Phone Number
    String street1 = "street1_example"; // String | Street Address
    String street2 = "street2_example"; // String | Street Address 2
    String city = "city_example"; // String | City
    String zip = "zip_example"; // String | Zip Code
    String state = "state_example"; // String | State
    String country = "country_example"; // String | Country
    String format = "format_example"; // String | Output image format. Must be one of png/eps/raw/svg
    try {
      apiInstance.qrcodeBusinessCardGet(firstname, lastname, email, middlename, company, phoneWork, phoneHome, phoneCell, street1, street2, city, zip, state, country, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling QrCodeApi#qrcodeBusinessCardGet");
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
| **firstname** | **String**| First Name | |
| **lastname** | **String**| Last Name | |
| **email** | **String**| Email id | |
| **middlename** | **String**| Middle Name | [optional] |
| **company** | **String**| Company Name | [optional] |
| **phoneWork** | **String**| Work Phone Number | [optional] |
| **phoneHome** | **String**| Home Phone Number | [optional] |
| **phoneCell** | **String**| Cell Phone Number | [optional] |
| **street1** | **String**| Street Address | [optional] |
| **street2** | **String**| Street Address 2 | [optional] |
| **city** | **String**| City | [optional] |
| **zip** | **String**| Zip Code | [optional] |
| **state** | **String**| State | [optional] |
| **country** | **String**| Country | [optional] |
| **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="qrcodeDecodePost"></a>
# **qrcodeDecodePost**
> qrcodeDecodePost(qrcodeDecodePostRequest)



Decode a QR Code image and return the cotents if successful

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    QrCodeApi apiInstance = new QrCodeApi(defaultClient);
    QrcodeDecodePostRequest qrcodeDecodePostRequest = new QrcodeDecodePostRequest(); // QrcodeDecodePostRequest | 
    try {
      apiInstance.qrcodeDecodePost(qrcodeDecodePostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling QrCodeApi#qrcodeDecodePost");
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
| **qrcodeDecodePostRequest** | [**QrcodeDecodePostRequest**](QrcodeDecodePostRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: mulitpart/form-data, mulitpart/form-data-endcoded, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="qrcodeEmailGet"></a>
# **qrcodeEmailGet**
> qrcodeEmailGet(email, subject, body, format)



Get a QR Code image for an email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    QrCodeApi apiInstance = new QrCodeApi(defaultClient);
    String email = "email_example"; // String | Email id to send the email to
    String subject = "subject_example"; // String | Subject of the email(optional)
    String body = "body_example"; // String | Body of the email(optional)
    String format = "format_example"; // String | Output image format. Must be one of png/png/eps/raw/svg
    try {
      apiInstance.qrcodeEmailGet(email, subject, body, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling QrCodeApi#qrcodeEmailGet");
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
| **email** | **String**| Email id to send the email to | |
| **subject** | **String**| Subject of the email(optional) | [optional] |
| **body** | **String**| Body of the email(optional) | [optional] |
| **format** | **String**| Output image format. Must be one of png/png/eps/raw/svg | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="qrcodePhoneGet"></a>
# **qrcodePhoneGet**
> qrcodePhoneGet(number, format)



Get a QR Code image for a phone number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    QrCodeApi apiInstance = new QrCodeApi(defaultClient);
    String number = "number_example"; // String | Phone Number
    String format = "format_example"; // String | Output image format. Must be one of png/eps/raw/svg
    try {
      apiInstance.qrcodePhoneGet(number, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling QrCodeApi#qrcodePhoneGet");
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
| **number** | **String**| Phone Number | |
| **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="qrcodeRawGet"></a>
# **qrcodeRawGet**
> qrcodeRawGet(rawtext, format)



Get a QR Code image for a block of raw data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    QrCodeApi apiInstance = new QrCodeApi(defaultClient);
    String rawtext = "rawtext_example"; // String | Raw Text value
    String format = "format_example"; // String | Output image format. Must be one of png/eps/raw/svg
    try {
      apiInstance.qrcodeRawGet(rawtext, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling QrCodeApi#qrcodeRawGet");
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
| **rawtext** | **String**| Raw Text value | |
| **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="qrcodeSkypeGet"></a>
# **qrcodeSkypeGet**
> qrcodeSkypeGet(username, format)



Get a QR Code image for a skype user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    QrCodeApi apiInstance = new QrCodeApi(defaultClient);
    String username = "username_example"; // String | Skype User name
    String format = "format_example"; // String | Output image format. Must be one of png/eps/raw/svg
    try {
      apiInstance.qrcodeSkypeGet(username, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling QrCodeApi#qrcodeSkypeGet");
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
| **username** | **String**| Skype User name | |
| **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="qrcodeSmsGet"></a>
# **qrcodeSmsGet**
> qrcodeSmsGet(number, format)



Get a QR Code image for a Phone number for SMS messaging

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    QrCodeApi apiInstance = new QrCodeApi(defaultClient);
    String number = "number_example"; // String | Phone Number to SMS
    String format = "format_example"; // String | Output image format. Must be one of png/eps/raw/svg
    try {
      apiInstance.qrcodeSmsGet(number, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling QrCodeApi#qrcodeSmsGet");
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
| **number** | **String**| Phone Number to SMS | |
| **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="qrcodeTextGet"></a>
# **qrcodeTextGet**
> qrcodeTextGet(text, format)



Get a QR Code image for a block of text

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    QrCodeApi apiInstance = new QrCodeApi(defaultClient);
    String text = "text_example"; // String | Text value
    String format = "format_example"; // String | Output image format. Must be one of png/eps/raw/svg
    try {
      apiInstance.qrcodeTextGet(text, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling QrCodeApi#qrcodeTextGet");
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
| **text** | **String**| Text value | |
| **format** | **String**| Output image format. Must be one of png/eps/raw/svg | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

<a id="qrcodeUrlGet"></a>
# **qrcodeUrlGet**
> qrcodeUrlGet(url, format)



Get a QR Code image for a url

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fungenerators.com");
    
    // Configure API key authorization: X-Fungenerators-Api-Secret
    ApiKeyAuth X-Fungenerators-Api-Secret = (ApiKeyAuth) defaultClient.getAuthentication("X-Fungenerators-Api-Secret");
    X-Fungenerators-Api-Secret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Fungenerators-Api-Secret.setApiKeyPrefix("Token");

    QrCodeApi apiInstance = new QrCodeApi(defaultClient);
    String url = "url_example"; // String | URL value
    String format = "format_example"; // String | Output image format. Must be one of png/raw/eps/svg
    try {
      apiInstance.qrcodeUrlGet(url, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling QrCodeApi#qrcodeUrlGet");
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
| **url** | **String**| URL value | |
| **format** | **String**| Output image format. Must be one of png/raw/eps/svg | [optional] |

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200  response |  -  |
| **401** | 401  response |  -  |

