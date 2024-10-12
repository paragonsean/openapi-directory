# AccountsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsDeleteAccountById**](AccountsApi.md#accountsDeleteAccountById) | **DELETE** /api/Accounts/{id} |  |
| [**accountsDeleteAccountHoldingByAccountidId**](AccountsApi.md#accountsDeleteAccountHoldingByAccountidId) | **DELETE** /api/Accounts/{accountId}/Holdings/{id} |  |
| [**accountsDeleteSavingsStrategiesByAccountid**](AccountsApi.md#accountsDeleteSavingsStrategiesByAccountid) | **DELETE** /api/Accounts/{accountId}/SavingsStrategies |  |
| [**accountsDeleteSavingsStrategyByAccountidId**](AccountsApi.md#accountsDeleteSavingsStrategyByAccountidId) | **DELETE** /api/Accounts/{accountId}/SavingsStrategies/{id} |  |
| [**accountsGetAccountHoldingByAccountidId**](AccountsApi.md#accountsGetAccountHoldingByAccountidId) | **GET** /api/Accounts/{accountId}/Holdings/{id} |  |
| [**accountsGetAccountHoldingsByAccountid**](AccountsApi.md#accountsGetAccountHoldingsByAccountid) | **GET** /api/Accounts/{accountId}/Holdings |  |
| [**accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid**](AccountsApi.md#accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid) | **GET** /api/Accounts |  |
| [**accountsGetById**](AccountsApi.md#accountsGetById) | **GET** /api/Accounts/{id} |  |
| [**accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId**](AccountsApi.md#accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId) | **GET** /api/Accounts/{accountId}/SavingsStrategies/{id} |  |
| [**accountsGetSavingsStrategiesByAccountIdByAccountid**](AccountsApi.md#accountsGetSavingsStrategiesByAccountIdByAccountid) | **GET** /api/Accounts/{accountId}/SavingsStrategies |  |
| [**accountsPostAccountHoldingByAccountidModel**](AccountsApi.md#accountsPostAccountHoldingByAccountidModel) | **POST** /api/Accounts/{accountId}/Holdings |  |
| [**accountsPostByModel**](AccountsApi.md#accountsPostByModel) | **POST** /api/Accounts |  |
| [**accountsPostSavingsStrategyByAccountidSavingsstrategy**](AccountsApi.md#accountsPostSavingsStrategyByAccountidSavingsstrategy) | **POST** /api/Accounts/{accountId}/SavingsStrategies |  |
| [**accountsPutByAccountidIdHolding**](AccountsApi.md#accountsPutByAccountidIdHolding) | **PUT** /api/Accounts/{accountId}/Holdings/{id} |  |
| [**accountsPutByIdModel**](AccountsApi.md#accountsPutByIdModel) | **PUT** /api/Accounts/{id} |  |
| [**accountsPutHoldingsByAccountidHoldings**](AccountsApi.md#accountsPutHoldingsByAccountidHoldings) | **PUT** /api/Accounts/{accountId}/Holdings |  |
| [**accountsPutSavingsStrategyByAccountidIdSavingsstrategy**](AccountsApi.md#accountsPutSavingsStrategyByAccountidIdSavingsstrategy) | **PUT** /api/Accounts/{accountId}/SavingsStrategies/{id} |  |


<a id="accountsDeleteAccountById"></a>
# **accountsDeleteAccountById**
> accountsDeleteAccountById(id)



Description: The operation removes an Account tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of an Account from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer id = 56; // Integer | The Account ID used to identify which Account to remove
    try {
      apiInstance.accountsDeleteAccountById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsDeleteAccountById");
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
| **id** | **Integer**| The Account ID used to identify which Account to remove | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsDeleteAccountHoldingByAccountidId"></a>
# **accountsDeleteAccountHoldingByAccountidId**
> accountsDeleteAccountHoldingByAccountidId(accountId, id)



Description: This operation deletes a single Account Holding for the specified Account Holding ID and Account ID.&lt;br /&gt;                Purpose: Provides the ability to remove individual holdings from a specified Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | The ID of the Account used to retrieve the Account data that the specified holding belongs to.
    Integer id = 56; // Integer | The ID of the Account Holding used to delete the Account Holding
    try {
      apiInstance.accountsDeleteAccountHoldingByAccountidId(accountId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsDeleteAccountHoldingByAccountidId");
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
| **accountId** | **Integer**| The ID of the Account used to retrieve the Account data that the specified holding belongs to. | |
| **id** | **Integer**| The ID of the Account Holding used to delete the Account Holding | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsDeleteSavingsStrategiesByAccountid"></a>
# **accountsDeleteSavingsStrategiesByAccountid**
> accountsDeleteSavingsStrategiesByAccountid(accountId)



Deletes all savings strategies tied to an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | Id of the account that holds the savings strategies
    try {
      apiInstance.accountsDeleteSavingsStrategiesByAccountid(accountId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsDeleteSavingsStrategiesByAccountid");
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
| **accountId** | **Integer**| Id of the account that holds the savings strategies | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsDeleteSavingsStrategyByAccountidId"></a>
# **accountsDeleteSavingsStrategyByAccountidId**
> accountsDeleteSavingsStrategyByAccountidId(accountId, id)



Deletes a specific savings strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | Id of the account that holds the savings strategy
    Integer id = 56; // Integer | Id of the savings strategy to be deleted
    try {
      apiInstance.accountsDeleteSavingsStrategyByAccountidId(accountId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsDeleteSavingsStrategyByAccountidId");
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
| **accountId** | **Integer**| Id of the account that holds the savings strategy | |
| **id** | **Integer**| Id of the savings strategy to be deleted | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsGetAccountHoldingByAccountidId"></a>
# **accountsGetAccountHoldingByAccountidId**
> AccountHoldingWithIdModel accountsGetAccountHoldingByAccountidId(accountId, id)



Description: This operation retrieves a single Account Holding for the specified Account Holding ID and Account ID.&lt;br /&gt;                Purpose: Provides access to the Account Holding information including description and market value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | The ID of the Account used to retrieve the Account Holding data
    Integer id = 56; // Integer | The ID of the Account Holding used to retrieve the Account Holding data
    try {
      AccountHoldingWithIdModel result = apiInstance.accountsGetAccountHoldingByAccountidId(accountId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsGetAccountHoldingByAccountidId");
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
| **accountId** | **Integer**| The ID of the Account used to retrieve the Account Holding data | |
| **id** | **Integer**| The ID of the Account Holding used to retrieve the Account Holding data | |

### Return type

[**AccountHoldingWithIdModel**](AccountHoldingWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsGetAccountHoldingsByAccountid"></a>
# **accountsGetAccountHoldingsByAccountid**
> AccountHoldingsModel accountsGetAccountHoldingsByAccountid(accountId)



Retrieves all holdings in the specified Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | The ID of the Account used to retrieve the Account Holding data
    try {
      AccountHoldingsModel result = apiInstance.accountsGetAccountHoldingsByAccountid(accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsGetAccountHoldingsByAccountid");
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
| **accountId** | **Integer**| The ID of the Account used to retrieve the Account Holding data | |

### Return type

[**AccountHoldingsModel**](AccountHoldingsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid"></a>
# **accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid**
> AccountsModel accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid(factFinderId, externalSourceId)



Description: This operation retrieves all Accounts for the specified Fact Finder ID and/or external source ID.&lt;br /&gt;                Purpose: Provides access to the Account information including description and market value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Accounts
    String externalSourceId = "externalSourceId_example"; // String | The external ID used to filter Accounts
    try {
      AccountsModel result = apiInstance.accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid(factFinderId, externalSourceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsGetAccountsByFactFinderIdByFactfinderidExternalsourceid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Accounts | |
| **externalSourceId** | **String**| The external ID used to filter Accounts | [optional] |

### Return type

[**AccountsModel**](AccountsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsGetById"></a>
# **accountsGetById**
> AccountWithIdModel accountsGetById(id)



Description: This operation retrieves a single Account for the specified Account ID.&lt;br /&gt;                Purpose: Provides access to the Account information including description and market value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Account used to retrieve the Account data
    try {
      AccountWithIdModel result = apiInstance.accountsGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsGetById");
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
| **id** | **Integer**| The ID of the Account used to retrieve the Account data | |

### Return type

[**AccountWithIdModel**](AccountWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId"></a>
# **accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId**
> SavingsStrategyWithIdModel accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId(accountId, id)



Get a specific savings strategy for an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | The id of the account to retrieve the savings strategies from
    Integer id = 56; // Integer | The id of the savings strategy to get
    try {
      SavingsStrategyWithIdModel result = apiInstance.accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId(accountId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsGetSavingsStrategiesByAccountIdAndSavingsStrategyIdByAccountidId");
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
| **accountId** | **Integer**| The id of the account to retrieve the savings strategies from | |
| **id** | **Integer**| The id of the savings strategy to get | |

### Return type

[**SavingsStrategyWithIdModel**](SavingsStrategyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsGetSavingsStrategiesByAccountIdByAccountid"></a>
# **accountsGetSavingsStrategiesByAccountIdByAccountid**
> SavingsStrategiesModel accountsGetSavingsStrategiesByAccountIdByAccountid(accountId)



Get all of the savings strategies for a specific account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | The id of the account to retrieve the savings strategies from
    try {
      SavingsStrategiesModel result = apiInstance.accountsGetSavingsStrategiesByAccountIdByAccountid(accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsGetSavingsStrategiesByAccountIdByAccountid");
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
| **accountId** | **Integer**| The id of the account to retrieve the savings strategies from | |

### Return type

[**SavingsStrategiesModel**](SavingsStrategiesModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsPostAccountHoldingByAccountidModel"></a>
# **accountsPostAccountHoldingByAccountidModel**
> AccountHoldingWithIdModel accountsPostAccountHoldingByAccountidModel(accountId, model)



Creates a holding and adds it to an existing Account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | The existing Account ID used to identify which Account to add the holding to
    AccountHoldingModel model = new AccountHoldingModel(); // AccountHoldingModel | The holding data
    try {
      AccountHoldingWithIdModel result = apiInstance.accountsPostAccountHoldingByAccountidModel(accountId, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsPostAccountHoldingByAccountidModel");
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
| **accountId** | **Integer**| The existing Account ID used to identify which Account to add the holding to | |
| **model** | [**AccountHoldingModel**](AccountHoldingModel.md)| The holding data | |

### Return type

[**AccountHoldingWithIdModel**](AccountHoldingWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsPostByModel"></a>
# **accountsPostByModel**
> AccountWithIdModel accountsPostByModel(model)



Description: The operation creates an Account.&lt;br /&gt;                Purpose: Allows for creation of Accounts on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    AccountModel model = new AccountModel(); // AccountModel | The Account to be added to the Fact Finder
    try {
      AccountWithIdModel result = apiInstance.accountsPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsPostByModel");
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
| **model** | [**AccountModel**](AccountModel.md)| The Account to be added to the Fact Finder | |

### Return type

[**AccountWithIdModel**](AccountWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsPostSavingsStrategyByAccountidSavingsstrategy"></a>
# **accountsPostSavingsStrategyByAccountidSavingsstrategy**
> SavingsStrategyWithIdModel accountsPostSavingsStrategyByAccountidSavingsstrategy(accountId, savingsStrategy)



Creates a savings strategy on a specific account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | Id of the account to create a savings strategy for
    SavingsStrategyModel savingsStrategy = new SavingsStrategyModel(); // SavingsStrategyModel | Values for the strategy to be created
    try {
      SavingsStrategyWithIdModel result = apiInstance.accountsPostSavingsStrategyByAccountidSavingsstrategy(accountId, savingsStrategy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsPostSavingsStrategyByAccountidSavingsstrategy");
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
| **accountId** | **Integer**| Id of the account to create a savings strategy for | |
| **savingsStrategy** | [**SavingsStrategyModel**](SavingsStrategyModel.md)| Values for the strategy to be created | |

### Return type

[**SavingsStrategyWithIdModel**](SavingsStrategyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsPutByAccountidIdHolding"></a>
# **accountsPutByAccountidIdHolding**
> AccountHoldingModel accountsPutByAccountidIdHolding(accountId, id, holding)



Updates a holding associated with an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | The account with the holding to be updated
    Integer id = 56; // Integer | The id of the holding to update
    AccountHoldingModel holding = new AccountHoldingModel(); // AccountHoldingModel | The holding values used to update the current holding
    try {
      AccountHoldingModel result = apiInstance.accountsPutByAccountidIdHolding(accountId, id, holding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsPutByAccountidIdHolding");
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
| **accountId** | **Integer**| The account with the holding to be updated | |
| **id** | **Integer**| The id of the holding to update | |
| **holding** | [**AccountHoldingModel**](AccountHoldingModel.md)| The holding values used to update the current holding | |

### Return type

[**AccountHoldingModel**](AccountHoldingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsPutByIdModel"></a>
# **accountsPutByIdModel**
> AccountWithIdModel accountsPutByIdModel(id, model)



Description: The operation updates an Account, deletes associated saving strategies if the account type changes.&lt;br /&gt;                Purpose: Allows for complete replacement of an Account on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer id = 56; // Integer | The existing Account ID used to identify which Account to update
    AccountModel model = new AccountModel(); // AccountModel | The Account to be updated on a Fact Finder
    try {
      AccountWithIdModel result = apiInstance.accountsPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsPutByIdModel");
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
| **id** | **Integer**| The existing Account ID used to identify which Account to update | |
| **model** | [**AccountModel**](AccountModel.md)| The Account to be updated on a Fact Finder | |

### Return type

[**AccountWithIdModel**](AccountWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsPutHoldingsByAccountidHoldings"></a>
# **accountsPutHoldingsByAccountidHoldings**
> AccountHoldingsModel accountsPutHoldingsByAccountidHoldings(accountId, holdings)



Updates all holdings associated with an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | The account with the holding to be updated
    AccountHoldingsWithoutIdModel holdings = new AccountHoldingsWithoutIdModel(); // AccountHoldingsWithoutIdModel | The list of holdings for an account
    try {
      AccountHoldingsModel result = apiInstance.accountsPutHoldingsByAccountidHoldings(accountId, holdings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsPutHoldingsByAccountidHoldings");
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
| **accountId** | **Integer**| The account with the holding to be updated | |
| **holdings** | [**AccountHoldingsWithoutIdModel**](AccountHoldingsWithoutIdModel.md)| The list of holdings for an account | |

### Return type

[**AccountHoldingsModel**](AccountHoldingsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

<a id="accountsPutSavingsStrategyByAccountidIdSavingsstrategy"></a>
# **accountsPutSavingsStrategyByAccountidIdSavingsstrategy**
> SavingsStrategyWithIdModel accountsPutSavingsStrategyByAccountidIdSavingsstrategy(accountId, id, savingsStrategy)



Updates a specific savings strategy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer accountId = 56; // Integer | Id of the account that holds the savings strategy
    Integer id = 56; // Integer | Id of the savings strategy to update
    SavingsStrategyModel savingsStrategy = new SavingsStrategyModel(); // SavingsStrategyModel | The model with which to update the savings strategy with
    try {
      SavingsStrategyWithIdModel result = apiInstance.accountsPutSavingsStrategyByAccountidIdSavingsstrategy(accountId, id, savingsStrategy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsPutSavingsStrategyByAccountidIdSavingsstrategy");
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
| **accountId** | **Integer**| Id of the account that holds the savings strategy | |
| **id** | **Integer**| Id of the savings strategy to update | |
| **savingsStrategy** | [**SavingsStrategyModel**](SavingsStrategyModel.md)| The model with which to update the savings strategy with | |

### Return type

[**SavingsStrategyWithIdModel**](SavingsStrategyWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Account data access. |  -  |
| **403** | Request is restricted for access to Account. |  -  |
| **404** | Account not found. |  -  |

