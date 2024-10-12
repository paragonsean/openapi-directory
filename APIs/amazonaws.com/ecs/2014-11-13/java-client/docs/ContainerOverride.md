

# ContainerOverride

<p>The overrides that are sent to a container. An empty container override can be passed in. An example of an empty container override is <code>{\"containerOverrides\": [ ] }</code>. If a non-empty container override is specified, the <code>name</code> parameter must be included.</p> <p>You can use Secrets Manager or Amazon Web Services Systems Manager Parameter Store to store the sensitive data. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/secrets-envvar.html\">Retrieve secrets through environment variables</a> in the Amazon ECS Developer Guide.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**command** | [**List**](List.md) |  |  [optional] |
|**environment** | [**List**](List.md) |  |  [optional] |
|**environmentFiles** | [**List**](List.md) |  |  [optional] |
|**cpu** | [**Integer**](Integer.md) |  |  [optional] |
|**memory** | [**Integer**](Integer.md) |  |  [optional] |
|**memoryReservation** | [**Integer**](Integer.md) |  |  [optional] |
|**resourceRequirements** | [**List**](List.md) |  |  [optional] |



