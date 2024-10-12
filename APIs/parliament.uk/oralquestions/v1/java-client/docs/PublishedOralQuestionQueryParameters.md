

# PublishedOralQuestionQueryParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answeringBodyIds** | **List&lt;Integer&gt;** | Which answering body is to respond. A list of answering bodies can be found &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;http://data.parliament.uk/membersdataplatform/services/mnis/referencedata/AnsweringBodies/\&quot;&gt;here&lt;/a&gt;. |  [optional] |
|**answeringDateEnd** | **OffsetDateTime** | Oral Questions where the answering date has been set on or before the date provided. Date format YYYY-MM-DD. |  [optional] |
|**answeringDateStart** | **OffsetDateTime** | Oral Questions where the answering date has been set on or after the date provided. Date format YYYY-MM-DD. |  [optional] |
|**askingMemberIds** | **List&lt;Integer&gt;** | The ID of the member asking the question. Lists of member IDs for each house are available &lt;a href&#x3D;\&quot;http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house&#x3D;Commons\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Commons&lt;/a&gt; and &lt;a href&#x3D;\&quot;http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house&#x3D;Lords\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Lords&lt;/a&gt;. |  [optional] |
|**oralQuestionTimeId** | **Integer** | Oral Questions where the question is within the question time with the ID provided |  [optional] |
|**questionType** | [**QuestionTypeEnum**](#QuestionTypeEnum) | Oral Questions where the question type is the selected type, substantive or topical. |  [optional] |
|**skip** | **Integer** | The number of records to skip from the first, default is 0. |  [optional] |
|**take** | **Integer** | The number of records to return, default is 25, maximum is 100. |  [optional] |
|**uiNs** | **List&lt;Integer&gt;** | The UIN for the question - note that UINs reset at the start of each Parliamentary session. |  [optional] |



## Enum: QuestionTypeEnum

| Name | Value |
|---- | -----|
| SUBSTANTIVE | &quot;Substantive&quot; |
| TOPICAL | &quot;Topical&quot; |



