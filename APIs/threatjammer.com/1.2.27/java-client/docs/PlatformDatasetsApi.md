# PlatformDatasetsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**queryDatatasetInformationOfAllTheResourceTypesV1DatasetIpGet**](PlatformDatasetsApi.md#queryDatatasetInformationOfAllTheResourceTypesV1DatasetIpGet) | **GET** /v1/dataset/ip | Get the list of all the datasets available in the platform. |
| [**queryDatatasetInformationOfTheResourceTypeV1DatasetIpNameGet**](PlatformDatasetsApi.md#queryDatatasetInformationOfTheResourceTypeV1DatasetIpNameGet) | **GET** /v1/dataset/ip/{name} | Get the detailed information of the dataset queried. |


<a id="queryDatatasetInformationOfAllTheResourceTypesV1DatasetIpGet"></a>
# **queryDatatasetInformationOfAllTheResourceTypesV1DatasetIpGet**
> DatasetTypeCollectionOutput queryDatatasetInformationOfAllTheResourceTypesV1DatasetIpGet()

Get the list of all the datasets available in the platform.

### What Obtain the list of all the datasets available in the platform. A dataset is a collection of different data sources that are related to a specific topic. The name of the dataset describes the specific topic.  ### Parameters No parameters are required.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;types&#x60;&#x60;: a list of JSON objects with the following fields:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual dataset information.     - &#x60;&#x60;type&#x60;&#x60;: what type of dataset is this. The only allowed value is &#x60;&#x60;ip&#x60;&#x60;.     - &#x60;&#x60;name&#x60;&#x60;: the name of the dataset in human readable form.     - &#x60;&#x60;description&#x60;&#x60;: a human readable long description of the dataset.     - &#x60;&#x60;status&#x60;&#x60;: the status of the dataset. The only allowed value is &#x60;&#x60;ENABLED&#x60;&#x60;.     - &#x60;&#x60;items&#x60;&#x60;: the number of &#39;live&#39; items in the dataset when the request is performed.  ### Errors It will return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    PlatformDatasetsApi apiInstance = new PlatformDatasetsApi(defaultClient);
    try {
      DatasetTypeCollectionOutput result = apiInstance.queryDatatasetInformationOfAllTheResourceTypesV1DatasetIpGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformDatasetsApi#queryDatatasetInformationOfAllTheResourceTypesV1DatasetIpGet");
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

[**DatasetTypeCollectionOutput**](DatasetTypeCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="queryDatatasetInformationOfTheResourceTypeV1DatasetIpNameGet"></a>
# **queryDatatasetInformationOfTheResourceTypeV1DatasetIpNameGet**
> DatasetTypeOutput queryDatatasetInformationOfTheResourceTypeV1DatasetIpNameGet(name)

Get the detailed information of the dataset queried.

### What Get the detailed information of the dataset queried by the name. A dataset is a collection of different data sources that are related to a specific topic. The name of the dataset describes the specific topic.  ### Parameters The endpoint accepts only the following parameter in the path: - &#x60;&#x60;name&#x60;&#x60;: (Mandatory) The code name that identifies uniquely the dataset in the platform. It must be composed of uppercase letters, numbers and underscores.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual dataset information. - &#x60;&#x60;type&#x60;&#x60;: what type of dataset is this. The only allowed value is &#x60;&#x60;ip&#x60;&#x60;. - &#x60;&#x60;name&#x60;&#x60;: the name of the dataset in human readable form. - &#x60;&#x60;description&#x60;&#x60;: a human readable long description of the dataset. - &#x60;&#x60;status&#x60;&#x60;: the status of the dataset. The only allowed value is &#x60;&#x60;ENABLED&#x60;&#x60;. - &#x60;&#x60;items&#x60;&#x60;: the number of &#39;live&#39; items in the dataset when the request is performed.  ### Errors - a &#x60;404 Not Found&#x60; error if the dataset code name was not found. - a &#x60;422 Unprocessable Entity&#x60; error if dataset code name does not follow the naming convention.  It will also return the API Global errors described in the API description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformDatasetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    PlatformDatasetsApi apiInstance = new PlatformDatasetsApi(defaultClient);
    String name = "name_example"; // String | 
    try {
      DatasetTypeOutput result = apiInstance.queryDatatasetInformationOfTheResourceTypeV1DatasetIpNameGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformDatasetsApi#queryDatatasetInformationOfTheResourceTypeV1DatasetIpNameGet");
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
| **name** | **String**|  | |

### Return type

[**DatasetTypeOutput**](DatasetTypeOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

