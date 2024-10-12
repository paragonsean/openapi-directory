

# BillingInformationPartial

Optional information required for issuing invoices. Only accounts with `billing_information` present can be used as a `billing_account`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) |  |  [optional] |
|**name** | **String** | Name of the organisation receiving invoices.  |  [optional] |
|**vatNumber** | **String** | Value-added tax number, required for european reverse charge system.  |  [optional] |



