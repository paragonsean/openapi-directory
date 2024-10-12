

# SvmEndpoint

An Amazon FSx for NetApp ONTAP storage virtual machine (SVM) has four endpoints that are used to access data or to manage the SVM using the NetApp ONTAP CLI, REST API, or NetApp CloudManager. They are the <code>Iscsi</code>, <code>Management</code>, <code>Nfs</code>, and <code>Smb</code> endpoints.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnSName** | **String** | The file system&#39;s DNS name. You can mount your file system using its DNS name. |  [optional] |
|**ipAddresses** | [**List**](List.md) |  |  [optional] |



