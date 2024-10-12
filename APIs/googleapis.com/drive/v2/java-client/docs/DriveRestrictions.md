

# DriveRestrictions

A set of restrictions that apply to this shared drive or items inside this shared drive.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminManagedRestrictions** | **Boolean** | Whether administrative privileges on this shared drive are required to modify restrictions. |  [optional] |
|**copyRequiresWriterPermission** | **Boolean** | Whether the options to copy, print, or download files inside this shared drive, should be disabled for readers and commenters. When this restriction is set to &#x60;true&#x60;, it will override the similarly named field to &#x60;true&#x60; for any file inside this shared drive. |  [optional] |
|**domainUsersOnly** | **Boolean** | Whether access to this shared drive and items inside this shared drive is restricted to users of the domain to which this shared drive belongs. This restriction may be overridden by other sharing policies controlled outside of this shared drive. |  [optional] |
|**driveMembersOnly** | **Boolean** | Whether access to items inside this shared drive is restricted to its members. |  [optional] |
|**sharingFoldersRequiresOrganizerPermission** | **Boolean** | If true, only users with the organizer role can share folders. If false, users with either the organizer role or the file organizer role can share folders. |  [optional] |



