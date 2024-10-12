

# StorageDatabasecenterPartnerapiV1mainDatabaseResourceHealthSignalData

Common model for database resource health signal data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalMetadata** | **Map&lt;String, Object&gt;** | Any other additional metadata |  [optional] |
|**compliance** | [**List&lt;StorageDatabasecenterPartnerapiV1mainCompliance&gt;**](StorageDatabasecenterPartnerapiV1mainCompliance.md) | Industry standards associated with this signal; if this signal is an issue, that could be a violation of the associated industry standard(s). For example, AUTO_BACKUP_DISABLED signal is associated with CIS GCP 1.1, CIS GCP 1.2, CIS GCP 1.3, NIST 800-53 and ISO-27001 compliance standards. If a database resource does not have automated backup enable, it will violate these following industry standards. |  [optional] |
|**description** | **String** | Description associated with signal |  [optional] |
|**eventTime** | **String** | Required. The last time at which the event described by this signal took place |  [optional] |
|**externalUri** | **String** | The external-uri of the signal, using which more information about this signal can be obtained. In GCP, this will take user to SCC page to get more details about signals. |  [optional] |
|**name** | **String** | Required. The name of the signal, ex: PUBLIC_SQL_INSTANCE, SQL_LOG_ERROR_VERBOSITY etc. |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) | Cloud provider name. Ex: GCP/AWS/Azure/OnPrem/SelfManaged |  [optional] |
|**resourceContainer** | **String** | Closest parent container of this resource. In GCP, &#39;container&#39; refers to a Cloud Resource Manager project. It must be resource name of a Cloud Resource Manager project with the format of \&quot;provider//\&quot;, such as \&quot;projects/123\&quot;. For GCP provided resources, number should be project number. |  [optional] |
|**resourceName** | **String** | Required. Database resource name associated with the signal. Resource name to follow CAIS resource_name format as noted here go/condor-common-datamodel |  [optional] |
|**signalClass** | [**SignalClassEnum**](#SignalClassEnum) | Required. The class of the signal, such as if it&#39;s a THREAT or VULNERABILITY. |  [optional] |
|**signalId** | **String** | Required. Unique identifier for the signal. This is an unique id which would be mainatined by partner to identify a signal. |  [optional] |
|**signalType** | [**SignalTypeEnum**](#SignalTypeEnum) | Required. Type of signal, for example, &#x60;AVAILABLE_IN_MULTIPLE_ZONES&#x60;, &#x60;LOGGING_MOST_ERRORS&#x60;, etc. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| PROVIDER_UNSPECIFIED | &quot;PROVIDER_UNSPECIFIED&quot; |
| GCP | &quot;GCP&quot; |
| AWS | &quot;AWS&quot; |
| AZURE | &quot;AZURE&quot; |
| ONPREM | &quot;ONPREM&quot; |
| SELFMANAGED | &quot;SELFMANAGED&quot; |
| PROVIDER_OTHER | &quot;PROVIDER_OTHER&quot; |



## Enum: SignalClassEnum

| Name | Value |
|---- | -----|
| CLASS_UNSPECIFIED | &quot;CLASS_UNSPECIFIED&quot; |
| THREAT | &quot;THREAT&quot; |
| VULNERABILITY | &quot;VULNERABILITY&quot; |
| MISCONFIGURATION | &quot;MISCONFIGURATION&quot; |
| OBSERVATION | &quot;OBSERVATION&quot; |
| ERROR | &quot;ERROR&quot; |



## Enum: SignalTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SIGNAL_TYPE_UNSPECIFIED&quot; |
| NOT_PROTECTED_BY_AUTOMATIC_FAILOVER | &quot;SIGNAL_TYPE_NOT_PROTECTED_BY_AUTOMATIC_FAILOVER&quot; |
| GROUP_NOT_REPLICATING_ACROSS_REGIONS | &quot;SIGNAL_TYPE_GROUP_NOT_REPLICATING_ACROSS_REGIONS&quot; |
| NOT_AVAILABLE_IN_MULTIPLE_ZONES | &quot;SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_ZONES&quot; |
| NOT_AVAILABLE_IN_MULTIPLE_REGIONS | &quot;SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_REGIONS&quot; |
| NO_PROMOTABLE_REPLICA | &quot;SIGNAL_TYPE_NO_PROMOTABLE_REPLICA&quot; |
| NO_AUTOMATED_BACKUP_POLICY | &quot;SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY&quot; |
| SHORT_BACKUP_RETENTION | &quot;SIGNAL_TYPE_SHORT_BACKUP_RETENTION&quot; |
| LAST_BACKUP_FAILED | &quot;SIGNAL_TYPE_LAST_BACKUP_FAILED&quot; |
| LAST_BACKUP_OLD | &quot;SIGNAL_TYPE_LAST_BACKUP_OLD&quot; |
| VIOLATES_CIS_GCP_FOUNDATION_2_0 | &quot;SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_2_0&quot; |
| VIOLATES_CIS_GCP_FOUNDATION_1_3 | &quot;SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_3&quot; |
| VIOLATES_CIS_GCP_FOUNDATION_1_2 | &quot;SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_2&quot; |
| VIOLATES_CIS_GCP_FOUNDATION_1_1 | &quot;SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_1&quot; |
| VIOLATES_CIS_GCP_FOUNDATION_1_0 | &quot;SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_0&quot; |
| VIOLATES_NIST_800_53 | &quot;SIGNAL_TYPE_VIOLATES_NIST_800_53&quot; |
| VIOLATES_ISO_27001 | &quot;SIGNAL_TYPE_VIOLATES_ISO_27001&quot; |
| VIOLATES_PCI_DSS_V3_2_1 | &quot;SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1&quot; |
| LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING | &quot;SIGNAL_TYPE_LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING&quot; |
| QUERY_DURATIONS_NOT_LOGGED | &quot;SIGNAL_TYPE_QUERY_DURATIONS_NOT_LOGGED&quot; |
| VERBOSE_ERROR_LOGGING | &quot;SIGNAL_TYPE_VERBOSE_ERROR_LOGGING&quot; |
| QUERY_LOCK_WAITS_NOT_LOGGED | &quot;SIGNAL_TYPE_QUERY_LOCK_WAITS_NOT_LOGGED&quot; |
| LOGGING_MOST_ERRORS | &quot;SIGNAL_TYPE_LOGGING_MOST_ERRORS&quot; |
| LOGGING_ONLY_CRITICAL_ERRORS | &quot;SIGNAL_TYPE_LOGGING_ONLY_CRITICAL_ERRORS&quot; |
| MINIMAL_ERROR_LOGGING | &quot;SIGNAL_TYPE_MINIMAL_ERROR_LOGGING&quot; |
| QUERY_STATISTICS_LOGGED | &quot;SIGNAL_TYPE_QUERY_STATISTICS_LOGGED&quot; |
| EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME | &quot;SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME&quot; |
| EXCESSIVE_LOGGING_OF_PARSER_STATISTICS | &quot;SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATISTICS&quot; |
| EXCESSIVE_LOGGING_OF_PLANNER_STATISTICS | &quot;SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATISTICS&quot; |
| NOT_LOGGING_ONLY_DDL_STATEMENTS | &quot;SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS&quot; |
| LOGGING_QUERY_STATISTICS | &quot;SIGNAL_TYPE_LOGGING_QUERY_STATISTICS&quot; |
| NOT_LOGGING_TEMPORARY_FILES | &quot;SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES&quot; |
| CONNECTION_MAX_NOT_CONFIGURED | &quot;SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED&quot; |
| USER_OPTIONS_CONFIGURED | &quot;SIGNAL_TYPE_USER_OPTIONS_CONFIGURED&quot; |
| EXPOSED_TO_PUBLIC_ACCESS | &quot;SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS&quot; |
| UNENCRYPTED_CONNECTIONS | &quot;SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS&quot; |
| NO_ROOT_PASSWORD | &quot;SIGNAL_TYPE_NO_ROOT_PASSWORD&quot; |
| WEAK_ROOT_PASSWORD | &quot;SIGNAL_TYPE_WEAK_ROOT_PASSWORD&quot; |
| ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED | &quot;SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED&quot; |
| SERVER_AUTHENTICATION_NOT_REQUIRED | &quot;SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED&quot; |
| EXPOSED_BY_OWNERSHIP_CHAINING | &quot;SIGNAL_TYPE_EXPOSED_BY_OWNERSHIP_CHAINING&quot; |
| EXPOSED_TO_EXTERNAL_SCRIPTS | &quot;SIGNAL_TYPE_EXPOSED_TO_EXTERNAL_SCRIPTS&quot; |
| EXPOSED_TO_LOCAL_DATA_LOADS | &quot;SIGNAL_TYPE_EXPOSED_TO_LOCAL_DATA_LOADS&quot; |
| CONNECTION_ATTEMPTS_NOT_LOGGED | &quot;SIGNAL_TYPE_CONNECTION_ATTEMPTS_NOT_LOGGED&quot; |
| DISCONNECTIONS_NOT_LOGGED | &quot;SIGNAL_TYPE_DISCONNECTIONS_NOT_LOGGED&quot; |
| LOGGING_EXCESSIVE_STATEMENT_INFO | &quot;SIGNAL_TYPE_LOGGING_EXCESSIVE_STATEMENT_INFO&quot; |
| EXPOSED_TO_REMOTE_ACCESS | &quot;SIGNAL_TYPE_EXPOSED_TO_REMOTE_ACCESS&quot; |
| DATABASE_NAMES_EXPOSED | &quot;SIGNAL_TYPE_DATABASE_NAMES_EXPOSED&quot; |
| SENSITIVE_TRACE_INFO_NOT_MASKED | &quot;SIGNAL_TYPE_SENSITIVE_TRACE_INFO_NOT_MASKED&quot; |
| PUBLIC_IP_ENABLED | &quot;SIGNAL_TYPE_PUBLIC_IP_ENABLED&quot; |
| IDLE | &quot;SIGNAL_TYPE_IDLE&quot; |
| OVERPROVISIONED | &quot;SIGNAL_TYPE_OVERPROVISIONED&quot; |
| HIGH_NUMBER_OF_OPEN_TABLES | &quot;SIGNAL_TYPE_HIGH_NUMBER_OF_OPEN_TABLES&quot; |
| HIGH_NUMBER_OF_TABLES | &quot;SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES&quot; |
| HIGH_TRANSACTION_ID_UTILIZATION | &quot;SIGNAL_TYPE_HIGH_TRANSACTION_ID_UTILIZATION&quot; |
| UNDERPROVISIONED | &quot;SIGNAL_TYPE_UNDERPROVISIONED&quot; |
| OUT_OF_DISK | &quot;SIGNAL_TYPE_OUT_OF_DISK&quot; |
| SERVER_CERTIFICATE_NEAR_EXPIRY | &quot;SIGNAL_TYPE_SERVER_CERTIFICATE_NEAR_EXPIRY&quot; |
| DATABASE_AUDITING_DISABLED | &quot;SIGNAL_TYPE_DATABASE_AUDITING_DISABLED&quot; |
| RESTRICT_AUTHORIZED_NETWORKS | &quot;SIGNAL_TYPE_RESTRICT_AUTHORIZED_NETWORKS&quot; |
| VIOLATE_POLICY_RESTRICT_PUBLIC_IP | &quot;SIGNAL_TYPE_VIOLATE_POLICY_RESTRICT_PUBLIC_IP&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| RESOLVED | &quot;RESOLVED&quot; |
| MUTED | &quot;MUTED&quot; |



