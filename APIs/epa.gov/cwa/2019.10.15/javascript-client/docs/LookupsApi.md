# USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi

All URIs are relative to *https://echodata.epa.gov/echo*

Method | HTTP request | Description
------------- | ------------- | -------------
[**restLookupsBpTribesGet**](LookupsApi.md#restLookupsBpTribesGet) | **GET** /rest_lookups.bp_tribes | ECHO BP Tribes Lookup Service
[**restLookupsBpTribesPost**](LookupsApi.md#restLookupsBpTribesPost) | **POST** /rest_lookups.bp_tribes | ECHO BP Tribes Lookup Service
[**restLookupsCwaParametersGet**](LookupsApi.md#restLookupsCwaParametersGet) | **GET** /rest_lookups.cwa_parameters | ECHO CWA Parameter Lookup Service
[**restLookupsCwaParametersPost**](LookupsApi.md#restLookupsCwaParametersPost) | **POST** /rest_lookups.cwa_parameters | ECHO CWA Parameter Lookup Service
[**restLookupsCwaPollutantsGet**](LookupsApi.md#restLookupsCwaPollutantsGet) | **GET** /rest_lookups.cwa_pollutants | ECHO CWA Pollutants Lookup Service
[**restLookupsCwaPollutantsPost**](LookupsApi.md#restLookupsCwaPollutantsPost) | **POST** /rest_lookups.cwa_pollutants | ECHO CWA Pollutants Lookup Service
[**restLookupsFederalAgenciesGet**](LookupsApi.md#restLookupsFederalAgenciesGet) | **GET** /rest_lookups.federal_agencies | ECHO Federal Agency Lookup Service
[**restLookupsFederalAgenciesPost**](LookupsApi.md#restLookupsFederalAgenciesPost) | **POST** /rest_lookups.federal_agencies | ECHO Federal Agency Lookup Service
[**restLookupsIcisInspectionTypesGet**](LookupsApi.md#restLookupsIcisInspectionTypesGet) | **GET** /rest_lookups.icis_inspection_types | ECHO ICIS NPDES Inspection Types Lookup Service
[**restLookupsIcisInspectionTypesPost**](LookupsApi.md#restLookupsIcisInspectionTypesPost) | **POST** /rest_lookups.icis_inspection_types | ECHO ICIS NPDES Inspection Types Lookup Service
[**restLookupsIcisLawSectionsGet**](LookupsApi.md#restLookupsIcisLawSectionsGet) | **GET** /rest_lookups.icis_law_sections | ECHO ICIS NPDES Law Sections Lookup Service
[**restLookupsIcisLawSectionsPost**](LookupsApi.md#restLookupsIcisLawSectionsPost) | **POST** /rest_lookups.icis_law_sections | ECHO ICIS NPDES Law Sections Lookup Service
[**restLookupsNaicsCodesGet**](LookupsApi.md#restLookupsNaicsCodesGet) | **GET** /rest_lookups.naics_codes | ECHO NAICS Codes Lookup Service
[**restLookupsNaicsCodesPost**](LookupsApi.md#restLookupsNaicsCodesPost) | **POST** /rest_lookups.naics_codes | ECHO NAICS Codes Lookup Service
[**restLookupsNpdesParametersGet**](LookupsApi.md#restLookupsNpdesParametersGet) | **GET** /rest_lookups.npdes_parameters | ECHO NPDES Parameters Lookup Service
[**restLookupsNpdesParametersPost**](LookupsApi.md#restLookupsNpdesParametersPost) | **POST** /rest_lookups.npdes_parameters | ECHO NPDES Parameters Lookup Service
[**restLookupsWbdCodeLuGet**](LookupsApi.md#restLookupsWbdCodeLuGet) | **GET** /rest_lookups.wbd_code_lu | ECHO WBD Code Lookup Service
[**restLookupsWbdCodeLuPost**](LookupsApi.md#restLookupsWbdCodeLuPost) | **POST** /rest_lookups.wbd_code_lu | ECHO WBD Code Lookup Service
[**restLookupsWbdNameLuGet**](LookupsApi.md#restLookupsWbdNameLuGet) | **GET** /rest_lookups.wbd_name_lu | ECHO WBD Name Lookup Service
[**restLookupsWbdNameLuPost**](LookupsApi.md#restLookupsWbdNameLuPost) | **POST** /rest_lookups.wbd_name_lu | ECHO WBD Name Lookup Service



## restLookupsBpTribesGet

> RestLookupsBpTribesGet200Response restLookupsBpTribesGet(opts)

ECHO BP Tribes Lookup Service

Returns the EPA Standard Indian Tribes and Native Alaskan Villages tribal_id and tribe_name.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsBpTribesGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsBpTribesGet200Response**](RestLookupsBpTribesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsBpTribesPost

> RestLookupsBpTribesGet200Response restLookupsBpTribesPost(opts)

ECHO BP Tribes Lookup Service

Returns the EPA Standard Indian Tribes and Native Alaskan Villages tribal_id and tribe_name.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsBpTribesPost(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsBpTribesGet200Response**](RestLookupsBpTribesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## restLookupsCwaParametersGet

> RestLookupsCwaParametersGet200Response restLookupsCwaParametersGet(opts)

ECHO CWA Parameter Lookup Service

Look up Clean Water Act parameter codes and descriptions in the Integrated Compliance Information System - National Pollutant Discharge Elimination System (ICIS-NPDES) by code or term.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsCwaParametersGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsCwaParametersGet200Response**](RestLookupsCwaParametersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsCwaParametersPost

> RestLookupsCwaParametersGet200Response restLookupsCwaParametersPost(opts)

ECHO CWA Parameter Lookup Service

Look up Clean Water Act parameter codes and descriptions in the Integrated Compliance Information System - National Pollutant Discharge Elimination System (ICIS-NPDES) by code or term.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsCwaParametersPost(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsCwaParametersGet200Response**](RestLookupsCwaParametersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## restLookupsCwaPollutantsGet

> RestLookupsCwaPollutantsGet200Response restLookupsCwaPollutantsGet(opts)

ECHO CWA Pollutants Lookup Service

Look up Clean Water Act pollutants by name

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsCwaPollutantsGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsCwaPollutantsGet200Response**](RestLookupsCwaPollutantsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsCwaPollutantsPost

> RestLookupsCwaPollutantsGet200Response restLookupsCwaPollutantsPost(opts)

ECHO CWA Pollutants Lookup Service

Look up Clean Water Act pollutants by name

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsCwaPollutantsPost(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsCwaPollutantsGet200Response**](RestLookupsCwaPollutantsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## restLookupsFederalAgenciesGet

> RestLookupsFederalAgenciesGet200Response restLookupsFederalAgenciesGet(opts)

ECHO Federal Agency Lookup Service

Look up Federal Agency Code

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsFederalAgenciesGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsFederalAgenciesGet200Response**](RestLookupsFederalAgenciesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsFederalAgenciesPost

> RestLookupsFederalAgenciesGet200Response restLookupsFederalAgenciesPost(opts)

ECHO Federal Agency Lookup Service

Look up Federal Agency Code

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsFederalAgenciesPost(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsFederalAgenciesGet200Response**](RestLookupsFederalAgenciesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## restLookupsIcisInspectionTypesGet

> RestLookupsIcisInspectionTypesGet200Response restLookupsIcisInspectionTypesGet(opts)

ECHO ICIS NPDES Inspection Types Lookup Service

Returns the ICIS NPDES Compliance Monitoring Type Code and Description.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsIcisInspectionTypesGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsIcisInspectionTypesGet200Response**](RestLookupsIcisInspectionTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsIcisInspectionTypesPost

> RestLookupsIcisInspectionTypesGet200Response restLookupsIcisInspectionTypesPost(opts)

ECHO ICIS NPDES Inspection Types Lookup Service

Returns the ICIS NPDES Compliance Monitoring Type Code and Description.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsIcisInspectionTypesPost(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsIcisInspectionTypesGet200Response**](RestLookupsIcisInspectionTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## restLookupsIcisLawSectionsGet

> RestLookupsIcisLawSectionsGet200Response restLookupsIcisLawSectionsGet(opts)

ECHO ICIS NPDES Law Sections Lookup Service

Returns the ICIS NPDES Law Section Descriptions.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
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

ECHO ICIS NPDES Law Sections Lookup Service

Returns the ICIS NPDES Law Section Descriptions.

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
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


## restLookupsNaicsCodesGet

> RestLookupsNaicsCodesGet200Response restLookupsNaicsCodesGet(opts)

ECHO NAICS Codes Lookup Service

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsNaicsCodesGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsNaicsCodesGet200Response**](RestLookupsNaicsCodesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsNaicsCodesPost

> RestLookupsNaicsCodesGet200Response restLookupsNaicsCodesPost(opts)

ECHO NAICS Codes Lookup Service

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example", // String | Enter a partial or complete search phrase or word.
  'searchCode': "searchCode_example" // String | Enter a partial or complete code value.
};
apiInstance.restLookupsNaicsCodesPost(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 
 **searchCode** | **String**| Enter a partial or complete code value. | [optional] 

### Return type

[**RestLookupsNaicsCodesGet200Response**](RestLookupsNaicsCodesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## restLookupsNpdesParametersGet

> RestLookupsNpdesParametersGet200Response restLookupsNpdesParametersGet(opts)

ECHO NPDES Parameters Lookup Service

ICIS Limit Parameter Code and Name lookup based on the supply of a partial parameter name. (NPDES &#x3D; National Pollutant Discharge Elimination System)

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example" // String | Enter a partial or complete search phrase or word.
};
apiInstance.restLookupsNpdesParametersGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 

### Return type

[**RestLookupsNpdesParametersGet200Response**](RestLookupsNpdesParametersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsNpdesParametersPost

> RestLookupsNpdesParametersGet200Response restLookupsNpdesParametersPost(opts)

ECHO NPDES Parameters Lookup Service

ICIS Limit Parameter Code and Name lookup based on the supply of a partial parameter name. (NPDES &#x3D; National Pollutant Discharge Elimination System)

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'searchTerm': "searchTerm_example" // String | Enter a partial or complete search phrase or word.
};
apiInstance.restLookupsNpdesParametersPost(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Enter a partial or complete search phrase or word. | [optional] 

### Return type

[**RestLookupsNpdesParametersGet200Response**](RestLookupsNpdesParametersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## restLookupsWbdCodeLuGet

> RestLookupsWbdCodeLuGet200Response restLookupsWbdCodeLuGet(opts)

ECHO WBD Code Lookup Service

USGS Watershed Boundary Dataset (WBD) Name lookup based on a supplied WBD Code and Watershed Level

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'wbdCode': "wbdCode_example", // String | Two-digit watershed code [Hydrologic Unit Code (HUC)].
  'wbdLevel': "wbdLevel_example" // String | The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
};
apiInstance.restLookupsWbdCodeLuGet(opts, (error, data, response) => {
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
 **wbdCode** | **String**| Two-digit watershed code [Hydrologic Unit Code (HUC)]. | [optional] 
 **wbdLevel** | **String**| The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12. | [optional] 

### Return type

[**RestLookupsWbdCodeLuGet200Response**](RestLookupsWbdCodeLuGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsWbdCodeLuPost

> RestLookupsWbdCodeLuGet200Response restLookupsWbdCodeLuPost(opts)

ECHO WBD Code Lookup Service

USGS Watershed Boundary Dataset (WBD) Name lookup based on a supplied WBD Code and Watershed Level

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'wbdCode': "wbdCode_example", // String | Two-digit watershed code [Hydrologic Unit Code (HUC)].
  'wbdLevel': "wbdLevel_example" // String | The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
};
apiInstance.restLookupsWbdCodeLuPost(opts, (error, data, response) => {
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
 **wbdCode** | **String**| Two-digit watershed code [Hydrologic Unit Code (HUC)]. | [optional] 
 **wbdLevel** | **String**| The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12. | [optional] 

### Return type

[**RestLookupsWbdCodeLuGet200Response**](RestLookupsWbdCodeLuGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## restLookupsWbdNameLuGet

> RestLookupsWbdNameLuGet200Response restLookupsWbdNameLuGet(wbdName, opts)

ECHO WBD Name Lookup Service

USGS Watershed Boundary Dataset (WBD) Code lookup based on a supplied WBD Name and Watershed Level

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let wbdName = "wbdName_example"; // String | Watershed Name Filter.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'wbdLevel': "wbdLevel_example" // String | The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
};
apiInstance.restLookupsWbdNameLuGet(wbdName, opts, (error, data, response) => {
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
 **wbdName** | **String**| Watershed Name Filter. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **wbdLevel** | **String**| The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12. | [optional] 

### Return type

[**RestLookupsWbdNameLuGet200Response**](RestLookupsWbdNameLuGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## restLookupsWbdNameLuPost

> RestLookupsWbdNameLuGet200Response restLookupsWbdNameLuPost(wbdName, opts)

ECHO WBD Name Lookup Service

USGS Watershed Boundary Dataset (WBD) Code lookup based on a supplied WBD Name and Watershed Level

### Example

```javascript
import USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices from 'u_s__epa_enforcement_and_compliance_history_online__echo_clean_water_act__cwa_rest_services';

let apiInstance = new USEpaEnforcementAndComplianceHistoryOnlineEchoCleanWaterActCwaRestServices.LookupsApi();
let wbdName = "wbdName_example"; // String | Watershed Name Filter.
let opts = {
  'output': "output_example", // String | Output Format Flag.  Enter one of the following keywords: - JSON = Data model formatted as Javascript Object Notation (default). - JSONP = Data model formatted as Javascript Object Notation with Padding.   - XML = Data model formatted as Extensible Markup Language.
  'callback': "callback_example", // String | JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response.
  'wbdLevel': "wbdLevel_example" // String | The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12.
};
apiInstance.restLookupsWbdNameLuPost(wbdName, opts, (error, data, response) => {
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
 **wbdName** | **String**| Watershed Name Filter. | 
 **output** | **String**| Output Format Flag.  Enter one of the following keywords: - JSON &#x3D; Data model formatted as Javascript Object Notation (default). - JSONP &#x3D; Data model formatted as Javascript Object Notation with Padding.   - XML &#x3D; Data model formatted as Extensible Markup Language. | [optional] 
 **callback** | **String**| JSONP Callback.  For use with JSONP and GEOJSONP output only.  Enter a name of the function in which to wrap the JSON response. | [optional] 
 **wbdLevel** | **String**| The number of digits of the watershed code [Hydrologic Unit Code (HUC)] returned in the ValueCode. Must be an even number between 4 and 12. | [optional] 

### Return type

[**RestLookupsWbdNameLuGet200Response**](RestLookupsWbdNameLuGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

