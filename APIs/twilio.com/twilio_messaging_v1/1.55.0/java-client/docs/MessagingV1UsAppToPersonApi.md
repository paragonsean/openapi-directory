# MessagingV1UsAppToPersonApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUsAppToPerson**](MessagingV1UsAppToPersonApi.md#createUsAppToPerson) | **POST** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p |  |
| [**deleteUsAppToPerson**](MessagingV1UsAppToPersonApi.md#deleteUsAppToPerson) | **DELETE** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid} |  |
| [**fetchUsAppToPerson**](MessagingV1UsAppToPersonApi.md#fetchUsAppToPerson) | **GET** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid} |  |
| [**listUsAppToPerson**](MessagingV1UsAppToPersonApi.md#listUsAppToPerson) | **GET** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p |  |
| [**updateUsAppToPerson**](MessagingV1UsAppToPersonApi.md#updateUsAppToPerson) | **POST** /v1/Services/{MessagingServiceSid}/Compliance/Usa2p/{Sid} |  |


<a id="createUsAppToPerson"></a>
# **createUsAppToPerson**
> MessagingV1ServiceUsAppToPerson createUsAppToPerson(messagingServiceSid, brandRegistrationSid, description, hasEmbeddedLinks, hasEmbeddedPhone, messageFlow, messageSamples, usAppToPersonUsecase, ageGated, directLending, helpKeywords, helpMessage, optInKeywords, optInMessage, optOutKeywords, optOutMessage, subscriberOptIn)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1UsAppToPersonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1UsAppToPersonApi apiInstance = new MessagingV1UsAppToPersonApi(defaultClient);
    String messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to create the resources from.
    String brandRegistrationSid = "brandRegistrationSid_example"; // String | A2P Brand Registration SID
    String description = "description_example"; // String | A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
    Boolean hasEmbeddedLinks = true; // Boolean | Indicates that this SMS campaign will send messages that contain links.
    Boolean hasEmbeddedPhone = true; // Boolean | Indicates that this SMS campaign will send messages that contain phone numbers.
    String messageFlow = "messageFlow_example"; // String | Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
    List<String> messageSamples = Arrays.asList(); // List<String> | An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars.
    String usAppToPersonUsecase = "usAppToPersonUsecase_example"; // String | A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
    Boolean ageGated = true; // Boolean | A boolean that specifies whether campaign is age gated or not.
    Boolean directLending = true; // Boolean | A boolean that specifies whether campaign allows direct lending or not.
    List<String> helpKeywords = Arrays.asList(); // List<String> | End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
    String helpMessage = "helpMessage_example"; // String | When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
    List<String> optInKeywords = Arrays.asList(); // List<String> | If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.
    String optInMessage = "optInMessage_example"; // String | If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.
    List<String> optOutKeywords = Arrays.asList(); // List<String> | End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
    String optOutMessage = "optOutMessage_example"; // String | Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
    Boolean subscriberOptIn = true; // Boolean | A boolean that specifies whether campaign has Subscriber Optin or not.
    try {
      MessagingV1ServiceUsAppToPerson result = apiInstance.createUsAppToPerson(messagingServiceSid, brandRegistrationSid, description, hasEmbeddedLinks, hasEmbeddedPhone, messageFlow, messageSamples, usAppToPersonUsecase, ageGated, directLending, helpKeywords, helpMessage, optInKeywords, optInMessage, optOutKeywords, optOutMessage, subscriberOptIn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1UsAppToPersonApi#createUsAppToPerson");
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
| **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to create the resources from. | |
| **brandRegistrationSid** | **String**| A2P Brand Registration SID | |
| **description** | **String**| A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters. | |
| **hasEmbeddedLinks** | **Boolean**| Indicates that this SMS campaign will send messages that contain links. | |
| **hasEmbeddedPhone** | **Boolean**| Indicates that this SMS campaign will send messages that contain phone numbers. | |
| **messageFlow** | **String**| Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum. | |
| **messageSamples** | [**List&lt;String&gt;**](String.md)| An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars. | |
| **usAppToPersonUsecase** | **String**| A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..] | |
| **ageGated** | **Boolean**| A boolean that specifies whether campaign is age gated or not. | [optional] |
| **directLending** | **Boolean**| A boolean that specifies whether campaign allows direct lending or not. | [optional] |
| **helpKeywords** | [**List&lt;String&gt;**](String.md)| End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum. | [optional] |
| **helpMessage** | **String**| When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). 20 character minimum. 320 character maximum. | [optional] |
| **optInKeywords** | [**List&lt;String&gt;**](String.md)| If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum. | [optional] |
| **optInMessage** | **String**| If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum. | [optional] |
| **optOutKeywords** | [**List&lt;String&gt;**](String.md)| End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum. | [optional] |
| **optOutMessage** | **String**| Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio&#39;s Default or Advanced Opt Out features). 20 character minimum. 320 character maximum. | [optional] |
| **subscriberOptIn** | **Boolean**| A boolean that specifies whether campaign has Subscriber Optin or not. | [optional] |

### Return type

[**MessagingV1ServiceUsAppToPerson**](MessagingV1ServiceUsAppToPerson.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteUsAppToPerson"></a>
# **deleteUsAppToPerson**
> deleteUsAppToPerson(messagingServiceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1UsAppToPersonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1UsAppToPersonApi apiInstance = new MessagingV1UsAppToPersonApi(defaultClient);
    String messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to delete the resource from.
    String sid = "sid_example"; // String | The SID of the US A2P Compliance resource to delete `QE2c6890da8086d771620e9b13fadeba0b`.
    try {
      apiInstance.deleteUsAppToPerson(messagingServiceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1UsAppToPersonApi#deleteUsAppToPerson");
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
| **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to delete the resource from. | |
| **sid** | **String**| The SID of the US A2P Compliance resource to delete &#x60;QE2c6890da8086d771620e9b13fadeba0b&#x60;. | |

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

<a id="fetchUsAppToPerson"></a>
# **fetchUsAppToPerson**
> MessagingV1ServiceUsAppToPerson fetchUsAppToPerson(messagingServiceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1UsAppToPersonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1UsAppToPersonApi apiInstance = new MessagingV1UsAppToPersonApi(defaultClient);
    String messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from.
    String sid = "sid_example"; // String | The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.
    try {
      MessagingV1ServiceUsAppToPerson result = apiInstance.fetchUsAppToPerson(messagingServiceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1UsAppToPersonApi#fetchUsAppToPerson");
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
| **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from. | |
| **sid** | **String**| The SID of the US A2P Compliance resource to fetch &#x60;QE2c6890da8086d771620e9b13fadeba0b&#x60;. | |

### Return type

[**MessagingV1ServiceUsAppToPerson**](MessagingV1ServiceUsAppToPerson.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listUsAppToPerson"></a>
# **listUsAppToPerson**
> ListUsAppToPersonResponse listUsAppToPerson(messagingServiceSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1UsAppToPersonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1UsAppToPersonApi apiInstance = new MessagingV1UsAppToPersonApi(defaultClient);
    String messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListUsAppToPersonResponse result = apiInstance.listUsAppToPerson(messagingServiceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1UsAppToPersonApi#listUsAppToPerson");
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
| **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to fetch the resource from. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListUsAppToPersonResponse**](ListUsAppToPersonResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateUsAppToPerson"></a>
# **updateUsAppToPerson**
> MessagingV1ServiceUsAppToPerson updateUsAppToPerson(messagingServiceSid, sid, ageGated, description, directLending, hasEmbeddedLinks, hasEmbeddedPhone, messageFlow, messageSamples)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1UsAppToPersonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1UsAppToPersonApi apiInstance = new MessagingV1UsAppToPersonApi(defaultClient);
    String messagingServiceSid = "messagingServiceSid_example"; // String | The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to update the resource from.
    String sid = "sid_example"; // String | The SID of the US A2P Compliance resource to update `QE2c6890da8086d771620e9b13fadeba0b`.
    Boolean ageGated = true; // Boolean | A boolean that specifies whether campaign requires age gate for federally legal content.
    String description = "description_example"; // String | A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
    Boolean directLending = true; // Boolean | A boolean that specifies whether campaign allows direct lending or not.
    Boolean hasEmbeddedLinks = true; // Boolean | Indicates that this SMS campaign will send messages that contain links.
    Boolean hasEmbeddedPhone = true; // Boolean | Indicates that this SMS campaign will send messages that contain phone numbers.
    String messageFlow = "messageFlow_example"; // String | Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
    List<String> messageSamples = Arrays.asList(); // List<String> | An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars.
    try {
      MessagingV1ServiceUsAppToPerson result = apiInstance.updateUsAppToPerson(messagingServiceSid, sid, ageGated, description, directLending, hasEmbeddedLinks, hasEmbeddedPhone, messageFlow, messageSamples);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1UsAppToPersonApi#updateUsAppToPerson");
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
| **messagingServiceSid** | **String**| The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to update the resource from. | |
| **sid** | **String**| The SID of the US A2P Compliance resource to update &#x60;QE2c6890da8086d771620e9b13fadeba0b&#x60;. | |
| **ageGated** | **Boolean**| A boolean that specifies whether campaign requires age gate for federally legal content. | |
| **description** | **String**| A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters. | |
| **directLending** | **Boolean**| A boolean that specifies whether campaign allows direct lending or not. | |
| **hasEmbeddedLinks** | **Boolean**| Indicates that this SMS campaign will send messages that contain links. | |
| **hasEmbeddedPhone** | **Boolean**| Indicates that this SMS campaign will send messages that contain phone numbers. | |
| **messageFlow** | **String**| Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum. | |
| **messageSamples** | [**List&lt;String&gt;**](String.md)| An array of sample message strings, min two and max five. Min length for each sample: 20 chars. Max length for each sample: 1024 chars. | |

### Return type

[**MessagingV1ServiceUsAppToPerson**](MessagingV1ServiceUsAppToPerson.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

