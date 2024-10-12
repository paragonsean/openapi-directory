# ServerlessV1DeploymentApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeployment**](ServerlessV1DeploymentApi.md#createDeployment) | **POST** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Deployments |  |
| [**fetchDeployment**](ServerlessV1DeploymentApi.md#fetchDeployment) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Deployments/{Sid} |  |
| [**listDeployment**](ServerlessV1DeploymentApi.md#listDeployment) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Deployments |  |


<a id="createDeployment"></a>
# **createDeployment**
> ServerlessV1ServiceEnvironmentDeployment createDeployment(serviceSid, environmentSid, buildSid)



Create a new Deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1DeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1DeploymentApi apiInstance = new ServerlessV1DeploymentApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Deployment resource under.
    String environmentSid = "environmentSid_example"; // String | The SID of the Environment for the Deployment.
    String buildSid = "buildSid_example"; // String | The SID of the Build for the Deployment.
    try {
      ServerlessV1ServiceEnvironmentDeployment result = apiInstance.createDeployment(serviceSid, environmentSid, buildSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1DeploymentApi#createDeployment");
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
| **serviceSid** | **String**| The SID of the Service to create the Deployment resource under. | |
| **environmentSid** | **String**| The SID of the Environment for the Deployment. | |
| **buildSid** | **String**| The SID of the Build for the Deployment. | [optional] |

### Return type

[**ServerlessV1ServiceEnvironmentDeployment**](ServerlessV1ServiceEnvironmentDeployment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchDeployment"></a>
# **fetchDeployment**
> ServerlessV1ServiceEnvironmentDeployment fetchDeployment(serviceSid, environmentSid, sid)



Retrieve a specific Deployment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1DeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1DeploymentApi apiInstance = new ServerlessV1DeploymentApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Deployment resource from.
    String environmentSid = "environmentSid_example"; // String | The SID of the Environment used by the Deployment to fetch.
    String sid = "sid_example"; // String | The SID that identifies the Deployment resource to fetch.
    try {
      ServerlessV1ServiceEnvironmentDeployment result = apiInstance.fetchDeployment(serviceSid, environmentSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1DeploymentApi#fetchDeployment");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Deployment resource from. | |
| **environmentSid** | **String**| The SID of the Environment used by the Deployment to fetch. | |
| **sid** | **String**| The SID that identifies the Deployment resource to fetch. | |

### Return type

[**ServerlessV1ServiceEnvironmentDeployment**](ServerlessV1ServiceEnvironmentDeployment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listDeployment"></a>
# **listDeployment**
> ListDeploymentResponse listDeployment(serviceSid, environmentSid, pageSize, page, pageToken)



Retrieve a list of all Deployments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1DeploymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1DeploymentApi apiInstance = new ServerlessV1DeploymentApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Deployment resources from.
    String environmentSid = "environmentSid_example"; // String | The SID of the Environment used by the Deployment resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDeploymentResponse result = apiInstance.listDeployment(serviceSid, environmentSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1DeploymentApi#listDeployment");
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
| **serviceSid** | **String**| The SID of the Service to read the Deployment resources from. | |
| **environmentSid** | **String**| The SID of the Environment used by the Deployment resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDeploymentResponse**](ListDeploymentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

