# GeodesystemsCom443.TypeConstructionPermitsApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchConstructionPermits**](TypeConstructionPermitsApi.md#searchConstructionPermits) | **GET** /repository/search/type/construction_permits | Search API for &#39;Construction Permits&#39; entry type



## searchConstructionPermits

> searchConstructionPermits(opts)

Search API for &#39;Construction Permits&#39; entry type

API to search for entries of type Construction Permits

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeConstructionPermitsApi();
let opts = {
  'text': "text_example", // String | Search text
  'name': "name_example", // String | Search name
  'description': "description_example", // String | Search description
  'fromdate': new Date("2013-10-20T19:20:30+01:00"), // Date | From date
  'todate': new Date("2013-10-20T19:20:30+01:00"), // Date | To date
  'createdateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive create date from
  'createdateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive create date to
  'changedateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive change date from
  'changedateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive change date to
  'group': "group_example", // String | Parent entry
  'filesuffix': "filesuffix_example", // String | File suffix
  'maxlatitude': 3.4, // Number | Northern bounds of search
  'minlongitude': 3.4, // Number | Western bounds of search
  'minlatitude': 3.4, // Number | Southern bounds of search
  'maxlongitude': 3.4, // Number | Eastern bounds of search
  'max': 56, // Number | Max number of results
  'skip': 56, // Number | Number to skip
  'searchDbConstructionPermitsAddress': "searchDbConstructionPermitsAddress_example", // String | Address
  'searchDbConstructionPermitsCaseStatus': "searchDbConstructionPermitsCaseStatus_example", // String | Case Status
  'searchDbConstructionPermitsCategory': "searchDbConstructionPermitsCategory_example", // String | Category
  'searchDbConstructionPermitsBuildingUsesAndWorkScopes': "searchDbConstructionPermitsBuildingUsesAndWorkScopes_example", // String | Building Uses And Work Scopes
  'searchDbConstructionPermitsPermitTypes': "searchDbConstructionPermitsPermitTypes_example", // String | Permit Types
  'searchDbConstructionPermitsTotalProjectValue': 3.4, // Number | Total Project Value
  'searchDbConstructionPermitsTotalSubpermitValue': 3.4, // Number | Total Subpermit Value
  'searchDbConstructionPermitsApplied': "searchDbConstructionPermitsApplied_example", // String | Applied
  'searchDbConstructionPermitsApproved': "searchDbConstructionPermitsApproved_example", // String | Approved
  'searchDbConstructionPermitsIssued': "searchDbConstructionPermitsIssued_example", // String | Issued
  'searchDbConstructionPermitsCoDate': "searchDbConstructionPermitsCoDate_example", // String | Co Date
  'searchDbConstructionPermitsCompletionDate': "searchDbConstructionPermitsCompletionDate_example", // String | Completion Date
  'searchDbConstructionPermitsNewResUnit': 56, // Number | New Res Unit
  'searchDbConstructionPermitsExistingResUnit': 56, // Number | Existing Res Unit
  'searchDbConstructionPermitsAffordableHsgUnit': 56, // Number | Affordable Hsg Unit
  'searchDbConstructionPermitsNewSf': 56, // Number | New Sf
  'searchDbConstructionPermitsRemodelSf': 56, // Number | Remodel Sf
  'searchDbConstructionPermitsNarrativeDescription': "searchDbConstructionPermitsNarrativeDescription_example", // String | Narrative Description
  'searchDbConstructionPermitsPrimaryFirstName': "searchDbConstructionPermitsPrimaryFirstName_example", // String | Primary First Name
  'searchDbConstructionPermitsPrimaryLastName': "searchDbConstructionPermitsPrimaryLastName_example", // String | Primary Last Name
  'searchDbConstructionPermitsPrimaryCompany': "searchDbConstructionPermitsPrimaryCompany_example", // String | Primary Company
  'searchDbConstructionPermitsContractorFirstName': "searchDbConstructionPermitsContractorFirstName_example", // String | Contractor First Name
  'searchDbConstructionPermitsContractorLastName': "searchDbConstructionPermitsContractorLastName_example", // String | Contractor Last Name
  'searchDbConstructionPermitsContractorCompany': "searchDbConstructionPermitsContractorCompany_example", // String | Contractor Company
  'searchDbConstructionPermitsOwner1FirstName': "searchDbConstructionPermitsOwner1FirstName_example", // String | Owner1 First Name
  'searchDbConstructionPermitsOwner1LastName': "searchDbConstructionPermitsOwner1LastName_example", // String | Owner1 Last Name
  'searchDbConstructionPermitsOwner1Company': "searchDbConstructionPermitsOwner1Company_example", // String | Owner1 Company
  'searchDbConstructionPermitsOwner2FirstName': "searchDbConstructionPermitsOwner2FirstName_example", // String | Owner2 First Name
  'searchDbConstructionPermitsOwner2LastName': "searchDbConstructionPermitsOwner2LastName_example", // String | Owner2 Last Name
  'searchDbConstructionPermitsOwner2Company': "searchDbConstructionPermitsOwner2Company_example" // String | Owner2 Company
};
apiInstance.searchConstructionPermits(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **String**| Search text | [optional] 
 **name** | **String**| Search name | [optional] 
 **description** | **String**| Search description | [optional] 
 **fromdate** | **Date**| From date | [optional] 
 **todate** | **Date**| To date | [optional] 
 **createdateFrom** | **Date**| Archive create date from | [optional] 
 **createdateTo** | **Date**| Archive create date to | [optional] 
 **changedateFrom** | **Date**| Archive change date from | [optional] 
 **changedateTo** | **Date**| Archive change date to | [optional] 
 **group** | **String**| Parent entry | [optional] 
 **filesuffix** | **String**| File suffix | [optional] 
 **maxlatitude** | **Number**| Northern bounds of search | [optional] 
 **minlongitude** | **Number**| Western bounds of search | [optional] 
 **minlatitude** | **Number**| Southern bounds of search | [optional] 
 **maxlongitude** | **Number**| Eastern bounds of search | [optional] 
 **max** | **Number**| Max number of results | [optional] 
 **skip** | **Number**| Number to skip | [optional] 
 **searchDbConstructionPermitsAddress** | **String**| Address | [optional] 
 **searchDbConstructionPermitsCaseStatus** | **String**| Case Status | [optional] 
 **searchDbConstructionPermitsCategory** | **String**| Category | [optional] 
 **searchDbConstructionPermitsBuildingUsesAndWorkScopes** | **String**| Building Uses And Work Scopes | [optional] 
 **searchDbConstructionPermitsPermitTypes** | **String**| Permit Types | [optional] 
 **searchDbConstructionPermitsTotalProjectValue** | **Number**| Total Project Value | [optional] 
 **searchDbConstructionPermitsTotalSubpermitValue** | **Number**| Total Subpermit Value | [optional] 
 **searchDbConstructionPermitsApplied** | **String**| Applied | [optional] 
 **searchDbConstructionPermitsApproved** | **String**| Approved | [optional] 
 **searchDbConstructionPermitsIssued** | **String**| Issued | [optional] 
 **searchDbConstructionPermitsCoDate** | **String**| Co Date | [optional] 
 **searchDbConstructionPermitsCompletionDate** | **String**| Completion Date | [optional] 
 **searchDbConstructionPermitsNewResUnit** | **Number**| New Res Unit | [optional] 
 **searchDbConstructionPermitsExistingResUnit** | **Number**| Existing Res Unit | [optional] 
 **searchDbConstructionPermitsAffordableHsgUnit** | **Number**| Affordable Hsg Unit | [optional] 
 **searchDbConstructionPermitsNewSf** | **Number**| New Sf | [optional] 
 **searchDbConstructionPermitsRemodelSf** | **Number**| Remodel Sf | [optional] 
 **searchDbConstructionPermitsNarrativeDescription** | **String**| Narrative Description | [optional] 
 **searchDbConstructionPermitsPrimaryFirstName** | **String**| Primary First Name | [optional] 
 **searchDbConstructionPermitsPrimaryLastName** | **String**| Primary Last Name | [optional] 
 **searchDbConstructionPermitsPrimaryCompany** | **String**| Primary Company | [optional] 
 **searchDbConstructionPermitsContractorFirstName** | **String**| Contractor First Name | [optional] 
 **searchDbConstructionPermitsContractorLastName** | **String**| Contractor Last Name | [optional] 
 **searchDbConstructionPermitsContractorCompany** | **String**| Contractor Company | [optional] 
 **searchDbConstructionPermitsOwner1FirstName** | **String**| Owner1 First Name | [optional] 
 **searchDbConstructionPermitsOwner1LastName** | **String**| Owner1 Last Name | [optional] 
 **searchDbConstructionPermitsOwner1Company** | **String**| Owner1 Company | [optional] 
 **searchDbConstructionPermitsOwner2FirstName** | **String**| Owner2 First Name | [optional] 
 **searchDbConstructionPermitsOwner2LastName** | **String**| Owner2 Last Name | [optional] 
 **searchDbConstructionPermitsOwner2Company** | **String**| Owner2 Company | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

