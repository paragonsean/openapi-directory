

# ResourceRequirements

ResourceRequirements describes the compute resource requirements.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limits** | **Map&lt;String, String&gt;** | (Optional) Only memory and CPU are supported. Limits describes the maximum amount of compute resources allowed. The values of the map is string form of the &#39;quantity&#39; k8s type: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go |  [optional] |
|**requests** | **Map&lt;String, String&gt;** | (Optional) Only memory and CPU are supported. Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. The values of the map is string form of the &#39;quantity&#39; k8s type: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go |  [optional] |



