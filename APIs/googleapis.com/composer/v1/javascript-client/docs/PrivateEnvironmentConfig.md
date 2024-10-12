# CloudComposerApi.PrivateEnvironmentConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudComposerConnectionSubnetwork** | **String** | Optional. When specified, the environment will use Private Service Connect instead of VPC peerings to connect to Cloud SQL in the Tenant Project, and the PSC endpoint in the Customer Project will use an IP address from this subnetwork. | [optional] 
**cloudComposerNetworkIpv4CidrBlock** | **String** | Optional. The CIDR block from which IP range for Cloud Composer Network in tenant project will be reserved. Needs to be disjoint from private_cluster_config.master_ipv4_cidr_block and cloud_sql_ipv4_cidr_block. This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. | [optional] 
**cloudComposerNetworkIpv4ReservedRange** | **String** | Output only. The IP range reserved for the tenant project&#39;s Cloud Composer network. This field is supported for Cloud Composer environments in versions composer-2.*.*-airflow-*.*.* and newer. | [optional] [readonly] 
**cloudSqlIpv4CidrBlock** | **String** | Optional. The CIDR block from which IP range in tenant project will be reserved for Cloud SQL. Needs to be disjoint from &#x60;web_server_ipv4_cidr_block&#x60;. | [optional] 
**enablePrivateBuildsOnly** | **Boolean** | Optional. If &#x60;true&#x60;, builds performed during operations that install Python packages have only private connectivity to Google services (including Artifact Registry) and VPC network (if either &#x60;NodeConfig.network&#x60; and &#x60;NodeConfig.subnetwork&#x60; fields or &#x60;NodeConfig.composer_network_attachment&#x60; field are specified). If &#x60;false&#x60;, the builds also have access to the internet. This field is supported for Cloud Composer environments in versions composer-3.*.*-airflow-*.*.* and newer. | [optional] 
**enablePrivateEnvironment** | **Boolean** | Optional. If &#x60;true&#x60;, a Private IP Cloud Composer environment is created. If this field is set to true, &#x60;IPAllocationPolicy.use_ip_aliases&#x60; must be set to true for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. | [optional] 
**enablePrivatelyUsedPublicIps** | **Boolean** | Optional. When enabled, IPs from public (non-RFC1918) ranges can be used for &#x60;IPAllocationPolicy.cluster_ipv4_cidr_block&#x60; and &#x60;IPAllocationPolicy.service_ipv4_cidr_block&#x60;. | [optional] 
**networkingConfig** | [**NetworkingConfig**](NetworkingConfig.md) |  | [optional] 
**privateClusterConfig** | [**PrivateClusterConfig**](PrivateClusterConfig.md) |  | [optional] 
**webServerIpv4CidrBlock** | **String** | Optional. The CIDR block from which IP range for web server will be reserved. Needs to be disjoint from &#x60;private_cluster_config.master_ipv4_cidr_block&#x60; and &#x60;cloud_sql_ipv4_cidr_block&#x60;. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. | [optional] 
**webServerIpv4ReservedRange** | **String** | Output only. The IP range reserved for the tenant project&#39;s App Engine VMs. This field is supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. | [optional] [readonly] 


