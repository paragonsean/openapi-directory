# OwnershipFindOwnershipApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ownershipGet**](OwnershipFindOwnershipApi.md#ownershipGet) | **GET** /ownership | Returns a paginated list of app licenses |
| [**ownershipInstallPost**](OwnershipFindOwnershipApi.md#ownershipInstallPost) | **POST** /ownership/install | Aquires an app license for a user (installs app) |
| [**ownershipOwnershipIdGet**](OwnershipFindOwnershipApi.md#ownershipOwnershipIdGet) | **GET** /ownership/{ownershipId} | Returns an ownership record |
| [**ownershipOwnershipIdPatch**](OwnershipFindOwnershipApi.md#ownershipOwnershipIdPatch) | **PATCH** /ownership/{ownershipId} | Updates ownership fields |
| [**ownershipOwnershipIdPost**](OwnershipFindOwnershipApi.md#ownershipOwnershipIdPost) | **POST** /ownership/{ownershipId} | Updates an ownership record |
| [**ownershipUninstallOwnershipIdPost**](OwnershipFindOwnershipApi.md#ownershipUninstallOwnershipIdPost) | **POST** /ownership/uninstall/{ownershipId} | Uninstalls a license for a particular user and app (uninstalls app) |


<a id="ownershipGet"></a>
# **ownershipGet**
> OwnershipPages ownershipGet(query, sort, pageNumber, limit)

Returns a paginated list of app licenses

 - Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OwnershipFindOwnershipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    OwnershipFindOwnershipApi apiInstance = new OwnershipFindOwnershipApi(defaultClient);
    String query = "query_example"; // String | A query document. Example: {'userId':'12'} matches all the ownership records that have the userId '12'.
    String sort = "sort_example"; // String | A sort document. Example: {'date':1} sorts the results by date in ascending order
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    try {
      OwnershipPages result = apiInstance.ownershipGet(query, sort, pageNumber, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OwnershipFindOwnershipApi#ownershipGet");
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
| **query** | **String**| A query document. Example: {&#39;userId&#39;:&#39;12&#39;} matches all the ownership records that have the userId &#39;12&#39;. | [optional] |
| **sort** | **String**| A sort document. Example: {&#39;date&#39;:1} sorts the results by date in ascending order | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |

### Return type

[**OwnershipPages**](OwnershipPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="ownershipInstallPost"></a>
# **ownershipInstallPost**
> Ownership ownershipInstallPost(appId, userId, modelId, model, customData)

Aquires an app license for a user (installs app)

 - This method is called on behalf of a user - This method requires either a modelId from the app or a custom model - User data and statistics are recorded when this method is called 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OwnershipFindOwnershipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    OwnershipFindOwnershipApi apiInstance = new OwnershipFindOwnershipApi(defaultClient);
    String appId = "appId_example"; // String | The id of the App being owned
    String userId = "userId_example"; // String | The id of the User requesting to own the App
    String modelId = "modelId_example"; // String | The id of the model associated with this ownership request
    String model = "model_example"; // String | A custom model that will override the app's default model for this install
    String customData = "customData_example"; // String | A custom JSON object to attach to this ownership record
    try {
      Ownership result = apiInstance.ownershipInstallPost(appId, userId, modelId, model, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OwnershipFindOwnershipApi#ownershipInstallPost");
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
| **appId** | **String**| The id of the App being owned | |
| **userId** | **String**| The id of the User requesting to own the App | |
| **modelId** | **String**| The id of the model associated with this ownership request | [optional] |
| **model** | **String**| A custom model that will override the app&#39;s default model for this install | [optional] |
| **customData** | **String**| A custom JSON object to attach to this ownership record | [optional] |

### Return type

[**Ownership**](Ownership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **402** | Payment Required - The App requires a user with pre-set payment details |  -  |
| **404** | Not Found - The App is either restricted or was not found |  -  |
| **409** | Already Exists - The User already owns this app (or is already participating in a trial) |  -  |
| **412** | Payment Failed - The User&#39;s payment details are invalid |  -  |
| **0** | OK |  -  |

<a id="ownershipOwnershipIdGet"></a>
# **ownershipOwnershipIdGet**
> Ownership ownershipOwnershipIdGet(ownershipId)

Returns an ownership record

 - Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OwnershipFindOwnershipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    OwnershipFindOwnershipApi apiInstance = new OwnershipFindOwnershipApi(defaultClient);
    String ownershipId = "ownershipId_example"; // String | The id belonging to the ownership record
    try {
      Ownership result = apiInstance.ownershipOwnershipIdGet(ownershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OwnershipFindOwnershipApi#ownershipOwnershipIdGet");
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
| **ownershipId** | **String**| The id belonging to the ownership record | |

### Return type

[**Ownership**](Ownership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="ownershipOwnershipIdPatch"></a>
# **ownershipOwnershipIdPatch**
> Ownership ownershipOwnershipIdPatch(ownershipId, customData, expires)

Updates ownership fields

 - Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OwnershipFindOwnershipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    OwnershipFindOwnershipApi apiInstance = new OwnershipFindOwnershipApi(defaultClient);
    String ownershipId = "ownershipId_example"; // String | The id of the ownership to be updated
    String customData = "customData_example"; // String | Custom JSON object that will be attached to this ownership record
    Long expires = 56L; // Long | The date (in millis) of when this app ownership expires
    try {
      Ownership result = apiInstance.ownershipOwnershipIdPatch(ownershipId, customData, expires);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OwnershipFindOwnershipApi#ownershipOwnershipIdPatch");
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
| **ownershipId** | **String**| The id of the ownership to be updated | |
| **customData** | **String**| Custom JSON object that will be attached to this ownership record | [optional] |
| **expires** | **Long**| The date (in millis) of when this app ownership expires | [optional] |

### Return type

[**Ownership**](Ownership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - The ownership was not found |  -  |
| **0** | OK |  -  |

<a id="ownershipOwnershipIdPost"></a>
# **ownershipOwnershipIdPost**
> Ownership ownershipOwnershipIdPost(ownershipId, customData, expires)

Updates an ownership record

 - Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OwnershipFindOwnershipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    OwnershipFindOwnershipApi apiInstance = new OwnershipFindOwnershipApi(defaultClient);
    String ownershipId = "ownershipId_example"; // String | The id of the ownership to be updated
    String customData = "customData_example"; // String | Custom JSON object that will be attached to this ownership record
    Long expires = 56L; // Long | The date (in millis) of when this app ownership expires
    try {
      Ownership result = apiInstance.ownershipOwnershipIdPost(ownershipId, customData, expires);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OwnershipFindOwnershipApi#ownershipOwnershipIdPost");
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
| **ownershipId** | **String**| The id of the ownership to be updated | |
| **customData** | **String**| Custom JSON object that will be attached to this ownership record | [optional] |
| **expires** | **Long**| The date (in millis) of when this app ownership expires | [optional] |

### Return type

[**Ownership**](Ownership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="ownershipUninstallOwnershipIdPost"></a>
# **ownershipUninstallOwnershipIdPost**
> Ownership ownershipUninstallOwnershipIdPost(ownershipId, userId, cancelOwnership, customData)

Uninstalls a license for a particular user and app (uninstalls app)

 - This method is called on behalf of a user - User data and statistics are recorded when this method is called 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OwnershipFindOwnershipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    OwnershipFindOwnershipApi apiInstance = new OwnershipFindOwnershipApi(defaultClient);
    String ownershipId = "ownershipId_example"; // String | The id of the ownership to be unintalled
    String userId = "userId_example"; // String | The id of the User requesting to uninstall the App
    Boolean cancelOwnership = true; // Boolean | True if this app will require payment to be re-installed. Default is false
    String customData = "customData_example"; // String | A custom JSON object to attach to this ownership record
    try {
      Ownership result = apiInstance.ownershipUninstallOwnershipIdPost(ownershipId, userId, cancelOwnership, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OwnershipFindOwnershipApi#ownershipUninstallOwnershipIdPost");
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
| **ownershipId** | **String**| The id of the ownership to be unintalled | |
| **userId** | **String**| The id of the User requesting to uninstall the App | |
| **cancelOwnership** | **Boolean**| True if this app will require payment to be re-installed. Default is false | [optional] |
| **customData** | **String**| A custom JSON object to attach to this ownership record | [optional] |

### Return type

[**Ownership**](Ownership.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - App is not found |  -  |
| **409** | App is not owned by this user |  -  |
| **0** | OK |  -  |

