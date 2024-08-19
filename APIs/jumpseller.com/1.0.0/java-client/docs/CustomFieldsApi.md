# CustomFieldsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customFieldsIdJsonDelete**](CustomFieldsApi.md#customFieldsIdJsonDelete) | **DELETE** /custom_fields/{id}.json | Delete an existing CustomField. |
| [**customFieldsIdJsonGet**](CustomFieldsApi.md#customFieldsIdJsonGet) | **GET** /custom_fields/{id}.json | Retrieve a single CustomField. |
| [**customFieldsIdJsonPut**](CustomFieldsApi.md#customFieldsIdJsonPut) | **PUT** /custom_fields/{id}.json | Update a CustomField. |
| [**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete**](CustomFieldsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete) | **DELETE** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Delete an existing CustomFieldSelectOption. |
| [**customFieldsJsonGet**](CustomFieldsApi.md#customFieldsJsonGet) | **GET** /custom_fields.json | Retrieve all Store&#39;s Custom Fields. |
| [**customFieldsJsonPost**](CustomFieldsApi.md#customFieldsJsonPost) | **POST** /custom_fields.json | Create a new Custom Field. |


<a id="customFieldsIdJsonDelete"></a>
# **customFieldsIdJsonDelete**
> String customFieldsIdJsonDelete(login, authtoken, id)

Delete an existing CustomField.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomField
    try {
      String result = apiInstance.customFieldsIdJsonDelete(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#customFieldsIdJsonDelete");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CustomField Not Found. |  -  |

<a id="customFieldsIdJsonGet"></a>
# **customFieldsIdJsonGet**
> CustomField customFieldsIdJsonGet(login, authtoken, id)

Retrieve a single CustomField.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomField
    try {
      CustomField result = apiInstance.customFieldsIdJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#customFieldsIdJsonGet");
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

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CustomField Not Found. |  -  |

<a id="customFieldsIdJsonPut"></a>
# **customFieldsIdJsonPut**
> CustomField customFieldsIdJsonPut(login, authtoken, id, customFieldEdit)

Update a CustomField.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomField
    CustomFieldEdit customFieldEdit = new CustomFieldEdit(); // CustomFieldEdit | CustomField parameters.
    try {
      CustomField result = apiInstance.customFieldsIdJsonPut(login, authtoken, id, customFieldEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#customFieldsIdJsonPut");
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
| **customFieldEdit** | [**CustomFieldEdit**](CustomFieldEdit.md)| CustomField parameters. | |

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CustomField Not Found. |  -  |

<a id="customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete"></a>
# **customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete**
> String customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete(login, authtoken, id, customFieldSelectOptionId)

Delete an existing CustomFieldSelectOption.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomField
    Integer customFieldSelectOptionId = 56; // Integer | Id of the CustomFieldSelectOption
    try {
      String result = apiInstance.customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete(login, authtoken, id, customFieldSelectOptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete");
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

**String**

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

<a id="customFieldsJsonGet"></a>
# **customFieldsJsonGet**
> List&lt;CustomField&gt; customFieldsJsonGet(login, authtoken)

Retrieve all Store&#39;s Custom Fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    try {
      List<CustomField> result = apiInstance.customFieldsJsonGet(login, authtoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#customFieldsJsonGet");
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

### Return type

[**List&lt;CustomField&gt;**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Custom Fields |  -  |

<a id="customFieldsJsonPost"></a>
# **customFieldsJsonPost**
> CustomField customFieldsJsonPost(login, authtoken, customFieldEdit)

Create a new Custom Field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    CustomFieldEdit customFieldEdit = new CustomFieldEdit(); // CustomFieldEdit | Custom Field parameters.
    try {
      CustomField result = apiInstance.customFieldsJsonPost(login, authtoken, customFieldEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#customFieldsJsonPost");
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
| **customFieldEdit** | [**CustomFieldEdit**](CustomFieldEdit.md)| Custom Field parameters. | |

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

