

# HostConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**binds** | **List&lt;String&gt;** | A list of volumes to be bound to the container. Each volume must be listed in the following format: VOLNAME:/CONTAINER_PATH:rw [ro].  |  [optional] |
|**extraHosts** | **List&lt;String&gt;** | A list of hostnames/IP mappings to be added to the container’s /etc/hosts file. Specified in the form [\&quot;hostname:IP\&quot;]  |  [optional] |
|**links** | **List&lt;String&gt;** | A list of containers that need to be linked. |  [optional] |
|**portBindings** | **List&lt;String&gt;** | The container ports that you want to expose to the public. Ports need to be specified in the form of &amp;lt;port&amp;gt;/&amp;lt;protocol&amp;gt;: [{ \&quot;HostIp\&quot;: \&quot;&amp;lt;IP&amp;gt;\&quot;, \&quot;HostPort\&quot;: \&quot;&amp;lt;port&amp;gt;\&quot; }]  |  [optional] |



