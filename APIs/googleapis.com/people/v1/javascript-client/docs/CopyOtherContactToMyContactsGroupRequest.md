# PeopleApi.CopyOtherContactToMyContactsGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyMask** | **String** | Required. A field mask to restrict which fields are copied into the new contact. Valid values are: * emailAddresses * names * phoneNumbers | [optional] 
**readMask** | **String** | Optional. A field mask to restrict which fields on the person are returned. Multiple fields can be specified by separating them with commas. Defaults to the copy mask with metadata and membership fields if not set. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined | [optional] 
**sources** | **[String]** | Optional. A mask of what source types to return. Defaults to READ_SOURCE_TYPE_CONTACT and READ_SOURCE_TYPE_PROFILE if not set. | [optional] 



## Enum: [SourcesEnum]


* `UNSPECIFIED` (value: `"READ_SOURCE_TYPE_UNSPECIFIED"`)

* `PROFILE` (value: `"READ_SOURCE_TYPE_PROFILE"`)

* `CONTACT` (value: `"READ_SOURCE_TYPE_CONTACT"`)

* `DOMAIN_CONTACT` (value: `"READ_SOURCE_TYPE_DOMAIN_CONTACT"`)




