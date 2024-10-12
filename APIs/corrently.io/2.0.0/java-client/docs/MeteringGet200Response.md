

# MeteringGet200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_1_8_0** | **Integer** | Reading as provided as input in Wh |  [optional] |
|**_1_8_1** | **Integer** | Green energy calculated using Green Power Index (GrünstromIndex) in Wh |  [optional] |
|**_1_8_2** | **Integer** | Grey energy calculated using Green Power Index (GrünstromIndex) in Wh |  [optional] |
|**processingTime** | **Integer** | Time this reading got imported into consensus (e.q. signed timestamp). |  [optional] |
|**account** | **String** | Stromkonto/Metering address allocated (this is not the MELOID!) |  [optional] |
|**co2GOekostrom** | **Integer** | CO2 Emission of metered energy in a green energy mix (e.q. Ökostromtarif) |  [optional] |
|**co2GStandard** | **Integer** | CO2 Emission of metered energy in a standard mix |  [optional] |
|**credits** | **Object** | Update credits this meter has. Gets refilled automtically to prevent too frequent updates |  [optional] |
|**timeStamp** | **Integer** | API Consensus time this reading was fully received |  [optional] |
|**ttl** | **Integer** | Time to Live for this reader. If no update is provided it gets decommissioned. |  [optional] |



