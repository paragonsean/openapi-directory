# OptimadeApi.Assembly

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupProbabilities** | **[Number]** | Statistical probability of each group. It MUST have the same length as &#x60;sites_in_groups&#x60;. It SHOULD sum to one. See below for examples of how to specify the probability of the occurrence of a vacancy. The possible reasons for the values not to sum to one are the same as already specified above for the &#x60;concentration&#x60; of each &#x60;species&#x60;. | 
**sitesInGroups** | **[[Number]]** | Index of the sites (0-based) that belong to each group for each assembly.  - **Examples**:     - &#x60;[[1], [2]]&#x60;: two groups, one with the second site, one with the third.     - &#x60;[[1,2], [3]]&#x60;: one group with the second and third site, one with the fourth. | 


