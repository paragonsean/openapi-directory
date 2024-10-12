

# BatchUpdateContactsRequest

A request to update a batch of contacts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contacts** | [**Map&lt;String, Person&gt;**](Person.md) | Required. A map of resource names to the person data to be updated. Allows up to 200 contacts in a single request. |  [optional] |
|**readMask** | **String** | Required. A field mask to restrict which fields on each person are returned. Multiple fields can be specified by separating them with commas. If read mask is left empty, the post-mutate-get is skipped and no data will be returned in the response. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined |  [optional] |
|**sources** | [**List&lt;SourcesEnum&gt;**](#List&lt;SourcesEnum&gt;) | Optional. A mask of what source types to return. Defaults to READ_SOURCE_TYPE_CONTACT and READ_SOURCE_TYPE_PROFILE if not set. |  [optional] |
|**updateMask** | **String** | Required. A field mask to restrict which fields on the person are updated. Multiple fields can be specified by separating them with commas. All specified fields will be replaced, or cleared if left empty for each person. Valid values are: * addresses * biographies * birthdays * calendarUrls * clientData * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * relations * sipAddresses * urls * userDefined |  [optional] |



## Enum: List&lt;SourcesEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;READ_SOURCE_TYPE_UNSPECIFIED&quot; |
| PROFILE | &quot;READ_SOURCE_TYPE_PROFILE&quot; |
| CONTACT | &quot;READ_SOURCE_TYPE_CONTACT&quot; |
| DOMAIN_CONTACT | &quot;READ_SOURCE_TYPE_DOMAIN_CONTACT&quot; |



