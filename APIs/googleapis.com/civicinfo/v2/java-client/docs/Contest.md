

# Contest

Information about a contest that appears on a voter's ballot.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ballotPlacement** | **String** | A number specifying the position of this contest on the voter&#39;s ballot. |  [optional] |
|**ballotTitle** | **String** | The official title on the ballot for this contest, only where available. |  [optional] |
|**candidates** | [**List&lt;Candidate&gt;**](Candidate.md) | The candidate choices for this contest. |  [optional] |
|**district** | [**ElectoralDistrict**](ElectoralDistrict.md) |  |  [optional] |
|**electorateSpecifications** | **String** | A description of any additional eligibility requirements for voting in this contest. |  [optional] |
|**level** | [**List&lt;LevelEnum&gt;**](#List&lt;LevelEnum&gt;) | The levels of government of the office for this contest. There may be more than one in cases where a jurisdiction effectively acts at two different levels of government; for example, the mayor of the District of Columbia acts at \&quot;locality\&quot; level, but also effectively at both \&quot;administrative-area-2\&quot; and \&quot;administrative-area-1\&quot;. |  [optional] |
|**numberElected** | **String** | The number of candidates that will be elected to office in this contest. |  [optional] |
|**numberVotingFor** | **String** | The number of candidates that a voter may vote for in this contest. |  [optional] |
|**office** | **String** | The name of the office for this contest. |  [optional] |
|**primaryParties** | **List&lt;String&gt;** | If this is a partisan election, the name of the party/parties it is for. |  [optional] |
|**referendumBallotResponses** | **List&lt;String&gt;** | The set of ballot responses for the referendum. A ballot response represents a line on the ballot. Common examples might include \&quot;yes\&quot; or \&quot;no\&quot; for referenda. This field is only populated for contests of type &#39;Referendum&#39;. |  [optional] |
|**referendumBrief** | **String** | Specifies a short summary of the referendum that is typically on the ballot below the title but above the text. This field is only populated for contests of type &#39;Referendum&#39;. |  [optional] |
|**referendumConStatement** | **String** | A statement in opposition to the referendum. It does not necessarily appear on the ballot. This field is only populated for contests of type &#39;Referendum&#39;. |  [optional] |
|**referendumEffectOfAbstain** | **String** | Specifies what effect abstaining (not voting) on the proposition will have (i.e. whether abstaining is considered a vote against it). This field is only populated for contests of type &#39;Referendum&#39;. |  [optional] |
|**referendumPassageThreshold** | **String** | The threshold of votes that the referendum needs in order to pass, e.g. \&quot;two-thirds\&quot;. This field is only populated for contests of type &#39;Referendum&#39;. |  [optional] |
|**referendumProStatement** | **String** | A statement in favor of the referendum. It does not necessarily appear on the ballot. This field is only populated for contests of type &#39;Referendum&#39;. |  [optional] |
|**referendumSubtitle** | **String** | A brief description of the referendum. This field is only populated for contests of type &#39;Referendum&#39;. |  [optional] |
|**referendumText** | **String** | The full text of the referendum. This field is only populated for contests of type &#39;Referendum&#39;. |  [optional] |
|**referendumTitle** | **String** | The title of the referendum (e.g. &#39;Proposition 42&#39;). This field is only populated for contests of type &#39;Referendum&#39;. |  [optional] |
|**referendumUrl** | **String** | A link to the referendum. This field is only populated for contests of type &#39;Referendum&#39;. |  [optional] |
|**roles** | [**List&lt;RolesEnum&gt;**](#List&lt;RolesEnum&gt;) | The roles which this office fulfills. |  [optional] |
|**sources** | [**List&lt;Source&gt;**](Source.md) | A list of sources for this contest. If multiple sources are listed, the data has been aggregated from those sources. |  [optional] |
|**special** | **String** | \&quot;Yes\&quot; or \&quot;No\&quot; depending on whether this a contest being held outside the normal election cycle. |  [optional] |
|**type** | **String** | The type of contest. Usually this will be &#39;General&#39;, &#39;Primary&#39;, or &#39;Run-off&#39; for contests with candidates. For referenda this will be &#39;Referendum&#39;. For Retention contests this will typically be &#39;Retention&#39;. |  [optional] |



## Enum: List&lt;LevelEnum&gt;

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



