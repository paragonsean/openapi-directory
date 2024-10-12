# ConversationsV1AddressConfigurationApi

All URIs are relative to *https://conversations.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createConfigurationAddress**](ConversationsV1AddressConfigurationApi.md#createConfigurationAddress) | **POST** /v1/Configuration/Addresses |  |
| [**deleteConfigurationAddress**](ConversationsV1AddressConfigurationApi.md#deleteConfigurationAddress) | **DELETE** /v1/Configuration/Addresses/{Sid} |  |
| [**fetchConfigurationAddress**](ConversationsV1AddressConfigurationApi.md#fetchConfigurationAddress) | **GET** /v1/Configuration/Addresses/{Sid} |  |
| [**listConfigurationAddress**](ConversationsV1AddressConfigurationApi.md#listConfigurationAddress) | **GET** /v1/Configuration/Addresses |  |
| [**updateConfigurationAddress**](ConversationsV1AddressConfigurationApi.md#updateConfigurationAddress) | **POST** /v1/Configuration/Addresses/{Sid} |  |


<a id="createConfigurationAddress"></a>
# **createConfigurationAddress**
> ConversationsV1ConfigurationAddress createConfigurationAddress(address, type, addressCountry, autoCreationConversationServiceSid, autoCreationEnabled, autoCreationStudioFlowSid, autoCreationStudioRetryCount, autoCreationType, autoCreationWebhookFilters, autoCreationWebhookMethod, autoCreationWebhookUrl, friendlyName)



Create a new address configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1AddressConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1AddressConfigurationApi apiInstance = new ConversationsV1AddressConfigurationApi(defaultClient);
    String address = "address_example"; // String | The unique address to be configured. The address can be a whatsapp address or phone number
    ConfigurationAddressEnumType type = ConfigurationAddressEnumType.fromValue("sms"); // ConfigurationAddressEnumType | 
    String addressCountry = "addressCountry_example"; // String | An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only applicable to short code addresses.
    String autoCreationConversationServiceSid = "autoCreationConversationServiceSid_example"; // String | Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
    Boolean autoCreationEnabled = true; // Boolean | Enable/Disable auto-creating conversations for messages to this address
    String autoCreationStudioFlowSid = "autoCreationStudioFlowSid_example"; // String | For type `studio`, the studio flow SID where the webhook should be sent to.
    Integer autoCreationStudioRetryCount = 56; // Integer | For type `studio`, number of times to retry the webhook request
    ConfigurationAddressEnumAutoCreationType autoCreationType = ConfigurationAddressEnumAutoCreationType.fromValue("webhook"); // ConfigurationAddressEnumAutoCreationType | 
    List<String> autoCreationWebhookFilters = Arrays.asList(); // List<String> | The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
    ConfigurationAddressEnumMethod autoCreationWebhookMethod = ConfigurationAddressEnumMethod.fromValue("GET"); // ConfigurationAddressEnumMethod | 
    String autoCreationWebhookUrl = "autoCreationWebhookUrl_example"; // String | For type `webhook`, the url for the webhook request.
    String friendlyName = "friendlyName_example"; // String | The human-readable name of this configuration, limited to 256 characters. Optional.
    try {
      ConversationsV1ConfigurationAddress result = apiInstance.createConfigurationAddress(address, type, addressCountry, autoCreationConversationServiceSid, autoCreationEnabled, autoCreationStudioFlowSid, autoCreationStudioRetryCount, autoCreationType, autoCreationWebhookFilters, autoCreationWebhookMethod, autoCreationWebhookUrl, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1AddressConfigurationApi#createConfigurationAddress");
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
| **address** | **String**| The unique address to be configured. The address can be a whatsapp address or phone number | |
| **type** | **ConfigurationAddressEnumType**|  | [enum: sms, whatsapp, messenger, gbm, email] |
| **addressCountry** | **String**| An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only applicable to short code addresses. | [optional] |
| **autoCreationConversationServiceSid** | **String**| Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service. | [optional] |
| **autoCreationEnabled** | **Boolean**| Enable/Disable auto-creating conversations for messages to this address | [optional] |
| **autoCreationStudioFlowSid** | **String**| For type &#x60;studio&#x60;, the studio flow SID where the webhook should be sent to. | [optional] |
| **autoCreationStudioRetryCount** | **Integer**| For type &#x60;studio&#x60;, number of times to retry the webhook request | [optional] |
| **autoCreationType** | **ConfigurationAddressEnumAutoCreationType**|  | [optional] [enum: webhook, studio, default] |
| **autoCreationWebhookFilters** | [**List&lt;String&gt;**](String.md)| The list of events, firing webhook event for this Conversation. Values can be any of the following: &#x60;onMessageAdded&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationStateUpdated&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onParticipantRemoved&#x60;, &#x60;onDeliveryUpdated&#x60; | [optional] |
| **autoCreationWebhookMethod** | **ConfigurationAddressEnumMethod**|  | [optional] [enum: GET, POST] |
| **autoCreationWebhookUrl** | **String**| For type &#x60;webhook&#x60;, the url for the webhook request. | [optional] |
| **friendlyName** | **String**| The human-readable name of this configuration, limited to 256 characters. Optional. | [optional] |

### Return type

[**ConversationsV1ConfigurationAddress**](ConversationsV1ConfigurationAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteConfigurationAddress"></a>
# **deleteConfigurationAddress**
> deleteConfigurationAddress(sid)



Remove an existing address configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1AddressConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1AddressConfigurationApi apiInstance = new ConversationsV1AddressConfigurationApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration
    try {
      apiInstance.deleteConfigurationAddress(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1AddressConfigurationApi#deleteConfigurationAddress");
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
| **sid** | **String**| The SID of the Address Configuration resource. This value can be either the &#x60;sid&#x60; or the &#x60;address&#x60; of the configuration | |

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

<a id="fetchConfigurationAddress"></a>
# **fetchConfigurationAddress**
> ConversationsV1ConfigurationAddress fetchConfigurationAddress(sid)



Fetch an address configuration 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1AddressConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1AddressConfigurationApi apiInstance = new ConversationsV1AddressConfigurationApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration
    try {
      ConversationsV1ConfigurationAddress result = apiInstance.fetchConfigurationAddress(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1AddressConfigurationApi#fetchConfigurationAddress");
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
| **sid** | **String**| The SID of the Address Configuration resource. This value can be either the &#x60;sid&#x60; or the &#x60;address&#x60; of the configuration | |

### Return type

[**ConversationsV1ConfigurationAddress**](ConversationsV1ConfigurationAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listConfigurationAddress"></a>
# **listConfigurationAddress**
> ListConfigurationAddressResponse listConfigurationAddress(type, pageSize, page, pageToken)



Retrieve a list of address configurations for an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1AddressConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1AddressConfigurationApi apiInstance = new ConversationsV1AddressConfigurationApi(defaultClient);
    String type = "type_example"; // String | Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListConfigurationAddressResponse result = apiInstance.listConfigurationAddress(type, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1AddressConfigurationApi#listConfigurationAddress");
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
| **type** | **String**| Filter the address configurations by its type. This value can be one of: &#x60;whatsapp&#x60;, &#x60;sms&#x60;. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListConfigurationAddressResponse**](ListConfigurationAddressResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateConfigurationAddress"></a>
# **updateConfigurationAddress**
> ConversationsV1ConfigurationAddress updateConfigurationAddress(sid, autoCreationConversationServiceSid, autoCreationEnabled, autoCreationStudioFlowSid, autoCreationStudioRetryCount, autoCreationType, autoCreationWebhookFilters, autoCreationWebhookMethod, autoCreationWebhookUrl, friendlyName)



Update an existing address configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1AddressConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1AddressConfigurationApi apiInstance = new ConversationsV1AddressConfigurationApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration
    String autoCreationConversationServiceSid = "autoCreationConversationServiceSid_example"; // String | Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
    Boolean autoCreationEnabled = true; // Boolean | Enable/Disable auto-creating conversations for messages to this address
    String autoCreationStudioFlowSid = "autoCreationStudioFlowSid_example"; // String | For type `studio`, the studio flow SID where the webhook should be sent to.
    Integer autoCreationStudioRetryCount = 56; // Integer | For type `studio`, number of times to retry the webhook request
    ConfigurationAddressEnumAutoCreationType autoCreationType = ConfigurationAddressEnumAutoCreationType.fromValue("webhook"); // ConfigurationAddressEnumAutoCreationType | 
    List<String> autoCreationWebhookFilters = Arrays.asList(); // List<String> | The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
    ConfigurationAddressEnumMethod autoCreationWebhookMethod = ConfigurationAddressEnumMethod.fromValue("GET"); // ConfigurationAddressEnumMethod | 
    String autoCreationWebhookUrl = "autoCreationWebhookUrl_example"; // String | For type `webhook`, the url for the webhook request.
    String friendlyName = "friendlyName_example"; // String | The human-readable name of this configuration, limited to 256 characters. Optional.
    try {
      ConversationsV1ConfigurationAddress result = apiInstance.updateConfigurationAddress(sid, autoCreationConversationServiceSid, autoCreationEnabled, autoCreationStudioFlowSid, autoCreationStudioRetryCount, autoCreationType, autoCreationWebhookFilters, autoCreationWebhookMethod, autoCreationWebhookUrl, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1AddressConfigurationApi#updateConfigurationAddress");
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
| **sid** | **String**| The SID of the Address Configuration resource. This value can be either the &#x60;sid&#x60; or the &#x60;address&#x60; of the configuration | |
| **autoCreationConversationServiceSid** | **String**| Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service. | [optional] |
| **autoCreationEnabled** | **Boolean**| Enable/Disable auto-creating conversations for messages to this address | [optional] |
| **autoCreationStudioFlowSid** | **String**| For type &#x60;studio&#x60;, the studio flow SID where the webhook should be sent to. | [optional] |
| **autoCreationStudioRetryCount** | **Integer**| For type &#x60;studio&#x60;, number of times to retry the webhook request | [optional] |
| **autoCreationType** | **ConfigurationAddressEnumAutoCreationType**|  | [optional] [enum: webhook, studio, default] |
| **autoCreationWebhookFilters** | [**List&lt;String&gt;**](String.md)| The list of events, firing webhook event for this Conversation. Values can be any of the following: &#x60;onMessageAdded&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationStateUpdated&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onParticipantRemoved&#x60;, &#x60;onDeliveryUpdated&#x60; | [optional] |
| **autoCreationWebhookMethod** | **ConfigurationAddressEnumMethod**|  | [optional] [enum: GET, POST] |
| **autoCreationWebhookUrl** | **String**| For type &#x60;webhook&#x60;, the url for the webhook request. | [optional] |
| **friendlyName** | **String**| The human-readable name of this configuration, limited to 256 characters. Optional. | [optional] |

### Return type

[**ConversationsV1ConfigurationAddress**](ConversationsV1ConfigurationAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

