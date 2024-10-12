# MagentoB2B.TeamCompanyIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyTeamRepositoryV1CreatePost**](TeamCompanyIdApi.md#companyTeamRepositoryV1CreatePost) | **POST** /V1/team/{companyId} | team/{companyId}



## companyTeamRepositoryV1CreatePost

> ErrorResponse companyTeamRepositoryV1CreatePost(companyId, opts)

team/{companyId}

Create a team in the company structure.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.TeamCompanyIdApi();
let companyId = 56; // Number | 
let opts = {
  'companyTeamRepositoryV1CreatePostRequest': new MagentoB2B.CompanyTeamRepositoryV1CreatePostRequest() // CompanyTeamRepositoryV1CreatePostRequest | 
};
apiInstance.companyTeamRepositoryV1CreatePost(companyId, opts, (error, data, response) => {
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
 **companyId** | **Number**|  | 
 **companyTeamRepositoryV1CreatePostRequest** | [**CompanyTeamRepositoryV1CreatePostRequest**](CompanyTeamRepositoryV1CreatePostRequest.md)|  | [optional] 

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

