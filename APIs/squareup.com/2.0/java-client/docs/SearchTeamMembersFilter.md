

# SearchTeamMembersFilter

Represents a filter used in a search for `TeamMember` objects. `AND` logic is applied between the individual fields, and `OR` logic is applied within list-based fields. For example, setting this filter value: ``` filter = (locations_ids = [\"A\", \"B\"], status = ACTIVE) ``` returns only active team members assigned to either location \"A\" or \"B\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locationIds** | **List&lt;String&gt;** | When present, filters by team members assigned to the specified locations. When empty, includes team members assigned to any location. |  [optional] |
|**status** | **String** | When present, filters by team members who match the given status. When empty, includes team members of all statuses. |  [optional] |



