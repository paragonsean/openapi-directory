# MembersApi.MembersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiMembersHistoryGet**](MembersApi.md#apiMembersHistoryGet) | **GET** /api/Members/History | Return members by ID with list of their historical names, parties and memberships
[**apiMembersIdBiographyGet**](MembersApi.md#apiMembersIdBiographyGet) | **GET** /api/Members/{id}/Biography | Return biography of member by ID
[**apiMembersIdContactGet**](MembersApi.md#apiMembersIdContactGet) | **GET** /api/Members/{id}/Contact | Return list of contact details of member by ID
[**apiMembersIdContributionSummaryGet**](MembersApi.md#apiMembersIdContributionSummaryGet) | **GET** /api/Members/{id}/ContributionSummary | Return contribution summary of member by ID
[**apiMembersIdEdmsGet**](MembersApi.md#apiMembersIdEdmsGet) | **GET** /api/Members/{id}/Edms | Return list of early day motions of member by ID
[**apiMembersIdExperienceGet**](MembersApi.md#apiMembersIdExperienceGet) | **GET** /api/Members/{id}/Experience | Return experience of member by ID
[**apiMembersIdFocusGet**](MembersApi.md#apiMembersIdFocusGet) | **GET** /api/Members/{id}/Focus | Return list of areas of focus of member by ID
[**apiMembersIdGet**](MembersApi.md#apiMembersIdGet) | **GET** /api/Members/{id} | Return member by ID
[**apiMembersIdLatestElectionResultGet**](MembersApi.md#apiMembersIdLatestElectionResultGet) | **GET** /api/Members/{id}/LatestElectionResult | Return latest election result of member by ID
[**apiMembersIdPortraitGet**](MembersApi.md#apiMembersIdPortraitGet) | **GET** /api/Members/{id}/Portrait | Return portrait of member by ID
[**apiMembersIdPortraitUrlGet**](MembersApi.md#apiMembersIdPortraitUrlGet) | **GET** /api/Members/{id}/PortraitUrl | Return portrait url of member by ID
[**apiMembersIdRegisteredInterestsGet**](MembersApi.md#apiMembersIdRegisteredInterestsGet) | **GET** /api/Members/{id}/RegisteredInterests | Return list of registered interests of member by ID
[**apiMembersIdStaffGet**](MembersApi.md#apiMembersIdStaffGet) | **GET** /api/Members/{id}/Staff | Return list of staff of member by ID
[**apiMembersIdSynopsisGet**](MembersApi.md#apiMembersIdSynopsisGet) | **GET** /api/Members/{id}/Synopsis | Return synopsis of member by ID
[**apiMembersIdThumbnailGet**](MembersApi.md#apiMembersIdThumbnailGet) | **GET** /api/Members/{id}/Thumbnail | Return thumbnail of member by ID
[**apiMembersIdThumbnailUrlGet**](MembersApi.md#apiMembersIdThumbnailUrlGet) | **GET** /api/Members/{id}/ThumbnailUrl | Return thumbnail url of member by ID
[**apiMembersIdVotingGet**](MembersApi.md#apiMembersIdVotingGet) | **GET** /api/Members/{id}/Voting | Return list of votes by member by ID
[**apiMembersIdWrittenQuestionsGet**](MembersApi.md#apiMembersIdWrittenQuestionsGet) | **GET** /api/Members/{id}/WrittenQuestions | Return list of written questions by member by ID
[**apiMembersSearchGet**](MembersApi.md#apiMembersSearchGet) | **GET** /api/Members/Search | Returns a list of current members of the Commons or Lords
[**apiMembersSearchHistoricalGet**](MembersApi.md#apiMembersSearchHistoricalGet) | **GET** /api/Members/SearchHistorical | Returns a list of members of the Commons or Lords



## apiMembersHistoryGet

> [MemberHistoryItem] apiMembersHistoryGet(opts)

Return members by ID with list of their historical names, parties and memberships

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let opts = {
  'ids': [null] // [Number] | List of MemberIds to find
};
apiInstance.apiMembersHistoryGet(opts, (error, data, response) => {
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
 **ids** | [**[Number]**](Number.md)| List of MemberIds to find | [optional] 

### Return type

[**[MemberHistoryItem]**](MemberHistoryItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdBiographyGet

> MemberBiographyItem apiMembersIdBiographyGet(id)

Return biography of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Biography of Member by ID specified
apiInstance.apiMembersIdBiographyGet(id, (error, data, response) => {
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
 **id** | **Number**| Biography of Member by ID specified | 

### Return type

[**MemberBiographyItem**](MemberBiographyItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdContactGet

> ContactInformationListItem apiMembersIdContactGet(id)

Return list of contact details of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Contact details of Member by ID specified
apiInstance.apiMembersIdContactGet(id, (error, data, response) => {
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
 **id** | **Number**| Contact details of Member by ID specified | 

### Return type

[**ContactInformationListItem**](ContactInformationListItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdContributionSummaryGet

> DebateContributionMembersServiceSearchResult apiMembersIdContributionSummaryGet(id, opts)

Return contribution summary of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Contribution summary of Member by ID specified
let opts = {
  'page': 56 // Number | 
};
apiInstance.apiMembersIdContributionSummaryGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Contribution summary of Member by ID specified | 
 **page** | **Number**|  | [optional] 

### Return type

[**DebateContributionMembersServiceSearchResult**](DebateContributionMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdEdmsGet

> EarlyDayMotionMembersServiceSearchResult apiMembersIdEdmsGet(id, opts)

Return list of early day motions of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Early day motions of Member by ID specified
let opts = {
  'page': 56 // Number | 
};
apiInstance.apiMembersIdEdmsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Early day motions of Member by ID specified | 
 **page** | **Number**|  | [optional] 

### Return type

[**EarlyDayMotionMembersServiceSearchResult**](EarlyDayMotionMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdExperienceGet

> BiographyExperienceListItem apiMembersIdExperienceGet(id)

Return experience of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Experience of Member by ID specified
apiInstance.apiMembersIdExperienceGet(id, (error, data, response) => {
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
 **id** | **Number**| Experience of Member by ID specified | 

### Return type

[**BiographyExperienceListItem**](BiographyExperienceListItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdFocusGet

> MemberFocusListItem apiMembersIdFocusGet(id)

Return list of areas of focus of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Areas of focus of Member by ID specified
apiInstance.apiMembersIdFocusGet(id, (error, data, response) => {
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
 **id** | **Number**| Areas of focus of Member by ID specified | 

### Return type

[**MemberFocusListItem**](MemberFocusListItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdGet

> MemberItem apiMembersIdGet(id, opts)

Return member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Member by ID specified
let opts = {
  'detailsForDate': new Date("2013-10-20T19:20:30+01:00") // Date | Member object will be populated with details from the date specified
};
apiInstance.apiMembersIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Member by ID specified | 
 **detailsForDate** | **Date**| Member object will be populated with details from the date specified | [optional] 

### Return type

[**MemberItem**](MemberItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdLatestElectionResultGet

> ElectionResultItem apiMembersIdLatestElectionResultGet(id)

Return latest election result of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Latest election result of Member by ID specified
apiInstance.apiMembersIdLatestElectionResultGet(id, (error, data, response) => {
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
 **id** | **Number**| Latest election result of Member by ID specified | 

### Return type

[**ElectionResultItem**](ElectionResultItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdPortraitGet

> apiMembersIdPortraitGet(id, opts)

Return portrait of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Portrait of Member by ID specified
let opts = {
  'cropType': new MembersApi.PortraitCropEnum(), // PortraitCropEnum | 
  'webVersion': true // Boolean | 
};
apiInstance.apiMembersIdPortraitGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Portrait of Member by ID specified | 
 **cropType** | [**PortraitCropEnum**](.md)|  | [optional] 
 **webVersion** | **Boolean**|  | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiMembersIdPortraitUrlGet

> StringItem apiMembersIdPortraitUrlGet(id)

Return portrait url of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Portrait url of Member by ID specified
apiInstance.apiMembersIdPortraitUrlGet(id, (error, data, response) => {
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
 **id** | **Number**| Portrait url of Member by ID specified | 

### Return type

[**StringItem**](StringItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdRegisteredInterestsGet

> RegisteredInterestCategoryListItem apiMembersIdRegisteredInterestsGet(id, opts)

Return list of registered interests of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Registered interests of Member by ID specified
let opts = {
  'house': new MembersApi.House() // House | Registered interests of Member by House specified
};
apiInstance.apiMembersIdRegisteredInterestsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Registered interests of Member by ID specified | 
 **house** | [**House**](.md)| Registered interests of Member by House specified | [optional] 

### Return type

[**RegisteredInterestCategoryListItem**](RegisteredInterestCategoryListItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdStaffGet

> StaffListItem apiMembersIdStaffGet(id)

Return list of staff of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Staff of Member by ID specified
apiInstance.apiMembersIdStaffGet(id, (error, data, response) => {
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
 **id** | **Number**| Staff of Member by ID specified | 

### Return type

[**StaffListItem**](StaffListItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdSynopsisGet

> StringItem apiMembersIdSynopsisGet(id)

Return synopsis of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Synopsis of Member by ID specified
apiInstance.apiMembersIdSynopsisGet(id, (error, data, response) => {
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
 **id** | **Number**| Synopsis of Member by ID specified | 

### Return type

[**StringItem**](StringItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdThumbnailGet

> apiMembersIdThumbnailGet(id)

Return thumbnail of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Thumbnail of Member by ID specified
apiInstance.apiMembersIdThumbnailGet(id, (error, data, response) => {
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
 **id** | **Number**| Thumbnail of Member by ID specified | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiMembersIdThumbnailUrlGet

> StringItem apiMembersIdThumbnailUrlGet(id)

Return thumbnail url of member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Thumbnail url of Member by ID specified
apiInstance.apiMembersIdThumbnailUrlGet(id, (error, data, response) => {
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
 **id** | **Number**| Thumbnail url of Member by ID specified | 

### Return type

[**StringItem**](StringItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdVotingGet

> VoteMembersServiceSearchResult apiMembersIdVotingGet(id, house, opts)

Return list of votes by member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Votes by Member by ID specified
let house = new MembersApi.House(); // House | 
let opts = {
  'page': 56 // Number | 
};
apiInstance.apiMembersIdVotingGet(id, house, opts, (error, data, response) => {
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
 **id** | **Number**| Votes by Member by ID specified | 
 **house** | [**House**](.md)|  | 
 **page** | **Number**|  | [optional] 

### Return type

[**VoteMembersServiceSearchResult**](VoteMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersIdWrittenQuestionsGet

> WrittenQuestionMembersServiceSearchResult apiMembersIdWrittenQuestionsGet(id, opts)

Return list of written questions by member by ID

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let id = 56; // Number | Written questions by Member by ID specified
let opts = {
  'page': 56 // Number | 
};
apiInstance.apiMembersIdWrittenQuestionsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Written questions by Member by ID specified | 
 **page** | **Number**|  | [optional] 

### Return type

[**WrittenQuestionMembersServiceSearchResult**](WrittenQuestionMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersSearchGet

> MemberMembersServiceSearchResult apiMembersSearchGet(opts)

Returns a list of current members of the Commons or Lords

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let opts = {
  'name': "name_example", // String | Members where name contains term specified
  'location': "location_example", // String | Members where postcode or geographical location matches the term specified
  'postTitle': "postTitle_example", // String | Members which have held the post specified
  'partyId': 56, // Number | Members which are currently affiliated with party with party ID
  'house': new MembersApi.House(), // House | Members where their most recent house is the house specified
  'constituencyId': 56, // Number | Members which currently hold the constituency with constituency id
  'nameStartsWith': "nameStartsWith_example", // String | Members with surname begining with letter(s) specified
  'gender': "gender_example", // String | Members with the gender specified
  'membershipStartedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Members who started on or after the date given
  'membershipEndedMembershipEndedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Members who left the House on or after the date given
  'membershipEndedMembershipEndReasonIds': [null], // [Number] | 
  'membershipInDateRangeWasMemberOnOrAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Members who were active on or after the date specified
  'membershipInDateRangeWasMemberOnOrBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Members who were active on or before the date specified
  'membershipInDateRangeWasMemberOfHouse': new MembersApi.House(), // House | Members who were active in the house specifid
  'isEligible': true, // Boolean | Members currently Eligible to sit in their House
  'isCurrentMember': true, // Boolean | Members who are current or former members
  'policyInterestId': 56, // Number | Members with specified policy interest
  'experience': "experience_example", // String | Members with specified experience
  'skip': 0, // Number | The number of records to skip from the first, default is 0
  'take': 20 // Number | The number of records to return, default is 20. Maximum is 20
};
apiInstance.apiMembersSearchGet(opts, (error, data, response) => {
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
 **name** | **String**| Members where name contains term specified | [optional] 
 **location** | **String**| Members where postcode or geographical location matches the term specified | [optional] 
 **postTitle** | **String**| Members which have held the post specified | [optional] 
 **partyId** | **Number**| Members which are currently affiliated with party with party ID | [optional] 
 **house** | [**House**](.md)| Members where their most recent house is the house specified | [optional] 
 **constituencyId** | **Number**| Members which currently hold the constituency with constituency id | [optional] 
 **nameStartsWith** | **String**| Members with surname begining with letter(s) specified | [optional] 
 **gender** | **String**| Members with the gender specified | [optional] 
 **membershipStartedSince** | **Date**| Members who started on or after the date given | [optional] 
 **membershipEndedMembershipEndedSince** | **Date**| Members who left the House on or after the date given | [optional] 
 **membershipEndedMembershipEndReasonIds** | [**[Number]**](Number.md)|  | [optional] 
 **membershipInDateRangeWasMemberOnOrAfter** | **Date**| Members who were active on or after the date specified | [optional] 
 **membershipInDateRangeWasMemberOnOrBefore** | **Date**| Members who were active on or before the date specified | [optional] 
 **membershipInDateRangeWasMemberOfHouse** | [**House**](.md)| Members who were active in the house specifid | [optional] 
 **isEligible** | **Boolean**| Members currently Eligible to sit in their House | [optional] 
 **isCurrentMember** | **Boolean**| Members who are current or former members | [optional] 
 **policyInterestId** | **Number**| Members with specified policy interest | [optional] 
 **experience** | **String**| Members with specified experience | [optional] 
 **skip** | **Number**| The number of records to skip from the first, default is 0 | [optional] [default to 0]
 **take** | **Number**| The number of records to return, default is 20. Maximum is 20 | [optional] [default to 20]

### Return type

[**MemberMembersServiceSearchResult**](MemberMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiMembersSearchHistoricalGet

> MemberMembersServiceSearchResult apiMembersSearchHistoricalGet(opts)

Returns a list of members of the Commons or Lords

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.MembersApi();
let opts = {
  'name': "name_example", // String | Members with names containing the term specified
  'dateToSearchFor': new Date("2013-10-20T19:20:30+01:00"), // Date | Members that were an active member of the Commons or Lords on the date specified
  'skip': 0, // Number | The number of records to skip from the first, default is 0
  'take': 20 // Number | The number of records to return, default is 20. Maximum is 20
};
apiInstance.apiMembersSearchHistoricalGet(opts, (error, data, response) => {
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
 **name** | **String**| Members with names containing the term specified | [optional] 
 **dateToSearchFor** | **Date**| Members that were an active member of the Commons or Lords on the date specified | [optional] 
 **skip** | **Number**| The number of records to skip from the first, default is 0 | [optional] [default to 0]
 **take** | **Number**| The number of records to return, default is 20. Maximum is 20 | [optional] [default to 20]

### Return type

[**MemberMembersServiceSearchResult**](MemberMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

