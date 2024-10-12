

# UpdateContactPhotoRequest

A request to update an existing contact's photo. All requests must have a valid photo format: JPEG or PNG.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**personFields** | **String** | Optional. A field mask to restrict which fields on the person are returned. Multiple fields can be specified by separating them with commas. Defaults to empty if not set, which will skip the post mutate get. Valid values are: * addresses * ageRanges * biographies * birthdays * calendarUrls * clientData * coverPhotos * emailAddresses * events * externalIds * genders * imClients * interests * locales * locations * memberships * metadata * miscKeywords * names * nicknames * occupations * organizations * phoneNumbers * photos * relations * sipAddresses * skills * urls * userDefined |  [optional] |
|**photoBytes** | **byte[]** | Required. Raw photo bytes |  [optional] |
|**sources** | [**List&lt;SourcesEnum&gt;**](#List&lt;SourcesEnum&gt;) | Optional. A mask of what source types to return. Defaults to READ_SOURCE_TYPE_CONTACT and READ_SOURCE_TYPE_PROFILE if not set. |  [optional] |



## Enum: List&lt;SourcesEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;READ_SOURCE_TYPE_UNSPECIFIED&quot; |
| PROFILE | &quot;READ_SOURCE_TYPE_PROFILE&quot; |
| CONTACT | &quot;READ_SOURCE_TYPE_CONTACT&quot; |
| DOMAIN_CONTACT | &quot;READ_SOURCE_TYPE_DOMAIN_CONTACT&quot; |



