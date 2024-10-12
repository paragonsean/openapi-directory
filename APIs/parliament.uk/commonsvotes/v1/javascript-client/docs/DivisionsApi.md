# CommonsVotesApi.DivisionsApi

All URIs are relative to *http://commonsvotes-api.parliament.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**divisionsGetDivisionById**](DivisionsApi.md#divisionsGetDivisionById) | **GET** /data/division/{divisionId}.{format} | Return a Division
[**divisionsGetDivisionsGroupsByParty**](DivisionsApi.md#divisionsGetDivisionsGroupsByParty) | **GET** /data/divisions.{format}/groupedbyparty | Return Divisions results grouped by party
[**divisionsGetVotingRecordsForMember**](DivisionsApi.md#divisionsGetVotingRecordsForMember) | **GET** /data/divisions.{format}/membervoting | Return voting records for a Member
[**divisionsSearchDivisions**](DivisionsApi.md#divisionsSearchDivisions) | **GET** /data/divisions.{format}/search | Return a list of Divisions
[**divisionsSearchTotalResults**](DivisionsApi.md#divisionsSearchTotalResults) | **GET** /data/divisions.{format}/searchTotalResults | Return total results count



## divisionsGetDivisionById

> PublishedDivision divisionsGetDivisionById(divisionId, format)

Return a Division

Single Division which has the specified Id

### Example

```javascript
import CommonsVotesApi from 'commons_votes_api';

let apiInstance = new CommonsVotesApi.DivisionsApi();
let divisionId = 56; // Number | Id number of a Division whose records are to be returned
let format = "format_example"; // String | xml or json
apiInstance.divisionsGetDivisionById(divisionId, format, (error, data, response) => {
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
 **divisionId** | **Number**| Id number of a Division whose records are to be returned | 
 **format** | **String**| xml or json | 

### Return type

[**PublishedDivision**](PublishedDivision.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## divisionsGetDivisionsGroupsByParty

> [DivisionGroupedByParty] divisionsGetDivisionsGroupsByParty(format, opts)

Return Divisions results grouped by party

Division results which meet the specified criteria grouped by parties

### Example

```javascript
import CommonsVotesApi from 'commons_votes_api';

let apiInstance = new CommonsVotesApi.DivisionsApi();
let format = "format_example"; // String | xml or json
let opts = {
  'queryParametersSearchTerm': "queryParametersSearchTerm_example", // String | Divisions containing search term within title or number
  'queryParametersMemberId': 56, // Number | Divisions returning Member with Member ID voting records
  'queryParametersIncludeWhenMemberWasTeller': true, // Boolean | Divisions where member was a teller as well as if they actually voted
  'queryParametersStartDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
  'queryParametersEndDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
  'queryParametersDivisionNumber': 56 // Number | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
};
apiInstance.divisionsGetDivisionsGroupsByParty(format, opts, (error, data, response) => {
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
 **format** | **String**| xml or json | 
 **queryParametersSearchTerm** | **String**| Divisions containing search term within title or number | [optional] 
 **queryParametersMemberId** | **Number**| Divisions returning Member with Member ID voting records | [optional] 
 **queryParametersIncludeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] 
 **queryParametersStartDate** | **Date**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] 
 **queryParametersEndDate** | **Date**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] 
 **queryParametersDivisionNumber** | **Number**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] 

### Return type

[**[DivisionGroupedByParty]**](DivisionGroupedByParty.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## divisionsGetVotingRecordsForMember

> [MemberVotingRecord] divisionsGetVotingRecordsForMember(format, queryParametersMemberId, opts)

Return voting records for a Member

List of voting records for a member which meet the specified criteria.

### Example

```javascript
import CommonsVotesApi from 'commons_votes_api';

let apiInstance = new CommonsVotesApi.DivisionsApi();
let format = "format_example"; // String | xml or json
let queryParametersMemberId = 56; // Number | Id number of a Member whose voting records are to be returned
let opts = {
  'queryParametersSkip': 56, // Number | The number of records to skip. Default is 0
  'queryParametersTake': 56, // Number | The number of records to return per page. Default is 25
  'queryParametersSearchTerm': "queryParametersSearchTerm_example", // String | Divisions containing search term within title or number
  'queryParametersIncludeWhenMemberWasTeller': true, // Boolean | Divisions where member was a teller as well as if they actually voted
  'queryParametersStartDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
  'queryParametersEndDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
  'queryParametersDivisionNumber': 56 // Number | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
};
apiInstance.divisionsGetVotingRecordsForMember(format, queryParametersMemberId, opts, (error, data, response) => {
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
 **format** | **String**| xml or json | 
 **queryParametersMemberId** | **Number**| Id number of a Member whose voting records are to be returned | 
 **queryParametersSkip** | **Number**| The number of records to skip. Default is 0 | [optional] 
 **queryParametersTake** | **Number**| The number of records to return per page. Default is 25 | [optional] 
 **queryParametersSearchTerm** | **String**| Divisions containing search term within title or number | [optional] 
 **queryParametersIncludeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] 
 **queryParametersStartDate** | **Date**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] 
 **queryParametersEndDate** | **Date**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] 
 **queryParametersDivisionNumber** | **Number**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] 

### Return type

[**[MemberVotingRecord]**](MemberVotingRecord.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## divisionsSearchDivisions

> [PublishedDivision] divisionsSearchDivisions(format, opts)

Return a list of Divisions

List of Divisions which meet the specified criteria

### Example

```javascript
import CommonsVotesApi from 'commons_votes_api';

let apiInstance = new CommonsVotesApi.DivisionsApi();
let format = "format_example"; // String | json or xml
let opts = {
  'queryParametersSkip': 56, // Number | The number of records to skip. Default is 0
  'queryParametersTake': 56, // Number | The number of records to return per page. Default is 25
  'queryParametersSearchTerm': "queryParametersSearchTerm_example", // String | Divisions containing search term within title or number
  'queryParametersMemberId': 56, // Number | Divisions returning Member with Member ID voting records
  'queryParametersIncludeWhenMemberWasTeller': true, // Boolean | Divisions where member was a teller as well as if they actually voted
  'queryParametersStartDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
  'queryParametersEndDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
  'queryParametersDivisionNumber': 56 // Number | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
};
apiInstance.divisionsSearchDivisions(format, opts, (error, data, response) => {
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
 **format** | **String**| json or xml | 
 **queryParametersSkip** | **Number**| The number of records to skip. Default is 0 | [optional] 
 **queryParametersTake** | **Number**| The number of records to return per page. Default is 25 | [optional] 
 **queryParametersSearchTerm** | **String**| Divisions containing search term within title or number | [optional] 
 **queryParametersMemberId** | **Number**| Divisions returning Member with Member ID voting records | [optional] 
 **queryParametersIncludeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] 
 **queryParametersStartDate** | **Date**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] 
 **queryParametersEndDate** | **Date**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] 
 **queryParametersDivisionNumber** | **Number**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] 

### Return type

[**[PublishedDivision]**](PublishedDivision.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## divisionsSearchTotalResults

> Number divisionsSearchTotalResults(format, opts)

Return total results count

Total count of Divisions meeting the specified criteria

### Example

```javascript
import CommonsVotesApi from 'commons_votes_api';

let apiInstance = new CommonsVotesApi.DivisionsApi();
let format = "format_example"; // String | json or xml
let opts = {
  'queryParametersSearchTerm': "queryParametersSearchTerm_example", // String | Divisions containing search term within title or number
  'queryParametersMemberId': 56, // Number | Divisions returning Member with Member ID voting records
  'queryParametersIncludeWhenMemberWasTeller': true, // Boolean | Divisions where member was a teller as well as if they actually voted
  'queryParametersStartDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd
  'queryParametersEndDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd
  'queryParametersDivisionNumber': 56 // Number | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint
};
apiInstance.divisionsSearchTotalResults(format, opts, (error, data, response) => {
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
 **format** | **String**| json or xml | 
 **queryParametersSearchTerm** | **String**| Divisions containing search term within title or number | [optional] 
 **queryParametersMemberId** | **Number**| Divisions returning Member with Member ID voting records | [optional] 
 **queryParametersIncludeWhenMemberWasTeller** | **Boolean**| Divisions where member was a teller as well as if they actually voted | [optional] 
 **queryParametersStartDate** | **Date**| Divisions where division date in one or after date provided. Date format is yyyy-MM-dd | [optional] 
 **queryParametersEndDate** | **Date**| Divisions where division date in one or before date provided. Date format is yyyy-MM-dd | [optional] 
 **queryParametersDivisionNumber** | **Number**| Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

