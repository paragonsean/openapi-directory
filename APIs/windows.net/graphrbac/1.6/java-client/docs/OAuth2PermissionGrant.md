

# OAuth2PermissionGrant


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | The id of the resource&#39;s service principal granted consent to impersonate the user when accessing the resource (represented by the resourceId property). |  [optional] |
|**consentType** | [**ConsentTypeEnum**](#ConsentTypeEnum) | Indicates if consent was provided by the administrator (on behalf of the organization) or by an individual. |  [optional] |
|**expiryTime** | **String** | Expiry time for TTL |  [optional] |
|**objectId** | **String** | The id of the permission grant |  [optional] |
|**odataType** | **String** | Microsoft.DirectoryServices.OAuth2PermissionGrant |  [optional] |
|**principalId** | **String** | When consent type is Principal, this property specifies the id of the user that granted consent and applies only for that user. |  [optional] |
|**resourceId** | **String** | Object Id of the resource you want to grant |  [optional] |
|**scope** | **String** | Specifies the value of the scope claim that the resource application should expect in the OAuth 2.0 access token. For example, User.Read |  [optional] |
|**startTime** | **String** | Start time for TTL |  [optional] |



## Enum: ConsentTypeEnum

| Name | Value |
|---- | -----|
| ALL_PRINCIPALS | &quot;AllPrincipals&quot; |
| PRINCIPAL | &quot;Principal&quot; |



