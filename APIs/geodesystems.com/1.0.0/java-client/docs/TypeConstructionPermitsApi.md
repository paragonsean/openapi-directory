# TypeConstructionPermitsApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchConstructionPermits**](TypeConstructionPermitsApi.md#searchConstructionPermits) | **GET** /repository/search/type/construction_permits | Search API for &#39;Construction Permits&#39; entry type |


<a id="searchConstructionPermits"></a>
# **searchConstructionPermits**
> searchConstructionPermits(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbConstructionPermitsAddress, searchDbConstructionPermitsCaseStatus, searchDbConstructionPermitsCategory, searchDbConstructionPermitsBuildingUsesAndWorkScopes, searchDbConstructionPermitsPermitTypes, searchDbConstructionPermitsTotalProjectValue, searchDbConstructionPermitsTotalSubpermitValue, searchDbConstructionPermitsApplied, searchDbConstructionPermitsApproved, searchDbConstructionPermitsIssued, searchDbConstructionPermitsCoDate, searchDbConstructionPermitsCompletionDate, searchDbConstructionPermitsNewResUnit, searchDbConstructionPermitsExistingResUnit, searchDbConstructionPermitsAffordableHsgUnit, searchDbConstructionPermitsNewSf, searchDbConstructionPermitsRemodelSf, searchDbConstructionPermitsNarrativeDescription, searchDbConstructionPermitsPrimaryFirstName, searchDbConstructionPermitsPrimaryLastName, searchDbConstructionPermitsPrimaryCompany, searchDbConstructionPermitsContractorFirstName, searchDbConstructionPermitsContractorLastName, searchDbConstructionPermitsContractorCompany, searchDbConstructionPermitsOwner1FirstName, searchDbConstructionPermitsOwner1LastName, searchDbConstructionPermitsOwner1Company, searchDbConstructionPermitsOwner2FirstName, searchDbConstructionPermitsOwner2LastName, searchDbConstructionPermitsOwner2Company)

Search API for &#39;Construction Permits&#39; entry type

API to search for entries of type Construction Permits

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeConstructionPermitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeConstructionPermitsApi apiInstance = new TypeConstructionPermitsApi(defaultClient);
    String text = "text_example"; // String | Search text
    String name = "name_example"; // String | Search name
    String description = "description_example"; // String | Search description
    OffsetDateTime fromdate = OffsetDateTime.now(); // OffsetDateTime | From date
    OffsetDateTime todate = OffsetDateTime.now(); // OffsetDateTime | To date
    OffsetDateTime createdateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive create date from
    OffsetDateTime createdateTo = OffsetDateTime.now(); // OffsetDateTime | Archive create date to
    OffsetDateTime changedateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive change date from
    OffsetDateTime changedateTo = OffsetDateTime.now(); // OffsetDateTime | Archive change date to
    String group = "group_example"; // String | Parent entry
    String filesuffix = "filesuffix_example"; // String | File suffix
    Float maxlatitude = 3.4F; // Float | Northern bounds of search
    Float minlongitude = 3.4F; // Float | Western bounds of search
    Float minlatitude = 3.4F; // Float | Southern bounds of search
    Float maxlongitude = 3.4F; // Float | Eastern bounds of search
    Integer max = 56; // Integer | Max number of results
    Integer skip = 56; // Integer | Number to skip
    String searchDbConstructionPermitsAddress = "searchDbConstructionPermitsAddress_example"; // String | Address
    String searchDbConstructionPermitsCaseStatus = "searchDbConstructionPermitsCaseStatus_example"; // String | Case Status
    String searchDbConstructionPermitsCategory = "searchDbConstructionPermitsCategory_example"; // String | Category
    String searchDbConstructionPermitsBuildingUsesAndWorkScopes = "searchDbConstructionPermitsBuildingUsesAndWorkScopes_example"; // String | Building Uses And Work Scopes
    String searchDbConstructionPermitsPermitTypes = "searchDbConstructionPermitsPermitTypes_example"; // String | Permit Types
    Double searchDbConstructionPermitsTotalProjectValue = 3.4D; // Double | Total Project Value
    Double searchDbConstructionPermitsTotalSubpermitValue = 3.4D; // Double | Total Subpermit Value
    String searchDbConstructionPermitsApplied = "searchDbConstructionPermitsApplied_example"; // String | Applied
    String searchDbConstructionPermitsApproved = "searchDbConstructionPermitsApproved_example"; // String | Approved
    String searchDbConstructionPermitsIssued = "searchDbConstructionPermitsIssued_example"; // String | Issued
    String searchDbConstructionPermitsCoDate = "searchDbConstructionPermitsCoDate_example"; // String | Co Date
    String searchDbConstructionPermitsCompletionDate = "searchDbConstructionPermitsCompletionDate_example"; // String | Completion Date
    Integer searchDbConstructionPermitsNewResUnit = 56; // Integer | New Res Unit
    Integer searchDbConstructionPermitsExistingResUnit = 56; // Integer | Existing Res Unit
    Integer searchDbConstructionPermitsAffordableHsgUnit = 56; // Integer | Affordable Hsg Unit
    Integer searchDbConstructionPermitsNewSf = 56; // Integer | New Sf
    Integer searchDbConstructionPermitsRemodelSf = 56; // Integer | Remodel Sf
    String searchDbConstructionPermitsNarrativeDescription = "searchDbConstructionPermitsNarrativeDescription_example"; // String | Narrative Description
    String searchDbConstructionPermitsPrimaryFirstName = "searchDbConstructionPermitsPrimaryFirstName_example"; // String | Primary First Name
    String searchDbConstructionPermitsPrimaryLastName = "searchDbConstructionPermitsPrimaryLastName_example"; // String | Primary Last Name
    String searchDbConstructionPermitsPrimaryCompany = "searchDbConstructionPermitsPrimaryCompany_example"; // String | Primary Company
    String searchDbConstructionPermitsContractorFirstName = "searchDbConstructionPermitsContractorFirstName_example"; // String | Contractor First Name
    String searchDbConstructionPermitsContractorLastName = "searchDbConstructionPermitsContractorLastName_example"; // String | Contractor Last Name
    String searchDbConstructionPermitsContractorCompany = "searchDbConstructionPermitsContractorCompany_example"; // String | Contractor Company
    String searchDbConstructionPermitsOwner1FirstName = "searchDbConstructionPermitsOwner1FirstName_example"; // String | Owner1 First Name
    String searchDbConstructionPermitsOwner1LastName = "searchDbConstructionPermitsOwner1LastName_example"; // String | Owner1 Last Name
    String searchDbConstructionPermitsOwner1Company = "searchDbConstructionPermitsOwner1Company_example"; // String | Owner1 Company
    String searchDbConstructionPermitsOwner2FirstName = "searchDbConstructionPermitsOwner2FirstName_example"; // String | Owner2 First Name
    String searchDbConstructionPermitsOwner2LastName = "searchDbConstructionPermitsOwner2LastName_example"; // String | Owner2 Last Name
    String searchDbConstructionPermitsOwner2Company = "searchDbConstructionPermitsOwner2Company_example"; // String | Owner2 Company
    try {
      apiInstance.searchConstructionPermits(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbConstructionPermitsAddress, searchDbConstructionPermitsCaseStatus, searchDbConstructionPermitsCategory, searchDbConstructionPermitsBuildingUsesAndWorkScopes, searchDbConstructionPermitsPermitTypes, searchDbConstructionPermitsTotalProjectValue, searchDbConstructionPermitsTotalSubpermitValue, searchDbConstructionPermitsApplied, searchDbConstructionPermitsApproved, searchDbConstructionPermitsIssued, searchDbConstructionPermitsCoDate, searchDbConstructionPermitsCompletionDate, searchDbConstructionPermitsNewResUnit, searchDbConstructionPermitsExistingResUnit, searchDbConstructionPermitsAffordableHsgUnit, searchDbConstructionPermitsNewSf, searchDbConstructionPermitsRemodelSf, searchDbConstructionPermitsNarrativeDescription, searchDbConstructionPermitsPrimaryFirstName, searchDbConstructionPermitsPrimaryLastName, searchDbConstructionPermitsPrimaryCompany, searchDbConstructionPermitsContractorFirstName, searchDbConstructionPermitsContractorLastName, searchDbConstructionPermitsContractorCompany, searchDbConstructionPermitsOwner1FirstName, searchDbConstructionPermitsOwner1LastName, searchDbConstructionPermitsOwner1Company, searchDbConstructionPermitsOwner2FirstName, searchDbConstructionPermitsOwner2LastName, searchDbConstructionPermitsOwner2Company);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeConstructionPermitsApi#searchConstructionPermits");
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
| **text** | **String**| Search text | [optional] |
| **name** | **String**| Search name | [optional] |
| **description** | **String**| Search description | [optional] |
| **fromdate** | **OffsetDateTime**| From date | [optional] |
| **todate** | **OffsetDateTime**| To date | [optional] |
| **createdateFrom** | **OffsetDateTime**| Archive create date from | [optional] |
| **createdateTo** | **OffsetDateTime**| Archive create date to | [optional] |
| **changedateFrom** | **OffsetDateTime**| Archive change date from | [optional] |
| **changedateTo** | **OffsetDateTime**| Archive change date to | [optional] |
| **group** | **String**| Parent entry | [optional] |
| **filesuffix** | **String**| File suffix | [optional] |
| **maxlatitude** | **Float**| Northern bounds of search | [optional] |
| **minlongitude** | **Float**| Western bounds of search | [optional] |
| **minlatitude** | **Float**| Southern bounds of search | [optional] |
| **maxlongitude** | **Float**| Eastern bounds of search | [optional] |
| **max** | **Integer**| Max number of results | [optional] |
| **skip** | **Integer**| Number to skip | [optional] |
| **searchDbConstructionPermitsAddress** | **String**| Address | [optional] |
| **searchDbConstructionPermitsCaseStatus** | **String**| Case Status | [optional] |
| **searchDbConstructionPermitsCategory** | **String**| Category | [optional] |
| **searchDbConstructionPermitsBuildingUsesAndWorkScopes** | **String**| Building Uses And Work Scopes | [optional] |
| **searchDbConstructionPermitsPermitTypes** | **String**| Permit Types | [optional] |
| **searchDbConstructionPermitsTotalProjectValue** | **Double**| Total Project Value | [optional] |
| **searchDbConstructionPermitsTotalSubpermitValue** | **Double**| Total Subpermit Value | [optional] |
| **searchDbConstructionPermitsApplied** | **String**| Applied | [optional] |
| **searchDbConstructionPermitsApproved** | **String**| Approved | [optional] |
| **searchDbConstructionPermitsIssued** | **String**| Issued | [optional] |
| **searchDbConstructionPermitsCoDate** | **String**| Co Date | [optional] |
| **searchDbConstructionPermitsCompletionDate** | **String**| Completion Date | [optional] |
| **searchDbConstructionPermitsNewResUnit** | **Integer**| New Res Unit | [optional] |
| **searchDbConstructionPermitsExistingResUnit** | **Integer**| Existing Res Unit | [optional] |
| **searchDbConstructionPermitsAffordableHsgUnit** | **Integer**| Affordable Hsg Unit | [optional] |
| **searchDbConstructionPermitsNewSf** | **Integer**| New Sf | [optional] |
| **searchDbConstructionPermitsRemodelSf** | **Integer**| Remodel Sf | [optional] |
| **searchDbConstructionPermitsNarrativeDescription** | **String**| Narrative Description | [optional] |
| **searchDbConstructionPermitsPrimaryFirstName** | **String**| Primary First Name | [optional] |
| **searchDbConstructionPermitsPrimaryLastName** | **String**| Primary Last Name | [optional] |
| **searchDbConstructionPermitsPrimaryCompany** | **String**| Primary Company | [optional] |
| **searchDbConstructionPermitsContractorFirstName** | **String**| Contractor First Name | [optional] |
| **searchDbConstructionPermitsContractorLastName** | **String**| Contractor Last Name | [optional] |
| **searchDbConstructionPermitsContractorCompany** | **String**| Contractor Company | [optional] |
| **searchDbConstructionPermitsOwner1FirstName** | **String**| Owner1 First Name | [optional] |
| **searchDbConstructionPermitsOwner1LastName** | **String**| Owner1 Last Name | [optional] |
| **searchDbConstructionPermitsOwner1Company** | **String**| Owner1 Company | [optional] |
| **searchDbConstructionPermitsOwner2FirstName** | **String**| Owner2 First Name | [optional] |
| **searchDbConstructionPermitsOwner2LastName** | **String**| Owner2 Last Name | [optional] |
| **searchDbConstructionPermitsOwner2Company** | **String**| Owner2 Company | [optional] |

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
| **200** | No response was specified |  -  |

