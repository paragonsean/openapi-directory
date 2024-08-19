# WelcomeApi

All URIs are relative to *https://api.netatmo.net/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addwebhook**](WelcomeApi.md#addwebhook) | **GET** /addwebhook |  |
| [**dropwebhook**](WelcomeApi.md#dropwebhook) | **GET** /dropwebhook |  |
| [**getcamerapicture**](WelcomeApi.md#getcamerapicture) | **GET** /getcamerapicture |  |
| [**geteventsuntil**](WelcomeApi.md#geteventsuntil) | **GET** /geteventsuntil |  |
| [**gethomedata**](WelcomeApi.md#gethomedata) | **GET** /gethomedata |  |
| [**getlasteventof**](WelcomeApi.md#getlasteventof) | **GET** /getlasteventof |  |
| [**getnextevents**](WelcomeApi.md#getnextevents) | **GET** /getnextevents |  |
| [**setpersonsaway**](WelcomeApi.md#setpersonsaway) | **POST** /setpersonsaway |  |
| [**setpersonshome**](WelcomeApi.md#setpersonshome) | **POST** /setpersonshome |  |


<a id="addwebhook"></a>
# **addwebhook**
> NAWelcomeWebhookResponse addwebhook(url, appType)



Links a callback url to a user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WelcomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    WelcomeApi apiInstance = new WelcomeApi(defaultClient);
    String url = "url_example"; // String | Your webhook callback url
    String appType = "appType_example"; // String | Webhooks are only available for Welcome, enter app_camera.
    try {
      NAWelcomeWebhookResponse result = apiInstance.addwebhook(url, appType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WelcomeApi#addwebhook");
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
| **url** | **String**| Your webhook callback url | |
| **appType** | **String**| Webhooks are only available for Welcome, enter app_camera. | |

### Return type

[**NAWelcomeWebhookResponse**](NAWelcomeWebhookResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dropwebhook"></a>
# **dropwebhook**
> NAWelcomeWebhookResponse dropwebhook(appType)



Dissociates a webhook from a user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WelcomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    WelcomeApi apiInstance = new WelcomeApi(defaultClient);
    String appType = "appType_example"; // String | For Welcome, use app_camera
    try {
      NAWelcomeWebhookResponse result = apiInstance.dropwebhook(appType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WelcomeApi#dropwebhook");
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
| **appType** | **String**| For Welcome, use app_camera | |

### Return type

[**NAWelcomeWebhookResponse**](NAWelcomeWebhookResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="getcamerapicture"></a>
# **getcamerapicture**
> byte[] getcamerapicture(imageId, key)



Returns the snapshot associated to an event. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WelcomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    WelcomeApi apiInstance = new WelcomeApi(defaultClient);
    String imageId = "imageId_example"; // String | id of the image (can be retrieved as 'id' in 'face' in Gethomedata, or as 'id' in 'snapshot' in Getnextevents, Getlasteventof and Geteventsuntil)
    String key = "key_example"; // String | Security key to access snapshots.
    try {
      byte[] result = apiInstance.getcamerapicture(imageId, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WelcomeApi#getcamerapicture");
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
| **imageId** | **String**| id of the image (can be retrieved as &#39;id&#39; in &#39;face&#39; in Gethomedata, or as &#39;id&#39; in &#39;snapshot&#39; in Getnextevents, Getlasteventof and Geteventsuntil) | |
| **key** | **String**| Security key to access snapshots. | |

### Return type

**byte[]**

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="geteventsuntil"></a>
# **geteventsuntil**
> NAWelcomeEventResponse geteventsuntil(homeId, eventId)



Returns the snapshot associated to an event. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WelcomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    WelcomeApi apiInstance = new WelcomeApi(defaultClient);
    String homeId = "homeId_example"; // String | ID of the Home you're interested in
    String eventId = "eventId_example"; // String | Your request will retrieve all the events until this one
    try {
      NAWelcomeEventResponse result = apiInstance.geteventsuntil(homeId, eventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WelcomeApi#geteventsuntil");
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
| **homeId** | **String**| ID of the Home you&#39;re interested in | |
| **eventId** | **String**| Your request will retrieve all the events until this one | |

### Return type

[**NAWelcomeEventResponse**](NAWelcomeEventResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="gethomedata"></a>
# **gethomedata**
> NAWelcomeHomeDataResponse gethomedata(homeId, size)



Returns information about users homes and cameras. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WelcomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    WelcomeApi apiInstance = new WelcomeApi(defaultClient);
    String homeId = "homeId_example"; // String | Specify if you're looking for the events of a specific Home.
    Integer size = 56; // Integer | Number of events to retrieve. Default is `30`.
    try {
      NAWelcomeHomeDataResponse result = apiInstance.gethomedata(homeId, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WelcomeApi#gethomedata");
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
| **homeId** | **String**| Specify if you&#39;re looking for the events of a specific Home. | [optional] |
| **size** | **Integer**| Number of events to retrieve. Default is &#x60;30&#x60;. | [optional] |

### Return type

[**NAWelcomeHomeDataResponse**](NAWelcomeHomeDataResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="getlasteventof"></a>
# **getlasteventof**
> NAWelcomeEventResponse getlasteventof(homeId, personId, offset)



Returns most recent events. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WelcomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    WelcomeApi apiInstance = new WelcomeApi(defaultClient);
    String homeId = "homeId_example"; // String | ID of the Home you're interested in
    String personId = "personId_example"; // String | Your request will retrieve all events of the given home until the most recent event of the given person
    Integer offset = 56; // Integer | Number of events to retrieve. Default is 30.
    try {
      NAWelcomeEventResponse result = apiInstance.getlasteventof(homeId, personId, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WelcomeApi#getlasteventof");
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
| **homeId** | **String**| ID of the Home you&#39;re interested in | |
| **personId** | **String**| Your request will retrieve all events of the given home until the most recent event of the given person | |
| **offset** | **Integer**| Number of events to retrieve. Default is 30. | [optional] |

### Return type

[**NAWelcomeEventResponse**](NAWelcomeEventResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="getnextevents"></a>
# **getnextevents**
> NAWelcomeEventResponse getnextevents(homeId, eventId, size)



Returns previous events. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WelcomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    WelcomeApi apiInstance = new WelcomeApi(defaultClient);
    String homeId = "homeId_example"; // String | ID of the Home you're interested in
    String eventId = "eventId_example"; // String | Your request will retrieve events occured before this one
    Integer size = 56; // Integer | Number of events to retrieve. Default is 30.
    try {
      NAWelcomeEventResponse result = apiInstance.getnextevents(homeId, eventId, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WelcomeApi#getnextevents");
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
| **homeId** | **String**| ID of the Home you&#39;re interested in | |
| **eventId** | **String**| Your request will retrieve events occured before this one | |
| **size** | **Integer**| Number of events to retrieve. Default is 30. | [optional] |

### Return type

[**NAWelcomeEventResponse**](NAWelcomeEventResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="setpersonsaway"></a>
# **setpersonsaway**
> NAWelcomePersonsAwayResponse setpersonsaway(homeId, personId)



Sets a person as &#39;Away&#39; or the Home as &#39;Empty&#39;. The event will be added to the user’s timeline. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WelcomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    WelcomeApi apiInstance = new WelcomeApi(defaultClient);
    String homeId = "homeId_example"; // String | ID of the Home you're interested in
    String personId = "personId_example"; // String | If a person_id is specified, that person will be set as 'Away'. If no person_id is specified, the Home will be set as 'Empty'.
    try {
      NAWelcomePersonsAwayResponse result = apiInstance.setpersonsaway(homeId, personId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WelcomeApi#setpersonsaway");
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
| **homeId** | **String**| ID of the Home you&#39;re interested in | |
| **personId** | **String**| If a person_id is specified, that person will be set as &#39;Away&#39;. If no person_id is specified, the Home will be set as &#39;Empty&#39;. | [optional] |

### Return type

[**NAWelcomePersonsAwayResponse**](NAWelcomePersonsAwayResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="setpersonshome"></a>
# **setpersonshome**
> NAWelcomePersonsHomeResponse setpersonshome(homeId, personIds)



Sets a person as &#39;At home&#39;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WelcomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    WelcomeApi apiInstance = new WelcomeApi(defaultClient);
    String homeId = "homeId_example"; // String | ID of the Home you're interested in
    String personIds = "personIds_example"; // String | List of persons IDs
    try {
      NAWelcomePersonsHomeResponse result = apiInstance.setpersonshome(homeId, personIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WelcomeApi#setpersonshome");
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
| **homeId** | **String**| ID of the Home you&#39;re interested in | |
| **personIds** | **String**| List of persons IDs | |

### Return type

[**NAWelcomePersonsHomeResponse**](NAWelcomePersonsHomeResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

