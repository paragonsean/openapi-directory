# ServerlessV1VariableApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVariable**](ServerlessV1VariableApi.md#createVariable) | **POST** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Variables |  |
| [**deleteVariable**](ServerlessV1VariableApi.md#deleteVariable) | **DELETE** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Variables/{Sid} |  |
| [**fetchVariable**](ServerlessV1VariableApi.md#fetchVariable) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Variables/{Sid} |  |
| [**listVariable**](ServerlessV1VariableApi.md#listVariable) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Variables |  |
| [**updateVariable**](ServerlessV1VariableApi.md#updateVariable) | **POST** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Variables/{Sid} |  |


<a id="createVariable"></a>
# **createVariable**
> ServerlessV1ServiceEnvironmentVariable createVariable(serviceSid, environmentSid, key, value)



Create a new Variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1VariableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1VariableApi apiInstance = new ServerlessV1VariableApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Variable resource under.
    String environmentSid = "environmentSid_example"; // String | The SID of the Environment in which the Variable resource exists.
    String key = "key_example"; // String | A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
    String value = "value_example"; // String | A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.
    try {
      ServerlessV1ServiceEnvironmentVariable result = apiInstance.createVariable(serviceSid, environmentSid, key, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1VariableApi#createVariable");
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
| **serviceSid** | **String**| The SID of the Service to create the Variable resource under. | |
| **environmentSid** | **String**| The SID of the Environment in which the Variable resource exists. | |
| **key** | **String**| A string by which the Variable resource can be referenced. It can be a maximum of 128 characters. | |
| **value** | **String**| A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size. | |

### Return type

[**ServerlessV1ServiceEnvironmentVariable**](ServerlessV1ServiceEnvironmentVariable.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteVariable"></a>
# **deleteVariable**
> deleteVariable(serviceSid, environmentSid, sid)



Delete a specific Variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1VariableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1VariableApi apiInstance = new ServerlessV1VariableApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to delete the Variable resource from.
    String environmentSid = "environmentSid_example"; // String | The SID of the Environment with the Variables to delete.
    String sid = "sid_example"; // String | The SID of the Variable resource to delete.
    try {
      apiInstance.deleteVariable(serviceSid, environmentSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1VariableApi#deleteVariable");
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
| **serviceSid** | **String**| The SID of the Service to delete the Variable resource from. | |
| **environmentSid** | **String**| The SID of the Environment with the Variables to delete. | |
| **sid** | **String**| The SID of the Variable resource to delete. | |

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

<a id="fetchVariable"></a>
# **fetchVariable**
> ServerlessV1ServiceEnvironmentVariable fetchVariable(serviceSid, environmentSid, sid)



Retrieve a specific Variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1VariableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1VariableApi apiInstance = new ServerlessV1VariableApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Variable resource from.
    String environmentSid = "environmentSid_example"; // String | The SID of the Environment with the Variable resource to fetch.
    String sid = "sid_example"; // String | The SID of the Variable resource to fetch.
    try {
      ServerlessV1ServiceEnvironmentVariable result = apiInstance.fetchVariable(serviceSid, environmentSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1VariableApi#fetchVariable");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Variable resource from. | |
| **environmentSid** | **String**| The SID of the Environment with the Variable resource to fetch. | |
| **sid** | **String**| The SID of the Variable resource to fetch. | |

### Return type

[**ServerlessV1ServiceEnvironmentVariable**](ServerlessV1ServiceEnvironmentVariable.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listVariable"></a>
# **listVariable**
> ListVariableResponse listVariable(serviceSid, environmentSid, pageSize, page, pageToken)



Retrieve a list of all Variables.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1VariableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1VariableApi apiInstance = new ServerlessV1VariableApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Variable resources from.
    String environmentSid = "environmentSid_example"; // String | The SID of the Environment with the Variable resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListVariableResponse result = apiInstance.listVariable(serviceSid, environmentSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1VariableApi#listVariable");
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
| **serviceSid** | **String**| The SID of the Service to read the Variable resources from. | |
| **environmentSid** | **String**| The SID of the Environment with the Variable resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListVariableResponse**](ListVariableResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateVariable"></a>
# **updateVariable**
> ServerlessV1ServiceEnvironmentVariable updateVariable(serviceSid, environmentSid, sid, key, value)



Update a specific Variable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1VariableApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1VariableApi apiInstance = new ServerlessV1VariableApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to update the Variable resource under.
    String environmentSid = "environmentSid_example"; // String | The SID of the Environment with the Variable resource to update.
    String sid = "sid_example"; // String | The SID of the Variable resource to update.
    String key = "key_example"; // String | A string by which the Variable resource can be referenced. It can be a maximum of 128 characters.
    String value = "value_example"; // String | A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size.
    try {
      ServerlessV1ServiceEnvironmentVariable result = apiInstance.updateVariable(serviceSid, environmentSid, sid, key, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1VariableApi#updateVariable");
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
| **serviceSid** | **String**| The SID of the Service to update the Variable resource under. | |
| **environmentSid** | **String**| The SID of the Environment with the Variable resource to update. | |
| **sid** | **String**| The SID of the Variable resource to update. | |
| **key** | **String**| A string by which the Variable resource can be referenced. It can be a maximum of 128 characters. | [optional] |
| **value** | **String**| A string that contains the actual value of the Variable. It can be a maximum of 450 bytes in size. | [optional] |

### Return type

[**ServerlessV1ServiceEnvironmentVariable**](ServerlessV1ServiceEnvironmentVariable.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

