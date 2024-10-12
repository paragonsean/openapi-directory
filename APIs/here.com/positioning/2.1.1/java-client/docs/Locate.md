

# Locate

Object wrapping the location data submitted in a request for a position. At least one of `gsm`, `wcdma`, `tdscdma`, `lte`, `cdma`, or `wlan` elements is required. Array elements should be unique within the request. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cdma** | [**List&lt;Cdma&gt;**](Cdma.md) | CDMA cells (CDMA2000) |  [optional] |
|**client** | [**ClientInfo**](ClientInfo.md) |  |  [optional] |
|**gsm** | [**List&lt;Gsm&gt;**](Gsm.md) | GSM cells (GERAN) |  [optional] |
|**lte** | [**List&lt;Lte&gt;**](Lte.md) | LTE cells (E-UTRA, 4G) |  [optional] |
|**tdscdma** | [**List&lt;Tdscdma&gt;**](Tdscdma.md) | TD-SCDMA cells (UTRA-TDD, 3G UMTS TDD) |  [optional] |
|**wcdma** | [**List&lt;Wcdma&gt;**](Wcdma.md) | WCDMA cells (UTRA-FDD, 3G UMTS) |  [optional] |
|**wlan** | [**List&lt;WlanLocate&gt;**](WlanLocate.md) | WLAN access positions. For privacy reasons positioning based on a single WLAN AP is not possible; there has to be at least one other matching wlan or cell. Alternatively, you can allow fallbacks to less accurate single WLAN AP location estimates by using the setting &#x60;fallback&#x3D;singleWifi&#x60;.  |  [optional] |



