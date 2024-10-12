

# BatchDeletePermissionsRequest

The request to remove one or more permissions from a note. A permission with the `OWNER` role can't be removed. If removing a permission fails, then the entire request fails and no changes are made. Returns a 400 bad request error if a specified permission does not exist on the note.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**names** | **List&lt;String&gt;** | Required. The names of the permissions to delete. Format: &#x60;notes/{note}/permissions/{permission}&#x60; |  [optional] |



