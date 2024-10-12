# StraindataApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20DatabaseStraindataGet**](StraindataApi.md#apiV20DatabaseStraindataGet) | **GET** /api/v2.0/{database}/straindata |  |


<a id="apiV20DatabaseStraindataGet"></a>
# **apiV20DatabaseStraindataGet**
> apiV20DatabaseStraindataGet(database, continent, offset, sampleAccession, latitude, collectionMonth, strainName, labContact, sortorder, n50, limit, serotype, region, country, collectionDate, customFields, onlyFields, sourceNiche, collectionYear, secondarySampleAccession, sourceDetails, substrains, version, sourceType, orderby, myStrains, collectionTime, county, uberstrain, topSpecies, comment, longitude, reldate, barcode, postcode, email, assemblyStatus, city)



Strain data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StraindataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StraindataApi apiInstance = new StraindataApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String continent = "continent_example"; // String | 
    Integer offset = 0; // Integer | Cursor position in results
    String sampleAccession = "sampleAccession_example"; // String | 
    Float latitude = 3.4F; // Float | 
    Integer collectionMonth = 56; // Integer | 
    String strainName = "strainName_example"; // String | 
    String labContact = "labContact_example"; // String | 
    String sortorder = "asc"; // String | Order of search results: asc or desc
    Integer n50 = 56; // Integer | 
    Integer limit = 50; // Integer | Number of results per page
    String serotype = "serotype_example"; // String | 
    String region = "region_example"; // String | 
    String country = "country_example"; // String | 
    Integer collectionDate = 56; // Integer | 
    String customFields = "customFields_example"; // String | 
    List<String> onlyFields = Arrays.asList(); // List<String> | 
    String sourceNiche = "sourceNiche_example"; // String | 
    Integer collectionYear = 56; // Integer | 
    String secondarySampleAccession = "secondarySampleAccession_example"; // String | 
    String sourceDetails = "sourceDetails_example"; // String | 
    Boolean substrains = true; // Boolean | 
    Integer version = 56; // Integer | 
    String sourceType = "sourceType_example"; // String | 
    String orderby = "orderby_example"; // String | Field to order by. Default: strain barcode
    Boolean myStrains = true; // Boolean | 
    String collectionTime = "collectionTime_example"; // String | 
    String county = "county_example"; // String | 
    String uberstrain = "uberstrain_example"; // String | 
    String topSpecies = "topSpecies_example"; // String | 
    String comment = "comment_example"; // String | 
    Float longitude = 3.4F; // Float | 
    Integer reldate = 56; // Integer | 
    List<String> barcode = Arrays.asList(); // List<String> | Unique barcode for Traces records, <database prefix>_<ID code>_AS e.g. SAL_AA0001AA_AS
    String postcode = "postcode_example"; // String | 
    String email = "email_example"; // String | 
    String assemblyStatus = "assemblyStatus_example"; // String | 
    String city = "city_example"; // String | 
    try {
      apiInstance.apiV20DatabaseStraindataGet(database, continent, offset, sampleAccession, latitude, collectionMonth, strainName, labContact, sortorder, n50, limit, serotype, region, country, collectionDate, customFields, onlyFields, sourceNiche, collectionYear, secondarySampleAccession, sourceDetails, substrains, version, sourceType, orderby, myStrains, collectionTime, county, uberstrain, topSpecies, comment, longitude, reldate, barcode, postcode, email, assemblyStatus, city);
    } catch (ApiException e) {
      System.err.println("Exception when calling StraindataApi#apiV20DatabaseStraindataGet");
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
| **strainName** | **String**|  | [optional] |
| **labContact** | **String**|  | [optional] |
| **sortorder** | **String**| Order of search results: asc or desc | [optional] [default to asc] |
| **n50** | **Integer**|  | [optional] |
| **limit** | **Integer**| Number of results per page | [optional] [default to 50] |
| **serotype** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |
| **country** | **String**|  | [optional] |
| **collectionDate** | **Integer**|  | [optional] |
| **customFields** | **String**|  | [optional] |
| **onlyFields** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **sourceNiche** | **String**|  | [optional] |
| **collectionYear** | **Integer**|  | [optional] |
| **secondarySampleAccession** | **String**|  | [optional] |
| **sourceDetails** | **String**|  | [optional] |
| **substrains** | **Boolean**|  | [optional] |
| **version** | **Integer**|  | [optional] |
| **sourceType** | **String**|  | [optional] |
| **orderby** | **String**| Field to order by. Default: strain barcode | [optional] |
| **myStrains** | **Boolean**|  | [optional] |
| **collectionTime** | **String**|  | [optional] |
| **county** | **String**|  | [optional] |
| **uberstrain** | **String**|  | [optional] |
| **topSpecies** | **String**|  | [optional] |
| **comment** | **String**|  | [optional] |
| **longitude** | **Float**|  | [optional] |
| **reldate** | **Integer**|  | [optional] |
| **barcode** | [**List&lt;String&gt;**](String.md)| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS | [optional] |
| **postcode** | **String**|  | [optional] |
| **email** | **String**|  | [optional] |
| **assemblyStatus** | **String**|  | [optional] |
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
| **200** | List of straindata objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

