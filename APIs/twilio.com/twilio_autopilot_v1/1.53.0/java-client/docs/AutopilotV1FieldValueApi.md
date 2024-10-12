# AutopilotV1FieldValueApi

All URIs are relative to *https://autopilot.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createFieldValue**](AutopilotV1FieldValueApi.md#createFieldValue) | **POST** /v1/Assistants/{AssistantSid}/FieldTypes/{FieldTypeSid}/FieldValues |  |
| [**deleteFieldValue**](AutopilotV1FieldValueApi.md#deleteFieldValue) | **DELETE** /v1/Assistants/{AssistantSid}/FieldTypes/{FieldTypeSid}/FieldValues/{Sid} |  |
| [**fetchFieldValue**](AutopilotV1FieldValueApi.md#fetchFieldValue) | **GET** /v1/Assistants/{AssistantSid}/FieldTypes/{FieldTypeSid}/FieldValues/{Sid} |  |
| [**listFieldValue**](AutopilotV1FieldValueApi.md#listFieldValue) | **GET** /v1/Assistants/{AssistantSid}/FieldTypes/{FieldTypeSid}/FieldValues |  |


<a id="createFieldValue"></a>
# **createFieldValue**
> AutopilotV1AssistantFieldTypeFieldValue createFieldValue(assistantSid, fieldTypeSid, language, value, synonymOf)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1FieldValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1FieldValueApi apiInstance = new AutopilotV1FieldValueApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the new resource.
    String fieldTypeSid = "fieldTypeSid_example"; // String | The SID of the Field Type associated with the Field Value.
    String language = "language_example"; // String | The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
    String value = "value_example"; // String | The Field Value data.
    String synonymOf = "synonymOf_example"; // String | The string value that indicates which word the field value is a synonym of.
    try {
      AutopilotV1AssistantFieldTypeFieldValue result = apiInstance.createFieldValue(assistantSid, fieldTypeSid, language, value, synonymOf);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1FieldValueApi#createFieldValue");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the new resource. | |
| **fieldTypeSid** | **String**| The SID of the Field Type associated with the Field Value. | |
| **language** | **String**| The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: &#x60;en-US&#x60; | |
| **value** | **String**| The Field Value data. | |
| **synonymOf** | **String**| The string value that indicates which word the field value is a synonym of. | [optional] |

### Return type

[**AutopilotV1AssistantFieldTypeFieldValue**](AutopilotV1AssistantFieldTypeFieldValue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteFieldValue"></a>
# **deleteFieldValue**
> deleteFieldValue(assistantSid, fieldTypeSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1FieldValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1FieldValueApi apiInstance = new AutopilotV1FieldValueApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to delete.
    String fieldTypeSid = "fieldTypeSid_example"; // String | The SID of the Field Type associated with the Field Value to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the FieldValue resource to delete.
    try {
      apiInstance.deleteFieldValue(assistantSid, fieldTypeSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1FieldValueApi#deleteFieldValue");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to delete. | |
| **fieldTypeSid** | **String**| The SID of the Field Type associated with the Field Value to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the FieldValue resource to delete. | |

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

<a id="fetchFieldValue"></a>
# **fetchFieldValue**
> AutopilotV1AssistantFieldTypeFieldValue fetchFieldValue(assistantSid, fieldTypeSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1FieldValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1FieldValueApi apiInstance = new AutopilotV1FieldValueApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resource to fetch.
    String fieldTypeSid = "fieldTypeSid_example"; // String | The SID of the Field Type associated with the Field Value to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the FieldValue resource to fetch.
    try {
      AutopilotV1AssistantFieldTypeFieldValue result = apiInstance.fetchFieldValue(assistantSid, fieldTypeSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1FieldValueApi#fetchFieldValue");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resource to fetch. | |
| **fieldTypeSid** | **String**| The SID of the Field Type associated with the Field Value to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the FieldValue resource to fetch. | |

### Return type

[**AutopilotV1AssistantFieldTypeFieldValue**](AutopilotV1AssistantFieldTypeFieldValue.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listFieldValue"></a>
# **listFieldValue**
> ListFieldValueResponse listFieldValue(assistantSid, fieldTypeSid, language, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1FieldValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1FieldValueApi apiInstance = new AutopilotV1FieldValueApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to read.
    String fieldTypeSid = "fieldTypeSid_example"; // String | The SID of the Field Type associated with the Field Value to read.
    String language = "language_example"; // String | The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListFieldValueResponse result = apiInstance.listFieldValue(assistantSid, fieldTypeSid, language, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1FieldValueApi#listFieldValue");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to read. | |
| **fieldTypeSid** | **String**| The SID of the Field Type associated with the Field Value to read. | |
| **language** | **String**| The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: &#x60;en-US&#x60; | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListFieldValueResponse**](ListFieldValueResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

