# Learnifier.OrganizationUnitsApi

All URIs are relative to *http://learnifier.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extorgunitGet**](OrganizationUnitsApi.md#extorgunitGet) | **GET** /extorgunit | Get Organization Unit with External Id
[**orgunitsGet**](OrganizationUnitsApi.md#orgunitsGet) | **GET** /orgunits | Organization Units
[**orgunitsOrgidGet**](OrganizationUnitsApi.md#orgunitsOrgidGet) | **GET** /orgunits/{orgid} | Get Organization Unit
[**orgunitsOrgidPatch**](OrganizationUnitsApi.md#orgunitsOrgidPatch) | **PATCH** /orgunits/{orgid} | Updates an Organization Unit
[**orgunitsPost**](OrganizationUnitsApi.md#orgunitsPost) | **POST** /orgunits | Adds an Organization Unit



## extorgunitGet

> OrgUnit extorgunitGet(extid)

Get Organization Unit with External Id

Returns information about the organization unit with the specified external id. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.OrganizationUnitsApi();
let extid = "extid_example"; // String | The external id of the organization unit
apiInstance.extorgunitGet(extid, (error, data, response) => {
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
 **extid** | **String**| The external id of the organization unit | 

### Return type

[**OrgUnit**](OrgUnit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsGet

> OrgUnits orgunitsGet()

Organization Units

The orgunits endpoint returns information about the available organization units (orgunits). The response includes the display name, internal and external id and client number. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.OrganizationUnitsApi();
apiInstance.orgunitsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**OrgUnits**](OrgUnits.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidGet

> OrgUnit orgunitsOrgidGet(orgid)

Get Organization Unit

Returns information about the specified organization unit. The response includes the display name, internal and external id and client number. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.OrganizationUnitsApi();
let orgid = 56; // Number | Id of the organization unit
apiInstance.orgunitsOrgidGet(orgid, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 

### Return type

[**OrgUnit**](OrgUnit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidPatch

> orgunitsOrgidPatch(orgid, body)

Updates an Organization Unit

Adds an Organization Unit

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.OrganizationUnitsApi();
let orgid = "orgid_example"; // String | 
let body = new Learnifier.UpdateOrganizationUnit(); // UpdateOrganizationUnit | 
apiInstance.orgunitsOrgidPatch(orgid, body, (error, data, response) => {
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
 **orgid** | **String**|  | 
 **body** | [**UpdateOrganizationUnit**](UpdateOrganizationUnit.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsPost

> AddOrganizationUnitResponse orgunitsPost(body)

Adds an Organization Unit

Adds an Organization Unit

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.OrganizationUnitsApi();
let body = new Learnifier.AddOrganizationUnit(); // AddOrganizationUnit | 
apiInstance.orgunitsPost(body, (error, data, response) => {
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
 **body** | [**AddOrganizationUnit**](AddOrganizationUnit.md)|  | 

### Return type

[**AddOrganizationUnitResponse**](AddOrganizationUnitResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

