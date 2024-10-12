

# InToto

This contains the fields corresponding to the definition of a software supply chain step in an in-toto layout. This information goes into a Grafeas note.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expectedCommand** | **List&lt;String&gt;** | This field contains the expected command used to perform the step. |  [optional] |
|**expectedMaterials** | [**List&lt;ArtifactRule&gt;**](ArtifactRule.md) | The following fields contain in-toto artifact rules identifying the artifacts that enter this supply chain step, and exit the supply chain step, i.e. materials and products of the step. |  [optional] |
|**expectedProducts** | [**List&lt;ArtifactRule&gt;**](ArtifactRule.md) |  |  [optional] |
|**signingKeys** | [**List&lt;SigningKey&gt;**](SigningKey.md) | This field contains the public keys that can be used to verify the signatures on the step metadata. |  [optional] |
|**stepName** | **String** | This field identifies the name of the step in the supply chain. |  [optional] |
|**threshold** | **String** | This field contains a value that indicates the minimum number of keys that need to be used to sign the step&#39;s in-toto link. |  [optional] |



