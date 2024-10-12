# GoogleCivicInformationApi.Contest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ballotPlacement** | **String** | A number specifying the position of this contest on the voter&#39;s ballot. | [optional] 
**ballotTitle** | **String** | The official title on the ballot for this contest, only where available. | [optional] 
**candidates** | [**[Candidate]**](Candidate.md) | The candidate choices for this contest. | [optional] 
**district** | [**ElectoralDistrict**](ElectoralDistrict.md) |  | [optional] 
**electorateSpecifications** | **String** | A description of any additional eligibility requirements for voting in this contest. | [optional] 
**level** | **[String]** | The levels of government of the office for this contest. There may be more than one in cases where a jurisdiction effectively acts at two different levels of government; for example, the mayor of the District of Columbia acts at \&quot;locality\&quot; level, but also effectively at both \&quot;administrative-area-2\&quot; and \&quot;administrative-area-1\&quot;. | [optional] 
**numberElected** | **String** | The number of candidates that will be elected to office in this contest. | [optional] 
**numberVotingFor** | **String** | The number of candidates that a voter may vote for in this contest. | [optional] 
**office** | **String** | The name of the office for this contest. | [optional] 
**primaryParties** | **[String]** | If this is a partisan election, the name of the party/parties it is for. | [optional] 
**referendumBallotResponses** | **[String]** | The set of ballot responses for the referendum. A ballot response represents a line on the ballot. Common examples might include \&quot;yes\&quot; or \&quot;no\&quot; for referenda. This field is only populated for contests of type &#39;Referendum&#39;. | [optional] 
**referendumBrief** | **String** | Specifies a short summary of the referendum that is typically on the ballot below the title but above the text. This field is only populated for contests of type &#39;Referendum&#39;. | [optional] 
**referendumConStatement** | **String** | A statement in opposition to the referendum. It does not necessarily appear on the ballot. This field is only populated for contests of type &#39;Referendum&#39;. | [optional] 
**referendumEffectOfAbstain** | **String** | Specifies what effect abstaining (not voting) on the proposition will have (i.e. whether abstaining is considered a vote against it). This field is only populated for contests of type &#39;Referendum&#39;. | [optional] 
**referendumPassageThreshold** | **String** | The threshold of votes that the referendum needs in order to pass, e.g. \&quot;two-thirds\&quot;. This field is only populated for contests of type &#39;Referendum&#39;. | [optional] 
**referendumProStatement** | **String** | A statement in favor of the referendum. It does not necessarily appear on the ballot. This field is only populated for contests of type &#39;Referendum&#39;. | [optional] 
**referendumSubtitle** | **String** | A brief description of the referendum. This field is only populated for contests of type &#39;Referendum&#39;. | [optional] 
**referendumText** | **String** | The full text of the referendum. This field is only populated for contests of type &#39;Referendum&#39;. | [optional] 
**referendumTitle** | **String** | The title of the referendum (e.g. &#39;Proposition 42&#39;). This field is only populated for contests of type &#39;Referendum&#39;. | [optional] 
**referendumUrl** | **String** | A link to the referendum. This field is only populated for contests of type &#39;Referendum&#39;. | [optional] 
**roles** | **[String]** | The roles which this office fulfills. | [optional] 
**sources** | [**[Source]**](Source.md) | A list of sources for this contest. If multiple sources are listed, the data has been aggregated from those sources. | [optional] 
**special** | **String** | \&quot;Yes\&quot; or \&quot;No\&quot; depending on whether this a contest being held outside the normal election cycle. | [optional] 
**type** | **String** | The type of contest. Usually this will be &#39;General&#39;, &#39;Primary&#39;, or &#39;Run-off&#39; for contests with candidates. For referenda this will be &#39;Referendum&#39;. For Retention contests this will typically be &#39;Retention&#39;. | [optional] 



## Enum: [LevelEnum]


* `international` (value: `"international"`)

* `country` (value: `"country"`)

* `administrativeArea1` (value: `"administrativeArea1"`)

* `regional` (value: `"regional"`)

* `administrativeArea2` (value: `"administrativeArea2"`)

* `locality` (value: `"locality"`)

* `subLocality1` (value: `"subLocality1"`)

* `subLocality2` (value: `"subLocality2"`)

* `special` (value: `"special"`)





## Enum: [RolesEnum]


* `headOfState` (value: `"headOfState"`)

* `headOfGovernment` (value: `"headOfGovernment"`)

* `deputyHeadOfGovernment` (value: `"deputyHeadOfGovernment"`)

* `governmentOfficer` (value: `"governmentOfficer"`)

* `executiveCouncil` (value: `"executiveCouncil"`)

* `legislatorUpperBody` (value: `"legislatorUpperBody"`)

* `legislatorLowerBody` (value: `"legislatorLowerBody"`)

* `highestCourtJudge` (value: `"highestCourtJudge"`)

* `judge` (value: `"judge"`)

* `schoolBoard` (value: `"schoolBoard"`)

* `specialPurposeOfficer` (value: `"specialPurposeOfficer"`)

* `otherRole` (value: `"otherRole"`)




