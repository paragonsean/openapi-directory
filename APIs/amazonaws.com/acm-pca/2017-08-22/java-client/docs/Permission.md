

# Permission

Permissions designate which private CA actions can be performed by an Amazon Web Services service or entity. In order for ACM to automatically renew private certificates, you must give the ACM service principal all available permissions (<code>IssueCertificate</code>, <code>GetCertificate</code>, and <code>ListPermissions</code>). Permissions can be assigned with the <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreatePermission.html\">CreatePermission</a> action, removed with the <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePermission.html\">DeletePermission</a> action, and listed with the <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListPermissions.html\">ListPermissions</a> action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateAuthorityArn** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**principal** | [**String**](String.md) |  |  [optional] |
|**sourceAccount** | [**String**](String.md) |  |  [optional] |
|**actions** | [**List**](List.md) |  |  [optional] |
|**policy** | [**String**](String.md) |  |  [optional] |



