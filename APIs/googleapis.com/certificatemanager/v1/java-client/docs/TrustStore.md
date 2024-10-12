

# TrustStore

Defines a trust store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intermediateCas** | [**List&lt;IntermediateCA&gt;**](IntermediateCA.md) | Set of intermediate CA certificates used for the path building phase of chain validation. The field is currently not supported if TrustConfig is used for the workload certificate feature. |  [optional] |
|**trustAnchors** | [**List&lt;TrustAnchor&gt;**](TrustAnchor.md) | List of Trust Anchors to be used while performing validation against a given TrustStore. |  [optional] |



