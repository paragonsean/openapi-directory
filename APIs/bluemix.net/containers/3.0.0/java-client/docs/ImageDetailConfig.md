

# ImageDetailConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**argsEscaped** | **Boolean** |  |  [optional] |
|**attachStderr** | **Boolean** | Attaches the container to stderr. |  [optional] |
|**attachStdin** | **Boolean** | Attaches the container to stdin. |  [optional] |
|**attachStdout** | **Boolean** | Attaches the container to stdout. |  [optional] |
|**cmd** | **List&lt;String&gt;** | The command and arguments in this list are passed to the container to be executed when the container is started. This command must be a long-running command. Do not use a short-lived command, for example, /bin/date, because it might cause the container to crash. &lt;br&gt;Sample long-running commands:&lt;br&gt;[\&quot;ping\&quot;,\&quot;localhost\&quot;]&lt;br&gt;[\&quot;tail\&quot;,\&quot;-f\&quot;,\&quot;/dev/null\&quot;]&lt;br&gt;[\&quot;sh\&quot;,\&quot;-c\&quot;,\&quot;while true; do date; sleep 20; done\&quot;]  |  [optional] |
|**domainmame** | **String** | The domain name to be used for the container. |  [optional] |
|**entrypoint** | **String** | The entrypoint specifies a command that will always be executed when the container starts. |  [optional] |
|**env** | **List&lt;String&gt;** | A list of environment variables in the form of key&#x3D;value pairs. All keys in this list have to be unique. List multiple keys separately and if you include quotation marks, include them around both the environment variable name and the value. |  [optional] |
|**exposedPorts** | **List&lt;String&gt;** | A list of all udp and tcp ports that have been publicly exposed during the container creation. |  [optional] |
|**hostname** | **String** | The host name of the container provided by Openstack.  |  [optional] |
|**image** | **String** | The unique ID of the image.  |  [optional] |
|**labels** | **List&lt;String&gt;** | List of custom metadata that was added to the image. Labels serve a wide range of uses, such as adding notes or license requirements to an image. Every label is a key/ value pair. |  [optional] |
|**onBuild** | **List&lt;String&gt;** | ??? |  [optional] |
|**openStdin** | **Boolean** | When set to true, it opens stdin. |  [optional] |
|**stdinOnce** | **Boolean** | When set to true it closes stdin after the attached client disconnects. |  [optional] |
|**tty** | **Boolean** | When set to true, attach standard streams to a tty, including stdin if it is not closed. |  [optional] |
|**user** | **String** | The user to be used inside the container. |  [optional] |
|**volumes** | **String** | Docker specific. Not supported by IBM Containers. The path to the volume that is created when deploying a container from the image. To use a volume in IBM Containers, you must first create a volume and then mount it to your container during creation. |  [optional] |
|**workingDir** | **String** | The working directory inside the container where specified commands are executed. |  [optional] |



