# StrainsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20DatabaseStrainsBarcodeGet**](StrainsApi.md#apiV20DatabaseStrainsBarcodeGet) | **GET** /api/v2.0/{database}/strains/{barcode} |  |
| [**apiV20DatabaseStrainsBarcodePost**](StrainsApi.md#apiV20DatabaseStrainsBarcodePost) | **POST** /api/v2.0/{database}/strains/{barcode} |  |
| [**apiV20DatabaseStrainsBarcodePut**](StrainsApi.md#apiV20DatabaseStrainsBarcodePut) | **PUT** /api/v2.0/{database}/strains/{barcode} |  |
| [**apiV20DatabaseStrainsGet**](StrainsApi.md#apiV20DatabaseStrainsGet) | **GET** /api/v2.0/{database}/strains |  |


<a id="apiV20DatabaseStrainsBarcodeGet"></a>
# **apiV20DatabaseStrainsBarcodeGet**
> apiV20DatabaseStrainsBarcodeGet(database, barcode, apiV20DatabaseStrainsBarcodeGetRequest)



Strain metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StrainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StrainsApi apiInstance = new StrainsApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
    ApiV20DatabaseStrainsBarcodeGetRequest apiV20DatabaseStrainsBarcodeGetRequest = new ApiV20DatabaseStrainsBarcodeGetRequest(); // ApiV20DatabaseStrainsBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseStrainsBarcodeGet(database, barcode, apiV20DatabaseStrainsBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling StrainsApi#apiV20DatabaseStrainsBarcodeGet");
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
| **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | |
| **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | |
| **apiV20DatabaseStrainsBarcodeGetRequest** | [**ApiV20DatabaseStrainsBarcodeGetRequest**](ApiV20DatabaseStrainsBarcodeGetRequest.md)|  | [optional] |

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
| **200** | List of strains objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

<a id="apiV20DatabaseStrainsBarcodePost"></a>
# **apiV20DatabaseStrainsBarcodePost**
> apiV20DatabaseStrainsBarcodePost(database, barcode, apiV20DatabaseStrainsBarcodeGetRequest)



Strain metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StrainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StrainsApi apiInstance = new StrainsApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
    ApiV20DatabaseStrainsBarcodeGetRequest apiV20DatabaseStrainsBarcodeGetRequest = new ApiV20DatabaseStrainsBarcodeGetRequest(); // ApiV20DatabaseStrainsBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseStrainsBarcodePost(database, barcode, apiV20DatabaseStrainsBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling StrainsApi#apiV20DatabaseStrainsBarcodePost");
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
| **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | |
| **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | |
| **apiV20DatabaseStrainsBarcodeGetRequest** | [**ApiV20DatabaseStrainsBarcodeGetRequest**](ApiV20DatabaseStrainsBarcodeGetRequest.md)|  | [optional] |

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
| **200** | List of strains objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

<a id="apiV20DatabaseStrainsBarcodePut"></a>
# **apiV20DatabaseStrainsBarcodePut**
> apiV20DatabaseStrainsBarcodePut(database, barcode, apiV20DatabaseStrainsBarcodeGetRequest)



Strain metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StrainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StrainsApi apiInstance = new StrainsApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
    ApiV20DatabaseStrainsBarcodeGetRequest apiV20DatabaseStrainsBarcodeGetRequest = new ApiV20DatabaseStrainsBarcodeGetRequest(); // ApiV20DatabaseStrainsBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseStrainsBarcodePut(database, barcode, apiV20DatabaseStrainsBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling StrainsApi#apiV20DatabaseStrainsBarcodePut");
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
| **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | |
| **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | |
| **apiV20DatabaseStrainsBarcodeGetRequest** | [**ApiV20DatabaseStrainsBarcodeGetRequest**](ApiV20DatabaseStrainsBarcodeGetRequest.md)|  | [optional] |

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
| **403** | Unauthorised access for this specific resource |  -  |

<a id="apiV20DatabaseStrainsGet"></a>
# **apiV20DatabaseStrainsGet**
> apiV20DatabaseStrainsGet(database, continent, offset, sampleAccession, latitude, collectionMonth, antigenicFormulas, strainName, labContact, sortorder, limit, serotype, region, country, collectionDate, returnAll, onlyFields, sourceNiche, collectionYear, secondarySampleAccession, sourceDetails, substrains, version, sourceType, orderby, myStrains, collectionTime, county, uberstrain, comment, longitude, reldate, assemblyBarcode, barcode, postcode, city)



Strain metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StrainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StrainsApi apiInstance = new StrainsApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String continent = "continent_example"; // String | 
    Integer offset = 0; // Integer | Cursor position in results
    String sampleAccession = "sampleAccession_example"; // String | 
    Float latitude = 3.4F; // Float | 
    Integer collectionMonth = 56; // Integer | 
    String antigenicFormulas = "antigenicFormulas_example"; // String | 
    String strainName = "strainName_example"; // String | 
    String labContact = "labContact_example"; // String | 
    String sortorder = "asc"; // String | Order of search results: asc or desc
    Integer limit = 50; // Integer | Number of results per page
    String serotype = "serotype_example"; // String | 
    String region = "region_example"; // String | 
    String country = "country_example"; // String | 
    Integer collectionDate = 56; // Integer | 
    Boolean returnAll = true; // Boolean | 
    List<String> onlyFields = Arrays.asList(); // List<String> | 
    String sourceNiche = "sourceNiche_example"; // String | 
    Integer collectionYear = 56; // Integer | 
    String secondarySampleAccession = "secondarySampleAccession_example"; // String | 
    String sourceDetails = "sourceDetails_example"; // String | 
    Boolean substrains = true; // Boolean | 
    Integer version = 56; // Integer | 
    String sourceType = "sourceType_example"; // String | 
    String orderby = "barcode"; // String | Field to order by. Default: barcode
    Boolean myStrains = true; // Boolean | 
    String collectionTime = "collectionTime_example"; // String | 
    String county = "county_example"; // String | 
    String uberstrain = "uberstrain_example"; // String | 
    String comment = "comment_example"; // String | 
    Float longitude = 3.4F; // Float | 
    Integer reldate = 56; // Integer | 
    String assemblyBarcode = "assemblyBarcode_example"; // String | 
    List<String> barcode = Arrays.asList(); // List<String> | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
    String postcode = "postcode_example"; // String | 
    String city = "city_example"; // String | 
    try {
      apiInstance.apiV20DatabaseStrainsGet(database, continent, offset, sampleAccession, latitude, collectionMonth, antigenicFormulas, strainName, labContact, sortorder, limit, serotype, region, country, collectionDate, returnAll, onlyFields, sourceNiche, collectionYear, secondarySampleAccession, sourceDetails, substrains, version, sourceType, orderby, myStrains, collectionTime, county, uberstrain, comment, longitude, reldate, assemblyBarcode, barcode, postcode, city);
    } catch (ApiException e) {
      System.err.println("Exception when calling StrainsApi#apiV20DatabaseStrainsGet");
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
| **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | |
| **continent** | **String**|  | [optional] |
| **offset** | **Integer**| Cursor position in results | [optional] [default to 0] |
| **sampleAccession** | **String**|  | [optional] |
| **latitude** | **Float**|  | [optional] |
| **collectionMonth** | **Integer**|  | [optional] |
| **antigenicFormulas** | **String**|  | [optional] |
| **strainName** | **String**|  | [optional] |
| **labContact** | **String**|  | [optional] |
| **sortorder** | **String**| Order of search results: asc or desc | [optional] [default to asc] |
| **limit** | **Integer**| Number of results per page | [optional] [default to 50] |
| **serotype** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |
| **country** | **String**|  | [optional] |
| **collectionDate** | **Integer**|  | [optional] |
| **returnAll** | **Boolean**|  | [optional] |
| **onlyFields** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **sourceNiche** | **String**|  | [optional] |
| **collectionYear** | **Integer**|  | [optional] |
| **secondarySampleAccession** | **String**|  | [optional] |
| **sourceDetails** | **String**|  | [optional] |
| **substrains** | **Boolean**|  | [optional] |
| **version** | **Integer**|  | [optional] |
| **sourceType** | **String**|  | [optional] |
| **orderby** | **String**| Field to order by. Default: barcode | [optional] [default to barcode] |
| **myStrains** | **Boolean**|  | [optional] |
| **collectionTime** | **String**|  | [optional] |
| **county** | **String**|  | [optional] |
| **uberstrain** | **String**|  | [optional] |
| **comment** | **String**|  | [optional] |
| **longitude** | **Float**|  | [optional] |
| **reldate** | **Integer**|  | [optional] |
| **assemblyBarcode** | **String**|  | [optional] |
| **barcode** | [**List&lt;String&gt;**](String.md)| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | [optional] |
| **postcode** | **String**|  | [optional] |
| **city** | **String**|  | [optional] |

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
| **200** | List of strains objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

