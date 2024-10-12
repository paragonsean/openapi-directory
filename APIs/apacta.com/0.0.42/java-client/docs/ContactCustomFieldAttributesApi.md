# ContactCustomFieldAttributesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contactCustomFieldAttributesContactCustomFieldAttributeIdGet**](ContactCustomFieldAttributesApi.md#contactCustomFieldAttributesContactCustomFieldAttributeIdGet) | **GET** /contact_custom_field_attributes/{contact_custom_field_attribute_id} | Details of 1 contact custom field attribute |
| [**contactCustomFieldAttributesGet**](ContactCustomFieldAttributesApi.md#contactCustomFieldAttributesGet) | **GET** /contact_custom_field_attributes | Get a list of contact custom field attributes |


<a id="contactCustomFieldAttributesContactCustomFieldAttributeIdGet"></a>
# **contactCustomFieldAttributesContactCustomFieldAttributeIdGet**
> ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response contactCustomFieldAttributesContactCustomFieldAttributeIdGet(contactCustomFieldAttributeId)

Details of 1 contact custom field attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactCustomFieldAttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ContactCustomFieldAttributesApi apiInstance = new ContactCustomFieldAttributesApi(defaultClient);
    String contactCustomFieldAttributeId = "contactCustomFieldAttributeId_example"; // String | 
    try {
      ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response result = apiInstance.contactCustomFieldAttributesContactCustomFieldAttributeIdGet(contactCustomFieldAttributeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactCustomFieldAttributesApi#contactCustomFieldAttributesContactCustomFieldAttributeIdGet");
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
| **contactCustomFieldAttributeId** | **String**|  | |

### Return type

[**ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response**](ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | ContactCustomFieldAttribute not found |  -  |

<a id="contactCustomFieldAttributesGet"></a>
# **contactCustomFieldAttributesGet**
> ContactCustomFieldAttributesGet200Response contactCustomFieldAttributesGet()

Get a list of contact custom field attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactCustomFieldAttributesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ContactCustomFieldAttributesApi apiInstance = new ContactCustomFieldAttributesApi(defaultClient);
    try {
      ContactCustomFieldAttributesGet200Response result = apiInstance.contactCustomFieldAttributesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactCustomFieldAttributesApi#contactCustomFieldAttributesGet");
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

[**ContactCustomFieldAttributesGet200Response**](ContactCustomFieldAttributesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

