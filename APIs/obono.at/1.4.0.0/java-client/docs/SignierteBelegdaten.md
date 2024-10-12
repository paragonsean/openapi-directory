

# SignierteBelegdaten

The complete `Beleg` that has been signed by the \"Signaturerstellungseinheit\" and stored in the \"Datenerfassungsprotokoll\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**belegDatumUhrzeit** | **String** |  |  [optional] |
|**belegnummer** | **String** |  |  [optional] |
|**betragBrutto** | **Integer** |  |  [optional] |
|**betragNetto** | **Integer** |  |  [optional] |
|**betragSatzBesondersBrutto** | **Integer** | The total amount in cents |  [optional] |
|**betragSatzBesondersNetto** | **Integer** | The total amount in cents |  [optional] |
|**betragSatzErmaessigt1Brutto** | **Integer** | The total amount in cents |  [optional] |
|**betragSatzErmaessigt1Netto** | **Integer** | The total amount in cents |  [optional] |
|**betragSatzErmaessigt2Brutto** | **Integer** | The total amount in cents |  [optional] |
|**betragSatzErmaessigt2Netto** | **Integer** | The total amount in cents |  [optional] |
|**betragSatzNormalBrutto** | **Integer** | The total amount in cents |  [optional] |
|**betragSatzNormalNetto** | **Integer** | The total amount in cents |  [optional] |
|**betragSatzNullBrutto** | **Integer** | The total amount in cents |  [optional] |
|**betragSatzNullNetto** | **Integer** | The total amount in cents |  [optional] |
|**externerBelegBelegkreis** | **String** |  |  [optional] |
|**externerBelegBezeichnung** | **String** |  |  [optional] |
|**externerBelegReferenz** | **String** |  |  [optional] |
|**kassenID** | **String** |  |  [optional] |
|**kunde** | **String** |  |  [optional] |
|**notizen** | **List&lt;String&gt;** |  |  [optional] |
|**posten** | [**List&lt;Posten&gt;**](Posten.md) |  |  [optional] |
|**rabatte** | [**List&lt;Rabatt&gt;**](Rabatt.md) |  |  [optional] |
|**storno** | **Boolean** | Storno? |  [optional] |
|**stornoBelegUUID** | **UUID** | The &#x60;Beleg-UUID&#x60; property of the &#x60;Beleg&#x60; to be cancelled |  [optional] |
|**stornoText** | **String** |  |  [optional] |
|**training** | **Boolean** | Training? |  [optional] |
|**unternehmenAdresse1** | **String** |  |  [optional] |
|**unternehmenAdresse2** | **String** |  |  [optional] |
|**unternehmenFusszeile** | **String** |  |  [optional] |
|**unternehmenID** | **String** |  |  [optional] |
|**unternehmenIDTyp** | [**UnternehmenIDTypEnum**](#UnternehmenIDTypEnum) |  |  [optional] |
|**unternehmenKopfzeile** | **String** |  |  [optional] |
|**unternehmenName** | **String** |  |  [optional] |
|**unternehmenOrt** | **String** |  |  [optional] |
|**unternehmenPLZ** | **String** |  |  [optional] |
|**zahlungen** | [**List&lt;Zahlung&gt;**](Zahlung.md) |  |  [optional] |
|**zertifikatSeriennummer** | **String** |  |  [optional] |



## Enum: UnternehmenIDTypEnum

| Name | Value |
|---- | -----|
| STEUERNUMMER | &quot;steuernummer&quot; |
| UID | &quot;uid&quot; |
| GLN | &quot;gln&quot; |



