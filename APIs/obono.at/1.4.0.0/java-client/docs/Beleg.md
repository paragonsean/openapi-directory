

# Beleg


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**belegCodes** | **List&lt;String&gt;** |  |  [optional] |
|**belegTypen** | [**List&lt;BelegTypenEnum&gt;**](#List&lt;BelegTypenEnum&gt;) |  |  [optional] |
|**belegdaten** | [**SignierteBelegdaten**](SignierteBelegdaten.md) |  |  [optional] |
|**JWS** | **String** | The signed &#x60;Beleg&#x60; as a JWS signature token. |  [optional] |
|**QR** | **String** | The portion of the &#x60;JWS&#x60; token to be used for generating QR codes. |  [optional] |
|**qrLink** | **String** | A hyperlink that retrieves the &#x60;QR&#x60; data. |  [optional] |
|**registrierkasseUUID** | **UUID** | The &#x60;_uuid&#x60; of the &#x60;Registrierkasse&#x60; that has issued this &#x60;Beleg&#x60;. |  [optional] |
|**signaturerstellungseinheitUUID** | **UUID** | The &#x60;_uuid&#x60; of the &#x60;Signaturerstellungseinheit&#x60; that has signed this &#x60;Beleg&#x60;. |  [optional] |
|**href** | **String** | URL of the particular &#x60;Beleg&#x60; instance. |  [optional] |
|**uuid** | **String** | Unique ID of the particular &#x60;Beleg&#x60; instance. |  [optional] |



## Enum: List&lt;BelegTypenEnum&gt;

| Name | Value |
|---- | -----|
| BELEGKREISINITIALISIERUNG | &quot;Belegkreisinitialisierung&quot; |
| KASSENBERICHT | &quot;Kassenbericht&quot; |
| MONATSABSCHLUSS | &quot;Monatsabschluss&quot; |
| STARTBELEG | &quot;Startbeleg&quot; |
| STORNO | &quot;Storno&quot; |
| SYSTEMBELEG | &quot;Systembeleg&quot; |
| TRAINING | &quot;Training&quot; |



