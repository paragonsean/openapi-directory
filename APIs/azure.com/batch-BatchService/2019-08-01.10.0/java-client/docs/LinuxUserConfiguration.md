

# LinuxUserConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gid** | **Integer** | The uid and gid properties must be specified together or not at all. If not specified the underlying operating system picks the gid. |  [optional] |
|**sshPrivateKey** | **String** | The private key must not be password protected. The private key is used to automatically configure asymmetric-key based authentication for SSH between Compute Nodes in a Linux Pool when the Pool&#39;s enableInterNodeCommunication property is true (it is ignored if enableInterNodeCommunication is false). It does this by placing the key pair into the user&#39;s .ssh directory. If not specified, password-less SSH is not configured between Compute Nodes (no modification of the user&#39;s .ssh directory is done). |  [optional] |
|**uid** | **Integer** | The uid and gid properties must be specified together or not at all. If not specified the underlying operating system picks the uid. |  [optional] |



