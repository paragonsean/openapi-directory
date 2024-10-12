# StrainsversionApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20DatabaseStrainsversionGet**](StrainsversionApi.md#apiV20DatabaseStrainsversionGet) | **GET** /api/v2.0/{database}/strainsversion |  |


<a id="apiV20DatabaseStrainsversionGet"></a>
# **apiV20DatabaseStrainsversionGet**
> apiV20DatabaseStrainsversionGet(database, continent, offset, sampleAccession, latitude, collectionMonth, antigenicFormulas, strainName, labContact, sortorder, limit, serotype, region, country, collectionDate, returnAll, onlyFields, sourceNiche, collectionYear, secondarySampleAccession, sourceDetails, substrains, version, sourceType, orderby, myStrains, collectionTime, county, uberstrain, comment, longitude, reldate, assemblyBarcode, barcode, postcode, city)



Strain previous metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StrainsversionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StrainsversionApi apiInstance = new StrainsversionApi(defaultClient);
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
      apiInstance.apiV20DatabaseStrainsversionGet(database, continent, offset, sampleAccession, latitude, collectionMonth, antigenicFormulas, strainName, labContact, sortorder, limit, serotype, region, country, collectionDate, returnAll, onlyFields, sourceNiche, collectionYear, secondarySampleAccession, sourceDetails, substrains, version, sourceType, orderby, myStrains, collectionTime, county, uberstrain, comment, longitude, reldate, assemblyBarcode, barcode, postcode, city);
    } catch (ApiException e) {
      System.err.println("Exception when calling StrainsversionApi#apiV20DatabaseStrainsversionGet");
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
| **200** | List of strainsversion objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

