# CustomFieldSelectOptionsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet**](CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet) | **GET** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Retrieve a single SelectOption from a CustomField. |
| [**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut**](CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut) | **PUT** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Update a SelectOption from a CustomField. |
| [**customFieldsIdSelectOptionsJsonGet**](CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsJsonGet) | **GET** /custom_fields/{id}/select_options.json | Retrieve all Store&#39;s Custom Fields. |
| [**customFieldsIdSelectOptionsJsonPost**](CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsJsonPost) | **POST** /custom_fields/{id}/select_options.json | Create a new Custom Field Select Option. |


<a id="customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet"></a>
# **customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet**
> CustomFieldSelectOption customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet(login, authtoken, id, customFieldSelectOptionId)

Retrieve a single SelectOption from a CustomField.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldSelectOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomFieldSelectOptionsApi apiInstance = new CustomFieldSelectOptionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomField
    Integer customFieldSelectOptionId = 56; // Integer | Id of the CustomFieldSelectOption
    try {
      CustomFieldSelectOption result = apiInstance.customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet(login, authtoken, id, customFieldSelectOptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldSelectOptionsApi#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the CustomField | |
| **customFieldSelectOptionId** | **Integer**| Id of the CustomFieldSelectOption | |

### Return type

[**CustomFieldSelectOption**](CustomFieldSelectOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CustomFieldSelectOption Not Found. |  -  |

<a id="customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut"></a>
# **customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut**
> CustomFieldSelectOption customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut(login, authtoken, id, customFieldSelectOptionId, customFieldSelectOptionEdit)

Update a SelectOption from a CustomField.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldSelectOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomFieldSelectOptionsApi apiInstance = new CustomFieldSelectOptionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomField
    Integer customFieldSelectOptionId = 56; // Integer | Id of the CustomFieldSelectOption
    CustomFieldSelectOptionEdit customFieldSelectOptionEdit = new CustomFieldSelectOptionEdit(); // CustomFieldSelectOptionEdit | CustomFieldSelectOption parameters.
    try {
      CustomFieldSelectOption result = apiInstance.customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut(login, authtoken, id, customFieldSelectOptionId, customFieldSelectOptionEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldSelectOptionsApi#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the CustomField | |
| **customFieldSelectOptionId** | **Integer**| Id of the CustomFieldSelectOption | |
| **customFieldSelectOptionEdit** | [**CustomFieldSelectOptionEdit**](CustomFieldSelectOptionEdit.md)| CustomFieldSelectOption parameters. | |

### Return type

[**CustomFieldSelectOption**](CustomFieldSelectOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CustomFieldSelectOption Not Found. |  -  |

<a id="customFieldsIdSelectOptionsJsonGet"></a>
# **customFieldsIdSelectOptionsJsonGet**
> List&lt;CustomFieldSelectOption&gt; customFieldsIdSelectOptionsJsonGet(login, authtoken, id)

Retrieve all Store&#39;s Custom Fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldSelectOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomFieldSelectOptionsApi apiInstance = new CustomFieldSelectOptionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomField
    try {
      List<CustomFieldSelectOption> result = apiInstance.customFieldsIdSelectOptionsJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldSelectOptionsApi#customFieldsIdSelectOptionsJsonGet");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **Integer**| Id of the CustomField | |

### Return type

[**List&lt;CustomFieldSelectOption&gt;**](CustomFieldSelectOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Custom Fields Select Options |  -  |

<a id="customFieldsIdSelectOptionsJsonPost"></a>
# **customFieldsIdSelectOptionsJsonPost**
> CustomFieldSelectOption customFieldsIdSelectOptionsJsonPost(login, authtoken, id, customFieldSelectOptionEdit)

Create a new Custom Field Select Option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldSelectOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomFieldSelectOptionsApi apiInstance = new CustomFieldSelectOptionsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    String id = "id_example"; // String | Automatically added
    CustomFieldSelectOptionEdit customFieldSelectOptionEdit = new CustomFieldSelectOptionEdit(); // CustomFieldSelectOptionEdit | Custom Field Select Option parameters.
    try {
      CustomFieldSelectOption result = apiInstance.customFieldsIdSelectOptionsJsonPost(login, authtoken, id, customFieldSelectOptionEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldSelectOptionsApi#customFieldsIdSelectOptionsJsonPost");
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
| **login** | **String**| API OAuth login. | |
| **authtoken** | **String**| API OAuth token. | |
| **id** | **String**| Automatically added | |
| **customFieldSelectOptionEdit** | [**CustomFieldSelectOptionEdit**](CustomFieldSelectOptionEdit.md)| Custom Field Select Option parameters. | |

### Return type

[**CustomFieldSelectOption**](CustomFieldSelectOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

