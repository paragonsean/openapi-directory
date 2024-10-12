# AltoroJRestApi.Class2AccountApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccount**](Class2AccountApi.md#getAccount) | **GET** /account | 
[**getAccountBalance**](Class2AccountApi.md#getAccountBalance) | **GET** /account/{accountNo} | 
[**getTransactions**](Class2AccountApi.md#getTransactions) | **POST** /account/{accountNo}/transactions | 
[**showLastTenTransactions**](Class2AccountApi.md#showLastTenTransactions) | **GET** /account/{accountNo}/transactions | 



## getAccount

> getAccount(authorization)



Returns a list of all the accounts owned by the user

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class2AccountApi();
let authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
apiInstance.getAccount(authorization, (error, data, response) => {
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
 **authorization** | **String**| Authorization token (provided upon successful login) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAccountBalance

> getAccountBalance(authorization, accountNo)



Returns details about a specific account

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class2AccountApi();
let authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
let accountNo = "accountNo_example"; // String | Account id
apiInstance.getAccountBalance(authorization, accountNo, (error, data, response) => {
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
 **authorization** | **String**| Authorization token (provided upon successful login) | 
 **accountNo** | **String**| Account id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTransactions

> getTransactions(authorization, accountNo, body)



Return transactions between 2 specific dates

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class2AccountApi();
let authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
let accountNo = "accountNo_example"; // String | Account id
let body = new AltoroJRestApi.Dates(); // Dates | A start date and an end date
apiInstance.getTransactions(authorization, accountNo, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token (provided upon successful login) | 
 **accountNo** | **String**| Account id | 
 **body** | [**Dates**](Dates.md)| A start date and an end date | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## showLastTenTransactions

> showLastTenTransactions(authorization, accountNo)



Returns the last 10 transactions attached to an account

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class2AccountApi();
let authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
let accountNo = "accountNo_example"; // String | Account id
apiInstance.showLastTenTransactions(authorization, accountNo, (error, data, response) => {
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
 **authorization** | **String**| Authorization token (provided upon successful login) | 
 **accountNo** | **String**| Account id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

