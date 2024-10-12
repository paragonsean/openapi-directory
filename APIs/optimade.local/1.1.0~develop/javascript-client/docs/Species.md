# OptimadeApi.Species

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attached** | **[String]** | If provided MUST be a list of length 1 or more of strings of chemical symbols for the elements attached to this site, or \&quot;X\&quot; for a non-chemical element. | [optional] 
**chemicalSymbols** | **[String]** | MUST be a list of strings of all chemical elements composing this species. Each item of the list MUST be one of the following:  - a valid chemical-element name, or - the special value &#x60;\&quot;X\&quot;&#x60; to represent a non-chemical element, or - the special value &#x60;\&quot;vacancy\&quot;&#x60; to represent that this site has a non-zero probability of having a vacancy (the respective probability is indicated in the &#x60;concentration&#x60; list, see below).  If any one entry in the &#x60;species&#x60; list has a &#x60;chemical_symbols&#x60; list that is longer than 1 element, the correct flag MUST be set in the list &#x60;structure_features&#x60;. | 
**concentration** | **[Number]** | MUST be a list of floats, with same length as &#x60;chemical_symbols&#x60;. The numbers represent the relative concentration of the corresponding chemical symbol in this species. The numbers SHOULD sum to one. Cases in which the numbers do not sum to one typically fall only in the following two categories:  - Numerical errors when representing float numbers in fixed precision, e.g. for two chemical symbols with concentrations &#x60;1/3&#x60; and &#x60;2/3&#x60;, the concentration might look something like &#x60;[0.33333333333, 0.66666666666]&#x60;. If the client is aware that the sum is not one because of numerical precision, it can renormalize the values so that the sum is exactly one. - Experimental errors in the data present in the database. In this case, it is the responsibility of the client to decide how to process the data.  Note that concentrations are uncorrelated between different site (even of the same species). | 
**mass** | **[Number]** | If present MUST be a list of floats expressed in a.m.u. Elements denoting vacancies MUST have masses equal to 0. | [optional] 
**name** | **String** | Gives the name of the species; the **name** value MUST be unique in the &#x60;species&#x60; list. | 
**nattached** | **[Number]** | If provided MUST be a list of length 1 or more of integers indicating the number of attached atoms of the kind specified in the value of the :field:&#x60;attached&#x60; key. | [optional] 
**originalName** | **String** | Can be any valid Unicode string, and SHOULD contain (if specified) the name of the species that is used internally in the source database.  Note: With regards to \&quot;source database\&quot;, we refer to the immediate source being queried via the OPTIMADE API implementation. | [optional] 


