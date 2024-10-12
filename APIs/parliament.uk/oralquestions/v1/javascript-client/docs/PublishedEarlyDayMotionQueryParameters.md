# HouseOfCommonsOralAndWrittenQuestionsApi.PublishedEarlyDayMotionQueryParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentStatusDateEnd** | **Date** | Early Day Motions where the current status has been set on or before the date provided. Date format YYYY-MM-DD. | [optional] 
**currentStatusDateStart** | **Date** | Early Day Motions where the current status has been set on or after the date provided. Date format YYYY-MM-DD. | [optional] 
**edmIds** | **[Number]** | Early Day Motions with an ID in the list provided. | [optional] 
**includeSponsoredByMember** | **Boolean** | Include Early Day Motions sponsored by Member specified | [optional] 
**isPrayer** | **Boolean** | Early Day Motions which are a prayer against a Negative Statutory Instrument. | [optional] 
**memberId** | **Number** | Return Early Day Motions tabled by Member with ID provided. | [optional] 
**orderBy** | **String** | Order results by date tabled, title or signature count. Default is date tabled. | [optional] 
**searchTerm** | **String** | Early Day Motions where the title includes the search term provided. | [optional] 
**skip** | **Number** | The number of records to skip from the first, default is 0. | [optional] 
**statuses** | **[String]** | Early Day Motions where current status is in the selected list. | [optional] 
**tabledEndDate** | **Date** | Early Day Motions where the date tabled is on or before the date provided. Date format YYYY-MM-DD. | [optional] 
**tabledStartDate** | **Date** | Early Day Motions where the date tabled is on or after the date provided. Date format YYYY-MM-DD. | [optional] 
**take** | **Number** | The number of records to return, default is 25, maximum is 100. | [optional] 
**uINWithAmendmentSuffix** | **String** | Early Day Motions with an UINWithAmendmentSuffix provided. | [optional] 



## Enum: OrderByEnum


* `DateTabledAsc` (value: `"DateTabledAsc"`)

* `DateTabledDesc` (value: `"DateTabledDesc"`)

* `TitleAsc` (value: `"TitleAsc"`)

* `TitleDesc` (value: `"TitleDesc"`)

* `SignatureCountAsc` (value: `"SignatureCountAsc"`)

* `SignatureCountDesc` (value: `"SignatureCountDesc"`)





## Enum: [StatusesEnum]


* `Published` (value: `"Published"`)

* `Withdrawn` (value: `"Withdrawn"`)




