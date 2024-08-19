# SquareConnectApi.Break

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakTypeId** | **String** | The &#x60;BreakType&#x60; that this &#x60;Break&#x60; was templated on. | 
**endAt** | **String** | RFC 3339; follows the same timezone information as &#x60;Shift&#x60;. Precision up to the minute is respected; seconds are truncated. | [optional] 
**expectedDuration** | **String** | Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of the break. | 
**id** | **String** | The UUID for this object. | [optional] 
**isPaid** | **Boolean** | Whether this break counts towards time worked for compensation purposes. | 
**name** | **String** | A human-readable name. | 
**startAt** | **String** | RFC 3339; follows the same timezone information as &#x60;Shift&#x60;. Precision up to the minute is respected; seconds are truncated. | 


