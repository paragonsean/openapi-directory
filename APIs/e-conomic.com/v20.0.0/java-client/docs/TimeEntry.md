

# TimeEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityNumber** | **Integer** | The activity identifier of time entry.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**date** | **OffsetDateTime** | The date of time entry.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**employeeNumber** | **Integer** | The employee identifier of time entry.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**isApproved** | **Boolean** | Bool value specifying if the time entry was approved. If time entry was approved, it can not be updated anymore.&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**isReconciled** | **Boolean** | Bool value specifying if the time entry was reconciled.&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** | The time entry last updated date.&lt;p class&#x3D;&#39;filter&#39;&gt;Read-only: true&lt;/p&gt;&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] [readonly] |
|**number** | **Integer** | The time entry identifier.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: true&lt;/p&gt; |  [optional] |
|**numberOfHours** | **Double** | Number of hours of time entry.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**objectVersion** | **String** | The object version, required for PUT requests.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: not filterable&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |
|**projectNumber** | **Integer** | The project identifier of time entry.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  |
|**text** | **String** | Text description of time entry.&lt;p class&#x3D;&#39;filter&#39;&gt;Filterable: eq, ne, lt, lte, gt, gte, in, nin, like&lt;/p&gt;&lt;p class&#x3D;&#39;sort&#39;&gt;Sortable: false&lt;/p&gt; |  [optional] |



