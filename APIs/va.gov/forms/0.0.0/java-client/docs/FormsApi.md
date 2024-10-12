# FormsApi

All URIs are relative to *https://sandbox-api.va.gov/services/va_forms/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findFormByFormName**](FormsApi.md#findFormByFormName) | **GET** /forms/{form_name} | Find form by form name |
| [**findForms**](FormsApi.md#findForms) | **GET** /forms | Returns all VA Forms and their last revision date |


<a id="findFormByFormName"></a>
# **findFormByFormName**
> FindFormByFormName200Response findFormByFormName(formName)

Find form by form name

Returns a single form and the full revision history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.va.gov/services/va_forms/v0");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    FormsApi apiInstance = new FormsApi(defaultClient);
    String formName = "10-10EZ"; // String | The VA form_name of the form being requested. The exact form name must be passed, including proper placement of prefixes and/or hyphens.
    try {
      FindFormByFormName200Response result = apiInstance.findFormByFormName(formName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormsApi#findFormByFormName");
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
| **formName** | **String**| The VA form_name of the form being requested. The exact form name must be passed, including proper placement of prefixes and/or hyphens. | |

### Return type

[**FindFormByFormName200Response**](FindFormByFormName200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | VA Form Show response |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **429** | Too many requests |  -  |

<a id="findForms"></a>
# **findForms**
> FindForms200Response findForms(query)

Returns all VA Forms and their last revision date

Returns an index of all available VA forms. Optionally, pass a query parameter to filter forms by form number or title.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.va.gov/services/va_forms/v0");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    FormsApi apiInstance = new FormsApi(defaultClient);
    String query = "query_example"; // String | Returns form data based on entered form name.
    try {
      FindForms200Response result = apiInstance.findForms(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormsApi#findForms");
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
| **query** | **String**| Returns form data based on entered form name. | [optional] |

### Return type

[**FindForms200Response**](FindForms200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | VA Forms index response |  -  |
| **401** | Unauthorized |  -  |
| **429** | Too many requests |  -  |

