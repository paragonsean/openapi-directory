

# ServiceAccountConfig

Describes the service account configuration for the tenant project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | ID of the IAM service account to be created in tenant project. The email format of the service account is \&quot;@.iam.gserviceaccount.com\&quot;. This account ID must be unique within tenant project and service producers have to guarantee it. The ID must be 6-30 characters long, and match the following regular expression: &#x60;[a-z]([-a-z0-9]*[a-z0-9])&#x60;. |  [optional] |
|**tenantProjectRoles** | **List&lt;String&gt;** | Roles for the associated service account for the tenant project. |  [optional] |



