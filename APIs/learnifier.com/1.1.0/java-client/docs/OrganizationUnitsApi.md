# OrganizationUnitsApi

All URIs are relative to *http://learnifier.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extorgunitGet**](OrganizationUnitsApi.md#extorgunitGet) | **GET** /extorgunit | Get Organization Unit with External Id |
| [**orgunitsGet**](OrganizationUnitsApi.md#orgunitsGet) | **GET** /orgunits | Organization Units |
| [**orgunitsOrgidGet**](OrganizationUnitsApi.md#orgunitsOrgidGet) | **GET** /orgunits/{orgid} | Get Organization Unit |
| [**orgunitsOrgidPatch**](OrganizationUnitsApi.md#orgunitsOrgidPatch) | **PATCH** /orgunits/{orgid} | Updates an Organization Unit |
| [**orgunitsPost**](OrganizationUnitsApi.md#orgunitsPost) | **POST** /orgunits | Adds an Organization Unit |


<a id="extorgunitGet"></a>
# **extorgunitGet**
> OrgUnit extorgunitGet(extid)

Get Organization Unit with External Id

Returns information about the organization unit with the specified external id. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationUnitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    OrganizationUnitsApi apiInstance = new OrganizationUnitsApi(defaultClient);
    String extid = "extid_example"; // String | The external id of the organization unit
    try {
      OrgUnit result = apiInstance.extorgunitGet(extid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationUnitsApi#extorgunitGet");
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
| **extid** | **String**| The external id of the organization unit | |

### Return type

[**OrgUnit**](OrgUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response with an organization unit |  -  |
| **404** | Organization Unit not found |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsGet"></a>
# **orgunitsGet**
> OrgUnits orgunitsGet()

Organization Units

The orgunits endpoint returns information about the available organization units (orgunits). The response includes the display name, internal and external id and client number. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationUnitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    OrganizationUnitsApi apiInstance = new OrganizationUnitsApi(defaultClient);
    try {
      OrgUnits result = apiInstance.orgunitsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationUnitsApi#orgunitsGet");
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

[**OrgUnits**](OrgUnits.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response with organization units |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidGet"></a>
# **orgunitsOrgidGet**
> OrgUnit orgunitsOrgidGet(orgid)

Get Organization Unit

Returns information about the specified organization unit. The response includes the display name, internal and external id and client number. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationUnitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    OrganizationUnitsApi apiInstance = new OrganizationUnitsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    try {
      OrgUnit result = apiInstance.orgunitsOrgidGet(orgid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationUnitsApi#orgunitsOrgidGet");
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
| **orgid** | **Integer**| Id of the organization unit | |

### Return type

[**OrgUnit**](OrgUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response with an organization unit |  -  |
| **404** | Organization Unit not found |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidPatch"></a>
# **orgunitsOrgidPatch**
> orgunitsOrgidPatch(orgid, body)

Updates an Organization Unit

Adds an Organization Unit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationUnitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    OrganizationUnitsApi apiInstance = new OrganizationUnitsApi(defaultClient);
    String orgid = "orgid_example"; // String | 
    UpdateOrganizationUnit body = new UpdateOrganizationUnit(); // UpdateOrganizationUnit | 
    try {
      apiInstance.orgunitsOrgidPatch(orgid, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationUnitsApi#orgunitsOrgidPatch");
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
| **orgid** | **String**|  | |
| **body** | [**UpdateOrganizationUnit**](UpdateOrganizationUnit.md)|  | |

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
| **201** | Organization Unit was successfully updated |  -  |
| **409** | An organization with the same clientNumber or external id already existed. |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsPost"></a>
# **orgunitsPost**
> AddOrganizationUnitResponse orgunitsPost(body)

Adds an Organization Unit

Adds an Organization Unit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationUnitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    OrganizationUnitsApi apiInstance = new OrganizationUnitsApi(defaultClient);
    AddOrganizationUnit body = new AddOrganizationUnit(); // AddOrganizationUnit | 
    try {
      AddOrganizationUnitResponse result = apiInstance.orgunitsPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationUnitsApi#orgunitsPost");
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
| **body** | [**AddOrganizationUnit**](AddOrganizationUnit.md)|  | |

### Return type

[**AddOrganizationUnitResponse**](AddOrganizationUnitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization Unit was successfully added |  -  |
| **409** | An organization with the same clientNumber or external id already existed. |  -  |
| **0** | Unexpected error |  -  |

