# CustomFieldsApi

All URIs are relative to *https://api-sandbox.rebilly.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCustomField**](CustomFieldsApi.md#getCustomField) | **GET** /custom-fields/{resource}/{name} | Retrieve a Custom Field |
| [**getCustomFieldCollection**](CustomFieldsApi.md#getCustomFieldCollection) | **GET** /custom-fields/{resource} | Retrieve Custom Fields |
| [**putCustomField**](CustomFieldsApi.md#putCustomField) | **PUT** /custom-fields/{resource}/{name} | Create or alter a Custom Field |


<a id="getCustomField"></a>
# **getCustomField**
> CustomField getCustomField(resource, name, organizationId)

Retrieve a Custom Field

Retrieve a schema of the given Custom Field for the given resource type. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String resource = "customers"; // String | The resource type string.
    String name = "name_example"; // String | The custom field's identifier string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      CustomField result = apiInstance.getCustomField(resource, name, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#getCustomField");
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
| **resource** | **String**| The resource type string. | [enum: customers, payment-instruments, subscriptions, transactions, websites, products, plans, bump-offers] |
| **name** | **String**| The custom field&#39;s identifier string. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**CustomField**](CustomField.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A schema of the Custom Field was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |
| **404** | Resource was not found. |  -  |

<a id="getCustomFieldCollection"></a>
# **getCustomFieldCollection**
> List&lt;CustomField&gt; getCustomFieldCollection(resource, organizationId, limit, offset)

Retrieve Custom Fields

Retrieve a schema of Custom Fields for the given resource type. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String resource = "customers"; // String | The resource type string.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    Integer limit = 56; // Integer | The collection items limit.
    Integer offset = 56; // Integer | The collection items offset.
    try {
      List<CustomField> result = apiInstance.getCustomFieldCollection(resource, organizationId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#getCustomFieldCollection");
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
| **resource** | **String**| The resource type string. | [enum: customers, payment-instruments, subscriptions, transactions, websites, products, plans, bump-offers] |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |
| **limit** | **Integer**| The collection items limit. | [optional] |
| **offset** | **Integer**| The collection items offset. | [optional] |

### Return type

[**List&lt;CustomField&gt;**](CustomField.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A schema of Custom Fields was retrieved successfully. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **403** | Access forbidden. |  -  |

<a id="putCustomField"></a>
# **putCustomField**
> CustomField putCustomField(resource, name, customField, organizationId)

Create or alter a Custom Field

Create or alter a schema of the given Custom Field for the given resource. type. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api-sandbox.rebilly.com");
    
    // Configure API key authorization: SecretApiKey
    ApiKeyAuth SecretApiKey = (ApiKeyAuth) defaultClient.getAuthentication("SecretApiKey");
    SecretApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SecretApiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: JWT
    HttpBearerAuth JWT = (HttpBearerAuth) defaultClient.getAuthentication("JWT");
    JWT.setBearerToken("BEARER TOKEN");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String resource = "customers"; // String | The resource type string.
    String name = "name_example"; // String | The custom field's identifier string.
    CustomField customField = new CustomField(); // CustomField | Custom Fields schema of the given resource type.
    String organizationId = "organizationId_example"; // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
    try {
      CustomField result = apiInstance.putCustomField(resource, name, customField, organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#putCustomField");
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
| **resource** | **String**| The resource type string. | [enum: customers, payment-instruments, subscriptions, transactions, websites, products, plans, bump-offers] |
| **name** | **String**| The custom field&#39;s identifier string. | |
| **customField** | [**CustomField**](CustomField.md)| Custom Fields schema of the given resource type. | |
| **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] |

### Return type

[**CustomField**](CustomField.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Custom Field was updated. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **201** | The Custom Fields was created. |  * Rate-Limit-Limit -  <br>  * Rate-Limit-Remaining -  <br>  * Rate-Limit-Reset -  <br>  |
| **401** | Unauthorized access, invalid credentials was used. |  -  |
| **409** | The schema is in use: remove all the associated data in order to remove or alter the schema.  |  -  |
| **422** | Invalid data was sent. |  -  |

