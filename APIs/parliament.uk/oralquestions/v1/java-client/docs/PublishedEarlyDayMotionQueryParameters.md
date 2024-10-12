

# PublishedEarlyDayMotionQueryParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentStatusDateEnd** | **OffsetDateTime** | Early Day Motions where the current status has been set on or before the date provided. Date format YYYY-MM-DD. |  [optional] |
|**currentStatusDateStart** | **OffsetDateTime** | Early Day Motions where the current status has been set on or after the date provided. Date format YYYY-MM-DD. |  [optional] |
|**edmIds** | **List&lt;Integer&gt;** | Early Day Motions with an ID in the list provided. |  [optional] |
|**includeSponsoredByMember** | **Boolean** | Include Early Day Motions sponsored by Member specified |  [optional] |
|**isPrayer** | **Boolean** | Early Day Motions which are a prayer against a Negative Statutory Instrument. |  [optional] |
|**memberId** | **Integer** | Return Early Day Motions tabled by Member with ID provided. |  [optional] |
|**orderBy** | [**OrderByEnum**](#OrderByEnum) | Order results by date tabled, title or signature count. Default is date tabled. |  [optional] |
|**searchTerm** | **String** | Early Day Motions where the title includes the search term provided. |  [optional] |
|**skip** | **Integer** | The number of records to skip from the first, default is 0. |  [optional] |
|**statuses** | [**List&lt;StatusesEnum&gt;**](#List&lt;StatusesEnum&gt;) | Early Day Motions where current status is in the selected list. |  [optional] |
|**tabledEndDate** | **OffsetDateTime** | Early Day Motions where the date tabled is on or before the date provided. Date format YYYY-MM-DD. |  [optional] |
|**tabledStartDate** | **OffsetDateTime** | Early Day Motions where the date tabled is on or after the date provided. Date format YYYY-MM-DD. |  [optional] |
|**take** | **Integer** | The number of records to return, default is 25, maximum is 100. |  [optional] |
|**uiNWithAmendmentSuffix** | **String** | Early Day Motions with an UINWithAmendmentSuffix provided. |  [optional] |



## Enum: OrderByEnum

| Name | Value |
|---- | -----|
| DATE_TABLED_ASC | &quot;DateTabledAsc&quot; |
| DATE_TABLED_DESC | &quot;DateTabledDesc&quot; |
| TITLE_ASC | &quot;TitleAsc&quot; |
| TITLE_DESC | &quot;TitleDesc&quot; |
| SIGNATURE_COUNT_ASC | &quot;SignatureCountAsc&quot; |
| SIGNATURE_COUNT_DESC | &quot;SignatureCountDesc&quot; |



## Enum: List&lt;StatusesEnum&gt;

| Name | Value |
|---- | -----|
| PUBLISHED | &quot;Published&quot; |
| WITHDRAWN | &quot;Withdrawn&quot; |



