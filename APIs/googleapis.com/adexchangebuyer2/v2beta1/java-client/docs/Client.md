

# Client

A client resource represents a client buyer—an agency, a brand, or an advertiser customer of the sponsor buyer. Users associated with the client buyer have restricted access to the Marketplace and certain other sections of the Authorized Buyers UI based on the role granted to the client buyer. All fields are required unless otherwise specified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientAccountId** | **String** | The globally-unique numerical ID of the client. The value of this field is ignored in create and update operations. |  [optional] |
|**clientName** | **String** | Name used to represent this client to publishers. You may have multiple clients that map to the same entity, but for each client the combination of &#x60;clientName&#x60; and entity must be unique. You can specify this field as empty. Maximum length of 255 characters is allowed. |  [optional] |
|**entityId** | **String** | Numerical identifier of the client entity. The entity can be an advertiser, a brand, or an agency. This identifier is unique among all the entities with the same type. The value of this field is ignored if the entity type is not provided. A list of all known advertisers with their identifiers is available in the [advertisers.txt](https://storage.googleapis.com/adx-rtb-dictionaries/advertisers.txt) file. A list of all known brands with their identifiers is available in the [brands.txt](https://storage.googleapis.com/adx-rtb-dictionaries/brands.txt) file. A list of all known agencies with their identifiers is available in the [agencies.txt](https://storage.googleapis.com/adx-rtb-dictionaries/agencies.txt) file. |  [optional] |
|**entityName** | **String** | The name of the entity. This field is automatically fetched based on the type and ID. The value of this field is ignored in create and update operations. |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | An optional field for specifying the type of the client entity: &#x60;ADVERTISER&#x60;, &#x60;BRAND&#x60;, or &#x60;AGENCY&#x60;. |  [optional] |
|**partnerClientId** | **String** | Optional arbitrary unique identifier of this client buyer from the standpoint of its Ad Exchange sponsor buyer. This field can be used to associate a client buyer with the identifier in the namespace of its sponsor buyer, lookup client buyers by that identifier and verify whether an Ad Exchange counterpart of a given client buyer already exists. If present, must be unique among all the client buyers for its Ad Exchange sponsor buyer. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | The role which is assigned to the client buyer. Each role implies a set of permissions granted to the client. Must be one of &#x60;CLIENT_DEAL_VIEWER&#x60;, &#x60;CLIENT_DEAL_NEGOTIATOR&#x60; or &#x60;CLIENT_DEAL_APPROVER&#x60;. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the client buyer. |  [optional] |
|**visibleToSeller** | **Boolean** | Whether the client buyer will be visible to sellers. |  [optional] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| ENTITY_TYPE_UNSPECIFIED | &quot;ENTITY_TYPE_UNSPECIFIED&quot; |
| ADVERTISER | &quot;ADVERTISER&quot; |
| BRAND | &quot;BRAND&quot; |
| AGENCY | &quot;AGENCY&quot; |
| ENTITY_TYPE_UNCLASSIFIED | &quot;ENTITY_TYPE_UNCLASSIFIED&quot; |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ROLE_UNSPECIFIED | &quot;CLIENT_ROLE_UNSPECIFIED&quot; |
| DEAL_VIEWER | &quot;CLIENT_DEAL_VIEWER&quot; |
| DEAL_NEGOTIATOR | &quot;CLIENT_DEAL_NEGOTIATOR&quot; |
| DEAL_APPROVER | &quot;CLIENT_DEAL_APPROVER&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CLIENT_STATUS_UNSPECIFIED | &quot;CLIENT_STATUS_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |



