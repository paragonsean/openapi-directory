

# ScanRunWarningTrace

Output only. Defines a warning trace message for ScanRun. Warning traces provide customers with useful information that helps make the scanning process more effective.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Output only. Indicates the warning code. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| INSUFFICIENT_CRAWL_RESULTS | &quot;INSUFFICIENT_CRAWL_RESULTS&quot; |
| TOO_MANY_CRAWL_RESULTS | &quot;TOO_MANY_CRAWL_RESULTS&quot; |
| TOO_MANY_FUZZ_TASKS | &quot;TOO_MANY_FUZZ_TASKS&quot; |
| BLOCKED_BY_IAP | &quot;BLOCKED_BY_IAP&quot; |
| NO_STARTING_URL_FOUND_FOR_MANAGED_SCAN | &quot;NO_STARTING_URL_FOUND_FOR_MANAGED_SCAN&quot; |



