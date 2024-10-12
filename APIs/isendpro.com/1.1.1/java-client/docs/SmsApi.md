# SmsApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendSms**](SmsApi.md#sendSms) | **POST** /sms | Envoyer un sms |
| [**sendSmsMulti**](SmsApi.md#sendSmsMulti) | **POST** /smsmulti | Envoyer des SMS |


<a id="sendSms"></a>
# **sendSms**
> SMSReponse sendSms(smsUniqueRequest)

Envoyer un sms

Envoi un sms vers un unique destinataire

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    SmsApi apiInstance = new SmsApi(defaultClient);
    SmsUniqueRequest smsUniqueRequest = new SmsUniqueRequest(); // SmsUniqueRequest | sms request
    try {
      SMSReponse result = apiInstance.sendSms(smsUniqueRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#sendSms");
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
| **smsUniqueRequest** | [**SmsUniqueRequest**](SmsUniqueRequest.md)| sms request | |

### Return type

[**SMSReponse**](SMSReponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, etat

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reponse OK |  -  |
| **400** | Dysfonctionnement |  -  |

<a id="sendSmsMulti"></a>
# **sendSmsMulti**
> SMSReponse sendSmsMulti(smSRequest)

Envoyer des SMS

Envoi de SMS vers 1 ou plusieurs destinataires 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    SmsApi apiInstance = new SmsApi(defaultClient);
    SMSRequest smSRequest = new SMSRequest(); // SMSRequest | sms request
    try {
      SMSReponse result = apiInstance.sendSmsMulti(smSRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmsApi#sendSmsMulti");
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
| **smSRequest** | [**SMSRequest**](SMSRequest.md)| sms request | |

### Return type

[**SMSReponse**](SMSReponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, etat

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reponse OK |  -  |
| **400** | Dysfonctionnement |  -  |

