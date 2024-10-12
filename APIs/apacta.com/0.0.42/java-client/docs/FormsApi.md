# FormsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**formsFormIdDelete**](FormsApi.md#formsFormIdDelete) | **DELETE** /forms/{form_id} | Delete a form |
| [**formsFormIdGet**](FormsApi.md#formsFormIdGet) | **GET** /forms/{form_id} | View form |
| [**formsFormIdPut**](FormsApi.md#formsFormIdPut) | **PUT** /forms/{form_id} | Edit a form |
| [**formsGet**](FormsApi.md#formsGet) | **GET** /forms | Retrieve array of forms |
| [**formsPost**](FormsApi.md#formsPost) | **POST** /forms | Add new form |
| [**formsUndeleteFormIdGet**](FormsApi.md#formsUndeleteFormIdGet) | **GET** /forms/undelete/{form_id} | Undelete form and related entities to it |
| [**formsViewTimeFormPdfFormIdGet**](FormsApi.md#formsViewTimeFormPdfFormIdGet) | **GET** /forms/view_time_form_pdf/{form_id} | Generate time form pdf |


<a id="formsFormIdDelete"></a>
# **formsFormIdDelete**
> formsFormIdDelete(formId)

Delete a form

You can only delete the forms that you&#39;ve submitted yourself

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

    FormsApi apiInstance = new FormsApi(defaultClient);
    String formId = "formId_example"; // String | 
    try {
      apiInstance.formsFormIdDelete(formId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormsApi#formsFormIdDelete");
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
| **formId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="formsFormIdGet"></a>
# **formsFormIdGet**
> FormsFormIdGet200Response formsFormIdGet(formId)

View form

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

    FormsApi apiInstance = new FormsApi(defaultClient);
    String formId = "formId_example"; // String | 
    try {
      FormsFormIdGet200Response result = apiInstance.formsFormIdGet(formId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormsApi#formsFormIdGet");
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
| **formId** | **String**|  | |

### Return type

[**FormsFormIdGet200Response**](FormsFormIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="formsFormIdPut"></a>
# **formsFormIdPut**
> formsFormIdPut(formId)

Edit a form

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

    FormsApi apiInstance = new FormsApi(defaultClient);
    String formId = "formId_example"; // String | 
    try {
      apiInstance.formsFormIdPut(formId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormsApi#formsFormIdPut");
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
| **formId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="formsGet"></a>
# **formsGet**
> FormsGet200Response formsGet(extended, dateFrom, dateTo, show, projectId, createdById, formTemplateId, formTemplateType, employeeName)

Retrieve array of forms

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

    FormsApi apiInstance = new FormsApi(defaultClient);
    String extended = "true"; // String | Used to have extended details from the forms from the `Form`'s `FormFields`
    String dateFrom = "dateFrom_example"; // String | Used in conjunction with `date_to` to only show forms within these dates - format like `2016-28-05`
    String dateTo = "dateTo_example"; // String | Used in conjunction with `date_from` to only show forms within these dates - format like `2016-28-30`
    String show = "show_example"; // String | Used to show forms with trashed
    UUID projectId = UUID.randomUUID(); // UUID | Used to filter on the `project_id` of the forms
    String createdById = "createdById_example"; // String | Used to filter on the `created_by_id` of the forms
    List<UUID> formTemplateId = Arrays.asList(); // List<UUID> | Used to filter on the `form_template_id` of the forms. Accept single value and array.
    String formTemplateType = "formTemplateType_example"; // String | Filter by `form_templates.identifier` containing string passed in `form_template_type`. Accept strings like [`qa`, `dagseddel`]
    String employeeName = "employeeName_example"; // String | Used to filter forms by user's first or last name
    try {
      FormsGet200Response result = apiInstance.formsGet(extended, dateFrom, dateTo, show, projectId, createdById, formTemplateId, formTemplateType, employeeName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormsApi#formsGet");
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
| **extended** | **String**| Used to have extended details from the forms from the &#x60;Form&#x60;&#39;s &#x60;FormFields&#x60; | [optional] [enum: true, false] |
| **dateFrom** | **String**| Used in conjunction with &#x60;date_to&#x60; to only show forms within these dates - format like &#x60;2016-28-05&#x60; | [optional] |
| **dateTo** | **String**| Used in conjunction with &#x60;date_from&#x60; to only show forms within these dates - format like &#x60;2016-28-30&#x60; | [optional] |
| **show** | **String**| Used to show forms with trashed | [optional] |
| **projectId** | **UUID**| Used to filter on the &#x60;project_id&#x60; of the forms | [optional] |
| **createdById** | **String**| Used to filter on the &#x60;created_by_id&#x60; of the forms | [optional] |
| **formTemplateId** | [**List&lt;UUID&gt;**](UUID.md)| Used to filter on the &#x60;form_template_id&#x60; of the forms. Accept single value and array. | [optional] |
| **formTemplateType** | **String**| Filter by &#x60;form_templates.identifier&#x60; containing string passed in &#x60;form_template_type&#x60;. Accept strings like [&#x60;qa&#x60;, &#x60;dagseddel&#x60;] | [optional] |
| **employeeName** | **String**| Used to filter forms by user&#39;s first or last name | [optional] |

### Return type

[**FormsGet200Response**](FormsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="formsPost"></a>
# **formsPost**
> ClockingRecordsPost201Response formsPost(formsPostRequest)

Add new form

Used to add a form into the system

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

    FormsApi apiInstance = new FormsApi(defaultClient);
    FormsPostRequest formsPostRequest = new FormsPostRequest(); // FormsPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.formsPost(formsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormsApi#formsPost");
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
| **formsPostRequest** | [**FormsPostRequest**](FormsPostRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **422** | Validation error |  -  |

<a id="formsUndeleteFormIdGet"></a>
# **formsUndeleteFormIdGet**
> EmptySuccessResponse formsUndeleteFormIdGet(formId)

Undelete form and related entities to it

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

    FormsApi apiInstance = new FormsApi(defaultClient);
    String formId = "formId_example"; // String | 
    try {
      EmptySuccessResponse result = apiInstance.formsUndeleteFormIdGet(formId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormsApi#formsUndeleteFormIdGet");
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
| **formId** | **String**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="formsViewTimeFormPdfFormIdGet"></a>
# **formsViewTimeFormPdfFormIdGet**
> EmptySuccessResponse formsViewTimeFormPdfFormIdGet(formId)

Generate time form pdf

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

    FormsApi apiInstance = new FormsApi(defaultClient);
    String formId = "formId_example"; // String | 
    try {
      EmptySuccessResponse result = apiInstance.formsViewTimeFormPdfFormIdGet(formId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormsApi#formsViewTimeFormPdfFormIdGet");
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
| **formId** | **String**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

