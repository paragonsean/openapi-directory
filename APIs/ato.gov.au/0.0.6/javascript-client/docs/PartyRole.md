# BusinessRegistries.PartyRole

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fromDate** | **Date** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 
**id** | [**RoleId**](RoleId.md) | The resource&#39;s unique identifier. | [optional] [readonly] 
**partyRoleType** | **String** | The party&#39;s role type. | [optional] [default to &#39;Employee&#39;]
**relatedPartyId** | [**PartyId**](PartyId.md) | The related party&#39;s unique identifier. | 
**relatedPartyRoleType** | **String** | The related party&#39;s role type. | [optional] [default to &#39;Employer&#39;]
**relationshipType** | **String** | The relationship type. | [default to &#39;Employment&#39;]
**toDate** | **Date** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 



## Enum: PartyRoleTypeEnum


* `Director` (value: `"Director"`)

* `Employee` (value: `"Employee"`)

* `Member` (value: `"Member"`)

* `Partner` (value: `"Partner"`)

* `Trustee` (value: `"Trustee"`)





## Enum: RelatedPartyRoleTypeEnum


* `Association` (value: `"Association"`)

* `Company` (value: `"Company"`)

* `Employer` (value: `"Employer"`)

* `Organisation` (value: `"Organisation"`)

* `Partnership` (value: `"Partnership"`)

* `Trust` (value: `"Trust"`)





## Enum: RelationshipTypeEnum


* `Directorship` (value: `"Directorship"`)

* `Employment` (value: `"Employment"`)

* `Membership` (value: `"Membership"`)

* `Partnership` (value: `"Partnership"`)

* `Trusteeship` (value: `"Trusteeship"`)




