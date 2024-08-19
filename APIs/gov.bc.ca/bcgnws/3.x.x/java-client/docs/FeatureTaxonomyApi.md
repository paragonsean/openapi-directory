# FeatureTaxonomyApi

All URIs are relative to *https://apps.gov.bc.ca/pub/bcgnws*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**featureCategoriesGet**](FeatureTaxonomyApi.md#featureCategoriesGet) | **GET** /featureCategories | Get all feature categories |
| [**featureClassesGet**](FeatureTaxonomyApi.md#featureClassesGet) | **GET** /featureClasses | Get all feature classes |
| [**featureTypesGet**](FeatureTaxonomyApi.md#featureTypesGet) | **GET** /featureTypes | Get all feature types |


<a id="featureCategoriesGet"></a>
# **featureCategoriesGet**
> featureCategoriesGet(outputFormat)

Get all feature categories

Gets a list of all feature categories used by the BC Geographical Names Information System (BCGNIS).  Note: there are three levels of classification in the BCGNIS feature taxonomy: classes, categories and types.  A type is a subset of a category, and a category is a subset of a class.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureTaxonomyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    FeatureTaxonomyApi apiInstance = new FeatureTaxonomyApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    try {
      apiInstance.featureCategoriesGet(outputFormat);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureTaxonomyApi#featureCategoriesGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml] |

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
| **200** | A list of feature categories |  -  |

<a id="featureClassesGet"></a>
# **featureClassesGet**
> featureClassesGet(outputFormat)

Get all feature classes

Gets a list of all feature classes used by the BC Geographical Names Information System (BCGNIS).  Note: there are three levels of classification in the BCGNIS feature taxonomy: classes, categories and types.  A type is a subset of a category, and a category is a subset of a class.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureTaxonomyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    FeatureTaxonomyApi apiInstance = new FeatureTaxonomyApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    try {
      apiInstance.featureClassesGet(outputFormat);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureTaxonomyApi#featureClassesGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml] |

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
| **200** | A list of feature classes |  -  |

<a id="featureTypesGet"></a>
# **featureTypesGet**
> featureTypesGet(outputFormat)

Get all feature types

Gets a list of all feature types used by the BC Geographical Names Information System (BCGNIS).  Note: there are three levels of classification in the BCGNIS feature taxonomy: classes, categories and types.  A type is a subset of a category, and a category is a subset of a class.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureTaxonomyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apps.gov.bc.ca/pub/bcgnws");

    FeatureTaxonomyApi apiInstance = new FeatureTaxonomyApi(defaultClient);
    String outputFormat = "json"; // String | The format of the output.
    try {
      apiInstance.featureTypesGet(outputFormat);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureTaxonomyApi#featureTypesGet");
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
| **outputFormat** | **String**| The format of the output. | [default to json] [enum: json, xml] |

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
| **200** | A list of feature types |  -  |

