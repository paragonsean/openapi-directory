# CustomerCategoriesApi

All URIs are relative to *https://api.jumpseller.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerCategoriesIdCustomersJsonDelete**](CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonDelete) | **DELETE** /customer_categories/{id}/customers.json | Delete Customers from an existing CustomerCategory. |
| [**customerCategoriesIdCustomersJsonGet**](CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonGet) | **GET** /customer_categories/{id}/customers.json | Retrieves the customers in a CustomerCategory. |
| [**customerCategoriesIdCustomersJsonPost**](CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonPost) | **POST** /customer_categories/{id}/customers.json | Adds Customers to a CustomerCategory. |
| [**customerCategoriesIdJsonDelete**](CustomerCategoriesApi.md#customerCategoriesIdJsonDelete) | **DELETE** /customer_categories/{id}.json | Delete an existing CustomerCategory. |
| [**customerCategoriesIdJsonGet**](CustomerCategoriesApi.md#customerCategoriesIdJsonGet) | **GET** /customer_categories/{id}.json | Retrieve a single CustomerCategory. |
| [**customerCategoriesIdJsonPut**](CustomerCategoriesApi.md#customerCategoriesIdJsonPut) | **PUT** /customer_categories/{id}.json | Update a CustomerCategory. |
| [**customerCategoriesJsonGet**](CustomerCategoriesApi.md#customerCategoriesJsonGet) | **GET** /customer_categories.json | Retrieve all Customer Categories. |
| [**customerCategoriesJsonPost**](CustomerCategoriesApi.md#customerCategoriesJsonPost) | **POST** /customer_categories.json | Create a new CustomerCategory. |


<a id="customerCategoriesIdCustomersJsonDelete"></a>
# **customerCategoriesIdCustomersJsonDelete**
> String customerCategoriesIdCustomersJsonDelete(login, authtoken, id, customersToCustomerCategory)

Delete Customers from an existing CustomerCategory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerCategoriesApi apiInstance = new CustomerCategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomerCategory
    CustomersToCustomerCategory customersToCustomerCategory = new CustomersToCustomerCategory(); // CustomersToCustomerCategory | Customer parameters.
    try {
      String result = apiInstance.customerCategoriesIdCustomersJsonDelete(login, authtoken, id, customersToCustomerCategory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerCategoriesApi#customerCategoriesIdCustomersJsonDelete");
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
| **id** | **Integer**| Id of the CustomerCategory | |
| **customersToCustomerCategory** | [**CustomersToCustomerCategory**](CustomersToCustomerCategory.md)| Customer parameters. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CustomerCategory Not Found. |  -  |

<a id="customerCategoriesIdCustomersJsonGet"></a>
# **customerCategoriesIdCustomersJsonGet**
> List&lt;Customer&gt; customerCategoriesIdCustomersJsonGet(login, authtoken, id)

Retrieves the customers in a CustomerCategory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerCategoriesApi apiInstance = new CustomerCategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomerCategory
    try {
      List<Customer> result = apiInstance.customerCategoriesIdCustomersJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerCategoriesApi#customerCategoriesIdCustomersJsonGet");
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
| **id** | **Integer**| Id of the CustomerCategory | |

### Return type

[**List&lt;Customer&gt;**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CustomerCategory Not Found. |  -  |

<a id="customerCategoriesIdCustomersJsonPost"></a>
# **customerCategoriesIdCustomersJsonPost**
> List&lt;Customer&gt; customerCategoriesIdCustomersJsonPost(login, authtoken, id, customersToCustomerCategory)

Adds Customers to a CustomerCategory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerCategoriesApi apiInstance = new CustomerCategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomerCategory
    CustomersToCustomerCategory customersToCustomerCategory = new CustomersToCustomerCategory(); // CustomersToCustomerCategory | Customer parameters.
    try {
      List<Customer> result = apiInstance.customerCategoriesIdCustomersJsonPost(login, authtoken, id, customersToCustomerCategory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerCategoriesApi#customerCategoriesIdCustomersJsonPost");
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
| **id** | **Integer**| Id of the CustomerCategory | |
| **customersToCustomerCategory** | [**CustomersToCustomerCategory**](CustomersToCustomerCategory.md)| Customer parameters. | |

### Return type

[**List&lt;Customer&gt;**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of Customers in the Customer Category |  -  |
| **404** | CustomerCategory Not Found. |  -  |

<a id="customerCategoriesIdJsonDelete"></a>
# **customerCategoriesIdJsonDelete**
> String customerCategoriesIdJsonDelete(login, authtoken, id)

Delete an existing CustomerCategory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerCategoriesApi apiInstance = new CustomerCategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomerCategory
    try {
      String result = apiInstance.customerCategoriesIdJsonDelete(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerCategoriesApi#customerCategoriesIdJsonDelete");
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
| **id** | **Integer**| Id of the CustomerCategory | |

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
| **404** | CustomerCategory Not Found. |  -  |

<a id="customerCategoriesIdJsonGet"></a>
# **customerCategoriesIdJsonGet**
> CustomerCategory customerCategoriesIdJsonGet(login, authtoken, id)

Retrieve a single CustomerCategory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerCategoriesApi apiInstance = new CustomerCategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomerCategory
    try {
      CustomerCategory result = apiInstance.customerCategoriesIdJsonGet(login, authtoken, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerCategoriesApi#customerCategoriesIdJsonGet");
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
| **id** | **Integer**| Id of the CustomerCategory | |

### Return type

[**CustomerCategory**](CustomerCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CustomerCategory Not Found. |  -  |

<a id="customerCategoriesIdJsonPut"></a>
# **customerCategoriesIdJsonPut**
> CustomerCategory customerCategoriesIdJsonPut(login, authtoken, id, customerCategoryEdit)

Update a CustomerCategory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerCategoriesApi apiInstance = new CustomerCategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer id = 56; // Integer | Id of the CustomerCategory
    CustomerCategoryEdit customerCategoryEdit = new CustomerCategoryEdit(); // CustomerCategoryEdit | CustomerCategory parameters.
    try {
      CustomerCategory result = apiInstance.customerCategoriesIdJsonPut(login, authtoken, id, customerCategoryEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerCategoriesApi#customerCategoriesIdJsonPut");
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
| **id** | **Integer**| Id of the CustomerCategory | |
| **customerCategoryEdit** | [**CustomerCategoryEdit**](CustomerCategoryEdit.md)| CustomerCategory parameters. | |

### Return type

[**CustomerCategory**](CustomerCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CustomerCategory Not Found. |  -  |

<a id="customerCategoriesJsonGet"></a>
# **customerCategoriesJsonGet**
> List&lt;CustomerCategory&gt; customerCategoriesJsonGet(login, authtoken, limit, page)

Retrieve all Customer Categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerCategoriesApi apiInstance = new CustomerCategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    Integer limit = 50; // Integer | List restriction
    Integer page = 1; // Integer | List page
    try {
      List<CustomerCategory> result = apiInstance.customerCategoriesJsonGet(login, authtoken, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerCategoriesApi#customerCategoriesJsonGet");
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
| **limit** | **Integer**| List restriction | [optional] [default to 50] |
| **page** | **Integer**| List page | [optional] [default to 1] |

### Return type

[**List&lt;CustomerCategory&gt;**](CustomerCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Customer Categories |  -  |

<a id="customerCategoriesJsonPost"></a>
# **customerCategoriesJsonPost**
> CustomerCategory customerCategoriesJsonPost(login, authtoken, customerCategoryEdit)

Create a new CustomerCategory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.jumpseller.com/v1");

    CustomerCategoriesApi apiInstance = new CustomerCategoriesApi(defaultClient);
    String login = "login_example"; // String | API OAuth login.
    String authtoken = "authtoken_example"; // String | API OAuth token.
    CustomerCategoryEdit customerCategoryEdit = new CustomerCategoryEdit(); // CustomerCategoryEdit | CustomerCategory parameters.
    try {
      CustomerCategory result = apiInstance.customerCategoriesJsonPost(login, authtoken, customerCategoryEdit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerCategoriesApi#customerCategoriesJsonPost");
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
| **customerCategoryEdit** | [**CustomerCategoryEdit**](CustomerCategoryEdit.md)| CustomerCategory parameters. | |

### Return type

[**CustomerCategory**](CustomerCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | CustomerCategory Not Found. |  -  |

