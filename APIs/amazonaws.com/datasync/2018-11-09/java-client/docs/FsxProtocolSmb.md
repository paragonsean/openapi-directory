

# FsxProtocolSmb

Specifies the Server Message Block (SMB) protocol configuration that DataSync uses to access your Amazon FSx for NetApp ONTAP file system. For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-access\">Accessing FSx for ONTAP file systems</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domain** | [**String**](String.md) |  |  [optional] |
|**mountOptions** | [**SmbMountOptions**](SmbMountOptions.md) |  |  [optional] |
|**password** | [**String**](String.md) |  |  |
|**user** | [**String**](String.md) |  |  |



