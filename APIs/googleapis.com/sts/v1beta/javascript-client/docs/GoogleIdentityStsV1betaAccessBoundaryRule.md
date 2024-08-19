# SecurityTokenServiceApi.GoogleIdentityStsV1betaAccessBoundaryRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityCondition** | [**GoogleTypeExpr**](GoogleTypeExpr.md) |  | [optional] 
**availablePermissions** | **[String]** | A list of permissions that may be allowed for use on the specified resource. The only supported values in the list are IAM roles, following the format of google.iam.v1.Binding.role. Example value: &#x60;inRole:roles/logging.viewer&#x60; for predefined roles and &#x60;inRole:organizations/{ORGANIZATION_ID}/roles/logging.viewer&#x60; for custom roles. | [optional] 
**availableResource** | **String** | The full resource name of a Google Cloud resource entity. The format definition is at https://cloud.google.com/apis/design/resource_names. Example value: &#x60;//cloudresourcemanager.googleapis.com/projects/my-project&#x60;. | [optional] 


