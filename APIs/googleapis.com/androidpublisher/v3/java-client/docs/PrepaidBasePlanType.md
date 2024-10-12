

# PrepaidBasePlanType

Represents a base plan that does not automatically renew at the end of the base plan, and must be manually renewed by the user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingPeriodDuration** | **String** | Required. Subscription period, specified in ISO 8601 format. For a list of acceptable billing periods, refer to the help center. |  [optional] |
|**timeExtension** | [**TimeExtensionEnum**](#TimeExtensionEnum) | Whether users should be able to extend this prepaid base plan in Google Play surfaces. Defaults to TIME_EXTENSION_ACTIVE if not specified. |  [optional] |



## Enum: TimeExtensionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TIME_EXTENSION_UNSPECIFIED&quot; |
| ACTIVE | &quot;TIME_EXTENSION_ACTIVE&quot; |
| INACTIVE | &quot;TIME_EXTENSION_INACTIVE&quot; |



