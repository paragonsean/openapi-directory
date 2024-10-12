# ResourcesApi

All URIs are relative to *http://conjur.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**showResource**](ResourcesApi.md#showResource) | **GET** /resources/{account}/{kind}/{identifier} | Shows a description of a single resource. |
| [**showResourcesForAccount**](ResourcesApi.md#showResourcesForAccount) | **GET** /resources/{account} | Lists resources within an organization account. |
| [**showResourcesForAllAccounts**](ResourcesApi.md#showResourcesForAllAccounts) | **GET** /resources | Lists resources within an organization account. |
| [**showResourcesForKind**](ResourcesApi.md#showResourcesForKind) | **GET** /resources/{account}/{kind} | Lists resources of the same kind within an organization account. |


<a id="showResource"></a>
# **showResource**
> Object showResource(account, kind, identifier, xRequestId, permittedRoles, privilege, check, role)

Shows a description of a single resource.

Details about a single resource.  If &#x60;permitted_roles&#x60; and &#x60;privilege&#x60; are given, Conjur lists the roles with the specified privilege on the resource.  If &#x60;check&#x60;, &#x60;privilege&#x60; and &#x60;role&#x60; are given, Conjur checks if the specified role has the privilege on the resource.  If &#x60;permitted_roles&#x60; and &#x60;check&#x60; are both given, Conjur responds to the &#x60;check&#x60; call ONLY.  ##### Permissions Required 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String account = "account_example"; // String | Organization account name
    String kind = "user"; // String | Type of resource
    String identifier = "conjur/authn-iam/test"; // String | ID of the resource for which to get the information about
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    Boolean permittedRoles = true; // Boolean | Lists the roles which have the named privilege on a resource.
    String privilege = "execute"; // String | Level of privilege to filter on. Can only be used in combination with `permitted_roles` or `check` parameter.
    Boolean check = true; // Boolean | Check whether a role has a privilege on a resource.
    String role = "myorg:host:host1"; // String | Role to check privilege on. Can only be used in combination with `check` parameter.
    try {
      Object result = apiInstance.showResource(account, kind, identifier, xRequestId, permittedRoles, privilege, check, role);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#showResource");
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
| **account** | **String**| Organization account name | |
| **kind** | **String**| Type of resource | |
| **identifier** | **String**| ID of the resource for which to get the information about | |
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |
| **permittedRoles** | **Boolean**| Lists the roles which have the named privilege on a resource. | [optional] |
| **privilege** | **String**| Level of privilege to filter on. Can only be used in combination with &#x60;permitted_roles&#x60; or &#x60;check&#x60; parameter. | [optional] |
| **check** | **Boolean**| Check whether a role has a privilege on a resource. | [optional] |
| **role** | **String**| Role to check privilege on. Can only be used in combination with &#x60;check&#x60; parameter. | [optional] |

### Return type

**Object**

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body contains the list of role memberships or permitted roles |  -  |
| **204** | Permissions check was successful |  -  |
| **400** | The server cannot process the request due to malformed request syntax |  -  |
| **401** | Authentication information is missing or invalid |  -  |
| **403** | The authenticated user lacks the necessary privileges |  -  |
| **404** | The requested resource does not exist, the authenticated user lacks the required privileges to enumerate this resource, or its value has not been set |  -  |
| **422** | A request parameter was either missing or invalid. |  -  |

<a id="showResourcesForAccount"></a>
# **showResourcesForAccount**
> showResourcesForAccount(account, xRequestId, kind, search, offset, limit, count, role, actingAs)

Lists resources within an organization account.

Lists resources within an organization account.  If a &#x60;kind&#x60; query parameter is given, narrows results to only resources of that kind.  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give &#x60;limit&#x60; a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is &#x60;true&#x60;, returns only the number of items in the list.  ##### Text search  If the &#x60;search&#x60; parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called &#x60;name&#x60; appear first, then those with another matching annotation value, and finally those with a matching  &#x60;kind&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String account = "account_example"; // String | Organization account name
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    String kind = "user"; // String | Type of resource
    ERRORUNKNOWN search = new ERRORUNKNOWN(); // ERRORUNKNOWN | Filter resources based on this value by name
    Integer offset = 56; // Integer | When listing resources, start at this item number.
    Integer limit = 56; // Integer | When listing resources, return up to this many results.
    Boolean count = true; // Boolean | When listing resources, if `true`, return only the count of the results.
    String role = "myorg:host:host1"; // String | Retrieves the resources list for a different role if the authenticated role has access
    String actingAs = "myorg:host:host1"; // String | Retrieves the resources list for a different role if the authenticated role has access
    try {
      apiInstance.showResourcesForAccount(account, xRequestId, kind, search, offset, limit, count, role, actingAs);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#showResourcesForAccount");
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
| **account** | **String**| Organization account name | |
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |
| **kind** | **String**| Type of resource | [optional] |
| **search** | [**ERRORUNKNOWN**](.md)| Filter resources based on this value by name | [optional] |
| **offset** | **Integer**| When listing resources, start at this item number. | [optional] |
| **limit** | **Integer**| When listing resources, return up to this many results. | [optional] |
| **count** | **Boolean**| When listing resources, if &#x60;true&#x60;, return only the count of the results. | [optional] |
| **role** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] |
| **actingAs** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] |

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | The server cannot process the request due to malformed request syntax |  -  |
| **401** | Authentication information is missing or invalid |  -  |
| **403** | The authenticated user lacks the necessary privileges |  -  |
| **422** | A request parameter was either missing or invalid. |  -  |

<a id="showResourcesForAllAccounts"></a>
# **showResourcesForAllAccounts**
> List&lt;ShowResourcesForAllAccounts200ResponseInner&gt; showResourcesForAllAccounts(xRequestId, account, kind, search, offset, limit, count, role, actingAs)

Lists resources within an organization account.

Lists resources within an organization account.  In the absence of an &#x60;account&#x60; query parameter, shows results for the account of the authorization token user.  If an &#x60;account&#x60; query parameter is given, shows results for the specified account.  If a &#x60;kind&#x60; query parameter is given, narrows results to only resources of that kind.  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give &#x60;limit&#x60; a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is &#x60;true&#x60;, returns only the number of items in the list.  ##### Text search  If the &#x60;search&#x60; parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called &#x60;name&#x60; appear first, then those with another matching annotation value, and finally those with a matching  &#x60;kind&#x60;.\&quot; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    String account = "myorg"; // String | Organization account name
    String kind = "user"; // String | Type of resource
    String search = "password"; // String | Filter resources based on this value by name
    Integer offset = 56; // Integer | When listing resources, start at this item number.
    Integer limit = 56; // Integer | When listing resources, return up to this many results.
    Boolean count = true; // Boolean | When listing resources, if `true`, return only the count of the results.
    String role = "myorg:host:host1"; // String | Retrieves the resources list for a different role if the authenticated role has access
    String actingAs = "myorg:host:host1"; // String | Retrieves the resources list for a different role if the authenticated role has access
    try {
      List<ShowResourcesForAllAccounts200ResponseInner> result = apiInstance.showResourcesForAllAccounts(xRequestId, account, kind, search, offset, limit, count, role, actingAs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#showResourcesForAllAccounts");
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
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |
| **account** | **String**| Organization account name | [optional] |
| **kind** | **String**| Type of resource | [optional] |
| **search** | **String**| Filter resources based on this value by name | [optional] |
| **offset** | **Integer**| When listing resources, start at this item number. | [optional] |
| **limit** | **Integer**| When listing resources, return up to this many results. | [optional] |
| **count** | **Boolean**| When listing resources, if &#x60;true&#x60;, return only the count of the results. | [optional] |
| **role** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] |
| **actingAs** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] |

### Return type

[**List&lt;ShowResourcesForAllAccounts200ResponseInner&gt;**](ShowResourcesForAllAccounts200ResponseInner.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body contains a list of resources |  -  |
| **401** | Authentication information is missing or invalid |  -  |
| **403** | The authenticated user lacks the necessary privileges |  -  |
| **422** | A request parameter was either missing or invalid. |  -  |

<a id="showResourcesForKind"></a>
# **showResourcesForKind**
> showResourcesForKind(account, kind, xRequestId, search, offset, limit, count, role, actingAs)

Lists resources of the same kind within an organization account.

Lists resources of the same kind within an organization account.  Kinds of resources include: policy, user, host, group, layer, or variable  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give &#x60;limit&#x60; a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is &#x60;true&#x60;, returns only the number of items in the list.  ##### Text search  If the &#x60;search&#x60; parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called &#x60;name&#x60; appear first, then those with another matching annotation value, and finally those with a matching  &#x60;kind&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    ResourcesApi apiInstance = new ResourcesApi(defaultClient);
    String account = "account_example"; // String | Organization account name
    String kind = "user"; // String | Type of resource
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    ERRORUNKNOWN search = new ERRORUNKNOWN(); // ERRORUNKNOWN | Filter resources based on this value by name
    Integer offset = 56; // Integer | When listing resources, start at this item number.
    Integer limit = 56; // Integer | When listing resources, return up to this many results.
    Boolean count = true; // Boolean | When listing resources, if `true`, return only the count of the results.
    String role = "myorg:host:host1"; // String | Retrieves the resources list for a different role if the authenticated role has access
    String actingAs = "myorg:host:host1"; // String | Retrieves the resources list for a different role if the authenticated role has access
    try {
      apiInstance.showResourcesForKind(account, kind, xRequestId, search, offset, limit, count, role, actingAs);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResourcesApi#showResourcesForKind");
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
| **account** | **String**| Organization account name | |
| **kind** | **String**| Type of resource | |
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |
| **search** | [**ERRORUNKNOWN**](.md)| Filter resources based on this value by name | [optional] |
| **offset** | **Integer**| When listing resources, start at this item number. | [optional] |
| **limit** | **Integer**| When listing resources, return up to this many results. | [optional] |
| **count** | **Boolean**| When listing resources, if &#x60;true&#x60;, return only the count of the results. | [optional] |
| **role** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] |
| **actingAs** | **String**| Retrieves the resources list for a different role if the authenticated role has access | [optional] |

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | The server cannot process the request due to malformed request syntax |  -  |
| **401** | Authentication information is missing or invalid |  -  |
| **403** | The authenticated user lacks the necessary privileges |  -  |
| **422** | A request parameter was either missing or invalid. |  -  |

