# CustomerAdditionalFieldsApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customersIdFieldsFieldIdDelete**](CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdDelete) | **DELETE** /customers/{id}/fields/{field_id} | Delete a Customer Additional Field. |
| [**customersIdFieldsFieldIdGet**](CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdGet) | **GET** /customers/{id}/fields/{field_id} | Retrieve a single Customer Additional Field. |
| [**customersIdFieldsFieldIdPut**](CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdPut) | **PUT** /customers/{id}/fields/{field_id} | Update a Customer Additional Field. |
| [**customersIdFieldsGet**](CustomerAdditionalFieldsApi.md#customersIdFieldsGet) | **GET** /customers/{id}/fields | Retrieves the Customer Additional Field of a Customer. |
| [**customersIdFieldsPost**](CustomerAdditionalFieldsApi.md#customersIdFieldsPost) | **POST** /customers/{id}/fields | Adds Customer Additional Fields to a Customer. |


<a id="customersIdFieldsFieldIdDelete"></a>
# **customersIdFieldsFieldIdDelete**
> String customersIdFieldsFieldIdDelete(login, authtoken, id, fieldId)

Delete a Customer Additional Field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAdditionalFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerAdditionalFieldsApi apiInstance = new CustomerAdditionalFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Customer
    Integer fieldId = 56; // Integer | Id of the Customer Additional Field
    try {
      String result = apiInstance.customersIdFieldsFieldIdDelete(login, authtoken, id, fieldId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAdditionalFieldsApi#customersIdFieldsFieldIdDelete");
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
| **id** | **Integer**| Id of the Customer | |
| **fieldId** | **Integer**| Id of the Customer Additional Field | |

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
| **404** | Customer Not Found. |  -  |

<a id="customersIdFieldsFieldIdGet"></a>
# **customersIdFieldsFieldIdGet**
> CustomerAdditionalField customersIdFieldsFieldIdGet(login, authtoken, id, fieldId)

Retrieve a single Customer Additional Field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAdditionalFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerAdditionalFieldsApi apiInstance = new CustomerAdditionalFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Customer
    Integer fieldId = 56; // Integer | Id of the Customer Additional Field
    try {
      CustomerAdditionalField result = apiInstance.customersIdFieldsFieldIdGet(login, authtoken, id, fieldId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAdditionalFieldsApi#customersIdFieldsFieldIdGet");
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
| **id** | **Integer**| Id of the Customer | |
| **fieldId** | **Integer**| Id of the Customer Additional Field | |

### Return type

[**CustomerAdditionalField**](CustomerAdditionalField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Customer Not Found. |  -  |

<a id="customersIdFieldsFieldIdPut"></a>
# **customersIdFieldsFieldIdPut**
> CustomerAdditionalField customersIdFieldsFieldIdPut(login, authtoken, id, fieldId, customerAdditionalFieldEdit)

Update a Customer Additional Field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAdditionalFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerAdditionalFieldsApi apiInstance = new CustomerAdditionalFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Customer
    Integer fieldId = 56; // Integer | Id of the Customer Additional Field
    CustomerAdditionalFieldEdit customerAdditionalFieldEdit = new CustomerAdditionalFieldEdit(); // CustomerAdditionalFieldEdit | Customer Additional Field parameters.
    try {
      CustomerAdditionalField result = apiInstance.customersIdFieldsFieldIdPut(login, authtoken, id, fieldId, customerAdditionalFieldEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAdditionalFieldsApi#customersIdFieldsFieldIdPut");
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
| **id** | **Integer**| Id of the Customer | |
| **fieldId** | **Integer**| Id of the Customer Additional Field | |
| **customerAdditionalFieldEdit** | [**CustomerAdditionalFieldEdit**](CustomerAdditionalFieldEdit.md)| Customer Additional Field parameters. | |

### Return type

[**CustomerAdditionalField**](CustomerAdditionalField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Customer Additional Field Bad Parameters. |  -  |
| **404** | Customer Additional Field Not Found. |  -  |

<a id="customersIdFieldsGet"></a>
# **customersIdFieldsGet**
> List&lt;CustomerAdditionalField&gt; customersIdFieldsGet(login, authtoken, id)

Retrieves the Customer Additional Field of a Customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAdditionalFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerAdditionalFieldsApi apiInstance = new CustomerAdditionalFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Customer
    try {
      List<CustomerAdditionalField> result = apiInstance.customersIdFieldsGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAdditionalFieldsApi#customersIdFieldsGet");
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
| **id** | **Integer**| Id of the Customer | |

### Return type

[**List&lt;CustomerAdditionalField&gt;**](CustomerAdditionalField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Customer Not Found. |  -  |

<a id="customersIdFieldsPost"></a>
# **customersIdFieldsPost**
> CustomerAdditionalField customersIdFieldsPost(login, authtoken, id, customerAdditionalFieldEdit)

Adds Customer Additional Fields to a Customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerAdditionalFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerAdditionalFieldsApi apiInstance = new CustomerAdditionalFieldsApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the Customer
    CustomerAdditionalFieldEdit customerAdditionalFieldEdit = new CustomerAdditionalFieldEdit(); // CustomerAdditionalFieldEdit | Customer Additional Field parameters.
    try {
      CustomerAdditionalField result = apiInstance.customersIdFieldsPost(login, authtoken, id, customerAdditionalFieldEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerAdditionalFieldsApi#customersIdFieldsPost");
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
| **id** | **Integer**| Id of the Customer | |
| **customerAdditionalFieldEdit** | [**CustomerAdditionalFieldEdit**](CustomerAdditionalFieldEdit.md)| Customer Additional Field parameters. | |

### Return type

[**CustomerAdditionalField**](CustomerAdditionalField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Customer Additional Field Not Found. |  -  |

