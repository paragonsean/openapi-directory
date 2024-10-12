# RubrikRestApi.SapHanaSystemSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainType** | [**ConfiguredSlaType**](ConfiguredSlaType.md) |  | [optional] 
**id** | **String** | The ID of the SAP HANA system. | 
**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. | [optional] 
**name** | **String** | The name of the Rubrik object. | 
**primaryClusterId** | **String** | The ID of the cluster that manages the Rubrik object. | 
**slaLastUpdateTime** | **Date** | The UTC time when the SLA Domain was last updated. | [optional] 
**containerType** | **String** | The container type of the SAP HANA system. Possible values are SINGLE_CONTAINER, MULTI_CONTAINER. | [optional] 
**hosts** | [**[SapHanaHost]**](SapHanaHost.md) |  | 
**instanceNumber** | **String** | The instance number of the SAP HANA system. | 
**lastRefreshTime** | **Date** | The UTC timestamp for when the SAP HANA system was last refreshed. | [optional] 
**numDbs** | **Number** | The number of databases in the SAP HANA system. | 
**sid** | **String** | The SAP System Identification (SID) code for the SAP HANA system. | 
**sslInfo** | [**SapHanaSslInfo**](SapHanaSslInfo.md) |  | [optional] 
**status** | **String** | The status of the SAP HANA system. | 
**statusMessage** | **String** | The message associated with the current SAP HANA system status. | [optional] 
**systemInfo** | [**SapHanaSystemInfo**](SapHanaSystemInfo.md) |  | [optional] 
**username** | **String** | The username of the SAP HANA system. | 



## Enum: ContainerTypeEnum


* `SINGLE_CONTAINER` (value: `"SINGLE_CONTAINER"`)

* `MULTI_CONTAINER` (value: `"MULTI_CONTAINER"`)





## Enum: StatusEnum


* `OK` (value: `"OK"`)

* `WARNING` (value: `"WARNING"`)

* `ERROR` (value: `"ERROR"`)

* `UNKNOWN` (value: `"UNKNOWN"`)




