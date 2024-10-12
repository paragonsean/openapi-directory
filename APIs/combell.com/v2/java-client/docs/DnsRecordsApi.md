# DnsRecordsApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dnsDomainNameRecordsGet**](DnsRecordsApi.md#dnsDomainNameRecordsGet) | **GET** /dns/{domainName}/records | Get records |
| [**dnsDomainNameRecordsPost**](DnsRecordsApi.md#dnsDomainNameRecordsPost) | **POST** /dns/{domainName}/records | Create a record |
| [**dnsDomainNameRecordsRecordIdDelete**](DnsRecordsApi.md#dnsDomainNameRecordsRecordIdDelete) | **DELETE** /dns/{domainName}/records/{recordId} | Delete a record |
| [**dnsDomainNameRecordsRecordIdGet**](DnsRecordsApi.md#dnsDomainNameRecordsRecordIdGet) | **GET** /dns/{domainName}/records/{recordId} | Get specific record |
| [**dnsDomainNameRecordsRecordIdPut**](DnsRecordsApi.md#dnsDomainNameRecordsRecordIdPut) | **PUT** /dns/{domainName}/records/{recordId} | Edit a record |


<a id="dnsDomainNameRecordsGet"></a>
# **dnsDomainNameRecordsGet**
> List&lt;DnsRecord&gt; dnsDomainNameRecordsGet(domainName, domainName2, skip, take, type, recordName, service)

Get records

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsRecordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DnsRecordsApi apiInstance = new DnsRecordsApi(defaultClient);
    String domainName = "domainName_example"; // String | The domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    Integer skip = 56; // Integer | The number of items to skip in the resultset.
    Integer take = 56; // Integer | The number of items to return in the resultset. The returned count can be equal or less than this number.
    String type = "type_example"; // String | Filters records matching the type. Most other filters only apply when this filter is specified.
    String recordName = "recordName_example"; // String | Filters records matching the record name. This filter only applies to lookups of A, CNAME, TXT, CAA, ALIAS and TLSA records.
    String service = "service_example"; // String | Filters records for the service. This filter only applies to lookups of SRV records.
    try {
      List<DnsRecord> result = apiInstance.dnsDomainNameRecordsGet(domainName, domainName2, skip, take, type, recordName, service);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsRecordsApi#dnsDomainNameRecordsGet");
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
| **domainName** | **String**| The domain name. | |
| **domainName2** | **String**| Automatically added | |
| **skip** | **Integer**| The number of items to skip in the resultset. | [optional] |
| **take** | **Integer**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] |
| **type** | **String**| Filters records matching the type. Most other filters only apply when this filter is specified. | [optional] |
| **recordName** | **String**| Filters records matching the record name. This filter only applies to lookups of A, CNAME, TXT, CAA, ALIAS and TLSA records. | [optional] |
| **service** | **String**| Filters records for the service. This filter only applies to lookups of SRV records. | [optional] |

### Return type

[**List&lt;DnsRecord&gt;**](DnsRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  |

<a id="dnsDomainNameRecordsPost"></a>
# **dnsDomainNameRecordsPost**
> dnsDomainNameRecordsPost(domainName, domainName2, dnsRecord)

Create a record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsRecordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DnsRecordsApi apiInstance = new DnsRecordsApi(defaultClient);
    String domainName = "domainName_example"; // String | The domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    DnsRecord dnsRecord = new DnsRecord(); // DnsRecord | The record to create
    try {
      apiInstance.dnsDomainNameRecordsPost(domainName, domainName2, dnsRecord);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsRecordsApi#dnsDomainNameRecordsPost");
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
| **domainName** | **String**| The domain name. | |
| **domainName2** | **String**| Automatically added | |
| **dnsRecord** | [**DnsRecord**](DnsRecord.md)| The record to create | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  * Location - The location referring to a resource that replaced the original resource. <br>  |

<a id="dnsDomainNameRecordsRecordIdDelete"></a>
# **dnsDomainNameRecordsRecordIdDelete**
> dnsDomainNameRecordsRecordIdDelete(domainName, recordId, domainName2, recordId2)

Delete a record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsRecordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DnsRecordsApi apiInstance = new DnsRecordsApi(defaultClient);
    String domainName = "domainName_example"; // String | The domain name.
    String recordId = "recordId_example"; // String | The id of the record.
    String domainName2 = "domainName_example"; // String | Automatically added
    String recordId2 = "recordId_example"; // String | Automatically added
    try {
      apiInstance.dnsDomainNameRecordsRecordIdDelete(domainName, recordId, domainName2, recordId2);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsRecordsApi#dnsDomainNameRecordsRecordIdDelete");
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
| **domainName** | **String**| The domain name. | |
| **recordId** | **String**| The id of the record. | |
| **domainName2** | **String**| Automatically added | |
| **recordId2** | **String**| Automatically added | |

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
| **204** | Success |  -  |

<a id="dnsDomainNameRecordsRecordIdGet"></a>
# **dnsDomainNameRecordsRecordIdGet**
> DnsRecord dnsDomainNameRecordsRecordIdGet(domainName, recordId, domainName2, recordId2)

Get specific record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsRecordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DnsRecordsApi apiInstance = new DnsRecordsApi(defaultClient);
    String domainName = "domainName_example"; // String | The domain name.
    String recordId = "recordId_example"; // String | The id of the record.
    String domainName2 = "domainName_example"; // String | Automatically added
    String recordId2 = "recordId_example"; // String | Automatically added
    try {
      DnsRecord result = apiInstance.dnsDomainNameRecordsRecordIdGet(domainName, recordId, domainName2, recordId2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsRecordsApi#dnsDomainNameRecordsRecordIdGet");
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
| **domainName** | **String**| The domain name. | |
| **recordId** | **String**| The id of the record. | |
| **domainName2** | **String**| Automatically added | |
| **recordId2** | **String**| Automatically added | |

### Return type

[**DnsRecord**](DnsRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="dnsDomainNameRecordsRecordIdPut"></a>
# **dnsDomainNameRecordsRecordIdPut**
> dnsDomainNameRecordsRecordIdPut(domainName, recordId, domainName2, recordId2, dnsRecord)

Edit a record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsRecordsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    DnsRecordsApi apiInstance = new DnsRecordsApi(defaultClient);
    String domainName = "domainName_example"; // String | The domain name.
    String recordId = "recordId_example"; // String | The id of the record.
    String domainName2 = "domainName_example"; // String | Automatically added
    String recordId2 = "recordId_example"; // String | Automatically added
    DnsRecord dnsRecord = new DnsRecord(); // DnsRecord | The record with updated values.
    try {
      apiInstance.dnsDomainNameRecordsRecordIdPut(domainName, recordId, domainName2, recordId2, dnsRecord);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsRecordsApi#dnsDomainNameRecordsRecordIdPut");
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
| **domainName** | **String**| The domain name. | |
| **recordId** | **String**| The id of the record. | |
| **domainName2** | **String**| Automatically added | |
| **recordId2** | **String**| Automatically added | |
| **dnsRecord** | [**DnsRecord**](DnsRecord.md)| The record with updated values. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

