# ApplicationApi

All URIs are relative to *https://graph.windows.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationsCreate**](ApplicationApi.md#applicationsCreate) | **POST** /{tenantID}/applications |  |
| [**applicationsDelete**](ApplicationApi.md#applicationsDelete) | **DELETE** /{tenantID}/applications/{applicationObjectId} |  |
| [**applicationsGet**](ApplicationApi.md#applicationsGet) | **GET** /{tenantID}/applications/{applicationObjectId} |  |
| [**applicationsList**](ApplicationApi.md#applicationsList) | **GET** /{tenantID}/applications |  |
| [**applicationsPatch**](ApplicationApi.md#applicationsPatch) | **PATCH** /{tenantID}/applications/{applicationObjectId} |  |
| [**deletedApplicationsHardDelete**](ApplicationApi.md#deletedApplicationsHardDelete) | **DELETE** /{tenantID}/deletedApplications/{applicationObjectId} |  |


<a id="applicationsCreate"></a>
# **applicationsCreate**
> Application applicationsCreate(apiVersion, tenantID, applicationCreateParameters)



Create a new application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    ApplicationCreateParameters applicationCreateParameters = new ApplicationCreateParameters(); // ApplicationCreateParameters | The parameters for creating an application.
    try {
      Application result = apiInstance.applicationsCreate(apiVersion, tenantID, applicationCreateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationsCreate");
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
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **applicationCreateParameters** | [**ApplicationCreateParameters**](ApplicationCreateParameters.md)| The parameters for creating an application. | |

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The application was created successfully. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applicationsDelete"></a>
# **applicationsDelete**
> applicationsDelete(applicationObjectId, apiVersion, tenantID)



Delete an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      apiInstance.applicationsDelete(applicationObjectId, apiVersion, tenantID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationsDelete");
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
| **applicationObjectId** | **String**| Application object ID. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applicationsGet"></a>
# **applicationsGet**
> Application applicationsGet(applicationObjectId, apiVersion, tenantID)



Get an application by object ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      Application result = apiInstance.applicationsGet(applicationObjectId, apiVersion, tenantID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationsGet");
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
| **applicationObjectId** | **String**| Application object ID. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applicationsList"></a>
# **applicationsList**
> ApplicationListResult applicationsList(apiVersion, tenantID, $filter)



Lists applications by filter parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    String $filter = "$filter_example"; // String | The filters to apply to the operation.
    try {
      ApplicationListResult result = apiInstance.applicationsList(apiVersion, tenantID, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationsList");
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
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **$filter** | **String**| The filters to apply to the operation. | [optional] |

### Return type

[**ApplicationListResult**](ApplicationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The operation was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="applicationsPatch"></a>
# **applicationsPatch**
> applicationsPatch(applicationObjectId, apiVersion, tenantID, applicationUpdateParameters)



Update an existing application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    ApplicationUpdateParameters applicationUpdateParameters = new ApplicationUpdateParameters(); // ApplicationUpdateParameters | Parameters to update an existing application.
    try {
      apiInstance.applicationsPatch(applicationObjectId, apiVersion, tenantID, applicationUpdateParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationsPatch");
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
| **applicationObjectId** | **String**| Application object ID. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |
| **applicationUpdateParameters** | [**ApplicationUpdateParameters**](ApplicationUpdateParameters.md)| Parameters to update an existing application. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="deletedApplicationsHardDelete"></a>
# **deletedApplicationsHardDelete**
> deletedApplicationsHardDelete(applicationObjectId, apiVersion, tenantID)



Hard-delete an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graph.windows.net");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String applicationObjectId = "applicationObjectId_example"; // String | Application object ID.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String tenantID = "tenantID_example"; // String | The tenant ID.
    try {
      apiInstance.deletedApplicationsHardDelete(applicationObjectId, apiVersion, tenantID);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#deletedApplicationsHardDelete");
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
| **applicationObjectId** | **String**| Application object ID. | |
| **apiVersion** | **String**| Client API version. | |
| **tenantID** | **String**| The tenant ID. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

