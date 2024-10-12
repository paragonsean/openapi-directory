# GoogleCivicInformationApi.Office

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**divisionId** | **String** | The OCD ID of the division with which this office is associated. | [optional] 
**levels** | **[String]** | The levels of government of which this office is part. There may be more than one in cases where a jurisdiction effectively acts at two different levels of government; for example, the mayor of the District of Columbia acts at \&quot;locality\&quot; level, but also effectively at both \&quot;administrative-area-2\&quot; and \&quot;administrative-area-1\&quot;. | [optional] 
**name** | **String** | The human-readable name of the office. | [optional] 
**officialIndices** | **[Number]** | List of indices in the officials array of people who presently hold this office. | [optional] 
**roles** | **[String]** | The roles which this office fulfills. Roles are not meant to be exhaustive, or to exactly specify the entire set of responsibilities of a given office, but are meant to be rough categories that are useful for general selection from or sorting of a list of offices. | [optional] 
**sources** | [**[Source]**](Source.md) | A list of sources for this office. If multiple sources are listed, the data has been aggregated from those sources. | [optional] 



## Enum: [LevelsEnum]


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




