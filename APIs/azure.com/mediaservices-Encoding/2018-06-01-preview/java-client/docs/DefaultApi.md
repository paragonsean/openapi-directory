# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobsCancelJob**](DefaultApi.md#jobsCancelJob) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName}/cancelJob | Cancel Job |
| [**jobsCreate**](DefaultApi.md#jobsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName} | Create Job |
| [**jobsDelete**](DefaultApi.md#jobsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName} | Delete Job |
| [**jobsGet**](DefaultApi.md#jobsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs/{jobName} | Get Job |
| [**jobsList**](DefaultApi.md#jobsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName}/jobs | List Jobs |
| [**transformsCreateOrUpdate**](DefaultApi.md#transformsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName} | Create or Update Transform |
| [**transformsDelete**](DefaultApi.md#transformsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName} | Delete Transform |
| [**transformsGet**](DefaultApi.md#transformsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName} | Get Transform |
| [**transformsList**](DefaultApi.md#transformsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms | List Transforms |
| [**transformsUpdate**](DefaultApi.md#transformsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/transforms/{transformName} | Update Transform |


<a id="jobsCancelJob"></a>
# **jobsCancelJob**
> jobsCancelJob(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion)

Cancel Job

Cancel a Job.

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
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String transformName = "transformName_example"; // String | The Transform name.
    String jobName = "jobName_example"; // String | The Job name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.jobsCancelJob(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsCancelJob");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **transformName** | **String**| The Transform name. | |
| **jobName** | **String**| The Job name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="jobsCreate"></a>
# **jobsCreate**
> Job jobsCreate(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion, parameters)

Create Job

Creates a Job.

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
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String transformName = "transformName_example"; // String | The Transform name.
    String jobName = "jobName_example"; // String | The Job name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    Job parameters = new Job(); // Job | The request parameters
    try {
      Job result = apiInstance.jobsCreate(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsCreate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **transformName** | **String**| The Transform name. | |
| **jobName** | **String**| The Job name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**Job**](Job.md)| The request parameters | |

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | Detailed error information. |  -  |

<a id="jobsDelete"></a>
# **jobsDelete**
> jobsDelete(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion)

Delete Job

Deletes a Job.

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
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String transformName = "transformName_example"; // String | The Transform name.
    String jobName = "jobName_example"; // String | The Job name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.jobsDelete(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsDelete");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **transformName** | **String**| The Transform name. | |
| **jobName** | **String**| The Job name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |
| **0** | Detailed error information. |  -  |

<a id="jobsGet"></a>
# **jobsGet**
> Job jobsGet(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion)

Get Job

Gets a Job.

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
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String transformName = "transformName_example"; // String | The Transform name.
    String jobName = "jobName_example"; // String | The Job name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      Job result = apiInstance.jobsGet(subscriptionId, resourceGroupName, accountName, transformName, jobName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsGet");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **transformName** | **String**| The Transform name. | |
| **jobName** | **String**| The Job name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NotFound |  -  |
| **0** | Detailed error information. |  -  |

<a id="jobsList"></a>
# **jobsList**
> JobCollection jobsList(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, $filter, $top, $skip)

List Jobs

Lists all of the Jobs for the Transform.

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
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String transformName = "transformName_example"; // String | The Transform name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Restricts the set of items returned.
    Integer $top = 56; // Integer | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    Integer $skip = 56; // Integer | Specifies a non-negative integer n that excludes the first n items of the queried collection from the result. The service returns items starting at position n+1.
    try {
      JobCollection result = apiInstance.jobsList(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobsList");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **transformName** | **String**| The Transform name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **$filter** | **String**| Restricts the set of items returned. | [optional] |
| **$top** | **Integer**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] |
| **$skip** | **Integer**| Specifies a non-negative integer n that excludes the first n items of the queried collection from the result. The service returns items starting at position n+1. | [optional] |

### Return type

[**JobCollection**](JobCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="transformsCreateOrUpdate"></a>
# **transformsCreateOrUpdate**
> Transform transformsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, parameters)

Create or Update Transform

Creates or updates a new Transform.

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
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String transformName = "transformName_example"; // String | The Transform name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    Transform parameters = new Transform(); // Transform | The request parameters
    try {
      Transform result = apiInstance.transformsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#transformsCreateOrUpdate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **transformName** | **String**| The Transform name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**Transform**](Transform.md)| The request parameters | |

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Detailed error information. |  -  |

<a id="transformsDelete"></a>
# **transformsDelete**
> transformsDelete(subscriptionId, resourceGroupName, accountName, transformName, apiVersion)

Delete Transform

Deletes a Transform.

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
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String transformName = "transformName_example"; // String | The Transform name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      apiInstance.transformsDelete(subscriptionId, resourceGroupName, accountName, transformName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#transformsDelete");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **transformName** | **String**| The Transform name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | NoContent |  -  |
| **0** | Detailed error information. |  -  |

<a id="transformsGet"></a>
# **transformsGet**
> Transform transformsGet(subscriptionId, resourceGroupName, accountName, transformName, apiVersion)

Get Transform

Gets a Transform.

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
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String transformName = "transformName_example"; // String | The Transform name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    try {
      Transform result = apiInstance.transformsGet(subscriptionId, resourceGroupName, accountName, transformName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#transformsGet");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **transformName** | **String**| The Transform name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | NotFound |  -  |
| **0** | Detailed error information. |  -  |

<a id="transformsList"></a>
# **transformsList**
> TransformCollection transformsList(subscriptionId, resourceGroupName, accountName, apiVersion, $filter, $top, $skip)

List Transforms

Lists the Transforms in the account.

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
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | Restricts the set of items returned.
    Integer $top = 56; // Integer | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    Integer $skip = 56; // Integer | Specifies a non-negative integer n that excludes the first n items of the queried collection from the result. The service returns items starting at position n+1.
    try {
      TransformCollection result = apiInstance.transformsList(subscriptionId, resourceGroupName, accountName, apiVersion, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#transformsList");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **$filter** | **String**| Restricts the set of items returned. | [optional] |
| **$top** | **Integer**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] |
| **$skip** | **Integer**| Specifies a non-negative integer n that excludes the first n items of the queried collection from the result. The service returns items starting at position n+1. | [optional] |

### Return type

[**TransformCollection**](TransformCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

<a id="transformsUpdate"></a>
# **transformsUpdate**
> Transform transformsUpdate(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, parameters)

Update Transform

Updates a Transform.

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
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
    String accountName = "accountName_example"; // String | The Media Services account name.
    String transformName = "transformName_example"; // String | The Transform name.
    String apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
    Transform parameters = new Transform(); // Transform | The request parameters
    try {
      Transform result = apiInstance.transformsUpdate(subscriptionId, resourceGroupName, accountName, transformName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#transformsUpdate");
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
| **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | |
| **accountName** | **String**| The Media Services account name. | |
| **transformName** | **String**| The Transform name. | |
| **apiVersion** | **String**| The Version of the API to be used with the client request. | |
| **parameters** | [**Transform**](Transform.md)| The request parameters | |

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Detailed error information. |  -  |

