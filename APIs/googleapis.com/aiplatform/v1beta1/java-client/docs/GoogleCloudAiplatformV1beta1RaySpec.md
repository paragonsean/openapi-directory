

# GoogleCloudAiplatformV1beta1RaySpec

Configuration information for the Ray cluster. For experimental launch, Ray cluster creation and Persistent cluster creation are 1:1 mapping: We will provision all the nodes within the Persistent cluster as Ray nodes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headNodeResourcePoolId** | **String** | Optional. This will be used to indicate which resource pool will serve as the Ray head node(the first node within that pool). Will use the machine from the first workerpool as the head node by default if this field isn&#39;t set. |  [optional] |
|**imageUri** | **String** | Optional. Default image for user to choose a preferred ML framework (for example, TensorFlow or Pytorch) by choosing from [Vertex prebuilt images](https://cloud.google.com/vertex-ai/docs/training/pre-built-containers). Either this or the resource_pool_images is required. Use this field if you need all the resource pools to have the same Ray image. Otherwise, use the {@code resource_pool_images} field. |  [optional] |
|**rayMetricSpec** | [**GoogleCloudAiplatformV1beta1RayMetricSpec**](GoogleCloudAiplatformV1beta1RayMetricSpec.md) |  |  [optional] |
|**resourcePoolImages** | **Map&lt;String, String&gt;** | Optional. Required if image_uri isn&#39;t set. A map of resource_pool_id to prebuild Ray image if user need to use different images for different head/worker pools. This map needs to cover all the resource pool ids. Example: { \&quot;ray_head_node_pool\&quot;: \&quot;head image\&quot; \&quot;ray_worker_node_pool1\&quot;: \&quot;worker image\&quot; \&quot;ray_worker_node_pool2\&quot;: \&quot;another worker image\&quot; } |  [optional] |



