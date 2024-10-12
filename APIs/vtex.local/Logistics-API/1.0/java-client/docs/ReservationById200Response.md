

# ReservationById200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizedDateUtc** | **String** | Authorized date in UTC. |  [optional] |
|**canceledDateUtc** | **String** | Canceled date in UTC. |  [optional] |
|**confirmedDateUtc** | **String** | Confirmed date in UTC. |  [optional] |
|**errors** | **List&lt;String&gt;** | Information on errors, if there are any. |  [optional] |
|**isSucess** | **Boolean** |  |  [optional] |
|**lastUpdateDateUtc** | **String** | Date of the last update in UTC. |  [optional] |
|**lockId** | **String** | Lock ID. |  [optional] |
|**maximumConfirmationDateUtc** | **String** | Maximum confirmation date in UTC. |  [optional] |
|**pickupPointItemOptions** | **String** | Pickup point item options. |  [optional] |
|**reservationDateUtc** | **String** | Reservation date in UTC. |  [optional] |
|**salesChannel** | **String** | Sales channel. |  [optional] |
|**slaRequest** | [**List&lt;ReservationById200ResponseSlaRequestInner&gt;**](ReservationById200ResponseSlaRequestInner.md) | Information on SLA request. |  [optional] |
|**status** | **Integer** | Reservation status, being:  &#x60;0&#x60;: &#x60;NotCommitted&#x60;  &#x60;1&#x60;: &#x60;Authorized&#x60;  &#x60;2&#x60;: &#x60;Confirmed&#x60;  &#x60;3&#x60;: &#x60;Canceled_AbortedCommitted&#x60;  &#x60;4&#x60;: &#x60;Canceled_AuthorizationExpired&#x60;  &#x60;5&#x60;: &#x60;Canceled_Manually&#x60; |  [optional] |



