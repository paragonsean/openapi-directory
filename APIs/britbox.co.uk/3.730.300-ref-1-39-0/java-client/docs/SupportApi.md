# SupportApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**forgotPassword**](SupportApi.md#forgotPassword) | **POST** /request-password-reset |  |
| [**getSubscriptionData**](SupportApi.md#getSubscriptionData) | **GET** /check-subscription/{id} |  |
| [**resetPassword**](SupportApi.md#resetPassword) | **POST** /reset-password |  |
| [**verifyEmail**](SupportApi.md#verifyEmail) | **POST** /verify-email |  |


<a id="forgotPassword"></a>
# **forgotPassword**
> forgotPassword(passwordResetEmailRequest, ff, lang)



Request the password of an account&#39;s primary profile be reset.  Should be called when a user has forgotten their password.  This will send an email with a password reset link to the email address of the primary profile of an account.  The link, once clicked, should take the user to the \&quot;reset-password\&quot; page of the website. Here they will enter their new password and submit to the /reset-password endpoint here, along with the password reset token provided in the original link. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SupportApi apiInstance = new SupportApi(defaultClient);
    PasswordResetEmailRequest passwordResetEmailRequest = new PasswordResetEmailRequest(); // PasswordResetEmailRequest | Email address of account to request a password reset on.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.forgotPassword(passwordResetEmailRequest, ff, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#forgotPassword");
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
| **passwordResetEmailRequest** | [**PasswordResetEmailRequest**](PasswordResetEmailRequest.md)| Email address of account to request a password reset on. | |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

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
| **204** | OK |  -  |
| **400** | Bad request. |  -  |
| **401** | Invalid access token. |  -  |
| **403** | Forbidden. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="getSubscriptionData"></a>
# **getSubscriptionData**
> SubscriptionDetails getSubscriptionData(id)



Returns the details of subscription data for a user with specified id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SupportApi apiInstance = new SupportApi(defaultClient);
    String id = "id_example"; // String | The identifier of the user to load. 
    try {
      SubscriptionDetails result = apiInstance.getSubscriptionData(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#getSubscriptionData");
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
| **id** | **String**| The identifier of the user to load.  | |

### Return type

[**SubscriptionDetails**](SubscriptionDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The data requested |  -  |
| **400** | Bad request. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="resetPassword"></a>
# **resetPassword**
> resetPassword(passwordResetRequest, ff, lang)



When a user requests to reset their password via the /request-password-reset endpoint, an email is sent to the email address of the primary profile of the account. This email contains a link with a reset token as query parameter. The link should take the user to the \&quot;reset-password\&quot; page of the website.  From the reset-password page a user should enter the new password they wish to use.  It should then be submitted to this endpoint, along with the reset token from the email link.  The token should be provided in the body as resetToken property. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    SupportApi apiInstance = new SupportApi(defaultClient);
    PasswordResetRequest passwordResetRequest = new PasswordResetRequest(); // PasswordResetRequest | ITV reset token from email link and a new password.
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.resetPassword(passwordResetRequest, ff, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#resetPassword");
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
| **passwordResetRequest** | [**PasswordResetRequest**](PasswordResetRequest.md)| ITV reset token from email link and a new password. | |
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

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
| **204** | OK |  -  |
| **400** | Bad request. |  -  |
| **401** | Invalid access token. |  -  |
| **403** | Forbidden. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

<a id="verifyEmail"></a>
# **verifyEmail**
> verifyEmail(ff, lang)



When an account is created an email is sent to the email address of the new account. This contains a link, which once clicked, verifies the email address of the account is correct.  The link contains a token as a query parameter which should be passed as the authorization bearer token to this endpoint to complete email verification.  The token has en expiry, so if the link is not clicked before it expires, the account holder may need to request a new verification email be sent. This can be done via the endpoint /account/request-email-verification. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure API key authorization: verifyEmailAuth
    ApiKeyAuth verifyEmailAuth = (ApiKeyAuth) defaultClient.getAuthentication("verifyEmailAuth");
    verifyEmailAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //verifyEmailAuth.setApiKeyPrefix("Token");

    SupportApi apiInstance = new SupportApi(defaultClient);
    List<String> ff = Arrays.asList(); // List<String> | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
    String lang = "lang_example"; // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
    try {
      apiInstance.verifyEmail(ff, lang);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupportApi#verifyEmail");
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
| **ff** | [**List&lt;String&gt;**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] [enum: all, idp, ldp, hb, rpt, cas, lrl, cd] |
| **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] |

### Return type

null (empty response body)

### Authorization

[verifyEmailAuth](../README.md#verifyEmailAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Bad request. |  -  |
| **401** | Invalid access token. |  -  |
| **403** | Forbidden. |  -  |
| **404** | Not found. |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal server error. |  -  |
| **0** | Service error. |  -  |

