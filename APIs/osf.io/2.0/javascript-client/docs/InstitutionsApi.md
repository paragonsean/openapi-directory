# OsfApiv2Documentation.InstitutionsApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**institutionsDetail**](InstitutionsApi.md#institutionsDetail) | **GET** /institutions/{institution_id}/ | Retrieve an institution
[**institutionsList**](InstitutionsApi.md#institutionsList) | **GET** /institutions/ | List all institutions
[**institutionsNodeList**](InstitutionsApi.md#institutionsNodeList) | **GET** /institutions/{institution_id}/nodes/ | List all affiliated nodes
[**institutionsRegistrationList**](InstitutionsApi.md#institutionsRegistrationList) | **GET** /institutions/{institution_id}/registrations/ | List all affiliated registrations
[**institutionsUsersList**](InstitutionsApi.md#institutionsUsersList) | **GET** /institutions/{institution_id}/users/ | List all affiliated users



## institutionsDetail

> [Institution] institutionsDetail(institutionId)

Retrieve an institution

Retrieves the details of an institution #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested institution, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.InstitutionsApi();
let institutionId = "institutionId_example"; // String | The unique identifier of the institution you wish to retrieve.
apiInstance.institutionsDetail(institutionId, (error, data, response) => {
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
 **institutionId** | **String**| The unique identifier of the institution you wish to retrieve. | 

### Return type

[**[Institution]**](Institution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## institutionsList

> [Institution] institutionsList()

List all institutions

 A paginated list of all verified institutions. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 institutions. Each resource in the array is a separate institution object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include institutions that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/?filter[id]&#x3D;cos.  Institutions may be filtered by their &#x60;id&#x60;, &#x60;name&#x60;, and &#x60;auth_url&#x60;

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.InstitutionsApi();
apiInstance.institutionsList((error, data, response) => {
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

[**[Institution]**](Institution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## institutionsNodeList

> [Node] institutionsNodeList(institutionId)

List all affiliated nodes

A paginated list of all nodes affiliated with an institution. #### Versioning As of version &#x60;2.2&#x60;, affiliated components (in addition to affiliated top-level projects) are returned from this endpoint. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 nodes. Each resource in the array is a separate nodes object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/cos/nodes?filter[title]&#x3D;science.  Nodes may be filtered by their &#x60;id&#x60;, &#x60;title&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;tags&#x60;, &#x60;category&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, &#x60;root&#x60;, &#x60;parent&#x60;, &#x60;contributors&#x60;, and &#x60;preprint&#x60;

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.InstitutionsApi();
let institutionId = "institutionId_example"; // String | The unique identifier of the institution you wish to retrieve.
apiInstance.institutionsNodeList(institutionId, (error, data, response) => {
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
 **institutionId** | **String**| The unique identifier of the institution you wish to retrieve. | 

### Return type

[**[Node]**](Node.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## institutionsRegistrationList

> institutionsRegistrationList(institutionId)

List all affiliated registrations

A paginated list of all registrations affiliated with an institution. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 registrations. Each resource in the array is a separate users object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include registrations that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/cos/registrations?filter[title]&#x3D;science.  Registrations may be filtered by their  &#x60;id&#x60;, &#x60;title&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;tags&#x60;, &#x60;category&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, &#x60;root&#x60;, &#x60;parent&#x60;, &#x60;contributors&#x60;, and &#x60;preprint&#x60;

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.InstitutionsApi();
let institutionId = "institutionId_example"; // String | The unique identifier of the institution you wish to retrieve.
apiInstance.institutionsRegistrationList(institutionId, (error, data, response) => {
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
 **institutionId** | **String**| The unique identifier of the institution you wish to retrieve. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## institutionsUsersList

> [User] institutionsUsersList(institutionId)

List all affiliated users

A paginated list of all users affiliated with an institution. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 users. Each resource in the array is a separate users object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include users that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/institutions/cos/users?filter[family_name]&#x3D;Nosek.  Users may be filtered by their &#x60;id&#x60;, &#x60;full_name&#x60;, &#x60;given_name&#x60;, &#x60;middle_names&#x60;, and &#x60;family_name&#x60;

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.InstitutionsApi();
let institutionId = "institutionId_example"; // String | The unique identifier of the institution you wish to retrieve.
apiInstance.institutionsUsersList(institutionId, (error, data, response) => {
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
 **institutionId** | **String**| The unique identifier of the institution you wish to retrieve. | 

### Return type

[**[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

