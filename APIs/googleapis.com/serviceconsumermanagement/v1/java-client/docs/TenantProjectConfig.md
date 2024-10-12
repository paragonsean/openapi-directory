

# TenantProjectConfig

This structure defines a tenant project to be added to the specified tenancy unit and its initial configuration and properties. A project lien is created for the tenant project to prevent the tenant project from being deleted accidentally. The lien is deleted as part of tenant project removal.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingConfig** | [**BillingConfig**](BillingConfig.md) |  |  [optional] |
|**folder** | **String** | Folder where project in this tenancy unit must be located This folder must have been previously created with the required permissions for the caller to create and configure a project in it. Valid folder resource names have the format &#x60;folders/{folder_number}&#x60; (for example, &#x60;folders/123456&#x60;). |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels that are applied to this project. |  [optional] |
|**serviceAccountConfig** | [**ServiceAccountConfig**](ServiceAccountConfig.md) |  |  [optional] |
|**services** | **List&lt;String&gt;** | Google Cloud API names of services that are activated on this project during provisioning. If any of these services can&#39;t be activated, the request fails. For example: &#39;compute.googleapis.com&#39;,&#39;cloudfunctions.googleapis.com&#39; |  [optional] |
|**tenantProjectPolicy** | [**TenantProjectPolicy**](TenantProjectPolicy.md) |  |  [optional] |



