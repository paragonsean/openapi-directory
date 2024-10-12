# AddressesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createClientAddress**](AddressesApi.md#createClientAddress) | **POST** /api/storage/profile-system/profiles/{profileId}/addresses | Create client address |
| [**deleteAddress**](AddressesApi.md#deleteAddress) | **DELETE** /api/storage/profile-system/profiles/{profileId}/addresses/{addressId} | Delete address |
| [**getAddress**](AddressesApi.md#getAddress) | **GET** /api/storage/profile-system/profiles/{profileId}/addresses/{addressId} | Get address |
| [**getAddressByVersion**](AddressesApi.md#getAddressByVersion) | **GET** /api/storage/profile-system/profiles/{profileId}/addresses/{addressId}/versions/{addressVersionId} | Get address by version |
| [**getClientAddresses**](AddressesApi.md#getClientAddresses) | **GET** /api/storage/profile-system/profiles/{profileId}/addresses | Get client addresses |
| [**getUnmaskedAddress**](AddressesApi.md#getUnmaskedAddress) | **GET** /api/storage/profile-system/profiles/{profileId}/addresses/{addressId}/unmask | Get unmasked address |
| [**getUnmaskedAddressByVersion**](AddressesApi.md#getUnmaskedAddressByVersion) | **GET** /api/storage/profile-system/profiles/{profileId}/addresses/{addressId}/versions/{addressVersionId}/unmask | Get unmasked address by version |
| [**getUnmaskedClientAddresses**](AddressesApi.md#getUnmaskedClientAddresses) | **GET** /api/storage/profile-system/profiles/{profileId}/addresses/unmask | Get unmasked client addresses |
| [**updateClientAddress**](AddressesApi.md#updateClientAddress) | **PATCH** /api/storage/profile-system/profiles/{profileId}/addresses/{addressId} | Update client address |


<a id="createClientAddress"></a>
# **createClientAddress**
> Object createClientAddress(contentType, accept, profileId, alternativeKey, address)

Create client address

Creates new address for a given client profile.    &gt; The &#x60;id&#x60; field returned by this request is the &#x60;addressId&#x60; used to retrieve or update information of a specific address later.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

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

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    Address address = new Address(); // Address | 
    try {
      Object result = apiInstance.createClientAddress(contentType, accept, profileId, alternativeKey, address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#createClientAddress");
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
| **address** | [**Address**](Address.md)|  | [optional] |

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

<a id="deleteAddress"></a>
# **deleteAddress**
> deleteAddress(contentType, accept, profileId, addressId, alternativeKey)

Delete address

Deletes a client&#39;s address by &#x60;profileId&#x60; and &#x60;addressId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

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

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String addressId = "bf82180e-cf9e-4089-9af6-ae1518555992"; // String | ID of a client's specific address as returned in the Create client address endpoint's response, in the `id` field.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    try {
      apiInstance.deleteAddress(contentType, accept, profileId, addressId, alternativeKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#deleteAddress");
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
| **addressId** | **String**| ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field. | |
| **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] |

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

<a id="getAddress"></a>
# **getAddress**
> Object getAddress(contentType, accept, profileId, addressId, alternativeKey)

Get address

Retrieves information of a specific address of a given client, by its respectives &#x60;adderssId&#x60; and &#x60;profileId&#x60;.    &gt; For security and privacy reasons, this request returns masked address data. For unmasked information, see Get unmasked address.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

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

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String addressId = "bf82180e-cf9e-4089-9af6-ae1518555992"; // String | ID of a client's specific address as returned in the Create client address endpoint's response, in the `id` field.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    try {
      Object result = apiInstance.getAddress(contentType, accept, profileId, addressId, alternativeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getAddress");
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
| **addressId** | **String**| ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field. | |
| **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getAddressByVersion"></a>
# **getAddressByVersion**
> Object getAddressByVersion(contentType, accept, profileId, addressId, addressVersionId, reason, alternativeKey)

Get address by version

Retrieves information of a specific version address of a given client.    &gt; For security and privacy reasons, this request returns masked address data by version. For unmasked information, see Get unmasked address by version.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

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

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String addressId = "bf82180e-cf9e-4089-9af6-ae1518555992"; // String | ID of a client's specific address as returned in the Create client address endpoint's response, in the `id` field.
    String addressVersionId = "86dfae79-1d23-43f2-a643-2fc8f1839461"; // String | ID of the version of a given client's address as returned by endpoints that create or update address information in the `version` field.
    String reason = "data-validation"; // String | Reason for requesting unmasked data.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    try {
      Object result = apiInstance.getAddressByVersion(contentType, accept, profileId, addressId, addressVersionId, reason, alternativeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getAddressByVersion");
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
| **addressId** | **String**| ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field. | |
| **addressVersionId** | **String**| ID of the version of a given client&#39;s address as returned by endpoints that create or update address information in the &#x60;version&#x60; field. | |
| **reason** | **String**| Reason for requesting unmasked data. | |
| **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getClientAddresses"></a>
# **getClientAddresses**
> List&lt;Object&gt; getClientAddresses(contentType, accept, profileId, alternativeKey)

Get client addresses

Retrieves information of all addresses of a given client, by its &#x60;profileId&#x60;.    &gt; For security and privacy reasons, this request returns masked address data. For unmasked information, see Get unmasked client addresses.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

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

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    try {
      List<Object> result = apiInstance.getClientAddresses(contentType, accept, profileId, alternativeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getClientAddresses");
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

<a id="getUnmaskedAddress"></a>
# **getUnmaskedAddress**
> Object getUnmaskedAddress(contentType, accept, profileId, addressId, reason, alternativeKey)

Get unmasked address

Retrieves unmasked information of a specific address of a given client, by its respectives &#x60;adderssId&#x60; and &#x60;profileId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

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

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String addressId = "bf82180e-cf9e-4089-9af6-ae1518555992"; // String | ID of a client's specific address as returned in the Create client address endpoint's response, in the `id` field.
    String reason = "data-validation"; // String | Reason for requesting unmasked data.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    try {
      Object result = apiInstance.getUnmaskedAddress(contentType, accept, profileId, addressId, reason, alternativeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getUnmaskedAddress");
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
| **addressId** | **String**| ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field. | |
| **reason** | **String**| Reason for requesting unmasked data. | |
| **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getUnmaskedAddressByVersion"></a>
# **getUnmaskedAddressByVersion**
> Object getUnmaskedAddressByVersion(contentType, accept, profileId, addressId, addressVersionId, reason, alternativeKey)

Get unmasked address by version

Retrieves unmasked information of a specific address version of a given client.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

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

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String addressId = "bf82180e-cf9e-4089-9af6-ae1518555992"; // String | ID of a client's specific address as returned in the Create client address endpoint's response, in the `id` field.
    String addressVersionId = "86dfae79-1d23-43f2-a643-2fc8f1839461"; // String | ID of the version of a given client's address as returned by endpoints that create or update address information in the `version` field.
    String reason = "data-validation"; // String | Reason for requesting unmasked data.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    try {
      Object result = apiInstance.getUnmaskedAddressByVersion(contentType, accept, profileId, addressId, addressVersionId, reason, alternativeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getUnmaskedAddressByVersion");
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
| **addressId** | **String**| ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field. | |
| **addressVersionId** | **String**| ID of the version of a given client&#39;s address as returned by endpoints that create or update address information in the &#x60;version&#x60; field. | |
| **reason** | **String**| Reason for requesting unmasked data. | |
| **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getUnmaskedClientAddresses"></a>
# **getUnmaskedClientAddresses**
> List&lt;Map&lt;String, Object&gt;&gt; getUnmaskedClientAddresses(contentType, accept, profileId, alternativeKey)

Get unmasked client addresses

Retrieves unmasked information of all addresses of a given client, by its &#x60;profileId&#x60;.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

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

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    try {
      List<Map<String, Object>> result = apiInstance.getUnmaskedClientAddresses(contentType, accept, profileId, alternativeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#getUnmaskedClientAddresses");
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

[**List&lt;Map&lt;String, Object&gt;&gt;**](Map.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateClientAddress"></a>
# **updateClientAddress**
> Object updateClientAddress(contentType, accept, profileId, addressId, alternativeKey, updateClientAddressRequest)

Update client address

Updates one or more fields of an existing address for a given client profile.    &gt; Learn more about the [Profile System](https://developers.vtex.com/vtex-rest-api/docs/profile-system) and its other API endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddressesApi;

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

    AddressesApi apiInstance = new AddressesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String profileId = "70caf394-8534-447e-a0ca-1803c669c771"; // String | ID of the client's profile as returned by the Create profile endpoint's response, in the `id` field. It can also be an `alternativeKey` according to your custom profile schema. In this case, this request should also send the `alternativeKey` parameter.
    String addressId = "bf82180e-cf9e-4089-9af6-ae1518555992"; // String | ID of a client's specific address as returned in the Create client address endpoint's response, in the `id` field.
    String alternativeKey = "email"; // String | The `profileId` path parameter may be substituted by other profile fields in this request. When making this request, send the `alternativeKey` parameter with a value equal to the key of the field you wish to use as `profileId`.    > Currently, there are two possible values for this parameter: `email` and `document`.
    UpdateClientAddressRequest updateClientAddressRequest = new UpdateClientAddressRequest(); // UpdateClientAddressRequest | 
    try {
      Object result = apiInstance.updateClientAddress(contentType, accept, profileId, addressId, alternativeKey, updateClientAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddressesApi#updateClientAddress");
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
| **addressId** | **String**| ID of a client&#39;s specific address as returned in the Create client address endpoint&#39;s response, in the &#x60;id&#x60; field. | |
| **alternativeKey** | **String**| The &#x60;profileId&#x60; path parameter may be substituted by other profile fields in this request. When making this request, send the &#x60;alternativeKey&#x60; parameter with a value equal to the key of the field you wish to use as &#x60;profileId&#x60;.    &gt; Currently, there are two possible values for this parameter: &#x60;email&#x60; and &#x60;document&#x60;. | [optional] |
| **updateClientAddressRequest** | [**UpdateClientAddressRequest**](UpdateClientAddressRequest.md)|  | [optional] |

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

