# OsfApiv2Documentation.PreprintsApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**preprintsBibliographicContributorsList**](PreprintsApi.md#preprintsBibliographicContributorsList) | **GET** /preprints/{preprint_id}/bibliographic_contributors/ | List all Bibliographic Contributors
[**preprintsCitationList**](PreprintsApi.md#preprintsCitationList) | **GET** /preprints/{preprint_id}/citation/ | Retrieve citation details
[**preprintsCitationRead**](PreprintsApi.md#preprintsCitationRead) | **GET** /preprints/{preprint_id}/citation/{style_id}/ | Retrieve a styled citation
[**preprintsContributorRead**](PreprintsApi.md#preprintsContributorRead) | **GET** /preprints/{preprint_id}/contributors/{user_id}/ | Retrieve a contributor
[**preprintsContributorsCreate**](PreprintsApi.md#preprintsContributorsCreate) | **POST** /preprints/{preprint_id}/contributors/ | Create a Contributor
[**preprintsContributorsList**](PreprintsApi.md#preprintsContributorsList) | **GET** /preprints/{preprint_id}/contributors/ | List all Contributors for a Preprint
[**preprintsCreate**](PreprintsApi.md#preprintsCreate) | **POST** /preprints/ | Create a preprint
[**preprintsList**](PreprintsApi.md#preprintsList) | **GET** /preprints/ | List all preprints
[**preprintsPartialUpdate**](PreprintsApi.md#preprintsPartialUpdate) | **PATCH** /preprints/{preprint_id}/ | Update a preprint
[**preprintsRead**](PreprintsApi.md#preprintsRead) | **GET** /preprints/{preprint_id}/ | Retrieve a preprint



## preprintsBibliographicContributorsList

> [Contributor1] preprintsBibliographicContributorsList(preprintId)

List all Bibliographic Contributors

A paginated list of the Preprint&#39;s Bibliographic Contributors, sorted by their index. Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor&#39;s detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the &#x60;data&#x60; key of the response.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]&#x3D;true.  Contributors may be filtered by their &#x60;bibliographic&#x60; and &#x60;permission&#x60; attributes.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.PreprintsApi();
let preprintId = "preprintId_example"; // String | The unique identifier of the preprint.
apiInstance.preprintsBibliographicContributorsList(preprintId, (error, data, response) => {
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
 **preprintId** | **String**| The unique identifier of the preprint. | 

### Return type

[**[Contributor1]**](Contributor1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## preprintsCitationList

> CitationDetail preprintsCitationList(preprintId)

Retrieve citation details

The citation details for a preprint, in CSL format. #### Returns Returns a JSON object with a &#x60;data&#x60; key that contains the representation of the details necessary for the preprint citation.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.PreprintsApi();
let preprintId = "preprintId_example"; // String | The unique identifier of the preprint whose citation you wish to retrieve.
apiInstance.preprintsCitationList(preprintId, (error, data, response) => {
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
 **preprintId** | **String**| The unique identifier of the preprint whose citation you wish to retrieve. | 

### Return type

[**CitationDetail**](CitationDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## preprintsCitationRead

> StyledCitation preprintsCitationRead(styleId, preprintId)

Retrieve a styled citation

The citation for a preprint in a specific style. #### Returns Returns a JSON object with a &#x60;data&#x60; key that contains the representation of the preprint citation, in the requested style.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.PreprintsApi();
let styleId = "styleId_example"; // String | The unique identifier of the citation style.
let preprintId = "preprintId_example"; // String | The unique identifier of the preprint.
apiInstance.preprintsCitationRead(styleId, preprintId, (error, data, response) => {
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
 **styleId** | **String**| The unique identifier of the citation style. | 
 **preprintId** | **String**| The unique identifier of the preprint. | 

### Return type

[**StyledCitation**](StyledCitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## preprintsContributorRead

> preprintsContributorRead(preprintId, userId)

Retrieve a contributor

Retrieves the details of a contributor on this Preprint. Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested contributor, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.PreprintsApi();
let preprintId = "preprintId_example"; // String | The unique identifier of the Preprint.
let userId = "userId_example"; // String | The unique identifier of the user.
apiInstance.preprintsContributorRead(preprintId, userId, (error, data, response) => {
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
 **preprintId** | **String**| The unique identifier of the Preprint. | 
 **userId** | **String**| The unique identifier of the user. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## preprintsContributorsCreate

> preprintsContributorsCreate(preprintId, contributor1)

Create a Contributor

Adds a contributor to a Preprint, effectively creating a relationship between the Preprint and a user.  Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot; contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not. #### Permissions Only project administrators can add contributors to a Preprint. #### Required A relationship object with a &#x60;data&#x60; key, containing the &#x60;users&#x60; type and valid user ID is required.  All attributes describing the relationship between the Preprint and the user are optional. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the new contributor, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.PreprintsApi();
let preprintId = "preprintId_example"; // String | The unique identifier of the Preprint.
let contributor1 = new OsfApiv2Documentation.Contributor1(); // Contributor1 | 
apiInstance.preprintsContributorsCreate(preprintId, contributor1, (error, data, response) => {
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
 **preprintId** | **String**| The unique identifier of the Preprint. | 
 **contributor1** | [**Contributor1**](Contributor1.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## preprintsContributorsList

> [Contributor1] preprintsContributorsList(preprintId)

List all Contributors for a Preprint

A paginated list of the Preprint&#39;s Contributors, sorted by their index.  Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of Contributors, the user relationship will not be exposed and the Contributor ID will be an empty string.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor&#39;s detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the &#x60;data&#x60; key of the response.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]&#x3D;true.  Contributors may be filtered by their &#x60;bibliographic&#x60; and &#x60;permission&#x60; attributes.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.PreprintsApi();
let preprintId = "preprintId_example"; // String | The unique identifier of the preprint.
apiInstance.preprintsContributorsList(preprintId, (error, data, response) => {
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
 **preprintId** | **String**| The unique identifier of the preprint. | 

### Return type

[**[Contributor1]**](Contributor1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## preprintsCreate

> preprintsCreate(preprint)

Create a preprint

Creates a new preprint. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the created preprint, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.PreprintsApi();
let preprint = new OsfApiv2Documentation.Preprint(); // Preprint | 
apiInstance.preprintsCreate(preprint, (error, data, response) => {
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
 **preprint** | [**Preprint**](Preprint.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## preprintsList

> [Preprint] preprintsList()

List all preprints

 A paginated list of preprints from all preprint providers. The returned preprints are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 preprints. Each resource in the array is a separate preprint object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include preprints that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/preprints/?filter[provider]&#x3D;socarxiv.  Preprints may be filtered by their &#x60;id&#x60;, &#x60;is_published&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, and &#x60;provider&#x60;.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.PreprintsApi();
apiInstance.preprintsList((error, data, response) => {
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

[**[Preprint]**](Preprint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## preprintsPartialUpdate

> preprintsPartialUpdate(preprintId, body)

Update a preprint

Updates the specified preprint by setting the values of the parameters passed. Any parameters not provided will be left unchanged. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the new representation of the updated preprint, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.PreprintsApi();
let preprintId = "preprintId_example"; // String | The unique identifier of the preprint.
let body = {key: null}; // Object | 
apiInstance.preprintsPartialUpdate(preprintId, body, (error, data, response) => {
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
 **preprintId** | **String**| The unique identifier of the preprint. | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## preprintsRead

> Preprint preprintsRead(preprintId)

Retrieve a preprint

Retrieves the details of a preprint. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested preprint, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.PreprintsApi();
let preprintId = "preprintId_example"; // String | The unique identifier of the preprint.
apiInstance.preprintsRead(preprintId, (error, data, response) => {
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
 **preprintId** | **String**| The unique identifier of the preprint. | 

### Return type

[**Preprint**](Preprint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

