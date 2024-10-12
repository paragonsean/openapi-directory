# SpecApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProductTypeListOfWorkgroup**](SpecApi.md#getProductTypeListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/productTypes | Get product type of workgroup level |
| [**getSpec**](SpecApi.md#getSpec) | **GET** /1.1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id} | List a specific spec of project Level |
| [**getSpecList**](SpecApi.md#getSpecList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/specs | List specs of project Level |
| [**getSpecProductTypeListOfWorkgroup**](SpecApi.md#getSpecProductTypeListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/productTypesOfSpecTypes | Get product type of spec level by workgroupId |
| [**getSpecTypeFields**](SpecApi.md#getSpecTypeFields) | **GET** /1.1/workgroups/{workgroup_id}/specTypes/{spec_type_id}/specTypeFields | Get Spec Type Fields |
| [**postSpec**](SpecApi.md#postSpec) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/specs | Create a Spec |
| [**postSpecProductTypeListOfWorkgroup**](SpecApi.md#postSpecProductTypeListOfWorkgroup) | **POST** /v1/workgroups/{workgroup_id}/productTypesOfSpecTypes | Register product types for spec types |
| [**putSpec**](SpecApi.md#putSpec) | **PUT** /1.1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id} | Update a specific Spec |
| [**v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet**](SpecApi.md#v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id} | List a specific spec of project Level |
| [**v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut**](SpecApi.md#v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id} | Update a specific Spec |
| [**v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet**](SpecApi.md#v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet) | **GET** /v1/workgroups/{workgroup_id}/specTypes/{spec_type_id}/specTypeFields | Get Spec Type Fields |


<a id="getProductTypeListOfWorkgroup"></a>
# **getProductTypeListOfWorkgroup**
> WorkgroupAttributeListVO getProductTypeListOfWorkgroup(workgroupId)

Get product type of workgroup level

Get product type of workgroup level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      WorkgroupAttributeListVO result = apiInstance.getProductTypeListOfWorkgroup(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#getProductTypeListOfWorkgroup");
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
| **workgroupId** | **String**|  | |

### Return type

[**WorkgroupAttributeListVO**](WorkgroupAttributeListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getSpec"></a>
# **getSpec**
> V1x1SpecExpandVO getSpec(workgroupId, projectId, specId)

List a specific spec of project Level

List a specific spec of project Level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String specId = "specId_example"; // String | 
    try {
      V1x1SpecExpandVO result = apiInstance.getSpec(workgroupId, projectId, specId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#getSpec");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **specId** | **String**|  | |

### Return type

[**V1x1SpecExpandVO**](V1x1SpecExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getSpecList"></a>
# **getSpecList**
> SpecListVO getSpecList(workgroupId, projectId)

List specs of project Level

List specs of project Level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    try {
      SpecListVO result = apiInstance.getSpecList(workgroupId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#getSpecList");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |

### Return type

[**SpecListVO**](SpecListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getSpecProductTypeListOfWorkgroup"></a>
# **getSpecProductTypeListOfWorkgroup**
> WorkgroupAttributeListVO getSpecProductTypeListOfWorkgroup(workgroupId)

Get product type of spec level by workgroupId

Get product type of spec level by workgroupId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      WorkgroupAttributeListVO result = apiInstance.getSpecProductTypeListOfWorkgroup(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#getSpecProductTypeListOfWorkgroup");
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
| **workgroupId** | **String**|  | |

### Return type

[**WorkgroupAttributeListVO**](WorkgroupAttributeListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getSpecTypeFields"></a>
# **getSpecTypeFields**
> SpecTypeFieldsListVO getSpecTypeFields(workgroupId, specTypeId)

Get Spec Type Fields

Get Spec Type Fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String specTypeId = "specTypeId_example"; // String | 
    try {
      SpecTypeFieldsListVO result = apiInstance.getSpecTypeFields(workgroupId, specTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#getSpecTypeFields");
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
| **workgroupId** | **String**|  | |
| **specTypeId** | **String**|  | |

### Return type

[**SpecTypeFieldsListVO**](SpecTypeFieldsListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="postSpec"></a>
# **postSpec**
> SpecVO postSpec(workgroupId, projectId, specPersistVO)

Create a Spec

Create a Spec

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    SpecPersistVO specPersistVO = new SpecPersistVO(); // SpecPersistVO | 
    try {
      SpecVO result = apiInstance.postSpec(workgroupId, projectId, specPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#postSpec");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **specPersistVO** | [**SpecPersistVO**](SpecPersistVO.md)|  | [optional] |

### Return type

[**SpecVO**](SpecVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful created |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

<a id="postSpecProductTypeListOfWorkgroup"></a>
# **postSpecProductTypeListOfWorkgroup**
> WgSpecPrdTypeRegPersistVO postSpecProductTypeListOfWorkgroup(workgroupId, wgSpecPrdTypeRegPersistVO)

Register product types for spec types

Register product types for spec types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    WgSpecPrdTypeRegPersistVO wgSpecPrdTypeRegPersistVO = new WgSpecPrdTypeRegPersistVO(); // WgSpecPrdTypeRegPersistVO | 
    try {
      WgSpecPrdTypeRegPersistVO result = apiInstance.postSpecProductTypeListOfWorkgroup(workgroupId, wgSpecPrdTypeRegPersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#postSpecProductTypeListOfWorkgroup");
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
| **workgroupId** | **String**|  | |
| **wgSpecPrdTypeRegPersistVO** | [**WgSpecPrdTypeRegPersistVO**](WgSpecPrdTypeRegPersistVO.md)|  | [optional] |

### Return type

[**WgSpecPrdTypeRegPersistVO**](WgSpecPrdTypeRegPersistVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful created |  -  |
| **422** | Invalid data |  -  |
| **500** | Internal server error |  -  |

<a id="putSpec"></a>
# **putSpec**
> SpecHTTPStatusVO putSpec(workgroupId, projectId, specId, v1X1SpecUpdatingPO)

Update a specific Spec

Update a specific Spec

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String specId = "specId_example"; // String | 
    V1X1SpecUpdatingPO v1X1SpecUpdatingPO = new V1X1SpecUpdatingPO(); // V1X1SpecUpdatingPO | 
    try {
      SpecHTTPStatusVO result = apiInstance.putSpec(workgroupId, projectId, specId, v1X1SpecUpdatingPO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#putSpec");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **specId** | **String**|  | |
| **v1X1SpecUpdatingPO** | [**V1X1SpecUpdatingPO**](V1X1SpecUpdatingPO.md)|  | [optional] |

### Return type

[**SpecHTTPStatusVO**](SpecHTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful updated |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet"></a>
# **v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet**
> SpecListVO v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet(workgroupId, projectId, specId)

List a specific spec of project Level

List a specific spec of project Level

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String specId = "specId_example"; // String | 
    try {
      SpecListVO result = apiInstance.v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet(workgroupId, projectId, specId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **specId** | **String**|  | |

### Return type

[**SpecListVO**](SpecListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut"></a>
# **v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut**
> SpecHTTPStatusVO v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut(workgroupId, projectId, specId, specUpdatePersistVO)

Update a specific Spec

Update a specific Spec

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String projectId = "projectId_example"; // String | 
    String specId = "specId_example"; // String | 
    SpecUpdatePersistVO specUpdatePersistVO = new SpecUpdatePersistVO(); // SpecUpdatePersistVO | 
    try {
      SpecHTTPStatusVO result = apiInstance.v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut(workgroupId, projectId, specId, specUpdatePersistVO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut");
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
| **workgroupId** | **String**|  | |
| **projectId** | **String**|  | |
| **specId** | **String**|  | |
| **specUpdatePersistVO** | [**SpecUpdatePersistVO**](SpecUpdatePersistVO.md)|  | [optional] |

### Return type

[**SpecHTTPStatusVO**](SpecHTTPStatusVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful updated |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet"></a>
# **v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet**
> PropertyParamListVO v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet(workgroupId, specTypeId)

Get Spec Type Fields

Get Spec Type Fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    SpecApi apiInstance = new SpecApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String specTypeId = "specTypeId_example"; // String | 
    try {
      PropertyParamListVO result = apiInstance.v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet(workgroupId, specTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecApi#v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet");
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
| **workgroupId** | **String**|  | |
| **specTypeId** | **String**|  | |

### Return type

[**PropertyParamListVO**](PropertyParamListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

