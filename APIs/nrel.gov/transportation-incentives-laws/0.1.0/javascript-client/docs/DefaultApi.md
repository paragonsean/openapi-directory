# TransportationLawsAndIncentives.DefaultApi

All URIs are relative to *http://localhost/api/transportation-incentives-laws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transportationIncentivesLawsAll**](DefaultApi.md#transportationIncentivesLawsAll) | **GET** /v1.{output_format} | Return a full list of laws and incentives that match your query.
[**transportationIncentivesLawsCategories**](DefaultApi.md#transportationIncentivesLawsCategories) | **GET** /v1/category-list.{output_format} | Return the law categories for a given category type.
[**transportationIncentivesLawsId**](DefaultApi.md#transportationIncentivesLawsId) | **GET** /v1/{id}.{output_format} | Fetch the details of a specific law given the law&#39;s ID.
[**transportationIncentivesLawsPocs**](DefaultApi.md#transportationIncentivesLawsPocs) | **GET** /v1/pocs.{output_format} | Get the points of contact for a given jurisdiction.



## transportationIncentivesLawsAll

> LawsResponse transportationIncentivesLawsAll(outputFormat, apiKey, opts)

Return a full list of laws and incentives that match your query.



### Example

```javascript
import TransportationLawsAndIncentives from 'transportation_laws_and_incentives';

let apiInstance = new TransportationLawsAndIncentives.DefaultApi();
let outputFormat = "'json'"; // String | Response format
let apiKey = "'DEMO_KEY'"; // String | API Key
let opts = {
  'limit': 10, // Number | Limit the number of laws returned
  'jurisdiction': "jurisdiction_example", // String | Return laws for the given Jurisdiction. Jurisdiction must be given as a two character state code (eg, 'CO' for Colorado). A single jurisdiction, or a comma-separate list of multiple jurisdiction, may be given.  Use the code 'US' for federal laws and the code 'DC' for Washington D.C.
  'technology': "technology_example", // String | Search by the technology type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: 'BIOD' for Biodiesel, 'ETH' for Ethanol / Flexible Fuel Vehicles, 'NG' for Natural Gas / Natural Gas Vehicles, 'LPG' for Liquefied Petroleum Gas (Propane) / Propane Vehicles, 'HY' for Hydrogen / Fuel Cell Electric Vehicles, 'ELEC' for All-Electric Vehicles (EVs), 'PHEV' for Plug-In Hybrid Electric Vehicles (PHEVs), 'HEV' for Hybrid Electric Vehicles (HEVs), 'NEVS' for Neighborhood Electric Vehicles (NEVs), 'RD' for Renewable Diesel, 'AFTMKTCONV' for Aftermarket Conversions, 'EFFEC' for Fuel Economy / Efficiency, 'IR' for Idle Reduction, 'AUTONOMOUS' for Connected and Autonomous Vehicles, and 'OTHER' for Other.
  'incentiveType': "incentiveType_example", // String | Search by the incentive type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: 'GNT' for Grants, 'TAX' for Tax Incentives, 'LOANS' for Loans and Leases, 'RBATE' for Rebates, 'EXEM' for Exemptions, 'TOU' for Time-of-Use Rate, and 'OTHER' for Other.
  'regulationType': "regulationType_example", // String | Search by the regulation type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: 'REQ' for Acquisition / Fuel Use, 'DREST' for Driving / Idling, 'REGIS' for Registration / Licensing, 'EVFEE' for EV Registration Fee, 'FUEL' for Fuel Taxes, 'STD' for Fuel Production / Quality, 'RFS' for Renewable Fuel Standard / Mandate, 'AIRQEMISSIONS' for Air Quality / Emissions, 'CCEINIT' for Climate Change / Energy Initiatives, 'UTILITY' for Utility Definition, 'BUILD' for Building Codes, 'RTC' for Right-to-Charge, and 'OTHER' for Other.
  'userType': "userType_example", // String | Search by the user type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: 'FLEET' for Commercial, 'GOV' for Government Entity, 'TRIBAL' for Tribal Government, 'IND' for Personal Vehicle Owner or Driver, 'STATION' for Alternative Fuel Infrastructure Operator, 'AFP' for Alternative Fuel Producer, 'PURCH' for Alternative Fuel Purchaser, 'MAN' for Alternative Fuel Vehicle (AFV) Manufacturer or Retrofitter, 'MUD' for Multi-Unit Dwelling, 'TRANS' for Transit, and 'OTHER' for Other.
  'poc': false, // Boolean | Include points of contacts in the return value.
  'recent': false, // Boolean | Return only recently added or updated laws and incentives
  'expired': false, // Boolean | The 'true' value returns only expired, repealed, or archived laws and incentives. The default 'false' value returns only current laws and incentives.
  'lawType': "lawType_example", // String | Search by the law type. A single type, or a comma-separate list of multiple types, may be given. Values are as follows: 'STATEINC' for State Incentives, 'UPINC ' for Utility/Private Incentives, 'LAWREG' for Laws and Regulations, 'INC' for Incentives, 'PROG' for Programs, 'LUP' for Last Updated, 'OVIEW' for Overview, and 'HILITE' for Highlights.
  'keyword': "keyword_example", // String | Search laws by keyword in title or text.
  'local': false // Boolean | Show only local examples of laws and incentives.
};
apiInstance.transportationIncentivesLawsAll(outputFormat, apiKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Response format | [default to &#39;json&#39;]
 **apiKey** | **String**| API Key | [default to &#39;DEMO_KEY&#39;]
 **limit** | **Number**| Limit the number of laws returned | [optional] [default to 10]
 **jurisdiction** | **String**| Return laws for the given Jurisdiction. Jurisdiction must be given as a two character state code (eg, &#39;CO&#39; for Colorado). A single jurisdiction, or a comma-separate list of multiple jurisdiction, may be given.  Use the code &#39;US&#39; for federal laws and the code &#39;DC&#39; for Washington D.C. | [optional] 
 **technology** | **String**| Search by the technology type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: &#39;BIOD&#39; for Biodiesel, &#39;ETH&#39; for Ethanol / Flexible Fuel Vehicles, &#39;NG&#39; for Natural Gas / Natural Gas Vehicles, &#39;LPG&#39; for Liquefied Petroleum Gas (Propane) / Propane Vehicles, &#39;HY&#39; for Hydrogen / Fuel Cell Electric Vehicles, &#39;ELEC&#39; for All-Electric Vehicles (EVs), &#39;PHEV&#39; for Plug-In Hybrid Electric Vehicles (PHEVs), &#39;HEV&#39; for Hybrid Electric Vehicles (HEVs), &#39;NEVS&#39; for Neighborhood Electric Vehicles (NEVs), &#39;RD&#39; for Renewable Diesel, &#39;AFTMKTCONV&#39; for Aftermarket Conversions, &#39;EFFEC&#39; for Fuel Economy / Efficiency, &#39;IR&#39; for Idle Reduction, &#39;AUTONOMOUS&#39; for Connected and Autonomous Vehicles, and &#39;OTHER&#39; for Other. | [optional] 
 **incentiveType** | **String**| Search by the incentive type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: &#39;GNT&#39; for Grants, &#39;TAX&#39; for Tax Incentives, &#39;LOANS&#39; for Loans and Leases, &#39;RBATE&#39; for Rebates, &#39;EXEM&#39; for Exemptions, &#39;TOU&#39; for Time-of-Use Rate, and &#39;OTHER&#39; for Other. | [optional] 
 **regulationType** | **String**| Search by the regulation type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: &#39;REQ&#39; for Acquisition / Fuel Use, &#39;DREST&#39; for Driving / Idling, &#39;REGIS&#39; for Registration / Licensing, &#39;EVFEE&#39; for EV Registration Fee, &#39;FUEL&#39; for Fuel Taxes, &#39;STD&#39; for Fuel Production / Quality, &#39;RFS&#39; for Renewable Fuel Standard / Mandate, &#39;AIRQEMISSIONS&#39; for Air Quality / Emissions, &#39;CCEINIT&#39; for Climate Change / Energy Initiatives, &#39;UTILITY&#39; for Utility Definition, &#39;BUILD&#39; for Building Codes, &#39;RTC&#39; for Right-to-Charge, and &#39;OTHER&#39; for Other. | [optional] 
 **userType** | **String**| Search by the user type. A single type, or a comma-separate list of multiple types, may be given. Values and what they stand for are as follows: &#39;FLEET&#39; for Commercial, &#39;GOV&#39; for Government Entity, &#39;TRIBAL&#39; for Tribal Government, &#39;IND&#39; for Personal Vehicle Owner or Driver, &#39;STATION&#39; for Alternative Fuel Infrastructure Operator, &#39;AFP&#39; for Alternative Fuel Producer, &#39;PURCH&#39; for Alternative Fuel Purchaser, &#39;MAN&#39; for Alternative Fuel Vehicle (AFV) Manufacturer or Retrofitter, &#39;MUD&#39; for Multi-Unit Dwelling, &#39;TRANS&#39; for Transit, and &#39;OTHER&#39; for Other. | [optional] 
 **poc** | **Boolean**| Include points of contacts in the return value. | [optional] [default to false]
 **recent** | **Boolean**| Return only recently added or updated laws and incentives | [optional] [default to false]
 **expired** | **Boolean**| The &#39;true&#39; value returns only expired, repealed, or archived laws and incentives. The default &#39;false&#39; value returns only current laws and incentives. | [optional] [default to false]
 **lawType** | **String**| Search by the law type. A single type, or a comma-separate list of multiple types, may be given. Values are as follows: &#39;STATEINC&#39; for State Incentives, &#39;UPINC &#39; for Utility/Private Incentives, &#39;LAWREG&#39; for Laws and Regulations, &#39;INC&#39; for Incentives, &#39;PROG&#39; for Programs, &#39;LUP&#39; for Last Updated, &#39;OVIEW&#39; for Overview, and &#39;HILITE&#39; for Highlights. | [optional] 
 **keyword** | **String**| Search laws by keyword in title or text. | [optional] 
 **local** | **Boolean**| Show only local examples of laws and incentives. | [optional] [default to false]

### Return type

[**LawsResponse**](LawsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## transportationIncentivesLawsCategories

> CategoryResults transportationIncentivesLawsCategories(outputFormat, apiKey, opts)

Return the law categories for a given category type.



### Example

```javascript
import TransportationLawsAndIncentives from 'transportation_laws_and_incentives';

let apiInstance = new TransportationLawsAndIncentives.DefaultApi();
let outputFormat = "'json'"; // String | Response format
let apiKey = "'DEMO_KEY'"; // String | API Key
let opts = {
  'type': "type_example" // String | Search by the category type.
};
apiInstance.transportationIncentivesLawsCategories(outputFormat, apiKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Response format | [default to &#39;json&#39;]
 **apiKey** | **String**| API Key | [default to &#39;DEMO_KEY&#39;]
 **type** | **String**| Search by the category type. | [optional] 

### Return type

[**CategoryResults**](CategoryResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## transportationIncentivesLawsId

> LawResult transportationIncentivesLawsId(outputFormat, apiKey, id, opts)

Fetch the details of a specific law given the law&#39;s ID.



### Example

```javascript
import TransportationLawsAndIncentives from 'transportation_laws_and_incentives';

let apiInstance = new TransportationLawsAndIncentives.DefaultApi();
let outputFormat = "'json'"; // String | Response format
let apiKey = "'DEMO_KEY'"; // String | API Key
let id = 56; // Number | The id of the law that you are searching
let opts = {
  'poc': false, // Boolean | Include points of contacts in the return value.
  'expired': false // Boolean | The 'true' value returns a record no matter its status (current, expired, archived, or repealed). The default 'false' value returns only current laws and incentives.
};
apiInstance.transportationIncentivesLawsId(outputFormat, apiKey, id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Response format | [default to &#39;json&#39;]
 **apiKey** | **String**| API Key | [default to &#39;DEMO_KEY&#39;]
 **id** | **Number**| The id of the law that you are searching | 
 **poc** | **Boolean**| Include points of contacts in the return value. | [optional] [default to false]
 **expired** | **Boolean**| The &#39;true&#39; value returns a record no matter its status (current, expired, archived, or repealed). The default &#39;false&#39; value returns only current laws and incentives. | [optional] [default to false]

### Return type

[**LawResult**](LawResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## transportationIncentivesLawsPocs

> PocResults transportationIncentivesLawsPocs(outputFormat, apiKey, jurisdiction)

Get the points of contact for a given jurisdiction.



### Example

```javascript
import TransportationLawsAndIncentives from 'transportation_laws_and_incentives';

let apiInstance = new TransportationLawsAndIncentives.DefaultApi();
let outputFormat = "'json'"; // String | Response format
let apiKey = "'DEMO_KEY'"; // String | API Key
let jurisdiction = "jurisdiction_example"; // String | Return the points of contact for the given Jurisdiction. Jurisdiction must be given as a two character state code (eg, 'CO' for Colorado). A single jurisdiction, or a comma-separate list of multiple jurisdiction, may be given.  Use the code 'US' for federal laws and the code 'DC' for Washington D.C.
apiInstance.transportationIncentivesLawsPocs(outputFormat, apiKey, jurisdiction, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outputFormat** | **String**| Response format | [default to &#39;json&#39;]
 **apiKey** | **String**| API Key | [default to &#39;DEMO_KEY&#39;]
 **jurisdiction** | **String**| Return the points of contact for the given Jurisdiction. Jurisdiction must be given as a two character state code (eg, &#39;CO&#39; for Colorado). A single jurisdiction, or a comma-separate list of multiple jurisdiction, may be given.  Use the code &#39;US&#39; for federal laws and the code &#39;DC&#39; for Washington D.C. | 

### Return type

[**PocResults**](PocResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

