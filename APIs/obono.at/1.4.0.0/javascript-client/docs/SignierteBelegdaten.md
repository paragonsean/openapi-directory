# ObonoRksvApi.SignierteBelegdaten

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**belegDatumUhrzeit** | **String** |  | [optional] 
**belegnummer** | **String** |  | [optional] 
**betragBrutto** | **Number** |  | [optional] 
**betragNetto** | **Number** |  | [optional] 
**betragSatzBesondersBrutto** | **Number** | The total amount in cents | [optional] 
**betragSatzBesondersNetto** | **Number** | The total amount in cents | [optional] 
**betragSatzErmaessigt1Brutto** | **Number** | The total amount in cents | [optional] 
**betragSatzErmaessigt1Netto** | **Number** | The total amount in cents | [optional] 
**betragSatzErmaessigt2Brutto** | **Number** | The total amount in cents | [optional] 
**betragSatzErmaessigt2Netto** | **Number** | The total amount in cents | [optional] 
**betragSatzNormalBrutto** | **Number** | The total amount in cents | [optional] 
**betragSatzNormalNetto** | **Number** | The total amount in cents | [optional] 
**betragSatzNullBrutto** | **Number** | The total amount in cents | [optional] 
**betragSatzNullNetto** | **Number** | The total amount in cents | [optional] 
**externerBelegBelegkreis** | **String** |  | [optional] 
**externerBelegBezeichnung** | **String** |  | [optional] 
**externerBelegReferenz** | **String** |  | [optional] 
**kassenID** | **String** |  | [optional] 
**kunde** | **String** |  | [optional] 
**notizen** | **[String]** |  | [optional] 
**posten** | [**[Posten]**](Posten.md) |  | [optional] 
**rabatte** | [**[Rabatt]**](Rabatt.md) |  | [optional] 
**storno** | **Boolean** | Storno? | [optional] 
**stornoBelegUUID** | **String** | The &#x60;Beleg-UUID&#x60; property of the &#x60;Beleg&#x60; to be cancelled | [optional] 
**stornoText** | **String** |  | [optional] 
**training** | **Boolean** | Training? | [optional] 
**unternehmenAdresse1** | **String** |  | [optional] 
**unternehmenAdresse2** | **String** |  | [optional] 
**unternehmenFusszeile** | **String** |  | [optional] 
**unternehmenID** | **String** |  | [optional] 
**unternehmenIDTyp** | **String** |  | [optional] 
**unternehmenKopfzeile** | **String** |  | [optional] 
**unternehmenName** | **String** |  | [optional] 
**unternehmenOrt** | **String** |  | [optional] 
**unternehmenPLZ** | **String** |  | [optional] 
**zahlungen** | [**[Zahlung]**](Zahlung.md) |  | [optional] 
**zertifikatSeriennummer** | **String** |  | [optional] 



## Enum: UnternehmenIDTypEnum


* `steuernummer` (value: `"steuernummer"`)

* `uid` (value: `"uid"`)

* `gln` (value: `"gln"`)




