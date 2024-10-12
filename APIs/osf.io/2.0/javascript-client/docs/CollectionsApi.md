# OsfApiv2Documentation.CollectionsApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collectionsAddMetadata**](CollectionsApi.md#collectionsAddMetadata) | **POST** /collections/{collection_id}/collected_metadata/ | Add Metadata or Subjects to a Entity in a Collection
[**collectionsCollectedMetadata**](CollectionsApi.md#collectionsCollectedMetadata) | **GET** /collections/{collection_id}/collected_metadata/{cgm_id}/subjects/ | Retrieve subject data for a specific piece of metadata info for a collection
[**collectionsCreate**](CollectionsApi.md#collectionsCreate) | **POST** /collections/ | Create a Collection
[**collectionsDelete**](CollectionsApi.md#collectionsDelete) | **DELETE** /collections/{collection_id}/ | Delete a Collection
[**collectionsDetail**](CollectionsApi.md#collectionsDetail) | **GET** /collections/{collection_id}/ | Retrieve a Collection
[**collectionsLinkedNodesList**](CollectionsApi.md#collectionsLinkedNodesList) | **GET** /collections/{collection_id}/linked_nodes | List All Linked Nodes for a Collection
[**collectionsLinkedNodesRelationships**](CollectionsApi.md#collectionsLinkedNodesRelationships) | **POST** /collections/{collection_id}/linked_nodes/relationships/ | Link Nodes to Collection
[**collectionsLinkedNodesRelationshipsCreate**](CollectionsApi.md#collectionsLinkedNodesRelationshipsCreate) | **GET** /collections/{collection_id}/linked_nodes/relationships/ | Give a Sparse List of Node Ids
[**collectionsLinkedNodesRelationshipsDelete**](CollectionsApi.md#collectionsLinkedNodesRelationshipsDelete) | **DELETE** /collections/{collection_id}/linked_nodes/relationships/ | Remove Nodes From Collection
[**collectionsLinkedPreprintsList**](CollectionsApi.md#collectionsLinkedPreprintsList) | **GET** /collections/{collection_id}/linked_preprints/ | List All Linked Preprints for a Collection
[**collectionsLinkedRegistrationsList**](CollectionsApi.md#collectionsLinkedRegistrationsList) | **GET** /collections/{collection_id}/linked_registrations/ | List All Linked Registrations for a Collection
[**collectionsLinkedRegistrationsRelationships**](CollectionsApi.md#collectionsLinkedRegistrationsRelationships) | **POST** /collections/{collection_id}/linked_registrations/relationships/ | Link Registrations to Collection
[**collectionsLinkedRegistrationsRelationshipsCreate**](CollectionsApi.md#collectionsLinkedRegistrationsRelationshipsCreate) | **GET** /collections/{collection_id}/linked_registrations/relationships/ | Give a Sparse List of Registrations Ids
[**collectionsLinkedRegistrationsRelationshipsDelete**](CollectionsApi.md#collectionsLinkedRegistrationsRelationshipsDelete) | **DELETE** /collections/{collection_id}/linked_registrations/relationships/ | Remove Registrations From Collection
[**collectionsList**](CollectionsApi.md#collectionsList) | **GET** /collections/ | List all Collections
[**collectionsMetadataDelete**](CollectionsApi.md#collectionsMetadataDelete) | **DELETE** /collections/{collection_id}/collected_metadata/{cgm_id} | Delete Collection Metadata from entitiy
[**collectionsMetadataDetail**](CollectionsApi.md#collectionsMetadataDetail) | **POST** /collections/{collection_id}/collected_metadata/{cgm_id} | Add Metadata or Subjects to an Entity in a Collection
[**collectionsMetadataRegistrationsDetail**](CollectionsApi.md#collectionsMetadataRegistrationsDetail) | **GET** /collections/{collection_id}/collected_metadata/{cgm_id} | Retrieve Specific Metadata for a Collection
[**collectionsMetadataRegistrationsList**](CollectionsApi.md#collectionsMetadataRegistrationsList) | **GET** /collections/{collection_id}/collected_metadata/ | Retrieve a list of collected metadata for a collection
[**collectionsMetadataSubjectsRelationships**](CollectionsApi.md#collectionsMetadataSubjectsRelationships) | **GET** /collections/{collection_id}/collected_metadata/{cgm_id}/relationships/subjects/ | Retrieve subject metadata for a specific piece of metadata in a collection
[**collectionsMetadataSubjectsRelationshipsUpdate**](CollectionsApi.md#collectionsMetadataSubjectsRelationshipsUpdate) | **POST** /collections/{collection_id}/collected_metadata/{cgm_id}/relationships/subjects/ | Update subjects for a specific piece of metadata in a collection



## collectionsAddMetadata

> collectionsAddMetadata(collectionId, body)

Add Metadata or Subjects to a Entity in a Collection

List of user created metadata for entities within a collection. #### Permissions To edit this collection a user must have collections write permissions #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let body = {key: null}; // Object | 
apiInstance.collectionsAddMetadata(collectionId, body, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## collectionsCollectedMetadata

> collectionsCollectedMetadata(collectionId, cgmId)

Retrieve subject data for a specific piece of metadata info for a collection

 #### Permissions In order to view these subject it must be a public collection or a user must have read permissions for collection.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error, other then permissions errors.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let cgmId = "cgmId_example"; // String | A short id for that piece of metadata
apiInstance.collectionsCollectedMetadata(collectionId, cgmId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **cgmId** | **String**| A short id for that piece of metadata | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionsCreate

> collectionsCreate(body)

Create a Collection

Retrieves a list collections, either public or related to the user #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.  Comments on private nodes are only visible to contributors and administrators on the parent node. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of comment objects. Each resource in the array is a separate comment object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let body = {key: null}; // Object | 
apiInstance.collectionsCreate(body, (error, data, response) => {
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
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## collectionsDelete

> collectionsDelete(collectionId)

Delete a Collection

Deletes a collection, if the user has appropriate permissions. #### Permissions Users must have write permissions on a collection in order to delete it #### Returns Nothing is returned in the body

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
apiInstance.collectionsDelete(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## collectionsDetail

> [Collection] collectionsDetail(collectionId)

Retrieve a Collection

Retrieves a collection, if the user has appropriate permissions.  #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
apiInstance.collectionsDetail(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 

### Return type

[**[Collection]**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## collectionsLinkedNodesList

> collectionsLinkedNodesList(collectionId)

List All Linked Nodes for a Collection

List of all nodes linked to the given collection. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
apiInstance.collectionsLinkedNodesList(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionsLinkedNodesRelationships

> collectionsLinkedNodesRelationships(collectionId, body)

Link Nodes to Collection

This endpoint allow users to a add a node to a collection by issuing a POST request. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of comment objects. Each resource in the array is a separate comment object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let body = {key: null}; // Object | 
apiInstance.collectionsLinkedNodesRelationships(collectionId, body, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## collectionsLinkedNodesRelationshipsCreate

> collectionsLinkedNodesRelationshipsCreate(collectionId)

Give a Sparse List of Node Ids

List of all the node ids linked to the given collection. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
apiInstance.collectionsLinkedNodesRelationshipsCreate(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionsLinkedNodesRelationshipsDelete

> collectionsLinkedNodesRelationshipsDelete(collectionId, body)

Remove Nodes From Collection

 This removes associated nodes from a collection #### Permissions Any user with write permissions on this collection should be to remove nodes from this collection. #### Returns Nothing in the response body.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let body = {key: null}; // Object | 
apiInstance.collectionsLinkedNodesRelationshipsDelete(collectionId, body, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## collectionsLinkedPreprintsList

> collectionsLinkedPreprintsList(collectionId)

List All Linked Preprints for a Collection

List of all preprints linked to the given collection. #### Permissions This returns all public preprints associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
apiInstance.collectionsLinkedPreprintsList(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, links, meta


## collectionsLinkedRegistrationsList

> collectionsLinkedRegistrationsList(collectionId)

List All Linked Registrations for a Collection

List of all registrations linked to the given collection. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
apiInstance.collectionsLinkedRegistrationsList(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, links, meta


## collectionsLinkedRegistrationsRelationships

> collectionsLinkedRegistrationsRelationships(collectionId, body)

Link Registrations to Collection

This endpoint allow users to a add a registration to a collection by issuing a POST request. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of comment objects. Each resource in the array is a separate comment object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let body = {key: null}; // Object | 
apiInstance.collectionsLinkedRegistrationsRelationships(collectionId, body, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## collectionsLinkedRegistrationsRelationshipsCreate

> collectionsLinkedRegistrationsRelationshipsCreate(collectionId)

Give a Sparse List of Registrations Ids

List of all the registration ids linked to the given collection. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
apiInstance.collectionsLinkedRegistrationsRelationshipsCreate(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionsLinkedRegistrationsRelationshipsDelete

> collectionsLinkedRegistrationsRelationshipsDelete(collectionId, body)

Remove Registrations From Collection

 This removes associated registrations from a collection #### Permissions Any user with write permissions on this collection should be to remove registrations from this collection. #### Returns Nothing in the response body.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let body = {key: null}; // Object | 
apiInstance.collectionsLinkedRegistrationsRelationshipsDelete(collectionId, body, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## collectionsList

> [Collection] collectionsList()

List all Collections

Retrieves a list collections, either public or related to the user #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.  Comments on private nodes are only visible to contributors and administrators on the parent node. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
apiInstance.collectionsList((error, data, response) => {
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

[**[Collection]**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json


## collectionsMetadataDelete

> collectionsMetadataDelete(collectionId, cgmId)

Delete Collection Metadata from entitiy

 #### Permissions Only a user with collection admin permissions can delete collected metadata #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let cgmId = "cgmId_example"; // String | A short id for that piece of metadata
apiInstance.collectionsMetadataDelete(collectionId, cgmId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **cgmId** | **String**| A short id for that piece of metadata | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## collectionsMetadataDetail

> collectionsMetadataDetail(collectionId, cgmId, body)

Add Metadata or Subjects to an Entity in a Collection

List of user created metadata for entities within a collection. #### Permissions To edit this collection a user must have collections write permissions #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let cgmId = "cgmId_example"; // String | A short id for that piece of metadata
let body = {key: null}; // Object | 
apiInstance.collectionsMetadataDetail(collectionId, cgmId, body, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **cgmId** | **String**| A short id for that piece of metadata | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## collectionsMetadataRegistrationsDetail

> collectionsMetadataRegistrationsDetail(collectionId, cgmId)

Retrieve Specific Metadata for a Collection

 #### Permissions In order to view this metadata it must be public or a user must have read permissions for collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let cgmId = "cgmId_example"; // String | A short id for that piece of metadata
apiInstance.collectionsMetadataRegistrationsDetail(collectionId, cgmId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **cgmId** | **String**| A short id for that piece of metadata | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: data, meta


## collectionsMetadataRegistrationsList

> collectionsMetadataRegistrationsList(collectionId)

Retrieve a list of collected metadata for a collection

List of user created metadata for entities within a collection. #### Permissions In order to view this metadata it must be public or a user must have read permissions for collection. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
apiInstance.collectionsMetadataRegistrationsList(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionsMetadataSubjectsRelationships

> collectionsMetadataSubjectsRelationships(collectionId, cgmId)

Retrieve subject metadata for a specific piece of metadata in a collection

 #### Permissions This is public for a logged out user when an entity is public. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let cgmId = "cgmId_example"; // String | A short id for that piece of metadata
apiInstance.collectionsMetadataSubjectsRelationships(collectionId, cgmId, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **cgmId** | **String**| A short id for that piece of metadata | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collectionsMetadataSubjectsRelationshipsUpdate

> collectionsMetadataSubjectsRelationshipsUpdate(collectionId, cgmId, body)

Update subjects for a specific piece of metadata in a collection

 #### Permissions This is editable for a user with a write permission for this collection.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of nodes ids. The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CollectionsApi();
let collectionId = "collectionId_example"; // String | A short id for that collection
let cgmId = "cgmId_example"; // String | A short id for that piece of metadata
let body = {key: null}; // Object | 
apiInstance.collectionsMetadataSubjectsRelationshipsUpdate(collectionId, cgmId, body, (error, data, response) => {
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
 **collectionId** | **String**| A short id for that collection | 
 **cgmId** | **String**| A short id for that piece of metadata | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

