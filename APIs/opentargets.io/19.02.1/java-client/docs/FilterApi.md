# FilterApi

All URIs are relative to *http://platform-api.opentargets.io/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAssociationFilter_0**](FilterApi.md#getAssociationFilter_0) | **GET** /platform/public/association/filter | Filter available associations |
| [**getEvidenceFilter_0**](FilterApi.md#getEvidenceFilter_0) | **GET** /platform/public/evidence/filter | Filter available evidence |
| [**postAssociationFilter_0**](FilterApi.md#postAssociationFilter_0) | **POST** /platform/public/association/filter | Batch query available associations |
| [**postEvidenceFilter_0**](FilterApi.md#postEvidenceFilter_0) | **POST** /platform/public/evidence/filter | Batch filter available evidence |


<a id="getAssociationFilter_0"></a>
# **getAssociationFilter_0**
> getAssociationFilter_0(target, disease, therapeuticArea, datasource, datatype, pathway, targetClass, uniprotkw, direct, datastructure, fields, facets, scorevalueMin, scorevalueMax, scorevalueTypes, size, from, format, sort, search)

Filter available associations

More complex queries for associations scores and objects can be done using this method, which allows to sort in different order, restrict to a specific class of diseases or targets, as well as filtering results by score and associated pathways. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    FilterApi apiInstance = new FilterApi(defaultClient);
    String target = "target_example"; // String | A target identifier listed as target.id.
    String disease = "disease_example"; // String | An EFO code listed as disease.id.
    String therapeuticArea = "therapeuticArea_example"; // String | An EFO code of a therapeutic area.
    String datasource = "datasource_example"; // String | Data source to consider.
    String datatype = "datatype_example"; // String | Data type to consider.
    String pathway = "pathway_example"; // String | A Reactome pathway identifier (returning only those targets linked to the specified pathway).
    String targetClass = "targetClass_example"; // String | A ChEMBL target class identifier (returning only those targets belonging to the specified class).
    String uniprotkw = "uniprotkw_example"; // String | A UniProt keyword (meaning all the targets linked to that keyword).
    Boolean direct = true; // Boolean | If `true`, it returns associations that have at least one direct evidence connecting the target and the disease. If `false` it only returns associations for which there is no direct evidence connecting the target and the disease, but only evidence connecting the target to a children of the disease in the EFO ontology.
    String datastructure = "datastructure_example"; // String | Type of data structure to return. Can be 'full', 'simple', 'ids', or 'count'.
    String fields = "fields_example"; // String | Fields you want to retrieve. This will get priority over the data structure requested.
    Boolean facets = false; // Boolean | Returns facets
    Float scorevalueMin = 0F; // Float | Filter by minimum score value. The default is 0, but using 0.2 is a good trade-off to filter lower quality data points.
    Float scorevalueMax = 3.4F; // Float | Filter by maximum score value.
    String scorevalueTypes = "scorevalueTypes_example"; // String | Score types to apply the score value min and max filters. The default is `overall`.
    BigDecimal size = new BigDecimal(78); // BigDecimal | Maximum amount of results to return. Defaults to 10, max is 10000.
    BigDecimal from = new BigDecimal(78); // BigDecimal | How many initial results should be skipped. Defaults to 0.
    String format = "format_example"; // String | Format to get the data back. Can be 'json', 'xml', 'tab' or 'csv'. **Note** that this option can only be used when calling the API directly and will not work in this page. The response here will always be JSON.
    String sort = "sort_example"; // String | Sort by the given score type. Defaults to 'overall' and descending order. Use '~' prefix to do ascending order e.g. '~overall'. You will call a data type score like: 'datatypes.literature', and a data source as 'datasources.gwas'. Supports multiple entries. 
    String search = "search_example"; // String | Restrict the filtered results to those matching the passed string. The matching is done with a phrase match prefix. 
    try {
      apiInstance.getAssociationFilter_0(target, disease, therapeuticArea, datasource, datatype, pathway, targetClass, uniprotkw, direct, datastructure, fields, facets, scorevalueMin, scorevalueMax, scorevalueTypes, size, from, format, sort, search);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilterApi#getAssociationFilter_0");
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
| **target** | **String**| A target identifier listed as target.id. | [optional] |
| **disease** | **String**| An EFO code listed as disease.id. | [optional] |
| **therapeuticArea** | **String**| An EFO code of a therapeutic area. | [optional] |
| **datasource** | **String**| Data source to consider. | [optional] |
| **datatype** | **String**| Data type to consider. | [optional] |
| **pathway** | **String**| A Reactome pathway identifier (returning only those targets linked to the specified pathway). | [optional] |
| **targetClass** | **String**| A ChEMBL target class identifier (returning only those targets belonging to the specified class). | [optional] |
| **uniprotkw** | **String**| A UniProt keyword (meaning all the targets linked to that keyword). | [optional] |
| **direct** | **Boolean**| If &#x60;true&#x60;, it returns associations that have at least one direct evidence connecting the target and the disease. If &#x60;false&#x60; it only returns associations for which there is no direct evidence connecting the target and the disease, but only evidence connecting the target to a children of the disease in the EFO ontology. | [optional] |
| **datastructure** | **String**| Type of data structure to return. Can be &#39;full&#39;, &#39;simple&#39;, &#39;ids&#39;, or &#39;count&#39;. | [optional] |
| **fields** | **String**| Fields you want to retrieve. This will get priority over the data structure requested. | [optional] |
| **facets** | **Boolean**| Returns facets | [optional] [default to false] |
| **scorevalueMin** | **Float**| Filter by minimum score value. The default is 0, but using 0.2 is a good trade-off to filter lower quality data points. | [optional] [default to 0] |
| **scorevalueMax** | **Float**| Filter by maximum score value. | [optional] |
| **scorevalueTypes** | **String**| Score types to apply the score value min and max filters. The default is &#x60;overall&#x60;. | [optional] |
| **size** | **BigDecimal**| Maximum amount of results to return. Defaults to 10, max is 10000. | [optional] |
| **from** | **BigDecimal**| How many initial results should be skipped. Defaults to 0. | [optional] |
| **format** | **String**| Format to get the data back. Can be &#39;json&#39;, &#39;xml&#39;, &#39;tab&#39; or &#39;csv&#39;. **Note** that this option can only be used when calling the API directly and will not work in this page. The response here will always be JSON. | [optional] |
| **sort** | **String**| Sort by the given score type. Defaults to &#39;overall&#39; and descending order. Use &#39;~&#39; prefix to do ascending order e.g. &#39;~overall&#39;. You will call a data type score like: &#39;datatypes.literature&#39;, and a data source as &#39;datasources.gwas&#39;. Supports multiple entries.  | [optional] |
| **search** | **String**| Restrict the filtered results to those matching the passed string. The matching is done with a phrase match prefix.  | [optional] |

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
| **200** | Successful response |  -  |

<a id="getEvidenceFilter_0"></a>
# **getEvidenceFilter_0**
> getEvidenceFilter_0(target, disease, dataSource, datatype, pathway, uniprotkw, datastructure, fields, scorevalueMin, scorevalueMax, sort, size, from, format)

Filter available evidence

The filter method allows to retrieve the specific data that supports a connection between targets and diseases. Filters can be used to restrict the results by source and type of data, or limit results to targets which are part of a particular pathway. Minimum and maximum scores can be specified as well as the type of evidence linking target and disease. **Note** that multiple genes and diseases can be specified in the same request. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    FilterApi apiInstance = new FilterApi(defaultClient);
    String target = "target_example"; // String | A target identifier listed as target.id.
    String disease = "disease_example"; // String | An EFO code listed as disease.id.
    String dataSource = "dataSource_example"; // String | Data source to consider.
    String datatype = "datatype_example"; // String | Data type to consider.
    String pathway = "pathway_example"; // String | A pathway identifier (meaning all the targets linked to that pathway).
    String uniprotkw = "uniprotkw_example"; // String | A UniProt keyword (meaning all the targets linked to that keyword).
    String datastructure = "datastructure_example"; // String | Type of data structure to return. Can be 'full', 'simple', 'ids', or 'count'.
    String fields = "fields_example"; // String | The fields you want to retrieve. This will get priority over the data structure requested.
    Float scorevalueMin = 0F; // Float | Filter by minimum score value. The default is 0, but using 0.2 is a good trade-off to filter lower quality data points.
    Float scorevalueMax = 3.4F; // Float | Filter by maximum score value.
    String sort = "sort_example"; // String | Sort by the given field. The default is 'scores.association_score' in descending order. Use '~' prefix to do ascending order e.g. '~scores.association_score'. It supports multiple entries. 
    BigDecimal size = new BigDecimal(78); // BigDecimal | Maximum amount of results to return. Defaults to 10, max is 10000.
    BigDecimal from = new BigDecimal(78); // BigDecimal | How many initial results should be skipped. Defaults to 0.
    String format = "format_example"; // String | Format to get the data back. Can be 'json', 'xml', 'tab' or 'csv'. **Note** that this option can only be used when calling the API directly and will not work in this page. The response here will always be JSON.
    try {
      apiInstance.getEvidenceFilter_0(target, disease, dataSource, datatype, pathway, uniprotkw, datastructure, fields, scorevalueMin, scorevalueMax, sort, size, from, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilterApi#getEvidenceFilter_0");
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
| **target** | **String**| A target identifier listed as target.id. | [optional] |
| **disease** | **String**| An EFO code listed as disease.id. | [optional] |
| **dataSource** | **String**| Data source to consider. | [optional] |
| **datatype** | **String**| Data type to consider. | [optional] |
| **pathway** | **String**| A pathway identifier (meaning all the targets linked to that pathway). | [optional] |
| **uniprotkw** | **String**| A UniProt keyword (meaning all the targets linked to that keyword). | [optional] |
| **datastructure** | **String**| Type of data structure to return. Can be &#39;full&#39;, &#39;simple&#39;, &#39;ids&#39;, or &#39;count&#39;. | [optional] |
| **fields** | **String**| The fields you want to retrieve. This will get priority over the data structure requested. | [optional] |
| **scorevalueMin** | **Float**| Filter by minimum score value. The default is 0, but using 0.2 is a good trade-off to filter lower quality data points. | [optional] [default to 0] |
| **scorevalueMax** | **Float**| Filter by maximum score value. | [optional] |
| **sort** | **String**| Sort by the given field. The default is &#39;scores.association_score&#39; in descending order. Use &#39;~&#39; prefix to do ascending order e.g. &#39;~scores.association_score&#39;. It supports multiple entries.  | [optional] |
| **size** | **BigDecimal**| Maximum amount of results to return. Defaults to 10, max is 10000. | [optional] |
| **from** | **BigDecimal**| How many initial results should be skipped. Defaults to 0. | [optional] |
| **format** | **String**| Format to get the data back. Can be &#39;json&#39;, &#39;xml&#39;, &#39;tab&#39; or &#39;csv&#39;. **Note** that this option can only be used when calling the API directly and will not work in this page. The response here will always be JSON. | [optional] |

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
| **200** | Successful response |  -  |

<a id="postAssociationFilter_0"></a>
# **postAssociationFilter_0**
> postAssociationFilter_0(body)

Batch query available associations

Complex queries and filters for association objects can also be submitted using a JSON object and the equivalent POST method. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    FilterApi apiInstance = new FilterApi(defaultClient);
    String body = "body_example"; // String | Filters to apply when retrieving association objects.
    try {
      apiInstance.postAssociationFilter_0(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilterApi#postAssociationFilter_0");
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
| **body** | **String**| Filters to apply when retrieving association objects. | |

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
| **200** | Successful response |  -  |

<a id="postEvidenceFilter_0"></a>
# **postEvidenceFilter_0**
> postEvidenceFilter_0(body)

Batch filter available evidence

POST version of [/public/evidence/filter](#!/public/get_public_evidence_filter). Filters can be specified as part of a &#x60;json&#x60; object in the body, simplifying the submission of queries. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://platform-api.opentargets.io/v3");

    FilterApi apiInstance = new FilterApi(defaultClient);
    String body = "body_example"; // String | Filters to apply when retrieving evidence string objects.
    try {
      apiInstance.postEvidenceFilter_0(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilterApi#postEvidenceFilter_0");
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
| **body** | **String**| Filters to apply when retrieving evidence string objects. | |

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
| **200** | Successful response |  -  |

