# ImportsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOperation**](ImportsApi.md#createOperation) | **POST** /imports/images | Begin the import of an image analyzed by Syft into the system |
| [**getOperation**](ImportsApi.md#getOperation) | **GET** /imports/images/{operation_id} | Get detail on a single import |
| [**importImageConfig**](ImportsApi.md#importImageConfig) | **POST** /imports/images/{operation_id}/image_config | Import a docker or OCI image config to associate with the image |
| [**importImageDockerfile**](ImportsApi.md#importImageDockerfile) | **POST** /imports/images/{operation_id}/dockerfile | Begin the import of an image analyzed by Syft into the system |
| [**importImageManifest**](ImportsApi.md#importImageManifest) | **POST** /imports/images/{operation_id}/manifest | Import a docker or OCI distribution manifest to associate with the image |
| [**importImagePackages**](ImportsApi.md#importImagePackages) | **POST** /imports/images/{operation_id}/packages | Begin the import of an image analyzed by Syft into the system |
| [**importImageParentManifest**](ImportsApi.md#importImageParentManifest) | **POST** /imports/images/{operation_id}/parent_manifest | Import a docker or OCI distribution manifest list to associate with the image |
| [**invalidateOperation**](ImportsApi.md#invalidateOperation) | **DELETE** /imports/images/{operation_id} | Invalidate operation ID so it can be garbage collected |
| [**listImportDockerfiles**](ImportsApi.md#listImportDockerfiles) | **GET** /imports/images/{operation_id}/dockerfile | List uploaded dockerfiles |
| [**listImportImageConfigs**](ImportsApi.md#listImportImageConfigs) | **GET** /imports/images/{operation_id}/image_config | List uploaded image configs |
| [**listImportImageManifests**](ImportsApi.md#listImportImageManifests) | **GET** /imports/images/{operation_id}/manifest | List uploaded image manifests |
| [**listImportPackages**](ImportsApi.md#listImportPackages) | **GET** /imports/images/{operation_id}/packages | List uploaded package manifests |
| [**listImportParentManifests**](ImportsApi.md#listImportParentManifests) | **GET** /imports/images/{operation_id}/parent_manifest | List uploaded parent manifests (manifest lists for a tag) |
| [**listOperations**](ImportsApi.md#listOperations) | **GET** /imports/images | Lists in-progress imports |


<a id="createOperation"></a>
# **createOperation**
> ImageImportOperation createOperation()

Begin the import of an image analyzed by Syft into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    try {
      ImageImportOperation result = apiInstance.createOperation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#createOperation");
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

[**ImageImportOperation**](ImageImportOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="getOperation"></a>
# **getOperation**
> ImageImportOperation getOperation(operationId)

Get detail on a single import

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    try {
      ImageImportOperation result = apiInstance.getOperation(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#getOperation");
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
| **operationId** | **String**|  | |

### Return type

[**ImageImportOperation**](ImageImportOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="importImageConfig"></a>
# **importImageConfig**
> ImageImportContentResponse importImageConfig(operationId, body)

Import a docker or OCI image config to associate with the image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    Object body = null; // Object | 
    try {
      ImageImportContentResponse result = apiInstance.importImageConfig(operationId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#importImageConfig");
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
| **operationId** | **String**|  | |
| **body** | **Object**|  | |

### Return type

[**ImageImportContentResponse**](ImageImportContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="importImageDockerfile"></a>
# **importImageDockerfile**
> ImageImportContentResponse importImageDockerfile(operationId, body)

Begin the import of an image analyzed by Syft into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    String body = "body_example"; // String | 
    try {
      ImageImportContentResponse result = apiInstance.importImageDockerfile(operationId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#importImageDockerfile");
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
| **operationId** | **String**|  | |
| **body** | **String**|  | |

### Return type

[**ImageImportContentResponse**](ImageImportContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain; utf-8
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="importImageManifest"></a>
# **importImageManifest**
> ImageImportContentResponse importImageManifest(operationId, body)

Import a docker or OCI distribution manifest to associate with the image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    Object body = null; // Object | 
    try {
      ImageImportContentResponse result = apiInstance.importImageManifest(operationId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#importImageManifest");
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
| **operationId** | **String**|  | |
| **body** | **Object**|  | |

### Return type

[**ImageImportContentResponse**](ImageImportContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.docker.distribution.manifest.v1+json, application/vnd.docker.distribution.manifest.v1+prettyjws, application/vnd.docker.distribution.manifest.v2+json, application/vnd.oci.image.manifest.v1+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="importImagePackages"></a>
# **importImagePackages**
> ImageImportContentResponse importImagePackages(operationId, imagePackageManifest)

Begin the import of an image analyzed by Syft into the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    ImagePackageManifest imagePackageManifest = new ImagePackageManifest(); // ImagePackageManifest | 
    try {
      ImageImportContentResponse result = apiInstance.importImagePackages(operationId, imagePackageManifest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#importImagePackages");
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
| **operationId** | **String**|  | |
| **imagePackageManifest** | [**ImagePackageManifest**](ImagePackageManifest.md)|  | |

### Return type

[**ImageImportContentResponse**](ImageImportContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="importImageParentManifest"></a>
# **importImageParentManifest**
> ImageImportContentResponse importImageParentManifest(operationId, body)

Import a docker or OCI distribution manifest list to associate with the image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    Object body = null; // Object | 
    try {
      ImageImportContentResponse result = apiInstance.importImageParentManifest(operationId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#importImageParentManifest");
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
| **operationId** | **String**|  | |
| **body** | **Object**|  | |

### Return type

[**ImageImportContentResponse**](ImageImportContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.docker.distribution.manifest.list.v2+json, application/vnd.oci.image.index.v1+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="invalidateOperation"></a>
# **invalidateOperation**
> ImageImportOperation invalidateOperation(operationId)

Invalidate operation ID so it can be garbage collected

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    try {
      ImageImportOperation result = apiInstance.invalidateOperation(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#invalidateOperation");
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
| **operationId** | **String**|  | |

### Return type

[**ImageImportOperation**](ImageImportOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="listImportDockerfiles"></a>
# **listImportDockerfiles**
> List&lt;String&gt; listImportDockerfiles(operationId)

List uploaded dockerfiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    try {
      List<String> result = apiInstance.listImportDockerfiles(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#listImportDockerfiles");
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
| **operationId** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="listImportImageConfigs"></a>
# **listImportImageConfigs**
> List&lt;String&gt; listImportImageConfigs(operationId)

List uploaded image configs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    try {
      List<String> result = apiInstance.listImportImageConfigs(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#listImportImageConfigs");
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
| **operationId** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="listImportImageManifests"></a>
# **listImportImageManifests**
> List&lt;String&gt; listImportImageManifests(operationId)

List uploaded image manifests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    try {
      List<String> result = apiInstance.listImportImageManifests(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#listImportImageManifests");
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
| **operationId** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="listImportPackages"></a>
# **listImportPackages**
> List&lt;String&gt; listImportPackages(operationId)

List uploaded package manifests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    try {
      List<String> result = apiInstance.listImportPackages(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#listImportPackages");
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
| **operationId** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="listImportParentManifests"></a>
# **listImportParentManifests**
> List&lt;String&gt; listImportParentManifests(operationId)

List uploaded parent manifests (manifest lists for a tag)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String operationId = "operationId_example"; // String | 
    try {
      List<String> result = apiInstance.listImportParentManifests(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#listImportParentManifests");
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
| **operationId** | **String**|  | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

<a id="listOperations"></a>
# **listOperations**
> List&lt;ImageImportOperation&gt; listOperations()

Lists in-progress imports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    try {
      List<ImageImportOperation> result = apiInstance.listOperations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#listOperations");
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

[**List&lt;ImageImportOperation&gt;**](ImageImportOperation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |
| **500** | Internal Error |  -  |

