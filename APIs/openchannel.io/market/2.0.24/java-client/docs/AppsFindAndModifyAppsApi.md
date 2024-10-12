# AppsFindAndModifyAppsApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsAppIdDelete**](AppsFindAndModifyAppsApi.md#appsAppIdDelete) | **DELETE** /apps/{appId} | Removes app and all versions |
| [**appsAppIdGet**](AppsFindAndModifyAppsApi.md#appsAppIdGet) | **GET** /apps/{appId} | Returns a single APPROVED or SUSPENDED app |
| [**appsAppIdLivePost**](AppsFindAndModifyAppsApi.md#appsAppIdLivePost) | **POST** /apps/{appId}/live | Change the live app to another, previously approved version |
| [**appsAppIdPublishPost**](AppsFindAndModifyAppsApi.md#appsAppIdPublishPost) | **POST** /apps/{appId}/publish | Publishes the current working version of the app to the marketplace |
| [**appsAppIdVersionsVersionDelete**](AppsFindAndModifyAppsApi.md#appsAppIdVersionsVersionDelete) | **DELETE** /apps/{appId}/versions/{version} | Removes AppVersion |
| [**appsAppIdVersionsVersionGet**](AppsFindAndModifyAppsApi.md#appsAppIdVersionsVersionGet) | **GET** /apps/{appId}/versions/{version} | Returns a single AppVersion |
| [**appsAppIdVersionsVersionPatch**](AppsFindAndModifyAppsApi.md#appsAppIdVersionsVersionPatch) | **PATCH** /apps/{appId}/versions/{version} | Updates the app fields or creates a new version |
| [**appsAppIdVersionsVersionPost**](AppsFindAndModifyAppsApi.md#appsAppIdVersionsVersionPost) | **POST** /apps/{appId}/versions/{version} | Updates the app or creates a new version |
| [**appsAppIdVersionsVersionStatusPost**](AppsFindAndModifyAppsApi.md#appsAppIdVersionsVersionStatusPost) | **POST** /apps/{appId}/versions/{version}/status | Allows a developer or administrator to change the status of apps |
| [**appsBySafeNameSafeNameGet**](AppsFindAndModifyAppsApi.md#appsBySafeNameSafeNameGet) | **GET** /apps/bySafeName/{safeName} | Returns a single APPROVED or SUSPENDED app |
| [**appsGet**](AppsFindAndModifyAppsApi.md#appsGet) | **GET** /apps | Returns a paginated list of APPROVED or SUSPENDED apps |
| [**appsPost**](AppsFindAndModifyAppsApi.md#appsPost) | **POST** /apps | Adds a new app for this developer |
| [**appsTextSearchGet**](AppsFindAndModifyAppsApi.md#appsTextSearchGet) | **GET** /apps/textSearch | Searches through the text of fields to find APPROVED or SUSPENDED apps |
| [**appsVersionsGet**](AppsFindAndModifyAppsApi.md#appsVersionsGet) | **GET** /apps/versions | Returns a paginated list of AppVersions |


<a id="appsAppIdDelete"></a>
# **appsAppIdDelete**
> appsAppIdDelete(appId, developerId)

Removes app and all versions

- This method is called on behalf of a developer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the App to be removed
    String developerId = "developerId_example"; // String | The unique id of the developer that is removing this app
    try {
      apiInstance.appsAppIdDelete(appId, developerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsAppIdDelete");
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
| **appId** | **String**| The id of the App to be removed | |
| **developerId** | **String**| The unique id of the developer that is removing this app | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **404** | Not Found - App is not found |  -  |

<a id="appsAppIdGet"></a>
# **appsAppIdGet**
> App appsAppIdGet(appId, userId, trackViews)

Returns a single APPROVED or SUSPENDED app

- A &#39;view&#39; event is recorded when trackViews is set to true 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the App to be located
    String userId = "userId_example"; // String | The unique id of the user that is requesting this resource
    Boolean trackViews = true; // Boolean | Whether this call should be tracked as a 'view' for this app. Default is false.
    try {
      App result = apiInstance.appsAppIdGet(appId, userId, trackViews);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsAppIdGet");
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
| **appId** | **String**| The id of the App to be located | |
| **userId** | **String**| The unique id of the user that is requesting this resource | [optional] |
| **trackViews** | **Boolean**| Whether this call should be tracked as a &#39;view&#39; for this app. Default is false. | [optional] |

### Return type

[**App**](App.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - The App is either restricted or was not found |  -  |
| **0** | OK |  -  |

<a id="appsAppIdLivePost"></a>
# **appsAppIdLivePost**
> appsAppIdLivePost(appId, developerId, version)

Change the live app to another, previously approved version

- This method is called on behalf of a developer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the App to be changed
    String developerId = "developerId_example"; // String | The unique id of the developer that is changing this AppVersion
    String version = "version_example"; // String | The new version of the live App
    try {
      apiInstance.appsAppIdLivePost(appId, developerId, version);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsAppIdLivePost");
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
| **appId** | **String**| The id of the App to be changed | |
| **developerId** | **String**| The unique id of the developer that is changing this AppVersion | |
| **version** | **String**| The new version of the live App | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - App is not found |  -  |

<a id="appsAppIdPublishPost"></a>
# **appsAppIdPublishPost**
> appsAppIdPublishPost(appId, developerId, version, autoApprove)

Publishes the current working version of the app to the marketplace

- This method is called on behalf of a developer.  - Only effects the current working version of the app. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the app to be published
    String developerId = "developerId_example"; // String | The unique id of the developer that is modifying this app
    Integer version = 56; // Integer | The version of the app to be published
    Boolean autoApprove = true; // Boolean | If true, this AppVersion is automatically approved and becomes immediately available to end users
    try {
      apiInstance.appsAppIdPublishPost(appId, developerId, version, autoApprove);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsAppIdPublishPost");
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
| **appId** | **String**| The id of the app to be published | |
| **developerId** | **String**| The unique id of the developer that is modifying this app | |
| **version** | **Integer**| The version of the app to be published | |
| **autoApprove** | **Boolean**| If true, this AppVersion is automatically approved and becomes immediately available to end users | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted - Publishing succeeded but there are restrictions |  -  |
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - App was not found |  -  |
| **409** | Conflict - An app with that name already exists |  -  |

<a id="appsAppIdVersionsVersionDelete"></a>
# **appsAppIdVersionsVersionDelete**
> appsAppIdVersionsVersionDelete(appId, version, developerId)

Removes AppVersion

- This method is called on behalf of a developer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the App to be removed
    String version = "version_example"; // String | The version of the App to be removed
    String developerId = "developerId_example"; // String | The unique id of the developer that is removing this app
    try {
      apiInstance.appsAppIdVersionsVersionDelete(appId, version, developerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsAppIdVersionsVersionDelete");
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
| **appId** | **String**| The id of the App to be removed | |
| **version** | **String**| The version of the App to be removed | |
| **developerId** | **String**| The unique id of the developer that is removing this app | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **404** | Not Found - App is not found |  -  |

<a id="appsAppIdVersionsVersionGet"></a>
# **appsAppIdVersionsVersionGet**
> AppVersion appsAppIdVersionsVersionGet(appId, version, developerId)

Returns a single AppVersion

- Only returns AppVersions owned by this developer 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the App to be located
    Integer version = 56; // Integer | The version number of the app
    String developerId = "developerId_example"; // String | The unique id of the developer that is requesting this resource
    try {
      AppVersion result = apiInstance.appsAppIdVersionsVersionGet(appId, version, developerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsAppIdVersionsVersionGet");
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
| **appId** | **String**| The id of the App to be located | |
| **version** | **Integer**| The version number of the app | |
| **developerId** | **String**| The unique id of the developer that is requesting this resource | [optional] |

### Return type

[**AppVersion**](AppVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - The App or version number was not found |  -  |
| **0** | OK |  -  |

<a id="appsAppIdVersionsVersionPatch"></a>
# **appsAppIdVersionsVersionPatch**
> AppVersion appsAppIdVersionsVersionPatch(appId, version, developerId, name, type, model, customData, attributes, restrict, allow, access, approvalRequired)

Updates the app fields or creates a new version

- This method is called on behalf of a developer. - Price and is required if the model is &#39;single&#39; or &#39;recurring&#39; - Returns the newly updated app - This endpoint updates only the fields provided in the request (relative update). In contrast, the POST version of this method replaces the entire object to match the request (absolute update).  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the App to be updated
    String version = "version_example"; // String | The version of the App to be updated
    String developerId = "developerId_example"; // String | The unique id of the developer that is updating this app
    String name = "name_example"; // String | The name of the app
    String type = "type_example"; // String | The type for this app
    String model = "model_example"; // String | A JSON object representing the pricing model type for this app
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    String attributes = "attributes_example"; // String | A custom set of app attributes defined by the administrator and attached to this app
    String restrict = "restrict_example"; // String | JSON object to restrict users from purchasing or viewing this app. Example: {'view':{'country':['Canada','Mexico']},'purchase':{'country':['Canada','Mexico']}} restricts users from canada and mexico from viewing or purchasing this app
    String allow = "allow_example"; // String | JSON object to allow users to purchase or view this app. Example: {'purchase':{'country':['Canada','Mexico']}} allows only users from canada and mexico to purchase this app
    String access = "access_example"; // String | JSON array of data access requirements
    String approvalRequired = "approvalRequired_example"; // String | False if updates should skip the approval process and be available immediately. Default is True
    try {
      AppVersion result = apiInstance.appsAppIdVersionsVersionPatch(appId, version, developerId, name, type, model, customData, attributes, restrict, allow, access, approvalRequired);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsAppIdVersionsVersionPatch");
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
| **appId** | **String**| The id of the App to be updated | |
| **version** | **String**| The version of the App to be updated | |
| **developerId** | **String**| The unique id of the developer that is updating this app | |
| **name** | **String**| The name of the app | [optional] |
| **type** | **String**| The type for this app | [optional] |
| **model** | **String**| A JSON object representing the pricing model type for this app | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |
| **attributes** | **String**| A custom set of app attributes defined by the administrator and attached to this app | [optional] |
| **restrict** | **String**| JSON object to restrict users from purchasing or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or purchasing this app | [optional] |
| **allow** | **String**| JSON object to allow users to purchase or view this app. Example: {&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} allows only users from canada and mexico to purchase this app | [optional] |
| **access** | **String**| JSON array of data access requirements | [optional] |
| **approvalRequired** | **String**| False if updates should skip the approval process and be available immediately. Default is True | [optional] |

### Return type

[**AppVersion**](AppVersion.md)

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
| **409** | Already Exists - An app with this name already exists |  -  |
| **0** | OK |  -  |

<a id="appsAppIdVersionsVersionPost"></a>
# **appsAppIdVersionsVersionPost**
> AppVersion appsAppIdVersionsVersionPost(appId, version, developerId, name, type, model, customData, attributes, restrict, allow, access, approvalRequired)

Updates the app or creates a new version

- This method is called on behalf of a developer. - Price and is required if the model is &#39;single&#39; or &#39;recurring&#39; - Returns the newly updated app - This endpoint replaces the entire object to match the request (absolute update). In contrast, the PATCH version of this endpoint updates only the fields provided in the request (relative update). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the App to be updated
    String version = "version_example"; // String | The version of the App to be updated
    String developerId = "developerId_example"; // String | The unique id of the developer that is updating this app
    String name = "name_example"; // String | The name of the app
    String type = "type_example"; // String | The type for this app
    String model = "model_example"; // String | A JSON object representing the pricing model type for this app
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    String attributes = "attributes_example"; // String | A custom set of app attributes defined by the administrator and attached to this app
    String restrict = "restrict_example"; // String | JSON object to restrict users from purchasing or viewing this app. Example: {'view':{'country':['Canada','Mexico']},'purchase':{'country':['Canada','Mexico']}} restricts users from canada and mexico from viewing or purchasing this app
    String allow = "allow_example"; // String | JSON object to allow users to purchase or view this app. Example: {'purchase':{'country':['Canada','Mexico']}} allows only users from canada and mexico to purchase this app
    String access = "access_example"; // String | JSON array of data access requirements
    String approvalRequired = "approvalRequired_example"; // String | False if updates should skip the approval process and be available immediately. Default is True
    try {
      AppVersion result = apiInstance.appsAppIdVersionsVersionPost(appId, version, developerId, name, type, model, customData, attributes, restrict, allow, access, approvalRequired);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsAppIdVersionsVersionPost");
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
| **appId** | **String**| The id of the App to be updated | |
| **version** | **String**| The version of the App to be updated | |
| **developerId** | **String**| The unique id of the developer that is updating this app | |
| **name** | **String**| The name of the app | [optional] |
| **type** | **String**| The type for this app | [optional] |
| **model** | **String**| A JSON object representing the pricing model type for this app | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |
| **attributes** | **String**| A custom set of app attributes defined by the administrator and attached to this app | [optional] |
| **restrict** | **String**| JSON object to restrict users from purchasing or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or purchasing this app | [optional] |
| **allow** | **String**| JSON object to allow users to purchase or view this app. Example: {&#39;purchase&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} allows only users from canada and mexico to purchase this app | [optional] |
| **access** | **String**| JSON array of data access requirements | [optional] |
| **approvalRequired** | **String**| False if updates should skip the approval process and be available immediately. Default is True | [optional] |

### Return type

[**AppVersion**](AppVersion.md)

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
| **409** | Already Exists - An app with this name already exists |  -  |
| **0** | OK |  -  |

<a id="appsAppIdVersionsVersionStatusPost"></a>
# **appsAppIdVersionsVersionStatusPost**
> appsAppIdVersionsVersionStatusPost(appId, version, developerId, status, modifiedBy, reason)

Allows a developer or administrator to change the status of apps

Only certain status changes are allowed. For instance, a developer is only able to suspend and unsuspend their app (which must already be approved). See here for a state change diagram of allowed status changes for administrators: https://support.openchannel.io/documentation/api/#415-apps-status-change 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the App to be updated
    Integer version = 56; // Integer | The version of the App to be updated
    String developerId = "developerId_example"; // String | The unique id of the developer that is modifying this app
    String status = "inReview"; // String | The new status for this app. Can be either 'inReview', 'approved', 'suspended' or 'rejected'
    String modifiedBy = "developer"; // String | The role initiating this status change. Can be either 'developer' or 'administrator' (default)
    String reason = "reason_example"; // String | The reason for this status change
    try {
      apiInstance.appsAppIdVersionsVersionStatusPost(appId, version, developerId, status, modifiedBy, reason);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsAppIdVersionsVersionStatusPost");
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
| **appId** | **String**| The id of the App to be updated | |
| **version** | **Integer**| The version of the App to be updated | |
| **developerId** | **String**| The unique id of the developer that is modifying this app | [optional] |
| **status** | **String**| The new status for this app. Can be either &#39;inReview&#39;, &#39;approved&#39;, &#39;suspended&#39; or &#39;rejected&#39; | [optional] [enum: inReview, approved, suspended, rejected] |
| **modifiedBy** | **String**| The role initiating this status change. Can be either &#39;developer&#39; or &#39;administrator&#39; (default) | [optional] [default to administrator] [enum: developer, administrator] |
| **reason** | **String**| The reason for this status change | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - App is not found |  -  |
| **412** | Precondition Failed - The app&#39;s new status is not valid because of the app&#39;s current status |  -  |

<a id="appsBySafeNameSafeNameGet"></a>
# **appsBySafeNameSafeNameGet**
> App appsBySafeNameSafeNameGet(safeName, userId, trackViews)

Returns a single APPROVED or SUSPENDED app

- A &#39;view&#39; event is recorded when trackViews is set to true 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String safeName = "safeName_example"; // String | The safeName of the App to be located
    String userId = "userId_example"; // String | The unique id of the user that is requesting this resource
    Boolean trackViews = true; // Boolean | Whether this call should be tracked as a 'view' for this app. Default is false.
    try {
      App result = apiInstance.appsBySafeNameSafeNameGet(safeName, userId, trackViews);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsBySafeNameSafeNameGet");
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
| **safeName** | **String**| The safeName of the App to be located | |
| **userId** | **String**| The unique id of the user that is requesting this resource | [optional] |
| **trackViews** | **Boolean**| Whether this call should be tracked as a &#39;view&#39; for this app. Default is false. | [optional] |

### Return type

[**App**](App.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - The App is either restricted or was not found |  -  |
| **0** | OK |  -  |

<a id="appsGet"></a>
# **appsGet**
> AppPages appsGet(query, sort, pageNumber, limit, userId, isOwner)

Returns a paginated list of APPROVED or SUSPENDED apps

- Results are paginated and the default is value is 1000 if no limit is provided - If no query is specified, returns all APPROVED or SUSPENDED apps within the marketplace 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String query = "query_example"; // String | A query document. Example: {'name':'MyApp'} matches all the apps that have the name 'MyApp'
    String sort = "sort_example"; // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    String userId = "userId_example"; // String | The unique id of the user requesting this resource
    Boolean isOwner = true; // Boolean | Whether this result should only contain apps that are owned by this user
    try {
      AppPages result = apiInstance.appsGet(query, sort, pageNumber, limit, userId, isOwner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsGet");
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
| **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;MyApp&#39;} matches all the apps that have the name &#39;MyApp&#39; | [optional] |
| **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |
| **userId** | **String**| The unique id of the user requesting this resource | [optional] |
| **isOwner** | **Boolean**| Whether this result should only contain apps that are owned by this user | [optional] |

### Return type

[**AppPages**](AppPages.md)

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

<a id="appsPost"></a>
# **appsPost**
> AppVersion appsPost(developerId, name, type, model, customData, attributes, restrict, allow, access)

Adds a new app for this developer

- This method is called on behalf of a developer. - Price is required if the model is &#39;single&#39; or &#39;recurring&#39; - Returns the newly created app 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String developerId = "developerId_example"; // String | The unique id of the developer that is adding this app
    String name = "name_example"; // String | The name of the app
    String type = "type_example"; // String | The type for this app
    String model = "model_example"; // String | A JSON object representing the pricing model type for this app
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    String attributes = "attributes_example"; // String | A custom set of app attributes defined by the administrator and attached to this app
    String restrict = "restrict_example"; // String | JSON object to restrict users from owning or viewing this app. Example: {'view':{'country':['Canada','Mexico']},'own':{'country':['Canada','Mexico']}} restricts users from canada and mexico from viewing or owning this app
    String allow = "allow_example"; // String | JSON object to restrict users from owning or viewing this app. Example: {'view':{'country':['Canada','Mexico']},'own':{'country':['Canada','Mexico']}} restricts users from canada and mexico from viewing or owning this app
    String access = "access_example"; // String | JSON array of data access requirements
    try {
      AppVersion result = apiInstance.appsPost(developerId, name, type, model, customData, attributes, restrict, allow, access);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsPost");
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
| **developerId** | **String**| The unique id of the developer that is adding this app | |
| **name** | **String**| The name of the app | |
| **type** | **String**| The type for this app | [optional] |
| **model** | **String**| A JSON object representing the pricing model type for this app | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |
| **attributes** | **String**| A custom set of app attributes defined by the administrator and attached to this app | [optional] |
| **restrict** | **String**| JSON object to restrict users from owning or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;own&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or owning this app | [optional] |
| **allow** | **String**| JSON object to restrict users from owning or viewing this app. Example: {&#39;view&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]},&#39;own&#39;:{&#39;country&#39;:[&#39;Canada&#39;,&#39;Mexico&#39;]}} restricts users from canada and mexico from viewing or owning this app | [optional] |
| **access** | **String**| JSON array of data access requirements | [optional] |

### Return type

[**AppVersion**](AppVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **409** | Already Exists - An app with this name already exists |  -  |
| **0** | OK |  -  |

<a id="appsTextSearchGet"></a>
# **appsTextSearchGet**
> SearchPages appsTextSearchGet(text, fields, query, pageNumber, limit, userId, isOwned)

Searches through the text of fields to find APPROVED or SUSPENDED apps

- Results are returned for the market provided within the basic authentication credentials 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String text = "text_example"; // String | The text to search for.
    String fields = "fields_example"; // String | A JSON array containing all the fields to be searched through. Example: ['name', 'customData.description']
    String query = "query_example"; // String | A query document. Example: {'name':'MyApp'} matches all the documents that have the name 'MyApp'
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    String userId = "userId_example"; // String | The unique id of the user requesting this resource
    Boolean isOwned = true; // Boolean | Whether this result should only contain apps that are owned by this user
    try {
      SearchPages result = apiInstance.appsTextSearchGet(text, fields, query, pageNumber, limit, userId, isOwned);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsTextSearchGet");
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
| **text** | **String**| The text to search for. | |
| **fields** | **String**| A JSON array containing all the fields to be searched through. Example: [&#39;name&#39;, &#39;customData.description&#39;] | |
| **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;MyApp&#39;} matches all the documents that have the name &#39;MyApp&#39; | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |
| **userId** | **String**| The unique id of the user requesting this resource | [optional] |
| **isOwned** | **Boolean**| Whether this result should only contain apps that are owned by this user | [optional] |

### Return type

[**SearchPages**](SearchPages.md)

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

<a id="appsVersionsGet"></a>
# **appsVersionsGet**
> VersionPages appsVersionsGet(query, sort, pageNumber, limit, developerId)

Returns a paginated list of AppVersions

- Results are paginated when limit is set, otherwise all results are returned - If no query is specified, returns all AppVersions within the marketplace - Only returns AppVersions owned by this developer 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsFindAndModifyAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppsFindAndModifyAppsApi apiInstance = new AppsFindAndModifyAppsApi(defaultClient);
    String query = "query_example"; // String | A query document. Example: {'name':'MyApp'} matches all the apps that have the name 'MyApp'
    String sort = "sort_example"; // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    String developerId = "developerId_example"; // String | The unique id of the developer requesting this resource
    try {
      VersionPages result = apiInstance.appsVersionsGet(query, sort, pageNumber, limit, developerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsFindAndModifyAppsApi#appsVersionsGet");
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
| **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;MyApp&#39;} matches all the apps that have the name &#39;MyApp&#39; | [optional] |
| **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |
| **developerId** | **String**| The unique id of the developer requesting this resource | [optional] |

### Return type

[**VersionPages**](VersionPages.md)

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

