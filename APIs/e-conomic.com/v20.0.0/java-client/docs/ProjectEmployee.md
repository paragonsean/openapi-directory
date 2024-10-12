

# ProjectEmployee


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Employee&#39;s home address.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**canApprove** | **Boolean** | Shows if the employee can approve for example time entries.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: not filterable&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**canInvoice** | **Boolean** | Shows if the employee can take for example a time entry to the invoice process.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**city** | **String** | Employee&#39;s city of residence.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**costPriceAfter** | **Double** | The cost after the cut off date.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: true&lt;/p&gt; |  [optional] |
|**costPriceBefore** | **Double** | The cost before the cut off date.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: true&lt;/p&gt; |  [optional] |
|**cutOffDate** | **LocalDate** | By default, salesPriceBefore is used, unless a cutoffDate and salesPriceAfter is determined. The cutoffDate serves the purpose of choosing which date the salesPriceAfter shall apply from. It can be null if only salesPriceBefore should apply.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: true&lt;/p&gt; |  [optional] |
|**employeeType** | **EmployeeType** | Employee types:  - 0: No user in e-conomic  - 1: Time Logger  - 2: Project Manager  - 3: Mobile Time Logger&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**groupNumber** | **Integer** | The number of the employee group that this employee belongs.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**isBarred** | **Boolean** | Shows if the employee can be registered on or is barred.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**isUser** | **Boolean** | Shows if the employee is also a user.&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**name** | **String** | Name of the employee.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin, like&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**number** | **Integer** | The unique number of the project employee.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: true&lt;/p&gt; |  |
|**objectVersion** | **String** | The object version, required for PUT requests.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: not filterable&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**salesPriceAfter** | **Double** | The sale price after the cut off date.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: true&lt;/p&gt; |  [optional] |
|**salesPriceBefore** | **Double** | The sale price before the cut off date.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: true&lt;/p&gt; |  [optional] |
|**userId** | **String** | User id of the employee if it&#39;s a user.&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**zipCode** | **String** | Employee&#39;s zip code.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |



