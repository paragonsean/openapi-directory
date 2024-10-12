# MassMessagesUsersApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**massMessagesUsersGet**](MassMessagesUsersApi.md#massMessagesUsersGet) | **GET** /mass_messages_users | View list of mass messages for specific user |
| [**massMessagesUsersMassMessagesUserIdGet**](MassMessagesUsersApi.md#massMessagesUsersMassMessagesUserIdGet) | **GET** /mass_messages_users/{mass_messages_user_id} | View mass message |
| [**massMessagesUsersMassMessagesUserIdPut**](MassMessagesUsersApi.md#massMessagesUsersMassMessagesUserIdPut) | **PUT** /mass_messages_users/{mass_messages_user_id} | Edit mass message |


<a id="massMessagesUsersGet"></a>
# **massMessagesUsersGet**
> MassMessagesUsersGet200Response massMessagesUsersGet(isRead)

View list of mass messages for specific user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MassMessagesUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MassMessagesUsersApi apiInstance = new MassMessagesUsersApi(defaultClient);
    Boolean isRead = true; // Boolean | Used to filter on the `is_read` of the mass messages
    try {
      MassMessagesUsersGet200Response result = apiInstance.massMessagesUsersGet(isRead);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MassMessagesUsersApi#massMessagesUsersGet");
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
| **isRead** | **Boolean**| Used to filter on the &#x60;is_read&#x60; of the mass messages | [optional] |

### Return type

[**MassMessagesUsersGet200Response**](MassMessagesUsersGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="massMessagesUsersMassMessagesUserIdGet"></a>
# **massMessagesUsersMassMessagesUserIdGet**
> MassMessagesUsersMassMessagesUserIdGet200Response massMessagesUsersMassMessagesUserIdGet(massMessagesUserId)

View mass message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MassMessagesUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MassMessagesUsersApi apiInstance = new MassMessagesUsersApi(defaultClient);
    String massMessagesUserId = "massMessagesUserId_example"; // String | 
    try {
      MassMessagesUsersMassMessagesUserIdGet200Response result = apiInstance.massMessagesUsersMassMessagesUserIdGet(massMessagesUserId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MassMessagesUsersApi#massMessagesUsersMassMessagesUserIdGet");
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
| **massMessagesUserId** | **String**|  | |

### Return type

[**MassMessagesUsersMassMessagesUserIdGet200Response**](MassMessagesUsersMassMessagesUserIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="massMessagesUsersMassMessagesUserIdPut"></a>
# **massMessagesUsersMassMessagesUserIdPut**
> ClockingRecordsClockingRecordIdPut200Response massMessagesUsersMassMessagesUserIdPut(massMessagesUserId)

Edit mass message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MassMessagesUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    MassMessagesUsersApi apiInstance = new MassMessagesUsersApi(defaultClient);
    String massMessagesUserId = "massMessagesUserId_example"; // String | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.massMessagesUsersMassMessagesUserIdPut(massMessagesUserId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MassMessagesUsersApi#massMessagesUsersMassMessagesUserIdPut");
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
| **massMessagesUserId** | **String**|  | |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

