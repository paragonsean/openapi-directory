

# GoogleCloudApigeeV1InstanceDeploymentStatus

The status of a deployment as reported by a single instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployedRevisions** | [**List&lt;GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevision&gt;**](GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRevision.md) | Revisions currently deployed in MPs. |  [optional] |
|**deployedRoutes** | [**List&lt;GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRoute&gt;**](GoogleCloudApigeeV1InstanceDeploymentStatusDeployedRoute.md) | Current routes deployed in the ingress routing table. A route which is missing will appear in &#x60;missing_routes&#x60;. |  [optional] |
|**instance** | **String** | ID of the instance reporting the status. |  [optional] |



