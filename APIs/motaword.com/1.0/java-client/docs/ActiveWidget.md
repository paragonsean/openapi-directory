

# ActiveWidget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminMode** | **Boolean** | Is the Active Widget in admin mode? This changes a couple of behaviors in the widget to configure some rules like elements, sections, pages, etc. |  [optional] |
|**allowHashInUrl** | **Boolean** | When true, hash params are included in filenames. When false, params are ignored. |  [optional] |
|**allowQueryInUrl** | **Boolean** | When true, query params are included in filenames. When false, params are ignored. |  [optional] |
|**autoDetectSourceLanguage** | **Boolean** | When true, we will ignore the source language of your project and try to automatically detect the source language of the given content. This is especially useful in environments with unpredictable source contents, such as a chat environment. |  [optional] |
|**createdAt** | **OffsetDateTime** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z |  [optional] |
|**debugMode** | **Boolean** | When true, Active ecosystem will print debug-level logs from all Active modules. |  [optional] |
|**elements** | **String** | Continuous project exclusive elements and rules |  [optional] |
|**followUser** | **Boolean** | Specify whether we should follow the user around in your website and automatically translate pages. |  [optional] |
|**forceCacheRefreshInterval** | **Boolean** | Determines whether to force-refresh local browser cache of your translations in certain period of times, no matter if there is a new activity in the project. |  [optional] |
|**hitBackendForExisting** | **Boolean** | When true, Active ecosystem will collect all strings on TMS no matter if the translation is present in the cache. |  [optional] |
|**id** | **Long** |  |  [optional] |
|**languageMappings** | **String** | Continuous project language mappings |  [optional] |
|**live** | **Boolean** | Whether ActiveJS should be considered live in an embedded site. Use &#x60;false&#x60; if you are still testing Active. Go to your Active dashboard and follow links to your website to actually test Active. |  [optional] |
|**modifyLinks** | **Boolean** | We can automatically localize the same-domain URLs in your page. The way we localize the URL depends on urlMode configuration. We can either add/update the locale query parameter, or add/update the path of the URL. |  [optional] |
|**name** | **String** |  |  [optional] |
|**optimizePerPage** | **Boolean** | When true, Active ecosystem will optimize the script and data flows per page, rather than per project. This decreases the bandwidth usage per script, but makes translation publishing more complex and script serving per-page. |  [optional] |
|**pages** | **String** | Continuous project page rules |  [optional] |
|**pathRegex** | **String** | Custom regex for path-type URL mode. |  [optional] |
|**position** | **String** | Options are \&quot;bottom-left\&quot;, \&quot;bottom-right\&quot;, \&quot;in-place\&quot; |  [optional] |
|**queryName** | **String** | Query parameter name to be used with query-type URL mode. Default is &#39;locale&#39;. |  [optional] |
|**rebootOnUrlChange** | **Boolean** | When true, Active ecosystem reboots itself when url changes. |  [optional] |
|**restrictedDomains** | **String** | JSON string for a list of domains that this widget&#39;s API interactions are limited to. |  [optional] |
|**sections** | **String** | Continuous project section rules |  [optional] |
|**testMode** | **Boolean** | Is the Active Widget in test mode? This changes a couple behaviors in the widget to make it easier for you to test and develop your Active integration. |  [optional] |
|**theme** | **String** | \\\&quot;light\\\&quot;, \\\&quot;dark\\\&quot; OR custom JSON. |  [optional] |
|**token** | **String** | Token that you should use when you are using this widget on your website. |  [optional] |
|**urlChangeMode** | **String** | When a user changes locale (or when we automatically detect and change it for them), we will change the URL of the page they are in. We can do this by actually redirecting the user to the new page, or by simply changing the URL in the address bar via browser&#39;s History API. When NULL, we won&#39;t apply any URL changes. |  [optional] |
|**urlMode** | **String** | When a user changes locale (or when we automatically detect and change it for them), we will change the URL of the page they are in. We can either change the path of the URL to prefix it with the locale code, or we can add a query parameter to the URL. We also use this mode to detect the locale for the current page when a user directly loads a page. When NULL, locale detection from URL will be disabled (even then, if the user has selected a locale manually, and followUser is enabled, we will still automatically translate the page in user&#39;s locale. |  [optional] |
|**useCache** | **Boolean** | Should we make use of local browser cache for your visitors? We will refresh the cache when Active JS detects new activity in your project. |  [optional] |
|**useDummyTranslations** | **Boolean** | When enabled, we will translate your website with dummy content, rather than actually using MT/TM. |  [optional] |
|**variables** | **String** | Continuous project variable definitions |  [optional] |



