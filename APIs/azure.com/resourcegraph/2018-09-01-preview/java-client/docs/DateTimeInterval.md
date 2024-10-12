

# DateTimeInterval

An interval in time specifying the date and time for the inclusive start and exclusive end, i.e. `[start, end)`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**end** | **OffsetDateTime** | A datetime indicating the exclusive/open end of the time interval, i.e. &#x60;[start, &#x60;**&#x60;end&#x60;**&#x60;)&#x60;. Specifying an &#x60;end&#x60; that occurs chronologically before &#x60;start&#x60; will result in an error. |  |
|**start** | **OffsetDateTime** | A datetime indicating the inclusive/closed start of the time interval, i.e. &#x60;[&#x60;**&#x60;start&#x60;**&#x60;, end)&#x60;. Specifying a &#x60;start&#x60; that occurs chronologically after &#x60;end&#x60; will result in an error. |  |



