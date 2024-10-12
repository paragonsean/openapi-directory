# PeopleApi.PersonMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **Boolean** | Output only. True if the person resource has been deleted. Populated only for &#x60;people.connections.list&#x60; and &#x60;otherContacts.list&#x60; sync requests. | [optional] [readonly] 
**linkedPeopleResourceNames** | **[String]** | Output only. Resource names of people linked to this resource. | [optional] [readonly] 
**objectType** | **String** | Output only. **DEPRECATED** (Please use &#x60;person.metadata.sources.profileMetadata.objectType&#x60; instead) The type of the person object. | [optional] [readonly] 
**previousResourceNames** | **[String]** | Output only. Any former resource names this person has had. Populated only for &#x60;people.connections.list&#x60; requests that include a sync token. The resource name may change when adding or removing fields that link a contact and profile such as a verified email, verified phone number, or profile URL. | [optional] [readonly] 
**sources** | [**[Source]**](Source.md) | The sources of data for the person. | [optional] 



## Enum: ObjectTypeEnum


* `OBJECT_TYPE_UNSPECIFIED` (value: `"OBJECT_TYPE_UNSPECIFIED"`)

* `PERSON` (value: `"PERSON"`)

* `PAGE` (value: `"PAGE"`)




