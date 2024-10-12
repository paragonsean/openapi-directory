

# AccountHolderUpcomingDeadlineNotificationContent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the account holder whom the event refers to. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) | The event name that will be trigger if no action is taken. |  [optional] |
|**executionDate** | **OffsetDateTime** | The execution date scheduled for the event. |  [optional] |
|**reason** | **String** | The reason that leads to scheduling of the event. |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| ACCESS_PII | &quot;AccessPii&quot; |
| API_TIER_UPDATE | &quot;ApiTierUpdate&quot; |
| CLOSE_ACCOUNT | &quot;CloseAccount&quot; |
| CLOSE_STORES | &quot;CloseStores&quot; |
| DELETE_BALANCE_ACCOUNTS | &quot;DeleteBalanceAccounts&quot; |
| DELETE_BANK_ACCOUNTS | &quot;DeleteBankAccounts&quot; |
| DELETE_LEGAL_ARRANGEMENTS | &quot;DeleteLegalArrangements&quot; |
| DELETE_LIABLE_BANK_ACCOUNT | &quot;DeleteLiableBankAccount&quot; |
| DELETE_PAYOUT_METHODS | &quot;DeletePayoutMethods&quot; |
| DELETE_SHAREHOLDERS | &quot;DeleteShareholders&quot; |
| DELETE_SIGNATORIES | &quot;DeleteSignatories&quot; |
| INACTIVATE_ACCOUNT | &quot;InactivateAccount&quot; |
| KYC_DEADLINE_EXTENSION | &quot;KYCDeadlineExtension&quot; |
| MIGRATE_ACCOUNT_TO_BP | &quot;MigrateAccountToBP&quot; |
| RECALCULATE_ACCOUNT_STATUS_AND_PROCESSING_TIER | &quot;RecalculateAccountStatusAndProcessingTier&quot; |
| REFUND_NOT_PAID_OUT_TRANSFERS | &quot;RefundNotPaidOutTransfers&quot; |
| RESOLVE_EVENTS | &quot;ResolveEvents&quot; |
| SAVE_ACCOUNT_HOLDER | &quot;SaveAccountHolder&quot; |
| SAVE_KYC_CHECK_STATUS | &quot;SaveKYCCheckStatus&quot; |
| SAVE_PEP_CHECKS | &quot;SavePEPChecks&quot; |
| SUSPEND_ACCOUNT | &quot;SuspendAccount&quot; |
| UN_SUSPEND_ACCOUNT | &quot;UnSuspendAccount&quot; |
| UPDATE_ACCOUNT_HOLDER_STATE | &quot;UpdateAccountHolderState&quot; |
| VERIFICATION | &quot;Verification&quot; |



