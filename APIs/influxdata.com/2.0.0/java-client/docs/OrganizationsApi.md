# OrganizationsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteOrgsID**](OrganizationsApi.md#deleteOrgsID) | **DELETE** /orgs/{orgID} | Delete an organization |
| [**deleteOrgsIDMembersID**](OrganizationsApi.md#deleteOrgsIDMembersID) | **DELETE** /orgs/{orgID}/members/{userID} | Remove a member from an organization |
| [**deleteOrgsIDOwnersID**](OrganizationsApi.md#deleteOrgsIDOwnersID) | **DELETE** /orgs/{orgID}/owners/{userID} | Remove an owner from an organization |
| [**getOrgs**](OrganizationsApi.md#getOrgs) | **GET** /orgs | List all organizations |
| [**getOrgsID**](OrganizationsApi.md#getOrgsID) | **GET** /orgs/{orgID} | Retrieve an organization |
| [**getOrgsIDMembers**](OrganizationsApi.md#getOrgsIDMembers) | **GET** /orgs/{orgID}/members | List all members of an organization |
| [**getOrgsIDOwners**](OrganizationsApi.md#getOrgsIDOwners) | **GET** /orgs/{orgID}/owners | List all owners of an organization |
| [**getOrgsIDSecrets_0**](OrganizationsApi.md#getOrgsIDSecrets_0) | **GET** /orgs/{orgID}/secrets | List all secret keys for an organization |
| [**patchOrgsID**](OrganizationsApi.md#patchOrgsID) | **PATCH** /orgs/{orgID} | Update an organization |
| [**patchOrgsIDSecrets_0**](OrganizationsApi.md#patchOrgsIDSecrets_0) | **PATCH** /orgs/{orgID}/secrets | Update secrets in an organization |
| [**postOrgs**](OrganizationsApi.md#postOrgs) | **POST** /orgs | Create an organization |
| [**postOrgsIDMembers**](OrganizationsApi.md#postOrgsIDMembers) | **POST** /orgs/{orgID}/members | Add a member to an organization |
| [**postOrgsIDOwners**](OrganizationsApi.md#postOrgsIDOwners) | **POST** /orgs/{orgID}/owners | Add an owner to an organization |
| [**postOrgsIDSecrets_0**](OrganizationsApi.md#postOrgsIDSecrets_0) | **POST** /orgs/{orgID}/secrets/delete | Delete secrets from an organization |


<a id="deleteOrgsID"></a>
# **deleteOrgsID**
> deleteOrgsID(orgID, zapTraceSpan)

Delete an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgID = "orgID_example"; // String | The ID of the organization to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteOrgsID(orgID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#deleteOrgsID");
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
| **orgID** | **String**| The ID of the organization to delete. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

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
| **204** | Delete has been accepted |  -  |
| **404** | Organization not found |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteOrgsIDMembersID"></a>
# **deleteOrgsIDMembersID**
> deleteOrgsIDMembersID(userID, orgID, zapTraceSpan)

Remove a member from an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String userID = "userID_example"; // String | The ID of the member to remove.
    String orgID = "orgID_example"; // String | The organization ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteOrgsIDMembersID(userID, orgID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#deleteOrgsIDMembersID");
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
| **userID** | **String**| The ID of the member to remove. | |
| **orgID** | **String**| The organization ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

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
| **204** | Member removed |  -  |
| **0** | Unexpected error |  -  |

<a id="deleteOrgsIDOwnersID"></a>
# **deleteOrgsIDOwnersID**
> deleteOrgsIDOwnersID(userID, orgID, zapTraceSpan)

Remove an owner from an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String userID = "userID_example"; // String | The ID of the owner to remove.
    String orgID = "orgID_example"; // String | The organization ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteOrgsIDOwnersID(userID, orgID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#deleteOrgsIDOwnersID");
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
| **userID** | **String**| The ID of the owner to remove. | |
| **orgID** | **String**| The organization ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

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
| **204** | Owner removed |  -  |
| **0** | Unexpected error |  -  |

<a id="getOrgs"></a>
# **getOrgs**
> Organizations getOrgs(zapTraceSpan, offset, limit, descending, org, orgID, userID)

List all organizations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    Integer offset = 56; // Integer | 
    Integer limit = 20; // Integer | 
    Boolean descending = false; // Boolean | 
    String org = "org_example"; // String | Filter organizations to a specific organization name.
    String orgID = "orgID_example"; // String | Filter organizations to a specific organization ID.
    String userID = "userID_example"; // String | Filter organizations to a specific user ID.
    try {
      Organizations result = apiInstance.getOrgs(zapTraceSpan, offset, limit, descending, org, orgID, userID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#getOrgs");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **offset** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **descending** | **Boolean**|  | [optional] [default to false] |
| **org** | **String**| Filter organizations to a specific organization name. | [optional] |
| **orgID** | **String**| Filter organizations to a specific organization ID. | [optional] |
| **userID** | **String**| Filter organizations to a specific user ID. | [optional] |

### Return type

[**Organizations**](Organizations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of organizations |  -  |
| **0** | Unexpected error |  -  |

<a id="getOrgsID"></a>
# **getOrgsID**
> Organization getOrgsID(orgID, zapTraceSpan)

Retrieve an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgID = "orgID_example"; // String | The ID of the organization to get.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Organization result = apiInstance.getOrgsID(orgID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#getOrgsID");
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
| **orgID** | **String**| The ID of the organization to get. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Organization**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization details |  -  |
| **0** | Unexpected error |  -  |

<a id="getOrgsIDMembers"></a>
# **getOrgsIDMembers**
> ResourceMembers getOrgsIDMembers(orgID, zapTraceSpan)

List all members of an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMembers result = apiInstance.getOrgsIDMembers(orgID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#getOrgsIDMembers");
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
| **orgID** | **String**| The organization ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of organization members |  -  |
| **404** | Organization not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getOrgsIDOwners"></a>
# **getOrgsIDOwners**
> ResourceOwners getOrgsIDOwners(orgID, zapTraceSpan)

List all owners of an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwners result = apiInstance.getOrgsIDOwners(orgID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#getOrgsIDOwners");
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
| **orgID** | **String**| The organization ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of organization owners |  -  |
| **404** | Organization not found |  -  |
| **0** | Unexpected error |  -  |

<a id="getOrgsIDSecrets_0"></a>
# **getOrgsIDSecrets_0**
> SecretKeysResponse getOrgsIDSecrets_0(orgID, zapTraceSpan)

List all secret keys for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization ID.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      SecretKeysResponse result = apiInstance.getOrgsIDSecrets_0(orgID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#getOrgsIDSecrets_0");
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
| **orgID** | **String**| The organization ID. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**SecretKeysResponse**](SecretKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all secret keys |  -  |
| **0** | Unexpected error |  -  |

<a id="patchOrgsID"></a>
# **patchOrgsID**
> Organization patchOrgsID(orgID, patchOrganizationRequest, zapTraceSpan)

Update an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgID = "orgID_example"; // String | The ID of the organization to get.
    PatchOrganizationRequest patchOrganizationRequest = new PatchOrganizationRequest(); // PatchOrganizationRequest | Organization update to apply
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Organization result = apiInstance.patchOrgsID(orgID, patchOrganizationRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#patchOrgsID");
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
| **orgID** | **String**| The ID of the organization to get. | |
| **patchOrganizationRequest** | [**PatchOrganizationRequest**](PatchOrganizationRequest.md)| Organization update to apply | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Organization**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Organization updated |  -  |
| **0** | Unexpected error |  -  |

<a id="patchOrgsIDSecrets_0"></a>
# **patchOrgsIDSecrets_0**
> patchOrgsIDSecrets_0(orgID, requestBody, zapTraceSpan)

Update secrets in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization ID.
    Map<String, String> requestBody = new HashMap(); // Map<String, String> | Secret key value pairs to update/add
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.patchOrgsIDSecrets_0(orgID, requestBody, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#patchOrgsIDSecrets_0");
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
| **orgID** | **String**| The organization ID. | |
| **requestBody** | [**Map&lt;String, String&gt;**](String.md)| Secret key value pairs to update/add | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Keys successfully patched |  -  |
| **0** | Unexpected error |  -  |

<a id="postOrgs"></a>
# **postOrgs**
> Organization postOrgs(postOrganizationRequest, zapTraceSpan)

Create an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    PostOrganizationRequest postOrganizationRequest = new PostOrganizationRequest(); // PostOrganizationRequest | Organization to create
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Organization result = apiInstance.postOrgs(postOrganizationRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#postOrgs");
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
| **postOrganizationRequest** | [**PostOrganizationRequest**](PostOrganizationRequest.md)| Organization to create | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Organization**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Organization created |  -  |
| **0** | Unexpected error |  -  |

<a id="postOrgsIDMembers"></a>
# **postOrgsIDMembers**
> ResourceMember postOrgsIDMembers(orgID, addResourceMemberRequestBody, zapTraceSpan)

Add a member to an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceMember result = apiInstance.postOrgsIDMembers(orgID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#postOrgsIDMembers");
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
| **orgID** | **String**| The organization ID. | |
| **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Added to organization created |  -  |
| **0** | Unexpected error |  -  |

<a id="postOrgsIDOwners"></a>
# **postOrgsIDOwners**
> ResourceOwner postOrgsIDOwners(orgID, addResourceMemberRequestBody, zapTraceSpan)

Add an owner to an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization ID.
    AddResourceMemberRequestBody addResourceMemberRequestBody = new AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      ResourceOwner result = apiInstance.postOrgsIDOwners(orgID, addResourceMemberRequestBody, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#postOrgsIDOwners");
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
| **orgID** | **String**| The organization ID. | |
| **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Organization owner added |  -  |
| **0** | Unexpected error |  -  |

<a id="postOrgsIDSecrets_0"></a>
# **postOrgsIDSecrets_0**
> postOrgsIDSecrets_0(orgID, secretKeys, zapTraceSpan)

Delete secrets from an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgID = "orgID_example"; // String | The organization ID.
    SecretKeys secretKeys = new SecretKeys(); // SecretKeys | Secret key to delete
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.postOrgsIDSecrets_0(orgID, secretKeys, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#postOrgsIDSecrets_0");
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
| **orgID** | **String**| The organization ID. | |
| **secretKeys** | [**SecretKeys**](SecretKeys.md)| Secret key to delete | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Keys successfully patched |  -  |
| **0** | Unexpected error |  -  |

