# FrankieFinancialApi.InternationalBusinessProfileCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**companyCode** | **String** | This is the company number returned in the search results  (InternationalBusinessSearchResponse.Companies.CompanyDTO[n].Code)  | [optional] 
**country** | **String** | The ISO 3166-1 alpha2 country code of country registry you wish to search. This is consistent for all countries except for:    - The United States which requires the state registry to query as well.     - As an example, for a Delaware query, the country code would be \&quot;US-DE\&quot;.     - A Texas query would use \&quot;US-TX\&quot;   - Canada, which also requires you to supply a territory code too.     - A Yukon query would use CA-YU, Manitoba would use CA-MB     - You can do an all jurisdiction search with CA-ALL   - United Arab Emirates (UAE)     - For Abu Dhabi, use \&quot;DI\&quot;      - For Dubai, use \&quot;DU\&quot;    See details here:     https://apidocs.frankiefinancial.com/docs/country-codes-for-international-business-queries  | 


