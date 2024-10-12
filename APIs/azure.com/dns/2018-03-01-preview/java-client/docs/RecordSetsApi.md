# RecordSetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recordSetsCreateOrUpdate**](RecordSetsApi.md#recordSetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName} |  |
| [**recordSetsDelete**](RecordSetsApi.md#recordSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName} |  |
| [**recordSetsGet**](RecordSetsApi.md#recordSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName} |  |
| [**recordSetsListAllByDnsZone**](RecordSetsApi.md#recordSetsListAllByDnsZone) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/all |  |
| [**recordSetsListByDnsZone**](RecordSetsApi.md#recordSetsListByDnsZone) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/recordsets |  |
| [**recordSetsListByType**](RecordSetsApi.md#recordSetsListByType) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType} |  |
| [**recordSetsUpdate**](RecordSetsApi.md#recordSetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName}/{recordType}/{relativeRecordSetName} |  |


<a id="recordSetsCreateOrUpdate"></a>
# **recordSetsCreateOrUpdate**
> RecordSet recordSetsCreateOrUpdate(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch)



Creates or updates a record set within a DNS zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RecordSetsApi apiInstance = new RecordSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
    String recordType = "A"; // String | The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the DNS zone is created).
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    RecordSet parameters = new RecordSet(); // RecordSet | Parameters supplied to the CreateOrUpdate operation.
    String ifMatch = "ifMatch_example"; // String | The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored.
    try {
      RecordSet result = apiInstance.recordSetsCreateOrUpdate(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordSetsApi#recordSetsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | |
| **recordType** | **String**| The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the DNS zone is created). | [enum: A, AAAA, CAA, CNAME, MX, NS, PTR, SOA, SRV, TXT] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**RecordSet**](RecordSet.md)| Parameters supplied to the CreateOrUpdate operation. | |
| **ifMatch** | **String**| The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes. | [optional] |
| **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored. | [optional] |

### Return type

[**RecordSet**](RecordSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The record set has been updated. |  -  |
| **201** | The record set has been created. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="recordSetsDelete"></a>
# **recordSetsDelete**
> recordSetsDelete(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, ifMatch)



Deletes a record set from a DNS zone. This operation cannot be undone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RecordSetsApi apiInstance = new RecordSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
    String recordType = "A"; // String | The type of DNS record in this record set. Record sets of type SOA cannot be deleted (they are deleted when the DNS zone is deleted).
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String ifMatch = "ifMatch_example"; // String | The etag of the record set. Omit this value to always delete the current record set. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes.
    try {
      apiInstance.recordSetsDelete(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordSetsApi#recordSetsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | |
| **recordType** | **String**| The type of DNS record in this record set. Record sets of type SOA cannot be deleted (they are deleted when the DNS zone is deleted). | [enum: A, AAAA, CAA, CNAME, MX, NS, PTR, SOA, SRV, TXT] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **ifMatch** | **String**| The etag of the record set. Omit this value to always delete the current record set. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The record set has been deleted. |  -  |
| **204** | The record set was not found. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="recordSetsGet"></a>
# **recordSetsGet**
> RecordSet recordSetsGet(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId)



Gets a record set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RecordSetsApi apiInstance = new RecordSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
    String recordType = "A"; // String | The type of DNS record in this record set.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      RecordSet result = apiInstance.recordSetsGet(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordSetsApi#recordSetsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | |
| **recordType** | **String**| The type of DNS record in this record set. | [enum: A, AAAA, CAA, CNAME, MX, NS, PTR, SOA, SRV, TXT] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**RecordSet**](RecordSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="recordSetsListAllByDnsZone"></a>
# **recordSetsListAllByDnsZone**
> RecordSetListResult recordSetsListAllByDnsZone(resourceGroupName, zoneName, apiVersion, subscriptionId, $top, $recordsetnamesuffix)



Lists all record sets in a DNS zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RecordSetsApi apiInstance = new RecordSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Integer $top = 56; // Integer | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    String $recordsetnamesuffix = "$recordsetnamesuffix_example"; // String | The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .<recordSetNameSuffix>
    try {
      RecordSetListResult result = apiInstance.recordSetsListAllByDnsZone(resourceGroupName, zoneName, apiVersion, subscriptionId, $top, $recordsetnamesuffix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordSetsApi#recordSetsListAllByDnsZone");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$top** | **Integer**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] |
| **$recordsetnamesuffix** | **String**| The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .&lt;recordSetNameSuffix&gt; | [optional] |

### Return type

[**RecordSetListResult**](RecordSetListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="recordSetsListByDnsZone"></a>
# **recordSetsListByDnsZone**
> RecordSetListResult recordSetsListByDnsZone(resourceGroupName, zoneName, apiVersion, subscriptionId, $top, $recordsetnamesuffix)



Lists all record sets in a DNS zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RecordSetsApi apiInstance = new RecordSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Integer $top = 56; // Integer | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    String $recordsetnamesuffix = "$recordsetnamesuffix_example"; // String | The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .<recordSetNameSuffix>
    try {
      RecordSetListResult result = apiInstance.recordSetsListByDnsZone(resourceGroupName, zoneName, apiVersion, subscriptionId, $top, $recordsetnamesuffix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordSetsApi#recordSetsListByDnsZone");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$top** | **Integer**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] |
| **$recordsetnamesuffix** | **String**| The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .&lt;recordSetNameSuffix&gt; | [optional] |

### Return type

[**RecordSetListResult**](RecordSetListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="recordSetsListByType"></a>
# **recordSetsListByType**
> RecordSetListResult recordSetsListByType(resourceGroupName, zoneName, recordType, apiVersion, subscriptionId, $top, $recordsetnamesuffix)



Lists the record sets of a specified type in a DNS zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RecordSetsApi apiInstance = new RecordSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String recordType = "A"; // String | The type of record sets to enumerate.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Integer $top = 56; // Integer | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    String $recordsetnamesuffix = "$recordsetnamesuffix_example"; // String | The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .<recordSetNameSuffix>
    try {
      RecordSetListResult result = apiInstance.recordSetsListByType(resourceGroupName, zoneName, recordType, apiVersion, subscriptionId, $top, $recordsetnamesuffix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordSetsApi#recordSetsListByType");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **recordType** | **String**| The type of record sets to enumerate. | [enum: A, AAAA, CAA, CNAME, MX, NS, PTR, SOA, SRV, TXT] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$top** | **Integer**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] |
| **$recordsetnamesuffix** | **String**| The suffix label of the record set name that has to be used to filter the record set enumerations. If this parameter is specified, Enumeration will return only records that end with .&lt;recordSetNameSuffix&gt; | [optional] |

### Return type

[**RecordSetListResult**](RecordSetListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="recordSetsUpdate"></a>
# **recordSetsUpdate**
> RecordSet recordSetsUpdate(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, parameters, ifMatch)



Updates a record set within a DNS zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    RecordSetsApi apiInstance = new RecordSetsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
    String recordType = "A"; // String | The type of DNS record in this record set.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    RecordSet parameters = new RecordSet(); // RecordSet | Parameters supplied to the Update operation.
    String ifMatch = "ifMatch_example"; // String | The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting concurrent changes.
    try {
      RecordSet result = apiInstance.recordSetsUpdate(resourceGroupName, zoneName, relativeRecordSetName, recordType, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordSetsApi#recordSetsUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | |
| **recordType** | **String**| The type of DNS record in this record set. | [enum: A, AAAA, CAA, CNAME, MX, NS, PTR, SOA, SRV, TXT] |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**RecordSet**](RecordSet.md)| Parameters supplied to the Update operation. | |
| **ifMatch** | **String**| The etag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen etag value to prevent accidentally overwriting concurrent changes. | [optional] |

### Return type

[**RecordSet**](RecordSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The record set has been updated. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

