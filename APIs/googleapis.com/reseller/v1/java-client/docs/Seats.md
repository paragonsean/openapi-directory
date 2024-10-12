

# Seats

JSON template for subscription seats.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** | Identifies the resource as a subscription seat setting. Value: &#x60;subscriptions#seats&#x60; |  [optional] |
|**licensedNumberOfSeats** | **Integer** | Read-only field containing the current number of users that are assigned a license for the product defined in &#x60;skuId&#x60;. This field&#39;s value is equivalent to the numerical count of users returned by the Enterprise License Manager API method: [&#x60;listForProductAndSku&#x60;](/admin-sdk/licensing/v1/reference/licenseAssignments/listForProductAndSku). |  [optional] |
|**maximumNumberOfSeats** | **Integer** | This is a required property and is exclusive to subscriptions with &#x60;FLEXIBLE&#x60; or &#x60;TRIAL&#x60; plans. This property sets the maximum number of licensed users allowed on a subscription. This quantity can be increased up to the maximum limit defined in the reseller&#39;s contract. The minimum quantity is the current number of users in the customer account. *Note: *G Suite subscriptions automatically assign a license to every user. |  [optional] |
|**numberOfSeats** | **Integer** | This is a required property and is exclusive to subscriptions with &#x60;ANNUAL_MONTHLY_PAY&#x60; and &#x60;ANNUAL_YEARLY_PAY&#x60; plans. This property sets the maximum number of licenses assignable to users on a subscription. The reseller can add more licenses, but once set, the &#x60;numberOfSeats&#x60; cannot be reduced until renewal. The reseller is invoiced based on the &#x60;numberOfSeats&#x60; value regardless of how many of these user licenses are assigned. *Note: *Google Workspace subscriptions automatically assign a license to every user. |  [optional] |



