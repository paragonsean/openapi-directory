

# RegisterApplicationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationId** | **String** | The ID of the application. |  |
|**applicationType** | [**ApplicationTypeEnum**](#ApplicationTypeEnum) | The type of the application. |  |
|**instances** | **List&lt;String&gt;** | The Amazon EC2 instances on which your SAP application is running. |  |
|**sapInstanceNumber** | **String** | The SAP instance number of the application. |  [optional] |
|**sid** | **String** | The System ID of the application. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags to be attached to the SAP application. |  [optional] |
|**credentials** | [**List&lt;ApplicationCredential&gt;**](ApplicationCredential.md) | The credentials of the SAP application. |  |



## Enum: ApplicationTypeEnum

| Name | Value |
|---- | -----|
| HANA | &quot;HANA&quot; |



