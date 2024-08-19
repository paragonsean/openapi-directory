

# LinuxConfiguration

Specifies the Linux operating system settings on the virtual machine. <br><br>For a list of supported Linux distributions, see [Linux on Azure-Endorsed Distributions](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-endorsed-distros?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json) <br><br> For running non-endorsed distributions, see [Information for Non-Endorsed Distributions](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-linux-create-upload-generic?toc=%2fazure%2fvirtual-machines%2flinux%2ftoc.json).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disablePasswordAuthentication** | **Boolean** | Specifies whether password authentication should be disabled. |  [optional] |
|**ssh** | [**SshConfiguration**](SshConfiguration.md) |  |  [optional] |



