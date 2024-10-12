# IntelligenceV2ServiceApi

All URIs are relative to *https://intelligence.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createService**](IntelligenceV2ServiceApi.md#createService) | **POST** /v2/Services |  |
| [**deleteService**](IntelligenceV2ServiceApi.md#deleteService) | **DELETE** /v2/Services/{Sid} |  |
| [**fetchService**](IntelligenceV2ServiceApi.md#fetchService) | **GET** /v2/Services/{Sid} |  |
| [**listService**](IntelligenceV2ServiceApi.md#listService) | **GET** /v2/Services |  |
| [**updateService**](IntelligenceV2ServiceApi.md#updateService) | **POST** /v2/Services/{Sid} |  |


<a id="createService"></a>
# **createService**
> IntelligenceV2Service createService(uniqueName, autoRedaction, autoTranscribe, dataLogging, friendlyName, languageCode, mediaRedaction, webhookHttpMethod, webhookUrl)



Create a new Service for the given Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2ServiceApi apiInstance = new IntelligenceV2ServiceApi(defaultClient);
    String uniqueName = "uniqueName_example"; // String | Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
    Boolean autoRedaction = true; // Boolean | Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
    Boolean autoTranscribe = true; // Boolean | Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
    Boolean dataLogging = true; // Boolean | Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
    String friendlyName = "friendlyName_example"; // String | A human readable description of this resource, up to 64 characters.
    String languageCode = "languageCode_example"; // String | The default language code of the audio.
    Boolean mediaRedaction = true; // Boolean | Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
    ServiceEnumHttpMethod webhookHttpMethod = ServiceEnumHttpMethod.fromValue("GET"); // ServiceEnumHttpMethod | 
    String webhookUrl = "webhookUrl_example"; // String | The URL Twilio will request when executing the Webhook.
    try {
      IntelligenceV2Service result = apiInstance.createService(uniqueName, autoRedaction, autoTranscribe, dataLogging, friendlyName, languageCode, mediaRedaction, webhookHttpMethod, webhookUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2ServiceApi#createService");
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
| **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID. | |
| **autoRedaction** | **Boolean**| Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service. | [optional] |
| **autoTranscribe** | **Boolean**| Instructs the Speech Recognition service to automatically transcribe all recordings made on the account. | [optional] |
| **dataLogging** | **Boolean**| Data logging allows Twilio to improve the quality of the speech recognition &amp; language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent. | [optional] |
| **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] |
| **languageCode** | **String**| The default language code of the audio. | [optional] |
| **mediaRedaction** | **Boolean**| Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise. | [optional] |
| **webhookHttpMethod** | **ServiceEnumHttpMethod**|  | [optional] [enum: GET, POST, NULL] |
| **webhookUrl** | **String**| The URL Twilio will request when executing the Webhook. | [optional] |

### Return type

[**IntelligenceV2Service**](IntelligenceV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteService"></a>
# **deleteService**
> deleteService(sid)



Delete a specific Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2ServiceApi apiInstance = new IntelligenceV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Service.
    try {
      apiInstance.deleteService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2ServiceApi#deleteService");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Service. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchService"></a>
# **fetchService**
> IntelligenceV2Service fetchService(sid)



Fetch a specific Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2ServiceApi apiInstance = new IntelligenceV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Service.
    try {
      IntelligenceV2Service result = apiInstance.fetchService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2ServiceApi#fetchService");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Service. | |

### Return type

[**IntelligenceV2Service**](IntelligenceV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listService"></a>
# **listService**
> ListServiceResponse listService(pageSize, page, pageToken)



Retrieves a list of all Services for an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2ServiceApi apiInstance = new IntelligenceV2ServiceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceResponse result = apiInstance.listService(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2ServiceApi#listService");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateService"></a>
# **updateService**
> IntelligenceV2Service updateService(sid, ifMatch, autoRedaction, autoTranscribe, dataLogging, friendlyName, languageCode, mediaRedaction, uniqueName, webhookHttpMethod, webhookUrl)



Update a specific Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2ServiceApi apiInstance = new IntelligenceV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Service.
    String ifMatch = "ifMatch_example"; // String | The If-Match HTTP request header
    Boolean autoRedaction = true; // Boolean | Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service.
    Boolean autoTranscribe = true; // Boolean | Instructs the Speech Recognition service to automatically transcribe all recordings made on the account.
    Boolean dataLogging = true; // Boolean | Data logging allows Twilio to improve the quality of the speech recognition & language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent.
    String friendlyName = "friendlyName_example"; // String | A human readable description of this resource, up to 64 characters.
    String languageCode = "languageCode_example"; // String | The default language code of the audio.
    Boolean mediaRedaction = true; // Boolean | Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise.
    String uniqueName = "uniqueName_example"; // String | Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID.
    ServiceEnumHttpMethod webhookHttpMethod = ServiceEnumHttpMethod.fromValue("GET"); // ServiceEnumHttpMethod | 
    String webhookUrl = "webhookUrl_example"; // String | The URL Twilio will request when executing the Webhook.
    try {
      IntelligenceV2Service result = apiInstance.updateService(sid, ifMatch, autoRedaction, autoTranscribe, dataLogging, friendlyName, languageCode, mediaRedaction, uniqueName, webhookHttpMethod, webhookUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2ServiceApi#updateService");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Service. | |
| **ifMatch** | **String**| The If-Match HTTP request header | [optional] |
| **autoRedaction** | **Boolean**| Instructs the Speech Recognition service to automatically redact PII from all transcripts made on this service. | [optional] |
| **autoTranscribe** | **Boolean**| Instructs the Speech Recognition service to automatically transcribe all recordings made on the account. | [optional] |
| **dataLogging** | **Boolean**| Data logging allows Twilio to improve the quality of the speech recognition &amp; language understanding services through using customer data to refine, fine tune and evaluate machine learning models. Note: Data logging cannot be activated via API, only via www.twilio.com, as it requires additional consent. | [optional] |
| **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] |
| **languageCode** | **String**| The default language code of the audio. | [optional] |
| **mediaRedaction** | **Boolean**| Instructs the Speech Recognition service to automatically redact PII from all transcripts media made on this service. The auto_redaction flag must be enabled, results in error otherwise. | [optional] |
| **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this Service, assigned by the developer, to be optionally used in addition to SID. | [optional] |
| **webhookHttpMethod** | **ServiceEnumHttpMethod**|  | [optional] [enum: GET, POST, NULL] |
| **webhookUrl** | **String**| The URL Twilio will request when executing the Webhook. | [optional] |

### Return type

[**IntelligenceV2Service**](IntelligenceV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

