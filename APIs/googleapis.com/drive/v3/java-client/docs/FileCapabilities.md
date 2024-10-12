

# FileCapabilities

Output only. Capabilities the current user has on this file. Each capability corresponds to a fine-grained action that a user may take.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canAcceptOwnership** | **Boolean** | Output only. Whether the current user is the pending owner of the file. Not populated for shared drive files. |  [optional] |
|**canAddChildren** | **Boolean** | Output only. Whether the current user can add children to this folder. This is always false when the item is not a folder. |  [optional] |
|**canAddFolderFromAnotherDrive** | **Boolean** | Output only. Whether the current user can add a folder from another drive (different shared drive or My Drive) to this folder. This is false when the item is not a folder. Only populated for items in shared drives. |  [optional] |
|**canAddMyDriveParent** | **Boolean** | Output only. Whether the current user can add a parent for the item without removing an existing parent in the same request. Not populated for shared drive files. |  [optional] |
|**canChangeCopyRequiresWriterPermission** | **Boolean** | Output only. Whether the current user can change the &#x60;copyRequiresWriterPermission&#x60; restriction of this file. |  [optional] |
|**canChangeSecurityUpdateEnabled** | **Boolean** | Output only. Whether the current user can change the securityUpdateEnabled field on link share metadata. |  [optional] |
|**canChangeViewersCanCopyContent** | **Boolean** | Deprecated: Output only. |  [optional] |
|**canComment** | **Boolean** | Output only. Whether the current user can comment on this file. |  [optional] |
|**canCopy** | **Boolean** | Output only. Whether the current user can copy this file. For an item in a shared drive, whether the current user can copy non-folder descendants of this item, or this item itself if it is not a folder. |  [optional] |
|**canDelete** | **Boolean** | Output only. Whether the current user can delete this file. |  [optional] |
|**canDeleteChildren** | **Boolean** | Output only. Whether the current user can delete children of this folder. This is false when the item is not a folder. Only populated for items in shared drives. |  [optional] |
|**canDownload** | **Boolean** | Output only. Whether the current user can download this file. |  [optional] |
|**canEdit** | **Boolean** | Output only. Whether the current user can edit this file. Other factors may limit the type of changes a user can make to a file. For example, see &#x60;canChangeCopyRequiresWriterPermission&#x60; or &#x60;canModifyContent&#x60;. |  [optional] |
|**canListChildren** | **Boolean** | Output only. Whether the current user can list the children of this folder. This is always false when the item is not a folder. |  [optional] |
|**canModifyContent** | **Boolean** | Output only. Whether the current user can modify the content of this file. |  [optional] |
|**canModifyContentRestriction** | **Boolean** | Deprecated: Output only. Use one of &#x60;canModifyEditorContentRestriction&#x60;, &#x60;canModifyOwnerContentRestriction&#x60; or &#x60;canRemoveContentRestriction&#x60;. |  [optional] |
|**canModifyEditorContentRestriction** | **Boolean** | Output only. Whether the current user can add or modify content restrictions on the file which are editor restricted. |  [optional] |
|**canModifyLabels** | **Boolean** | Output only. Whether the current user can modify the labels on the file. |  [optional] |
|**canModifyOwnerContentRestriction** | **Boolean** | Output only. Whether the current user can add or modify content restrictions which are owner restricted. |  [optional] |
|**canMoveChildrenOutOfDrive** | **Boolean** | Output only. Whether the current user can move children of this folder outside of the shared drive. This is false when the item is not a folder. Only populated for items in shared drives. |  [optional] |
|**canMoveChildrenOutOfTeamDrive** | **Boolean** | Deprecated: Output only. Use &#x60;canMoveChildrenOutOfDrive&#x60; instead. |  [optional] |
|**canMoveChildrenWithinDrive** | **Boolean** | Output only. Whether the current user can move children of this folder within this drive. This is false when the item is not a folder. Note that a request to move the child may still fail depending on the current user&#39;s access to the child and to the destination folder. |  [optional] |
|**canMoveChildrenWithinTeamDrive** | **Boolean** | Deprecated: Output only. Use &#x60;canMoveChildrenWithinDrive&#x60; instead. |  [optional] |
|**canMoveItemIntoTeamDrive** | **Boolean** | Deprecated: Output only. Use &#x60;canMoveItemOutOfDrive&#x60; instead. |  [optional] |
|**canMoveItemOutOfDrive** | **Boolean** | Output only. Whether the current user can move this item outside of this drive by changing its parent. Note that a request to change the parent of the item may still fail depending on the new parent that is being added. |  [optional] |
|**canMoveItemOutOfTeamDrive** | **Boolean** | Deprecated: Output only. Use &#x60;canMoveItemOutOfDrive&#x60; instead. |  [optional] |
|**canMoveItemWithinDrive** | **Boolean** | Output only. Whether the current user can move this item within this drive. Note that a request to change the parent of the item may still fail depending on the new parent that is being added and the parent that is being removed. |  [optional] |
|**canMoveItemWithinTeamDrive** | **Boolean** | Deprecated: Output only. Use &#x60;canMoveItemWithinDrive&#x60; instead. |  [optional] |
|**canMoveTeamDriveItem** | **Boolean** | Deprecated: Output only. Use &#x60;canMoveItemWithinDrive&#x60; or &#x60;canMoveItemOutOfDrive&#x60; instead. |  [optional] |
|**canReadDrive** | **Boolean** | Output only. Whether the current user can read the shared drive to which this file belongs. Only populated for items in shared drives. |  [optional] |
|**canReadLabels** | **Boolean** | Output only. Whether the current user can read the labels on the file. |  [optional] |
|**canReadRevisions** | **Boolean** | Output only. Whether the current user can read the revisions resource of this file. For a shared drive item, whether revisions of non-folder descendants of this item, or this item itself if it is not a folder, can be read. |  [optional] |
|**canReadTeamDrive** | **Boolean** | Deprecated: Output only. Use &#x60;canReadDrive&#x60; instead. |  [optional] |
|**canRemoveChildren** | **Boolean** | Output only. Whether the current user can remove children from this folder. This is always false when the item is not a folder. For a folder in a shared drive, use &#x60;canDeleteChildren&#x60; or &#x60;canTrashChildren&#x60; instead. |  [optional] |
|**canRemoveContentRestriction** | **Boolean** | Output only. Whether there is a content restriction on the file that can be removed by the current user. |  [optional] |
|**canRemoveMyDriveParent** | **Boolean** | Output only. Whether the current user can remove a parent from the item without adding another parent in the same request. Not populated for shared drive files. |  [optional] |
|**canRename** | **Boolean** | Output only. Whether the current user can rename this file. |  [optional] |
|**canShare** | **Boolean** | Output only. Whether the current user can modify the sharing settings for this file. |  [optional] |
|**canTrash** | **Boolean** | Output only. Whether the current user can move this file to trash. |  [optional] |
|**canTrashChildren** | **Boolean** | Output only. Whether the current user can trash children of this folder. This is false when the item is not a folder. Only populated for items in shared drives. |  [optional] |
|**canUntrash** | **Boolean** | Output only. Whether the current user can restore this file from trash. |  [optional] |



