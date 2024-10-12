

# Gsm

GSM measurement

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cid** | **Integer** | Cell identifier (GERAN CID) |  |
|**lac** | **Integer** | Location Area Code (LAC). Note, value 65534 is invalid. |  |
|**localId** | [**GsmLocalId**](GsmLocalId.md) |  |  [optional] |
|**mcc** | **Integer** | Mobile Country Code (MCC). Note: 0xx is for test networks, 1xx and 8xx are not used  |  |
|**mnc** | **Integer** | Mobile Network Code (MNC). |  |
|**nmr** | [**List&lt;GsmNmr&gt;**](GsmNmr.md) | GSM Network measurements |  [optional] |
|**rxLevel** | **Integer** | Received Signal power (dBm). Power less than -110dBm should be mapped to -110. Power greater than -25dBm should be mapped to -25.  |  [optional] |
|**ta** | **Integer** | Timing advance (TA). Expressed in the units of GSM bits equaling to 48/13 μs ~ 1107 meters. |  [optional] |



