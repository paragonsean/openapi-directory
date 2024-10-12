

# DatabaseResourceRecommendationSignalData

Common model for database resource recommendation signal data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalMetadata** | **Map&lt;String, Object&gt;** | Optional. Any other additional metadata specific to recommendation |  [optional] |
|**lastRefreshTime** | **String** | Required. last time recommendationw as refreshed |  [optional] |
|**recommendationState** | [**RecommendationStateEnum**](#RecommendationStateEnum) | Required. Recommendation state |  [optional] |
|**recommender** | **String** | Required. Name of recommendation. Examples: organizations/1234/locations/us-central1/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations/9876 |  [optional] |
|**recommenderId** | **String** | Required. ID of recommender. Examples: \&quot;google.cloudsql.instance.PerformanceRecommender\&quot; |  [optional] |
|**recommenderSubtype** | **String** | Required. Contains an identifier for a subtype of recommendations produced for the same recommender. Subtype is a function of content and impact, meaning a new subtype might be added when significant changes to &#x60;content&#x60; or &#x60;primary_impact.category&#x60; are introduced. See the Recommenders section to see a list of subtypes for a given Recommender. Examples: For recommender &#x3D; \&quot;google.cloudsql.instance.PerformanceRecommender\&quot;, recommender_subtype can be \&quot;MYSQL_HIGH_NUMBER_OF_OPEN_TABLES_BEST_PRACTICE\&quot;/\&quot;POSTGRES_HIGH_TRANSACTION_ID_UTILIZATION_BEST_PRACTICE\&quot; |  [optional] |
|**resourceName** | **String** | Required. Database resource name associated with the signal. Resource name to follow CAIS resource_name format as noted here go/condor-common-datamodel |  [optional] |
|**signalType** | [**SignalTypeEnum**](#SignalTypeEnum) | Required. Type of signal, for example, &#x60;SIGNAL_TYPE_IDLE&#x60;, &#x60;SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES&#x60;, etc. |  [optional] |



## Enum: RecommendationStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CLAIMED | &quot;CLAIMED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| DISMISSED | &quot;DISMISSED&quot; |



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



