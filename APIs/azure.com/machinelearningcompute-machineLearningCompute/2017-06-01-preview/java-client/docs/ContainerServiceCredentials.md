

# ContainerServiceCredentials

Information about the Azure Container Registry which contains the images deployed to the cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acsKubeConfig** | **String** | The ACS kube config file. |  [optional] [readonly] |
|**imagePullSecretName** | **String** | The ACR image pull secret name which was created in Kubernetes. |  [optional] [readonly] |
|**servicePrincipalConfiguration** | [**ServicePrincipalProperties**](ServicePrincipalProperties.md) |  |  [optional] |



