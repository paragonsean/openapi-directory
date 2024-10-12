# EmailTemplatesApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2EmailTemplatesIdJsonGet**](EmailTemplatesApi.md#v2EmailTemplatesIdJsonGet) | **GET** /v2/email_templates/{id}.json | Fetch an email template |
| [**v2EmailTemplatesJsonGet**](EmailTemplatesApi.md#v2EmailTemplatesJsonGet) | **GET** /v2/email_templates.json | List email templates |


<a id="v2EmailTemplatesIdJsonGet"></a>
# **v2EmailTemplatesIdJsonGet**
> EmailTemplate v2EmailTemplatesIdJsonGet(id, includeSignature)

Fetch an email template

Fetches an email template, by ID only. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    EmailTemplatesApi apiInstance = new EmailTemplatesApi(defaultClient);
    String id = "id_example"; // String | EmailTemplate ID
    Boolean includeSignature = true; // Boolean | Optionally will return the templates with the current user's email signature
    try {
      EmailTemplate result = apiInstance.v2EmailTemplatesIdJsonGet(id, includeSignature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailTemplatesApi#v2EmailTemplatesIdJsonGet");
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
| **id** | **String**| EmailTemplate ID | |
| **includeSignature** | **Boolean**| Optionally will return the templates with the current user&#39;s email signature | [optional] |

### Return type

[**EmailTemplate**](EmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2EmailTemplatesJsonGet"></a>
# **v2EmailTemplatesJsonGet**
> List&lt;EmailTemplate&gt; v2EmailTemplatesJsonGet(ids, updatedAt, linkedToTeamTemplate, search, tagIds, tag, filterByOwner, groupId, includeCadenceTemplates, includeArchivedTemplates, cadenceId, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts)

List email templates

Fetches multiple email template records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    EmailTemplatesApi apiInstance = new EmailTemplatesApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of email templates to fetch. If a record can't be found, that record won't be returned and your request will be successful
    List<String> updatedAt = Arrays.asList(); // List<String> | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
    Boolean linkedToTeamTemplate = true; // Boolean | Filters email templates by whether they are linked to a team template or not
    String search = "search_example"; // String | Filters email templates by title or subject
    List<Integer> tagIds = Arrays.asList(); // List<Integer> | Filters email templates by tags applied to the template by tag ID, not to exceed 100 IDs
    List<String> tag = Arrays.asList(); // List<String> | Filters email templates by tags applied to the template, not to exceed 100 tags
    Boolean filterByOwner = true; // Boolean | Filters email templates by current authenticated user
    List<Integer> groupId = Arrays.asList(); // List<Integer> | Filters email templates by groups applied to the template by group ID. Not to exceed 500 IDs. Returns templates that are assigned to any of the group ids.
    Boolean includeCadenceTemplates = true; // Boolean | Filters email templates based on whether or not the template has been used on a cadence
    Boolean includeArchivedTemplates = true; // Boolean | Filters email templates to include archived templates or not
    List<Integer> cadenceId = Arrays.asList(); // List<Integer> | Filters email templates to those belonging to the cadence. Not to exceed 100 IDs. If a record can't be found, that record won't be returned and your request will be successful
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: created_at, updated_at, last_used_at. Defaults to updated_at
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    Integer perPage = 56; // Integer | How many records to show per page in the range [1, 100]. Defaults to 25
    Integer page = 56; // Integer | The current page to fetch results from. Defaults to 1
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean limitPagingCounts = true; // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
    try {
      List<EmailTemplate> result = apiInstance.v2EmailTemplatesJsonGet(ids, updatedAt, linkedToTeamTemplate, search, tagIds, tag, filterByOwner, groupId, includeCadenceTemplates, includeArchivedTemplates, cadenceId, sortBy, sortDirection, perPage, page, includePagingCounts, limitPagingCounts);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailTemplatesApi#v2EmailTemplatesJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of email templates to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **updatedAt** | [**List&lt;String&gt;**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] |
| **linkedToTeamTemplate** | **Boolean**| Filters email templates by whether they are linked to a team template or not | [optional] |
| **search** | **String**| Filters email templates by title or subject | [optional] |
| **tagIds** | [**List&lt;Integer&gt;**](Integer.md)| Filters email templates by tags applied to the template by tag ID, not to exceed 100 IDs | [optional] |
| **tag** | [**List&lt;String&gt;**](String.md)| Filters email templates by tags applied to the template, not to exceed 100 tags | [optional] |
| **filterByOwner** | **Boolean**| Filters email templates by current authenticated user | [optional] |
| **groupId** | [**List&lt;Integer&gt;**](Integer.md)| Filters email templates by groups applied to the template by group ID. Not to exceed 500 IDs. Returns templates that are assigned to any of the group ids. | [optional] |
| **includeCadenceTemplates** | **Boolean**| Filters email templates based on whether or not the template has been used on a cadence | [optional] |
| **includeArchivedTemplates** | **Boolean**| Filters email templates to include archived templates or not | [optional] |
| **cadenceId** | [**List&lt;Integer&gt;**](Integer.md)| Filters email templates to those belonging to the cadence. Not to exceed 100 IDs. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at, last_used_at. Defaults to updated_at | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |
| **perPage** | **Integer**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] |
| **page** | **Integer**| The current page to fetch results from. Defaults to 1 | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] |

### Return type

[**List&lt;EmailTemplate&gt;**](EmailTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

