# OrganisationsRolesApi

All URIs are relative to *http://api.abr.ato.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**organisationsPartyIdRolesGet**](OrganisationsRolesApi.md#organisationsPartyIdRolesGet) | **GET** /organisations/{partyId}/roles | Retrieve a list of roles |
| [**organisationsPartyIdRolesPost**](OrganisationsRolesApi.md#organisationsPartyIdRolesPost) | **POST** /organisations/{partyId}/roles | Create a role |
| [**organisationsPartyIdRolesRoleIdDelete**](OrganisationsRolesApi.md#organisationsPartyIdRolesRoleIdDelete) | **DELETE** /organisations/{partyId}/roles/{roleId} | Delete a role |
| [**organisationsPartyIdRolesRoleIdGet**](OrganisationsRolesApi.md#organisationsPartyIdRolesRoleIdGet) | **GET** /organisations/{partyId}/roles/{roleId} | Retrieve a role |
| [**organisationsPartyIdRolesRoleIdPut**](OrganisationsRolesApi.md#organisationsPartyIdRolesRoleIdPut) | **PUT** /organisations/{partyId}/roles/{roleId} | Update a role |


<a id="organisationsPartyIdRolesGet"></a>
# **organisationsPartyIdRolesGet**
> List&lt;PartyRole&gt; organisationsPartyIdRolesGet(apiKey, partyId)

Retrieve a list of roles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsRolesApi apiInstance = new OrganisationsRolesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    try {
      List<PartyRole> result = apiInstance.organisationsPartyIdRolesGet(apiKey, partyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsRolesApi#organisationsPartyIdRolesGet");
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
| **apiKey** | **String**| The API key. | |
| **partyId** | **String**| The party identifier. | |

### Return type

[**List&lt;PartyRole&gt;**](PartyRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Roles were retrieved successfully |  * Link - Information about pagination is provided in the [Link](https://tools.ietf.org/html/rfc5988#page-6) header. For example:      Link: &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;2&gt;; rel&#x3D;\&quot;next\&quot;,           &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;34&gt;; rel&#x3D;\&quot;last\&quot;  &#x60;rel&#x3D;\&quot;next\&quot;&#x60; states that the next page is &#x60;page&#x3D;2&#x60;. This makes sense, since by default, all paginated queries start at page &#x60;1&#x60;. &#x60;rel&#x3D;\&quot;last\&quot;&#x60; provides some more information, stating that the last page of results is on &#x60;page 34&#x60;. Accordingly, we have 33 more pages of information that we can consume.  <br>  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="organisationsPartyIdRolesPost"></a>
# **organisationsPartyIdRolesPost**
> PartyRole organisationsPartyIdRolesPost(apiKey, partyId, partyRole)

Create a role

Create a role 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsRolesApi apiInstance = new OrganisationsRolesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    PartyRole partyRole = new PartyRole(); // PartyRole | Role resource
    try {
      PartyRole result = apiInstance.organisationsPartyIdRolesPost(apiKey, partyId, partyRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsRolesApi#organisationsPartyIdRolesPost");
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
| **apiKey** | **String**| The API key. | |
| **partyId** | **String**| The party identifier. | |
| **partyRole** | [**PartyRole**](PartyRole.md)| Role resource | |

### Return type

[**PartyRole**](PartyRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Role was created |  * Location - A [Location](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.30) header pointing to the location of the new resource.  <br>  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |

<a id="organisationsPartyIdRolesRoleIdDelete"></a>
# **organisationsPartyIdRolesRoleIdDelete**
> organisationsPartyIdRolesRoleIdDelete(apiKey, partyId, roleId)

Delete a role

Delete a role 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsRolesApi apiInstance = new OrganisationsRolesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String roleId = "roleId_example"; // String | The role identifier.
    try {
      apiInstance.organisationsPartyIdRolesRoleIdDelete(apiKey, partyId, roleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsRolesApi#organisationsPartyIdRolesRoleIdDelete");
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
| **apiKey** | **String**| The API key. | |
| **partyId** | **String**| The party identifier. | |
| **roleId** | **String**| The role identifier. | |

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
| **204** | Role was deleted |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="organisationsPartyIdRolesRoleIdGet"></a>
# **organisationsPartyIdRolesRoleIdGet**
> PartyRole organisationsPartyIdRolesRoleIdGet(apiKey, partyId, roleId)

Retrieve a role

Retrieve a role 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsRolesApi apiInstance = new OrganisationsRolesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String roleId = "roleId_example"; // String | The role identifier.
    try {
      PartyRole result = apiInstance.organisationsPartyIdRolesRoleIdGet(apiKey, partyId, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsRolesApi#organisationsPartyIdRolesRoleIdGet");
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
| **apiKey** | **String**| The API key. | |
| **partyId** | **String**| The party identifier. | |
| **roleId** | **String**| The role identifier. | |

### Return type

[**PartyRole**](PartyRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role was retrieved successfully |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

<a id="organisationsPartyIdRolesRoleIdPut"></a>
# **organisationsPartyIdRolesRoleIdPut**
> PartyRole organisationsPartyIdRolesRoleIdPut(apiKey, partyId, roleId, partyRole)

Update a role

Update a role 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganisationsRolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    OrganisationsRolesApi apiInstance = new OrganisationsRolesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    String partyId = "partyId_example"; // String | The party identifier.
    String roleId = "roleId_example"; // String | The role identifier.
    PartyRole partyRole = new PartyRole(); // PartyRole | Role resource
    try {
      PartyRole result = apiInstance.organisationsPartyIdRolesRoleIdPut(apiKey, partyId, roleId, partyRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganisationsRolesApi#organisationsPartyIdRolesRoleIdPut");
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
| **apiKey** | **String**| The API key. | |
| **partyId** | **String**| The party identifier. | |
| **roleId** | **String**| The role identifier. | |
| **partyRole** | [**PartyRole**](PartyRole.md)| Role resource | |

### Return type

[**PartyRole**](PartyRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role was updated |  -  |
| **400** | The client specified an invalid argument |  -  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

