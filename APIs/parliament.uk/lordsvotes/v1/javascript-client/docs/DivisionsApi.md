# LordsVotesApi.DivisionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataDivisionsDivisionIdGet**](DivisionsApi.md#dataDivisionsDivisionIdGet) | **GET** /data/Divisions/{divisionId} | Return a Division
[**dataDivisionsGroupedbypartyGet**](DivisionsApi.md#dataDivisionsGroupedbypartyGet) | **GET** /data/Divisions/groupedbyparty | Return Divisions results grouped by party
[**dataDivisionsMembervotingGet**](DivisionsApi.md#dataDivisionsMembervotingGet) | **GET** /data/Divisions/membervoting | Return voting records for a Member
[**dataDivisionsSearchGet**](DivisionsApi.md#dataDivisionsSearchGet) | **GET** /data/Divisions/search | Return a list of Divisions
[**dataDivisionsSearchTotalResultsGet**](DivisionsApi.md#dataDivisionsSearchTotalResultsGet) | **GET** /data/Divisions/searchTotalResults | Return total results count



## dataDivisionsDivisionIdGet

> DivisionViewModel dataDivisionsDivisionIdGet(divisionId)

Return a Division

Get a single Division which has the Id specified.

### Example

```javascript
import LordsVotesApi from 'lords_votes_api';

let apiInstance = new LordsVotesApi.DivisionsApi();
let divisionId = 56; // Number | Division with ID specified
apiInstance.dataDivisionsDivisionIdGet(divisionId, (error, data, response) => {
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
 **divisionId** | **Number**| Division with ID specified | 

### Return type

[**DivisionViewModel**](DivisionViewModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## dataDivisionsGroupedbypartyGet

> DivisionGroupByPartyViewModel dataDivisionsGroupedbypartyGet(opts)

Return Divisions results grouped by party

Get a list of Divisions which contain grouped by party

### Example

```javascript
import LordsVotesApi from 'lords_votes_api';

let apiInstance = new LordsVotesApi.DivisionsApi();
let opts = {
  'searchTerm': "searchTerm_example", // String | Divisions containing search term within title or number
  'memberId': 56, // Number | Divisions returning Member with Member ID voting records
  'includeWhenMemberWasTeller': true, // Boolean | Divisions where member was a teller as well as if they actually voted
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
  'divisionNumber': 56, // Number | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
  'totalVotesCastComparator': new LordsVotesApi.Comparators(), // Comparators | comparison operator to use
  'totalVotesCastValueToCompare': 56, // Number | value to compare to with the operator provided
  'majorityComparator': new LordsVotesApi.Comparators(), // Comparators | comparison operator to use
  'majorityValueToCompare': 56 // Number | value to compare to with the operator provided
};
apiInstance.dataDivisionsGroupedbypartyGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Divisions containing search term within title or number | [optional] 
 **memberId** | **Number**| Divisions returning Member with Member ID voting records | [optional] 
 **includeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] 
 **startDate** | **Date**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] 
 **endDate** | **Date**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] 
 **divisionNumber** | **Number**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] 
 **totalVotesCastComparator** | [**Comparators**](.md)| comparison operator to use | [optional] 
 **totalVotesCastValueToCompare** | **Number**| value to compare to with the operator provided | [optional] 
 **majorityComparator** | [**Comparators**](.md)| comparison operator to use | [optional] 
 **majorityValueToCompare** | **Number**| value to compare to with the operator provided | [optional] 

### Return type

[**DivisionGroupByPartyViewModel**](DivisionGroupByPartyViewModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## dataDivisionsMembervotingGet

> MemberVotingRecordViewModel dataDivisionsMembervotingGet(memberId, opts)

Return voting records for a Member

Get a list of voting records for a Member.

### Example

```javascript
import LordsVotesApi from 'lords_votes_api';

let apiInstance = new LordsVotesApi.DivisionsApi();
let memberId = 56; // Number | Id number of a Member whose voting records are to be returned
let opts = {
  'searchTerm': "searchTerm_example", // String | Divisions containing search term within title or number
  'includeWhenMemberWasTeller': true, // Boolean | Divisions where member was a teller as well as if they actually voted
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
  'divisionNumber': 56, // Number | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
  'totalVotesCastComparator': new LordsVotesApi.Comparators(), // Comparators | comparison operator to use
  'totalVotesCastValueToCompare': 56, // Number | value to compare to with the operator provided
  'majorityComparator': new LordsVotesApi.Comparators(), // Comparators | comparison operator to use
  'majorityValueToCompare': 56, // Number | value to compare to with the operator provided
  'skip': 0, // Number | The number of records to skip. Must be a positive integer. Default is 0
  'take': 25 // Number | The number of records to return per page. Must be more than 0. Default is 25
};
apiInstance.dataDivisionsMembervotingGet(memberId, opts, (error, data, response) => {
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
 **memberId** | **Number**| Id number of a Member whose voting records are to be returned | 
 **searchTerm** | **String**| Divisions containing search term within title or number | [optional] 
 **includeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] 
 **startDate** | **Date**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] 
 **endDate** | **Date**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] 
 **divisionNumber** | **Number**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] 
 **totalVotesCastComparator** | [**Comparators**](.md)| comparison operator to use | [optional] 
 **totalVotesCastValueToCompare** | **Number**| value to compare to with the operator provided | [optional] 
 **majorityComparator** | [**Comparators**](.md)| comparison operator to use | [optional] 
 **majorityValueToCompare** | **Number**| value to compare to with the operator provided | [optional] 
 **skip** | **Number**| The number of records to skip. Must be a positive integer. Default is 0 | [optional] [default to 0]
 **take** | **Number**| The number of records to return per page. Must be more than 0. Default is 25 | [optional] [default to 25]

### Return type

[**MemberVotingRecordViewModel**](MemberVotingRecordViewModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## dataDivisionsSearchGet

> [DivisionViewModel] dataDivisionsSearchGet(opts)

Return a list of Divisions

Get a list of Divisions which meet the specified criteria.

### Example

```javascript
import LordsVotesApi from 'lords_votes_api';

let apiInstance = new LordsVotesApi.DivisionsApi();
let opts = {
  'searchTerm': "searchTerm_example", // String | Divisions containing search term within title or number
  'memberId': 56, // Number | Divisions returning Member with Member ID voting records
  'includeWhenMemberWasTeller': true, // Boolean | Divisions where member was a teller as well as if they actually voted
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
  'divisionNumber': 56, // Number | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
  'totalVotesCastComparator': new LordsVotesApi.Comparators(), // Comparators | comparison operator to use
  'totalVotesCastValueToCompare': 56, // Number | value to compare to with the operator provided
  'majorityComparator': new LordsVotesApi.Comparators(), // Comparators | comparison operator to use
  'majorityValueToCompare': 56, // Number | value to compare to with the operator provided
  'skip': 0, // Number | The number of records to skip. Must be a positive integer. Default is 0
  'take': 25 // Number | The number of records to return per page. Must be more than 0. Default is 25
};
apiInstance.dataDivisionsSearchGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Divisions containing search term within title or number | [optional] 
 **memberId** | **Number**| Divisions returning Member with Member ID voting records | [optional] 
 **includeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] 
 **startDate** | **Date**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] 
 **endDate** | **Date**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] 
 **divisionNumber** | **Number**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] 
 **totalVotesCastComparator** | [**Comparators**](.md)| comparison operator to use | [optional] 
 **totalVotesCastValueToCompare** | **Number**| value to compare to with the operator provided | [optional] 
 **majorityComparator** | [**Comparators**](.md)| comparison operator to use | [optional] 
 **majorityValueToCompare** | **Number**| value to compare to with the operator provided | [optional] 
 **skip** | **Number**| The number of records to skip. Must be a positive integer. Default is 0 | [optional] [default to 0]
 **take** | **Number**| The number of records to return per page. Must be more than 0. Default is 25 | [optional] [default to 25]

### Return type

[**[DivisionViewModel]**](DivisionViewModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## dataDivisionsSearchTotalResultsGet

> Number dataDivisionsSearchTotalResultsGet(opts)

Return total results count

Get total count of Divisions meeting the specified query, useful for paging lists etc...

### Example

```javascript
import LordsVotesApi from 'lords_votes_api';

let apiInstance = new LordsVotesApi.DivisionsApi();
let opts = {
  'searchTerm': "searchTerm_example", // String | Divisions containing search term within title or number
  'memberId': 56, // Number | Divisions returning Member with Member ID voting records
  'includeWhenMemberWasTeller': true, // Boolean | Divisions where member was a teller as well as if they actually voted
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
  'divisionNumber': 56, // Number | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
  'totalVotesCastComparator': new LordsVotesApi.Comparators(), // Comparators | comparison operator to use
  'totalVotesCastValueToCompare': 56, // Number | value to compare to with the operator provided
  'majorityComparator': new LordsVotesApi.Comparators(), // Comparators | comparison operator to use
  'majorityValueToCompare': 56 // Number | value to compare to with the operator provided
};
apiInstance.dataDivisionsSearchTotalResultsGet(opts, (error, data, response) => {
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
 **searchTerm** | **String**| Divisions containing search term within title or number | [optional] 
 **memberId** | **Number**| Divisions returning Member with Member ID voting records | [optional] 
 **includeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] 
 **startDate** | **Date**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] 
 **endDate** | **Date**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] 
 **divisionNumber** | **Number**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] 
 **totalVotesCastComparator** | [**Comparators**](.md)| comparison operator to use | [optional] 
 **totalVotesCastValueToCompare** | **Number**| value to compare to with the operator provided | [optional] 
 **majorityComparator** | [**Comparators**](.md)| comparison operator to use | [optional] 
 **majorityValueToCompare** | **Number**| value to compare to with the operator provided | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

