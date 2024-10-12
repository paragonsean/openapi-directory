

# EnrollVmwareAdminClusterRequest

Message for enrolling an existing VMware admin cluster to the GKE on-prem API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**membership** | **String** | Required. This is the full resource name of this admin cluster&#39;s fleet membership. |  [optional] |
|**vmwareAdminClusterId** | **String** | User provided OnePlatform identifier that is used as part of the resource name. This must be unique among all GKE on-prem clusters within a project and location and will return a 409 if the cluster already exists. (https://tools.ietf.org/html/rfc1123) format. |  [optional] |



