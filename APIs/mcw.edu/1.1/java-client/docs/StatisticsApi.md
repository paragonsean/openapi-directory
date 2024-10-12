# StatisticsApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getActiveObjectCountUsingGET**](StatisticsApi.md#getActiveObjectCountUsingGET) | **GET** /stats/count/activeObject/{speciesTypeKey}/{dateYYYYMMDD} | Count of active objects by type, for specified species and date |
| [**getActiveObjectDiffUsingGET**](StatisticsApi.md#getActiveObjectDiffUsingGET) | **GET** /stats/diff/activeObject/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of active objects, by type, for specified species and date range |
| [**getGeneTypeCountUsingGET**](StatisticsApi.md#getGeneTypeCountUsingGET) | **GET** /stats/count/geneType/{speciesTypeKey}/{dateYYYYMMDD} | Count of gene types, for specified species and date |
| [**getGeneTypeDiffUsingGET**](StatisticsApi.md#getGeneTypeDiffUsingGET) | **GET** /stats/diff/geneType/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of gene types, for specified species and date range |
| [**getObjectStatusCountUsingGET**](StatisticsApi.md#getObjectStatusCountUsingGET) | **GET** /stats/count/objectStatus/{speciesTypeKey}/{dateYYYYMMDD} | Count of objects with given status, for specified species and date |
| [**getObjectStatusDiffUsingGET**](StatisticsApi.md#getObjectStatusDiffUsingGET) | **GET** /stats/diff/objectStatus/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of objects with given status, for specified species and date range |
| [**getObjectsWithRefSeqCountUsingGET**](StatisticsApi.md#getObjectsWithRefSeqCountUsingGET) | **GET** /stats/count/objectWithRefSeq/{speciesTypeKey}/{dateYYYYMMDD} | Count of objects with reference sequence(s), by object type, for specified species and date |
| [**getObjectsWithRefSeqDiffUsingGET**](StatisticsApi.md#getObjectsWithRefSeqDiffUsingGET) | **GET** /stats/diff/objectWithRefSeq/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of objects with reference sequence(s), by object type, for specified species and date range |
| [**getObjectsWithReferenceCountUsingGET**](StatisticsApi.md#getObjectsWithReferenceCountUsingGET) | **GET** /stats/count/objectWithReference/{speciesTypeKey}/{dateYYYYMMDD} | Count of objects with reference, by object type, for specified species and date |
| [**getObjectsWithReferenceDiffUsingGET**](StatisticsApi.md#getObjectsWithReferenceDiffUsingGET) | **GET** /stats/diff/objectWithReference/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of objects with reference, by object type, for specified species and date range |
| [**getObjectsWithXDBsCountUsingGET**](StatisticsApi.md#getObjectsWithXDBsCountUsingGET) | **GET** /stats/count/objectWithXdb/{speciesTypeKey}/{objectKey}/{dateYYYYMMDD} | Count of objects with external database ids, by database id, for specified species, object type and date |
| [**getObjectsWithXDBsDiffUsingGET**](StatisticsApi.md#getObjectsWithXDBsDiffUsingGET) | **GET** /stats/diff/objectWithXdb/{speciesTypeKey}/{objectKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of objects with external database ids, by database id, for specified species, object type and date range |
| [**getProteinInteractionCountUsingGET**](StatisticsApi.md#getProteinInteractionCountUsingGET) | **GET** /stats/count/proteinInteraction/{speciesTypeKey}/{dateYYYYMMDD} | Count of protein interactions, for specified species and date |
| [**getProteinInteractionDiffUsingGET**](StatisticsApi.md#getProteinInteractionDiffUsingGET) | **GET** /stats/diff/proteinInteraction/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of protein interactions, for specified species and date range |
| [**getQtlInheritanceTypeCountUsingGET**](StatisticsApi.md#getQtlInheritanceTypeCountUsingGET) | **GET** /stats/count/qtlInheritanceType/{speciesTypeKey}/{dateYYYYMMDD} | Count of strains, by qtl inheritance type, for specified species and date |
| [**getQtlInheritanceTypeDiffUsingGET**](StatisticsApi.md#getQtlInheritanceTypeDiffUsingGET) | **GET** /stats/diff/qtlInheritanceType/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of strains, by qtl inheritance type, for specified species and date range |
| [**getRetiredObjectCountUsingGET**](StatisticsApi.md#getRetiredObjectCountUsingGET) | **GET** /stats/count/retiredObject/{speciesTypeKey}/{dateYYYYMMDD} | Count of retired objects by type, for specified species and date |
| [**getRetiredObjectDiffUsingGET**](StatisticsApi.md#getRetiredObjectDiffUsingGET) | **GET** /stats/diff/retiredObject/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of retired objects, by type, for specified species and date range |
| [**getStrainTypeCountUsingGET**](StatisticsApi.md#getStrainTypeCountUsingGET) | **GET** /stats/count/strainType/{speciesTypeKey}/{dateYYYYMMDD} | Count of strain types, for specified species and date |
| [**getStrainTypeDiffUsingGET**](StatisticsApi.md#getStrainTypeDiffUsingGET) | **GET** /stats/diff/strainType/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of strain types, for specified species and date range |
| [**getTermStatsUsingGET**](StatisticsApi.md#getTermStatsUsingGET) | **GET** /stats/term/{accId}/{filterAccId} | getTermStats |
| [**getWithdrawnObjectCountUsingGET**](StatisticsApi.md#getWithdrawnObjectCountUsingGET) | **GET** /stats/count/withdrawnObject/{speciesTypeKey}/{dateYYYYMMDD} | Count of withdrawn objects by type, for specified species and date |
| [**getWithdrawnObjectDiffUsingGET**](StatisticsApi.md#getWithdrawnObjectDiffUsingGET) | **GET** /stats/diff/withdrawnObject/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of withdrawn objects, by type, for specified species and date range |
| [**getXdbsCountUsingGET**](StatisticsApi.md#getXdbsCountUsingGET) | **GET** /stats/count/xdb/{speciesTypeKey}/{dateYYYYMMDD} | Count of external database ids, for specied species and date |
| [**getXdbsDiffUsingGET**](StatisticsApi.md#getXdbsDiffUsingGET) | **GET** /stats/diff/xdb/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of external database ids, for specified species and date range |


<a id="getActiveObjectCountUsingGET"></a>
# **getActiveObjectCountUsingGET**
> Map&lt;String, String&gt; getActiveObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of active objects by type, for specified species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getActiveObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getActiveObjectCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getActiveObjectDiffUsingGET"></a>
# **getActiveObjectDiffUsingGET**
> Map&lt;String, String&gt; getActiveObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of active objects, by type, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getActiveObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getActiveObjectDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getGeneTypeCountUsingGET"></a>
# **getGeneTypeCountUsingGET**
> Map&lt;String, String&gt; getGeneTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of gene types, for specified species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getGeneTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getGeneTypeCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getGeneTypeDiffUsingGET"></a>
# **getGeneTypeDiffUsingGET**
> Map&lt;String, String&gt; getGeneTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of gene types, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getGeneTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getGeneTypeDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getObjectStatusCountUsingGET"></a>
# **getObjectStatusCountUsingGET**
> Map&lt;String, String&gt; getObjectStatusCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of objects with given status, for specified species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getObjectStatusCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getObjectStatusCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getObjectStatusDiffUsingGET"></a>
# **getObjectStatusDiffUsingGET**
> Map&lt;String, String&gt; getObjectStatusDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of objects with given status, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getObjectStatusDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getObjectStatusDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getObjectsWithRefSeqCountUsingGET"></a>
# **getObjectsWithRefSeqCountUsingGET**
> Map&lt;String, String&gt; getObjectsWithRefSeqCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of objects with reference sequence(s), by object type, for specified species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getObjectsWithRefSeqCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getObjectsWithRefSeqCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getObjectsWithRefSeqDiffUsingGET"></a>
# **getObjectsWithRefSeqDiffUsingGET**
> Map&lt;String, String&gt; getObjectsWithRefSeqDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of objects with reference sequence(s), by object type, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getObjectsWithRefSeqDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getObjectsWithRefSeqDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getObjectsWithReferenceCountUsingGET"></a>
# **getObjectsWithReferenceCountUsingGET**
> Map&lt;String, String&gt; getObjectsWithReferenceCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of objects with reference, by object type, for specified species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getObjectsWithReferenceCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getObjectsWithReferenceCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getObjectsWithReferenceDiffUsingGET"></a>
# **getObjectsWithReferenceDiffUsingGET**
> Map&lt;String, String&gt; getObjectsWithReferenceDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of objects with reference, by object type, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getObjectsWithReferenceDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getObjectsWithReferenceDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getObjectsWithXDBsCountUsingGET"></a>
# **getObjectsWithXDBsCountUsingGET**
> Map&lt;String, String&gt; getObjectsWithXDBsCountUsingGET(speciesTypeKey, objectKey, dateYYYYMMDD)

Count of objects with external database ids, by database id, for specified species, object type and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    Integer objectKey = 56; // Integer | objectKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getObjectsWithXDBsCountUsingGET(speciesTypeKey, objectKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getObjectsWithXDBsCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **objectKey** | **Integer**| objectKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getObjectsWithXDBsDiffUsingGET"></a>
# **getObjectsWithXDBsDiffUsingGET**
> Map&lt;String, String&gt; getObjectsWithXDBsDiffUsingGET(speciesTypeKey, objectKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of objects with external database ids, by database id, for specified species, object type and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    Integer objectKey = 56; // Integer | objectKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getObjectsWithXDBsDiffUsingGET(speciesTypeKey, objectKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getObjectsWithXDBsDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **objectKey** | **Integer**| objectKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getProteinInteractionCountUsingGET"></a>
# **getProteinInteractionCountUsingGET**
> Map&lt;String, String&gt; getProteinInteractionCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of protein interactions, for specified species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getProteinInteractionCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getProteinInteractionCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getProteinInteractionDiffUsingGET"></a>
# **getProteinInteractionDiffUsingGET**
> Map&lt;String, String&gt; getProteinInteractionDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of protein interactions, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getProteinInteractionDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getProteinInteractionDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getQtlInheritanceTypeCountUsingGET"></a>
# **getQtlInheritanceTypeCountUsingGET**
> Map&lt;String, String&gt; getQtlInheritanceTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of strains, by qtl inheritance type, for specified species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getQtlInheritanceTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getQtlInheritanceTypeCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getQtlInheritanceTypeDiffUsingGET"></a>
# **getQtlInheritanceTypeDiffUsingGET**
> Map&lt;String, String&gt; getQtlInheritanceTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of strains, by qtl inheritance type, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getQtlInheritanceTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getQtlInheritanceTypeDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getRetiredObjectCountUsingGET"></a>
# **getRetiredObjectCountUsingGET**
> Map&lt;String, String&gt; getRetiredObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of retired objects by type, for specified species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getRetiredObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getRetiredObjectCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getRetiredObjectDiffUsingGET"></a>
# **getRetiredObjectDiffUsingGET**
> Map&lt;String, String&gt; getRetiredObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of retired objects, by type, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getRetiredObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getRetiredObjectDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getStrainTypeCountUsingGET"></a>
# **getStrainTypeCountUsingGET**
> Map&lt;String, String&gt; getStrainTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of strain types, for specified species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getStrainTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getStrainTypeCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getStrainTypeDiffUsingGET"></a>
# **getStrainTypeDiffUsingGET**
> Map&lt;String, String&gt; getStrainTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of strain types, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getStrainTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getStrainTypeDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getTermStatsUsingGET"></a>
# **getTermStatsUsingGET**
> Map&lt;String, Integer&gt; getTermStatsUsingGET(accId, filterAccId)

getTermStats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    String accId = "accId_example"; // String | accId
    String filterAccId = "filterAccId_example"; // String | filterAccId
    try {
      Map<String, Integer> result = apiInstance.getTermStatsUsingGET(accId, filterAccId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getTermStatsUsingGET");
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
| **accId** | **String**| accId | |
| **filterAccId** | **String**| filterAccId | |

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getWithdrawnObjectCountUsingGET"></a>
# **getWithdrawnObjectCountUsingGET**
> Map&lt;String, String&gt; getWithdrawnObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of withdrawn objects by type, for specified species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getWithdrawnObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getWithdrawnObjectCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getWithdrawnObjectDiffUsingGET"></a>
# **getWithdrawnObjectDiffUsingGET**
> Map&lt;String, String&gt; getWithdrawnObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of withdrawn objects, by type, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getWithdrawnObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getWithdrawnObjectDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getXdbsCountUsingGET"></a>
# **getXdbsCountUsingGET**
> Map&lt;String, String&gt; getXdbsCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of external database ids, for specied species and date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getXdbsCountUsingGET(speciesTypeKey, dateYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getXdbsCountUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateYYYYMMDD** | **String**| dateYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getXdbsDiffUsingGET"></a>
# **getXdbsDiffUsingGET**
> Map&lt;String, String&gt; getXdbsDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of external database ids, for specified species and date range

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | speciesTypeKey
    String dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
    String dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
    try {
      Map<String, String> result = apiInstance.getXdbsDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getXdbsDiffUsingGET");
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
| **speciesTypeKey** | **Integer**| speciesTypeKey | |
| **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | |
| **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

