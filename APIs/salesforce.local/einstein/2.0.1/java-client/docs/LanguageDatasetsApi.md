# LanguageDatasetsApi

All URIs are relative to *http://salesforce.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDataset**](LanguageDatasetsApi.md#deleteDataset) | **DELETE** /v2/language/datasets/{datasetId} | Delete a Dataset |
| [**get**](LanguageDatasetsApi.md#get) | **GET** /v2/language/deletion/{id} | Get Deletion Status |
| [**getDataset**](LanguageDatasetsApi.md#getDataset) | **GET** /v2/language/datasets/{datasetId} | Get a Dataset |
| [**listDatasets**](LanguageDatasetsApi.md#listDatasets) | **GET** /v2/language/datasets | Get All Datasets |
| [**uploadDatasetAsync**](LanguageDatasetsApi.md#uploadDatasetAsync) | **POST** /v2/language/datasets/upload | Create a Dataset From a File Asynchronously |
| [**uploadDatasetSync**](LanguageDatasetsApi.md#uploadDatasetSync) | **POST** /v2/language/datasets/upload/sync | Create a Dataset From a File Synchronously |


<a id="deleteDataset"></a>
# **deleteDataset**
> DeletionResponse deleteDataset(datasetId)

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
import org.openapitools.client.api.LanguageDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageDatasetsApi apiInstance = new LanguageDatasetsApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    try {
      DeletionResponse result = apiInstance.deleteDataset(datasetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageDatasetsApi#deleteDataset");
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
| **200** | Success |  -  |

<a id="get"></a>
# **get**
> DeletionResponse get(id)

Get Deletion Status

Returns the status of a language dataset or model deletion. When you delete a dataset or model, the deletion may not occur immediately. Use this call to find out when the deletion is complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageDatasetsApi apiInstance = new LanguageDatasetsApi(defaultClient);
    String id = "Z2JTFBF3A7XKIJC5QEJXMO4HSY"; // String | Deletion Id
    try {
      DeletionResponse result = apiInstance.get(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageDatasetsApi#get");
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

<a id="getDataset"></a>
# **getDataset**
> Dataset getDataset(datasetId)

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
import org.openapitools.client.api.LanguageDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageDatasetsApi apiInstance = new LanguageDatasetsApi(defaultClient);
    String datasetId = "SomeDatasetId"; // String | Dataset Id
    try {
      Dataset result = apiInstance.getDataset(datasetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageDatasetsApi#getDataset");
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

<a id="listDatasets"></a>
# **listDatasets**
> DatasetList listDatasets(offset, count, global)

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
import org.openapitools.client.api.LanguageDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageDatasetsApi apiInstance = new LanguageDatasetsApi(defaultClient);
    String offset = "0"; // String | Index of the dataset from which you want to start paging
    String count = "25"; // String | Number of datsets to return. Maximum valid value is 25. If you specify a number greater than 25, the call returns 25 datasets.
    Boolean global = false; // Boolean | If true, returns all global datasets. Global datasets are public datasets that Salesforce provides.
    try {
      DatasetList result = apiInstance.listDatasets(offset, count, global);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageDatasetsApi#listDatasets");
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

<a id="uploadDatasetAsync"></a>
# **uploadDatasetAsync**
> Dataset uploadDatasetAsync(data, name, path, type)

Create a Dataset From a File Asynchronously

Creates a dataset, labels, and examples from the specified .csv, .tsv, or .json file. The call returns immediately and continues to upload data in the background.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageDatasetsApi apiInstance = new LanguageDatasetsApi(defaultClient);
    String data = "data_example"; // String | Path to the .csv, .tsv, or .json file on the local drive (FilePart).
    String name = "name_example"; // String | Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the file name.
    String path = "path_example"; // String | URL of the .csv, .tsv, or .json file.
    String type = "text-intent"; // String | Type of dataset data.
    try {
      Dataset result = apiInstance.uploadDatasetAsync(data, name, path, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageDatasetsApi#uploadDatasetAsync");
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
| **data** | **String**| Path to the .csv, .tsv, or .json file on the local drive (FilePart). | [optional] |
| **name** | **String**| Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the file name. | [optional] |
| **path** | **String**| URL of the .csv, .tsv, or .json file. | [optional] |
| **type** | **String**| Type of dataset data. | [optional] [enum: text-intent, text-sentiment] |

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

<a id="uploadDatasetSync"></a>
# **uploadDatasetSync**
> Dataset uploadDatasetSync(data, name, path, type)

Create a Dataset From a File Synchronously

Creates a dataset, labels, and examples from the specified .csv, .tsv, or .json file. The call returns after the dataset is created and all of the data is uploaded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LanguageDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://salesforce.local");
    
    // Configure HTTP bearer authorization: bearer_token
    HttpBearerAuth bearer_token = (HttpBearerAuth) defaultClient.getAuthentication("bearer_token");
    bearer_token.setBearerToken("BEARER TOKEN");

    LanguageDatasetsApi apiInstance = new LanguageDatasetsApi(defaultClient);
    String data = "data_example"; // String | Path to the .csv, .tsv, or .json file on the local drive (FilePart).
    String name = "name_example"; // String | Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the file name.
    String path = "path_example"; // String | URL of the .csv, .tsv, or .json file.
    String type = "text-intent"; // String | Type of dataset data.
    try {
      Dataset result = apiInstance.uploadDatasetSync(data, name, path, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LanguageDatasetsApi#uploadDatasetSync");
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
| **data** | **String**| Path to the .csv, .tsv, or .json file on the local drive (FilePart). | [optional] |
| **name** | **String**| Name of the dataset. Optional. If this parameter is omitted, the dataset name is derived from the file name. | [optional] |
| **path** | **String**| URL of the .csv, .tsv, or .json file. | [optional] |
| **type** | **String**| Type of dataset data. | [optional] [enum: text-intent, text-sentiment] |

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

