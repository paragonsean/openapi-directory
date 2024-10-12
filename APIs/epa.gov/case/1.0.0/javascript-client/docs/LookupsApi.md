# USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.LookupsApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**restLookupsIcisLawSectionsGet**](LookupsApi.md#restLookupsIcisLawSectionsGet) | **GET** /rest_lookups.icis_law_sections | ECHO ICIS Law Sections Lookup Service
[**restLookupsIcisLawSectionsPost**](LookupsApi.md#restLookupsIcisLawSectionsPost) | **POST** /rest_lookups.icis_law_sections | ECHO ICIS Law Sections Lookup Service



## restLookupsIcisLawSectionsGet

> RestLookupsIcisLawSectionsGet200Response restLookupsIcisLawSectionsGet(opts)

ECHO ICIS Law Sections Lookup Service

Returns the ICIS Law Section Descriptions.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'statuteCode': "statuteCode_example", // String | 
  'statusFlag': "statusFlag_example", // String | 
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example", // String | Enter a partial or complete code value.
  'sortOrder': 3.4 // Number | 
};
apiInstance.restLookupsIcisLawSectionsGet(opts, (error, data, response) => {
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
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **statuteCode** | **String**|  | [optional] 
 **statusFlag** | **String**|  | [optional] 
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 
 **sortOrder** | **Number**|  | [optional] 

### Return type

[**RestLookupsIcisLawSectionsGet200Response**](RestLookupsIcisLawSectionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsIcisLawSectionsPost

> RestLookupsIcisLawSectionsGet200Response restLookupsIcisLawSectionsPost(opts)

ECHO ICIS Law Sections Lookup Service

Returns the ICIS Law Section Descriptions.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch from 'u_s__epa_enforcement_and_compliance_history_online__echo_enforcement_case_search';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoEnforcementCaseSearch.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'statuteCode': "statuteCode_example", // String | 
  'statusFlag': "statusFlag_example", // String | 
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example", // String | Enter a partial or complete code value.
  'sortOrder': 3.4 // Number | 
};
apiInstance.restLookupsIcisLawSectionsPost(opts, (error, data, response) => {
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
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **statuteCode** | **String**|  | [optional] 
 **statusFlag** | **String**|  | [optional] 
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 
 **sortOrder** | **Number**|  | [optional] 

### Return type

[**RestLookupsIcisLawSectionsGet200Response**](RestLookupsIcisLawSectionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

