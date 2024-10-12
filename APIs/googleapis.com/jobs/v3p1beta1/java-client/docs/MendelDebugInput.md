

# MendelDebugInput

Message representing input to a Mendel server for debug forcing. See go/mendel-debug-forcing for more details. Next ID: 2

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namespacedDebugInput** | [**Map&lt;String, NamespacedDebugInput&gt;**](NamespacedDebugInput.md) | When a request spans multiple servers, a MendelDebugInput may travel with the request and take effect in all the servers. This field is a map of namespaces to NamespacedMendelDebugInput protos. In a single server, up to two NamespacedMendelDebugInput protos are applied: 1. NamespacedMendelDebugInput with the global namespace (key &#x3D;&#x3D; \&quot;\&quot;). 2. NamespacedMendelDebugInput with the server&#39;s namespace. When both NamespacedMendelDebugInput protos are present, they are merged. See go/mendel-debug-forcing for more details. |  [optional] |



