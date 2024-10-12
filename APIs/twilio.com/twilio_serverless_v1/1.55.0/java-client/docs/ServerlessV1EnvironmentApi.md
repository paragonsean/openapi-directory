# ServerlessV1EnvironmentApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEnvironment**](ServerlessV1EnvironmentApi.md#createEnvironment) | **POST** /v1/Services/{ServiceSid}/Environments |  |
| [**deleteEnvironment**](ServerlessV1EnvironmentApi.md#deleteEnvironment) | **DELETE** /v1/Services/{ServiceSid}/Environments/{Sid} |  |
| [**fetchEnvironment**](ServerlessV1EnvironmentApi.md#fetchEnvironment) | **GET** /v1/Services/{ServiceSid}/Environments/{Sid} |  |
| [**listEnvironment**](ServerlessV1EnvironmentApi.md#listEnvironment) | **GET** /v1/Services/{ServiceSid}/Environments |  |


<a id="createEnvironment"></a>
# **createEnvironment**
> ServerlessV1ServiceEnvironment createEnvironment(serviceSid, uniqueName, domainSuffix)



Create a new environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1EnvironmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1EnvironmentApi apiInstance = new ServerlessV1EnvironmentApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Environment resource under.
    String uniqueName = "uniqueName_example"; // String | A user-defined string that uniquely identifies the Environment resource. It can be a maximum of 100 characters.
    String domainSuffix = "domainSuffix_example"; // String | A URL-friendly name that represents the environment and forms part of the domain name. It can be a maximum of 16 characters.
    try {
      ServerlessV1ServiceEnvironment result = apiInstance.createEnvironment(serviceSid, uniqueName, domainSuffix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1EnvironmentApi#createEnvironment");
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
| **serviceSid** | **String**| The SID of the Service to create the Environment resource under. | |
| **uniqueName** | **String**| A user-defined string that uniquely identifies the Environment resource. It can be a maximum of 100 characters. | |
| **domainSuffix** | **String**| A URL-friendly name that represents the environment and forms part of the domain name. It can be a maximum of 16 characters. | [optional] |

### Return type

[**ServerlessV1ServiceEnvironment**](ServerlessV1ServiceEnvironment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteEnvironment"></a>
# **deleteEnvironment**
> deleteEnvironment(serviceSid, sid)



Delete a specific environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1EnvironmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1EnvironmentApi apiInstance = new ServerlessV1EnvironmentApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to delete the Environment resource from.
    String sid = "sid_example"; // String | The SID of the Environment resource to delete.
    try {
      apiInstance.deleteEnvironment(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1EnvironmentApi#deleteEnvironment");
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
| **serviceSid** | **String**| The SID of the Service to delete the Environment resource from. | |
| **sid** | **String**| The SID of the Environment resource to delete. | |

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

<a id="fetchEnvironment"></a>
# **fetchEnvironment**
> ServerlessV1ServiceEnvironment fetchEnvironment(serviceSid, sid)



Retrieve a specific environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1EnvironmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1EnvironmentApi apiInstance = new ServerlessV1EnvironmentApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Environment resource from.
    String sid = "sid_example"; // String | The SID of the Environment resource to fetch.
    try {
      ServerlessV1ServiceEnvironment result = apiInstance.fetchEnvironment(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1EnvironmentApi#fetchEnvironment");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Environment resource from. | |
| **sid** | **String**| The SID of the Environment resource to fetch. | |

### Return type

[**ServerlessV1ServiceEnvironment**](ServerlessV1ServiceEnvironment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listEnvironment"></a>
# **listEnvironment**
> ListEnvironmentResponse listEnvironment(serviceSid, pageSize, page, pageToken)



Retrieve a list of all environments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1EnvironmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1EnvironmentApi apiInstance = new ServerlessV1EnvironmentApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Environment resources from.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListEnvironmentResponse result = apiInstance.listEnvironment(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1EnvironmentApi#listEnvironment");
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
| **serviceSid** | **String**| The SID of the Service to read the Environment resources from. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListEnvironmentResponse**](ListEnvironmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

