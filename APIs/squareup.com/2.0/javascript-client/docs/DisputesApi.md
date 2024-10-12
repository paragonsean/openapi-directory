# SquareConnectApi.DisputesApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptDispute**](DisputesApi.md#acceptDispute) | **POST** /v2/disputes/{dispute_id}/accept | AcceptDispute
[**createDisputeEvidenceText**](DisputesApi.md#createDisputeEvidenceText) | **POST** /v2/disputes/{dispute_id}/evidence-text | CreateDisputeEvidenceText
[**deleteDisputeEvidence**](DisputesApi.md#deleteDisputeEvidence) | **DELETE** /v2/disputes/{dispute_id}/evidence/{evidence_id} | DeleteDisputeEvidence
[**listDisputeEvidence**](DisputesApi.md#listDisputeEvidence) | **GET** /v2/disputes/{dispute_id}/evidence | ListDisputeEvidence
[**listDisputes**](DisputesApi.md#listDisputes) | **GET** /v2/disputes | ListDisputes
[**retrieveDispute**](DisputesApi.md#retrieveDispute) | **GET** /v2/disputes/{dispute_id} | RetrieveDispute
[**retrieveDisputeEvidence**](DisputesApi.md#retrieveDisputeEvidence) | **GET** /v2/disputes/{dispute_id}/evidence/{evidence_id} | RetrieveDisputeEvidence
[**submitEvidence**](DisputesApi.md#submitEvidence) | **POST** /v2/disputes/{dispute_id}/submit-evidence | SubmitEvidence



## acceptDispute

> AcceptDisputeResponse acceptDispute(disputeId)

AcceptDispute

Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and updates the dispute state to ACCEPTED.  Square debits the disputed amount from the seller’s Square account. If the Square account does not have sufficient funds, Square debits the associated bank account.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DisputesApi();
let disputeId = "disputeId_example"; // String | The ID of the dispute you want to accept.
apiInstance.acceptDispute(disputeId, (error, data, response) => {
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
 **disputeId** | **String**| The ID of the dispute you want to accept. | 

### Return type

[**AcceptDisputeResponse**](AcceptDisputeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createDisputeEvidenceText

> CreateDisputeEvidenceTextResponse createDisputeEvidenceText(disputeId, createDisputeEvidenceTextRequest)

CreateDisputeEvidenceText

Uploads text to use as evidence for a dispute challenge.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DisputesApi();
let disputeId = "disputeId_example"; // String | The ID of the dispute you want to upload evidence for.
let createDisputeEvidenceTextRequest = new SquareConnectApi.CreateDisputeEvidenceTextRequest(); // CreateDisputeEvidenceTextRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createDisputeEvidenceText(disputeId, createDisputeEvidenceTextRequest, (error, data, response) => {
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
 **disputeId** | **String**| The ID of the dispute you want to upload evidence for. | 
 **createDisputeEvidenceTextRequest** | [**CreateDisputeEvidenceTextRequest**](CreateDisputeEvidenceTextRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateDisputeEvidenceTextResponse**](CreateDisputeEvidenceTextResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDisputeEvidence

> DeleteDisputeEvidenceResponse deleteDisputeEvidence(disputeId, evidenceId)

DeleteDisputeEvidence

Removes specified evidence from a dispute.  Square does not send the bank any evidence that is removed. Also, you cannot remove evidence after submitting it to the bank using [SubmitEvidence](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/submit-evidence).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DisputesApi();
let disputeId = "disputeId_example"; // String | The ID of the dispute you want to remove evidence from.
let evidenceId = "evidenceId_example"; // String | The ID of the evidence you want to remove.
apiInstance.deleteDisputeEvidence(disputeId, evidenceId, (error, data, response) => {
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
 **disputeId** | **String**| The ID of the dispute you want to remove evidence from. | 
 **evidenceId** | **String**| The ID of the evidence you want to remove. | 

### Return type

[**DeleteDisputeEvidenceResponse**](DeleteDisputeEvidenceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDisputeEvidence

> ListDisputeEvidenceResponse listDisputeEvidence(disputeId, opts)

ListDisputeEvidence

Returns a list of evidence associated with a dispute.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DisputesApi();
let disputeId = "disputeId_example"; // String | The ID of the dispute.
let opts = {
  'cursor': "cursor_example" // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
};
apiInstance.listDisputeEvidence(disputeId, opts, (error, data, response) => {
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
 **disputeId** | **String**| The ID of the dispute. | 
 **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] 

### Return type

[**ListDisputeEvidenceResponse**](ListDisputeEvidenceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDisputes

> ListDisputesResponse listDisputes(opts)

ListDisputes

Returns a list of disputes associated with a particular account.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DisputesApi();
let opts = {
  'cursor': "cursor_example", // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
  'states': "states_example", // String | The dispute states to filter the result. If not specified, the endpoint returns all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`, or `LOST`).
  'locationId': "locationId_example" // String | The ID of the location for which to return a list of disputes. If not specified, the endpoint returns all open disputes (the dispute status is not `INQUIRY_CLOSED`, `WON`, or `LOST`) associated with all locations.
};
apiInstance.listDisputes(opts, (error, data, response) => {
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
 **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] 
 **states** | **String**| The dispute states to filter the result. If not specified, the endpoint returns all open disputes (the dispute status is not &#x60;INQUIRY_CLOSED&#x60;, &#x60;WON&#x60;, or &#x60;LOST&#x60;). | [optional] 
 **locationId** | **String**| The ID of the location for which to return a list of disputes. If not specified, the endpoint returns all open disputes (the dispute status is not &#x60;INQUIRY_CLOSED&#x60;, &#x60;WON&#x60;, or &#x60;LOST&#x60;) associated with all locations. | [optional] 

### Return type

[**ListDisputesResponse**](ListDisputesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveDispute

> RetrieveDisputeResponse retrieveDispute(disputeId)

RetrieveDispute

Returns details about a specific dispute.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DisputesApi();
let disputeId = "disputeId_example"; // String | The ID of the dispute you want more details about.
apiInstance.retrieveDispute(disputeId, (error, data, response) => {
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
 **disputeId** | **String**| The ID of the dispute you want more details about. | 

### Return type

[**RetrieveDisputeResponse**](RetrieveDisputeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveDisputeEvidence

> RetrieveDisputeEvidenceResponse retrieveDisputeEvidence(disputeId, evidenceId)

RetrieveDisputeEvidence

Returns the evidence metadata specified by the evidence ID in the request URL path  You must maintain a copy of the evidence you upload if you want to reference it later. You cannot download the evidence after you upload it.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DisputesApi();
let disputeId = "disputeId_example"; // String | The ID of the dispute that you want to retrieve evidence from.
let evidenceId = "evidenceId_example"; // String | The ID of the evidence to retrieve.
apiInstance.retrieveDisputeEvidence(disputeId, evidenceId, (error, data, response) => {
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
 **disputeId** | **String**| The ID of the dispute that you want to retrieve evidence from. | 
 **evidenceId** | **String**| The ID of the evidence to retrieve. | 

### Return type

[**RetrieveDisputeEvidenceResponse**](RetrieveDisputeEvidenceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## submitEvidence

> SubmitEvidenceResponse submitEvidence(disputeId)

SubmitEvidence

Submits evidence to the cardholder&#39;s bank.  Before submitting evidence, Square compiles all available evidence. This includes evidence uploaded using the [CreateDisputeEvidenceFile](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-file) and [CreateDisputeEvidenceText](https://developer.squareup.com/reference/square_2021-08-18/disputes-api/create-dispute-evidence-text) endpoints and evidence automatically provided by Square, when available.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.DisputesApi();
let disputeId = "disputeId_example"; // String | The ID of the dispute that you want to submit evidence for.
apiInstance.submitEvidence(disputeId, (error, data, response) => {
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
 **disputeId** | **String**| The ID of the dispute that you want to submit evidence for. | 

### Return type

[**SubmitEvidenceResponse**](SubmitEvidenceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

