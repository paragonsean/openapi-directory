# UsersReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**flextimeAdjustmentsGetFlextimeAdjustment**](UsersReadApi.md#flextimeAdjustmentsGetFlextimeAdjustment) | **GET** /v1/flextimeadjustments/{guid} | Get Flextime Adjustment by ID. |
| [**flextimeAdjustmentsGetFlextimeAdjustments**](UsersReadApi.md#flextimeAdjustmentsGetFlextimeAdjustments) | **GET** /v1/users/{userGuid}/flextimeadjustments | Get the Flextime Adjustments. |
| [**flextimeGetFlextime**](UsersReadApi.md#flextimeGetFlextime) | **GET** /v1/users/{userGuid}/flextime | Get the flextime balance for a user for a specified date. Total balance is returned for the given date. Month balance is the balance for the month of the given date. Values are returned only if the advanced time tracking add-on is active. |
| [**keywordsGetUserKeywords**](UsersReadApi.md#keywordsGetUserKeywords) | **GET** /v1/users/{userGuid}/keywords | Get all the keywords for user. |
| [**projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser**](UsersReadApi.md#projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser) | **GET** /v1/users/{userGuid}/projectmembercostexceptions | Get all cost exceptions of project members for user. |
| [**userCustomValuesGetUserCustomValue**](UsersReadApi.md#userCustomValuesGetUserCustomValue) | **GET** /v1/users/customvalues/{guid} | Get user custom value by ID. |
| [**userCustomValuesGetUserCustomValues**](UsersReadApi.md#userCustomValuesGetUserCustomValues) | **GET** /v1/users/{userGuid}/customvalues | Get the user custom values. |
| [**usersGetUser**](UsersReadApi.md#usersGetUser) | **GET** /v1/users/{guid} | Get user by ID. |
| [**usersGetUsers**](UsersReadApi.md#usersGetUsers) | **GET** /v1/users | Get users |
| [**workContractsGetCurrentWorkContractForUser**](UsersReadApi.md#workContractsGetCurrentWorkContractForUser) | **GET** /v1/users/{userGuid}/workcontracts/current | Gets current work contract for the user |
| [**workContractsGetWorkContract_0**](UsersReadApi.md#workContractsGetWorkContract_0) | **GET** /v1/workcontracts/{guid} | Get work contract by ID. |
| [**workContractsGetWorkContractsForUser**](UsersReadApi.md#workContractsGetWorkContractsForUser) | **GET** /v1/users/{userGuid}/workcontracts | Get all the work contracts for the user. |
| [**workdaysGetWorkdays**](UsersReadApi.md#workdaysGetWorkdays) | **GET** /v1/users/{userGuid}/workdays | Get workdays for a user. |


<a id="flextimeAdjustmentsGetFlextimeAdjustment"></a>
# **flextimeAdjustmentsGetFlextimeAdjustment**
> FlextimeAdjustmentOutputModel flextimeAdjustmentsGetFlextimeAdjustment(guid)

Get Flextime Adjustment by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the Flextime Adjustment.
    try {
      FlextimeAdjustmentOutputModel result = apiInstance.flextimeAdjustmentsGetFlextimeAdjustment(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#flextimeAdjustmentsGetFlextimeAdjustment");
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
| **guid** | **String**| GUID used to get the Flextime Adjustment. | |

### Return type

[**FlextimeAdjustmentOutputModel**](FlextimeAdjustmentOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flextime Adjustment. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="flextimeAdjustmentsGetFlextimeAdjustments"></a>
# **flextimeAdjustmentsGetFlextimeAdjustments**
> List&lt;FlextimeAdjustmentOutputModel&gt; flextimeAdjustmentsGetFlextimeAdjustments(userGuid, pageToken, rowCount)

Get the Flextime Adjustments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | ID of the user for whom to get the adjustments.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    try {
      List<FlextimeAdjustmentOutputModel> result = apiInstance.flextimeAdjustmentsGetFlextimeAdjustments(userGuid, pageToken, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#flextimeAdjustmentsGetFlextimeAdjustments");
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
| **userGuid** | **String**| ID of the user for whom to get the adjustments. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |

### Return type

[**List&lt;FlextimeAdjustmentOutputModel&gt;**](FlextimeAdjustmentOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Flextime Adjustments. |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="flextimeGetFlextime"></a>
# **flextimeGetFlextime**
> FlextimeModel flextimeGetFlextime(userGuid, eventDate)

Get the flextime balance for a user for a specified date. Total balance is returned for the given date. Month balance is the balance for the month of the given date. Values are returned only if the advanced time tracking add-on is active.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | Id of the user.
    OffsetDateTime eventDate = OffsetDateTime.now(); // OffsetDateTime | Date for which to get the balance. Max 12 months into the future.
    try {
      FlextimeModel result = apiInstance.flextimeGetFlextime(userGuid, eventDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#flextimeGetFlextime");
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
| **userGuid** | **String**| Id of the user. | |
| **eventDate** | **OffsetDateTime**| Date for which to get the balance. Max 12 months into the future. | [optional] |

### Return type

[**FlextimeModel**](FlextimeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | FlextimeModel. |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsGetUserKeywords"></a>
# **keywordsGetUserKeywords**
> List&lt;UserKeywordModel&gt; keywordsGetUserKeywords(userGuid, active, sortings)

Get all the keywords for user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | ID of the user for who keywords are requested.
    Boolean active = true; // Boolean | If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Keyword&sortings[0].value=Desc\".
    try {
      List<UserKeywordModel> result = apiInstance.keywordsGetUserKeywords(userGuid, active, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#keywordsGetUserKeywords");
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
| **userGuid** | **String**| ID of the user for who keywords are requested. | |
| **active** | **Boolean**| If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords. | [optional] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] |

### Return type

[**List&lt;UserKeywordModel&gt;**](UserKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keywords. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser"></a>
# **projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser**
> List&lt;ProjectMemberCostExceptionOutputModel&gt; projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser(userGuid, isProjectClosed, firstRow, rowCount)

Get all cost exceptions of project members for user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | Guid of the user.
    Boolean isProjectClosed = true; // Boolean | Search only for open or closed projects. Default all projects.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    try {
      List<ProjectMemberCostExceptionOutputModel> result = apiInstance.projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser(userGuid, isProjectClosed, firstRow, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#projectMemberCostExceptionsGetProjectMemberCostExceptionsForUser");
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
| **userGuid** | **String**| Guid of the user. | |
| **isProjectClosed** | **Boolean**| Search only for open or closed projects. Default all projects. | [optional] |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |

### Return type

[**List&lt;ProjectMemberCostExceptionOutputModel&gt;**](ProjectMemberCostExceptionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the member cost exceptions for one project. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="userCustomValuesGetUserCustomValue"></a>
# **userCustomValuesGetUserCustomValue**
> UserCustomValueOutputModel userCustomValuesGetUserCustomValue(guid)

Get user custom value by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the user custom value.
    try {
      UserCustomValueOutputModel result = apiInstance.userCustomValuesGetUserCustomValue(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#userCustomValuesGetUserCustomValue");
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
| **guid** | **String**| Id used to get the user custom value. | |

### Return type

[**UserCustomValueOutputModel**](UserCustomValueOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="userCustomValuesGetUserCustomValues"></a>
# **userCustomValuesGetUserCustomValues**
> List&lt;UserCustomValueOutputModel&gt; userCustomValuesGetUserCustomValues(userGuid, pageToken, rowCount, isActive, targets, changedSince)

Get the user custom values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | ID of the user.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    Boolean isActive = true; // Boolean | Optional: Get only values of active or inactive user custom properties.
    List<String> targets = Arrays.asList(); // List<String> | Optional: List of target for which to get the values.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get user custom values that have been added or changed after this date time (greater or equal).
    try {
      List<UserCustomValueOutputModel> result = apiInstance.userCustomValuesGetUserCustomValues(userGuid, pageToken, rowCount, isActive, targets, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#userCustomValuesGetUserCustomValues");
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
| **userGuid** | **String**| ID of the user. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **isActive** | **Boolean**| Optional: Get only values of active or inactive user custom properties. | [optional] |
| **targets** | [**List&lt;String&gt;**](String.md)| Optional: List of target for which to get the values. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get user custom values that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;UserCustomValueOutputModel&gt;**](UserCustomValueOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * NextPageToken - Page token to fetch the next page <br>  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="usersGetUser"></a>
# **usersGetUser**
> UserOutputModel usersGetUser(guid)

Get user by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the user.
    try {
      UserOutputModel result = apiInstance.usersGetUser(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#usersGetUser");
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
| **guid** | **String**| GUID used to get the user. | |

### Return type

[**UserOutputModel**](UserOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="usersGetUsers"></a>
# **usersGetUsers**
> List&lt;UserOutputModel&gt; usersGetUsers(pageToken, rowCount, isActive, businessUnitGuids, keywordGuids, changedSince, supervisorUserGuids, code, email, purpose)

Get users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | 
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch.
    Boolean isActive = true; // Boolean | If not given, return all users, if given as true return only active users, if given as false returns only inactive users
    List<String> businessUnitGuids = Arrays.asList(); // List<String> | Optional: ID of the business unit of the user. If not provided, returns for all business units. Default all.
    List<String> keywordGuids = Arrays.asList(); // List<String> | Optional: ID of the keyword of the user. If not provided, returns for all keywords. Default all.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get users that have been added or changed after this date time (greater or equal).
    List<String> supervisorUserGuids = Arrays.asList(); // List<String> | Optional: ID of the supervisor to get subordinates for.
    String code = ""; // String | Optional: Code of the user.
    String email = ""; // String | Optional: Email address of the user.
    GetUsersPurpose purpose = GetUsersPurpose.fromValue("AbsenceOwner"); // GetUsersPurpose | Optional: Filter users by purpose.
    try {
      List<UserOutputModel> result = apiInstance.usersGetUsers(pageToken, rowCount, isActive, businessUnitGuids, keywordGuids, changedSince, supervisorUserGuids, code, email, purpose);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#usersGetUsers");
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
| **pageToken** | **String**|  | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch. | [optional] |
| **isActive** | **Boolean**| If not given, return all users, if given as true return only active users, if given as false returns only inactive users | [optional] |
| **businessUnitGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the business unit of the user. If not provided, returns for all business units. Default all. | [optional] |
| **keywordGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the keyword of the user. If not provided, returns for all keywords. Default all. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get users that have been added or changed after this date time (greater or equal). | [optional] |
| **supervisorUserGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the supervisor to get subordinates for. | [optional] |
| **code** | **String**| Optional: Code of the user. | [optional] [default to ] |
| **email** | **String**| Optional: Email address of the user. | [optional] [default to ] |
| **purpose** | [**GetUsersPurpose**](.md)| Optional: Filter users by purpose. | [optional] [enum: AbsenceOwner, AccountOwner, ActivityOwner, ActivityParticipant, BillingContact, ProjectManager, SalesPerson, SuperiorUser, TermsOfServiceApprover] |

### Return type

[**List&lt;UserOutputModel&gt;**](UserOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the users |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workContractsGetCurrentWorkContractForUser"></a>
# **workContractsGetCurrentWorkContractForUser**
> WorkContractOutputModel workContractsGetCurrentWorkContractForUser(userGuid)

Gets current work contract for the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | Id of the user
    try {
      WorkContractOutputModel result = apiInstance.workContractsGetCurrentWorkContractForUser(userGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#workContractsGetCurrentWorkContractForUser");
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
| **userGuid** | **String**| Id of the user | |

### Return type

[**WorkContractOutputModel**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Work contracts |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workContractsGetWorkContract_0"></a>
# **workContractsGetWorkContract_0**
> WorkContractOutputModel workContractsGetWorkContract_0(guid)

Get work contract by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String guid = "guid_example"; // String | Id used to get the work contract.
    try {
      WorkContractOutputModel result = apiInstance.workContractsGetWorkContract_0(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#workContractsGetWorkContract_0");
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
| **guid** | **String**| Id used to get the work contract. | |

### Return type

[**WorkContractOutputModel**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workContractsGetWorkContractsForUser"></a>
# **workContractsGetWorkContractsForUser**
> List&lt;WorkContractOutputModel&gt; workContractsGetWorkContractsForUser(userGuid)

Get all the work contracts for the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | Id of the user.
    try {
      List<WorkContractOutputModel> result = apiInstance.workContractsGetWorkContractsForUser(userGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#workContractsGetWorkContractsForUser");
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
| **userGuid** | **String**| Id of the user. | |

### Return type

[**List&lt;WorkContractOutputModel&gt;**](WorkContractOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Work contracts. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workdaysGetWorkdays"></a>
# **workdaysGetWorkdays**
> List&lt;WorkdayModel&gt; workdaysGetWorkdays(userGuid, startDate, endDate)

Get workdays for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersReadApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersReadApi apiInstance = new UsersReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | ID of the user.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Start date of the workdays.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | End date of the workdays.
    try {
      List<WorkdayModel> result = apiInstance.workdaysGetWorkdays(userGuid, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersReadApi#workdaysGetWorkdays");
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
| **userGuid** | **String**| ID of the user. | |
| **startDate** | **OffsetDateTime**| Start date of the workdays. | |
| **endDate** | **OffsetDateTime**| End date of the workdays. | |

### Return type

[**List&lt;WorkdayModel&gt;**](WorkdayModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User&#39;s workdays. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

