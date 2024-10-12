# LumminaryApiSpecApi

All URIs are relative to *http://api.lumminary.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAuthorizationsQueue**](LumminaryApiSpecApi.md#getAuthorizationsQueue) | **GET** /products/{productId}/authorizations |  |
| [**getClientGene**](LumminaryApiSpecApi.md#getClientGene) | **GET** /clients/{clientId}/datasets/{datasetId}/genes/{geneSymbol} | Get gene by symbol |
| [**getClientSnp**](LumminaryApiSpecApi.md#getClientSnp) | **GET** /clients/{clientId}/datasets/{datasetId}/snps/{snpId} | Get SNP information |
| [**getClientSnpGroup**](LumminaryApiSpecApi.md#getClientSnpGroup) | **GET** /clients/{clientId}/datasets/{datasetId}/snps/ |  |
| [**getGene**](LumminaryApiSpecApi.md#getGene) | **GET** /reference/genes/databases/{databaseName}/accessions/{accession} | Generic gene information |
| [**getProduct**](LumminaryApiSpecApi.md#getProduct) | **GET** /products/{productId} | Get product details |
| [**getProductAuthorization**](LumminaryApiSpecApi.md#getProductAuthorization) | **GET** /products/{productId}/authorizations/{authorizationId} |  |
| [**getReferenceChromosome**](LumminaryApiSpecApi.md#getReferenceChromosome) | **GET** /reference/genomes/{genomeBuildAccession}/chromosomes/{chromosomeAccession} | Sequence for a region of the reference genome |
| [**getReferenceGenome**](LumminaryApiSpecApi.md#getReferenceGenome) | **GET** /reference/genomes/{genomeBuildAccession}/chromosomes | Reference genome metadata |
| [**getReferenceGenomesGroup**](LumminaryApiSpecApi.md#getReferenceGenomesGroup) | **GET** /reference/genomes/ | Reference genome builds |
| [**getReferenceSnp**](LumminaryApiSpecApi.md#getReferenceSnp) | **GET** /reference/snps/{snpAccession} | Reference SNP data |
| [**postAuthorizationResultCredentials**](LumminaryApiSpecApi.md#postAuthorizationResultCredentials) | **POST** /products/{productId}/authorizations/{authorizationId}/credentials | Provide a result for the authorization |
| [**postAuthorizationResultFile**](LumminaryApiSpecApi.md#postAuthorizationResultFile) | **POST** /products/{productId}/authorizations/{authorizationId}/file | Provide a file result to the authorization, e |
| [**postClientSnpGroup**](LumminaryApiSpecApi.md#postClientSnpGroup) | **POST** /clients/{clientId}/datasets/{datasetId}/snps/ | Get a large group of SNPs |
| [**postJwtAuth**](LumminaryApiSpecApi.md#postJwtAuth) | **POST** /auth/jwt | General-purpose authentication |
| [**postProductAuthorization**](LumminaryApiSpecApi.md#postProductAuthorization) | **POST** /products/{productId}/authorizations/{authorizationId} | Signal that processing is complete, without uploading any result |
| [**postProductAuthorizationUnfulfillable**](LumminaryApiSpecApi.md#postProductAuthorizationUnfulfillable) | **POST** /products/{productId}/authorizations/{authorizationId}/unfulfillable | Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons |


<a id="getAuthorizationsQueue"></a>
# **getAuthorizationsQueue**
> List&lt;Authorization&gt; getAuthorizationsQueue(productId, seqNumStart, xFields)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String productId = "productId_example"; // String | The UUID of the product
    String seqNumStart = "seqNumStart_example"; // String | The first sequence number from which to fetch (the sequence number of the last processed authorization)
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      List<Authorization> result = apiInstance.getAuthorizationsQueue(productId, seqNumStart, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getAuthorizationsQueue");
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
| **productId** | **String**| The UUID of the product | |
| **seqNumStart** | **String**| The first sequence number from which to fetch (the sequence number of the last processed authorization) | [optional] |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**List&lt;Authorization&gt;**](Authorization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Product not found |  -  |

<a id="getClientGene"></a>
# **getClientGene**
> ClientGene getClientGene(clientId, datasetId, geneSymbol, xFields)

Get gene by symbol

Gets A gene by its symbol, which can be found by querying the reference/ resource.  Will return a 404 if a gene exists as a reference, but its genomic coordinates intersect no SNPs in the dataset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String clientId = "clientId_example"; // String | The UUID of the client
    String datasetId = "datasetId_example"; // String | The UUID of one of the client's dataset
    String geneSymbol = "geneSymbol_example"; // String | The symbol of a gene to be fetched
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      ClientGene result = apiInstance.getClientGene(clientId, datasetId, geneSymbol, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getClientGene");
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
| **clientId** | **String**| The UUID of the client | |
| **datasetId** | **String**| The UUID of one of the client&#39;s dataset | |
| **geneSymbol** | **String**| The symbol of a gene to be fetched | |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**ClientGene**](ClientGene.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Resource not found |  -  |

<a id="getClientSnp"></a>
# **getClientSnp**
> ClientSNP getClientSnp(clientId, datasetId, snpId, xFields)

Get SNP information

Gets SNP information, as provided by the dataset.  If fetching this as an product, the client must have already granted access to the snip (see the &#39;products&#39; group)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String clientId = "clientId_example"; // String | The UUID of the client
    String datasetId = "datasetId_example"; // String | The UUID of one of the client's dataset
    String snpId = "snpId_example"; // String | The rsId of a SNP to be fetched
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      ClientSNP result = apiInstance.getClientSnp(clientId, datasetId, snpId, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getClientSnp");
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
| **clientId** | **String**| The UUID of the client | |
| **datasetId** | **String**| The UUID of one of the client&#39;s dataset | |
| **snpId** | **String**| The rsId of a SNP to be fetched | |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**ClientSNP**](ClientSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Resource not found |  -  |

<a id="getClientSnpGroup"></a>
# **getClientSnpGroup**
> List&lt;ClientSNP&gt; getClientSnpGroup(clientId, datasetId, xFields)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String clientId = "clientId_example"; // String | The UUID of the client
    String datasetId = "datasetId_example"; // String | The UUID of one of the client's dataset
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      List<ClientSNP> result = apiInstance.getClientSnpGroup(clientId, datasetId, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getClientSnpGroup");
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
| **clientId** | **String**| The UUID of the client | |
| **datasetId** | **String**| The UUID of one of the client&#39;s dataset | |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**List&lt;ClientSNP&gt;**](ClientSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Resource not found |  -  |

<a id="getGene"></a>
# **getGene**
> PublicGene getGene(databaseName, accession, dbsnpBuild, referenceGenome, xFields)

Generic gene information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String databaseName = "databaseName_example"; // String | The name of the database to search. E.g: Genbank
    String accession = "accession_example"; // String | The accession within the selected database
    Integer dbsnpBuild = 149; // Integer | The dbSNP build for which to consider snps belonging to the gene. Defaults to 149
    String referenceGenome = "GRCH37P13"; // String | The reference genome for which gene annotations will be returned. Defaults to GRCh37p13
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      PublicGene result = apiInstance.getGene(databaseName, accession, dbsnpBuild, referenceGenome, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getGene");
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
| **databaseName** | **String**| The name of the database to search. E.g: Genbank | |
| **accession** | **String**| The accession within the selected database | |
| **dbsnpBuild** | **Integer**| The dbSNP build for which to consider snps belonging to the gene. Defaults to 149 | [optional] [default to 149] |
| **referenceGenome** | **String**| The reference genome for which gene annotations will be returned. Defaults to GRCh37p13 | [optional] [default to GRCH37P13] |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**PublicGene**](PublicGene.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Resource not found |  -  |

<a id="getProduct"></a>
# **getProduct**
> Product getProduct(productId, xFields)

Get product details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String productId = "productId_example"; // String | The UUID of the product
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      Product result = apiInstance.getProduct(productId, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getProduct");
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
| **productId** | **String**| The UUID of the product | |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**Product**](Product.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Product not found |  -  |

<a id="getProductAuthorization"></a>
# **getProductAuthorization**
> Authorization getProductAuthorization(productId, authorizationId, xFields)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String productId = "productId_example"; // String | The UUID of the product
    String authorizationId = "authorizationId_example"; // String | The UUID of the authorization
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      Authorization result = apiInstance.getProductAuthorization(productId, authorizationId, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getProductAuthorization");
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
| **productId** | **String**| The UUID of the product | |
| **authorizationId** | **String**| The UUID of the authorization | |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**Authorization**](Authorization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Object not found |  -  |

<a id="getReferenceChromosome"></a>
# **getReferenceChromosome**
> ReferenceSequence getReferenceChromosome(genomeBuildAccession, chromosomeAccession, rangeStart, rangeStop, xFields)

Sequence for a region of the reference genome

Fetch a closed interval of nucleotides on a given chromosome. Includes start and stop positions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String genomeBuildAccession = "genomeBuildAccession_example"; // String | The accession of the reference genome
    String chromosomeAccession = "chromosomeAccession_example"; // String | The accession to the chromosome
    Integer rangeStart = 56; // Integer | Location on the chromosome
    Integer rangeStop = 56; // Integer | Location on the chromosome
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      ReferenceSequence result = apiInstance.getReferenceChromosome(genomeBuildAccession, chromosomeAccession, rangeStart, rangeStop, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getReferenceChromosome");
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
| **genomeBuildAccession** | **String**| The accession of the reference genome | |
| **chromosomeAccession** | **String**| The accession to the chromosome | |
| **rangeStart** | **Integer**| Location on the chromosome | |
| **rangeStop** | **Integer**| Location on the chromosome | |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**ReferenceSequence**](ReferenceSequence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Resource not found |  -  |

<a id="getReferenceGenome"></a>
# **getReferenceGenome**
> List&lt;ReferenceChromosomeOverview&gt; getReferenceGenome(genomeBuildAccession, xFields)

Reference genome metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String genomeBuildAccession = "genomeBuildAccession_example"; // String | 
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      List<ReferenceChromosomeOverview> result = apiInstance.getReferenceGenome(genomeBuildAccession, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getReferenceGenome");
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
| **genomeBuildAccession** | **String**|  | |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**List&lt;ReferenceChromosomeOverview&gt;**](ReferenceChromosomeOverview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Resource not found |  -  |

<a id="getReferenceGenomesGroup"></a>
# **getReferenceGenomesGroup**
> List&lt;ReferenceGenomeOverview&gt; getReferenceGenomesGroup(xFields)

Reference genome builds

Lists reference genome builds that are available

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      List<ReferenceGenomeOverview> result = apiInstance.getReferenceGenomesGroup(xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getReferenceGenomesGroup");
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
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**List&lt;ReferenceGenomeOverview&gt;**](ReferenceGenomeOverview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getReferenceSnp"></a>
# **getReferenceSnp**
> PublicSNP getReferenceSnp(snpAccession, dbsnpVersion, grchVersion, xFields)

Reference SNP data

Get reference SNP information, from dbSNP

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String snpAccession = "snpAccession_example"; // String | The rsId of the SNP
    Integer dbsnpVersion = 149; // Integer | The dbSNP build. Defaults to 149
    String grchVersion = "GRCH37P13"; // String | The GRCh build on which to place snips. Defaults to GRCh37p13
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      PublicSNP result = apiInstance.getReferenceSnp(snpAccession, dbsnpVersion, grchVersion, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#getReferenceSnp");
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
| **snpAccession** | **String**| The rsId of the SNP | |
| **dbsnpVersion** | **Integer**| The dbSNP build. Defaults to 149 | [optional] [default to 149] |
| **grchVersion** | **String**| The GRCh build on which to place snips. Defaults to GRCh37p13 | [optional] [default to GRCH37P13] |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**PublicSNP**](PublicSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Resource not found |  -  |

<a id="postAuthorizationResultCredentials"></a>
# **postAuthorizationResultCredentials**
> ReportCredentials postAuthorizationResultCredentials(productId, authorizationId, xFields, credentialsUsername, credentialsPassword, reportUrl)

Provide a result for the authorization

These can be log-in credentials for a website where the result is available

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String productId = "productId_example"; // String | The UUID of the product
    String authorizationId = "authorizationId_example"; // String | The UUID of the authorization
    String xFields = "xFields_example"; // String | An optional fields mask
    String credentialsUsername = "credentialsUsername_example"; // String | Credentials for accessing the result. Includes password, username and url
    String credentialsPassword = "credentialsPassword_example"; // String | Credentials for accessing the result. Includes password, username and url
    String reportUrl = "reportUrl_example"; // String | Credentials for accessing the result. Includes password, username and url
    try {
      ReportCredentials result = apiInstance.postAuthorizationResultCredentials(productId, authorizationId, xFields, credentialsUsername, credentialsPassword, reportUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#postAuthorizationResultCredentials");
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
| **productId** | **String**| The UUID of the product | |
| **authorizationId** | **String**| The UUID of the authorization | |
| **xFields** | **String**| An optional fields mask | [optional] |
| **credentialsUsername** | **String**| Credentials for accessing the result. Includes password, username and url | [optional] |
| **credentialsPassword** | **String**| Credentials for accessing the result. Includes password, username and url | [optional] |
| **reportUrl** | **String**| Credentials for accessing the result. Includes password, username and url | [optional] |

### Return type

[**ReportCredentials**](ReportCredentials.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **201** | Result saved |  -  |
| **404** | Object not found |  -  |

<a id="postAuthorizationResultFile"></a>
# **postAuthorizationResultFile**
> ReportFile postAuthorizationResultFile(productId, authorizationId, originalFilename, xFields, fileReport)

Provide a file result to the authorization, e

g. a pdf report

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String productId = "productId_example"; // String | The UUID of the product
    String authorizationId = "authorizationId_example"; // String | The UUID of the authorization
    String originalFilename = "originalFilename_example"; // String | Optional original filename for the report. If not provided, the filename of uploaded file will be used
    String xFields = "xFields_example"; // String | An optional fields mask
    File fileReport = new File("/path/to/file"); // File | A binary file (e.g. pdf) that contains the result of the authorization
    try {
      ReportFile result = apiInstance.postAuthorizationResultFile(productId, authorizationId, originalFilename, xFields, fileReport);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#postAuthorizationResultFile");
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
| **productId** | **String**| The UUID of the product | |
| **authorizationId** | **String**| The UUID of the authorization | |
| **originalFilename** | **String**| Optional original filename for the report. If not provided, the filename of uploaded file will be used | [optional] |
| **xFields** | **String**| An optional fields mask | [optional] |
| **fileReport** | **File**| A binary file (e.g. pdf) that contains the result of the authorization | [optional] |

### Return type

[**ReportFile**](ReportFile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **201** | Result saved |  -  |
| **404** | Object not found |  -  |

<a id="postClientSnpGroup"></a>
# **postClientSnpGroup**
> List&lt;ClientSNP&gt; postClientSnpGroup(clientId, datasetId, snps, xFields)

Get a large group of SNPs

SNPs that are not present in the dataset are ignored, 404 is returned only if the dataset/client does not exist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String clientId = "clientId_example"; // String | The UUID of the client
    String datasetId = "datasetId_example"; // String | The UUID of one of the client's dataset
    String snps = "snps_example"; // String | JSON-encoded list of snps to be fetched
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      List<ClientSNP> result = apiInstance.postClientSnpGroup(clientId, datasetId, snps, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#postClientSnpGroup");
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
| **clientId** | **String**| The UUID of the client | |
| **datasetId** | **String**| The UUID of one of the client&#39;s dataset | |
| **snps** | **String**| JSON-encoded list of snps to be fetched | |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**List&lt;ClientSNP&gt;**](ClientSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Resource not found |  -  |

<a id="postJwtAuth"></a>
# **postJwtAuth**
> JavascriptWebToken postJwtAuth(username, password, role, xFields)

General-purpose authentication

## Note: * The JWT tokens returned should be passed to any resource that requires authentication, in the Authentication header, in the format &#x60;Bearer: your-token-here&#x60; * Only JWT authentication tokens are provided (no refresh tokens). These tokens are valid for 30 seconds from the moment they were issued

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String username = "username_example"; // String | The email for a Client, or the API for a partner product
    String password = "password_example"; // String | The passowrd for a Client, or the API key for a service
    String role = "role_example"; // String | The role for which authentication will be made. Value : role_product
    String xFields = "xFields_example"; // String | An optional fields mask
    try {
      JavascriptWebToken result = apiInstance.postJwtAuth(username, password, role, xFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#postJwtAuth");
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
| **username** | **String**| The email for a Client, or the API for a partner product | |
| **password** | **String**| The passowrd for a Client, or the API key for a service | |
| **role** | **String**| The role for which authentication will be made. Value : role_product | |
| **xFields** | **String**| An optional fields mask | [optional] |

### Return type

[**JavascriptWebToken**](JavascriptWebToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="postProductAuthorization"></a>
# **postProductAuthorization**
> postProductAuthorization(productId, authorizationId)

Signal that processing is complete, without uploading any result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String productId = "productId_example"; // String | The UUID of the product
    String authorizationId = "authorizationId_example"; // String | The UUID of the authorization
    try {
      apiInstance.postProductAuthorization(productId, authorizationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#postProductAuthorization");
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
| **productId** | **String**| The UUID of the product | |
| **authorizationId** | **String**| The UUID of the authorization | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Result saved |  -  |
| **404** | Object not found |  -  |

<a id="postProductAuthorizationUnfulfillable"></a>
# **postProductAuthorizationUnfulfillable**
> postProductAuthorizationUnfulfillable(productId, authorizationId)

Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LumminaryApiSpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.lumminary.com/v1");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    LumminaryApiSpecApi apiInstance = new LumminaryApiSpecApi(defaultClient);
    String productId = "productId_example"; // String | The UUID of the product
    String authorizationId = "authorizationId_example"; // String | The UUID of the authorization
    try {
      apiInstance.postProductAuthorizationUnfulfillable(productId, authorizationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LumminaryApiSpecApi#postProductAuthorizationUnfulfillable");
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
| **productId** | **String**| The UUID of the product | |
| **authorizationId** | **String**| The UUID of the authorization | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **404** | Object not found |  -  |

