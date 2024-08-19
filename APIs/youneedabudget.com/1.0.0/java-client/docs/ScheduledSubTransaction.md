

# ScheduledSubTransaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Long** | The scheduled subtransaction amount in milliunits format |  |
|**categoryId** | **UUID** |  |  [optional] |
|**deleted** | **Boolean** | Whether or not the scheduled subtransaction has been deleted.  Deleted scheduled subtransactions will only be included in delta requests. |  |
|**id** | **UUID** |  |  |
|**memo** | **String** |  |  [optional] |
|**payeeId** | **UUID** |  |  [optional] |
|**scheduledTransactionId** | **UUID** |  |  |
|**transferAccountId** | **UUID** | If a transfer, the account_id which the scheduled subtransaction transfers to |  [optional] |



