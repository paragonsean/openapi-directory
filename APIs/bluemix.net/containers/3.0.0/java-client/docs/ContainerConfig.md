

# ContainerConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**argsEscaped** | **Boolean** |  |  [optional] |
|**attachStderr** | **String** | Attaches the container to stderr. |  [optional] |
|**attachStdin** | **String** | Attaches the container to sdtin. |  [optional] |
|**attachStdout** | **String** | Attaches the container to stdout. |  [optional] |
|**cmd** | **List&lt;String&gt;** | The command and arguments in this list are passed to the container to be executed when the container is started. This command must be a long-running command. Do not use a short-lived command, for example, /bin/date, because it might cause the container to crash. &lt;br&gt;Sample long-running commands:&lt;br&gt;[\&quot;ping\&quot;,\&quot;localhost\&quot;]&lt;br&gt;[\&quot;tail\&quot;,\&quot;-f\&quot;,\&quot;/dev/null\&quot;]&lt;br&gt;[\&quot;sh\&quot;,\&quot;-c\&quot;,\&quot;while true; do date; sleep 20; done\&quot;]  |  [optional] |
|**domainname** | **String** | The domain name to be used for the container. |  [optional] |
|**env** | **List&lt;String&gt;** | A list of environment variables in the form of key&#x3D;value pairs. All keys in this list have to be unique. List multiple keys separately and if you include quotation marks, include them around both the environment variable name and the value. |  [optional] |
|**exposedPorts** | **List&lt;String&gt;** | List of public ports that were exposed during container creation.  |  [optional] |
|**hostname** | **String** | The host name to be used for the container. |  [optional] |
|**image** | **String** | Full path to the image that the container is based on in your private Bluemix registry. |  [optional] |
|**imageArchitecture** | **String** | The hardware architecture the image is based on. It can either be &#39;amd64&#39; indicating an Intel-based architecture, or &#39;ppc64le&#39; representing a Power-based architecture. |  [optional] |
|**labels** | **List&lt;String&gt;** | List of custom metadata that was added to the container. Labels serve a wide range of uses, such as adding notes to a container. Every label is a key/ value pair. |  [optional] |
|**memory** | **Integer** | The amount of container memory that is assigned to the container in Megabyte. |  [optional] |
|**memorySwap** | **String** | The total container memory limit (memory + swap) |  [optional] |
|**openStdin** | **String** | When set to true, it opens stdin.  |  [optional] |
|**portSpecs** | **String** | Not supported by IBM Containers, empty string. |  [optional] |
|**stdinOnce** | **String** | When set to true it closes stdin after the attached client disconnects. |  [optional] |
|**tty** | **String** | When set to true, attach standard streams to a tty, including stdin if it is not closed. |  [optional] |
|**user** | **String** | User to be used inside the container. |  [optional] |
|**VCPU** | **Integer** | Number of virtual CPUs that are assigned to the container. |  [optional] |
|**volumesFrom** | **String** | List of volumes to inherit from another container. This feature is not supported in IBM Containers. |  [optional] |
|**workingDir** | **String** | The working directory inside the container where specified commands are executed.  |  [optional] |



