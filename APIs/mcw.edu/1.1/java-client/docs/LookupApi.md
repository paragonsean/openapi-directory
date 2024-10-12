# LookupApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEnsemblGeneMappingUsingGET**](LookupApi.md#getEnsemblGeneMappingUsingGET) | **GET** /lookup/id/map/EnsemblGene/{rgdId} | Translate an RGD ID to an Ensembl Gene  ID |
| [**getEnsemblGeneMappingUsingPOST**](LookupApi.md#getEnsemblGeneMappingUsingPOST) | **POST** /lookup/id/map/EnsemblGene | Translate RGD IDs to Ensembl Gene IDs |
| [**getEnsemblProteinMappingUsingGET**](LookupApi.md#getEnsemblProteinMappingUsingGET) | **GET** /lookup/id/map/EnsemblProtein/{rgdId} | Translate an RGD ID to an Ensembl Protein ID |
| [**getEnsemblProteinMappingUsingPOST**](LookupApi.md#getEnsemblProteinMappingUsingPOST) | **POST** /lookup/id/map/EnsemblProtein | Translate RGD IDs to Ensembl Protein IDs |
| [**getEnsemblTranscriptMappingUsingGET**](LookupApi.md#getEnsemblTranscriptMappingUsingGET) | **GET** /lookup/id/map/EnsemblTranscript/{rgdId} | Translate an RGD ID to an Ensembl Transcript ID |
| [**getEnsemblTranscriptMappingUsingPOST**](LookupApi.md#getEnsemblTranscriptMappingUsingPOST) | **POST** /lookup/id/map/EnsemblTranscript | Translate RGD IDs to Ensembl Transcript IDs |
| [**getGTEXMappingUsingGET**](LookupApi.md#getGTEXMappingUsingGET) | **GET** /lookup/id/map/GTEx/{rgdId} | Translate an RGD ID to an GTEx ID |
| [**getGTEXMappingUsingPOST**](LookupApi.md#getGTEXMappingUsingPOST) | **POST** /lookup/id/map/GTEx | Translate RGD IDs to GTEx IDs |
| [**getGenBankNucleotideMappingUsingGET**](LookupApi.md#getGenBankNucleotideMappingUsingGET) | **GET** /lookup/id/map/GenBankNucleotide/{rgdId} | Translate an RGD ID to a GenBank Nucleotide ID |
| [**getGenBankNucleotideMappingUsingPOST**](LookupApi.md#getGenBankNucleotideMappingUsingPOST) | **POST** /lookup/id/map/GenBankNucleotide | Translate RGD IDs to GenBank Nucleotide IDs |
| [**getGenBankProteinMappingUsingGET**](LookupApi.md#getGenBankProteinMappingUsingGET) | **GET** /lookup/id/map/GenBankProtein/{rgdId} | Translate an RGD ID to a GenBank Protein ID |
| [**getGenBankProteinMappingUsingPOST**](LookupApi.md#getGenBankProteinMappingUsingPOST) | **POST** /lookup/id/map/GenBankProtein | Translate RGD IDs to GenBank Protein IDs |
| [**getGeneTypesUsingGET**](LookupApi.md#getGeneTypesUsingGET) | **GET** /lookup/geneTypes | Returns a list of gene types avialable in RGD |
| [**getHGNCMappingUsingGET**](LookupApi.md#getHGNCMappingUsingGET) | **GET** /lookup/id/map/HGNC/{rgdId} | Translate an RGD ID to an HGNC ID |
| [**getHGNCMappingUsingPOST**](LookupApi.md#getHGNCMappingUsingPOST) | **POST** /lookup/id/map/HGNC | Translate RGD IDs to HGNC IDs |
| [**getMGIMappingUsingGET**](LookupApi.md#getMGIMappingUsingGET) | **GET** /lookup/id/map/MGI/{rgdId} | Translate an RGD ID to an MGI ID |
| [**getMGIMappingUsingPOST**](LookupApi.md#getMGIMappingUsingPOST) | **POST** /lookup/id/map/MGI | Translate RGD IDs to MGI IDs |
| [**getMapsUsingGET**](LookupApi.md#getMapsUsingGET) | **GET** /lookup/maps/{speciesTypeKey} | Return a list assembly maps for a species |
| [**getMapsUsingGET1**](LookupApi.md#getMapsUsingGET1) | **GET** /lookup/standardUnit/{accId} | Return a standardUnit for an ontology if it exists |
| [**getNCBIGeneMappingUsingGET**](LookupApi.md#getNCBIGeneMappingUsingGET) | **GET** /lookup/id/map/NCBIGene/{rgdId} | Translate an RGD ID to an NCBI Gene ID |
| [**getNCBIGeneMappingUsingPOST**](LookupApi.md#getNCBIGeneMappingUsingPOST) | **POST** /lookup/id/map/NCBIGene | Translate RGD IDs to NCBI Gene IDs |
| [**getSpeciesTypesUsingGET**](LookupApi.md#getSpeciesTypesUsingGET) | **GET** /lookup/speciesTypeKeys | Return a Map of species type keys available in RGD |
| [**getUniProtMappingUsingGET**](LookupApi.md#getUniProtMappingUsingGET) | **GET** /lookup/id/map/UniProt/{rgdId} | Translate an RGD ID to a UniProt ID |
| [**getUniProtMappingUsingPOST**](LookupApi.md#getUniProtMappingUsingPOST) | **POST** /lookup/id/map/UniProt | Translate RGD IDs to UniProt IDs |


<a id="getEnsemblGeneMappingUsingGET"></a>
# **getEnsemblGeneMappingUsingGET**
> Map&lt;String, String&gt; getEnsemblGeneMappingUsingGET(rgdId)

Translate an RGD ID to an Ensembl Gene  ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      Map<String, String> result = apiInstance.getEnsemblGeneMappingUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getEnsemblGeneMappingUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

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

<a id="getEnsemblGeneMappingUsingPOST"></a>
# **getEnsemblGeneMappingUsingPOST**
> Map&lt;String, String&gt; getEnsemblGeneMappingUsingPOST(rgDIDListRequest)

Translate RGD IDs to Ensembl Gene IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    RGDIDListRequest rgDIDListRequest = new RGDIDListRequest(); // RGDIDListRequest | data
    try {
      Map<String, String> result = apiInstance.getEnsemblGeneMappingUsingPOST(rgDIDListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getEnsemblGeneMappingUsingPOST");
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
| **rgDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getEnsemblProteinMappingUsingGET"></a>
# **getEnsemblProteinMappingUsingGET**
> Map&lt;String, String&gt; getEnsemblProteinMappingUsingGET(rgdId)

Translate an RGD ID to an Ensembl Protein ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      Map<String, String> result = apiInstance.getEnsemblProteinMappingUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getEnsemblProteinMappingUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

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

<a id="getEnsemblProteinMappingUsingPOST"></a>
# **getEnsemblProteinMappingUsingPOST**
> Map&lt;String, String&gt; getEnsemblProteinMappingUsingPOST(rgDIDListRequest)

Translate RGD IDs to Ensembl Protein IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    RGDIDListRequest rgDIDListRequest = new RGDIDListRequest(); // RGDIDListRequest | data
    try {
      Map<String, String> result = apiInstance.getEnsemblProteinMappingUsingPOST(rgDIDListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getEnsemblProteinMappingUsingPOST");
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
| **rgDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getEnsemblTranscriptMappingUsingGET"></a>
# **getEnsemblTranscriptMappingUsingGET**
> Map&lt;String, String&gt; getEnsemblTranscriptMappingUsingGET(rgdId)

Translate an RGD ID to an Ensembl Transcript ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      Map<String, String> result = apiInstance.getEnsemblTranscriptMappingUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getEnsemblTranscriptMappingUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

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

<a id="getEnsemblTranscriptMappingUsingPOST"></a>
# **getEnsemblTranscriptMappingUsingPOST**
> Map&lt;String, String&gt; getEnsemblTranscriptMappingUsingPOST(rgDIDListRequest)

Translate RGD IDs to Ensembl Transcript IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    RGDIDListRequest rgDIDListRequest = new RGDIDListRequest(); // RGDIDListRequest | data
    try {
      Map<String, String> result = apiInstance.getEnsemblTranscriptMappingUsingPOST(rgDIDListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getEnsemblTranscriptMappingUsingPOST");
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
| **rgDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getGTEXMappingUsingGET"></a>
# **getGTEXMappingUsingGET**
> Map&lt;String, String&gt; getGTEXMappingUsingGET(rgdId)

Translate an RGD ID to an GTEx ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      Map<String, String> result = apiInstance.getGTEXMappingUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getGTEXMappingUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

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

<a id="getGTEXMappingUsingPOST"></a>
# **getGTEXMappingUsingPOST**
> Map&lt;String, String&gt; getGTEXMappingUsingPOST(rgDIDListRequest)

Translate RGD IDs to GTEx IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    RGDIDListRequest rgDIDListRequest = new RGDIDListRequest(); // RGDIDListRequest | data
    try {
      Map<String, String> result = apiInstance.getGTEXMappingUsingPOST(rgDIDListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getGTEXMappingUsingPOST");
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
| **rgDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getGenBankNucleotideMappingUsingGET"></a>
# **getGenBankNucleotideMappingUsingGET**
> Map&lt;String, String&gt; getGenBankNucleotideMappingUsingGET(rgdId)

Translate an RGD ID to a GenBank Nucleotide ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      Map<String, String> result = apiInstance.getGenBankNucleotideMappingUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getGenBankNucleotideMappingUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

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

<a id="getGenBankNucleotideMappingUsingPOST"></a>
# **getGenBankNucleotideMappingUsingPOST**
> Map&lt;String, String&gt; getGenBankNucleotideMappingUsingPOST(rgDIDListRequest)

Translate RGD IDs to GenBank Nucleotide IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    RGDIDListRequest rgDIDListRequest = new RGDIDListRequest(); // RGDIDListRequest | data
    try {
      Map<String, String> result = apiInstance.getGenBankNucleotideMappingUsingPOST(rgDIDListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getGenBankNucleotideMappingUsingPOST");
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
| **rgDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getGenBankProteinMappingUsingGET"></a>
# **getGenBankProteinMappingUsingGET**
> Map&lt;String, String&gt; getGenBankProteinMappingUsingGET(rgdId)

Translate an RGD ID to a GenBank Protein ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      Map<String, String> result = apiInstance.getGenBankProteinMappingUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getGenBankProteinMappingUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

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

<a id="getGenBankProteinMappingUsingPOST"></a>
# **getGenBankProteinMappingUsingPOST**
> Map&lt;String, String&gt; getGenBankProteinMappingUsingPOST(rgDIDListRequest)

Translate RGD IDs to GenBank Protein IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    RGDIDListRequest rgDIDListRequest = new RGDIDListRequest(); // RGDIDListRequest | data
    try {
      Map<String, String> result = apiInstance.getGenBankProteinMappingUsingPOST(rgDIDListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getGenBankProteinMappingUsingPOST");
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
| **rgDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getGeneTypesUsingGET"></a>
# **getGeneTypesUsingGET**
> List&lt;String&gt; getGeneTypesUsingGET()

Returns a list of gene types avialable in RGD

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    try {
      List<String> result = apiInstance.getGeneTypesUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getGeneTypesUsingGET");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

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

<a id="getHGNCMappingUsingGET"></a>
# **getHGNCMappingUsingGET**
> Map&lt;String, String&gt; getHGNCMappingUsingGET(rgdId)

Translate an RGD ID to an HGNC ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      Map<String, String> result = apiInstance.getHGNCMappingUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getHGNCMappingUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

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

<a id="getHGNCMappingUsingPOST"></a>
# **getHGNCMappingUsingPOST**
> Map&lt;String, String&gt; getHGNCMappingUsingPOST(rgDIDListRequest)

Translate RGD IDs to HGNC IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    RGDIDListRequest rgDIDListRequest = new RGDIDListRequest(); // RGDIDListRequest | data
    try {
      Map<String, String> result = apiInstance.getHGNCMappingUsingPOST(rgDIDListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getHGNCMappingUsingPOST");
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
| **rgDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getMGIMappingUsingGET"></a>
# **getMGIMappingUsingGET**
> Map&lt;String, String&gt; getMGIMappingUsingGET(rgdId)

Translate an RGD ID to an MGI ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      Map<String, String> result = apiInstance.getMGIMappingUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getMGIMappingUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

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

<a id="getMGIMappingUsingPOST"></a>
# **getMGIMappingUsingPOST**
> Map&lt;String, String&gt; getMGIMappingUsingPOST(rgDIDListRequest)

Translate RGD IDs to MGI IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    RGDIDListRequest rgDIDListRequest = new RGDIDListRequest(); // RGDIDListRequest | data
    try {
      Map<String, String> result = apiInstance.getMGIMappingUsingPOST(rgDIDListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getMGIMappingUsingPOST");
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
| **rgDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getMapsUsingGET"></a>
# **getMapsUsingGET**
> List&lt;Map&gt; getMapsUsingGET(speciesTypeKey)

Return a list assembly maps for a species

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer speciesTypeKey = 56; // Integer | RGD species type key. A full list of keys is available throught the lookup service.  1=human, 2=mouse, 3=rat,ect
    try {
      List<Map> result = apiInstance.getMapsUsingGET(speciesTypeKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getMapsUsingGET");
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
| **speciesTypeKey** | **Integer**| RGD species type key. A full list of keys is available throught the lookup service.  1&#x3D;human, 2&#x3D;mouse, 3&#x3D;rat,ect | |

### Return type

[**List&lt;Map&gt;**](Map.md)

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

<a id="getMapsUsingGET1"></a>
# **getMapsUsingGET1**
> String getMapsUsingGET1(accId)

Return a standardUnit for an ontology if it exists

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    String accId = "accId_example"; // String | RGD term acc
    try {
      String result = apiInstance.getMapsUsingGET1(accId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getMapsUsingGET1");
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
| **accId** | **String**| RGD term acc | |

### Return type

**String**

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

<a id="getNCBIGeneMappingUsingGET"></a>
# **getNCBIGeneMappingUsingGET**
> Map&lt;String, String&gt; getNCBIGeneMappingUsingGET(rgdId)

Translate an RGD ID to an NCBI Gene ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      Map<String, String> result = apiInstance.getNCBIGeneMappingUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getNCBIGeneMappingUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

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

<a id="getNCBIGeneMappingUsingPOST"></a>
# **getNCBIGeneMappingUsingPOST**
> Map&lt;String, String&gt; getNCBIGeneMappingUsingPOST(rgDIDListRequest)

Translate RGD IDs to NCBI Gene IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    RGDIDListRequest rgDIDListRequest = new RGDIDListRequest(); // RGDIDListRequest | data
    try {
      Map<String, String> result = apiInstance.getNCBIGeneMappingUsingPOST(rgDIDListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getNCBIGeneMappingUsingPOST");
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
| **rgDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getSpeciesTypesUsingGET"></a>
# **getSpeciesTypesUsingGET**
> Object getSpeciesTypesUsingGET()

Return a Map of species type keys available in RGD

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    try {
      Object result = apiInstance.getSpeciesTypesUsingGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getSpeciesTypesUsingGET");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

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

<a id="getUniProtMappingUsingGET"></a>
# **getUniProtMappingUsingGET**
> Map&lt;String, String&gt; getUniProtMappingUsingGET(rgdId)

Translate an RGD ID to a UniProt ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    Integer rgdId = 56; // Integer | RGD ID
    try {
      Map<String, String> result = apiInstance.getUniProtMappingUsingGET(rgdId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getUniProtMappingUsingGET");
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
| **rgdId** | **Integer**| RGD ID | |

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

<a id="getUniProtMappingUsingPOST"></a>
# **getUniProtMappingUsingPOST**
> Map&lt;String, String&gt; getUniProtMappingUsingPOST(rgDIDListRequest)

Translate RGD IDs to UniProt IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://rest.rgd.mcw.edu/rgdws");

    LookupApi apiInstance = new LookupApi(defaultClient);
    RGDIDListRequest rgDIDListRequest = new RGDIDListRequest(); // RGDIDListRequest | data
    try {
      Map<String, String> result = apiInstance.getUniProtMappingUsingPOST(rgDIDListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getUniProtMappingUsingPOST");
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
| **rgDIDListRequest** | [**RGDIDListRequest**](RGDIDListRequest.md)| data | [optional] |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

