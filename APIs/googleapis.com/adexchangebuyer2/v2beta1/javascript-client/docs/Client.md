# AdExchangeBuyerApiIi.Client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientAccountId** | **String** | The globally-unique numerical ID of the client. The value of this field is ignored in create and update operations. | [optional] 
**clientName** | **String** | Name used to represent this client to publishers. You may have multiple clients that map to the same entity, but for each client the combination of &#x60;clientName&#x60; and entity must be unique. You can specify this field as empty. Maximum length of 255 characters is allowed. | [optional] 
**entityId** | **String** | Numerical identifier of the client entity. The entity can be an advertiser, a brand, or an agency. This identifier is unique among all the entities with the same type. The value of this field is ignored if the entity type is not provided. A list of all known advertisers with their identifiers is available in the [advertisers.txt](https://storage.googleapis.com/adx-rtb-dictionaries/advertisers.txt) file. A list of all known brands with their identifiers is available in the [brands.txt](https://storage.googleapis.com/adx-rtb-dictionaries/brands.txt) file. A list of all known agencies with their identifiers is available in the [agencies.txt](https://storage.googleapis.com/adx-rtb-dictionaries/agencies.txt) file. | [optional] 
**entityName** | **String** | The name of the entity. This field is automatically fetched based on the type and ID. The value of this field is ignored in create and update operations. | [optional] 
**entityType** | **String** | An optional field for specifying the type of the client entity: &#x60;ADVERTISER&#x60;, &#x60;BRAND&#x60;, or &#x60;AGENCY&#x60;. | [optional] 
**partnerClientId** | **String** | Optional arbitrary unique identifier of this client buyer from the standpoint of its Ad Exchange sponsor buyer. This field can be used to associate a client buyer with the identifier in the namespace of its sponsor buyer, lookup client buyers by that identifier and verify whether an Ad Exchange counterpart of a given client buyer already exists. If present, must be unique among all the client buyers for its Ad Exchange sponsor buyer. | [optional] 
**role** | **String** | The role which is assigned to the client buyer. Each role implies a set of permissions granted to the client. Must be one of &#x60;CLIENT_DEAL_VIEWER&#x60;, &#x60;CLIENT_DEAL_NEGOTIATOR&#x60; or &#x60;CLIENT_DEAL_APPROVER&#x60;. | [optional] 
**status** | **String** | The status of the client buyer. | [optional] 
**visibleToSeller** | **Boolean** | Whether the client buyer will be visible to sellers. | [optional] 



## Enum: EntityTypeEnum


* `ENTITY_TYPE_UNSPECIFIED` (value: `"ENTITY_TYPE_UNSPECIFIED"`)

* `ADVERTISER` (value: `"ADVERTISER"`)

* `BRAND` (value: `"BRAND"`)

* `AGENCY` (value: `"AGENCY"`)

* `ENTITY_TYPE_UNCLASSIFIED` (value: `"ENTITY_TYPE_UNCLASSIFIED"`)





## Enum: RoleEnum


* `ROLE_UNSPECIFIED` (value: `"CLIENT_ROLE_UNSPECIFIED"`)

* `DEAL_VIEWER` (value: `"CLIENT_DEAL_VIEWER"`)

* `DEAL_NEGOTIATOR` (value: `"CLIENT_DEAL_NEGOTIATOR"`)

* `DEAL_APPROVER` (value: `"CLIENT_DEAL_APPROVER"`)





## Enum: StatusEnum


* `CLIENT_STATUS_UNSPECIFIED` (value: `"CLIENT_STATUS_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `ACTIVE` (value: `"ACTIVE"`)




