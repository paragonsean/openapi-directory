

# IPAllocationPolicy

Configuration for controlling how IPs are allocated in the GKE cluster running the Apache Airflow software.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterIpv4CidrBlock** | **String** | Optional. The IP address range used to allocate IP addresses to pods in the GKE cluster. For Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*, this field is applicable only when &#x60;use_ip_aliases&#x60; is true. Set to blank to have GKE choose a range with the default size. Set to /netmask (e.g. &#x60;/14&#x60;) to have GKE choose a range with a specific netmask. Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. &#x60;10.96.0.0/14&#x60;) from the RFC-1918 private networks (e.g. &#x60;10.0.0.0/8&#x60;, &#x60;172.16.0.0/12&#x60;, &#x60;192.168.0.0/16&#x60;) to pick a specific range to use. |  [optional] |
|**clusterSecondaryRangeName** | **String** | Optional. The name of the GKE cluster&#39;s secondary range used to allocate IP addresses to pods. For Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*, this field is applicable only when &#x60;use_ip_aliases&#x60; is true. |  [optional] |
|**servicesIpv4CidrBlock** | **String** | Optional. The IP address range of the services IP addresses in this GKE cluster. For Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*, this field is applicable only when &#x60;use_ip_aliases&#x60; is true. Set to blank to have GKE choose a range with the default size. Set to /netmask (e.g. &#x60;/14&#x60;) to have GKE choose a range with a specific netmask. Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. &#x60;10.96.0.0/14&#x60;) from the RFC-1918 private networks (e.g. &#x60;10.0.0.0/8&#x60;, &#x60;172.16.0.0/12&#x60;, &#x60;192.168.0.0/16&#x60;) to pick a specific range to use. |  [optional] |
|**servicesSecondaryRangeName** | **String** | Optional. The name of the services&#39; secondary range used to allocate IP addresses to the GKE cluster. For Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*, this field is applicable only when &#x60;use_ip_aliases&#x60; is true. |  [optional] |
|**useIpAliases** | **Boolean** | Optional. Whether or not to enable Alias IPs in the GKE cluster. If &#x60;true&#x60;, a VPC-native cluster is created. This field is only supported for Cloud Composer environments in versions composer-1.*.*-airflow-*.*.*. Environments in newer versions always use VPC-native GKE clusters. |  [optional] |



