# CloudRunAdminApi.TCPSocketAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **String** | (Optional) Optional: Host name to connect to, defaults to the pod IP. | [optional] 
**port** | **Number** | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. This field is currently limited to integer types only because of proto&#39;s inability to properly support the IntOrString golang type. | [optional] 


