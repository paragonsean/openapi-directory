# LinodeApi.IPv6RangeBGP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isBgp** | **Boolean** | Whether this IPv6 range is shared.  | [optional] [readonly] 
**linodes** | **[Number]** | A list of Linodes targeted by this IPv6 range. Includes Linodes with IP sharing.  | [optional] [readonly] 
**prefix** | **Number** | The prefix length of the address, denoting how many addresses can be assigned from this range calculated as 2 &lt;sup&gt;128-prefix&lt;/sup&gt;.  | [optional] 
**range** | **String** | The IPv6 range of addresses in this pool.  | [optional] [readonly] 
**region** | **String** | The region for this range of IPv6 addresses.  | [optional] [readonly] 


