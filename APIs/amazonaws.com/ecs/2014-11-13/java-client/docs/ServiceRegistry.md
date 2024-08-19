

# ServiceRegistry

<p>The details for the service registry.</p> <p>Each service may be associated with one service registry. Multiple service registries for each service are not supported.</p> <p>When you add, update, or remove the service registries configuration, Amazon ECS starts a new deployment. New tasks are registered and deregistered to the updated service registry configuration.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**registryArn** | [**String**](String.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**containerName** | [**String**](String.md) |  |  [optional] |
|**containerPort** | [**Integer**](Integer.md) |  |  [optional] |



