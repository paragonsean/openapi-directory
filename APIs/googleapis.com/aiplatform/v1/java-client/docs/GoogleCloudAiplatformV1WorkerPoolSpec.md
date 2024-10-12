

# GoogleCloudAiplatformV1WorkerPoolSpec

Represents the spec of a worker pool in a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerSpec** | [**GoogleCloudAiplatformV1ContainerSpec**](GoogleCloudAiplatformV1ContainerSpec.md) |  |  [optional] |
|**diskSpec** | [**GoogleCloudAiplatformV1DiskSpec**](GoogleCloudAiplatformV1DiskSpec.md) |  |  [optional] |
|**machineSpec** | [**GoogleCloudAiplatformV1MachineSpec**](GoogleCloudAiplatformV1MachineSpec.md) |  |  [optional] |
|**nfsMounts** | [**List&lt;GoogleCloudAiplatformV1NfsMount&gt;**](GoogleCloudAiplatformV1NfsMount.md) | Optional. List of NFS mount spec. |  [optional] |
|**pythonPackageSpec** | [**GoogleCloudAiplatformV1PythonPackageSpec**](GoogleCloudAiplatformV1PythonPackageSpec.md) |  |  [optional] |
|**replicaCount** | **String** | Optional. The number of worker replicas to use for this worker pool. |  [optional] |



