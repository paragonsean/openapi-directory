

# RevisionSpec

RevisionSpec holds the desired state of the Revision (from the client).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerConcurrency** | **Integer** | ContainerConcurrency specifies the maximum allowed in-flight (concurrent) requests per container instance of the Revision. If not specified, defaults to 80. |  [optional] |
|**containers** | [**List&lt;Container&gt;**](Container.md) | Required. Containers holds the single container that defines the unit of execution for this Revision. In the context of a Revision, we disallow a number of fields on this Container, including: name and lifecycle. In Cloud Run, only a single container may be provided. |  [optional] |
|**enableServiceLinks** | **Boolean** | Not supported by Cloud Run. |  [optional] |
|**imagePullSecrets** | [**List&lt;LocalObjectReference&gt;**](LocalObjectReference.md) | Not supported by Cloud Run. |  [optional] |
|**serviceAccountName** | **String** | Email address of the IAM service account associated with the revision of the service. The service account represents the identity of the running revision, and determines what permissions the revision has. If not provided, the revision will use the project&#39;s default service account. |  [optional] |
|**timeoutSeconds** | **Integer** | TimeoutSeconds holds the max duration the instance is allowed for responding to a request. Cloud Run: defaults to 300 seconds (5 minutes). Maximum allowed value is 3600 seconds (1 hour). |  [optional] |
|**volumes** | [**List&lt;Volume&gt;**](Volume.md) |  |  [optional] |



