

# AttachTenantProjectRequest

Request to attach an existing project to the tenancy unit as a new tenant resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**externalResource** | **String** | When attaching an external project, this is in the format of &#x60;projects/{project_number}&#x60;. |  [optional] |
|**reservedResource** | **String** | When attaching a reserved project already in tenancy units, this is the tag of a tenant resource under the tenancy unit for the managed service&#39;s service producer project. The reserved tenant resource must be in an active state. |  [optional] |
|**tag** | **String** | Required. Tag of the tenant resource after attachment. Must be less than 128 characters. Required. |  [optional] |



