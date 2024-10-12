# UserCustomFieldAttributesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userCustomFieldAttributesGet**](UserCustomFieldAttributesApi.md#userCustomFieldAttributesGet) | **GET** /user_custom_field_attributes | Get a list of user custom field attributes |
| [**userCustomFieldAttributesUserCustomFieldAttributeIdGet**](UserCustomFieldAttributesApi.md#userCustomFieldAttributesUserCustomFieldAttributeIdGet) | **GET** /user_custom_field_attributes/{user_custom_field_attribute_id} | Details of 1 user custom field attribute |


<a id="userCustomFieldAttributesGet"></a>
# **userCustomFieldAttributesGet**
> UserCustomFieldAttributesGet200Response userCustomFieldAttributesGet()

Get a list of user custom field attributes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserCustomFieldAttributesApi;

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

    UserCustomFieldAttributesApi apiInstance = new UserCustomFieldAttributesApi(defaultClient);
    try {
      UserCustomFieldAttributesGet200Response result = apiInstance.userCustomFieldAttributesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserCustomFieldAttributesApi#userCustomFieldAttributesGet");
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

[**UserCustomFieldAttributesGet200Response**](UserCustomFieldAttributesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="userCustomFieldAttributesUserCustomFieldAttributeIdGet"></a>
# **userCustomFieldAttributesUserCustomFieldAttributeIdGet**
> UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response userCustomFieldAttributesUserCustomFieldAttributeIdGet(userCustomFieldAttributeId)

Details of 1 user custom field attribute

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserCustomFieldAttributesApi;

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

    UserCustomFieldAttributesApi apiInstance = new UserCustomFieldAttributesApi(defaultClient);
    String userCustomFieldAttributeId = "userCustomFieldAttributeId_example"; // String | 
    try {
      UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response result = apiInstance.userCustomFieldAttributesUserCustomFieldAttributeIdGet(userCustomFieldAttributeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserCustomFieldAttributesApi#userCustomFieldAttributesUserCustomFieldAttributeIdGet");
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
| **userCustomFieldAttributeId** | **String**|  | |

### Return type

[**UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response**](UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | UserCustomFieldAttribute not found |  -  |

