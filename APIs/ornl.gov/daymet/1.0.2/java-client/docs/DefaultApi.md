# DefaultApi

All URIs are relative to *https://daymet.ornl.gov/single-pixel*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiDataGet**](DefaultApi.md#apiDataGet) | **GET** /api/data | Download Daymet Data |
| [**previewGet**](DefaultApi.md#previewGet) | **GET** /preview | Preview Daymet Data in a web browser |
| [**sendSaveDataGet**](DefaultApi.md#sendSaveDataGet) | **GET** /send/saveData | Download Daymet Data |
| [**visualizeGet**](DefaultApi.md#visualizeGet) | **GET** /visualize | Visualize Daymet Data in a web browser |


<a id="apiDataGet"></a>
# **apiDataGet**
> apiDataGet(lat, lon, format, vars, years, start, end)

Download Daymet Data

Returns a csv or json of the requested data to local machine

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://daymet.ornl.gov/single-pixel");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String format = "csv"; // String | Specify a format for data retrieval.
    List<String> vars = Arrays.asList(); // List<String> | Daymet Daily weather estimates.
    List<String> years = Arrays.asList(); // List<String> | Subset on years [1980..2019].
    LocalDate start = LocalDate.now(); // LocalDate | Subset on dates (start date).
    LocalDate end = LocalDate.now(); // LocalDate | Subset on dates (end date).
    try {
      apiInstance.apiDataGet(lat, lon, format, vars, years, start, end);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiDataGet");
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
| **lat** | **Double**| Latitude component of location. | |
| **lon** | **Double**| Longitude component of location. | |
| **format** | **String**| Specify a format for data retrieval. | [enum: csv, json] |
| **vars** | [**List&lt;String&gt;**](String.md)| Daymet Daily weather estimates. | [optional] |
| **years** | [**List&lt;String&gt;**](String.md)| Subset on years [1980..2019]. | [optional] |
| **start** | **LocalDate**| Subset on dates (start date). | [optional] |
| **end** | **LocalDate**| Subset on dates (end date). | [optional] |

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
| **200** | Successful Execution |  -  |
| **0** | Unexpected Error |  -  |

<a id="previewGet"></a>
# **previewGet**
> previewGet(lat, lon, format, vars, years, start, end)

Preview Daymet Data in a web browser

Returns a table to the browser displaying requested data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://daymet.ornl.gov/single-pixel");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location
    Double lon = 3.4D; // Double | Longitude component of location.
    String format = "csv"; // String | Specify a format for data retrieval.
    List<String> vars = Arrays.asList(); // List<String> | Daymet Daily weather estimates.
    List<String> years = Arrays.asList(); // List<String> | Subset on years [1980..2019].
    LocalDate start = LocalDate.now(); // LocalDate | Subset on dates (start date).
    LocalDate end = LocalDate.now(); // LocalDate | Subset on dates (end date).
    try {
      apiInstance.previewGet(lat, lon, format, vars, years, start, end);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#previewGet");
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
| **lat** | **Double**| Latitude component of location | |
| **lon** | **Double**| Longitude component of location. | |
| **format** | **String**| Specify a format for data retrieval. | [enum: csv, json] |
| **vars** | [**List&lt;String&gt;**](String.md)| Daymet Daily weather estimates. | [optional] |
| **years** | [**List&lt;String&gt;**](String.md)| Subset on years [1980..2019]. | [optional] |
| **start** | **LocalDate**| Subset on dates (start date). | [optional] |
| **end** | **LocalDate**| Subset on dates (end date). | [optional] |

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
| **200** | Successful Execution |  -  |
| **0** | Unexpected Error |  -  |

<a id="sendSaveDataGet"></a>
# **sendSaveDataGet**
> sendSaveDataGet(lat, lon, format, vars, years, start, end)

Download Daymet Data

Returns a csv or json of the requested data to local machine

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://daymet.ornl.gov/single-pixel");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String format = "csv"; // String | Specify a format for data retrieval.
    List<String> vars = Arrays.asList(); // List<String> | Daymet Daily weather estimates.
    List<String> years = Arrays.asList(); // List<String> | Subset on years [1980..2019].
    LocalDate start = LocalDate.now(); // LocalDate | Subset on dates (start date).
    LocalDate end = LocalDate.now(); // LocalDate | Subset on dates (end date).
    try {
      apiInstance.sendSaveDataGet(lat, lon, format, vars, years, start, end);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendSaveDataGet");
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
| **lat** | **Double**| Latitude component of location. | |
| **lon** | **Double**| Longitude component of location. | |
| **format** | **String**| Specify a format for data retrieval. | [enum: csv, json] |
| **vars** | [**List&lt;String&gt;**](String.md)| Daymet Daily weather estimates. | [optional] |
| **years** | [**List&lt;String&gt;**](String.md)| Subset on years [1980..2019]. | [optional] |
| **start** | **LocalDate**| Subset on dates (start date). | [optional] |
| **end** | **LocalDate**| Subset on dates (end date). | [optional] |

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
| **200** | Successful Execution |  -  |
| **0** | Unexpected Error |  -  |

<a id="visualizeGet"></a>
# **visualizeGet**
> visualizeGet(lat, lon, format, vars, years, start, end)

Visualize Daymet Data in a web browser

Returns plots to a web browser of requested data using Plotly

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://daymet.ornl.gov/single-pixel");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude component of location.
    Double lon = 3.4D; // Double | Longitude component of location.
    String format = "csv"; // String | Specify a format for data retrieval.
    List<String> vars = Arrays.asList(); // List<String> | Daymet Daily weather estimates.
    List<String> years = Arrays.asList(); // List<String> | Subset on years [1980..2019].
    LocalDate start = LocalDate.now(); // LocalDate | Subset on dates (start date).
    LocalDate end = LocalDate.now(); // LocalDate | Subset on dates (end date).
    try {
      apiInstance.visualizeGet(lat, lon, format, vars, years, start, end);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#visualizeGet");
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
| **lat** | **Double**| Latitude component of location. | |
| **lon** | **Double**| Longitude component of location. | |
| **format** | **String**| Specify a format for data retrieval. | [enum: csv, json] |
| **vars** | [**List&lt;String&gt;**](String.md)| Daymet Daily weather estimates. | [optional] |
| **years** | [**List&lt;String&gt;**](String.md)| Subset on years [1980..2019]. | [optional] |
| **start** | **LocalDate**| Subset on dates (start date). | [optional] |
| **end** | **LocalDate**| Subset on dates (end date). | [optional] |

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
| **200** | Successful Execution |  -  |
| **0** | Unexpected Error |  -  |

