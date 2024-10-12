# TwilioWireless.WirelessV1SimDataSession

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the DataSession resource. | [optional] 
**cellId** | **String** | The unique ID of the cellular tower that the device was attached to at the moment when the Data Session was last updated. | [optional] 
**cellLocationEstimate** | **Object** | An object that describes the estimated location in latitude and longitude where the device&#39;s Data Session took place. The location is derived from the &#x60;cell_id&#x60; when the Data Session was last updated. See [Cell Location Estimate Object](https://www.twilio.com/docs/iot/wireless/api/datasession-resource#cell-location-estimate-object).  | [optional] 
**end** | **Date** | The date that the record ended, given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | [optional] 
**imei** | **String** | The &#39;international mobile equipment identity&#39; is the unique ID of the device using the SIM to connect. An IMEI is a 15-digit string: 14 digits for the device identifier plus a check digit calculated using the Luhn formula. | [optional] 
**lastUpdated** | **Date** | The date that the resource was last updated, given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | [optional] 
**operatorCountry** | **String** | The three letter country code representing where the device&#39;s Data Session took place. This is determined by looking up the &#x60;operator_mcc&#x60;. | [optional] 
**operatorMcc** | **String** | The &#39;mobile country code&#39; is the unique ID of the home country where the Data Session took place. See: [MCC/MNC lookup](http://mcc-mnc.com/). | [optional] 
**operatorMnc** | **String** | The &#39;mobile network code&#39; is the unique ID specific to the mobile operator network where the Data Session took place. | [optional] 
**operatorName** | **String** | The friendly name of the mobile operator network that the [SIM](https://www.twilio.com/docs/iot/wireless/api/sim-resource)-connected device is attached to. This is determined by looking up the &#x60;operator_mnc&#x60;. | [optional] 
**packetsDownloaded** | **Number** | The number of packets downloaded by the device between the &#x60;start&#x60; time and when the Data Session was last updated. | [optional] 
**packetsUploaded** | **Number** | The number of packets uploaded by the device between the &#x60;start&#x60; time and when the Data Session was last updated. | [optional] 
**radioLink** | **String** | The generation of wireless technology that the device was using. | [optional] 
**sid** | **String** | The unique string that we created to identify the DataSession resource. | [optional] 
**simSid** | **String** | The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource) that the Data Session is for. | [optional] 
**start** | **Date** | The date that the Data Session started, given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | [optional] 


