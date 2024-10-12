# CloudRunAdminApi.RevisionStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**[GoogleCloudRunV1Condition]**](GoogleCloudRunV1Condition.md) | Conditions communicate information about ongoing/complete reconciliation processes that bring the \&quot;spec\&quot; inline with the observed state of the world. As a Revision is being prepared, it will incrementally update conditions. Revision-specific conditions include: * &#x60;ResourcesAvailable&#x60;: &#x60;True&#x60; when underlying resources have been provisioned. * &#x60;ContainerHealthy&#x60;: &#x60;True&#x60; when the Revision readiness check completes. * &#x60;Active&#x60;: &#x60;True&#x60; when the Revision may receive traffic. | [optional] 
**desiredReplicas** | **Number** | Output only. The configured number of instances running this revision. For Cloud Run, this only includes instances provisioned using the minScale annotation. It does not include instances created by autoscaling. | [optional] [readonly] 
**imageDigest** | **String** | ImageDigest holds the resolved digest for the image specified within .Spec.Container.Image. The digest is resolved during the creation of Revision. This field holds the digest value regardless of whether a tag or digest was originally specified in the Container object. | [optional] 
**logUrl** | **String** | Optional. Specifies the generated logging url for this particular revision based on the revision url template specified in the controller&#39;s config. | [optional] 
**observedGeneration** | **Number** | ObservedGeneration is the &#39;Generation&#39; of the Revision that was last processed by the controller. Clients polling for completed reconciliation should poll until observedGeneration &#x3D; metadata.generation, and the Ready condition&#39;s status is True or False. | [optional] 
**serviceName** | **String** | Not currently used by Cloud Run. | [optional] 


