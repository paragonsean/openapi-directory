# AdministrationsApi

All URIs are relative to *https://api.storecove.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAdministration**](AdministrationsApi.md#createAdministration) | **POST** /legal_entities/{legal_entity_id}/administrations | Create a new Administration |
| [**deleteAdministration**](AdministrationsApi.md#deleteAdministration) | **DELETE** /legal_entities/{legal_entity_id}/administrations/{id} | Delete Administration |
| [**getAdministration**](AdministrationsApi.md#getAdministration) | **GET** /legal_entities/{legal_entity_id}/administrations/{id} | Get Administration |
| [**updateAdministration**](AdministrationsApi.md#updateAdministration) | **PATCH** /legal_entities/{legal_entity_id}/administrations/{id} | Update Administration |


<a id="createAdministration"></a>
# **createAdministration**
> Administration createAdministration(legalEntityId, administrationCreate)

Create a new Administration

Deprecated. Create a new Administration. An Administration is an email destination for purchase invoices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AdministrationsApi apiInstance = new AdministrationsApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity for which to create the Administration
    AdministrationCreate administrationCreate = new AdministrationCreate(); // AdministrationCreate | Administration to create
    try {
      Administration result = apiInstance.createAdministration(legalEntityId, administrationCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationsApi#createAdministration");
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
| **legalEntityId** | **Long**| The id of the LegalEntity for which to create the Administration | |
| **administrationCreate** | [**AdministrationCreate**](AdministrationCreate.md)| Administration to create | |

### Return type

[**Administration**](Administration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="deleteAdministration"></a>
# **deleteAdministration**
> deleteAdministration(legalEntityId, id)

Delete Administration

Deprecated. Delete an Administration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AdministrationsApi apiInstance = new AdministrationsApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity the Administration belongs to
    Long id = 56L; // Long | The id of the Administration
    try {
      apiInstance.deleteAdministration(legalEntityId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationsApi#deleteAdministration");
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
| **legalEntityId** | **Long**| The id of the LegalEntity the Administration belongs to | |
| **id** | **Long**| The id of the Administration | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAdministration"></a>
# **getAdministration**
> Administration getAdministration(legalEntityId, id)

Get Administration

Deprecated. Get an Administration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AdministrationsApi apiInstance = new AdministrationsApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity the Administration belongs to
    Long id = 56L; // Long | The id of the Administration
    try {
      Administration result = apiInstance.getAdministration(legalEntityId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationsApi#getAdministration");
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
| **legalEntityId** | **Long**| The id of the LegalEntity the Administration belongs to | |
| **id** | **Long**| The id of the Administration | |

### Return type

[**Administration**](Administration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="updateAdministration"></a>
# **updateAdministration**
> Administration updateAdministration(legalEntityId, id, administrationUpdate)

Update Administration

Deprecated. Update an Administration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    AdministrationsApi apiInstance = new AdministrationsApi(defaultClient);
    Long legalEntityId = 56L; // Long | The id of the LegalEntity the Administration belongs to
    Long id = 56L; // Long | The id of the Administration to be updated
    AdministrationUpdate administrationUpdate = new AdministrationUpdate(); // AdministrationUpdate | Administration to update
    try {
      Administration result = apiInstance.updateAdministration(legalEntityId, id, administrationUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrationsApi#updateAdministration");
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
| **legalEntityId** | **Long**| The id of the LegalEntity the Administration belongs to | |
| **id** | **Long**| The id of the Administration to be updated | |
| **administrationUpdate** | [**AdministrationUpdate**](AdministrationUpdate.md)| Administration to update | |

### Return type

[**Administration**](Administration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

