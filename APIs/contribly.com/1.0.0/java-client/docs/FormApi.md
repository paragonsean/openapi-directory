# FormApi

All URIs are relative to *https://api.contribly.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**formResponsesGet**](FormApi.md#formResponsesGet) | **GET** /form-responses | List form responses |
| [**formResponsesIdGet**](FormApi.md#formResponsesIdGet) | **GET** /form-responses/{id} | Get a single form response by id |
| [**formResponsesPost**](FormApi.md#formResponsesPost) | **POST** /form-responses | Submit a response to a form |
| [**formsGet**](FormApi.md#formsGet) | **GET** /forms | List forms |
| [**formsIdDelete**](FormApi.md#formsIdDelete) | **DELETE** /forms/{id} | Delete this form and all of it&#39;s responses. |
| [**formsIdGet**](FormApi.md#formsIdGet) | **GET** /forms/{id} | Get a single form by id |
| [**formsPost**](FormApi.md#formsPost) | **POST** /forms | Create a form |


<a id="formResponsesGet"></a>
# **formResponsesGet**
> List&lt;FormResponse&gt; formResponsesGet(user, form, contribution)

List form responses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    FormApi apiInstance = new FormApi(defaultClient);
    String user = "user_example"; // String | Restrict results to responses submitted by this user.
    String form = "form_example"; // String | Restrict results to responses submitted to this form.
    String contribution = "contribution_example"; // String | Restrict results to responses relating to this contribution.
    try {
      List<FormResponse> result = apiInstance.formResponsesGet(user, form, contribution);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#formResponsesGet");
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
| **user** | **String**| Restrict results to responses submitted by this user. | [optional] |
| **form** | **String**| Restrict results to responses submitted to this form. | [optional] |
| **contribution** | **String**| Restrict results to responses relating to this contribution. | [optional] |

### Return type

[**List&lt;FormResponse&gt;**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of form responses |  * X-total-count - Total number of matching users <br>  |

<a id="formResponsesIdGet"></a>
# **formResponsesIdGet**
> FormResponse formResponsesIdGet(id)

Get a single form response by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    FormApi apiInstance = new FormApi(defaultClient);
    String id = "id_example"; // String | Id of the assignment to return
    try {
      FormResponse result = apiInstance.formResponsesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#formResponsesIdGet");
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
| **id** | **String**| Id of the assignment to return | |

### Return type

[**FormResponse**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Form response found |  -  |
| **404** | Not found |  -  |

<a id="formResponsesPost"></a>
# **formResponsesPost**
> FormResponse formResponsesPost(formResponseSubmission)

Submit a response to a form

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    FormApi apiInstance = new FormApi(defaultClient);
    FormResponseSubmission formResponseSubmission = new FormResponseSubmission(); // FormResponseSubmission | Form response
    try {
      FormResponse result = apiInstance.formResponsesPost(formResponseSubmission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#formResponsesPost");
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
| **formResponseSubmission** | [**FormResponseSubmission**](FormResponseSubmission.md)| Form response | |

### Return type

[**FormResponse**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Form response saved |  -  |

<a id="formsGet"></a>
# **formsGet**
> List&lt;Form&gt; formsGet(ownedBy)

List forms

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    FormApi apiInstance = new FormApi(defaultClient);
    String ownedBy = "ownedBy_example"; // String | Restrict results to forms owned by this user.
    try {
      List<Form> result = apiInstance.formsGet(ownedBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#formsGet");
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
| **ownedBy** | **String**| Restrict results to forms owned by this user. | |

### Return type

[**List&lt;Form&gt;**](Form.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of forms |  * X-total-count - Total number of matching users <br>  |

<a id="formsIdDelete"></a>
# **formsIdDelete**
> formsIdDelete(id)

Delete this form and all of it&#39;s responses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    FormApi apiInstance = new FormApi(defaultClient);
    String id = "id_example"; // String | Id of the form to delete
    try {
      apiInstance.formsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#formsIdDelete");
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
| **id** | **String**| Id of the form to delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Form deleted |  -  |
| **404** | Not found |  -  |

<a id="formsIdGet"></a>
# **formsIdGet**
> Form formsIdGet(id)

Get a single form by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    FormApi apiInstance = new FormApi(defaultClient);
    String id = "id_example"; // String | Id of the form to return
    try {
      Form result = apiInstance.formsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#formsIdGet");
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
| **id** | **String**| Id of the form to return | |

### Return type

[**Form**](Form.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Form found |  -  |
| **404** | Not found |  -  |

<a id="formsPost"></a>
# **formsPost**
> Form formsPost(formSubmission)

Create a form

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FormApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    FormApi apiInstance = new FormApi(defaultClient);
    FormSubmission formSubmission = new FormSubmission(); // FormSubmission | Form object to be created
    try {
      Form result = apiInstance.formsPost(formSubmission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FormApi#formsPost");
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
| **formSubmission** | [**FormSubmission**](FormSubmission.md)| Form object to be created | |

### Return type

[**Form**](Form.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Form created |  -  |

