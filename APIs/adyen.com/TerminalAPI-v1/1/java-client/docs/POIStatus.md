

# POIStatus

Indicate the availability of the POI Terminal components. The data element is absent if the component is not part of the POI Terminal. State of a POI Terminal.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardReaderOKFlag** | **Boolean** | If card reader device present. |  [optional] |
|**cashHandlingDevice** | [**List&lt;CashHandlingDevice&gt;**](CashHandlingDevice.md) |  |  [optional] |
|**communicationOKFlag** | **Boolean** | If communication infrastructure present. |  [optional] |
|**fraudPreventionFlag** | **Boolean** | default False. |  [optional] |
|**globalStatus** | **GlobalStatus** |  |  |
|**peDOKFlag** | **Boolean** | If PED present. |  [optional] |
|**printerStatus** | **PrinterStatus** |  |  [optional] |
|**securityOKFlag** | **Boolean** | If security module present. |  [optional] |



