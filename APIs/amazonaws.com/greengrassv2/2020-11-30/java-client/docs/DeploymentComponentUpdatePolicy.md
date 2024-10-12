

# DeploymentComponentUpdatePolicy

<p>Contains information about a deployment's policy that defines when components are safe to update.</p> <p>Each component on a device can report whether or not it's ready to update. After a component and its dependencies are ready, they can apply the update in the deployment. You can configure whether or not the deployment notifies components of an update and waits for a response. You specify the amount of time each component has to respond to the update notification.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**timeoutInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**action** | [**DeploymentComponentUpdatePolicyAction**](DeploymentComponentUpdatePolicyAction.md) |  |  [optional] |



