# GeodesystemsCom443.TypeBolderRentalHousingApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchBolderRentalHousing**](TypeBolderRentalHousingApi.md#searchBolderRentalHousing) | **GET** /repository/search/type/bolder_rental_housing | Search API for &#39;Boulder Rental Housing&#39; entry type



## searchBolderRentalHousing

> searchBolderRentalHousing(opts)

Search API for &#39;Boulder Rental Housing&#39; entry type

API to search for entries of type Boulder Rental Housing

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeBolderRentalHousingApi();
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
  'searchDbBolderRentalHousingPropaddr1': "searchDbBolderRentalHousingPropaddr1_example", // String | Property Address
  'searchDbBolderRentalHousingRentaltype': "searchDbBolderRentalHousingRentaltype_example", // String | Rental Type
  'searchDbBolderRentalHousingBldgtype': "searchDbBolderRentalHousingBldgtype_example", // String | Building Type
  'searchDbBolderRentalHousingDwellunits': 56, // Number | Dwelling Units
  'searchDbBolderRentalHousingRoomunits': 56, // Number | Room Units
  'searchDbBolderRentalHousingNeighbrhd': "searchDbBolderRentalHousingNeighbrhd_example", // String | Neighborhood
  'searchDbBolderRentalHousingComplexnm': "searchDbBolderRentalHousingComplexnm_example", // String | Complex Name
  'searchDbBolderRentalHousingName': "searchDbBolderRentalHousingName_example", // String | Name
  'searchDbBolderRentalHousingPersontype': "searchDbBolderRentalHousingPersontype_example", // String | Person Type
  'searchDbBolderRentalHousingCompany': "searchDbBolderRentalHousingCompany_example", // String | Company
  'searchDbBolderRentalHousingEngcompl': "searchDbBolderRentalHousingEngcompl_example", // String | Engcompl
  'searchDbBolderRentalHousingLicenseexp': "searchDbBolderRentalHousingLicenseexp_example", // String | Expiration Date
  'searchDbBolderRentalHousingLicensenum': "searchDbBolderRentalHousingLicensenum_example", // String | Licensenum
  'searchDbBolderRentalHousingPpl1Coname': "searchDbBolderRentalHousingPpl1Coname_example", // String | Ppl1 Coname
  'searchDbBolderRentalHousingPerson1': "searchDbBolderRentalHousingPerson1_example", // String | Person 1
  'searchDbBolderRentalHousingPpl1Role': "searchDbBolderRentalHousingPpl1Role_example", // String | Ppl1 Role
  'searchDbBolderRentalHousingPpl2Coname': "searchDbBolderRentalHousingPpl2Coname_example", // String | Ppl2 Coname
  'searchDbBolderRentalHousingPerson2': "searchDbBolderRentalHousingPerson2_example", // String | Person 2
  'searchDbBolderRentalHousingPpl2Role': "searchDbBolderRentalHousingPpl2Role_example", // String | Ppl2 Role
  'searchDbBolderRentalHousingLocation': "searchDbBolderRentalHousingLocation_example" // String | Location
};
apiInstance.searchBolderRentalHousing(opts, (error, data, response) => {
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
 **searchDbBolderRentalHousingPropaddr1** | **String**| Property Address | [optional] 
 **searchDbBolderRentalHousingRentaltype** | **String**| Rental Type | [optional] 
 **searchDbBolderRentalHousingBldgtype** | **String**| Building Type | [optional] 
 **searchDbBolderRentalHousingDwellunits** | **Number**| Dwelling Units | [optional] 
 **searchDbBolderRentalHousingRoomunits** | **Number**| Room Units | [optional] 
 **searchDbBolderRentalHousingNeighbrhd** | **String**| Neighborhood | [optional] 
 **searchDbBolderRentalHousingComplexnm** | **String**| Complex Name | [optional] 
 **searchDbBolderRentalHousingName** | **String**| Name | [optional] 
 **searchDbBolderRentalHousingPersontype** | **String**| Person Type | [optional] 
 **searchDbBolderRentalHousingCompany** | **String**| Company | [optional] 
 **searchDbBolderRentalHousingEngcompl** | **String**| Engcompl | [optional] 
 **searchDbBolderRentalHousingLicenseexp** | **String**| Expiration Date | [optional] 
 **searchDbBolderRentalHousingLicensenum** | **String**| Licensenum | [optional] 
 **searchDbBolderRentalHousingPpl1Coname** | **String**| Ppl1 Coname | [optional] 
 **searchDbBolderRentalHousingPerson1** | **String**| Person 1 | [optional] 
 **searchDbBolderRentalHousingPpl1Role** | **String**| Ppl1 Role | [optional] 
 **searchDbBolderRentalHousingPpl2Coname** | **String**| Ppl2 Coname | [optional] 
 **searchDbBolderRentalHousingPerson2** | **String**| Person 2 | [optional] 
 **searchDbBolderRentalHousingPpl2Role** | **String**| Ppl2 Role | [optional] 
 **searchDbBolderRentalHousingLocation** | **String**| Location | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

