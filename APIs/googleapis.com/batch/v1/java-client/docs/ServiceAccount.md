

# ServiceAccount

Carries information about a Google Cloud service account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | Email address of the service account. If not specified, the default Compute Engine service account for the project will be used. If instance template is being used, the service account has to be specified in the instance template and it has to match the email field here. |  [optional] |
|**scopes** | **List&lt;String&gt;** | List of scopes to be enabled for this service account on the VM, in addition to the cloud-platform API scope that will be added by default. |  [optional] |



