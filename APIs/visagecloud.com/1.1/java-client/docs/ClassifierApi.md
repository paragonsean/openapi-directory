# ClassifierApi

All URIs are relative to *https://visagecloud.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSVMClassifierUsingPOST**](ClassifierApi.md#addSVMClassifierUsingPOST) | **POST** /rest/v1.1/classifier/svm | Create new SVM classifier with given name |
| [**getClassiferFullUsingGET**](ClassifierApi.md#getClassiferFullUsingGET) | **GET** /rest/v1.1/classifier/svm | Get classifier full |
| [**getClassiferStatusUsingGET**](ClassifierApi.md#getClassiferStatusUsingGET) | **GET** /rest/v1.1/classifier/svm/status | Get classifer status |
| [**removeClassiferUsingDELETE**](ClassifierApi.md#removeClassiferUsingDELETE) | **DELETE** /rest/v1.1/classifier/svm | Delete existing classifier |


<a id="addSVMClassifierUsingPOST"></a>
# **addSVMClassifierUsingPOST**
> RestResponse addSVMClassifierUsingPOST(accessKey, secretKey, name, collectionIds, classificationAttributeName, preprocessor, considerViewPoints, seed, trainingRatio, probabilityParameter, gammaParameter, nuParameter, cParameter, svmTypeParameter, kernelTypeParameter, cacheSizeParameter, epsParameter)

Create new SVM classifier with given name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassifierApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ClassifierApi apiInstance = new ClassifierApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String name = "name_example"; // String | The name of the SVM classifier that will be created
    List<String> collectionIds = Arrays.asList(); // List<String> | Collection ids
    String classificationAttributeName = "classificationAttributeName_example"; // String | Classification attribute name
    String preprocessor = "FeaturePreprocessor"; // String | Preprocessor
    Boolean considerViewPoints = false; // Boolean | Consider view point
    Integer seed = 179425537; // Integer | Seed for divididing training and evaluation sets
    Double trainingRatio = 0.8D; // Double | Training ratio
    Integer probabilityParameter = 1; // Integer | Probability parameter
    Double gammaParameter = 0.5D; // Double | Gamma parameter
    Double nuParameter = 0.25D; // Double | Nu parameter
    Double cParameter = 1.0D; // Double | c parameter
    Integer svmTypeParameter = 0; // Integer | SVM type parameter
    Integer kernelTypeParameter = 0; // Integer | Kernel type parameter
    Double cacheSizeParameter = 500.0D; // Double | Cache size parameter
    Double epsParameter = 0.001D; // Double | Eps parameter
    try {
      RestResponse result = apiInstance.addSVMClassifierUsingPOST(accessKey, secretKey, name, collectionIds, classificationAttributeName, preprocessor, considerViewPoints, seed, trainingRatio, probabilityParameter, gammaParameter, nuParameter, cParameter, svmTypeParameter, kernelTypeParameter, cacheSizeParameter, epsParameter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassifierApi#addSVMClassifierUsingPOST");
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
| **name** | **String**| The name of the SVM classifier that will be created | |
| **collectionIds** | [**List&lt;String&gt;**](String.md)| Collection ids | |
| **classificationAttributeName** | **String**| Classification attribute name | |
| **preprocessor** | **String**| Preprocessor | [optional] [default to FeaturePreprocessor] |
| **considerViewPoints** | **Boolean**| Consider view point | [optional] [default to false] |
| **seed** | **Integer**| Seed for divididing training and evaluation sets | [optional] [default to 179425537] |
| **trainingRatio** | **Double**| Training ratio | [optional] [default to 0.8] |
| **probabilityParameter** | **Integer**| Probability parameter | [optional] [default to 1] |
| **gammaParameter** | **Double**| Gamma parameter | [optional] [default to 0.5] |
| **nuParameter** | **Double**| Nu parameter | [optional] [default to 0.25] |
| **cParameter** | **Double**| c parameter | [optional] [default to 1.0] |
| **svmTypeParameter** | **Integer**| SVM type parameter | [optional] [default to 0] |
| **kernelTypeParameter** | **Integer**| Kernel type parameter | [optional] [default to 0] |
| **cacheSizeParameter** | **Double**| Cache size parameter | [optional] [default to 500.0] |
| **epsParameter** | **Double**| Eps parameter | [optional] [default to 0.001] |

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
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getClassiferFullUsingGET"></a>
# **getClassiferFullUsingGET**
> RestResponse getClassiferFullUsingGET(accessKey, secretKey, id)

Get classifier full

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassifierApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ClassifierApi apiInstance = new ClassifierApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String id = "id_example"; // String | The id of the classifier that you want the status for
    try {
      RestResponse result = apiInstance.getClassiferFullUsingGET(accessKey, secretKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassifierApi#getClassiferFullUsingGET");
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
| **id** | **String**| The id of the classifier that you want the status for | |

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

<a id="getClassiferStatusUsingGET"></a>
# **getClassiferStatusUsingGET**
> RestResponse getClassiferStatusUsingGET(accessKey, secretKey, id)

Get classifer status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassifierApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ClassifierApi apiInstance = new ClassifierApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String id = "id_example"; // String | The id of the classifier that you want the status for
    try {
      RestResponse result = apiInstance.getClassiferStatusUsingGET(accessKey, secretKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassifierApi#getClassiferStatusUsingGET");
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
| **id** | **String**| The id of the classifier that you want the status for | |

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

<a id="removeClassiferUsingDELETE"></a>
# **removeClassiferUsingDELETE**
> RestResponse removeClassiferUsingDELETE(accessKey, secretKey, id)

Delete existing classifier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClassifierApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    ClassifierApi apiInstance = new ClassifierApi(defaultClient);
    String accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
    String secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
    String id = "id_example"; // String | The id of the classifier that will be removed
    try {
      RestResponse result = apiInstance.removeClassiferUsingDELETE(accessKey, secretKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClassifierApi#removeClassiferUsingDELETE");
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
| **id** | **String**| The id of the classifier that will be removed | |

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
| **204** | No Content |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

