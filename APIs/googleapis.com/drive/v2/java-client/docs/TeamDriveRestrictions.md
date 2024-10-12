

# TeamDriveRestrictions

A set of restrictions that apply to this Team Drive or items inside this Team Drive.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminManagedRestrictions** | **Boolean** | Whether administrative privileges on this Team Drive are required to modify restrictions. |  [optional] |
|**copyRequiresWriterPermission** | **Boolean** | Whether the options to copy, print, or download files inside this Team Drive, should be disabled for readers and commenters. When this restriction is set to &#x60;true&#x60;, it will override the similarly named field to &#x60;true&#x60; for any file inside this Team Drive. |  [optional] |
|**domainUsersOnly** | **Boolean** | Whether access to this Team Drive and items inside this Team Drive is restricted to users of the domain to which this Team Drive belongs. This restriction may be overridden by other sharing policies controlled outside of this Team Drive. |  [optional] |
|**sharingFoldersRequiresOrganizerPermission** | **Boolean** | If true, only users with the organizer role can share folders. If false, users with either the organizer role or the file organizer role can share folders. |  [optional] |
|**teamMembersOnly** | **Boolean** | Whether access to items inside this Team Drive is restricted to members of this Team Drive. |  [optional] |



