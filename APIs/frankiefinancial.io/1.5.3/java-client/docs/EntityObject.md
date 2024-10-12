

# EntityObject

Describes all of the data being used to verify an entity. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;AddressObject&gt;**](AddressObject.md) | Collection of address objects. |  [optional] |
|**dateOfBirth** | [**DOBObject**](DOBObject.md) |  |  [optional] |
|**entityId** | **UUID** | When an entity is first created, it is assigned an ID. When updating an entity, make sure you set the entityId One exception to this is when an entity is created from a document object. It is expected that this object would be passed into a /check or /entity call to set it.  |  [optional] |
|**entityProfile** | **String** | If the entity is using the new profiles feature, then their profile name will be found here.  Note: If setting a profile, you must ensure that the profile matches a known configuration.  Please contact Frankie developer support if you&#39;re unsure as to what valid values are.  |  [optional] |
|**entityType** | **EnumEntityType** |  |  [optional] |
|**extraData** | [**List&lt;KeyValuePairObject&gt;**](KeyValuePairObject.md) | Set of key-value pairs that provide arbitrary additional type-specific data. You can use these fields to store external IDs, or other non-identity related items if you need to. If updating an existing entity, then existing values with the same name will be overwritten. New values will be added.  See here for more information about possible values you can use:   https://apidocs.frankiefinancial.com/docs/entity-extradata-key-value-pairs  |  [optional] |
|**flags** | [**List&lt;EntityFlagObject&gt;**](EntityFlagObject.md) | Used to set additional information flags with regards to this entity and for ongoing processing.  Flags might include having the entity (not) participate in regular pep/sanctions screening Others will follow over time.  |  [optional] |
|**gender** | **EnumGender** |  |  [optional] |
|**identityDocs** | [**List&lt;IdentityDocumentObject&gt;**](IdentityDocumentObject.md) | Collection of identity documents (photos, scans, selfies, etc) |  [optional] |
|**name** | [**PersonalNameObject**](PersonalNameObject.md) |  |  [optional] |
|**organisationData** | [**OrganisationDataObject**](OrganisationDataObject.md) |  |  [optional] |



