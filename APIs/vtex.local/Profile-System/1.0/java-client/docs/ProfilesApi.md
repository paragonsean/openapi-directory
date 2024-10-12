# ProfilesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createClientProfile**](ProfilesApi.md#createClientProfile) | **POST** /api/storage/profile-system/profiles | Create client profile |
| [**deleteClientProfile**](ProfilesApi.md#deleteClientProfile) | **DELETE** /api/storage/profile-system/profiles/{profileId} | Delete client profile |
| [**getProfile**](ProfilesApi.md#getProfile) | **GET** /api/storage/profile-system/profiles/{profileId} | Get profile |
| [**getProfileByVersion**](ProfilesApi.md#getProfileByVersion) | **GET** /api/storage/profile-system/profiles/{profileId}/versions/{profileVersionId} | Get profile by version |
| [**getUnmaskedProfile**](ProfilesApi.md#getUnmaskedProfile) | **GET** /api/storage/profile-system/profiles/{profileId}/unmask | Get unmasked profile |
| [**getUnmaskedProfileByVersion**](ProfilesApi.md#getUnmaskedProfileByVersion) | **GET** /api/storage/profile-system/profiles/{profileId}/versions/{profileVersionId}/unmask | Get unmasked profile by version |
| [**updateClientProfile**](ProfilesApi.md#updateClientProfile) | **PATCH** /api/storage/profile-system/profiles/{profileId} | Updates client profile |


<a id="createClientProfile"></a>
# **createClientProfile**
> Object createClientProfile(contentType, accept, ttl, profile)

Create client profile

Creates new client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; The &#x60;id&#x60; field returned by this request is the &#x60;profileId&#x60; used to retrieve information on a specific profile later.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer ttl = 365; // Integer | This parameter sets the the Time To Live (TTL), in days, of the specific document being created or updated with this request. After this period of time from the moment of the request, the document is deleted. By sending this parameter you override the TTL set for the schema.    > Currently, the available default document schemas have no TTL. This means that documents are stored indefinitely, unless a TTL is sent when creating or updating.
    Profile profile = new Profile(); // Profile | 
    try {
      Object result = apiInstance.createClientProfile(contentType, accept, ttl, profile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#createClientProfile");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **ttl** | **Integer**| This parameter sets the the Time To Live (TTL), in days, of the specific document being created or updated with this request. After this period of time from the moment of the request, the document is deleted. By sending this parameter you override the TTL set for the schema.    &gt; Currently, the available default document schemas have no TTL. This means that documents are stored indefinitely, unless a TTL is sent when creating or updating. | [optional] |
| **profile** | [**Profile**](Profile.md)|  | [optional] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteClientProfile"></a>
# **deleteClientProfile**
> deleteClientProfile(contentType, accept, profileId)

Delete client profile

Deletes a client profile by &#x60;profileId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    try {
      apiInstance.deleteClientProfile(contentType, accept, profileId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#deleteClientProfile");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="getProfile"></a>
# **getProfile**
> List&lt;Object&gt; getProfile(contentType, accept, profileId, alternativeKey)

Get profile

Retrieves the information of a specific client, by its &#x60;profileId&#x60;.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; For security and privacy reasons, this request returns masked profile data. For unmasked information, see Get unmasked profile.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    try {
      List<Object> result = apiInstance.getProfile(contentType, accept, profileId, alternativeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getProfile");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | |
| **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getProfileByVersion"></a>
# **getProfileByVersion**
> List&lt;Object&gt; getProfileByVersion(contentType, accept, profileId, profileVersionId)

Get profile by version

Retrieves the information of a specific version of a client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; For security and privacy reasons, this request returns masked profile data. For unmasked information, see Get unmasked profile by version.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String profileVersionId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the version of the client's profile as returned by endpoints that create or update profile information in the `version` field.
    try {
      List<Object> result = apiInstance.getProfileByVersion(contentType, accept, profileId, profileVersionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getProfileByVersion");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | |
| **profileVersionId** | **String**| ID of the version of the client&#39;s profile as returned by endpoints that create or update profile information in the &#x60;version&#x60; field. | |

### Return type

**List&lt;Object&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getUnmaskedProfile"></a>
# **getUnmaskedProfile**
> List&lt;Object&gt; getUnmaskedProfile(contentType, accept, profileId, reason, alternativeKey)

Get unmasked profile

Retrieves unmasked information of a specific client, by its &#x60;profileId&#x60;.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String reason = "data-validation"; // String | Reason for requesting unmasked data.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    try {
      List<Object> result = apiInstance.getUnmaskedProfile(contentType, accept, profileId, reason, alternativeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getUnmaskedProfile");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | |
| **reason** | **String**| Reason for requesting unmasked data. | |
| **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getUnmaskedProfileByVersion"></a>
# **getUnmaskedProfileByVersion**
> List&lt;Object&gt; getUnmaskedProfileByVersion(contentType, accept, profileId, profileVersionId, reason)

Get unmasked profile by version

Retrieves unmasked information of a specific version of a client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String profileVersionId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the version of the client's profile as returned by endpoints that create or update profile information in the `version` field.
    String reason = "data-validation"; // String | Reason for requesting unmasked data.
    try {
      List<Object> result = apiInstance.getUnmaskedProfileByVersion(contentType, accept, profileId, profileVersionId, reason);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#getUnmaskedProfileByVersion");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | |
| **profileVersionId** | **String**| ID of the version of the client&#39;s profile as returned by endpoints that create or update profile information in the &#x60;version&#x60; field. | |
| **reason** | **String**| Reason for requesting unmasked data. | |

### Return type

**List&lt;Object&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateClientProfile"></a>
# **updateClientProfile**
> Object updateClientProfile(contentType, accept, profileId, alternativeKey, ttl, updateClientProfileRequest)

Updates client profile

Updates one or more fields of an existing client profile.    &gt; Since your store&#39;s profile schema is customizable, the schema and examples presented below may differ from yours. Your integration must be adapted accordingly.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    Integer ttl = 365; // Integer | This parameter sets the the Time To Live (TTL), in days, of the specific document being created or updated with this request. After this period of time from the moment of the request, the document is deleted. By sending this parameter you override the TTL set for the schema.    > Currently, the available default document schemas have no TTL. This means that documents are stored indefinitely, unless a TTL is sent when creating or updating.
    UpdateClientProfileRequest updateClientProfileRequest = new UpdateClientProfileRequest(); // UpdateClientProfileRequest | 
    try {
      Object result = apiInstance.updateClientProfile(contentType, accept, profileId, alternativeKey, ttl, updateClientProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#updateClientProfile");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **profileId** | **String**| ID of the client&#39;s profile as returned by the Create profile endpoint&#39;s response, in the &#x60;id&#x60; field. It can also be an &#x60;alternativeKey&#x60; according to your custom profile schema. In this case, this request should also send the &#x60;alternativeKey&#x60; parameter. | |
| **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] |
| **ttl** | **Integer**| This parameter sets the the Time To Live (TTL), in days, of the specific document being created or updated with this request. After this period of time from the moment of the request, the document is deleted. By sending this parameter you override the TTL set for the schema.    &gt; Currently, the available default document schemas have no TTL. This means that documents are stored indefinitely, unless a TTL is sent when creating or updating. | [optional] |
| **updateClientProfileRequest** | [**UpdateClientProfileRequest**](UpdateClientProfileRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

