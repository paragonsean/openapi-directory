

# Office

Information about an Office held by one or more Officials.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**divisionId** | **String** | The OCD ID of the division with which this office is associated. |  [optional] |
|**levels** | [**List&lt;LevelsEnum&gt;**](#List&lt;LevelsEnum&gt;) | The levels of government of which this office is part. There may be more than one in cases where a jurisdiction effectively acts at two different levels of government; for example, the mayor of the District of Columbia acts at \&quot;locality\&quot; level, but also effectively at both \&quot;administrative-area-2\&quot; and \&quot;administrative-area-1\&quot;. |  [optional] |
|**name** | **String** | The human-readable name of the office. |  [optional] |
|**officialIndices** | **List&lt;Integer&gt;** | List of indices in the officials array of people who presently hold this office. |  [optional] |
|**roles** | [**List&lt;RolesEnum&gt;**](#List&lt;RolesEnum&gt;) | The roles which this office fulfills. Roles are not meant to be exhaustive, or to exactly specify the entire set of responsibilities of a given office, but are meant to be rough categories that are useful for general selection from or sorting of a list of offices. |  [optional] |
|**sources** | [**List&lt;Source&gt;**](Source.md) | A list of sources for this office. If multiple sources are listed, the data has been aggregated from those sources. |  [optional] |



## Enum: List&lt;LevelsEnum&gt;

| Name | Value |
|---- | -----|
| INTERNATIONAL | &quot;international&quot; |
| COUNTRY | &quot;country&quot; |
| ADMINISTRATIVE_AREA1 | &quot;administrativeArea1&quot; |
| REGIONAL | &quot;regional&quot; |
| ADMINISTRATIVE_AREA2 | &quot;administrativeArea2&quot; |
| LOCALITY | &quot;locality&quot; |
| SUB_LOCALITY1 | &quot;subLocality1&quot; |
| SUB_LOCALITY2 | &quot;subLocality2&quot; |
| SPECIAL | &quot;special&quot; |



## Enum: List&lt;RolesEnum&gt;

| Name | Value |
|---- | -----|
| HEAD_OF_STATE | &quot;headOfState&quot; |
| HEAD_OF_GOVERNMENT | &quot;headOfGovernment&quot; |
| DEPUTY_HEAD_OF_GOVERNMENT | &quot;deputyHeadOfGovernment&quot; |
| GOVERNMENT_OFFICER | &quot;governmentOfficer&quot; |
| EXECUTIVE_COUNCIL | &quot;executiveCouncil&quot; |
| LEGISLATOR_UPPER_BODY | &quot;legislatorUpperBody&quot; |
| LEGISLATOR_LOWER_BODY | &quot;legislatorLowerBody&quot; |
| HIGHEST_COURT_JUDGE | &quot;highestCourtJudge&quot; |
| JUDGE | &quot;judge&quot; |
| SCHOOL_BOARD | &quot;schoolBoard&quot; |
| SPECIAL_PURPOSE_OFFICER | &quot;specialPurposeOfficer&quot; |
| OTHER_ROLE | &quot;otherRole&quot; |



