# CustomFieldsApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2CustomFieldsIdJsonDelete**](CustomFieldsApi.md#v2CustomFieldsIdJsonDelete) | **DELETE** /v2/custom_fields/{id}.json | Delete a custom field |
| [**v2CustomFieldsIdJsonGet**](CustomFieldsApi.md#v2CustomFieldsIdJsonGet) | **GET** /v2/custom_fields/{id}.json | Fetch a custom field |
| [**v2CustomFieldsIdJsonPut**](CustomFieldsApi.md#v2CustomFieldsIdJsonPut) | **PUT** /v2/custom_fields/{id}.json | Update a custom field |
| [**v2CustomFieldsJsonGet**](CustomFieldsApi.md#v2CustomFieldsJsonGet) | **GET** /v2/custom_fields.json | List custom fields |
| [**v2CustomFieldsJsonPost**](CustomFieldsApi.md#v2CustomFieldsJsonPost) | **POST** /v2/custom_fields.json | Create a custom field |


<a id="v2CustomFieldsIdJsonDelete"></a>
# **v2CustomFieldsIdJsonDelete**
> v2CustomFieldsIdJsonDelete(id)

Delete a custom field

Deletes a custom field. 

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
    defaultClient.setBasePath("https://api.salesloft.com");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String id = "id_example"; // String | Custom Field ID
    try {
      apiInstance.v2CustomFieldsIdJsonDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#v2CustomFieldsIdJsonDelete");
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
| **id** | **String**| Custom Field ID | |

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
| **204** | The Custom Field has been deleted successfully |  -  |

<a id="v2CustomFieldsIdJsonGet"></a>
# **v2CustomFieldsIdJsonGet**
> CustomField v2CustomFieldsIdJsonGet(id)

Fetch a custom field

Fetches a custom field, by ID only. 

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
    defaultClient.setBasePath("https://api.salesloft.com");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String id = "id_example"; // String | Custom Field ID
    try {
      CustomField result = apiInstance.v2CustomFieldsIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#v2CustomFieldsIdJsonGet");
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
| **id** | **String**| Custom Field ID | |

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2CustomFieldsIdJsonPut"></a>
# **v2CustomFieldsIdJsonPut**
> CustomField v2CustomFieldsIdJsonPut(id, fieldType, name)

Update a custom field

Update a custom field. 

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
    defaultClient.setBasePath("https://api.salesloft.com");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String id = "id_example"; // String | Custom Field ID
    String fieldType = "fieldType_example"; // String | The field type of the custom field. Value must be one of: person, company, opportunity
    String name = "name_example"; // String | The name of the custom field
    try {
      CustomField result = apiInstance.v2CustomFieldsIdJsonPut(id, fieldType, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#v2CustomFieldsIdJsonPut");
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
| **id** | **String**| Custom Field ID | |
| **fieldType** | **String**| The field type of the custom field. Value must be one of: person, company, opportunity | [optional] |
| **name** | **String**| The name of the custom field | [optional] |

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2CustomFieldsJsonGet"></a>
# **v2CustomFieldsJsonGet**
> List&lt;CustomField&gt; v2CustomFieldsJsonGet(ids, fieldType, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List custom fields

Fetches multiple custom field records. The records can be filtered, paged, and sorted according to the respective parameters. 

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
    defaultClient.setBasePath("https://api.salesloft.com");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of custom fields to fetch.
    String fieldType = "fieldType_example"; // String | Type of field to fetch. Value must be one of: person, company, opportunity
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at, name. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<CustomField> result = apiInstance.v2CustomFieldsJsonGet(ids, fieldType, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#v2CustomFieldsJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of custom fields to fetch. | [optional] |
| **fieldType** | **String**| Type of field to fetch. Value must be one of: person, company, opportunity | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at, name. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;CustomField&gt;**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2CustomFieldsJsonPost"></a>
# **v2CustomFieldsJsonPost**
> CustomField v2CustomFieldsJsonPost(name, fieldType)

Create a custom field

Creates a custom field. 

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
    defaultClient.setBasePath("https://api.salesloft.com");

    CustomFieldsApi apiInstance = new CustomFieldsApi(defaultClient);
    String name = "name_example"; // String | The name of the custom field
    String fieldType = "fieldType_example"; // String | The field type of the custom field. Value must be one of: person, company, opportunity
    try {
      CustomField result = apiInstance.v2CustomFieldsJsonPost(name, fieldType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomFieldsApi#v2CustomFieldsJsonPost");
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
| **name** | **String**| The name of the custom field | |
| **fieldType** | **String**| The field type of the custom field. Value must be one of: person, company, opportunity | [optional] |

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

