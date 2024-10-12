

# PartyRole

The Party Role resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fromDate** | **OffsetDateTime** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |
|**id** | [**RoleId**](RoleId.md) | The resource&#39;s unique identifier. |  [optional] [readonly] |
|**partyRoleType** | [**PartyRoleTypeEnum**](#PartyRoleTypeEnum) | The party&#39;s role type. |  [optional] |
|**relatedPartyId** | [**PartyId**](PartyId.md) | The related party&#39;s unique identifier. |  |
|**relatedPartyRoleType** | [**RelatedPartyRoleTypeEnum**](#RelatedPartyRoleTypeEnum) | The related party&#39;s role type. |  [optional] |
|**relationshipType** | [**RelationshipTypeEnum**](#RelationshipTypeEnum) | The relationship type. |  |
|**toDate** | **OffsetDateTime** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |



## Enum: PartyRoleTypeEnum

| Name | Value |
|---- | -----|
| DIRECTOR | &quot;Director&quot; |
| EMPLOYEE | &quot;Employee&quot; |
| MEMBER | &quot;Member&quot; |
| PARTNER | &quot;Partner&quot; |
| TRUSTEE | &quot;Trustee&quot; |



## Enum: RelatedPartyRoleTypeEnum

| Name | Value |
|---- | -----|
| ASSOCIATION | &quot;Association&quot; |
| COMPANY | &quot;Company&quot; |
| EMPLOYER | &quot;Employer&quot; |
| ORGANISATION | &quot;Organisation&quot; |
| PARTNERSHIP | &quot;Partnership&quot; |
| TRUST | &quot;Trust&quot; |



## Enum: RelationshipTypeEnum

| Name | Value |
|---- | -----|
| DIRECTORSHIP | &quot;Directorship&quot; |
| EMPLOYMENT | &quot;Employment&quot; |
| MEMBERSHIP | &quot;Membership&quot; |
| PARTNERSHIP | &quot;Partnership&quot; |
| TRUSTEESHIP | &quot;Trusteeship&quot; |



