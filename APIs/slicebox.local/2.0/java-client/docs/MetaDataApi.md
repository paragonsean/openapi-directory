# MetaDataApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metadataFlatseriesGet**](MetaDataApi.md#metadataFlatseriesGet) | **GET** /metadata/flatseries |  |
| [**metadataFlatseriesIdGet**](MetaDataApi.md#metadataFlatseriesIdGet) | **GET** /metadata/flatseries/{id} |  |
| [**metadataFlatseriesQueryPost**](MetaDataApi.md#metadataFlatseriesQueryPost) | **POST** /metadata/flatseries/query |  |
| [**metadataImagesGet**](MetaDataApi.md#metadataImagesGet) | **GET** /metadata/images |  |
| [**metadataImagesIdGet**](MetaDataApi.md#metadataImagesIdGet) | **GET** /metadata/images/{id} |  |
| [**metadataImagesQueryPost**](MetaDataApi.md#metadataImagesQueryPost) | **POST** /metadata/images/query |  |
| [**metadataPatientsGet**](MetaDataApi.md#metadataPatientsGet) | **GET** /metadata/patients |  |
| [**metadataPatientsIdGet**](MetaDataApi.md#metadataPatientsIdGet) | **GET** /metadata/patients/{id} |  |
| [**metadataPatientsIdImagesGet**](MetaDataApi.md#metadataPatientsIdImagesGet) | **GET** /metadata/patients/{id}/images |  |
| [**metadataPatientsQueryPost**](MetaDataApi.md#metadataPatientsQueryPost) | **POST** /metadata/patients/query |  |
| [**metadataSeriesGet**](MetaDataApi.md#metadataSeriesGet) | **GET** /metadata/series |  |
| [**metadataSeriesIdGet**](MetaDataApi.md#metadataSeriesIdGet) | **GET** /metadata/series/{id} |  |
| [**metadataSeriesIdSeriestagsGet**](MetaDataApi.md#metadataSeriesIdSeriestagsGet) | **GET** /metadata/series/{id}/seriestags |  |
| [**metadataSeriesIdSeriestagsPost**](MetaDataApi.md#metadataSeriesIdSeriestagsPost) | **POST** /metadata/series/{id}/seriestags |  |
| [**metadataSeriesIdSeriestypesDelete**](MetaDataApi.md#metadataSeriesIdSeriestypesDelete) | **DELETE** /metadata/series/{id}/seriestypes |  |
| [**metadataSeriesIdSeriestypesGet**](MetaDataApi.md#metadataSeriesIdSeriestypesGet) | **GET** /metadata/series/{id}/seriestypes |  |
| [**metadataSeriesIdSourceGet**](MetaDataApi.md#metadataSeriesIdSourceGet) | **GET** /metadata/series/{id}/source |  |
| [**metadataSeriesQueryPost**](MetaDataApi.md#metadataSeriesQueryPost) | **POST** /metadata/series/query |  |
| [**metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete**](MetaDataApi.md#metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete) | **DELETE** /metadata/series/{seriesId}/seriestags/{seriesTagId} |  |
| [**metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete**](MetaDataApi.md#metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete) | **DELETE** /metadata/series/{seriesId}/seriestypes/{seriesTypeId} |  |
| [**metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut**](MetaDataApi.md#metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut) | **PUT** /metadata/series/{seriesId}/seriestypes/{seriesTypeId} |  |
| [**metadataSeriestagsGet**](MetaDataApi.md#metadataSeriestagsGet) | **GET** /metadata/seriestags |  |
| [**metadataStudiesGet**](MetaDataApi.md#metadataStudiesGet) | **GET** /metadata/studies |  |
| [**metadataStudiesIdGet**](MetaDataApi.md#metadataStudiesIdGet) | **GET** /metadata/studies/{id} |  |
| [**metadataStudiesIdImagesGet**](MetaDataApi.md#metadataStudiesIdImagesGet) | **GET** /metadata/studies/{id}/images |  |
| [**metadataStudiesQueryPost**](MetaDataApi.md#metadataStudiesQueryPost) | **POST** /metadata/studies/query |  |
| [**seriestypesSeriesQueryPost**](MetaDataApi.md#seriestypesSeriesQueryPost) | **POST** /seriestypes/series/query |  |


<a id="metadataFlatseriesGet"></a>
# **metadataFlatseriesGet**
> List&lt;FlatSeries&gt; metadataFlatseriesGet(startindex, count, orderby, orderascending, filter, sources, seriestypes, seriestags)



Returns a list of flattened metadata on the patient, study and series levels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of flat series
    Long count = 20L; // Long | size of returned slice of flat series
    String orderby = "orderby_example"; // String | flat series property to order results by
    Boolean orderascending = true; // Boolean | order result ascendingly if true, descendingly otherwise
    String filter = "filter_example"; // String | filter the results by matching substrings of flat series properties against this value
    String sources = "sources_example"; // String | filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    String seriestypes = "seriestypes_example"; // String | filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
    String seriestags = "seriestags_example"; // String | filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
    try {
      List<FlatSeries> result = apiInstance.metadataFlatseriesGet(startindex, count, orderby, orderascending, filter, sources, seriestypes, seriestags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataFlatseriesGet");
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
| **startindex** | **Long**| start index of returned slice of flat series | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of flat series | [optional] [default to 20] |
| **orderby** | **String**| flat series property to order results by | [optional] |
| **orderascending** | **Boolean**| order result ascendingly if true, descendingly otherwise | [optional] [default to true] |
| **filter** | **String**| filter the results by matching substrings of flat series properties against this value | [optional] |
| **sources** | **String**| filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] |
| **seriestypes** | **String**| filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22. | [optional] |
| **seriestags** | **String**| filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11. | [optional] |

### Return type

[**List&lt;FlatSeries&gt;**](FlatSeries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flat series |  -  |

<a id="metadataFlatseriesIdGet"></a>
# **metadataFlatseriesIdGet**
> FlatSeries metadataFlatseriesIdGet(id)



Return the flat series with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of flat series
    try {
      FlatSeries result = apiInstance.metadataFlatseriesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataFlatseriesIdGet");
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
| **id** | **Long**| ID of flat series | |

### Return type

[**FlatSeries**](FlatSeries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flat series response |  -  |
| **404** | flat series not found (invalid ID) |  -  |

<a id="metadataFlatseriesQueryPost"></a>
# **metadataFlatseriesQueryPost**
> List&lt;FlatSeries&gt; metadataFlatseriesQueryPost(query)



submit a query for flat series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Query query = new Query(); // Query | parameters of flat series query
    try {
      List<FlatSeries> result = apiInstance.metadataFlatseriesQueryPost(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataFlatseriesQueryPost");
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
| **query** | [**Query**](Query.md)| parameters of flat series query | |

### Return type

[**List&lt;FlatSeries&gt;**](FlatSeries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | flat series |  -  |

<a id="metadataImagesGet"></a>
# **metadataImagesGet**
> List&lt;Image&gt; metadataImagesGet(seriesid, startindex, count)



Returns a list of metadata on the image level of the DICOM hierarchy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long seriesid = 56L; // Long | reference to series to list images for
    Long startindex = 0L; // Long | start index of returned slice of images
    Long count = 20L; // Long | size of returned slice of images
    try {
      List<Image> result = apiInstance.metadataImagesGet(seriesid, startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataImagesGet");
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
| **seriesid** | **Long**| reference to series to list images for | |
| **startindex** | **Long**| start index of returned slice of images | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of images | [optional] [default to 20] |

### Return type

[**List&lt;Image&gt;**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | images |  -  |

<a id="metadataImagesIdGet"></a>
# **metadataImagesIdGet**
> Image metadataImagesIdGet(id)



Return the image with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of image
    try {
      Image result = apiInstance.metadataImagesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataImagesIdGet");
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
| **id** | **Long**| ID of image | |

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | image response |  -  |
| **404** | image not found (invalid ID) |  -  |

<a id="metadataImagesQueryPost"></a>
# **metadataImagesQueryPost**
> List&lt;Image&gt; metadataImagesQueryPost(query)



submit a query for images

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Query query = new Query(); // Query | parameters of images query
    try {
      List<Image> result = apiInstance.metadataImagesQueryPost(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataImagesQueryPost");
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
| **query** | [**Query**](Query.md)| parameters of images query | |

### Return type

[**List&lt;Image&gt;**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | images |  -  |

<a id="metadataPatientsGet"></a>
# **metadataPatientsGet**
> List&lt;Patient&gt; metadataPatientsGet(startindex, count, orderby, orderascending, filter, sources, seriestypes, seriestags)



Returns a list of metadata on the patient level of the DICOM hierarchy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of patients
    Long count = 20L; // Long | size of returned slice of patients
    String orderby = "orderby_example"; // String | patient property to order results by
    Boolean orderascending = true; // Boolean | order result ascendingly if true, descendingly otherwise
    String filter = "filter_example"; // String | filter the results by matching substrings of patient properties against this value
    String sources = "sources_example"; // String | filter the results by matching on one or more underlying series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    String seriestypes = "seriestypes_example"; // String | filter the results by matching on one or more underlying series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows results including series assigned to either of the series types with ids 3, 7 and 22.
    String seriestags = "seriestags_example"; // String | filter the results by matching on one or more underlying series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows results including series with either of the series tags with ids 6, 2 and 11.
    try {
      List<Patient> result = apiInstance.metadataPatientsGet(startindex, count, orderby, orderascending, filter, sources, seriestypes, seriestags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataPatientsGet");
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
| **startindex** | **Long**| start index of returned slice of patients | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of patients | [optional] [default to 20] |
| **orderby** | **String**| patient property to order results by | [optional] |
| **orderascending** | **Boolean**| order result ascendingly if true, descendingly otherwise | [optional] [default to true] |
| **filter** | **String**| filter the results by matching substrings of patient properties against this value | [optional] |
| **sources** | **String**| filter the results by matching on one or more underlying series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] |
| **seriestypes** | **String**| filter the results by matching on one or more underlying series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows results including series assigned to either of the series types with ids 3, 7 and 22. | [optional] |
| **seriestags** | **String**| filter the results by matching on one or more underlying series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows results including series with either of the series tags with ids 6, 2 and 11. | [optional] |

### Return type

[**List&lt;Patient&gt;**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | patients |  -  |

<a id="metadataPatientsIdGet"></a>
# **metadataPatientsIdGet**
> Patient metadataPatientsIdGet(id)



Return the patient with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of patient
    try {
      Patient result = apiInstance.metadataPatientsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataPatientsIdGet");
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
| **id** | **Long**| ID of patient | |

### Return type

[**Patient**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | patient response |  -  |
| **404** | patient not found (invalid ID) |  -  |

<a id="metadataPatientsIdImagesGet"></a>
# **metadataPatientsIdImagesGet**
> List&lt;Image&gt; metadataPatientsIdImagesGet(id, sources, seriestypes, seriestags)



Returns all images for the patient with the supplied patient ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of patient
    String sources = "sources_example"; // String | filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    String seriestypes = "seriestypes_example"; // String | filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
    String seriestags = "seriestags_example"; // String | filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
    try {
      List<Image> result = apiInstance.metadataPatientsIdImagesGet(id, sources, seriestypes, seriestags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataPatientsIdImagesGet");
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
| **id** | **Long**| ID of patient | |
| **sources** | **String**| filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] |
| **seriestypes** | **String**| filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22. | [optional] |
| **seriestags** | **String**| filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11. | [optional] |

### Return type

[**List&lt;Image&gt;**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of images |  -  |

<a id="metadataPatientsQueryPost"></a>
# **metadataPatientsQueryPost**
> List&lt;Patient&gt; metadataPatientsQueryPost(query)



submit a query for patients

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Query query = new Query(); // Query | parameters of patient query
    try {
      List<Patient> result = apiInstance.metadataPatientsQueryPost(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataPatientsQueryPost");
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
| **query** | [**Query**](Query.md)| parameters of patient query | |

### Return type

[**List&lt;Patient&gt;**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | patients |  -  |

<a id="metadataSeriesGet"></a>
# **metadataSeriesGet**
> List&lt;Series&gt; metadataSeriesGet(studyid, startindex, count, sources, seriestypes, seriestags)



Returns a list of metadata on the series level of the DICOM hierarchy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long studyid = 56L; // Long | reference to study to list series for
    Long startindex = 0L; // Long | start index of returned slice of series
    Long count = 20L; // Long | size of returned slice of series
    String sources = "sources_example"; // String | filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    String seriestypes = "seriestypes_example"; // String | filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
    String seriestags = "seriestags_example"; // String | filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
    try {
      List<Series> result = apiInstance.metadataSeriesGet(studyid, startindex, count, sources, seriestypes, seriestags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesGet");
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
| **studyid** | **Long**| reference to study to list series for | |
| **startindex** | **Long**| start index of returned slice of series | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of series | [optional] [default to 20] |
| **sources** | **String**| filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] |
| **seriestypes** | **String**| filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22. | [optional] |
| **seriestags** | **String**| filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11. | [optional] |

### Return type

[**List&lt;Series&gt;**](Series.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | series |  -  |

<a id="metadataSeriesIdGet"></a>
# **metadataSeriesIdGet**
> Series metadataSeriesIdGet(id)



Return the series with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of series
    try {
      Series result = apiInstance.metadataSeriesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesIdGet");
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
| **id** | **Long**| ID of series | |

### Return type

[**Series**](Series.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | series response |  -  |
| **404** | series not found (invalid ID) |  -  |

<a id="metadataSeriesIdSeriestagsGet"></a>
# **metadataSeriesIdSeriestagsGet**
> List&lt;Seriestag&gt; metadataSeriesIdSeriestagsGet(id)



get the list of series tags for the series with the supplied ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of series
    try {
      List<Seriestag> result = apiInstance.metadataSeriesIdSeriestagsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesIdSeriestagsGet");
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
| **id** | **Long**| ID of series | |

### Return type

[**List&lt;Seriestag&gt;**](Seriestag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of series tags |  -  |
| **404** | series not found (invalid ID) |  -  |

<a id="metadataSeriesIdSeriestagsPost"></a>
# **metadataSeriesIdSeriestagsPost**
> Seriestag metadataSeriesIdSeriestagsPost(id, query)



add a series tag to the series with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of series
    Seriestag query = new Seriestag(); // Seriestag | series tag to add
    try {
      Seriestag result = apiInstance.metadataSeriesIdSeriestagsPost(id, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesIdSeriestagsPost");
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
| **id** | **Long**| ID of series | |
| **query** | [**Seriestag**](Seriestag.md)| series tag to add | |

### Return type

[**Seriestag**](Seriestag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | added series tag |  -  |
| **404** | if no series with the supplied ID exists |  -  |

<a id="metadataSeriesIdSeriestypesDelete"></a>
# **metadataSeriesIdSeriestypesDelete**
> metadataSeriesIdSeriestypesDelete(id)



Delete all series types for the series with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of series
    try {
      apiInstance.metadataSeriesIdSeriestypesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesIdSeriestypesDelete");
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
| **id** | **Long**| ID of series | |

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
| **204** | series types deleted |  -  |

<a id="metadataSeriesIdSeriestypesGet"></a>
# **metadataSeriesIdSeriestypesGet**
> List&lt;Seriestype&gt; metadataSeriesIdSeriestypesGet(id)



get the list of series types for the series with the supplied ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of series
    try {
      List<Seriestype> result = apiInstance.metadataSeriesIdSeriestypesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesIdSeriestypesGet");
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
| **id** | **Long**| ID of series | |

### Return type

[**List&lt;Seriestype&gt;**](Seriestype.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of series types |  -  |
| **404** | series not found (invalid ID) |  -  |

<a id="metadataSeriesIdSourceGet"></a>
# **metadataSeriesIdSourceGet**
> Source metadataSeriesIdSourceGet(id)



Return the source of the series with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of series
    try {
      Source result = apiInstance.metadataSeriesIdSourceGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesIdSourceGet");
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
| **id** | **Long**| ID of series | |

### Return type

[**Source**](Source.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | source for series |  -  |
| **404** | series not found (invalid ID) |  -  |

<a id="metadataSeriesQueryPost"></a>
# **metadataSeriesQueryPost**
> List&lt;Series&gt; metadataSeriesQueryPost(query)



submit a query for series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Query query = new Query(); // Query | parameters of series query
    try {
      List<Series> result = apiInstance.metadataSeriesQueryPost(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesQueryPost");
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
| **query** | [**Query**](Query.md)| parameters of series query | |

### Return type

[**List&lt;Series&gt;**](Series.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | series |  -  |

<a id="metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete"></a>
# **metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete**
> metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete(seriesId, seriesTagId)



Delete the series tag with the supplied series tag ID from the series with the supplied series ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long seriesId = 56L; // Long | ID of series
    Long seriesTagId = 56L; // Long | ID of series tag to remove
    try {
      apiInstance.metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete(seriesId, seriesTagId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete");
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
| **seriesId** | **Long**| ID of series | |
| **seriesTagId** | **Long**| ID of series tag to remove | |

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
| **204** | series tag removed |  -  |

<a id="metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete"></a>
# **metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete**
> metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete(seriesId, seriesTypeId)



Delete the series type with the supplied series type ID from the series with the supplied series ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long seriesId = 56L; // Long | ID of series
    Long seriesTypeId = 56L; // Long | ID of series type to remove
    try {
      apiInstance.metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete(seriesId, seriesTypeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete");
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
| **seriesId** | **Long**| ID of series | |
| **seriesTypeId** | **Long**| ID of series type to remove | |

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
| **204** | series type removed |  -  |

<a id="metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut"></a>
# **metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut**
> metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut(seriesId, seriesTypeId)



Add the series type with the supplied series type ID to the series with the supplied series ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long seriesId = 56L; // Long | ID of series
    Long seriesTypeId = 56L; // Long | ID of series type to add
    try {
      apiInstance.metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut(seriesId, seriesTypeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut");
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
| **seriesId** | **Long**| ID of series | |
| **seriesTypeId** | **Long**| ID of series type to add | |

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
| **204** | series type added |  -  |
| **404** | no series or series type found for the supplied ID(s) |  -  |

<a id="metadataSeriestagsGet"></a>
# **metadataSeriestagsGet**
> List&lt;Seriestag&gt; metadataSeriestagsGet()



Returns a list of series tags currently currently in use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    try {
      List<Seriestag> result = apiInstance.metadataSeriestagsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataSeriestagsGet");
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

[**List&lt;Seriestag&gt;**](Seriestag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a list of unique series tags currently used to tag series |  -  |

<a id="metadataStudiesGet"></a>
# **metadataStudiesGet**
> List&lt;Study&gt; metadataStudiesGet(patientid, startindex, count, sources, seriestypes, seriestags)



Returns a list of metadata on the study level of the DICOM hierarchy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long patientid = 56L; // Long | reference to patient to list studies for
    Long startindex = 0L; // Long | start index of returned slice of studies
    Long count = 20L; // Long | size of returned slice of studies
    String sources = "sources_example"; // String | filter the results by matching on one or more underlying series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    String seriestypes = "seriestypes_example"; // String | filter the results by matching on one or more underlying series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows results including series assigned to either of the series types with ids 3, 7 and 22.
    String seriestags = "seriestags_example"; // String | filter the results by matching on one or more underlying series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows results including series with either of the series tags with ids 6, 2 and 11.
    try {
      List<Study> result = apiInstance.metadataStudiesGet(patientid, startindex, count, sources, seriestypes, seriestags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataStudiesGet");
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
| **patientid** | **Long**| reference to patient to list studies for | |
| **startindex** | **Long**| start index of returned slice of studies | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of studies | [optional] [default to 20] |
| **sources** | **String**| filter the results by matching on one or more underlying series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] |
| **seriestypes** | **String**| filter the results by matching on one or more underlying series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows results including series assigned to either of the series types with ids 3, 7 and 22. | [optional] |
| **seriestags** | **String**| filter the results by matching on one or more underlying series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows results including series with either of the series tags with ids 6, 2 and 11. | [optional] |

### Return type

[**List&lt;Study&gt;**](Study.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | studies |  -  |

<a id="metadataStudiesIdGet"></a>
# **metadataStudiesIdGet**
> Study metadataStudiesIdGet(id)



Return the study with the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of study
    try {
      Study result = apiInstance.metadataStudiesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataStudiesIdGet");
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
| **id** | **Long**| ID of study | |

### Return type

[**Study**](Study.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | study response |  -  |
| **404** | study not found (invalid ID) |  -  |

<a id="metadataStudiesIdImagesGet"></a>
# **metadataStudiesIdImagesGet**
> List&lt;Image&gt; metadataStudiesIdImagesGet(id, sources, seriestypes, seriestags)



Returns all images for the study with the supplied study ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Long id = 56L; // Long | ID of study
    String sources = "sources_example"; // String | filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
    String seriestypes = "seriestypes_example"; // String | filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
    String seriestags = "seriestags_example"; // String | filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
    try {
      List<Image> result = apiInstance.metadataStudiesIdImagesGet(id, sources, seriestypes, seriestags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataStudiesIdImagesGet");
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
| **id** | **Long**| ID of study | |
| **sources** | **String**| filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] |
| **seriestypes** | **String**| filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22. | [optional] |
| **seriestags** | **String**| filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11. | [optional] |

### Return type

[**List&lt;Image&gt;**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of images |  -  |
| **404** | study not found (invalid ID) |  -  |

<a id="metadataStudiesQueryPost"></a>
# **metadataStudiesQueryPost**
> List&lt;Study&gt; metadataStudiesQueryPost(query)



submit a query for studies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Query query = new Query(); // Query | parameters of study query
    try {
      List<Study> result = apiInstance.metadataStudiesQueryPost(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#metadataStudiesQueryPost");
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
| **query** | [**Query**](Query.md)| parameters of study query | |

### Return type

[**List&lt;Study&gt;**](Study.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | studies |  -  |

<a id="seriestypesSeriesQueryPost"></a>
# **seriestypesSeriesQueryPost**
> Seriesidseriestypesresult seriestypesSeriesQueryPost(query)



submit a query for seriestypes for a list of series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetaDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    MetaDataApi apiInstance = new MetaDataApi(defaultClient);
    Idsquery query = new Idsquery(); // Idsquery | parameters of series query
    try {
      Seriesidseriestypesresult result = apiInstance.seriestypesSeriesQueryPost(query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetaDataApi#seriestypesSeriesQueryPost");
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
| **query** | [**Idsquery**](Idsquery.md)| parameters of series query | |

### Return type

[**Seriesidseriestypesresult**](Seriesidseriestypesresult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | series |  -  |

