

# Assembly

A description of groups of sites that are statistically correlated.  - **Examples** (for each entry of the assemblies list):     - `{\"sites_in_groups\": [[0], [1]], \"group_probabilities: [0.3, 0.7]}`: the first site and the second site never occur at the same time in the unit cell.       Statistically, 30 % of the times the first site is present, while 70 % of the times the second site is present.     - `{\"sites_in_groups\": [[1,2], [3]], \"group_probabilities: [0.3, 0.7]}`: the second and third site are either present together or not present; they form the first group of atoms for this assembly.       The second group is formed by the fourth site. Sites of the first group (the second and the third) are never present at the same time as the fourth site.       30 % of times sites 1 and 2 are present (and site 3 is absent); 70 % of times site 3 is present (and sites 1 and 2 are absent).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupProbabilities** | **List&lt;BigDecimal&gt;** | Statistical probability of each group. It MUST have the same length as &#x60;sites_in_groups&#x60;. It SHOULD sum to one. See below for examples of how to specify the probability of the occurrence of a vacancy. The possible reasons for the values not to sum to one are the same as already specified above for the &#x60;concentration&#x60; of each &#x60;species&#x60;. |  |
|**sitesInGroups** | **List&lt;List&lt;Integer&gt;&gt;** | Index of the sites (0-based) that belong to each group for each assembly.  - **Examples**:     - &#x60;[[1], [2]]&#x60;: two groups, one with the second site, one with the third.     - &#x60;[[1,2], [3]]&#x60;: one group with the second and third site, one with the fourth. |  |



