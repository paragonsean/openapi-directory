

# SasPortalProvisionDeploymentRequest

Request for [ProvisionDeployment]. [spectrum.sas.portal.v1alpha1.Provisioning.ProvisionDeployment]. GCP Project, Organization Info, and caller’s GAIA ID should be retrieved from the RPC handler, and used as inputs to create a new SAS organization (if not exists) and a new SAS deployment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**newDeploymentDisplayName** | **String** | Optional. If this field is set, and a new SAS Portal Deployment needs to be created, its display name will be set to the value of this field. |  [optional] |
|**newOrganizationDisplayName** | **String** | Optional. If this field is set, and a new SAS Portal Organization needs to be created, its display name will be set to the value of this field. |  [optional] |
|**organizationId** | **String** | Optional. If this field is set then a new deployment will be created under the organization specified by this id. |  [optional] |



