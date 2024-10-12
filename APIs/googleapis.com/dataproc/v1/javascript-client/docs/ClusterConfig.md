# CloudDataprocApi.ClusterConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscalingConfig** | [**AutoscalingConfig**](AutoscalingConfig.md) |  | [optional] 
**auxiliaryNodeGroups** | [**[AuxiliaryNodeGroup]**](AuxiliaryNodeGroup.md) | Optional. The node group settings. | [optional] 
**configBucket** | **String** | Optional. A Cloud Storage bucket used to stage job dependencies, config files, and job driver console output. If you do not specify a staging bucket, Cloud Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster&#39;s staging bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket (see Dataproc staging and temp buckets (https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket)). This field requires a Cloud Storage bucket name, not a gs://... URI to a Cloud Storage bucket. | [optional] 
**dataprocMetricConfig** | [**DataprocMetricConfig**](DataprocMetricConfig.md) |  | [optional] 
**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  | [optional] 
**endpointConfig** | [**EndpointConfig**](EndpointConfig.md) |  | [optional] 
**gceClusterConfig** | [**GceClusterConfig**](GceClusterConfig.md) |  | [optional] 
**gkeClusterConfig** | [**GkeClusterConfig**](GkeClusterConfig.md) |  | [optional] 
**initializationActions** | [**[NodeInitializationAction]**](NodeInitializationAction.md) | Optional. Commands to execute on each node after config is completed. By default, executables are run on master and all worker nodes. You can test a node&#39;s role metadata to run an executable on a master or worker node, as shown below using curl (you can also use wget): ROLE&#x3D;$(curl -H Metadata-Flavor:Google http://metadata/computeMetadata/v1/instance/attributes/dataproc-role) if [[ \&quot;${ROLE}\&quot; &#x3D;&#x3D; &#39;Master&#39; ]]; then ... master specific actions ... else ... worker specific actions ... fi  | [optional] 
**lifecycleConfig** | [**LifecycleConfig**](LifecycleConfig.md) |  | [optional] 
**masterConfig** | [**InstanceGroupConfig**](InstanceGroupConfig.md) |  | [optional] 
**metastoreConfig** | [**MetastoreConfig**](MetastoreConfig.md) |  | [optional] 
**secondaryWorkerConfig** | [**InstanceGroupConfig**](InstanceGroupConfig.md) |  | [optional] 
**securityConfig** | [**SecurityConfig**](SecurityConfig.md) |  | [optional] 
**softwareConfig** | [**SoftwareConfig**](SoftwareConfig.md) |  | [optional] 
**tempBucket** | **String** | Optional. A Cloud Storage bucket used to store ephemeral cluster and jobs data, such as Spark and MapReduce history files. If you do not specify a temp bucket, Dataproc will determine a Cloud Storage location (US, ASIA, or EU) for your cluster&#39;s temp bucket according to the Compute Engine zone where your cluster is deployed, and then create and manage this project-level, per-location bucket. The default bucket has a TTL of 90 days, but you can use any TTL (or none) if you specify a bucket (see Dataproc staging and temp buckets (https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/staging-bucket)). This field requires a Cloud Storage bucket name, not a gs://... URI to a Cloud Storage bucket. | [optional] 
**workerConfig** | [**InstanceGroupConfig**](InstanceGroupConfig.md) |  | [optional] 


