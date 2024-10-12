# MagentoB2B.TeamTeamIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyTeamRepositoryV1DeleteByIdDelete**](TeamTeamIdApi.md#companyTeamRepositoryV1DeleteByIdDelete) | **DELETE** /V1/team/{teamId} | team/{teamId}
[**companyTeamRepositoryV1GetGet**](TeamTeamIdApi.md#companyTeamRepositoryV1GetGet) | **GET** /V1/team/{teamId} | team/{teamId}
[**companyTeamRepositoryV1SavePut**](TeamTeamIdApi.md#companyTeamRepositoryV1SavePut) | **PUT** /V1/team/{teamId} | team/{teamId}



## companyTeamRepositoryV1DeleteByIdDelete

> ErrorResponse companyTeamRepositoryV1DeleteByIdDelete(teamId)

team/{teamId}

Delete a team from the company structure.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TeamTeamIdApi();
let teamId = 56; // Number | 
apiInstance.companyTeamRepositoryV1DeleteByIdDelete(teamId, (error, data, response) => {
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
 **teamId** | **Number**|  | 

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## companyTeamRepositoryV1GetGet

> CompanyDataTeamInterface companyTeamRepositoryV1GetGet(teamId)

team/{teamId}

Returns data for a team in the company, by entity id.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TeamTeamIdApi();
let teamId = 56; // Number | 
apiInstance.companyTeamRepositoryV1GetGet(teamId, (error, data, response) => {
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
 **teamId** | **Number**|  | 

### Return type

[**CompanyDataTeamInterface**](CompanyDataTeamInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## companyTeamRepositoryV1SavePut

> Boolean companyTeamRepositoryV1SavePut(teamId, opts)

team/{teamId}

Update a team in the company structure.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TeamTeamIdApi();
let teamId = "teamId_example"; // String | 
let opts = {
  'companyTeamRepositoryV1CreatePostRequest': new MagentoB2B.CompanyTeamRepositoryV1CreatePostRequest() // CompanyTeamRepositoryV1CreatePostRequest | 
};
apiInstance.companyTeamRepositoryV1SavePut(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**|  | 
 **companyTeamRepositoryV1CreatePostRequest** | [**CompanyTeamRepositoryV1CreatePostRequest**](CompanyTeamRepositoryV1CreatePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

