# DefaultApi

All URIs are relative to *https://api.openalpr.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConfig**](DefaultApi.md#getConfig) | **GET** /config |  |
| [**recognizeBytes**](DefaultApi.md#recognizeBytes) | **POST** /recognize_bytes |  |
| [**recognizeFile**](DefaultApi.md#recognizeFile) | **POST** /recognize |  |
| [**recognizeUrl**](DefaultApi.md#recognizeUrl) | **POST** /recognize_url |  |


<a id="getConfig"></a>
# **getConfig**
> GetConfig200Response getConfig()



Get a list of available results for plate and vehicle recognition 

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
    defaultClient.setBasePath("https://api.openalpr.com/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      GetConfig200Response result = apiInstance.getConfig();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getConfig");
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

[**GetConfig200Response**](GetConfig200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok |  -  |

<a id="recognizeBytes"></a>
# **recognizeBytes**
> RecognizeFile200Response recognizeBytes(secretKey, country, imageBytes, recognizeVehicle, returnImage, topn)



Send an image for OpenALPR to analyze and provide metadata back The image is sent as base64 encoded bytes. 

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
    defaultClient.setBasePath("https://api.openalpr.com/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String secretKey = "secretKey_example"; // String | The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/ 
    String country = "country_example"; // String | Defines the training data used by OpenALPR.  \"us\" analyzes  North-American style plates.  \"eu\" analyzes European-style plates.  This field is required if using the \"plate\" task 
    String imageBytes = "imageBytes_example"; // String | The image file that you wish to analyze encoded in base64 
    Integer recognizeVehicle = 0; // Integer | If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request 
    Integer returnImage = 0; // Integer | If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response 
    Integer topn = 10; // Integer | The number of results you would like to be returned for plate  candidates and vehicle classifications 
    try {
      RecognizeFile200Response result = apiInstance.recognizeBytes(secretKey, country, imageBytes, recognizeVehicle, returnImage, topn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#recognizeBytes");
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
| **secretKey** | **String**| The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/  | |
| **country** | **String**| Defines the training data used by OpenALPR.  \&quot;us\&quot; analyzes  North-American style plates.  \&quot;eu\&quot; analyzes European-style plates.  This field is required if using the \&quot;plate\&quot; task  | |
| **imageBytes** | **String**| The image file that you wish to analyze encoded in base64  | |
| **recognizeVehicle** | **Integer**| If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request  | [optional] [default to 0] [enum: 0, 1] |
| **returnImage** | **Integer**| If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response  | [optional] [default to 0] [enum: 0, 1] |
| **topn** | **Integer**| The number of results you would like to be returned for plate  candidates and vehicle classifications  | [optional] [default to 10] |

### Return type

[**RecognizeFile200Response**](RecognizeFile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Ratelimit-Reset - Epoch time when the next period begins <br>  * X-Ratelimit-Remaining - Number of remaining requests allowed during this period <br>  * X-RateLimit-Limit - Maximum number of requests allowed from your IP in a period <br>  |
| **400** | Parameter is invalid |  -  |
| **401** | User not authorized or invalid secret_key |  -  |
| **402** | Monthly usage limit exceeded |  -  |
| **403** | Temporary rate-limit exceeded |  -  |

<a id="recognizeFile"></a>
# **recognizeFile**
> RecognizeFile200Response recognizeFile(secretKey, country, image, recognizeVehicle, returnImage, topn, isCropped)



Send an image for OpenALPR to analyze and provide metadata back The image is sent as a file using a form data POST 

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
    defaultClient.setBasePath("https://api.openalpr.com/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String secretKey = "secretKey_example"; // String | The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/ 
    String country = "country_example"; // String | Defines the training data used by OpenALPR.  \"us\" analyzes  North-American style plates.  \"eu\" analyzes European-style plates.  This field is required if using the \"plate\" task 
    File image = new File("/path/to/file"); // File | The image file that you wish to analyze 
    Integer recognizeVehicle = 0; // Integer | If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request 
    Integer returnImage = 0; // Integer | If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response 
    Integer topn = 10; // Integer | The number of results you would like to be returned for plate  candidates and vehicle classifications 
    Integer isCropped = 0; // Integer | When providing a plate or vehicle that is already cropped,   this performs a recognition against the full crop and does not  attempt to localize the plate/vehicle 
    try {
      RecognizeFile200Response result = apiInstance.recognizeFile(secretKey, country, image, recognizeVehicle, returnImage, topn, isCropped);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#recognizeFile");
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
| **secretKey** | **String**| The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/  | |
| **country** | **String**| Defines the training data used by OpenALPR.  \&quot;us\&quot; analyzes  North-American style plates.  \&quot;eu\&quot; analyzes European-style plates.  This field is required if using the \&quot;plate\&quot; task  | |
| **image** | **File**| The image file that you wish to analyze  | |
| **recognizeVehicle** | **Integer**| If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request  | [optional] [default to 0] [enum: 0, 1] |
| **returnImage** | **Integer**| If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response  | [optional] [default to 0] [enum: 0, 1] |
| **topn** | **Integer**| The number of results you would like to be returned for plate  candidates and vehicle classifications  | [optional] [default to 10] |
| **isCropped** | **Integer**| When providing a plate or vehicle that is already cropped,   this performs a recognition against the full crop and does not  attempt to localize the plate/vehicle  | [optional] [default to 0] [enum: 0, 1] |

### Return type

[**RecognizeFile200Response**](RecognizeFile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Ratelimit-Reset - Epoch time when the next period begins <br>  * X-Ratelimit-Remaining - Number of remaining requests allowed during this period <br>  * X-RateLimit-Limit - Maximum number of requests allowed from your IP in a period <br>  |
| **400** | Parameter is invalid |  -  |
| **401** | User not authorized or invalid secret_key |  -  |
| **402** | Monthly usage limit exceeded |  -  |
| **403** | Temporary rate-limit exceeded |  -  |

<a id="recognizeUrl"></a>
# **recognizeUrl**
> RecognizeFile200Response recognizeUrl(imageUrl, secretKey, country, recognizeVehicle, returnImage, topn)



Send an image for OpenALPR to analyze and provide metadata back The image is sent as a URL.  The OpenALPR service will download the image  and process it 

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
    defaultClient.setBasePath("https://api.openalpr.com/v3");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String imageUrl = "imageUrl_example"; // String | A URL to an image that you wish to analyze 
    String secretKey = "secretKey_example"; // String | The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/ 
    String country = "country_example"; // String | Defines the training data used by OpenALPR.  \"us\" analyzes  North-American style plates.  \"eu\" analyzes European-style plates.  This field is required if using the \"plate\" task 
    Integer recognizeVehicle = 0; // Integer | If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request 
    Integer returnImage = 0; // Integer | If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response 
    Integer topn = 10; // Integer | The number of results you would like to be returned for plate  candidates and vehicle classifications 
    try {
      RecognizeFile200Response result = apiInstance.recognizeUrl(imageUrl, secretKey, country, recognizeVehicle, returnImage, topn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#recognizeUrl");
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
| **imageUrl** | **String**| A URL to an image that you wish to analyze  | |
| **secretKey** | **String**| The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/  | |
| **country** | **String**| Defines the training data used by OpenALPR.  \&quot;us\&quot; analyzes  North-American style plates.  \&quot;eu\&quot; analyzes European-style plates.  This field is required if using the \&quot;plate\&quot; task  | |
| **recognizeVehicle** | **Integer**| If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request  | [optional] [default to 0] [enum: 0, 1] |
| **returnImage** | **Integer**| If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response  | [optional] [default to 0] [enum: 0, 1] |
| **topn** | **Integer**| The number of results you would like to be returned for plate  candidates and vehicle classifications  | [optional] [default to 10] |

### Return type

[**RecognizeFile200Response**](RecognizeFile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-Ratelimit-Reset - Epoch time when the next period begins <br>  * X-Ratelimit-Remaining - Number of remaining requests allowed during this period <br>  * X-RateLimit-Limit - Maximum number of requests allowed from your IP in a period <br>  |
| **400** | Parameter is invalid |  -  |
| **401** | User not authorized or invalid secret_key |  -  |
| **402** | Monthly usage limit exceeded |  -  |
| **403** | Temporary rate-limit exceeded |  -  |

