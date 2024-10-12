# PrincipalApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assignRolesToPrincipals**](PrincipalApi.md#assignRolesToPrincipals) | **POST** /principal/role | Assign roles to principals |
| [**getRolesForPrincipals**](PrincipalApi.md#getRolesForPrincipals) | **GET** /principal/role | Get roles assigned to principals |
| [**revokeRolesFromPrincipals**](PrincipalApi.md#revokeRolesFromPrincipals) | **POST** /principal/role/bulk_revoke | Revoke roles from principals |
| [**searchPrincipalsV1**](PrincipalApi.md#searchPrincipalsV1) | **GET** /principal | Search for principals |


<a id="assignRolesToPrincipals"></a>
# **assignRolesToPrincipals**
> List&lt;RoleInfo&gt; assignRolesToPrincipals(roleAssignmentRequest)

Assign roles to principals

Assign a set of roles to the specified principals.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrincipalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PrincipalApi apiInstance = new PrincipalApi(defaultClient);
    RoleAssignmentRequest roleAssignmentRequest = new RoleAssignmentRequest(); // RoleAssignmentRequest | A set of roles and a set of principals to which the roles should be granted. 
    try {
      List<RoleInfo> result = apiInstance.assignRolesToPrincipals(roleAssignmentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrincipalApi#assignRolesToPrincipals");
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
| **roleAssignmentRequest** | [**RoleAssignmentRequest**](RoleAssignmentRequest.md)| A set of roles and a set of principals to which the roles should be granted.  | |

### Return type

[**List&lt;RoleInfo&gt;**](RoleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Role information for roles assigned to the principal.  |  -  |

<a id="getRolesForPrincipals"></a>
# **getRolesForPrincipals**
> List&lt;PrincipalWithRoleInfo&gt; getRolesForPrincipals(principals)

Get roles assigned to principals

Get a list of role information for all roles assigned to the principals. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrincipalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PrincipalApi apiInstance = new PrincipalApi(defaultClient);
    List<String> principals = Arrays.asList(); // List<String> | IDs of the principals.
    try {
      List<PrincipalWithRoleInfo> result = apiInstance.getRolesForPrincipals(principals);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrincipalApi#getRolesForPrincipals");
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
| **principals** | [**List&lt;String&gt;**](String.md)| IDs of the principals. | |

### Return type

[**List&lt;PrincipalWithRoleInfo&gt;**](PrincipalWithRoleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of roles assigned to the principal. |  -  |

<a id="revokeRolesFromPrincipals"></a>
# **revokeRolesFromPrincipals**
> revokeRolesFromPrincipals(roleAssignmentRequest)

Revoke roles from principals

Revoke a set of roles from the specified principals. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrincipalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PrincipalApi apiInstance = new PrincipalApi(defaultClient);
    RoleAssignmentRequest roleAssignmentRequest = new RoleAssignmentRequest(); // RoleAssignmentRequest | A set of roles to revoke from a set of principals.
    try {
      apiInstance.revokeRolesFromPrincipals(roleAssignmentRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrincipalApi#revokeRolesFromPrincipals");
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
| **roleAssignmentRequest** | [**RoleAssignmentRequest**](RoleAssignmentRequest.md)| A set of roles to revoke from a set of principals. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfuly revoked roles from principals. |  -  |

<a id="searchPrincipalsV1"></a>
# **searchPrincipalsV1**
> PrincipalSummaryV1ListResponse searchPrincipalsV1(limit, offset, sortBy, sortOrder, authDomainId, organizationId, isAssignedRolesOrIsLocal, roleId, name, principalType, isTotpEnabled)

Search for principals

Search for principals based on the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrincipalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PrincipalApi apiInstance = new PrincipalApi(defaultClient);
    Integer limit = 56; // Integer | Maximum number of results to return.
    Integer offset = 56; // Integer | Starting offset of the results to return.
    String sortBy = "Name"; // String | Attribute by which to sort. Default is \"name\".
    String sortOrder = "asc"; // String | Sort order. Default order is ascending.
    String authDomainId = "authDomainId_example"; // String | ID of the authentication domain that contains the principal.
    String organizationId = "organizationId_example"; // String | ID of the organization of which the principal is a member.
    Boolean isAssignedRolesOrIsLocal = true; // Boolean | A Boolean that specifies whether the principal has any roles assigned or is a local user. When a principal is a local user, or when the principal has any roles assigned, this value is 'true'. 
    String roleId = "roleId_example"; // String | ID of a role assigned to the principal.
    String name = "name_example"; // String | The name of the principal.
    String principalType = "User"; // String | The type of principal.
    Boolean isTotpEnabled = true; // Boolean | Indicates if the principal has TOTP authentication enabled. Returns the users with TOTP authentication enabled when the value is true. 
    try {
      PrincipalSummaryV1ListResponse result = apiInstance.searchPrincipalsV1(limit, offset, sortBy, sortOrder, authDomainId, organizationId, isAssignedRolesOrIsLocal, roleId, name, principalType, isTotpEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrincipalApi#searchPrincipalsV1");
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
| **limit** | **Integer**| Maximum number of results to return. | [optional] |
| **offset** | **Integer**| Starting offset of the results to return. | [optional] |
| **sortBy** | **String**| Attribute by which to sort. Default is \&quot;name\&quot;. | [optional] [enum: Name, PrincipalType, Description, FirstName, LastName, EmailAddress, DisplayName] |
| **sortOrder** | **String**| Sort order. Default order is ascending. | [optional] [enum: asc, desc] |
| **authDomainId** | **String**| ID of the authentication domain that contains the principal. | [optional] |
| **organizationId** | **String**| ID of the organization of which the principal is a member. | [optional] |
| **isAssignedRolesOrIsLocal** | **Boolean**| A Boolean that specifies whether the principal has any roles assigned or is a local user. When a principal is a local user, or when the principal has any roles assigned, this value is &#39;true&#39;.  | [optional] |
| **roleId** | **String**| ID of a role assigned to the principal. | [optional] |
| **name** | **String**| The name of the principal. | [optional] |
| **principalType** | **String**| The type of principal. | [optional] [enum: User, Group] |
| **isTotpEnabled** | **Boolean**| Indicates if the principal has TOTP authentication enabled. Returns the users with TOTP authentication enabled when the value is true.  | [optional] |

### Return type

[**PrincipalSummaryV1ListResponse**](PrincipalSummaryV1ListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of matching principals. |  -  |

