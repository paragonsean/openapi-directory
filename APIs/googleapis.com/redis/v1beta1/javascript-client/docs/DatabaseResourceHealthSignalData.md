# GoogleCloudMemorystoreForRedisApi.DatabaseResourceHealthSignalData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalMetadata** | **{String: Object}** | Any other additional metadata | [optional] 
**compliance** | [**[Compliance]**](Compliance.md) | Industry standards associated with this signal; if this signal is an issue, that could be a violation of the associated industry standard(s). For example, AUTO_BACKUP_DISABLED signal is associated with CIS GCP 1.1, CIS GCP 1.2, CIS GCP 1.3, NIST 800-53 and ISO-27001 compliance standards. If a database resource does not have automated backup enable, it will violate these following industry standards. | [optional] 
**description** | **String** | Description associated with signal | [optional] 
**eventTime** | **String** | Required. The last time at which the event described by this signal took place | [optional] 
**externalUri** | **String** | The external-uri of the signal, using which more information about this signal can be obtained. In GCP, this will take user to SCC page to get more details about signals. | [optional] 
**name** | **String** | Required. The name of the signal, ex: PUBLIC_SQL_INSTANCE, SQL_LOG_ERROR_VERBOSITY etc. | [optional] 
**provider** | **String** | Cloud provider name. Ex: GCP/AWS/Azure/OnPrem/SelfManaged | [optional] 
**resourceContainer** | **String** | Closest parent container of this resource. In GCP, &#39;container&#39; refers to a Cloud Resource Manager project. It must be resource name of a Cloud Resource Manager project with the format of \&quot;provider//\&quot;, such as \&quot;projects/123\&quot;. For GCP provided resources, number should be project number. | [optional] 
**resourceName** | **String** | Required. Database resource name associated with the signal. Resource name to follow CAIS resource_name format as noted here go/condor-common-datamodel | [optional] 
**signalClass** | **String** | Required. The class of the signal, such as if it&#39;s a THREAT or VULNERABILITY. | [optional] 
**signalId** | **String** | Required. Unique identifier for the signal. This is an unique id which would be mainatined by partner to identify a signal. | [optional] 
**signalType** | **String** | Required. Type of signal, for example, &#x60;AVAILABLE_IN_MULTIPLE_ZONES&#x60;, &#x60;LOGGING_MOST_ERRORS&#x60;, etc. | [optional] 
**state** | **String** |  | [optional] 



## Enum: ProviderEnum


* `PROVIDER_UNSPECIFIED` (value: `"PROVIDER_UNSPECIFIED"`)

* `GCP` (value: `"GCP"`)

* `AWS` (value: `"AWS"`)

* `AZURE` (value: `"AZURE"`)

* `ONPREM` (value: `"ONPREM"`)

* `SELFMANAGED` (value: `"SELFMANAGED"`)

* `PROVIDER_OTHER` (value: `"PROVIDER_OTHER"`)





## Enum: SignalClassEnum


* `CLASS_UNSPECIFIED` (value: `"CLASS_UNSPECIFIED"`)

* `THREAT` (value: `"THREAT"`)

* `VULNERABILITY` (value: `"VULNERABILITY"`)

* `MISCONFIGURATION` (value: `"MISCONFIGURATION"`)

* `OBSERVATION` (value: `"OBSERVATION"`)

* `ERROR` (value: `"ERROR"`)





## Enum: SignalTypeEnum


* `UNSPECIFIED` (value: `"SIGNAL_TYPE_UNSPECIFIED"`)

* `NOT_PROTECTED_BY_AUTOMATIC_FAILOVER` (value: `"SIGNAL_TYPE_NOT_PROTECTED_BY_AUTOMATIC_FAILOVER"`)

* `GROUP_NOT_REPLICATING_ACROSS_REGIONS` (value: `"SIGNAL_TYPE_GROUP_NOT_REPLICATING_ACROSS_REGIONS"`)

* `NOT_AVAILABLE_IN_MULTIPLE_ZONES` (value: `"SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_ZONES"`)

* `NOT_AVAILABLE_IN_MULTIPLE_REGIONS` (value: `"SIGNAL_TYPE_NOT_AVAILABLE_IN_MULTIPLE_REGIONS"`)

* `NO_PROMOTABLE_REPLICA` (value: `"SIGNAL_TYPE_NO_PROMOTABLE_REPLICA"`)

* `NO_AUTOMATED_BACKUP_POLICY` (value: `"SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY"`)

* `SHORT_BACKUP_RETENTION` (value: `"SIGNAL_TYPE_SHORT_BACKUP_RETENTION"`)

* `LAST_BACKUP_FAILED` (value: `"SIGNAL_TYPE_LAST_BACKUP_FAILED"`)

* `LAST_BACKUP_OLD` (value: `"SIGNAL_TYPE_LAST_BACKUP_OLD"`)

* `VIOLATES_CIS_GCP_FOUNDATION_2_0` (value: `"SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_2_0"`)

* `VIOLATES_CIS_GCP_FOUNDATION_1_3` (value: `"SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_3"`)

* `VIOLATES_CIS_GCP_FOUNDATION_1_2` (value: `"SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_2"`)

* `VIOLATES_CIS_GCP_FOUNDATION_1_1` (value: `"SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_1"`)

* `VIOLATES_CIS_GCP_FOUNDATION_1_0` (value: `"SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_0"`)

* `VIOLATES_NIST_800_53` (value: `"SIGNAL_TYPE_VIOLATES_NIST_800_53"`)

* `VIOLATES_ISO_27001` (value: `"SIGNAL_TYPE_VIOLATES_ISO_27001"`)

* `VIOLATES_PCI_DSS_V3_2_1` (value: `"SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1"`)

* `LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING` (value: `"SIGNAL_TYPE_LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING"`)

* `QUERY_DURATIONS_NOT_LOGGED` (value: `"SIGNAL_TYPE_QUERY_DURATIONS_NOT_LOGGED"`)

* `VERBOSE_ERROR_LOGGING` (value: `"SIGNAL_TYPE_VERBOSE_ERROR_LOGGING"`)

* `QUERY_LOCK_WAITS_NOT_LOGGED` (value: `"SIGNAL_TYPE_QUERY_LOCK_WAITS_NOT_LOGGED"`)

* `LOGGING_MOST_ERRORS` (value: `"SIGNAL_TYPE_LOGGING_MOST_ERRORS"`)

* `LOGGING_ONLY_CRITICAL_ERRORS` (value: `"SIGNAL_TYPE_LOGGING_ONLY_CRITICAL_ERRORS"`)

* `MINIMAL_ERROR_LOGGING` (value: `"SIGNAL_TYPE_MINIMAL_ERROR_LOGGING"`)

* `QUERY_STATISTICS_LOGGED` (value: `"SIGNAL_TYPE_QUERY_STATISTICS_LOGGED"`)

* `EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME` (value: `"SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME"`)

* `EXCESSIVE_LOGGING_OF_PARSER_STATISTICS` (value: `"SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATISTICS"`)

* `EXCESSIVE_LOGGING_OF_PLANNER_STATISTICS` (value: `"SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATISTICS"`)

* `NOT_LOGGING_ONLY_DDL_STATEMENTS` (value: `"SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS"`)

* `LOGGING_QUERY_STATISTICS` (value: `"SIGNAL_TYPE_LOGGING_QUERY_STATISTICS"`)

* `NOT_LOGGING_TEMPORARY_FILES` (value: `"SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES"`)

* `CONNECTION_MAX_NOT_CONFIGURED` (value: `"SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED"`)

* `USER_OPTIONS_CONFIGURED` (value: `"SIGNAL_TYPE_USER_OPTIONS_CONFIGURED"`)

* `EXPOSED_TO_PUBLIC_ACCESS` (value: `"SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS"`)

* `UNENCRYPTED_CONNECTIONS` (value: `"SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS"`)

* `NO_ROOT_PASSWORD` (value: `"SIGNAL_TYPE_NO_ROOT_PASSWORD"`)

* `WEAK_ROOT_PASSWORD` (value: `"SIGNAL_TYPE_WEAK_ROOT_PASSWORD"`)

* `ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED` (value: `"SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED"`)

* `SERVER_AUTHENTICATION_NOT_REQUIRED` (value: `"SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED"`)

* `EXPOSED_BY_OWNERSHIP_CHAINING` (value: `"SIGNAL_TYPE_EXPOSED_BY_OWNERSHIP_CHAINING"`)

* `EXPOSED_TO_EXTERNAL_SCRIPTS` (value: `"SIGNAL_TYPE_EXPOSED_TO_EXTERNAL_SCRIPTS"`)

* `EXPOSED_TO_LOCAL_DATA_LOADS` (value: `"SIGNAL_TYPE_EXPOSED_TO_LOCAL_DATA_LOADS"`)

* `CONNECTION_ATTEMPTS_NOT_LOGGED` (value: `"SIGNAL_TYPE_CONNECTION_ATTEMPTS_NOT_LOGGED"`)

* `DISCONNECTIONS_NOT_LOGGED` (value: `"SIGNAL_TYPE_DISCONNECTIONS_NOT_LOGGED"`)

* `LOGGING_EXCESSIVE_STATEMENT_INFO` (value: `"SIGNAL_TYPE_LOGGING_EXCESSIVE_STATEMENT_INFO"`)

* `EXPOSED_TO_REMOTE_ACCESS` (value: `"SIGNAL_TYPE_EXPOSED_TO_REMOTE_ACCESS"`)

* `DATABASE_NAMES_EXPOSED` (value: `"SIGNAL_TYPE_DATABASE_NAMES_EXPOSED"`)

* `SENSITIVE_TRACE_INFO_NOT_MASKED` (value: `"SIGNAL_TYPE_SENSITIVE_TRACE_INFO_NOT_MASKED"`)

* `PUBLIC_IP_ENABLED` (value: `"SIGNAL_TYPE_PUBLIC_IP_ENABLED"`)

* `IDLE` (value: `"SIGNAL_TYPE_IDLE"`)

* `OVERPROVISIONED` (value: `"SIGNAL_TYPE_OVERPROVISIONED"`)

* `HIGH_NUMBER_OF_OPEN_TABLES` (value: `"SIGNAL_TYPE_HIGH_NUMBER_OF_OPEN_TABLES"`)

* `HIGH_NUMBER_OF_TABLES` (value: `"SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES"`)

* `HIGH_TRANSACTION_ID_UTILIZATION` (value: `"SIGNAL_TYPE_HIGH_TRANSACTION_ID_UTILIZATION"`)

* `UNDERPROVISIONED` (value: `"SIGNAL_TYPE_UNDERPROVISIONED"`)

* `OUT_OF_DISK` (value: `"SIGNAL_TYPE_OUT_OF_DISK"`)

* `SERVER_CERTIFICATE_NEAR_EXPIRY` (value: `"SIGNAL_TYPE_SERVER_CERTIFICATE_NEAR_EXPIRY"`)

* `DATABASE_AUDITING_DISABLED` (value: `"SIGNAL_TYPE_DATABASE_AUDITING_DISABLED"`)

* `RESTRICT_AUTHORIZED_NETWORKS` (value: `"SIGNAL_TYPE_RESTRICT_AUTHORIZED_NETWORKS"`)

* `VIOLATE_POLICY_RESTRICT_PUBLIC_IP` (value: `"SIGNAL_TYPE_VIOLATE_POLICY_RESTRICT_PUBLIC_IP"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `RESOLVED` (value: `"RESOLVED"`)

* `MUTED` (value: `"MUTED"`)




