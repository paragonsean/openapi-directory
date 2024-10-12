

# CloudAuditLoggingFeatureSpec

**Cloud Audit Logging**: Spec for Audit Logging Allowlisting.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowlistedServiceAccounts** | **List&lt;String&gt;** | Service account that should be allowlisted to send the audit logs; eg cloudauditlogging@gcp-project.iam.gserviceaccount.com. These accounts must already exist, but do not need to have any permissions granted to them. The customer&#39;s entitlements will be checked prior to allowlisting (i.e. the customer must be an Anthos customer.) |  [optional] |



