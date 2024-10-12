

# InstancePoolProperties

Properties of an instance pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | The license type. Possible values are &#39;LicenseIncluded&#39; (price for SQL license is included) and &#39;BasePrice&#39; (without SQL license price). |  |
|**subnetId** | **String** | Resource ID of the subnet to place this instance pool in. |  |
|**vCores** | **Integer** | Count of vCores belonging to this instance pool. |  |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| LICENSE_INCLUDED | &quot;LicenseIncluded&quot; |
| BASE_PRICE | &quot;BasePrice&quot; |



