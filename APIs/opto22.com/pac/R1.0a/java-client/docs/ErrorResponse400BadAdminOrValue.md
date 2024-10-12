

# ErrorResponse400BadAdminOrValue


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorCode** | **Integer** | Details: ** -1 ** Invalid or no strategy. Use PAC Control to download strategy logic. ** -3 ** Buffer overrun or invalid length. The number or range of table indicies you specified exceeds elements in the PAC Control table. ** -8 ** Invalid data. Check format of data written. Compare to what&#39;s read for the same endpoint. ** -12 ** You&#39;ve passed a table index that is less than zero or greater than the length of the table minus 1. ** -13 ** The value you passed to write is outside of the valid range for the PAC Control data type you&#39;re writing to. For example, if you specified the value 999999999999999 for an integer32 (since integer32 data types must be in the range: -2147483648 to 2147483647). ** -17 or -20 ** The controller is busy with another task, for example, downloading a new strategy. Try again later. ** -36 ** Endpoint is not defined. ** -109 ** Attempting to write without write permissions. Check /admin/keys settings. ** -13019 ** Invalid endpoint. Check syntax of the URL (e.g. did you use &#39;ev&#39; instead of &#39;eu&#39;). ** 400 ** Before using the API on this device, you must first change the default user name and password via the URL /admin/keys. Use the default User Name: &#39;admin&#39; and Password: &#39;password&#39; to log ininitially. |  |
|**message** | **String** |  |  |



