

# Service

A Service is a discrete, autonomous, and network-accessible unit, designed to solve an individual concern (Wikipedia (https://en.wikipedia.org/wiki/Service-orientation)). In Cloud Monitoring, a Service acts as the root resource under which operational aspects of the service are accessible.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appEngine** | [**AppEngine**](AppEngine.md) |  |  [optional] |
|**basicService** | [**BasicService**](BasicService.md) |  |  [optional] |
|**cloudEndpoints** | [**CloudEndpoints**](CloudEndpoints.md) |  |  [optional] |
|**cloudRun** | [**CloudRun**](CloudRun.md) |  |  [optional] |
|**clusterIstio** | [**ClusterIstio**](ClusterIstio.md) |  |  [optional] |
|**custom** | **Object** | Use a custom service to designate a service that you want to monitor when none of the other service types (like App Engine, Cloud Run, or a GKE type) matches your intended service. |  [optional] |
|**displayName** | **String** | Name used for UI elements listing this Service. |  [optional] |
|**gkeNamespace** | [**GkeNamespace**](GkeNamespace.md) |  |  [optional] |
|**gkeService** | [**GkeService**](GkeService.md) |  |  [optional] |
|**gkeWorkload** | [**GkeWorkload**](GkeWorkload.md) |  |  [optional] |
|**istioCanonicalService** | [**IstioCanonicalService**](IstioCanonicalService.md) |  |  [optional] |
|**meshIstio** | [**MeshIstio**](MeshIstio.md) |  |  [optional] |
|**name** | **String** | Resource name for this Service. The format is: projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]  |  [optional] |
|**telemetry** | [**Telemetry**](Telemetry.md) |  |  [optional] |
|**userLabels** | **Map&lt;String, String&gt;** | Labels which have been used to annotate the service. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value. |  [optional] |



