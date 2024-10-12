# MartApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMartCaseAssociationsResource**](MartApi.md#getMartCaseAssociationsResource) | **GET** /mart/case/{object_category}/{taxon} | Bulk download of case associations |
| [**getMartDiseaseAssociationsResource**](MartApi.md#getMartDiseaseAssociationsResource) | **GET** /mart/disease/{object_category}/{taxon} | Bulk download of disease associations |
| [**getMartGeneAssociationsResource**](MartApi.md#getMartGeneAssociationsResource) | **GET** /mart/gene/{object_category}/{taxon} | Bulk download of gene associations |
| [**getMartOrthologAssociationsResource**](MartApi.md#getMartOrthologAssociationsResource) | **GET** /mart/ortholog/{taxon1}/{taxon2} | Bulk download of orthologs |
| [**getMartParalogAssociationsResource**](MartApi.md#getMartParalogAssociationsResource) | **GET** /mart/paralog/{taxon1}/{taxon2} | Bulk download of paralogs |


<a id="getMartCaseAssociationsResource"></a>
# **getMartCaseAssociationsResource**
> getMartCaseAssociationsResource(taxon, objectCategory, slim)

Bulk download of case associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    MartApi apiInstance = new MartApi(defaultClient);
    String taxon = "taxon_example"; // String | taxon of case, must be of form NCBITaxon:9606
    String objectCategory = "objectCategory_example"; // String | Category of entity at link Subject (target), e.g. phenotype, disease
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    try {
      apiInstance.getMartCaseAssociationsResource(taxon, objectCategory, slim);
    } catch (ApiException e) {
      System.err.println("Exception when calling MartApi#getMartCaseAssociationsResource");
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
| **taxon** | **String**| taxon of case, must be of form NCBITaxon:9606 | |
| **objectCategory** | **String**| Category of entity at link Subject (target), e.g. phenotype, disease | |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |

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
| **200** | Success |  -  |

<a id="getMartDiseaseAssociationsResource"></a>
# **getMartDiseaseAssociationsResource**
> getMartDiseaseAssociationsResource(taxon, objectCategory, slim)

Bulk download of disease associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    MartApi apiInstance = new MartApi(defaultClient);
    String taxon = "taxon_example"; // String | taxon of disease, must be of form NCBITaxon:9606
    String objectCategory = "objectCategory_example"; // String | Category of entity at link Object (target), e.g. phenotype, disease
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    try {
      apiInstance.getMartDiseaseAssociationsResource(taxon, objectCategory, slim);
    } catch (ApiException e) {
      System.err.println("Exception when calling MartApi#getMartDiseaseAssociationsResource");
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
| **taxon** | **String**| taxon of disease, must be of form NCBITaxon:9606 | |
| **objectCategory** | **String**| Category of entity at link Object (target), e.g. phenotype, disease | |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |

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
| **200** | Success |  -  |

<a id="getMartGeneAssociationsResource"></a>
# **getMartGeneAssociationsResource**
> getMartGeneAssociationsResource(taxon, objectCategory, slim)

Bulk download of gene associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    MartApi apiInstance = new MartApi(defaultClient);
    String taxon = "taxon_example"; // String | taxon of gene, must be of form NCBITaxon:9606
    String objectCategory = "objectCategory_example"; // String | Category of entity at link Object (target), e.g. phenotype, disease
    List<String> slim = Arrays.asList(); // List<String> | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
    try {
      apiInstance.getMartGeneAssociationsResource(taxon, objectCategory, slim);
    } catch (ApiException e) {
      System.err.println("Exception when calling MartApi#getMartGeneAssociationsResource");
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
| **taxon** | **String**| taxon of gene, must be of form NCBITaxon:9606 | |
| **objectCategory** | **String**| Category of entity at link Object (target), e.g. phenotype, disease | |
| **slim** | [**List&lt;String&gt;**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] |

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
| **200** | Success |  -  |

<a id="getMartOrthologAssociationsResource"></a>
# **getMartOrthologAssociationsResource**
> getMartOrthologAssociationsResource(taxon2, taxon1)

Bulk download of orthologs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    MartApi apiInstance = new MartApi(defaultClient);
    String taxon2 = "taxon2_example"; // String | object taxon, e.g. NCBITaxon:10090
    String taxon1 = "taxon1_example"; // String | subject taxon, e.g. NCBITaxon:9606
    try {
      apiInstance.getMartOrthologAssociationsResource(taxon2, taxon1);
    } catch (ApiException e) {
      System.err.println("Exception when calling MartApi#getMartOrthologAssociationsResource");
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
| **taxon2** | **String**| object taxon, e.g. NCBITaxon:10090 | |
| **taxon1** | **String**| subject taxon, e.g. NCBITaxon:9606 | |

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
| **200** | Success |  -  |

<a id="getMartParalogAssociationsResource"></a>
# **getMartParalogAssociationsResource**
> getMartParalogAssociationsResource(taxon2, taxon1)

Bulk download of paralogs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MartApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    MartApi apiInstance = new MartApi(defaultClient);
    String taxon2 = "taxon2_example"; // String | object taxon, e.g. NCBITaxon:9606
    String taxon1 = "taxon1_example"; // String | subject taxon, e.g. NCBITaxon:9606
    try {
      apiInstance.getMartParalogAssociationsResource(taxon2, taxon1);
    } catch (ApiException e) {
      System.err.println("Exception when calling MartApi#getMartParalogAssociationsResource");
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
| **taxon2** | **String**| object taxon, e.g. NCBITaxon:9606 | |
| **taxon1** | **String**| subject taxon, e.g. NCBITaxon:9606 | |

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
| **200** | Success |  -  |

