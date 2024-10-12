

# DeploymentCircuitBreaker

<note> <p>The deployment circuit breaker can only be used for services using the rolling update (<code>ECS</code>) deployment type.</p> </note> <p>The <b>deployment circuit breaker</b> determines whether a service deployment will fail if the service can't reach a steady state. If it is turned on, a service deployment will transition to a failed state and stop launching new tasks. You can also configure Amazon ECS to roll back your service to the last completed deployment after a failure. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html\">Rolling update</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>For more information about API failure reasons, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html\">API failure reasons</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enable** | [**Boolean**](Boolean.md) |  |  |
|**rollback** | [**Boolean**](Boolean.md) |  |  |



