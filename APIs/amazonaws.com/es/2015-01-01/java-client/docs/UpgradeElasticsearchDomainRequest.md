

# UpgradeElasticsearchDomainRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | **String** | The name of an Elasticsearch domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen). |  |
|**targetVersion** | **String** | The version of Elasticsearch that you intend to upgrade the domain to. |  |
|**performCheckOnly** | **Boolean** |  This flag, when set to True, indicates that an Upgrade Eligibility Check needs to be performed. This will not actually perform the Upgrade.  |  [optional] |



