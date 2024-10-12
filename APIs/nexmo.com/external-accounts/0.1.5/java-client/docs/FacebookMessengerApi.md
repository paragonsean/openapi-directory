# FacebookMessengerApi

All URIs are relative to *https://api.nexmo.com/beta/chatapp-accounts*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMessengerAccount**](FacebookMessengerApi.md#createMessengerAccount) | **POST** /messenger | Create a Messenger account |
| [**deleteMessengerAccount**](FacebookMessengerApi.md#deleteMessengerAccount) | **DELETE** /messenger/{external_id} | Delete a Messenger account |
| [**getMessengerAccount**](FacebookMessengerApi.md#getMessengerAccount) | **GET** /messenger/{external_id} | Retrieve a Messenger account |
| [**updateMessengerAccount**](FacebookMessengerApi.md#updateMessengerAccount) | **PATCH** /messenger/{external_id} | Update a Messenger account |


<a id="createMessengerAccount"></a>
# **createMessengerAccount**
> MessengerAccountResponse createMessengerAccount(createMessengerAccountRequest)

Create a Messenger account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacebookMessengerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/beta/chatapp-accounts");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FacebookMessengerApi apiInstance = new FacebookMessengerApi(defaultClient);
    CreateMessengerAccountRequest createMessengerAccountRequest = new CreateMessengerAccountRequest(); // CreateMessengerAccountRequest | 
    try {
      MessengerAccountResponse result = apiInstance.createMessengerAccount(createMessengerAccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacebookMessengerApi#createMessengerAccount");
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
| **createMessengerAccountRequest** | [**CreateMessengerAccountRequest**](CreateMessengerAccountRequest.md)|  | |

### Return type

[**MessengerAccountResponse**](MessengerAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created. |  -  |
| **400** | Bad Request. |  -  |
| **401** | Unauthorized. |  -  |
| **403** | Forbidden. |  -  |

<a id="deleteMessengerAccount"></a>
# **deleteMessengerAccount**
> deleteMessengerAccount(externalId)

Delete a Messenger account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacebookMessengerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/beta/chatapp-accounts");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FacebookMessengerApi apiInstance = new FacebookMessengerApi(defaultClient);
    String externalId = "externalId_example"; // String | External id of the account you want to delete. In this case it is the Facebook Page ID.
    try {
      apiInstance.deleteMessengerAccount(externalId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacebookMessengerApi#deleteMessengerAccount");
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
| **externalId** | **String**| External id of the account you want to delete. In this case it is the Facebook Page ID. | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content. |  -  |
| **401** | Unauthorized. |  -  |
| **403** | Forbidden. |  -  |
| **404** | Not Found. |  -  |

<a id="getMessengerAccount"></a>
# **getMessengerAccount**
> MessengerAccountResponse getMessengerAccount(externalId)

Retrieve a Messenger account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacebookMessengerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/beta/chatapp-accounts");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FacebookMessengerApi apiInstance = new FacebookMessengerApi(defaultClient);
    String externalId = "externalId_example"; // String | External id of the account you want to retrieve. In this case it is the Facebook Page ID.
    try {
      MessengerAccountResponse result = apiInstance.getMessengerAccount(externalId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacebookMessengerApi#getMessengerAccount");
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
| **externalId** | **String**| External id of the account you want to retrieve. In this case it is the Facebook Page ID. | |

### Return type

[**MessengerAccountResponse**](MessengerAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **401** | Unauthorized. |  -  |
| **404** | Not Found. |  -  |

<a id="updateMessengerAccount"></a>
# **updateMessengerAccount**
> UpdateMessengerAccount200Response updateMessengerAccount(externalId, updateMessengerAccountRequest)

Update a Messenger account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacebookMessengerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/beta/chatapp-accounts");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FacebookMessengerApi apiInstance = new FacebookMessengerApi(defaultClient);
    String externalId = "externalId_example"; // String | External id of the account you want to update. In this case it is the Facebook Page ID.
    UpdateMessengerAccountRequest updateMessengerAccountRequest = new UpdateMessengerAccountRequest(); // UpdateMessengerAccountRequest | Request body can contain any of the following
    try {
      UpdateMessengerAccount200Response result = apiInstance.updateMessengerAccount(externalId, updateMessengerAccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacebookMessengerApi#updateMessengerAccount");
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
| **externalId** | **String**| External id of the account you want to update. In this case it is the Facebook Page ID. | |
| **updateMessengerAccountRequest** | [**UpdateMessengerAccountRequest**](UpdateMessengerAccountRequest.md)| Request body can contain any of the following | |

### Return type

[**UpdateMessengerAccount200Response**](UpdateMessengerAccount200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **400** | Bad Request. |  -  |
| **401** | Unauthorized. |  -  |
| **403** | Forbidden. |  -  |
| **404** | Not Found. |  -  |

