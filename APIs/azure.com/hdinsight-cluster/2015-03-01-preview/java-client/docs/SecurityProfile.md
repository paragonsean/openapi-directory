

# SecurityProfile

The security profile which contains Ssh public key for the HDInsight cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aaddsResourceId** | **String** | The resource ID of the user&#39;s Azure Active Directory Domain Service. |  [optional] |
|**clusterUsersGroupDNs** | **List&lt;String&gt;** | Optional. The Distinguished Names for cluster user groups |  [optional] |
|**directoryType** | [**DirectoryTypeEnum**](#DirectoryTypeEnum) | The directory type. |  [optional] |
|**domain** | **String** | The organization&#39;s active directory domain. |  [optional] |
|**domainUserPassword** | **String** | The domain admin password. |  [optional] |
|**domainUsername** | **String** | The domain user account that will have admin privileges on the cluster. |  [optional] |
|**ldapsUrls** | **List&lt;String&gt;** | The LDAPS protocol URLs to communicate with the Active Directory. |  [optional] |
|**msiResourceId** | **String** | User assigned identity that has permissions to read and create cluster-related artifacts in the user&#39;s AADDS. |  [optional] |
|**organizationalUnitDN** | **String** | The organizational unit within the Active Directory to place the cluster and service accounts. |  [optional] |



## Enum: DirectoryTypeEnum

| Name | Value |
|---- | -----|
| ACTIVE_DIRECTORY | &quot;ActiveDirectory&quot; |



