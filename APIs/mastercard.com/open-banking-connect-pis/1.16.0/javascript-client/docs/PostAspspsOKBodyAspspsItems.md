# OpenBankingPaymentsInitiationService.PostAspspsOKBodyAspspsItems

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspspServices** | **[String]** | Provided services, AIS - account information, PIS - payment initiation | [optional] 
**capabilities** | **{String: Boolean}** | Capabilities related to api profile assigned to ASPSP | [optional] 
**country** | **String** | Country code | [optional] 
**id** | **String** | Identification of the ASPSP | [optional] 
**logo** | [**LogoObject**](LogoObject.md) |  | [optional] 
**name** | **String** | Name of the ASPSP | [optional] 
**profile** | **String** | ASPSP profile | [optional] 



## Enum: [AspspServicesEnum]


* `AIS` (value: `"AIS"`)

* `PIS` (value: `"PIS"`)

* `COF` (value: `"COF"`)




