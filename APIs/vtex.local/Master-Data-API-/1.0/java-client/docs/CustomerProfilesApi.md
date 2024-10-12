# CustomerProfilesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNewCustomerProfilev2**](CustomerProfilesApi.md#createNewCustomerProfilev2) | **POST** /api/dataentities/Client/documents | Create new customer profile |
| [**deleteCustomerProfile**](CustomerProfilesApi.md#deleteCustomerProfile) | **DELETE** /api/dataentities/Client/documents/{id} | Delete customer profile |
| [**updateCustomerProfile**](CustomerProfilesApi.md#updateCustomerProfile) | **PATCH** /api/dataentities/Client/documents/{id} | Update customer profile |


<a id="createNewCustomerProfilev2"></a>
# **createNewCustomerProfilev2**
> DocumentResponse createNewCustomerProfilev2(contentType, accept, createUpdateProfileRequests, schema)

Create new customer profile

Creates new customer profile.    &gt; You can use this request to create customer profiles according to any &#x60;CL&#x60; schema. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for the schemas you are using. Learn more about how to use [Master Data v2 schemas](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerProfilesApi;

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

    CustomerProfilesApi apiInstance = new CustomerProfilesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    CreateUpdateProfileRequests createUpdateProfileRequests = new CreateUpdateProfileRequests(); // CreateUpdateProfileRequests | 
    String schema = "schema"; // String | Name of the schema the document to be created needs to be compliant with.
    try {
      DocumentResponse result = apiInstance.createNewCustomerProfilev2(contentType, accept, createUpdateProfileRequests, schema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerProfilesApi#createNewCustomerProfilev2");
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
| **createUpdateProfileRequests** | [**CreateUpdateProfileRequests**](CreateUpdateProfileRequests.md)|  | |
| **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] |

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteCustomerProfile"></a>
# **deleteCustomerProfile**
> DocumentResponse deleteCustomerProfile(contentType, accept, id)

Delete customer profile

Deletes a customer profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerProfilesApi;

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

    CustomerProfilesApi apiInstance = new CustomerProfilesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
    try {
      DocumentResponse result = apiInstance.deleteCustomerProfile(contentType, accept, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerProfilesApi#deleteCustomerProfile");
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
| **id** | **String**| ID of the Document. | |

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateCustomerProfile"></a>
# **updateCustomerProfile**
> DocumentResponse updateCustomerProfile(contentType, accept, id, createUpdateProfileRequests, schema)

Update customer profile

Partially updates a customer profile.    &gt; You can use this request to update customer profiles according to any &#x60;CL&#x60; schema. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for the schemas you are using. Learn more about how to use [Master Data v2 schemas](https://developers.vtex.com/vtex-rest-api/docs/master-data-schema-lifecycle).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerProfilesApi;

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

    CustomerProfilesApi apiInstance = new CustomerProfilesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
    CreateUpdateProfileRequests createUpdateProfileRequests = new CreateUpdateProfileRequests(); // CreateUpdateProfileRequests | 
    String schema = "schema"; // String | Name of the schema the document to be created needs to be compliant with.
    try {
      DocumentResponse result = apiInstance.updateCustomerProfile(contentType, accept, id, createUpdateProfileRequests, schema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerProfilesApi#updateCustomerProfile");
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
| **id** | **String**| ID of the Document. | |
| **createUpdateProfileRequests** | [**CreateUpdateProfileRequests**](CreateUpdateProfileRequests.md)|  | |
| **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] |

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

