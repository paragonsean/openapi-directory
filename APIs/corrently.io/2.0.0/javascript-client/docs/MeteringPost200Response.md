# CorrentlyIo.MeteringPost200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_180** | **Number** | Reading as provided as input in Wh | [optional] 
**_181** | **Number** | Green energy calculated using Green Power Index (GrünstromIndex) in Wh | [optional] 
**_182** | **Number** | Grey energy calculated using Green Power Index (GrünstromIndex) in Wh | [optional] 
**processingTime** | **Number** | Time this reading got imported into consensus (e.q. signed timestamp). | [optional] 
**account** | **String** | Stromkonto/Metering address allocated (this is not the MELOID!) | [optional] 
**co2GOekostrom** | **Number** | CO2 Emission of metered energy in a green energy mix (e.q. Ökostromtarif) | [optional] 
**co2GStandard** | **Number** | CO2 Emission of metered energy in a standard mix | [optional] 
**timeStamp** | **Number** | API Consensus time this reading was fully received | [optional] 


