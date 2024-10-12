

# RegistrantInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Address of the registrant. |  [optional] |
|**city** | **String** | City of the registrant. |  [optional] |
|**companyName** | **String** | Company name of the registrant.&lt;br /&gt;  The registrant is a company if not empty, otherwise the registrant is an individual when validating extra fields. |  [optional] |
|**countryCode** | **String** | Country code of the registrant.  Syntax: &#39;BE&#39;, &#39;NL, &#39;FR&#39;, ... |  [optional] |
|**email** | **String** | Email of the registrant. |  [optional] |
|**enterpriseNumber** | **String** | Enterprise number of the registrant.&lt;br /&gt;  Syntax: &#39;BE0123456789&#39; |  [optional] |
|**extraFields** | [**List&lt;ExtraField&gt;**](ExtraField.md) | List of registrant extra fields for the domain name.  &lt;table&gt;&lt;tr&gt;&lt;th&gt;Extension&lt;/th&gt;&lt;th&gt;Registrant specifics&lt;/th&gt;&lt;th&gt;Required extra field(s)&lt;/th&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;.dk&lt;/td&gt;&lt;td&gt;is a company&lt;/td&gt;&lt;td&gt;CompanyNumber&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;.es&lt;/td&gt;&lt;td&gt;is a company&lt;/td&gt;&lt;td&gt;CompanyNumber&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;.es&lt;/td&gt;&lt;td&gt;is an individual&lt;/td&gt;&lt;td&gt;PassportNumber&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;.fr&lt;/td&gt;&lt;td&gt;is a company&lt;/td&gt;&lt;td&gt;CompanyNumber&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;.it&lt;/td&gt;&lt;td&gt;is an individual and has country code &#39;IT&#39;&lt;/td&gt;&lt;td&gt;CodiceFiscal&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;.it&lt;/td&gt;&lt;td&gt;is an individual and has not country code &#39;IT&#39;&lt;/td&gt;&lt;td&gt;PassportNumber&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;.nu&lt;/td&gt;&lt;td&gt;is a company&lt;/td&gt;&lt;td&gt;CompanyNumber&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;.nu&lt;/td&gt;&lt;td&gt;is an individual&lt;/td&gt;&lt;td&gt;PassportNumber&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;.se&lt;/td&gt;&lt;td&gt;is a company&lt;/td&gt;&lt;td&gt;CompanyNumber&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;.se&lt;/td&gt;&lt;td&gt;is an individual&lt;/td&gt;&lt;td&gt;PassportNumber&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt; |  [optional] |
|**fax** | **String** | Fax of the registrant.  Syntax: &#39;+32.123456789&#39; |  [optional] |
|**firstName** | **String** | First name of the registrant. |  [optional] |
|**languageCode** | **String** | Language code of the registrant.  Syntax: &#39;nl&#39;, &#39;fr&#39;, &#39;en&#39;, &#39;de&#39;, ... |  [optional] |
|**lastName** | **String** | Last name of the registrant. |  [optional] |
|**phone** | **String** | Phone of the registrant.&lt;br /&gt;  Syntax: &#39;+32.123456789&#39; |  [optional] |
|**postalCode** | **String** | Postal code of the registrant. |  [optional] |



