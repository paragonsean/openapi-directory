# VisionExamplesApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addExample**](VisionExamplesApi.md#addExample) | **POST** /v2/vision/datasets/{datasetId}/examples | Create an Example |
| [**getExamples1**](VisionExamplesApi.md#getExamples1) | **GET** /v2/vision/datasets/{datasetId}/examples | Get All Examples |
| [**getExamplesByLabel1**](VisionExamplesApi.md#getExamplesByLabel1) | **GET** /v2/vision/examples | Get All Examples for Label |
| [**provideFeedback1**](VisionExamplesApi.md#provideFeedback1) | **POST** /v2/vision/feedback | Create a Feedback Example |
| [**updateDatasetAsync1**](VisionExamplesApi.md#updateDatasetAsync1) | **PUT** /v2/vision/bulkfeedback | Create Feedback Examples From a Zip File |
| [**updateDatasetAsync2**](VisionExamplesApi.md#updateDatasetAsync2) | **PUT** /v2/vision/datasets/{datasetId}/upload | Create Examples From a Zip File |


<a id="addExample"></a>
# **addExample**
> Example addExample(datasetId, data, labelId, name)

Create an Example

Adds an example with the specified label to a dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionExamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionExamplesApi apiInstance = new VisionExamplesApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    String data = "data_example"; // String | Location of the local image file to upload.
    Long labelId = 56L; // Long | ID of the label to add to the example.
    String name = "name_example"; // String | Name of the example. Maximum length is 180 characters.
    try {
      Example result = apiInstance.addExample(datasetId, data, labelId, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionExamplesApi#addExample");
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
| **datasetId** | **String**| Dataset Id | |
| **data** | **String**| Location of the local image file to upload. | [optional] |
| **labelId** | **Long**| ID of the label to add to the example. | [optional] |
| **name** | **String**| Name of the example. Maximum length is 180 characters. | [optional] |

### Return type

[**Example**](Example.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Example created |  -  |

<a id="getExamples1"></a>
# **getExamples1**
> ExampleList getExamples1(datasetId, offset, count, source)

Get All Examples

Returns all the examples for the specified dataset. By default, returns examples created by uploading them from a .zip file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionExamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionExamplesApi apiInstance = new VisionExamplesApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    String offset = "0"; // String | Index of the example from which you want to start paging.
    String count = "100"; // String | Number of examples to return.
    String source = "all"; // String | return examples that were created in the dataset as feedback
    try {
      ExampleList result = apiInstance.getExamples1(datasetId, offset, count, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionExamplesApi#getExamples1");
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
| **datasetId** | **String**| Dataset Id | |
| **offset** | **String**| Index of the example from which you want to start paging. | [optional] [default to 0] |
| **count** | **String**| Number of examples to return. | [optional] [default to 100] |
| **source** | **String**| return examples that were created in the dataset as feedback | [optional] [enum: all, feedback, upload] |

### Return type

[**ExampleList**](ExampleList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getExamplesByLabel1"></a>
# **getExamplesByLabel1**
> ExampleList getExamplesByLabel1(labelId, offset, count)

Get All Examples for Label

Returns all the examples for the specified label. Returns both uploaded examples and feedback examples.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionExamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionExamplesApi apiInstance = new VisionExamplesApi(defaultClient);
    String labelId = "SomeLabelId"; // String | Label Id
    String offset = "0"; // String | Index of the example from which you want to start paging.
    String count = "100"; // String | Number of examples to return.
    try {
      ExampleList result = apiInstance.getExamplesByLabel1(labelId, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionExamplesApi#getExamplesByLabel1");
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
| **labelId** | **String**| Label Id | [optional] |
| **offset** | **String**| Index of the example from which you want to start paging. | [optional] [default to 0] |
| **count** | **String**| Number of examples to return. | [optional] [default to 100] |

### Return type

[**ExampleList**](ExampleList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="provideFeedback1"></a>
# **provideFeedback1**
> Example provideFeedback1(data, expectedLabel, modelId, name)

Create a Feedback Example

Adds a feedback example to the dataset associated with the specified model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionExamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionExamplesApi apiInstance = new VisionExamplesApi(defaultClient);
    String data = "data_example"; // String | Local image file to upload.
    String expectedLabel = "expectedLabel_example"; // String | Correct label for the example. Must be a label that exists in the dataset.
    String modelId = "modelId_example"; // String | ID of the model that misclassified the image. The feedback example is added to the dataset associated with this model.
    String name = "name_example"; // String | Name of the example. Optional. Maximum length is 180 characters.
    try {
      Example result = apiInstance.provideFeedback1(data, expectedLabel, modelId, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionExamplesApi#provideFeedback1");
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
| **data** | **String**| Local image file to upload. | [optional] |
| **expectedLabel** | **String**| Correct label for the example. Must be a label that exists in the dataset. | [optional] |
| **modelId** | **String**| ID of the model that misclassified the image. The feedback example is added to the dataset associated with this model. | [optional] |
| **name** | **String**| Name of the example. Optional. Maximum length is 180 characters. | [optional] |

### Return type

[**Example**](Example.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Upload success |  -  |

<a id="updateDatasetAsync1"></a>
# **updateDatasetAsync1**
> Dataset updateDatasetAsync1(data, modelId)

Create Feedback Examples From a Zip File

Adds feedback examples to the dataset associated with the specified object detection model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionExamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionExamplesApi apiInstance = new VisionExamplesApi(defaultClient);
    String data = "data_example"; // String | Local .zip file to upload. The maximum .zip file size you can upload from a local drive is 50 MB.
    String modelId = "modelId_example"; // String | ID of the model that misclassified the images. The feedback examples are added to the dataset associated with this model.
    try {
      Dataset result = apiInstance.updateDatasetAsync1(data, modelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionExamplesApi#updateDatasetAsync1");
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
| **data** | **String**| Local .zip file to upload. The maximum .zip file size you can upload from a local drive is 50 MB. | [optional] |
| **modelId** | **String**| ID of the model that misclassified the images. The feedback examples are added to the dataset associated with this model. | [optional] |

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update success |  -  |

<a id="updateDatasetAsync2"></a>
# **updateDatasetAsync2**
> Dataset updateDatasetAsync2(datasetId, data, path)

Create Examples From a Zip File

Adds examples from a .zip file to a dataset. You can use this call only with a dataset that was created from a .zip file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionExamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionExamplesApi apiInstance = new VisionExamplesApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    String data = "data_example"; // String | Location of the local image file to upload.
    String path = "path_example"; // String | URL of the .zip file.
    try {
      Dataset result = apiInstance.updateDatasetAsync2(datasetId, data, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionExamplesApi#updateDatasetAsync2");
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
| **datasetId** | **String**| Dataset Id | |
| **data** | **String**| Location of the local image file to upload. | [optional] |
| **path** | **String**| URL of the .zip file. | [optional] |

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Upload success |  -  |

