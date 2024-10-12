

# IPAddressesAssignRequest

Request object for IP Addresses Assign (POST /networking/ips/assign).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignments** | [**List&lt;IPAddressesAssignRequestAssignmentsInner&gt;**](IPAddressesAssignRequestAssignmentsInner.md) | The list of assignments to make. You must have read_write access to all IPs being assigned and all Linodes being assigned to in order for the assignments to succeed.  |  |
|**region** | **String** | The ID of the Region in which these assignments are to take place. All IPs and Linodes must exist in this Region.  |  |



