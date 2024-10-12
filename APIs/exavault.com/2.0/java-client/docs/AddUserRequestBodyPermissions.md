

# AddUserRequestBodyPermissions

An object containing name/value pairs for each permission. Any permission that is not passed will be set to `false` by default. Note that users will be unable to see any files in the account unless you include `list` permission. When creating a user with the `role` **admin**, you should set all of the permissions to `true`

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changePassword** | **Boolean** |  |  [optional] |
|**delete** | **Boolean** |  |  [optional] |
|**deleteFormData** | **Boolean** |  |  [optional] |
|**download** | **Boolean** |  |  [optional] |
|**_list** | **Boolean** |  |  [optional] |
|**modify** | **Boolean** |  |  [optional] |
|**notification** | **Boolean** |  |  [optional] |
|**share** | **Boolean** |  |  [optional] |
|**upload** | **Boolean** |  |  [optional] |
|**viewFormData** | **Boolean** |  |  [optional] |



