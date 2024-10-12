# LongviewApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createLongviewClient**](LongviewApi.md#createLongviewClient) | **POST** /longview/clients | Longview Client Create |
| [**deleteLongviewClient**](LongviewApi.md#deleteLongviewClient) | **DELETE** /longview/clients/{clientId} | Longview Client Delete |
| [**getLongviewClient**](LongviewApi.md#getLongviewClient) | **GET** /longview/clients/{clientId} | Longview Client View |
| [**getLongviewClients**](LongviewApi.md#getLongviewClients) | **GET** /longview/clients | Longview Clients List |
| [**getLongviewPlan**](LongviewApi.md#getLongviewPlan) | **GET** /longview/plan | Longview Plan View |
| [**getLongviewSubscription**](LongviewApi.md#getLongviewSubscription) | **GET** /longview/subscriptions/{subscriptionId} | Longview Subscription View |
| [**getLongviewSubscriptions**](LongviewApi.md#getLongviewSubscriptions) | **GET** /longview/subscriptions | Longview Subscriptions List |
| [**updateLongviewClient**](LongviewApi.md#updateLongviewClient) | **PUT** /longview/clients/{clientId} | Longview Client Update |
| [**updateLongviewPlan**](LongviewApi.md#updateLongviewPlan) | **PUT** /longview/plan | Longview Plan Update |


<a id="createLongviewClient"></a>
# **createLongviewClient**
> LongviewClient createLongviewClient(longviewClient)

Longview Client Create

Creates a Longview Client.  This Client will not begin monitoring the status of your server until you configure the Longview Client application on your Linode using the returning &#x60;install_code&#x60; and &#x60;api_key&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LongviewApi apiInstance = new LongviewApi(defaultClient);
    LongviewClient longviewClient = new LongviewClient(); // LongviewClient | Information about the LongviewClient to create.
    try {
      LongviewClient result = apiInstance.createLongviewClient(longviewClient);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongviewApi#createLongviewClient");
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
| **longviewClient** | [**LongviewClient**](LongviewClient.md)| Information about the LongviewClient to create. | |

### Return type

[**LongviewClient**](LongviewClient.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Longview Client created successfully. |  -  |
| **0** | Error |  -  |

<a id="deleteLongviewClient"></a>
# **deleteLongviewClient**
> Object deleteLongviewClient(clientId)

Longview Client Delete

Deletes a Longview Client from your Account.  **All information stored for this client will be lost.**  This _does not_ uninstall the Longview Client application for your Linode - you must do that manually. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LongviewApi apiInstance = new LongviewApi(defaultClient);
    Integer clientId = 56; // Integer | The Longview Client ID to access.
    try {
      Object result = apiInstance.deleteLongviewClient(clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongviewApi#deleteLongviewClient");
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
| **clientId** | **Integer**| The Longview Client ID to access. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Longview Client deleted successfully. |  -  |
| **0** | Error |  -  |

<a id="getLongviewClient"></a>
# **getLongviewClient**
> LongviewClient getLongviewClient(clientId)

Longview Client View

Returns a single Longview Client you can access. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LongviewApi apiInstance = new LongviewApi(defaultClient);
    Integer clientId = 56; // Integer | The Longview Client ID to access.
    try {
      LongviewClient result = apiInstance.getLongviewClient(clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongviewApi#getLongviewClient");
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
| **clientId** | **Integer**| The Longview Client ID to access. | |

### Return type

[**LongviewClient**](LongviewClient.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Longview Client. |  -  |
| **0** | Error |  -  |

<a id="getLongviewClients"></a>
# **getLongviewClients**
> GetLongviewClients200Response getLongviewClients(page, pageSize)

Longview Clients List

Returns a paginated list of Longview Clients you have access to. Longview Client is used to monitor stats on your Linode with the help of the Longview Client application. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LongviewApi apiInstance = new LongviewApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetLongviewClients200Response result = apiInstance.getLongviewClients(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongviewApi#getLongviewClients");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetLongviewClients200Response**](GetLongviewClients200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of Longview Clients. |  -  |
| **0** | Error |  -  |

<a id="getLongviewPlan"></a>
# **getLongviewPlan**
> LongviewSubscription getLongviewPlan()

Longview Plan View

Get the details of your current Longview plan. This returns a &#x60;LongviewSubscription&#x60; object for your current Longview Pro plan, or an empty set &#x60;{}&#x60; if your current plan is Longview Free.  You must have at least one of the following &#x60;global&#x60; [User Grants](/docs/api/account/#users-grants-view) in order to access this endpoint:    - &#x60;\&quot;account_access\&quot;: read_write&#x60;   - &#x60;\&quot;account_access\&quot;: read_only&#x60;   - &#x60;\&quot;longview_subscription\&quot;: true&#x60;   - &#x60;\&quot;add_longview\&quot;: true&#x60;   To update your subscription plan, send a request to [Update Longview Plan](/docs/api/longview/#longview-plan-update). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LongviewApi apiInstance = new LongviewApi(defaultClient);
    try {
      LongviewSubscription result = apiInstance.getLongviewPlan();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongviewApi#getLongviewPlan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LongviewSubscription**](LongviewSubscription.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Longview plan details for this account. |  -  |
| **0** | Error |  -  |

<a id="getLongviewSubscription"></a>
# **getLongviewSubscription**
> LongviewSubscription getLongviewSubscription(subscriptionId)

Longview Subscription View

Get the Longview plan details as a single &#x60;LongviewSubscription&#x60; object for the provided subscription ID. This is a public endpoint and requires no authentication. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    LongviewApi apiInstance = new LongviewApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Longview Subscription to look up.
    try {
      LongviewSubscription result = apiInstance.getLongviewSubscription(subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongviewApi#getLongviewSubscription");
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
| **subscriptionId** | **String**| The Longview Subscription to look up. | |

### Return type

[**LongviewSubscription**](LongviewSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Longview Subscription details. |  -  |
| **0** | Error |  -  |

<a id="getLongviewSubscriptions"></a>
# **getLongviewSubscriptions**
> GetLongviewSubscriptions200Response getLongviewSubscriptions(page, pageSize)

Longview Subscriptions List

Returns a paginated list of available Longview Subscriptions. This is a public endpoint and requires no authentication. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    LongviewApi apiInstance = new LongviewApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetLongviewSubscriptions200Response result = apiInstance.getLongviewSubscriptions(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongviewApi#getLongviewSubscriptions");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetLongviewSubscriptions200Response**](GetLongviewSubscriptions200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of Longview Subscriptions. |  -  |
| **0** | Error |  -  |

<a id="updateLongviewClient"></a>
# **updateLongviewClient**
> LongviewClient updateLongviewClient(clientId, longviewClient)

Longview Client Update

Updates a Longview Client.  This cannot update how it monitors your server; use the Longview Client application on your Linode for monitoring configuration. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LongviewApi apiInstance = new LongviewApi(defaultClient);
    Integer clientId = 56; // Integer | The Longview Client ID to access.
    LongviewClient longviewClient = new LongviewClient(); // LongviewClient | The fields to update.
    try {
      LongviewClient result = apiInstance.updateLongviewClient(clientId, longviewClient);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongviewApi#updateLongviewClient");
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
| **clientId** | **Integer**| The Longview Client ID to access. | |
| **longviewClient** | [**LongviewClient**](LongviewClient.md)| The fields to update. | |

### Return type

[**LongviewClient**](LongviewClient.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Longview Client updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateLongviewPlan"></a>
# **updateLongviewPlan**
> LongviewSubscription updateLongviewPlan(longviewPlan)

Longview Plan Update

Update your Longview plan to that of the given subcription ID. This returns a &#x60;LongviewSubscription&#x60; object for the updated Longview Pro plan, or an empty set &#x60;{}&#x60; if the updated plan is Longview Free.  You must have &#x60;\&quot;longview_subscription\&quot;: true&#x60; configured as a &#x60;global&#x60; [User Grant](/docs/api/account/#users-grants-view) in order to access this endpoint.  You can send a request to the [List Longview Subscriptions](/docs/api/longview/#longview-subscriptions-list) endpoint to receive the details, including &#x60;id&#x60;&#39;s, of each plan. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LongviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LongviewApi apiInstance = new LongviewApi(defaultClient);
    LongviewPlan longviewPlan = new LongviewPlan(); // LongviewPlan | Update your Longview subscription plan.
    try {
      LongviewSubscription result = apiInstance.updateLongviewPlan(longviewPlan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LongviewApi#updateLongviewPlan");
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
| **longviewPlan** | [**LongviewPlan**](LongviewPlan.md)| Update your Longview subscription plan. | |

### Return type

[**LongviewSubscription**](LongviewSubscription.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated Longview plan details for this account. |  -  |
| **0** | Error |  -  |

