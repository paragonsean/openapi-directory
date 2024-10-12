# SourceOauthApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**completeSourceOAuth**](SourceOauthApi.md#completeSourceOAuth) | **POST** /v1/source_oauths/complete_oauth | Given a source def ID generate an access/refresh token etc. |
| [**getSourceOAuthConsent**](SourceOauthApi.md#getSourceOAuthConsent) | **POST** /v1/source_oauths/get_consent_url | Given a source connector definition ID, return the URL to the consent screen where to redirect the user to. |
| [**setInstancewideSourceOauthParams**](SourceOauthApi.md#setInstancewideSourceOauthParams) | **POST** /v1/source_oauths/oauth_params/create | Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector&#39;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#39;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.  |


<a id="completeSourceOAuth"></a>
# **completeSourceOAuth**
> Map&lt;String, Object&gt; completeSourceOAuth(completeSourceOauthRequest)

Given a source def ID generate an access/refresh token etc.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceOauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceOauthApi apiInstance = new SourceOauthApi(defaultClient);
    CompleteSourceOauthRequest completeSourceOauthRequest = new CompleteSourceOauthRequest(); // CompleteSourceOauthRequest | 
    try {
      Map<String, Object> result = apiInstance.completeSourceOAuth(completeSourceOauthRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceOauthApi#completeSourceOAuth");
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
| **completeSourceOauthRequest** | [**CompleteSourceOauthRequest**](CompleteSourceOauthRequest.md)|  | |

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

<a id="getSourceOAuthConsent"></a>
# **getSourceOAuthConsent**
> OAuthConsentRead getSourceOAuthConsent(sourceOauthConsentRequest)

Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceOauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceOauthApi apiInstance = new SourceOauthApi(defaultClient);
    SourceOauthConsentRequest sourceOauthConsentRequest = new SourceOauthConsentRequest(); // SourceOauthConsentRequest | 
    try {
      OAuthConsentRead result = apiInstance.getSourceOAuthConsent(sourceOauthConsentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceOauthApi#getSourceOAuthConsent");
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
| **sourceOauthConsentRequest** | [**SourceOauthConsentRequest**](SourceOauthConsentRequest.md)|  | |

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

<a id="setInstancewideSourceOauthParams"></a>
# **setInstancewideSourceOauthParams**
> setInstancewideSourceOauthParams(setInstancewideSourceOauthParamsRequestBody)

Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector&#39;s configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company&#39;s Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceOauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    SourceOauthApi apiInstance = new SourceOauthApi(defaultClient);
    SetInstancewideSourceOauthParamsRequestBody setInstancewideSourceOauthParamsRequestBody = new SetInstancewideSourceOauthParamsRequestBody(); // SetInstancewideSourceOauthParamsRequestBody | 
    try {
      apiInstance.setInstancewideSourceOauthParams(setInstancewideSourceOauthParamsRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceOauthApi#setInstancewideSourceOauthParams");
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
| **setInstancewideSourceOauthParamsRequestBody** | [**SetInstancewideSourceOauthParamsRequestBody**](SetInstancewideSourceOauthParamsRequestBody.md)|  | |

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

