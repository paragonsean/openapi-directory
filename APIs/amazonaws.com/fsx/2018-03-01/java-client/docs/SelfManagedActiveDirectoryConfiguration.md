

# SelfManagedActiveDirectoryConfiguration

The configuration that Amazon FSx uses to join a FSx for Windows File Server file system or an FSx for ONTAP storage virtual machine (SVM) to a self-managed (including on-premises) Microsoft Active Directory (AD) directory. For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html\"> Using Amazon FSx for Windows with your self-managed Microsoft Active Directory</a> or <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html\">Managing FSx for ONTAP SVMs</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | [**String**](String.md) |  |  |
|**organizationalUnitDistinguishedName** | [**String**](String.md) |  |  [optional] |
|**fileSystemAdministratorsGroup** | [**String**](String.md) |  |  [optional] |
|**userName** | [**String**](String.md) |  |  |
|**password** | [**String**](String.md) |  |  |
|**dnsIps** | [**List**](List.md) |  |  |



