

# AccountUpdatePartial

Account Update Request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) |  |  [optional] |
|**billingInformation** | [**BillingInformation**](BillingInformation.md) |  |  [optional] |
|**discoverable** | **Boolean** | The account will be included for all members of the ix in the list of accounts.  Only &#x60;id&#x60;, &#x60;name&#x60; and &#x60;present_in_metro_area_networks&#x60; are provided to other members. |  [optional] |
|**externalRef** | **String** | Reference field, free to use for the API user. |  [optional] |
|**legalName** | **String** | Legal name of the organisation. Only required when it&#39;s different from the account name.  |  [optional] |
|**managingAccount** | **String** | The &#x60;id&#x60; of a managing account. Can be used for creating a customer hierachy.  |  [optional] |
|**metroAreaNetworkPresence** | **List&lt;String&gt;** | Informal list of &#x60;MetroAreaNetwork&#x60; ids, indicating the presence to other accounts. The list is maintained by the account and can be empty.  |  [optional] |
|**name** | **String** | Name of the account, how it gets represented in e.g. a \&quot;customers list\&quot;.  |  [optional] |



