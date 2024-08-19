

# GoogleCloudAiplatformV1beta1WorkerPoolSpec

Represents the spec of a worker pool in a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerSpec** | [**GoogleCloudAiplatformV1beta1ContainerSpec**](GoogleCloudAiplatformV1beta1ContainerSpec.md) |  |  [optional] |
|**diskSpec** | [**GoogleCloudAiplatformV1beta1DiskSpec**](GoogleCloudAiplatformV1beta1DiskSpec.md) |  |  [optional] |
|**machineSpec** | [**GoogleCloudAiplatformV1beta1MachineSpec**](GoogleCloudAiplatformV1beta1MachineSpec.md) |  |  [optional] |
|**nfsMounts** | [**List&lt;GoogleCloudAiplatformV1beta1NfsMount&gt;**](GoogleCloudAiplatformV1beta1NfsMount.md) | Optional. List of NFS mount spec. |  [optional] |
|**pythonPackageSpec** | [**GoogleCloudAiplatformV1beta1PythonPackageSpec**](GoogleCloudAiplatformV1beta1PythonPackageSpec.md) |  |  [optional] |
|**replicaCount** | **String** | Optional. The number of worker replicas to use for this worker pool. |  [optional] |



