# CloudRunAdminApi.SecurityContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runAsUser** | **Number** | The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. | [optional] 


