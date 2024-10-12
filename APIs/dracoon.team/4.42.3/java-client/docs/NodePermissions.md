

# NodePermissions

Node permissions

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**change** | **Boolean** | User / Group may update metadata of nodes: rename files and folders, change classification, etc. |  |
|**create** | **Boolean** | User / Group may upload files, create folders and copy / move files to this room, overwriting is not possible. |  |
|**delete** | **Boolean** | User / Group may overwrite and remove files / folders, move files from this room. |  |
|**deleteRecycleBin** | **Boolean** | User / Group may permanently remove files / folders from the recycle bin. |  |
|**manage** | **Boolean** | User / Group may grant all of the above permissions to other users and groups independently,  may update room metadata and create / update / delete subordinary rooms, has all permissions. |  |
|**manageDownloadShare** | **Boolean** | User / Group may create Download Shares for files and containers view all previously created Download Shares in this room. |  |
|**manageUploadShare** | **Boolean** | User / Group may create Upload Shares for containers, view all previously created Upload Shares in this room. |  |
|**read** | **Boolean** | User / Group may see all rooms, files and folders in the room and download everything, copy files from this room. |  |
|**readRecycleBin** | **Boolean** | User / Group may look up files / folders in the recycle bin. |  |
|**restoreRecycleBin** | **Boolean** | User / Group may restore files / folders from recycle bin - room permissions required. |  |



