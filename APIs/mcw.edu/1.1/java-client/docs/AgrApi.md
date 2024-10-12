# AgrApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAffectedGenomicModelsUsingGET**](AgrApi.md#getAffectedGenomicModelsUsingGET) | **GET** /agr/affectedGenomicModels/{taxonId} | Get affected genomic models (rat strains with gene alleles) submitted by RGD to AGR by taxonId |
| [**getAllelesForTaxonUsingGET**](AgrApi.md#getAllelesForTaxonUsingGET) | **GET** /agr/alleles/{taxonId} | Get gene allele records submitted by RGD to AGR by taxonId |
| [**getExpressionForTaxonUsingGET**](AgrApi.md#getExpressionForTaxonUsingGET) | **GET** /agr/expression/{taxonId} | Get expression annotations submitted by RGD to AGR by taxonId |
| [**getGenesForLatestAssemblyUsingGET**](AgrApi.md#getGenesForLatestAssemblyUsingGET) | **GET** /agr/{taxonId} | Get gene records submitted by RGD to AGR by taxonId |
| [**getPhenotypesForTaxonUsingGET**](AgrApi.md#getPhenotypesForTaxonUsingGET) | **GET** /agr/phenotypes/{taxonId} | Get phenotype annotations submitted by RGD to AGR by taxonId |
| [**getVariantsForTaxonUsingGET**](AgrApi.md#getVariantsForTaxonUsingGET) | **GET** /agr/variants/{taxonId} | Get basic variant records submitted by RGD to AGR by taxonId |


<a id="getAffectedGenomicModelsUsingGET"></a>
# **getAffectedGenomicModelsUsingGET**
> Map&lt;String, Object&gt; getAffectedGenomicModelsUsingGET(taxonId)

Get affected genomic models (rat strains with gene alleles) submitted by RGD to AGR by taxonId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgrApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AgrApi apiInstance = new AgrApi(defaultClient);
    String taxonId = "taxonId_example"; // String | The taxon ID for species
    try {
      Map<String, Object> result = apiInstance.getAffectedGenomicModelsUsingGET(taxonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgrApi#getAffectedGenomicModelsUsingGET");
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
| **taxonId** | **String**| The taxon ID for species | |

### Return type

**Map&lt;String, Object&gt;**

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

<a id="getAllelesForTaxonUsingGET"></a>
# **getAllelesForTaxonUsingGET**
> Map&lt;String, Object&gt; getAllelesForTaxonUsingGET(taxonId)

Get gene allele records submitted by RGD to AGR by taxonId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgrApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AgrApi apiInstance = new AgrApi(defaultClient);
    String taxonId = "taxonId_example"; // String | The taxon ID for species
    try {
      Map<String, Object> result = apiInstance.getAllelesForTaxonUsingGET(taxonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgrApi#getAllelesForTaxonUsingGET");
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
| **taxonId** | **String**| The taxon ID for species | |

### Return type

**Map&lt;String, Object&gt;**

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

<a id="getExpressionForTaxonUsingGET"></a>
# **getExpressionForTaxonUsingGET**
> Map&lt;String, Object&gt; getExpressionForTaxonUsingGET(taxonId)

Get expression annotations submitted by RGD to AGR by taxonId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgrApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AgrApi apiInstance = new AgrApi(defaultClient);
    String taxonId = "taxonId_example"; // String | The taxon ID for species
    try {
      Map<String, Object> result = apiInstance.getExpressionForTaxonUsingGET(taxonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgrApi#getExpressionForTaxonUsingGET");
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
| **taxonId** | **String**| The taxon ID for species | |

### Return type

**Map&lt;String, Object&gt;**

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

<a id="getGenesForLatestAssemblyUsingGET"></a>
# **getGenesForLatestAssemblyUsingGET**
> Map&lt;String, Object&gt; getGenesForLatestAssemblyUsingGET(taxonId)

Get gene records submitted by RGD to AGR by taxonId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgrApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AgrApi apiInstance = new AgrApi(defaultClient);
    String taxonId = "taxonId_example"; // String | The taxon ID for species
    try {
      Map<String, Object> result = apiInstance.getGenesForLatestAssemblyUsingGET(taxonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgrApi#getGenesForLatestAssemblyUsingGET");
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
| **taxonId** | **String**| The taxon ID for species | |

### Return type

**Map&lt;String, Object&gt;**

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

<a id="getPhenotypesForTaxonUsingGET"></a>
# **getPhenotypesForTaxonUsingGET**
> Map&lt;String, Object&gt; getPhenotypesForTaxonUsingGET(taxonId)

Get phenotype annotations submitted by RGD to AGR by taxonId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgrApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AgrApi apiInstance = new AgrApi(defaultClient);
    String taxonId = "taxonId_example"; // String | The taxon ID for species
    try {
      Map<String, Object> result = apiInstance.getPhenotypesForTaxonUsingGET(taxonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgrApi#getPhenotypesForTaxonUsingGET");
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
| **taxonId** | **String**| The taxon ID for species | |

### Return type

**Map&lt;String, Object&gt;**

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

<a id="getVariantsForTaxonUsingGET"></a>
# **getVariantsForTaxonUsingGET**
> Map&lt;String, Object&gt; getVariantsForTaxonUsingGET(taxonId)

Get basic variant records submitted by RGD to AGR by taxonId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AgrApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    AgrApi apiInstance = new AgrApi(defaultClient);
    String taxonId = "taxonId_example"; // String | The taxon ID for species
    try {
      Map<String, Object> result = apiInstance.getVariantsForTaxonUsingGET(taxonId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AgrApi#getVariantsForTaxonUsingGET");
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
| **taxonId** | **String**| The taxon ID for species | |

### Return type

**Map&lt;String, Object&gt;**

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

