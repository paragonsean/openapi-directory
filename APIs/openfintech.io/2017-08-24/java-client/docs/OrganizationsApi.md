# OrganizationsApi

All URIs are relative to *https://api.openfintech.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**organizationsGet**](OrganizationsApi.md#organizationsGet) | **GET** /organizations | List of organizations |
| [**organizationsIdGet**](OrganizationsApi.md#organizationsIdGet) | **GET** /organizations/{id} | Organization by ID |


<a id="organizationsGet"></a>
# **organizationsGet**
> OrganizationsResponse organizationsGet(pageNumber, pageSize, filterSearch, filterName, filterCode, filterStatus, filterIndustries, sort)

List of organizations

This endpoint retrievs the list of organizations present in the system. The data displays general, public information, without reference to the type of activity (for example - name, address, contacts, etc.). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    Integer pageNumber = 56; // Integer | Current page number.
    Integer pageSize = 56; // Integer | Page size.<br>*Default value: 100* 
    String filterSearch = "filterSearch_example"; // String | Full text search with id, name, code.
    String filterName = "filterName_example"; // String | Filtering by name.
    String filterCode = "filterCode_example"; // String | Filtering by code.
    Set<String> filterStatus = Arrays.asList(); // Set<String> | Filtration by status.
    String filterIndustries = "filterIndustries_example"; // String | Filtering by industries.
    Set<String> sort = Arrays.asList(); // Set<String> | Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | description | -description | 
    try {
      OrganizationsResponse result = apiInstance.organizationsGet(pageNumber, pageSize, filterSearch, filterName, filterCode, filterStatus, filterIndustries, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#organizationsGet");
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
| **pageNumber** | **Integer**| Current page number. | [optional] |
| **pageSize** | **Integer**| Page size.&lt;br&gt;*Default value: 100*  | [optional] |
| **filterSearch** | **String**| Full text search with id, name, code. | [optional] |
| **filterName** | **String**| Filtering by name. | [optional] |
| **filterCode** | **String**| Filtering by code. | [optional] |
| **filterStatus** | [**Set&lt;String&gt;**](String.md)| Filtration by status. | [optional] [enum: active, blocked, deleted] |
| **filterIndustries** | **String**| Filtering by industries. | [optional] |
| **sort** | [**Set&lt;String&gt;**](String.md)| Sort params:&lt;br&gt;  | ASC | DESC | |-----|------| | name | -name | | code | -code | | status | -status | | description | -description |  | [optional] [enum: name, -name, code, -code, status, -status, description, -description] |

### Return type

[**OrganizationsResponse**](OrganizationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Organizations. |  -  |

<a id="organizationsIdGet"></a>
# **organizationsIdGet**
> OrganizationResponse organizationsIdGet(id)

Organization by ID

Returns organization with specific ID. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.openfintech.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String id = "id_example"; // String | Unique ID.
    try {
      OrganizationResponse result = apiInstance.organizationsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#organizationsIdGet");
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
| **id** | **String**| Unique ID. | |

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization information. |  -  |
| **404** | Organization ID is not valid. |  -  |

