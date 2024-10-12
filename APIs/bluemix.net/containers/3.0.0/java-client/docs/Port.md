

# Port


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**IP** | **String** | Public IP address that was bound to the container in IPv4 format. |  [optional] |
|**privatePort** | **String** | The private port of the container on which the container listens during run time. |  [optional] |
|**publicPort** | **String** | The public port that was exposed during container creation. When a public port is exposed, a public IP address can be bound to the container which makes the container accessible from the internet. |  [optional] |
|**type** | **String** | The type of IP protocol that is used for the port. It can either be &#x60;udp&#x60; or &#x60;tcp&#x60;.   |  [optional] |



