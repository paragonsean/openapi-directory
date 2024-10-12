# AnalysisApi

All URIs are relative to *https://visagecloud.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**compareFacesUsingGET**](AnalysisApi.md#compareFacesUsingGET) | **GET** /rest/v1.1/analysis/compare | Compare several faces identified by faceHash, without depending on mapping faces to profiles |
| [**performAnalysisUsingPOST**](AnalysisApi.md#performAnalysisUsingPOST) | **POST** /rest/v1.1/analysis/detection | Perform detection on a given picture or picture URL |
| [**performRecognitionUsingPOST**](AnalysisApi.md#performRecognitionUsingPOST) | **POST** /rest/v1.1/analysis/recognition | Perform labeled recognition on a given picture or picture URL |
| [**retrieveAnalysisUsingGET**](AnalysisApi.md#retrieveAnalysisUsingGET) | **GET** /rest/v1.1/analysis/retrieve | Retrieve a complete analysis object including both detection and recognition information |
| [**retriveLatestUsingGET**](AnalysisApi.md#retriveLatestUsingGET) | **GET** /rest/v1.1/analysis/listLatest | Retrieve the last *count* operations per current account |


<a id="compareFacesUsingGET"></a>
# **compareFacesUsingGET**
> RestResponse compareFacesUsingGET(accessKey, secretKey, faceHashes, showDetails)

Compare several faces identified by faceHash, without depending on mapping faces to profiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    List<String> faceHashes = Arrays.asList(); // List<String> | The IDs of the faces which you want compared, comma-separated
    Boolean showDetails = false; // Boolean | Show details
    try {
      RestResponse result = apiInstance.compareFacesUsingGET(accessKey, secretKey, faceHashes, showDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#compareFacesUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **faceHashes** | [**List&lt;String&gt;**](String.md)| The IDs of the faces which you want compared, comma-separated | |
| **showDetails** | **Boolean**| Show details | [optional] [default to false] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="performAnalysisUsingPOST"></a>
# **performAnalysisUsingPOST**
> RestResponse performAnalysisUsingPOST(accessKey, secretKey, storeAnalysisPicture, storeFacePictures, storeResult, retentionTime, pictureURL, algorithmVersion, autoRotate, skipEXIF, waitForPictureUpload, filters, options, picture)

Perform detection on a given picture or picture URL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    Boolean storeAnalysisPicture = true; // Boolean | Boolean value indicating whether you want the picture of the analysis to be stored for later retrieval
    Boolean storeFacePictures = true; // Boolean | Boolean value indicating whether you want the faces inside the picture to be stored for later retrieval
    Boolean storeResult = true; // Boolean | Boolean value indicating whether you want the result of the analysis to be stored
    Integer retentionTime = 56; // Integer | How many seconds the results should be retained in stoarage?
    String pictureURL = "pictureURL_example"; // String | The URL of the picture, assuming it is served by a third party server. Server should be accesible from the Internet or through another netwoek by VisageCloud infrastructure
    String algorithmVersion = "V1"; // String | Algorithm version (V2 is more performant but not backward compatible)
    Boolean autoRotate = false; // Boolean | Auto-rotate to find flipped or rotate faces
    Boolean skipEXIF = false; // Boolean | Skip EXIF rotation procesing
    Boolean waitForPictureUpload = false; // Boolean | Waits until the picture is successfully uploaded, before returning the response back the the client
    List<String> filters = Arrays.asList(); // List<String> | [For advanced users only] Change feature filters for robustness of feature extraction. Tweaking this parameter may affect per
    String options = "options_example"; // String | [For advanced users only] Options for preprocessing of image.
    String picture = "picture_example"; // String | The multipart/form-data version of the image, in case a direct upload is used. At least one of picture or pictureURL must be present
    try {
      RestResponse result = apiInstance.performAnalysisUsingPOST(accessKey, secretKey, storeAnalysisPicture, storeFacePictures, storeResult, retentionTime, pictureURL, algorithmVersion, autoRotate, skipEXIF, waitForPictureUpload, filters, options, picture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#performAnalysisUsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **storeAnalysisPicture** | **Boolean**| Boolean value indicating whether you want the picture of the analysis to be stored for later retrieval | [optional] [default to true] |
| **storeFacePictures** | **Boolean**| Boolean value indicating whether you want the faces inside the picture to be stored for later retrieval | [optional] [default to true] |
| **storeResult** | **Boolean**| Boolean value indicating whether you want the result of the analysis to be stored | [optional] [default to true] |
| **retentionTime** | **Integer**| How many seconds the results should be retained in stoarage? | [optional] |
| **pictureURL** | **String**| The URL of the picture, assuming it is served by a third party server. Server should be accesible from the Internet or through another netwoek by VisageCloud infrastructure | [optional] |
| **algorithmVersion** | **String**| Algorithm version (V2 is more performant but not backward compatible) | [optional] [default to V2] [enum: V1, V2] |
| **autoRotate** | **Boolean**| Auto-rotate to find flipped or rotate faces | [optional] [default to false] |
| **skipEXIF** | **Boolean**| Skip EXIF rotation procesing | [optional] [default to false] |
| **waitForPictureUpload** | **Boolean**| Waits until the picture is successfully uploaded, before returning the response back the the client | [optional] [default to false] |
| **filters** | [**List&lt;String&gt;**](String.md)| [For advanced users only] Change feature filters for robustness of feature extraction. Tweaking this parameter may affect per | [optional] |
| **options** | **String**| [For advanced users only] Options for preprocessing of image. | [optional] |
| **picture** | **String**| The multipart/form-data version of the image, in case a direct upload is used. At least one of picture or pictureURL must be present | [optional] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="performRecognitionUsingPOST"></a>
# **performRecognitionUsingPOST**
> RestResponse performRecognitionUsingPOST(accessKey, secretKey, collectionId, storeAnalysisPicture, storeFacePictures, storeResult, retentionTime, labels, attributeFilters, pictureURL, algorithmVersion, autoRotate, skipEXIFRotationProcessing, waitForPictureUpload, filters, options, picture)

Perform labeled recognition on a given picture or picture URL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
    Boolean storeAnalysisPicture = true; // Boolean | Boolean value indicating whether you want the picture of the analysis to be stored for later retrieval
    Boolean storeFacePictures = true; // Boolean | Boolean value indicating whether you want the faces inside the picture to be stored for later retrieval
    Boolean storeResult = true; // Boolean | Boolean value indicating whether you want the result of the analysis to be stored
    Integer retentionTime = 56; // Integer | How many seconds the results should be retained in stoarage?
    List<String> labels = Arrays.asList(); // List<String> | Labels associated with the given picture or picture URL
    List<String> attributeFilters = Arrays.asList(); // List<String> | Filters that will be applied on the recognition operation
    String pictureURL = "pictureURL_example"; // String | The URL of the picture
    String algorithmVersion = "V1"; // String | Algorithm version (V2 is more performant but not backward compatible)
    Boolean autoRotate = false; // Boolean | Auto-rotate to find flipped or rotate faces
    Boolean skipEXIFRotationProcessing = false; // Boolean | Skip EXIF rotation procesing
    Boolean waitForPictureUpload = false; // Boolean | Waits until the picture is successfully uploaded, before returning the response back the the client
    List<String> filters = Arrays.asList(); // List<String> | [For advanced users only] Change feature filters for robustness of feature extraction. Tweaking this parameter may affect per
    String options = "options_example"; // String | [For advanced users only] Options for preprocessing of image.
    String picture = "picture_example"; // String | The picture itself
    try {
      RestResponse result = apiInstance.performRecognitionUsingPOST(accessKey, secretKey, collectionId, storeAnalysisPicture, storeFacePictures, storeResult, retentionTime, labels, attributeFilters, pictureURL, algorithmVersion, autoRotate, skipEXIFRotationProcessing, waitForPictureUpload, filters, options, picture);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#performRecognitionUsingPOST");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | |
| **storeAnalysisPicture** | **Boolean**| Boolean value indicating whether you want the picture of the analysis to be stored for later retrieval | [optional] [default to true] |
| **storeFacePictures** | **Boolean**| Boolean value indicating whether you want the faces inside the picture to be stored for later retrieval | [optional] [default to true] |
| **storeResult** | **Boolean**| Boolean value indicating whether you want the result of the analysis to be stored | [optional] [default to true] |
| **retentionTime** | **Integer**| How many seconds the results should be retained in stoarage? | [optional] |
| **labels** | [**List&lt;String&gt;**](String.md)| Labels associated with the given picture or picture URL | [optional] |
| **attributeFilters** | [**List&lt;String&gt;**](String.md)| Filters that will be applied on the recognition operation | [optional] [enum: NO_FILTER, GENDER_FILTER, AGE_GROUP_FILTER] |
| **pictureURL** | **String**| The URL of the picture | [optional] |
| **algorithmVersion** | **String**| Algorithm version (V2 is more performant but not backward compatible) | [optional] [default to V2] [enum: V1, V2] |
| **autoRotate** | **Boolean**| Auto-rotate to find flipped or rotate faces | [optional] [default to false] |
| **skipEXIFRotationProcessing** | **Boolean**| Skip EXIF rotation procesing | [optional] [default to false] |
| **waitForPictureUpload** | **Boolean**| Waits until the picture is successfully uploaded, before returning the response back the the client | [optional] [default to false] |
| **filters** | [**List&lt;String&gt;**](String.md)| [For advanced users only] Change feature filters for robustness of feature extraction. Tweaking this parameter may affect per | [optional] |
| **options** | **String**| [For advanced users only] Options for preprocessing of image. | [optional] |
| **picture** | **String**| The picture itself | [optional] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="retrieveAnalysisUsingGET"></a>
# **retrieveAnalysisUsingGET**
> RestResponse retrieveAnalysisUsingGET(accessKey, secretKey, analysisId)

Retrieve a complete analysis object including both detection and recognition information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String analysisId = "analysisId_example"; // String | The ID of the analysis for which the data will be retrieved
    try {
      RestResponse result = apiInstance.retrieveAnalysisUsingGET(accessKey, secretKey, analysisId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#retrieveAnalysisUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **analysisId** | **String**| The ID of the analysis for which the data will be retrieved | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="retriveLatestUsingGET"></a>
# **retriveLatestUsingGET**
> RestResponse retriveLatestUsingGET(accessKey, secretKey, count)

Retrieve the last *count* operations per current account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalysisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AnalysisApi apiInstance = new AnalysisApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    Integer count = 100; // Integer | How many records to retrieve at a time
    try {
      RestResponse result = apiInstance.retriveLatestUsingGET(accessKey, secretKey, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalysisApi#retriveLatestUsingGET");
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
| **accessKey** | **String**| The accessKey provided by VisageCloud | |
| **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | |
| **count** | **Integer**| How many records to retrieve at a time | [optional] [default to 100] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

