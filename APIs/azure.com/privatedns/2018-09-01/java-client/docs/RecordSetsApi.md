# RecordSetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recordSetsCreateOrUpdate**](RecordSetsApi.md#recordSetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/{recordType}/{relativeRecordSetName} |  |
| [**recordSetsDelete**](RecordSetsApi.md#recordSetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/{recordType}/{relativeRecordSetName} |  |
| [**recordSetsGet**](RecordSetsApi.md#recordSetsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/{recordType}/{relativeRecordSetName} |  |
| [**recordSetsList**](RecordSetsApi.md#recordSetsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/ALL |  |
| [**recordSetsListByType**](RecordSetsApi.md#recordSetsListByType) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/{recordType} |  |
| [**recordSetsUpdate**](RecordSetsApi.md#recordSetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/{recordType}/{relativeRecordSetName} |  |


<a id="recordSetsCreateOrUpdate"></a>
# **recordSetsCreateOrUpdate**
> RecordSet recordSetsCreateOrUpdate(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch)



Creates or updates a record set within a Private DNS zone.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String recordType = "A"; // String | The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the Private DNS zone is created).
    String relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    RecordSet parameters = new RecordSet(); // RecordSet | Parameters supplied to the CreateOrUpdate operation.
    String ifMatch = "ifMatch_example"; // String | The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored.
    try {
      RecordSet result = apiInstance.recordSetsCreateOrUpdate(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch);
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **recordType** | **String**| The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the Private DNS zone is created). | [enum: A, AAAA, CNAME, MX, PTR, SOA, SRV, TXT] |
| **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**RecordSet**](RecordSet.md)| Parameters supplied to the CreateOrUpdate operation. | |
| **ifMatch** | **String**| The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes. | [optional] |
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
> recordSetsDelete(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, ifMatch)



Deletes a record set from a Private DNS zone. This operation cannot be undone.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String recordType = "A"; // String | The type of DNS record in this record set. Record sets of type SOA cannot be deleted (they are deleted when the Private DNS zone is deleted).
    String relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String ifMatch = "ifMatch_example"; // String | The ETag of the record set. Omit this value to always delete the current record set. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
    try {
      apiInstance.recordSetsDelete(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, ifMatch);
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **recordType** | **String**| The type of DNS record in this record set. Record sets of type SOA cannot be deleted (they are deleted when the Private DNS zone is deleted). | [enum: A, AAAA, CNAME, MX, PTR, SOA, SRV, TXT] |
| **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **ifMatch** | **String**| The ETag of the record set. Omit this value to always delete the current record set. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes. | [optional] |

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
> RecordSet recordSetsGet(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId)



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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String recordType = "A"; // String | The type of DNS record in this record set.
    String relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      RecordSet result = apiInstance.recordSetsGet(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId);
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **recordType** | **String**| The type of DNS record in this record set. | [enum: A, AAAA, CNAME, MX, PTR, SOA, SRV, TXT] |
| **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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

<a id="recordSetsList"></a>
# **recordSetsList**
> RecordSetListResult recordSetsList(resourceGroupName, privateZoneName, apiVersion, subscriptionId, $top, $recordsetnamesuffix)



Lists all record sets in a Private DNS zone.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    String $recordsetnamesuffix = "$recordsetnamesuffix_example"; // String | The suffix label of the record set name to be used to filter the record set enumeration. If this parameter is specified, the returned enumeration will only contain records that end with \".<recordsetnamesuffix>\".
    try {
      RecordSetListResult result = apiInstance.recordSetsList(resourceGroupName, privateZoneName, apiVersion, subscriptionId, $top, $recordsetnamesuffix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordSetsApi#recordSetsList");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] |
| **$recordsetnamesuffix** | **String**| The suffix label of the record set name to be used to filter the record set enumeration. If this parameter is specified, the returned enumeration will only contain records that end with \&quot;.&lt;recordsetnamesuffix&gt;\&quot;. | [optional] |

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
> RecordSetListResult recordSetsListByType(resourceGroupName, privateZoneName, recordType, apiVersion, subscriptionId, $top, $recordsetnamesuffix)



Lists the record sets of a specified type in a Private DNS zone.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String recordType = "A"; // String | The type of record sets to enumerate.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    String $recordsetnamesuffix = "$recordsetnamesuffix_example"; // String | The suffix label of the record set name to be used to filter the record set enumeration. If this parameter is specified, the returned enumeration will only contain records that end with \".<recordsetnamesuffix>\".
    try {
      RecordSetListResult result = apiInstance.recordSetsListByType(resourceGroupName, privateZoneName, recordType, apiVersion, subscriptionId, $top, $recordsetnamesuffix);
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **recordType** | **String**| The type of record sets to enumerate. | [enum: A, AAAA, CNAME, MX, PTR, SOA, SRV, TXT] |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] |
| **$recordsetnamesuffix** | **String**| The suffix label of the record set name to be used to filter the record set enumeration. If this parameter is specified, the returned enumeration will only contain records that end with \&quot;.&lt;recordsetnamesuffix&gt;\&quot;. | [optional] |

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
> RecordSet recordSetsUpdate(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, parameters, ifMatch)



Updates a record set within a Private DNS zone.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String recordType = "A"; // String | The type of DNS record in this record set.
    String relativeRecordSetName = "relativeRecordSetName_example"; // String | The name of the record set, relative to the name of the zone.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    RecordSet parameters = new RecordSet(); // RecordSet | Parameters supplied to the Update operation.
    String ifMatch = "ifMatch_example"; // String | The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    try {
      RecordSet result = apiInstance.recordSetsUpdate(resourceGroupName, privateZoneName, recordType, relativeRecordSetName, apiVersion, subscriptionId, parameters, ifMatch);
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **recordType** | **String**| The type of DNS record in this record set. | [enum: A, AAAA, CNAME, MX, PTR, SOA, SRV, TXT] |
| **relativeRecordSetName** | **String**| The name of the record set, relative to the name of the zone. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**RecordSet**](RecordSet.md)| Parameters supplied to the Update operation. | |
| **ifMatch** | **String**| The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. | [optional] |

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

