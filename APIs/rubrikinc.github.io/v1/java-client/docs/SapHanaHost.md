

# SapHanaHost


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostName** | **String** | The IP address or fully qualified domain name of the SAP HANA host. |  |
|**hostType** | [**HostTypeEnum**](#HostTypeEnum) | The type of the SAP HANA system host. Possible values are MASTER, SLAVE, SECONDARY_MASTER or SECONDARY_SLAVE . |  [optional] |
|**hostUuid** | **String** | The ID of the SAP HANA system host. |  |
|**sapHanaHostName** | **String** | The local name of the SAP HANA host. |  [optional] |
|**status** | **String** | The status of the SAP HANA system host. |  |



## Enum: HostTypeEnum

| Name | Value |
|---- | -----|
| MASTER | &quot;MASTER&quot; |
| SLAVE | &quot;SLAVE&quot; |
| SECONDARY_MASTER | &quot;SECONDARY_MASTER&quot; |
| SECONDARY_SLAVE | &quot;SECONDARY_SLAVE&quot; |



