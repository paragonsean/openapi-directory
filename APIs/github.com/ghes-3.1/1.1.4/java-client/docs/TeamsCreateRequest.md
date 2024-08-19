

# TeamsCreateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the team. |  [optional] |
|**ldapDn** | **String** | The [distinguished name](https://www.ldap.com/ldap-dns-and-rdns) (DN) of the LDAP entry to map to a team. LDAP synchronization must be enabled to map LDAP entries to a team. Use the \&quot;[Update LDAP mapping for a team](https://docs.github.com/enterprise-server@3.1/rest/reference/enterprise-admin#update-ldap-mapping-for-a-team)\&quot; endpoint to change the LDAP DN. For more information, see \&quot;[Using LDAP](https://docs.github.com/enterprise-server@3.1/admin/identity-and-access-management/authenticating-users-for-your-github-enterprise-server-instance/using-ldap#enabling-ldap-sync).\&quot; |  [optional] |
|**maintainers** | **List&lt;String&gt;** | List GitHub IDs for organization members who will become team maintainers. |  [optional] |
|**name** | **String** | The name of the team. |  |
|**parentTeamId** | **Integer** | The ID of a team to set as the parent team. |  [optional] |
|**permission** | [**PermissionEnum**](#PermissionEnum) | **Deprecated**. The permission that new repositories will be added to the team with when none is specified. |  [optional] |
|**privacy** | [**PrivacyEnum**](#PrivacyEnum) | The level of privacy this team should have. The options are:   **For a non-nested team:**   \\* &#x60;secret&#x60; - only visible to organization owners and members of this team.   \\* &#x60;closed&#x60; - visible to all members of this organization.   Default: &#x60;secret&#x60;   **For a parent or child team:**   \\* &#x60;closed&#x60; - visible to all members of this organization.   Default for child team: &#x60;closed&#x60; |  [optional] |
|**repoNames** | **List&lt;String&gt;** | The full name (e.g., \&quot;organization-name/repository-name\&quot;) of repositories to add the team to. |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| PULL | &quot;pull&quot; |
| PUSH | &quot;push&quot; |



## Enum: PrivacyEnum

| Name | Value |
|---- | -----|
| SECRET | &quot;secret&quot; |
| CLOSED | &quot;closed&quot; |



