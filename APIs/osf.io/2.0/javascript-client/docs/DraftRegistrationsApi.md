# OsfApiv2Documentation.DraftRegistrationsApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**draftRegistrationContributorsCreate**](DraftRegistrationsApi.md#draftRegistrationContributorsCreate) | **POST** /draft_registrations/{draft_id}/contributors/ | Add a contributor to a Draft Registration
[**draftRegistrationContributorsList**](DraftRegistrationsApi.md#draftRegistrationContributorsList) | **GET** /draft_registrations/{draft_id}/contributors/ | Retreive a list Contributors from a Draft Registration
[**draftRegistrationsCreate**](DraftRegistrationsApi.md#draftRegistrationsCreate) | **POST** /draft_registrations/ | Create a Draft Registration
[**draftRegistrationsDraftIdContributorsUserIdGet**](DraftRegistrationsApi.md#draftRegistrationsDraftIdContributorsUserIdGet) | **GET** /draft_registrations/{draft_id}/contributors/{user_id}/ | Retreive a Contributor from a Draft Registration
[**draftRegistrationsDraftIdDelete**](DraftRegistrationsApi.md#draftRegistrationsDraftIdDelete) | **DELETE** /draft_registrations/{draft_id}/ | Delete a draft registration
[**draftRegistrationsDraftIdGet**](DraftRegistrationsApi.md#draftRegistrationsDraftIdGet) | **GET** /draft_registrations/{draft_id}/ | Retrieve a Draft Registration
[**draftRegistrationsDraftIdInstitutionsGet**](DraftRegistrationsApi.md#draftRegistrationsDraftIdInstitutionsGet) | **GET** /draft_registrations/{draft_id}/institutions/ | Retrieve Institutions afilliated with a Draft Registration
[**draftRegistrationsDraftIdPatch**](DraftRegistrationsApi.md#draftRegistrationsDraftIdPatch) | **PATCH** /draft_registrations/{draft_id}/ | Update a Draft Registration
[**draftRegistrationsRead**](DraftRegistrationsApi.md#draftRegistrationsRead) | **GET** /draft_registrations/ | Retrieve a list of Draft Registrations
[**nodesDraftRegistrationsRead**](DraftRegistrationsApi.md#nodesDraftRegistrationsRead) | **GET** /nodes/{node_id}/draft_registrations/{draft_id}/ | Retrieve a Draft Registration
[**nodesDraftRegistrationsSubjects**](DraftRegistrationsApi.md#nodesDraftRegistrationsSubjects) | **GET** /draft_registrations/{draft_id}/subjects/ | Retrieve Subjects associated with a Draft Registration



## draftRegistrationContributorsCreate

> draftRegistrationContributorsCreate(draftId, contributor)

Add a contributor to a Draft Registration

Adds a contributor to a Draft Registration, contributors can view, edit, register or delete a Draft Registration depending on their permissions. Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot; contributors. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not. #### Permissions Only project administrators can add contributors to a Draft Registration. #### Required A relationship object with a &#x60;data&#x60; key, containing the &#x60;users&#x60; type and valid user ID is required. All attributes describing the relationship between the node and the user are optional. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the new contributor, if the request is successful. If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
let draftId = "draftId_example"; // String | The unique identifier of the Draft Registration.
let contributor = new OsfApiv2Documentation.Contributor(); // Contributor | 
apiInstance.draftRegistrationContributorsCreate(draftId, contributor, (error, data, response) => {
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
 **draftId** | **String**| The unique identifier of the Draft Registration. | 
 **contributor** | [**Contributor**](Contributor.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## draftRegistrationContributorsList

> draftRegistrationContributorsList(draftId)

Retreive a list Contributors from a Draft Registration

Retrieves the details of all given Contributors for a Draft Registration. Contributors are users who can make changes to the Draft Registration. Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
let draftId = "draftId_example"; // String | The unique identifier of the Draft Registration.
apiInstance.draftRegistrationContributorsList(draftId, (error, data, response) => {
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
 **draftId** | **String**| The unique identifier of the Draft Registration. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## draftRegistrationsCreate

> DraftRegistration draftRegistrationsCreate(draftRegistration)

Create a Draft Registration

This creates a Draft Registration that can be used to edit and register research. Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it&#39;s metadata edited. A Draft Registration created by this endpoint will not have a Project linked with it by default, but if the user includes a &#x60;branched_from&#x60; attribute in their Draft Registration creation payload with the value of the &#x60;branched_from&#x60; being guid of a Project they have permissions for the Draft Registration will be linked to the Project. If you linked your Draft Registration on a Project, your original Project remains editable and will now have the Draft Registration linked to it.  #### Permissions Any user can create a Draft Registration. If the &#x60;branched_from&#x60; attribute is provided, then the user must be an ADMIN contributor on the Project being registered. #### Required Required fields for creating a Draft Registration include:  &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&#x60;schema_id&#x60; #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the created Draft Registration, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
let draftRegistration = new OsfApiv2Documentation.DraftRegistration(); // DraftRegistration | 
apiInstance.draftRegistrationsCreate(draftRegistration, (error, data, response) => {
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
 **draftRegistration** | [**DraftRegistration**](DraftRegistration.md)|  | 

### Return type

[**DraftRegistration**](DraftRegistration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*, application/json


## draftRegistrationsDraftIdContributorsUserIdGet

> draftRegistrationsDraftIdContributorsUserIdGet(draftId, userId)

Retreive a Contributor from a Draft Registration

Retrieves the details of a given contributor.  Contributors are users who can view or edit to the Draft Registrations.  Contributors are categorized as either \&quot;bibliographic\&quot; or \&quot;non-bibliographic\&quot;. From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
let draftId = "draftId_example"; // String | The unique identifier of the Draft Registration.
let userId = "userId_example"; // String | The unique identifier of the Contributor.
apiInstance.draftRegistrationsDraftIdContributorsUserIdGet(draftId, userId, (error, data, response) => {
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
 **draftId** | **String**| The unique identifier of the Draft Registration. | 
 **userId** | **String**| The unique identifier of the Contributor. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## draftRegistrationsDraftIdDelete

> draftRegistrationsDraftIdDelete(draftId)

Delete a draft registration

Permanently deletes a draft registration. A draft that has already been registered cannot be deleted. #### Permissions Only draft registration contributors with ADMIN permissions may delete draft registrations #### Returns If the request is successful, no content is returned. If the request is unsuccessful, a JSON object with an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes]() to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
let draftId = "draftId_example"; // String | The unique identifier of the draft registration.
apiInstance.draftRegistrationsDraftIdDelete(draftId, (error, data, response) => {
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
 **draftId** | **String**| The unique identifier of the draft registration. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## draftRegistrationsDraftIdGet

> DraftRegistration draftRegistrationsDraftIdGet(draftId)

Retrieve a Draft Registration

Retrieve the details of a given Draft Registration Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it&#39;s metadata edited.  If you based your Draft Registration on a Project, your original Project remains editable but will now have the Draft Registration linked to it. #### Permissions Only draft registration contributors may view draft registrations. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested draft registration, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
let draftId = "draftId_example"; // String | The unique identifier of the draft registration.
apiInstance.draftRegistrationsDraftIdGet(draftId, (error, data, response) => {
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
 **draftId** | **String**| The unique identifier of the draft registration. | 

### Return type

[**DraftRegistration**](DraftRegistration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## draftRegistrationsDraftIdInstitutionsGet

> Institution draftRegistrationsDraftIdInstitutionsGet(draftId)

Retrieve Institutions afilliated with a Draft Registration

Once a properly authenticated user has marked their registration as affiliated with an institution, that institution and any others added will appear in this list.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
let draftId = "draftId_example"; // String | The unique identifier of the draft registration.
apiInstance.draftRegistrationsDraftIdInstitutionsGet(draftId, (error, data, response) => {
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
 **draftId** | **String**| The unique identifier of the draft registration. | 

### Return type

[**Institution**](Institution.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## draftRegistrationsDraftIdPatch

> draftRegistrationsDraftIdPatch(draftId, body)

Update a Draft Registration

Updates a Draft Registration by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged. Note this will not register or change the machine state of a Draft Registration, it can only edit the Draft Registration&#39;s attributes prior to its registration. #### Permissions Only draft registration contributors may view draft registrations and only draft registration contributors with WRITE or ADMIN permissions may update draft registrations. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the new representation of the updated draft registration, if the request is successful. If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
let draftId = "draftId_example"; // String | The unique identifier of the draft registration.
let body = {key: null}; // Object | 
apiInstance.draftRegistrationsDraftIdPatch(draftId, body, (error, data, response) => {
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
 **draftId** | **String**| The unique identifier of the draft registration. | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## draftRegistrationsRead

> DraftRegistration draftRegistrationsRead()

Retrieve a list of Draft Registrations

Retrieve a list of all currently available Draft Registrations for that user. #### Permissions Only Draft Registration contributors may view draft registrations. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested draft registration, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
apiInstance.draftRegistrationsRead((error, data, response) => {
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

[**DraftRegistration**](DraftRegistration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## nodesDraftRegistrationsRead

> DraftRegistration nodesDraftRegistrationsRead(nodeId, draftId)

Retrieve a Draft Registration

Retrieve the details of a given draft registration. Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it&#39;s metadata edited.  Your original project remains editable but will now have the draft registration linked to it. #### Permissions Only project administrators may view draft registrations. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested draft registration, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
let nodeId = "nodeId_example"; // String | The unique identifier of the node.
let draftId = "draftId_example"; // String | The unique identifier of the draft registration.
apiInstance.nodesDraftRegistrationsRead(nodeId, draftId, (error, data, response) => {
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
 **nodeId** | **String**| The unique identifier of the node. | 
 **draftId** | **String**| The unique identifier of the draft registration. | 

### Return type

[**DraftRegistration**](DraftRegistration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## nodesDraftRegistrationsSubjects

> Subject nodesDraftRegistrationsSubjects(draftId)

Retrieve Subjects associated with a Draft Registration

This retrieves a list of subjects associated with a Draft Registration. Subjects are formatted here in a flat paginated list, but are hierarchical and nested by specificity of subject matter.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.DraftRegistrationsApi();
let draftId = "draftId_example"; // String | The unique identifier of the draft registration.
apiInstance.nodesDraftRegistrationsSubjects(draftId, (error, data, response) => {
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
 **draftId** | **String**| The unique identifier of the draft registration. | 

### Return type

[**Subject**](Subject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

