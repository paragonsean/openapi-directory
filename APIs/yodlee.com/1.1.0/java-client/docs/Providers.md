

# Providers


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**PRIORITY** | [**PRIORITYEnum**](#PRIORITYEnum) | Indicates the priority for which the service is invoked.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**accountType** | [**List&lt;AccountTypeEnum&gt;**](#List&lt;AccountTypeEnum&gt;) | AccountType supported by the provider, eg: Brokerage Cash, Current&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**associatedProviderIds** | **List&lt;Long&gt;** | The screen-scraping providers that are associated to the Open Banking provider ID.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: All Containers&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**authParameter** | [**List&lt;AuthParameterEnum&gt;**](#List&lt;AuthParameterEnum&gt;) | AuthParameter appears in the response only in case of token-based aggregation sites.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**authType** | [**AuthTypeEnum**](#AuthTypeEnum) | The authentication type enabled at the provider site. &lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**baseUrl** | **String** | The base URL of the provider&#39;s site.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**capability** | [**List&lt;Capability&gt;**](Capability.md) | Capability of the site&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt;&lt;br&gt;&lt;b&gt;Note : &lt;/b&gt; capability has been deprecated |  [optional] [readonly] |
|**countryISOCode** | **String** | Country to which the provider belongs.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**dataset** | [**List&lt;ProvidersDataset&gt;**](ProvidersDataset.md) | Logical grouping of dataset attributes into datasets such as Basic Aggregation Data, Account Profile and Documents&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**favicon** | **String** | Favicon link of the provider.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**forgetPasswordUrl** | **String** | The forget password URL of the provider site.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**help** | **String** | Text to guide user through linking an account that belongs to the site&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**id** | **Long** | Unique identifier for the provider site(e.g., financial institution sites, biller sites, lender sites, etc.).&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**isAddedByUser** | **String** | Indicates that the site has been added by the user at least once.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**isAutoRefreshEnabled** | **Boolean** | Indicates if a provider site is auto-refreshed.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**isConsentRequired** | **Boolean** | Indicates if a provider site requires consent.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**languageISOCode** | **String** | The language in which the provider details are provided. For example, a site supports two languages English and French. English being the primary language, the provider response will be provided in French depending on the user&#39;s locale. The language follows the two letter ISO code.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**lastModified** | **String** | Determines when the provider information was updated by Yodlee. If the customer caches the data, the cache is recommended to be refreshed based on this field.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**loginHelp** | **String** | Help text to guide the user to choose the correct provider site.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**loginUrl** | **String** | The login URL of the provider&#39;s site.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**logo** | **String** | The logo link of the provider institution. The link will return the logo in the PNG format.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**name** | **String** | The name of a provider site.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**primaryLanguageISOCode** | **String** | The primary language of the site.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Determines if the provider is supported for the cobrand (customer), is in the beta stage, etc. &lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET providers/{providerId}&lt;/li&gt;&lt;li&gt;GET providers&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |



## Enum: PRIORITYEnum

| Name | Value |
|---- | -----|
| POPULAR | &quot;POPULAR&quot; |
| SUGGESTED | &quot;SUGGESTED&quot; |
| COBRAND | &quot;COBRAND&quot; |
| SEARCH | &quot;SEARCH&quot; |
| ALL | &quot;ALL&quot; |



## Enum: List&lt;AccountTypeEnum&gt;

| Name | Value |
|---- | -----|
| CURRENT | &quot;CURRENT&quot; |
| BROKERAGE_CASH | &quot;BROKERAGE_CASH&quot; |



## Enum: List&lt;AuthParameterEnum&gt;

| Name | Value |
|---- | -----|
| AUTHORIZATION_CODE | &quot;authorizationCode&quot; |
| ID_TOKEN | &quot;idToken&quot; |
| AUTH_RESPONSE | &quot;authResponse&quot; |



## Enum: AuthTypeEnum

| Name | Value |
|---- | -----|
| OAUTH | &quot;OAUTH&quot; |
| CREDENTIALS | &quot;CREDENTIALS&quot; |
| MFA_CREDENTIALS | &quot;MFA_CREDENTIALS&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUPPORTED | &quot;Supported&quot; |
| BETA | &quot;Beta&quot; |
| UNSUPPORTED | &quot;Unsupported&quot; |



