# HereNetworkPositioningApiV2.Locate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdma** | [**[Cdma]**](Cdma.md) | CDMA cells (CDMA2000) | [optional] 
**client** | [**ClientInfo**](ClientInfo.md) |  | [optional] 
**gsm** | [**[Gsm]**](Gsm.md) | GSM cells (GERAN) | [optional] 
**lte** | [**[Lte]**](Lte.md) | LTE cells (E-UTRA, 4G) | [optional] 
**tdscdma** | [**[Tdscdma]**](Tdscdma.md) | TD-SCDMA cells (UTRA-TDD, 3G UMTS TDD) | [optional] 
**wcdma** | [**[Wcdma]**](Wcdma.md) | WCDMA cells (UTRA-FDD, 3G UMTS) | [optional] 
**wlan** | [**[WlanLocate]**](WlanLocate.md) | WLAN access positions. For privacy reasons positioning based on a single WLAN AP is not possible; there has to be at least one other matching wlan or cell. Alternatively, you can allow fallbacks to less accurate single WLAN AP location estimates by using the setting &#x60;fallback&#x3D;singleWifi&#x60;.  | [optional] 


