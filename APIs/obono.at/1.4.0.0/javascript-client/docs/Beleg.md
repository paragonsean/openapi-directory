# ObonoRksvApi.Beleg

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**belegCodes** | **[String]** |  | [optional] 
**belegTypen** | **[String]** |  | [optional] 
**belegdaten** | [**SignierteBelegdaten**](SignierteBelegdaten.md) |  | [optional] 
**JWS** | **String** | The signed &#x60;Beleg&#x60; as a JWS signature token. | [optional] 
**QR** | **String** | The portion of the &#x60;JWS&#x60; token to be used for generating QR codes. | [optional] 
**qRLink** | **String** | A hyperlink that retrieves the &#x60;QR&#x60; data. | [optional] 
**registrierkasseUUID** | **String** | The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; that has issued this &#x60;Beleg&#x60;. | [optional] 
**signaturerstellungseinheitUUID** | **String** | The &#x60;_uuid&#x60; of the &#x60;Signaturerstellungseinheit&#x60; that has signed this &#x60;Beleg&#x60;. | [optional] 
**href** | **String** | URL of the particular &#x60;Beleg&#x60; instance. | [optional] 
**uuid** | **String** | Unique ID of the particular &#x60;Beleg&#x60; instance. | [optional] 



## Enum: [BelegTypenEnum]


* `Belegkreisinitialisierung` (value: `"Belegkreisinitialisierung"`)

* `Kassenbericht` (value: `"Kassenbericht"`)

* `Monatsabschluss` (value: `"Monatsabschluss"`)

* `Startbeleg` (value: `"Startbeleg"`)

* `Storno` (value: `"Storno"`)

* `Systembeleg` (value: `"Systembeleg"`)

* `Training` (value: `"Training"`)




