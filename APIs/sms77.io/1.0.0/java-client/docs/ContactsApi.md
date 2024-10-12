# ContactsApi

All URIs are relative to *https://gateway.seven.io/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contactsGet**](ContactsApi.md#contactsGet) | **GET** /contacts |  |
| [**contactsPOST**](ContactsApi.md#contactsPOST) | **POST** /contacts |  |


<a id="contactsGet"></a>
# **contactsGet**
> String contactsGet(action, json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String action = "read"; // String | Determines the action to execute.
    BigDecimal json = new BigDecimal("0"); // BigDecimal | Defines whether to return the response as JSON or CSV separated by semicolon.
    try {
      String result = apiInstance.contactsGet(action, json);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsGet");
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
| **action** | **String**| Determines the action to execute. | [enum: read] |
| **json** | **BigDecimal**| Defines whether to return the response as JSON or CSV separated by semicolon. | [optional] [default to 0] [enum: 0, 1] |

### Return type

**String**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK (CSV) |  -  |

<a id="contactsPOST"></a>
# **contactsPOST**
> String contactsPOST(action, json, id, nick, empfaenger, email)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ContactsApi apiInstance = new ContactsApi(defaultClient);
    String action = "del"; // String | Determines the action to execute.
    BigDecimal json = new BigDecimal("0"); // BigDecimal | Defines whether to return the response as JSON or CSV separated by semicolon.
    String id = "id_example"; // String | The contact ID for editing/deletion.
    String nick = "nick_example"; // String | The contacts name.
    String empfaenger = "empfaenger_example"; // String | The contacts phone number.
    String email = "email_example"; // String | The contacts email address.
    try {
      String result = apiInstance.contactsPOST(action, json, id, nick, empfaenger, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactsApi#contactsPOST");
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
| **action** | **String**| Determines the action to execute. | [enum: del, write] |
| **json** | **BigDecimal**| Defines whether to return the response as JSON or CSV separated by semicolon. | [optional] [default to 0] [enum: 0, 1] |
| **id** | **String**| The contact ID for editing/deletion. | [optional] |
| **nick** | **String**| The contacts name. | [optional] |
| **empfaenger** | **String**| The contacts phone number. | [optional] |
| **email** | **String**| The contacts email address. | [optional] |

### Return type

**String**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

