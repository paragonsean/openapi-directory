# VisageCloud.ProfileApi

All URIs are relative to *https://visagecloud.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addProfileUsingPOST**](ProfileApi.md#addProfileUsingPOST) | **POST** /rest/v1.1/profile/profile | Creates a new profile with no faces associated to it (empty profile)
[**deleteProfile2UsingDELETE**](ProfileApi.md#deleteProfile2UsingDELETE) | **DELETE** /rest/v1.1/profile/profile | Deletes a profile and unmaps all its faces
[**deleteProfileUsingDELETE**](ProfileApi.md#deleteProfileUsingDELETE) | **DELETE** /rest/v1.1/profile/{id} | Deletes a profile and unmaps all its faces
[**getClassificationAttributesFromProfileUsingGET**](ProfileApi.md#getClassificationAttributesFromProfileUsingGET) | **GET** /rest/v1.1/profile/classificationAttributes | Gets classification attributes from a profile
[**getFacesFromProfileUsingGET**](ProfileApi.md#getFacesFromProfileUsingGET) | **GET** /rest/v1.1/profile/map | Gets all the faceHashes associated to a profile
[**getProfileEnrollmentStatusUsingGET**](ProfileApi.md#getProfileEnrollmentStatusUsingGET) | **GET** /rest/v1.1/profile/enrollmentStatus | Gets the enrollment status of a profile: information on whether it is suitable for authentication.
[**getProfileUsingGET**](ProfileApi.md#getProfileUsingGET) | **GET** /rest/v1.1/profile/{id} | Retrieves a profile
[**mapClassificationAttributesToProfileUsingPUT**](ProfileApi.md#mapClassificationAttributesToProfileUsingPUT) | **PUT** /rest/v1.1/profile/classificationAttributes | Maps classification attributes to a profile
[**mapFacesToProfileUsingPOST**](ProfileApi.md#mapFacesToProfileUsingPOST) | **POST** /rest/v1.1/profile/map | Adds (maps) a list of faces, identified by faceHashes, to a profile, identified by profileId
[**removeClassificationAttributesFromProfileUsingDELETE**](ProfileApi.md#removeClassificationAttributesFromProfileUsingDELETE) | **DELETE** /rest/v1.1/profile/classificationAttributes | Removes classification attributes from a profile
[**removeFacesFromProfileUsingDELETE**](ProfileApi.md#removeFacesFromProfileUsingDELETE) | **DELETE** /rest/v1.1/profile/map | Removes (unmaps) a list of faces, identified by faceHashes, from a profile, identified by profileId
[**updateProfileUsingPATCH**](ProfileApi.md#updateProfileUsingPATCH) | **PATCH** /rest/v1.1/profile/{id} | Update an existing profile with a given id



## addProfileUsingPOST

> RestResponse addProfileUsingPOST(accessKey, secretKey, collectionId, opts)

Creates a new profile with no faces associated to it (empty profile)

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
let opts = {
  'externalId': "externalId_example", // String | External reference to additional information you don’t want to share with VisageCloud
  'screenName': "screenName_example", // String | Human-readable label for the profile
  'labels': ["null"], // [String] | Allows you to do finer filtering in face recognition
  'classificationAttributes': "classificationAttributes_example", // String | Comma separated key:value classification attributes
  'details': "details_example" // String | Comma separated key:value details of profile
};
apiInstance.addProfileUsingPOST(accessKey, secretKey, collectionId, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | 
 **externalId** | **String**| External reference to additional information you don’t want to share with VisageCloud | [optional] 
 **screenName** | **String**| Human-readable label for the profile | [optional] 
 **labels** | [**[String]**](String.md)| Allows you to do finer filtering in face recognition | [optional] 
 **classificationAttributes** | **String**| Comma separated key:value classification attributes | [optional] 
 **details** | **String**| Comma separated key:value details of profile | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProfile2UsingDELETE

> RestResponse deleteProfile2UsingDELETE(accessKey, secretKey, collectionId, profileId)

Deletes a profile and unmaps all its faces

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
let profileId = "profileId_example"; // String | The profile id (provide this if you don't have the externalId
apiInstance.deleteProfile2UsingDELETE(accessKey, secretKey, collectionId, profileId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | 
 **profileId** | **String**| The profile id (provide this if you don&#39;t have the externalId | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProfileUsingDELETE

> RestResponse deleteProfileUsingDELETE(accessKey, secretKey, collectionId, id)

Deletes a profile and unmaps all its faces

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
let id = "id_example"; // String | The profile id (provide this if you don't have the externalId
apiInstance.deleteProfileUsingDELETE(accessKey, secretKey, collectionId, id, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | 
 **id** | **String**| The profile id (provide this if you don&#39;t have the externalId | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClassificationAttributesFromProfileUsingGET

> RestResponse getClassificationAttributesFromProfileUsingGET(accessKey, secretKey, profileId, collectionId)

Gets classification attributes from a profile

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let profileId = "profileId_example"; // String | The profile associated with the classification attributes
let collectionId = "collectionId_example"; // String | The collection that contains the profile
apiInstance.getClassificationAttributesFromProfileUsingGET(accessKey, secretKey, profileId, collectionId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **profileId** | **String**| The profile associated with the classification attributes | 
 **collectionId** | **String**| The collection that contains the profile | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getFacesFromProfileUsingGET

> RestResponse getFacesFromProfileUsingGET(accessKey, secretKey, profileId, collectionId)

Gets all the faceHashes associated to a profile

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let profileId = "profileId_example"; // String | The profile that contains the faces
let collectionId = "collectionId_example"; // String | The collection that contains the profile
apiInstance.getFacesFromProfileUsingGET(accessKey, secretKey, profileId, collectionId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **profileId** | **String**| The profile that contains the faces | 
 **collectionId** | **String**| The collection that contains the profile | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfileEnrollmentStatusUsingGET

> RestResponse getProfileEnrollmentStatusUsingGET(accessKey, secretKey, profileId, collectionId)

Gets the enrollment status of a profile: information on whether it is suitable for authentication.

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let profileId = "profileId_example"; // String | The profile that contains the faces
let collectionId = "collectionId_example"; // String | The collection that contains the profile
apiInstance.getProfileEnrollmentStatusUsingGET(accessKey, secretKey, profileId, collectionId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **profileId** | **String**| The profile that contains the faces | 
 **collectionId** | **String**| The collection that contains the profile | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfileUsingGET

> RestResponse getProfileUsingGET(accessKey, secretKey, collectionId, id, opts)

Retrieves a profile

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
let id = "id_example"; // String | The profile id (provide this if you don't have the externalId
let opts = {
  'withFaces': "'false'" // String | Retrieves the profile with all its associated faces
};
apiInstance.getProfileUsingGET(accessKey, secretKey, collectionId, id, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | 
 **id** | **String**| The profile id (provide this if you don&#39;t have the externalId | 
 **withFaces** | **String**| Retrieves the profile with all its associated faces | [optional] [default to &#39;false&#39;]

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapClassificationAttributesToProfileUsingPUT

> RestResponse mapClassificationAttributesToProfileUsingPUT(accessKey, secretKey, profileId, collectionId, classificationAttributes)

Maps classification attributes to a profile

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let profileId = "profileId_example"; // String | The profile associated with the classification attributes
let collectionId = "collectionId_example"; // String | The collection that contains the profile
let classificationAttributes = "classificationAttributes_example"; // String | Comma separated key:value classification attributes
apiInstance.mapClassificationAttributesToProfileUsingPUT(accessKey, secretKey, profileId, collectionId, classificationAttributes, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **profileId** | **String**| The profile associated with the classification attributes | 
 **collectionId** | **String**| The collection that contains the profile | 
 **classificationAttributes** | **String**| Comma separated key:value classification attributes | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## mapFacesToProfileUsingPOST

> RestResponse mapFacesToProfileUsingPOST(accessKey, secretKey, faceHashes, profileId, collectionId)

Adds (maps) a list of faces, identified by faceHashes, to a profile, identified by profileId

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let faceHashes = "faceHashes_example"; // String | Comma separated face hashes, that will be associated to a profile
let profileId = "profileId_example"; // String | The profile that will store the face
let collectionId = "collectionId_example"; // String | The collection that contains the profile
apiInstance.mapFacesToProfileUsingPOST(accessKey, secretKey, faceHashes, profileId, collectionId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **faceHashes** | **String**| Comma separated face hashes, that will be associated to a profile | 
 **profileId** | **String**| The profile that will store the face | 
 **collectionId** | **String**| The collection that contains the profile | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeClassificationAttributesFromProfileUsingDELETE

> RestResponse removeClassificationAttributesFromProfileUsingDELETE(accessKey, secretKey, profileId, collectionId)

Removes classification attributes from a profile

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let profileId = "profileId_example"; // String | The profile associated with the classification attributes
let collectionId = "collectionId_example"; // String | The collection that contains the profile
apiInstance.removeClassificationAttributesFromProfileUsingDELETE(accessKey, secretKey, profileId, collectionId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **profileId** | **String**| The profile associated with the classification attributes | 
 **collectionId** | **String**| The collection that contains the profile | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## removeFacesFromProfileUsingDELETE

> RestResponse removeFacesFromProfileUsingDELETE(accessKey, secretKey, faceHashes, profileId, collectionId)

Removes (unmaps) a list of faces, identified by faceHashes, from a profile, identified by profileId

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey provided by VisageCloud
let faceHashes = "faceHashes_example"; // String | Comma separated face hashes, that will be removed from a profile
let profileId = "profileId_example"; // String | The profile that contains the face
let collectionId = "collectionId_example"; // String | The collection that contains the profile
apiInstance.removeFacesFromProfileUsingDELETE(accessKey, secretKey, faceHashes, profileId, collectionId, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey provided by VisageCloud | 
 **faceHashes** | **String**| Comma separated face hashes, that will be removed from a profile | 
 **profileId** | **String**| The profile that contains the face | 
 **collectionId** | **String**| The collection that contains the profile | 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateProfileUsingPATCH

> RestResponse updateProfileUsingPATCH(accessKey, secretKey, id, collectionId, opts)

Update an existing profile with a given id

### Example

```javascript
import VisageCloud from 'visage_cloud';

let apiInstance = new VisageCloud.ProfileApi();
let accessKey = "accessKey_example"; // String | The accessKey provided by VisageCloud
let secretKey = "secretKey_example"; // String | The secretKey or readOnlyKey provided by VisageCloud
let id = "id_example"; // String | The id of the profile that will be updated
let collectionId = "collectionId_example"; // String | Uniquely identified collection that can store multiple profiles
let opts = {
  'externalId': "externalId_example", // String | External reference to additional information you don’t want to share with VisageCloud
  'screenName': "screenName_example", // String | Human-readable label for the profile
  'labels': ["null"], // [String] | Allows you to do finer filtering in face recognition
  'classificationAttributes': "classificationAttributes_example", // String | Comma separated key:value classification attributes
  'details': "details_example" // String | Comma separated key:value details of profile
};
apiInstance.updateProfileUsingPATCH(accessKey, secretKey, id, collectionId, opts, (error, data, response) => {
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
 **accessKey** | **String**| The accessKey provided by VisageCloud | 
 **secretKey** | **String**| The secretKey or readOnlyKey provided by VisageCloud | 
 **id** | **String**| The id of the profile that will be updated | 
 **collectionId** | **String**| Uniquely identified collection that can store multiple profiles | 
 **externalId** | **String**| External reference to additional information you don’t want to share with VisageCloud | [optional] 
 **screenName** | **String**| Human-readable label for the profile | [optional] 
 **labels** | [**[String]**](String.md)| Allows you to do finer filtering in face recognition | [optional] 
 **classificationAttributes** | **String**| Comma separated key:value classification attributes | [optional] 
 **details** | **String**| Comma separated key:value details of profile | [optional] 

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

