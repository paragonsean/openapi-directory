

# Product


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizedScopes** | **List&lt;String&gt;** | A list of scopes that the product can require from clients |  |
|**email** | **String** | The contact email for the product |  [optional] |
|**productUuid** | **String** | The product identifier |  |
|**redirectUri** | **String** | A redirect url registered as a callback for the Connect with Lumminary authorization flow |  [optional] |
|**snpsAuthorized** | **List&lt;String&gt;** | A superset of snps_min_required, containing all SNPs to which an Product has access (includes optional SNPs) |  |
|**snpsAuthorizedAny** | **Boolean** | A boolean value specifying if SNP set is not strict |  |
|**snpsMinRequired** | [**SnpsMinRequired**](SnpsMinRequired.md) |  |  |
|**snpsMinRequiredAny** | **Boolean** | A boolean value specifying if SNP set is not strict |  |



