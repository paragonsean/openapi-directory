

# CreateContainer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bluemixApp** | **String** | The name of the Cloud Foundry app that you want to bind to your container. The Cloud Foundry app must be created in the same space where you want to create your container. |  [optional] |
|**cmd** | **List&lt;String&gt;** | The command and arguments in this list are passed to the container to be executed when the container is started. This command must be a long-running command. Do not use a short-lived command, for example, /bin/date, because it might cause the container to crash. &lt;br&gt;Sample long-running commands:&lt;br&gt;[\&quot;ping\&quot;,\&quot;localhost\&quot;]&lt;br&gt;[\&quot;tail\&quot;,\&quot;-f\&quot;,\&quot;/dev/null\&quot;]&lt;br&gt;[\&quot;sh\&quot;,\&quot;-c\&quot;,\&quot;while true; do date; sleep 20; done\&quot;]  |  [optional] |
|**cpuset** | **String** | Pins the container processes to a specific CPU core on the compute host. For example: 0 means that processes are executed on the first core only. |  [optional] |
|**env** | **List&lt;String&gt;** | A list of environment variables in the form of key&#x3D;value pairs. All keys in this list have to be unique. List multiple keys separately and if you include quotation marks, include them around both the environment variable name and the value. |  [optional] |
|**exposedPorts** | **List&lt;String&gt;** | All public ports that need to be exposed for the container, so the container can be accessed from the Internet. |  [optional] |
|**hostConfig** | [**HostConfig**](HostConfig.md) |  |  [optional] |
|**image** | **String** | Full path to the image in your private Bluemix registry in the format &#x60;registry.ng.bluemix.net/namespace/image&#x60;.  |  |
|**memory** | **Integer** | The container memory that is set for the container in Megabyte. Choose one of the following sizes: Pico 64 MB, Nano 128 MB, Micro 256 MB, Tiny 512 MB, Small 1 GB (1024 MB), Medium 2 GB (2048 MB), Large 4 GB (4096 MB) XLarge 8GB (8192 MB) and 2XLarge 16 GB (16384 MB). |  [optional] |
|**numberCpus** | **Integer** | Number of virtual CPUs that are allocated to the container. |  [optional] |
|**volumes** | **String** | Mount a volume to a container by specifying the details in the following format: &#x60;VOLUME_NAME:/DIRECTORY_PATH[:ro]&#x60;. Example: testvolume:/volumedata/temp:rw. By default, all volumes will be set up with read-write access inside the container (rw). If you wish to set up your volume with read-only access, enter &#x60;ro&#x60;.  Note: To mount a volume to a container, you must create the volume in your space first by using the &#x60;cf ic volume-create&#x60; command, or calling the &#x60;POST /volumes/create endpoint&#x60;. |  [optional] |



