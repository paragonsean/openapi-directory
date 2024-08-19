

# Ulimit

<p>The <code>ulimit</code> settings to pass to the container.</p> <p>Amazon ECS tasks hosted on Fargate use the default resource limit values set by the operating system with the exception of the <code>nofile</code> resource limit parameter which Fargate overrides. The <code>nofile</code> resource limit sets a restriction on the number of open files that a container can use. The default <code>nofile</code> soft limit is <code>1024</code> and the default hard limit is <code>4096</code>.</p> <p>You can specify the <code>ulimit</code> settings for a container in a task definition.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**UlimitName**](UlimitName.md) |  |  |
|**softLimit** | [**Integer**](Integer.md) |  |  |
|**hardLimit** | [**Integer**](Integer.md) |  |  |



