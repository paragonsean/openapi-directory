# VisionDatasetsApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDataset**](VisionDatasetsApi.md#createDataset) | **POST** /v2/vision/datasets | Create a Dataset |
| [**deleteDataset1**](VisionDatasetsApi.md#deleteDataset1) | **DELETE** /v2/vision/datasets/{datasetId} | Delete a Dataset |
| [**get1**](VisionDatasetsApi.md#get1) | **GET** /v2/vision/deletion/{id} | Get Deletion Status |
| [**getDataset1**](VisionDatasetsApi.md#getDataset1) | **GET** /v2/vision/datasets/{datasetId} | Get a Dataset |
| [**listDatasets1**](VisionDatasetsApi.md#listDatasets1) | **GET** /v2/vision/datasets | Get All Datasets |
| [**uploadDatasetAsync1**](VisionDatasetsApi.md#uploadDatasetAsync1) | **POST** /v2/vision/datasets/upload | Create a Dataset From a Zip File Asynchronously |
| [**uploadDatasetSync1**](VisionDatasetsApi.md#uploadDatasetSync1) | **POST** /v2/vision/datasets/upload/sync | Create a Dataset From a Zip File Synchronously |


<a id="createDataset"></a>
# **createDataset**
> Dataset createDataset(labels, name, type)

Create a Dataset

Creates a dataset and labels, if they&#39;re specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionDatasetsApi apiInstance = new VisionDatasetsApi(defaultClient);
    String labels = "labels_example"; // String | Optional comma-separated list of labels. If specified, creates the labels in the dataset. Maximum number of labels per dataset is 250.
    String name = "name_example"; // String | Name of the dataset. Maximum length is 180 characters.
    String type = "image"; // String | Type of dataset data
    try {
      Dataset result = apiInstance.createDataset(labels, name, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionDatasetsApi#createDataset");
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
| **labels** | **String**| Optional comma-separated list of labels. If specified, creates the labels in the dataset. Maximum number of labels per dataset is 250. | [optional] |
| **name** | **String**| Name of the dataset. Maximum length is 180 characters. | [optional] |
| **type** | **String**| Type of dataset data | [optional] [enum: image, image-multi-label] |

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
| **200** | Creation success |  -  |

<a id="deleteDataset1"></a>
# **deleteDataset1**
> DeletionResponse deleteDataset1(datasetId)

Delete a Dataset

Deletes the specified dataset and associated labels and examples.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionDatasetsApi apiInstance = new VisionDatasetsApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    try {
      DeletionResponse result = apiInstance.deleteDataset1(datasetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionDatasetsApi#deleteDataset1");
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

### Return type

[**DeletionResponse**](DeletionResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |

<a id="get1"></a>
# **get1**
> DeletionResponse get1(id)

Get Deletion Status

Returns the status of an image dataset or model deletion. When you delete a dataset or model, the deletion may not occur immediately. Use this call to find out when the deletion is complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionDatasetsApi apiInstance = new VisionDatasetsApi(defaultClient);
    String id = "Z2JTFBF3A7XKIJC5QEJXMO4HSY"; // String | Deletion Id
    try {
      DeletionResponse result = apiInstance.get1(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionDatasetsApi#get1");
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
| **id** | **String**| Deletion Id | |

### Return type

[**DeletionResponse**](DeletionResponse.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | deletion status |  -  |

<a id="getDataset1"></a>
# **getDataset1**
> Dataset getDataset1(datasetId)

Get a Dataset

Returns a single dataset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionDatasetsApi apiInstance = new VisionDatasetsApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    try {
      Dataset result = apiInstance.getDataset1(datasetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionDatasetsApi#getDataset1");
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

### Return type

[**Dataset**](Dataset.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listDatasets1"></a>
# **listDatasets1**
> DatasetList listDatasets1(offset, count, global)

Get All Datasets

Returns a list of datasets and their labels that were created by the current user. The response is sorted by dataset ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionDatasetsApi apiInstance = new VisionDatasetsApi(defaultClient);
    String offset = "0"; // String | Index of the dataset from which you want to start paging
    String count = "25"; // String | Number of datsets to return. Maximum valid value is 25. If you specify a number greater than 25, the call returns 25 datasets.
    Boolean global = false; // Boolean | If true, returns all global datasets. Global datasets are public datasets that Salesforce provides.
    try {
      DatasetList result = apiInstance.listDatasets1(offset, count, global);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionDatasetsApi#listDatasets1");
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
| **offset** | **String**| Index of the dataset from which you want to start paging | [optional] [default to 0] |
| **count** | **String**| Number of datsets to return. Maximum valid value is 25. If you specify a number greater than 25, the call returns 25 datasets. | [optional] [default to 25] |
| **global** | **Boolean**| If true, returns all global datasets. Global datasets are public datasets that Salesforce provides. | [optional] [default to false] |

### Return type

[**DatasetList**](DatasetList.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="uploadDatasetAsync1"></a>
# **uploadDatasetAsync1**
> Dataset uploadDatasetAsync1(data, name, path, type)

Create a Dataset From a Zip File Asynchronously

Creates a dataset, labels, and examples from the specified .zip file. The call returns immediately and continues to upload the images in the background.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionDatasetsApi apiInstance = new VisionDatasetsApi(defaultClient);
    String data = "data_example"; // String | Path to the .zip file on the local drive (FilePart).
    String name = "name_example"; // String | Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the .zip file name.
    String path = "path_example"; // String | URL of the .zip file.
    String type = "image"; // String | Type of dataset data.
    try {
      Dataset result = apiInstance.uploadDatasetAsync1(data, name, path, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionDatasetsApi#uploadDatasetAsync1");
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
| **data** | **String**| Path to the .zip file on the local drive (FilePart). | [optional] |
| **name** | **String**| Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the .zip file name. | [optional] |
| **path** | **String**| URL of the .zip file. | [optional] |
| **type** | **String**| Type of dataset data. | [optional] [enum: image, image-detection, image-multi-label] |

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
| **200** | Upload initiated |  -  |

<a id="uploadDatasetSync1"></a>
# **uploadDatasetSync1**
> Dataset uploadDatasetSync1(data, name, path, type)

Create a Dataset From a Zip File Synchronously

Creates a dataset, labels, and examples from the specified .zip file. The call returns after the dataset is created and all of the images are uploaded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VisionDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    VisionDatasetsApi apiInstance = new VisionDatasetsApi(defaultClient);
    String data = "data_example"; // String | Path to the .zip file on the local drive (FilePart).
    String name = "name_example"; // String | Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the .zip file name.
    String path = "path_example"; // String | URL of the .zip file.
    String type = "image"; // String | Type of dataset data.
    try {
      Dataset result = apiInstance.uploadDatasetSync1(data, name, path, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VisionDatasetsApi#uploadDatasetSync1");
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
| **data** | **String**| Path to the .zip file on the local drive (FilePart). | [optional] |
| **name** | **String**| Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the .zip file name. | [optional] |
| **path** | **String**| URL of the .zip file. | [optional] |
| **type** | **String**| Type of dataset data. | [optional] [enum: image, image-detection, image-multi-label] |

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

