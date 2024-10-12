# SingleQrCodeApi

All URIs are relative to *https://run.byvalue.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dispatcherQrcodeContactPost**](SingleQrCodeApi.md#dispatcherQrcodeContactPost) | **POST** /qrcode/contact | Contact QR Code |
| [**dispatcherQrcodeCryptoPost**](SingleQrCodeApi.md#dispatcherQrcodeCryptoPost) | **POST** /qrcode/crypto | Cryptocurrency payment QR Code |
| [**dispatcherQrcodeEmailPost**](SingleQrCodeApi.md#dispatcherQrcodeEmailPost) | **POST** /qrcode/email | Email QR Code |
| [**dispatcherQrcodeGeoPost**](SingleQrCodeApi.md#dispatcherQrcodeGeoPost) | **POST** /qrcode/geo | Geolocation QR Code |
| [**dispatcherQrcodePhonePost**](SingleQrCodeApi.md#dispatcherQrcodePhonePost) | **POST** /qrcode/phone | Telephone QR Code |
| [**dispatcherQrcodePost**](SingleQrCodeApi.md#dispatcherQrcodePost) | **POST** /qrcode | Arbitrary data type QR Code |
| [**dispatcherQrcodeSmsPost**](SingleQrCodeApi.md#dispatcherQrcodeSmsPost) | **POST** /qrcode/sms | SMS QR Code |
| [**dispatcherQrcodeTextPost**](SingleQrCodeApi.md#dispatcherQrcodeTextPost) | **POST** /qrcode/text | Text QR Code |
| [**dispatcherQrcodeWifiPost**](SingleQrCodeApi.md#dispatcherQrcodeWifiPost) | **POST** /qrcode/wifi | WiFi QR Code |


<a id="dispatcherQrcodeContactPost"></a>
# **dispatcherQrcodeContactPost**
> File dispatcherQrcodeContactPost(contactQRCode)

Contact QR Code

This endpoint allows you to create a QR Code that allows user to quickly add contact information to the phone book. The code contains an appropriately encoded electronic business card. After scanning, the device prompts to save the contact in the phone book.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleQrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: Byvalue
    ApiKeyAuth Byvalue = (ApiKeyAuth) defaultClient.getAuthentication("Byvalue");
    Byvalue.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Byvalue.setApiKeyPrefix("Token");

    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    SingleQrCodeApi apiInstance = new SingleQrCodeApi(defaultClient);
    ContactQRCode contactQRCode = new ContactQRCode(); // ContactQRCode | 
    try {
      File result = apiInstance.dispatcherQrcodeContactPost(contactQRCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleQrCodeApi#dispatcherQrcodeContactPost");
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
| **contactQRCode** | [**ContactQRCode**](ContactQRCode.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a QR Code image |  -  |
| **400** | Invalid request |  -  |
| **415** | Request Content-Type not supported or not specified |  -  |
| **422** | Validation Error |  -  |
| **424** | Embedded image download error |  -  |
| **500** | Internal Server Error |  -  |

<a id="dispatcherQrcodeCryptoPost"></a>
# **dispatcherQrcodeCryptoPost**
> File dispatcherQrcodeCryptoPost(cryptoPaymentQRCode)

Cryptocurrency payment QR Code

This endpoint allows you to create a QR Code that allows user to make a quick cryptocurrency transfer. The code contains appropriately encoded data for the payment. After scanning the code, the cryptocurrency wallet application asks user to perform the transfer without rewriting all necessary data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleQrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: Byvalue
    ApiKeyAuth Byvalue = (ApiKeyAuth) defaultClient.getAuthentication("Byvalue");
    Byvalue.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Byvalue.setApiKeyPrefix("Token");

    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    SingleQrCodeApi apiInstance = new SingleQrCodeApi(defaultClient);
    CryptoPaymentQRCode cryptoPaymentQRCode = new CryptoPaymentQRCode(); // CryptoPaymentQRCode | 
    try {
      File result = apiInstance.dispatcherQrcodeCryptoPost(cryptoPaymentQRCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleQrCodeApi#dispatcherQrcodeCryptoPost");
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
| **cryptoPaymentQRCode** | [**CryptoPaymentQRCode**](CryptoPaymentQRCode.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a QR Code image |  -  |
| **400** | Invalid request |  -  |
| **415** | Request Content-Type not supported or not specified |  -  |
| **422** | Validation Error |  -  |
| **424** | Embedded image download error |  -  |
| **500** | Internal Server Error |  -  |

<a id="dispatcherQrcodeEmailPost"></a>
# **dispatcherQrcodeEmailPost**
> File dispatcherQrcodeEmailPost(emailQRCode)

Email QR Code

This endpoint allows the creation of a QR Code allowing the user to quickly send an email. The code contains an appropriately encoded message template. After scanning, the device starts the e-mail client with pre-filled specified fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleQrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: Byvalue
    ApiKeyAuth Byvalue = (ApiKeyAuth) defaultClient.getAuthentication("Byvalue");
    Byvalue.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Byvalue.setApiKeyPrefix("Token");

    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    SingleQrCodeApi apiInstance = new SingleQrCodeApi(defaultClient);
    EmailQRCode emailQRCode = new EmailQRCode(); // EmailQRCode | 
    try {
      File result = apiInstance.dispatcherQrcodeEmailPost(emailQRCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleQrCodeApi#dispatcherQrcodeEmailPost");
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
| **emailQRCode** | [**EmailQRCode**](EmailQRCode.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a QR Code image |  -  |
| **400** | Invalid request |  -  |
| **415** | Request Content-Type not supported or not specified |  -  |
| **422** | Validation Error |  -  |
| **424** | Embedded image download error |  -  |
| **500** | Internal Server Error |  -  |

<a id="dispatcherQrcodeGeoPost"></a>
# **dispatcherQrcodeGeoPost**
> File dispatcherQrcodeGeoPost(geolocationQRCode)

Geolocation QR Code

This endpoint allows you to create a QR Code that allows to share location with the user. The code contains appropriately encoded geographic coordinates. After scanning the code, device maps application is invoked, pointing to the selected location (address).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleQrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: Byvalue
    ApiKeyAuth Byvalue = (ApiKeyAuth) defaultClient.getAuthentication("Byvalue");
    Byvalue.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Byvalue.setApiKeyPrefix("Token");

    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    SingleQrCodeApi apiInstance = new SingleQrCodeApi(defaultClient);
    GeolocationQRCode geolocationQRCode = new GeolocationQRCode(); // GeolocationQRCode | 
    try {
      File result = apiInstance.dispatcherQrcodeGeoPost(geolocationQRCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleQrCodeApi#dispatcherQrcodeGeoPost");
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
| **geolocationQRCode** | [**GeolocationQRCode**](GeolocationQRCode.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a QR Code image |  -  |
| **400** | Invalid request |  -  |
| **415** | Request Content-Type not supported or not specified |  -  |
| **422** | Validation Error |  -  |
| **424** | Embedded image download error |  -  |
| **500** | Internal Server Error |  -  |

<a id="dispatcherQrcodePhonePost"></a>
# **dispatcherQrcodePhonePost**
> File dispatcherQrcodePhonePost(phoneQRCode)

Telephone QR Code

This endpoint allows you to create a QR Code that allows user to make quick telephone call. The code contains appropriately encoded telephone number. After scanning the code, device dialer is invoked with prefilled phone number. To make a call, the user only needs to press the green phone key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleQrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: Byvalue
    ApiKeyAuth Byvalue = (ApiKeyAuth) defaultClient.getAuthentication("Byvalue");
    Byvalue.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Byvalue.setApiKeyPrefix("Token");

    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    SingleQrCodeApi apiInstance = new SingleQrCodeApi(defaultClient);
    PhoneQRCode phoneQRCode = new PhoneQRCode(); // PhoneQRCode | 
    try {
      File result = apiInstance.dispatcherQrcodePhonePost(phoneQRCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleQrCodeApi#dispatcherQrcodePhonePost");
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
| **phoneQRCode** | [**PhoneQRCode**](PhoneQRCode.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a QR Code image |  -  |
| **400** | Invalid request |  -  |
| **415** | Request Content-Type not supported or not specified |  -  |
| **422** | Validation Error |  -  |
| **424** | Embedded image download error |  -  |
| **500** | Internal Server Error |  -  |

<a id="dispatcherQrcodePost"></a>
# **dispatcherQrcodePost**
> File dispatcherQrcodePost(autoQRCode)

Arbitrary data type QR Code

This endpoint aggregates the functionality of all other endpoints in the group. The data type in the &#x60;data&#x60; field is recognized automatically and the data is encoded in an appropriate way.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleQrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: Byvalue
    ApiKeyAuth Byvalue = (ApiKeyAuth) defaultClient.getAuthentication("Byvalue");
    Byvalue.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Byvalue.setApiKeyPrefix("Token");

    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    SingleQrCodeApi apiInstance = new SingleQrCodeApi(defaultClient);
    AutoQRCode autoQRCode = new AutoQRCode(); // AutoQRCode | 
    try {
      File result = apiInstance.dispatcherQrcodePost(autoQRCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleQrCodeApi#dispatcherQrcodePost");
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
| **autoQRCode** | [**AutoQRCode**](AutoQRCode.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a QR Code image |  -  |
| **400** | Invalid request |  -  |
| **415** | Request Content-Type not supported or not specified |  -  |
| **422** | Validation Error |  -  |
| **424** | Embedded image download error |  -  |
| **500** | Internal Server Error |  -  |

<a id="dispatcherQrcodeSmsPost"></a>
# **dispatcherQrcodeSmsPost**
> File dispatcherQrcodeSmsPost(smSQRCode)

SMS QR Code

This endpoint allows you to create a QR Code that allows user to quickly send SMS. The code contains appropriately encoded recipient number and message template. After scanning the code, device message application is invoked with prefilled phone number and text, ready to be sent. To send a SMS, the user only needs to press *Send* button.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleQrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: Byvalue
    ApiKeyAuth Byvalue = (ApiKeyAuth) defaultClient.getAuthentication("Byvalue");
    Byvalue.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Byvalue.setApiKeyPrefix("Token");

    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    SingleQrCodeApi apiInstance = new SingleQrCodeApi(defaultClient);
    SMSQRCode smSQRCode = new SMSQRCode(); // SMSQRCode | 
    try {
      File result = apiInstance.dispatcherQrcodeSmsPost(smSQRCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleQrCodeApi#dispatcherQrcodeSmsPost");
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
| **smSQRCode** | [**SMSQRCode**](SMSQRCode.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a QR Code image |  -  |
| **400** | Invalid request |  -  |
| **415** | Request Content-Type not supported or not specified |  -  |
| **422** | Validation Error |  -  |
| **424** | Embedded image download error |  -  |
| **500** | Internal Server Error |  -  |

<a id="dispatcherQrcodeTextPost"></a>
# **dispatcherQrcodeTextPost**
> File dispatcherQrcodeTextPost(textQRCode)

Text QR Code

This endpoint allows you to create a QR Code containing any text, in particular, an URL that may redirect the user to the website. After QR code is scanned, website will be displayed to the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleQrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: Byvalue
    ApiKeyAuth Byvalue = (ApiKeyAuth) defaultClient.getAuthentication("Byvalue");
    Byvalue.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Byvalue.setApiKeyPrefix("Token");

    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    SingleQrCodeApi apiInstance = new SingleQrCodeApi(defaultClient);
    TextQRCode textQRCode = new TextQRCode(); // TextQRCode | 
    try {
      File result = apiInstance.dispatcherQrcodeTextPost(textQRCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleQrCodeApi#dispatcherQrcodeTextPost");
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
| **textQRCode** | [**TextQRCode**](TextQRCode.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a QR Code image |  -  |
| **400** | Invalid request |  -  |
| **415** | Request Content-Type not supported or not specified |  -  |
| **422** | Validation Error |  -  |
| **424** | Embedded image download error |  -  |
| **500** | Internal Server Error |  -  |

<a id="dispatcherQrcodeWifiPost"></a>
# **dispatcherQrcodeWifiPost**
> File dispatcherQrcodeWifiPost(wiFiQRCode)

WiFi QR Code

This endpoint allows you to create a QR Code that allows user to quickly connect to a WiFi network. The code contains properly encoded network credentials. After scanning, the device can automatically connect to the network without having to enter the password manually.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleQrCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.byvalue.org");
    
    // Configure API key authorization: Byvalue
    ApiKeyAuth Byvalue = (ApiKeyAuth) defaultClient.getAuthentication("Byvalue");
    Byvalue.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Byvalue.setApiKeyPrefix("Token");

    // Configure API key authorization: RapidAPI
    ApiKeyAuth RapidAPI = (ApiKeyAuth) defaultClient.getAuthentication("RapidAPI");
    RapidAPI.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //RapidAPI.setApiKeyPrefix("Token");

    SingleQrCodeApi apiInstance = new SingleQrCodeApi(defaultClient);
    WiFiQRCode wiFiQRCode = new WiFiQRCode(); // WiFiQRCode | 
    try {
      File result = apiInstance.dispatcherQrcodeWifiPost(wiFiQRCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleQrCodeApi#dispatcherQrcodeWifiPost");
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
| **wiFiQRCode** | [**WiFiQRCode**](WiFiQRCode.md)|  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/pdf, application/postscript, image/jpeg, image/png, image/svg+xml, image/webp, application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a QR Code image |  -  |
| **400** | Invalid request |  -  |
| **415** | Request Content-Type not supported or not specified |  -  |
| **422** | Validation Error |  -  |
| **424** | Embedded image download error |  -  |
| **500** | Internal Server Error |  -  |

