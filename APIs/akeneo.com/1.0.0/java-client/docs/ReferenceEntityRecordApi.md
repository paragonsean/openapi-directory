# ReferenceEntityRecordApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getReferenceEntityRecords**](ReferenceEntityRecordApi.md#getReferenceEntityRecords) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/records | Get the list of the records of a reference entity |
| [**getReferenceEntityRecordsCode**](ReferenceEntityRecordApi.md#getReferenceEntityRecordsCode) | **GET** /api/rest/v1/reference-entities/{reference_entity_code}/records/{code} | Get a record of a given reference entity |
| [**patchReferenceEntityRecords**](ReferenceEntityRecordApi.md#patchReferenceEntityRecords) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/records | Update/create several reference entity records |
| [**patchReferenceEntityRecordsCode**](ReferenceEntityRecordApi.md#patchReferenceEntityRecordsCode) | **PATCH** /api/rest/v1/reference-entities/{reference_entity_code}/records/{code} | Update/create a record of a given reference entity |


<a id="getReferenceEntityRecords"></a>
# **getReferenceEntityRecords**
> ReferenceEntityRecord getReferenceEntityRecords(referenceEntityCode, search, channel, locales, searchAfter)

Get the list of the records of a reference entity

This endpoint allows you to get a list of records of a given reference entity. Records are paginated and can be filtered.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityRecordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityRecordApi apiInstance = new ReferenceEntityRecordApi(defaultClient);
    String referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
    String search = "search_example"; // String | Filter records of the reference entity, for more details see the <a href=\"/documentation/filter.html#filter-reference-entity-records\">Filters</a> section
    String channel = "channel_example"; // String | Filter attribute values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#record-values-by-channel\">Filter attribute values by channel</a> section
    String locales = "locales_example"; // String | Filter attribute values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the <a href=\"/documentation/filter.html#record-values-by-locale\">Filter attribute values by locale</a> section
    String searchAfter = "cursor to the first page"; // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    try {
      ReferenceEntityRecord result = apiInstance.getReferenceEntityRecords(referenceEntityCode, search, channel, locales, searchAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityRecordApi#getReferenceEntityRecords");
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
| **referenceEntityCode** | **String**| Code of the reference entity | |
| **search** | **String**| Filter records of the reference entity, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-reference-entity-records\&quot;&gt;Filters&lt;/a&gt; section | [optional] |
| **channel** | **String**| Filter attribute values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#record-values-by-channel\&quot;&gt;Filter attribute values by channel&lt;/a&gt; section | [optional] |
| **locales** | **String**| Filter attribute values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#record-values-by-locale\&quot;&gt;Filter attribute values by locale&lt;/a&gt; section | [optional] |
| **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page] |

### Return type

[**ReferenceEntityRecord**](ReferenceEntityRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, _embedded, _links, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the records of the given reference entity paginated |  -  |
| **401** | Authentication required |  -  |
| **406** | Not Acceptable |  -  |

<a id="getReferenceEntityRecordsCode"></a>
# **getReferenceEntityRecordsCode**
> PatchReferenceEntityRecordsRequestInner getReferenceEntityRecordsCode(referenceEntityCode, code)

Get a record of a given reference entity

This endpoint allows you to get the information about a given record for a given reference entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityRecordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityRecordApi apiInstance = new ReferenceEntityRecordApi(defaultClient);
    String referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
    String code = "code_example"; // String | Code of the resource
    try {
      PatchReferenceEntityRecordsRequestInner result = apiInstance.getReferenceEntityRecordsCode(referenceEntityCode, code);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityRecordApi#getReferenceEntityRecordsCode");
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
| **referenceEntityCode** | **String**| Code of the reference entity | |
| **code** | **String**| Code of the resource | |

### Return type

[**PatchReferenceEntityRecordsRequestInner**](PatchReferenceEntityRecordsRequestInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Authentication required |  -  |
| **404** | Resource not found |  -  |
| **406** | Not Acceptable |  -  |

<a id="patchReferenceEntityRecords"></a>
# **patchReferenceEntityRecords**
> List&lt;PatchAssets200ResponseInner&gt; patchReferenceEntityRecords(referenceEntityCode, body)

Update/create several reference entity records

This endpoint allows you to update and/or create several records of one given reference entity at once. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#patch-reference-entity-record-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the record does not already exist for the given reference entity, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityRecordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityRecordApi apiInstance = new ReferenceEntityRecordApi(defaultClient);
    String referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
    List<PatchReferenceEntityRecordsRequestInner> body = Arrays.asList(); // List<PatchReferenceEntityRecordsRequestInner> | 
    try {
      List<PatchAssets200ResponseInner> result = apiInstance.patchReferenceEntityRecords(referenceEntityCode, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityRecordApi#patchReferenceEntityRecords");
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
| **referenceEntityCode** | **String**| Code of the reference entity | |
| **body** | [**List&lt;PatchReferenceEntityRecordsRequestInner&gt;**](PatchReferenceEntityRecordsRequestInner.md)|  | |

### Return type

[**List&lt;PatchAssets200ResponseInner&gt;**](PatchAssets200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Authentication required |  -  |
| **413** | Request Entity Too Large |  -  |
| **415** | Unsupported Media type |  -  |

<a id="patchReferenceEntityRecordsCode"></a>
# **patchReferenceEntityRecordsCode**
> patchReferenceEntityRecordsCode(referenceEntityCode, code, body)

Update/create a record of a given reference entity

This endpoint allows you to update a given record of a given renference entity. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#patch-reference-entity-record-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the record does not already exist for the given reference entity, it creates it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceEntityRecordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    ReferenceEntityRecordApi apiInstance = new ReferenceEntityRecordApi(defaultClient);
    String referenceEntityCode = "referenceEntityCode_example"; // String | Code of the reference entity
    String code = "code_example"; // String | Code of the resource
    PatchReferenceEntityRecordsCodeRequest body = new PatchReferenceEntityRecordsCodeRequest(); // PatchReferenceEntityRecordsCodeRequest | 
    try {
      apiInstance.patchReferenceEntityRecordsCode(referenceEntityCode, code, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceEntityRecordApi#patchReferenceEntityRecordsCode");
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
| **referenceEntityCode** | **String**| Code of the reference entity | |
| **code** | **String**| Code of the resource | |
| **body** | [**PatchReferenceEntityRecordsCodeRequest**](PatchReferenceEntityRecordsCodeRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message, _links

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - URI of the created resource <br>  |
| **204** | No content to return |  * Location - URI of the created resource <br>  |
| **401** | Authentication required |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

