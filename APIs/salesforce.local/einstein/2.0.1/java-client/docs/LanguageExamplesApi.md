# LanguageExamplesApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getExamples**](LanguageExamplesApi.md#getExamples) | **GET** /v2/language/datasets/{datasetId}/examples | Get All Examples |
| [**getExamplesByLabel**](LanguageExamplesApi.md#getExamplesByLabel) | **GET** /v2/language/examples | Get All Examples for Label |
| [**provideFeedback**](LanguageExamplesApi.md#provideFeedback) | **POST** /v2/language/feedback | Create a Feedback Example |
| [**updateDatasetAsync**](LanguageExamplesApi.md#updateDatasetAsync) | **PUT** /v2/language/datasets/{datasetId}/upload | Create Examples From a File |


<a id="getExamples"></a>
# **getExamples**
> ExampleList getExamples(datasetId, offset, count, source)

Get All Examples

Returns all the examples for the specified dataset,

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageExamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageExamplesApi apiInstance = new LanguageExamplesApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    String offset = "0"; // String | Index of the example from which you want to start paging.
    String count = "100"; // String | Number of examples to return.
    String source = "all"; // String | return examples that were created in the dataset as feedback
    try {
      ExampleList result = apiInstance.getExamples(datasetId, offset, count, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageExamplesApi#getExamples");
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

<a id="getExamplesByLabel"></a>
# **getExamplesByLabel**
> ExampleList getExamplesByLabel(labelId, offset, count)

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
import org.openapitools.client.api.LanguageExamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageExamplesApi apiInstance = new LanguageExamplesApi(defaultClient);
    String labelId = "SomeLabelId"; // String | Label Id
    String offset = "0"; // String | Index of the example from which you want to start paging.
    String count = "100"; // String | Number of examples to return.
    try {
      ExampleList result = apiInstance.getExamplesByLabel(labelId, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageExamplesApi#getExamplesByLabel");
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

<a id="provideFeedback"></a>
# **provideFeedback**
> Example provideFeedback(document, expectedLabel, modelId, name)

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
import org.openapitools.client.api.LanguageExamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageExamplesApi apiInstance = new LanguageExamplesApi(defaultClient);
    String document = "document_example"; // String | Intent or sentiment string to add to the dataset.
    String expectedLabel = "expectedLabel_example"; // String | Correct label for the example. Must be a label that exists in the dataset.
    String modelId = "modelId_example"; // String | ID of the model that misclassified the image. The feedback example is added to the dataset associated with this model.
    String name = "name_example"; // String | Name of the example. Optional. Maximum length is 180 characters.
    try {
      Example result = apiInstance.provideFeedback(document, expectedLabel, modelId, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageExamplesApi#provideFeedback");
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
| **document** | **String**| Intent or sentiment string to add to the dataset. | [optional] |
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

<a id="updateDatasetAsync"></a>
# **updateDatasetAsync**
> Dataset updateDatasetAsync(datasetId, data, type)

Create Examples From a File

Adds examples from a .csv, .tsv, or .json file to a dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageExamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageExamplesApi apiInstance = new LanguageExamplesApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    String data = "data_example"; // String | Path to the .csv, .tsv, or .json file on a local drive. 
    String type = "type_example"; // String | URL of the .csv, .tsv, or .json file.
    try {
      Dataset result = apiInstance.updateDatasetAsync(datasetId, data, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageExamplesApi#updateDatasetAsync");
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
| **data** | **String**| Path to the .csv, .tsv, or .json file on a local drive.  | [optional] |
| **type** | **String**| URL of the .csv, .tsv, or .json file. | [optional] |

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

