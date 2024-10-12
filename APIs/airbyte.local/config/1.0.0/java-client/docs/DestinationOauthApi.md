# DestinationOauthApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**completeDestinationOAuth**](DestinationOauthApi.md#completeDestinationOAuth) | **POST** /v1/destination_oauths/complete_oauth | Given a destination def ID generate an access/refresh token etc. |
| [**getDestinationOAuthConsent**](DestinationOauthApi.md#getDestinationOAuthConsent) | **POST** /v1/destination_oauths/get_consent_url | Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to. |
| [**setInstancewideDestinationOauthParams**](DestinationOauthApi.md#setInstancewideDestinationOauthParams) | **POST** /v1/destination_oauths/oauth_params/create | Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector&#39;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#39;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.  |


<a id="completeDestinationOAuth"></a>
# **completeDestinationOAuth**
> Map&lt;String, Object&gt; completeDestinationOAuth(completeDestinationOAuthRequest)

Given a destination def ID generate an access/refresh token etc.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationOauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationOauthApi apiInstance = new DestinationOauthApi(defaultClient);
    CompleteDestinationOAuthRequest completeDestinationOAuthRequest = new CompleteDestinationOAuthRequest(); // CompleteDestinationOAuthRequest | 
    try {
      Map<String, Object> result = apiInstance.completeDestinationOAuth(completeDestinationOAuthRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationOauthApi#completeDestinationOAuth");
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
| **completeDestinationOAuthRequest** | [**CompleteDestinationOAuthRequest**](CompleteDestinationOAuthRequest.md)|  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getDestinationOAuthConsent"></a>
# **getDestinationOAuthConsent**
> OAuthConsentRead getDestinationOAuthConsent(destinationOauthConsentRequest)

Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationOauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationOauthApi apiInstance = new DestinationOauthApi(defaultClient);
    DestinationOauthConsentRequest destinationOauthConsentRequest = new DestinationOauthConsentRequest(); // DestinationOauthConsentRequest | 
    try {
      OAuthConsentRead result = apiInstance.getDestinationOAuthConsent(destinationOauthConsentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationOauthApi#getDestinationOAuthConsent");
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
| **destinationOauthConsentRequest** | [**DestinationOauthConsentRequest**](DestinationOauthConsentRequest.md)|  | |

### Return type

[**OAuthConsentRead**](OAuthConsentRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="setInstancewideDestinationOauthParams"></a>
# **setInstancewideDestinationOauthParams**
> setInstancewideDestinationOauthParams(setInstancewideDestinationOauthParamsRequestBody)

Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector&#39;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#39;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DestinationOauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    DestinationOauthApi apiInstance = new DestinationOauthApi(defaultClient);
    SetInstancewideDestinationOauthParamsRequestBody setInstancewideDestinationOauthParamsRequestBody = new SetInstancewideDestinationOauthParamsRequestBody(); // SetInstancewideDestinationOauthParamsRequestBody | 
    try {
      apiInstance.setInstancewideDestinationOauthParams(setInstancewideDestinationOauthParamsRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling DestinationOauthApi#setInstancewideDestinationOauthParams");
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
| **setInstancewideDestinationOauthParamsRequestBody** | [**SetInstancewideDestinationOauthParamsRequestBody**](SetInstancewideDestinationOauthParamsRequestBody.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **400** | Exception occurred; see message for details. |  -  |
| **404** | Object with given id was not found. |  -  |

