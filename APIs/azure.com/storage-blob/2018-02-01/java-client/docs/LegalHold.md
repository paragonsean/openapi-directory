

# LegalHold

The LegalHold property of a blob container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hasLegalHold** | **Boolean** | The hasLegalHold public property is set to true by SRP if there are at least one existing tag. The hasLegalHold public property is set to false by SRP if all existing legal hold tags are cleared out. There can be a maximum of 1000 blob containers with hasLegalHold&#x3D;true for a given account. |  [optional] [readonly] |
|**tags** | **List&lt;String&gt;** | Each tag should be 3 to 23 alphanumeric characters and is normalized to lower case at SRP. |  |



