# PresentationApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**presentationGetAccountsByFactfinderidExternalsourceid**](PresentationApi.md#presentationGetAccountsByFactfinderidExternalsourceid) | **GET** /api/Presentation/Accounts |  |
| [**presentationGetDemographicOwnersByFactfinderid**](PresentationApi.md#presentationGetDemographicOwnersByFactfinderid) | **GET** /api/Presentation/Demographics/Owners |  |
| [**presentationGetDemographicRelationships**](PresentationApi.md#presentationGetDemographicRelationships) | **GET** /api/Presentation/Demographics/Relationships |  |
| [**presentationGetIncomesByFactfinderid**](PresentationApi.md#presentationGetIncomesByFactfinderid) | **GET** /api/Presentation/Incomes |  |
| [**presentationGetLiabilitiesByFactfinderid**](PresentationApi.md#presentationGetLiabilitiesByFactfinderid) | **GET** /api/Presentation/Liabilities |  |
| [**presentationGetLifeInsurancePoliciesByFactfinderid**](PresentationApi.md#presentationGetLifeInsurancePoliciesByFactfinderid) | **GET** /api/Presentation/LifeInsurancePolicies |  |
| [**presentationGetPensionsByFactfinderid**](PresentationApi.md#presentationGetPensionsByFactfinderid) | **GET** /api/Presentation/Pensions |  |


<a id="presentationGetAccountsByFactfinderidExternalsourceid"></a>
# **presentationGetAccountsByFactfinderidExternalsourceid**
> AccountsWithSubEntitiesModel presentationGetAccountsByFactfinderidExternalsourceid(factFinderId, externalSourceId)



Description: This operation retrieves all current Accounts for the specified Fact Finder ID, as well as                             all of the holdings and savings strategies belonging to those accounts.&lt;br /&gt;                Purpose: Provides access to the Accounts in a Fact Finder as well as any sub-entities belonging to them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PresentationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    PresentationApi apiInstance = new PresentationApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Accounts
    String externalSourceId = "externalSourceId_example"; // String | The external ID used to filter Accounts
    try {
      AccountsWithSubEntitiesModel result = apiInstance.presentationGetAccountsByFactfinderidExternalsourceid(factFinderId, externalSourceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PresentationApi#presentationGetAccountsByFactfinderidExternalsourceid");
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

[**AccountsWithSubEntitiesModel**](AccountsWithSubEntitiesModel.md)

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

<a id="presentationGetDemographicOwnersByFactfinderid"></a>
# **presentationGetDemographicOwnersByFactfinderid**
> OwnersModel presentationGetDemographicOwnersByFactfinderid(factFinderId)



Description: This operation retrieves owner values for the fact finder based on demographics data                Purpose: Provides the list of valid options for owner, student, beneficiary, etc.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PresentationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    PresentationApi apiInstance = new PresentationApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve owners.
    try {
      OwnersModel result = apiInstance.presentationGetDemographicOwnersByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PresentationApi#presentationGetDemographicOwnersByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve owners. | |

### Return type

[**OwnersModel**](OwnersModel.md)

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
| **401** | Unauthorized for Demographic information data access. |  -  |
| **403** | Request is restricted for access to Demographic information. |  -  |
| **404** | Fact Finder not found. |  -  |

<a id="presentationGetDemographicRelationships"></a>
# **presentationGetDemographicRelationships**
> RelationshipTypesModel presentationGetDemographicRelationships()



Description: This operation retrieves all relationship types relevant to demographics.&lt;br /&gt;                Purpose: Provides a list of relationship types organized by whether or not they can be defined as children.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PresentationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    PresentationApi apiInstance = new PresentationApi(defaultClient);
    try {
      RelationshipTypesModel result = apiInstance.presentationGetDemographicRelationships();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PresentationApi#presentationGetDemographicRelationships");
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

[**RelationshipTypesModel**](RelationshipTypesModel.md)

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
| **404** | Object not found. |  -  |

<a id="presentationGetIncomesByFactfinderid"></a>
# **presentationGetIncomesByFactfinderid**
> IncomesModel presentationGetIncomesByFactfinderid(factFinderId)



Description: This operation retrieves all current Incomes for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Incomes in a Fact Finder, filtered by Incomes that are current.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PresentationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    PresentationApi apiInstance = new PresentationApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Incomes
    try {
      IncomesModel result = apiInstance.presentationGetIncomesByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PresentationApi#presentationGetIncomesByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Incomes | |

### Return type

[**IncomesModel**](IncomesModel.md)

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
| **401** | Unauthorized for Income data access. |  -  |
| **403** | Request is restricted for access to Income. |  -  |
| **404** | Income not found. |  -  |

<a id="presentationGetLiabilitiesByFactfinderid"></a>
# **presentationGetLiabilitiesByFactfinderid**
> LiabilitiesModel presentationGetLiabilitiesByFactfinderid(factFinderId)



Description: This operation retrieves all current Liabilities for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Liabilities in a Fact Finder, filtered by Liabilities that are current.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PresentationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    PresentationApi apiInstance = new PresentationApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Liabilities
    try {
      LiabilitiesModel result = apiInstance.presentationGetLiabilitiesByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PresentationApi#presentationGetLiabilitiesByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Liabilities | |

### Return type

[**LiabilitiesModel**](LiabilitiesModel.md)

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
| **401** | Unauthorized for Liability data access. |  -  |
| **403** | Request is restricted for access to Liability. |  -  |
| **404** | Liability not found. |  -  |

<a id="presentationGetLifeInsurancePoliciesByFactfinderid"></a>
# **presentationGetLifeInsurancePoliciesByFactfinderid**
> LifeInsurancePoliciesWithSubEntitiesModel presentationGetLifeInsurancePoliciesByFactfinderid(factFinderId)



Description: This operation retrieves all life insurance policies, including subaccounts if available, for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Life Insurance Policies in a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PresentationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    PresentationApi apiInstance = new PresentationApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Life Insurance Policies.
    try {
      LifeInsurancePoliciesWithSubEntitiesModel result = apiInstance.presentationGetLifeInsurancePoliciesByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PresentationApi#presentationGetLifeInsurancePoliciesByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Life Insurance Policies. | |

### Return type

[**LifeInsurancePoliciesWithSubEntitiesModel**](LifeInsurancePoliciesWithSubEntitiesModel.md)

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
| **401** | Unauthorized for Life Insurance Policy data access. |  -  |
| **403** | Request is restricted for access to Life Insurance Policy. |  -  |
| **404** | Life Insurance Policy not found. |  -  |

<a id="presentationGetPensionsByFactfinderid"></a>
# **presentationGetPensionsByFactfinderid**
> DefinedBenefitPensionsModel presentationGetPensionsByFactfinderid(factFinderId)



Description: This operation retrieves all future Defined Benefit Pensions for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Pensions in a Fact Finder, filtered by Pensions that are in the future.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PresentationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    PresentationApi apiInstance = new PresentationApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Pensions.
    try {
      DefinedBenefitPensionsModel result = apiInstance.presentationGetPensionsByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PresentationApi#presentationGetPensionsByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Pensions. | |

### Return type

[**DefinedBenefitPensionsModel**](DefinedBenefitPensionsModel.md)

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
| **401** | Unauthorized for Defined Benefit Pension data access. |  -  |
| **403** | Request is restricted for access to Defined Benefit Pension. |  -  |
| **404** | Defined Benefit Pension not found. |  -  |

