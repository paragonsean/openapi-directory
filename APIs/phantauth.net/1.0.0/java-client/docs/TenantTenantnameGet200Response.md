

# TenantTenantnameGet200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atId** | **String** | The URL of the tenant&#39;s JSON representation. |  [optional] |
|**about** | **String** | A detailed description of the tenant. If it takes the value of an URL, the description is downloaded from the given URL, otherwise the value it takes is the description itself. Markdown formatting can be used in the description. |  [optional] |
|**attribution** | **String** | The attribution of the external data source or random user generator. Its value can have markdown formatting, that is, the external source can contain highlights and links. |  [optional] |
|**depot** | **String** | It defines the place of the CSV file containing the resource data in [RFC 6570 - URI temaplate](https://tools.ietf.org/html/rfc6570) format. The URI template receives the type of the object to be generated (user, team) in the &#x60;kind&#x60; parameter.  The first line of the CSV file contains the resource property names, the following lines, on the other hand, contain the relevant data. In the case of nested properties, a &#39;.&#39; character separates the elements of the property name (e.g. address.formatted). |  [optional] |
|**depots** | **List&lt;Object&gt;** | A list of resource types supported by the external CSV set in &#x60;depot&#x60;. |  [optional] |
|**domain** | **Boolean** | True in the case of a domain tenant collecting several tenants, otherwise false. |  [optional] |
|**factories** | **List&lt;Object&gt;** | A list of resource types supported by the external generator set in &#x60;factory&#x60;. |  [optional] |
|**factory** | **String** | The address of the custom random resource generator (user, team) in [RFC 6570 - URI temaplate](https://tools.ietf.org/html/rfc6570) format. The URI template receives the type of the object to be generated (user, team) in the &#x60;kind&#x60; parameter, and the identifier of the object to be generated in the &#x60;name&#x60; parameter. |  [optional] |
|**favicon** | **String** | The URL of the tenant favicon. The image from this address appears as a shortcut icon in the browser when a user visits the tenant&#39;s webpages. |  [optional] |
|**issuer** | **String** | The URL of the tenant OpenID Connect issuer. This value allows you to get, for example, the [OpenID Provider Metadata](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata). As a webpage, it contains information on the use if the given tenant. |  |
|**logo** | **String** | The URL of the tenant logo. The image from this address appears in the address bar of the tenant&#39;s webpages and the pages that contain the list of available tenants. |  [optional] |
|**name** | **String** | The displayed tenant name. In lack of such name, the DNS name of the tenant is displayed in the address bar of the tenant&#39;s webpages. |  [optional] |
|**script** | **String** | The URL of a custom JavaScript file can be automatically inserted in the login.html, consent.html, és test.html pages. |  [optional] |
|**sheet** | **String** | It is used to give the identifyer of a public Google Sheet document. The first line of the table contains the user property names, the following lines, on the other hand, contain the relevant data. In the case of nested properties, a &#39;.&#39; character separates the elements of the property name (e.g. address.formatted). |  [optional] |
|**sub** | **String** | The fully qualified DNS domain name of the tenant. In the case of official and shared tenants (phantauth.net and phantauth.cf DNS domain), the DNS domain can be omitted (e.g. *default* or *faker*). |  |
|**subtenant** | **Boolean** | True in the case of a tenant referred to in a domain tenant, otherwise false. |  [optional] |
|**summary** | **String** | A one-line description, the watchword of the tenant. It appears on the tenant&#39;s startup page and the pages that contain the list of available tenants. It takes the valua of an unformatted text. |  [optional] |
|**template** | **String** | It defines the place of the templates of the HTML pages of the tenant in [RFC 6570 - URI temaplate](https://tools.ietf.org/html/rfc6570) format. The URI template receives the page name in a &#x60;resource&#x60; parameter. By default, it takes the following value: &#x60;https://default.phantauth.net{/resource}&#x60;. |  [optional] |
|**theme** | **String** | The URL of the CSS style sheet used for the tenant&#39;s webpages. The default webpage templates were created by the use of the Bootstrap library, therefore, the Bootstrap CSS URL has to be provided when such a webpage is used. |  [optional] |
|**userinfo** | **String** |  |  [optional] |
|**website** | **String** | The website address associated with the tenant. If a tenant doesn&#39;t have a website, its value is identical with that of the &#x60;issuer&#x60; property. |  [optional] |



