# ServerlessV1BuildApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBuild**](ServerlessV1BuildApi.md#createBuild) | **POST** /v1/Services/{ServiceSid}/Builds |  |
| [**deleteBuild**](ServerlessV1BuildApi.md#deleteBuild) | **DELETE** /v1/Services/{ServiceSid}/Builds/{Sid} |  |
| [**fetchBuild**](ServerlessV1BuildApi.md#fetchBuild) | **GET** /v1/Services/{ServiceSid}/Builds/{Sid} |  |
| [**listBuild**](ServerlessV1BuildApi.md#listBuild) | **GET** /v1/Services/{ServiceSid}/Builds |  |


<a id="createBuild"></a>
# **createBuild**
> ServerlessV1ServiceBuild createBuild(serviceSid, assetVersions, dependencies, functionVersions, runtime)



Create a new Build resource. At least one function version or asset version is required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1BuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1BuildApi apiInstance = new ServerlessV1BuildApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Build resource under.
    List<String> assetVersions = Arrays.asList(); // List<String> | The list of Asset Version resource SIDs to include in the Build.
    String dependencies = "dependencies_example"; // String | A list of objects that describe the Dependencies included in the Build. Each object contains the `name` and `version` of the dependency.
    List<String> functionVersions = Arrays.asList(); // List<String> | The list of the Function Version resource SIDs to include in the Build.
    String runtime = "runtime_example"; // String | The Runtime version that will be used to run the Build resource when it is deployed.
    try {
      ServerlessV1ServiceBuild result = apiInstance.createBuild(serviceSid, assetVersions, dependencies, functionVersions, runtime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1BuildApi#createBuild");
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
| **serviceSid** | **String**| The SID of the Service to create the Build resource under. | |
| **assetVersions** | [**List&lt;String&gt;**](String.md)| The list of Asset Version resource SIDs to include in the Build. | [optional] |
| **dependencies** | **String**| A list of objects that describe the Dependencies included in the Build. Each object contains the &#x60;name&#x60; and &#x60;version&#x60; of the dependency. | [optional] |
| **functionVersions** | [**List&lt;String&gt;**](String.md)| The list of the Function Version resource SIDs to include in the Build. | [optional] |
| **runtime** | **String**| The Runtime version that will be used to run the Build resource when it is deployed. | [optional] |

### Return type

[**ServerlessV1ServiceBuild**](ServerlessV1ServiceBuild.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteBuild"></a>
# **deleteBuild**
> deleteBuild(serviceSid, sid)



Delete a Build resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1BuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1BuildApi apiInstance = new ServerlessV1BuildApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to delete the Build resource from.
    String sid = "sid_example"; // String | The SID of the Build resource to delete.
    try {
      apiInstance.deleteBuild(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1BuildApi#deleteBuild");
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
| **serviceSid** | **String**| The SID of the Service to delete the Build resource from. | |
| **sid** | **String**| The SID of the Build resource to delete. | |

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

<a id="fetchBuild"></a>
# **fetchBuild**
> ServerlessV1ServiceBuild fetchBuild(serviceSid, sid)



Retrieve a specific Build resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1BuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1BuildApi apiInstance = new ServerlessV1BuildApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Build resource from.
    String sid = "sid_example"; // String | The SID of the Build resource to fetch.
    try {
      ServerlessV1ServiceBuild result = apiInstance.fetchBuild(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1BuildApi#fetchBuild");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Build resource from. | |
| **sid** | **String**| The SID of the Build resource to fetch. | |

### Return type

[**ServerlessV1ServiceBuild**](ServerlessV1ServiceBuild.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listBuild"></a>
# **listBuild**
> ListBuildResponse listBuild(serviceSid, pageSize, page, pageToken)



Retrieve a list of all Builds.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1BuildApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1BuildApi apiInstance = new ServerlessV1BuildApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Build resources from.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListBuildResponse result = apiInstance.listBuild(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1BuildApi#listBuild");
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
| **serviceSid** | **String**| The SID of the Service to read the Build resources from. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListBuildResponse**](ListBuildResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

