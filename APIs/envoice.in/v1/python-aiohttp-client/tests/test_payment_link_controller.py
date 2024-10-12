# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_result_payment_link import ListResultPaymentLink
from openapi_server.models.payment_link import PaymentLink
from openapi_server.models.payment_link_uri_api_model import PaymentLinkUriApiModel


pytestmark = pytest.mark.asyncio

async def test_payment_link_api_all(client):
    """Test case for payment_link_api_all

    Create a payment link
    """
    params = [('queryOptions.page', 56),
                    ('queryOptions.pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/paymentlink/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_payment_link_api_delete(client):
    """Test case for payment_link_api_delete

    Delete an existing payment link
    """
    body = {"Invoice":{"ShouldSendReminders":True,"InvoiceCategoryId":3,"Payments":[{"PaidOn":"2000-01-23T04:56:07.000+00:00","Type":"Other","ReferenceId":"ReferenceId","Amount":8.969578798196912,"Note":"Note","IsAutomatic":True,"Id":7,"InvoiceId":3},{"PaidOn":"2000-01-23T04:56:07.000+00:00","Type":"Other","ReferenceId":"ReferenceId","Amount":8.969578798196912,"Note":"Note","IsAutomatic":True,"Id":7,"InvoiceId":3}],"Attachments":[{"Type":"External","OriginalFileName":"OriginalFileName","Size":5,"Id":1,"InvoiceId":4,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"},{"Type":"External","OriginalFileName":"OriginalFileName","Size":5,"Id":1,"InvoiceId":4,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"}],"CurrencyId":6,"Duedate":"2000-01-23T04:56:07.000+00:00","TaxAmount":5.533258397034986,"Number":"Number","PaymentGateways":[{"Id":0,"Name":"Name"},{"Id":0,"Name":"Name"}],"AccessToken":"AccessToken","RecurringProfileId":3,"ClientId":9,"Items":[{"Description":"Description","TaxPercentage":7.143538047012306,"Quantity":5.944895607614016,"TaxId":3,"TotalAmount":0.8851374739011653,"InvoiceId":6,"Cost":6.965117697638846,"DiscountAmount":1.284659006116532,"WorkTypeId":7,"TaxAmount":3.353193347011243,"DiscountPercentage":2.8841621266687802,"Id":6,"SubTotalAmount":6.704019297950036},{"Description":"Description","TaxPercentage":7.143538047012306,"Quantity":5.944895607614016,"TaxId":3,"TotalAmount":0.8851374739011653,"InvoiceId":6,"Cost":6.965117697638846,"DiscountAmount":1.284659006116532,"WorkTypeId":7,"TaxAmount":3.353193347011243,"DiscountPercentage":2.8841621266687802,"Id":6,"SubTotalAmount":6.704019297950036}],"Notes":"Notes","Activities":[{"Type":"Created","EstimationNumber":"EstimationNumber","Message":"Message","UserId":7,"EstimationId":1,"OrderNumber":"OrderNumber","Id":1,"InvoiceNumber":"InvoiceNumber","InvoiceId":1,"OrderId":6,"Link":"Link"},{"Type":"Created","EstimationNumber":"EstimationNumber","Message":"Message","UserId":7,"EstimationId":1,"OrderNumber":"OrderNumber","Id":1,"InvoiceNumber":"InvoiceNumber","InvoiceId":1,"OrderId":6,"Link":"Link"}],"Status":"Draft","ClonedFromId":9,"PaymentLinkId":4,"EstimationId":9,"PoNumber":"PoNumber","Terms":"Terms","TotalAmount":3.2588565619047607,"OrderId":6,"DiscountAmount":8.762042012749001,"EnablePartialPayments":True,"IssuedOn":"2000-01-23T04:56:07.000+00:00","UserId":4,"Id":6,"IsDigitallySigned":True,"SubTotalAmount":7.04836565559697},"User":{"Status":"Normal","SubscriptionPlan":{"SystemCancelationReason":"FailToCaptureFee","Recurrence":"Monthly","IsActive":True,"OrderIdentifier":"OrderIdentifier","SaleId":5,"TrialNumberOfDays":7,"HasDuePaymentSince":"2000-01-23T04:56:07.000+00:00","Name":"Name","CurrencyCode":"CurrencyCode","Identifier":"Identifier","Version":3,"HasDuePayment":True,"TrialStartsOn":"2000-01-23T04:56:07.000+00:00","Features":["Api","Api"],"CancellatedOn":"2000-01-23T04:56:07.000+00:00","Status":"ActiveTrial","OnHold":True,"ExternalIdentifier":"ExternalIdentifier","LastPaymentOn":"2000-01-23T04:56:07.000+00:00","MaxClients":3,"TrialEndsOn":"2000-01-23T04:56:07.000+00:00","CouponCode":"CouponCode","Price":9.897492629215506,"UserId":0,"IsLifetime":True,"Id":3},"VerifiedOn":"2000-01-23T04:56:07.000+00:00","Email":"Email","LastSeenOn":"2000-01-23T04:56:07.000+00:00","PasswordSalt":"PasswordSalt","ReferrerKey":"ReferrerKey","IsLocked":True,"HasBeenOnboarded":True,"ActionNotificationsLastReadOn":"2000-01-23T04:56:07.000+00:00","ExternalConnections":[{"ExternalUsername":"ExternalUsername","AccessToken":"AccessToken","UserId":6,"ExpiresOn":"2000-01-23T04:56:07.000+00:00","AccessTokenSecret":"AccessTokenSecret","Data":"Data","ExternalUserId":"ExternalUserId","Id":8,"Provider":"Provider"},{"ExternalUsername":"ExternalUsername","AccessToken":"AccessToken","UserId":6,"ExpiresOn":"2000-01-23T04:56:07.000+00:00","AccessTokenSecret":"AccessTokenSecret","Data":"Data","ExternalUserId":"ExternalUserId","Id":8,"Provider":"Provider"}],"ReferralPath":"ReferralPath","Name":"Name","YearsOfExperience":"One","Type":"Anonymous","ReferredUsers":8,"Username":"Username","KnowledgeNotificationsLastReadOn":"2000-01-23T04:56:07.000+00:00","Id":4,"IsVerified":True,"Settings":{"EnableClientPortal":True,"EnablePredictiveInvoicing":True,"Address":"Address","Iban":"Iban","StoreCurrencyId":0,"StoreEmail":"StoreEmail","StoreCurrency":{"Symbol":"Symbol","Value":"Value","Id":3,"Code":"Code","Name":"Name"},"CurrencySymbol":"CurrencySymbol","StoreDescription":"StoreDescription","Currency":{"Symbol":"Symbol","Value":"Value","Id":3,"Code":"Code","Name":"Name"},"StoreCheckoutFields":"ShowMinimumRequiredFields","CountryId":1,"UserSignature":"UserSignature","StoreCustomJavaScript":"StoreCustomJavaScript","StoreLanguageId":5,"EnableRecurringInvoicing":True,"StoreName":"StoreName","Terms":"Terms","Cname":"Cname","StorePurchaseEmailMessage":"StorePurchaseEmailMessage","StoreColorHex":"StoreColorHex","Profession":"Other","BackgroundImage":"BackgroundImage","InvoiceTemplate":"Default","Country":{"Value":"Value","Id":9,"Name":"Name"},"Swift":"Swift","Id":8,"StoreLanguage":{"Id":5,"Name":"Name","UiCulture":"UiCulture"},"StorePurchaseThankYouMessage":"StorePurchaseThankYouMessage","ApiKey":"ApiKey","Bank":"Bank","HasInvoiceLogo":True,"CurrencyId":3,"CompanyRegistrationNumber":"CompanyRegistrationNumber","ReferralProgram":"Enabled","StoreUrl":"StoreUrl","DoNotTrack":True,"DefaultDueDateInDays":9,"BankAccount":"BankAccount","ReceiveSmsNotifications":True,"VatNumber":"VatNumber","DefaultDateFormat":"DefaultDateFormat","StoreTextColorHex":"StoreTextColorHex","YearsOfExperience":7,"AccountantEmail":"AccountantEmail","UserId":8,"InvoiceTemplateColorHex":"InvoiceTemplateColorHex","ApiSecret":"ApiSecret","PhoneNumber":"PhoneNumber","SubscribeToProductEmails":True},"Password":"Password"},"TotalAmount":1.7325933120207193,"CurrencyId":2,"DiscountAmount":4.145608029883936,"TaxAmount":2.9409642974827896,"Number":"Number","AccessToken":"AccessToken","UserId":2,"Currency":{"Symbol":"Symbol","Value":"Value","Id":3,"Code":"Code","Name":"Name"},"ClientId":9,"Items":[{"TaxPercentage":4.86315908102884,"PaymentLinkId":4,"WorkType":{"UserId":4,"Title":"Title","Id":8},"Quantity":7.260521264802104,"Tax":{"Percentage":9.702963800023566,"UserId":0,"Id":0,"Name":"Name"},"TaxId":5,"TotalAmount":6.073898085781152,"Cost":0.2025324113236393,"DiscountAmount":6.628464275087742,"WorkTypeId":3,"TaxAmount":7.933506881737151,"DiscountPercentage":4.258773108174356,"Id":1,"SubTotalAmount":9.132027271330688},{"TaxPercentage":4.86315908102884,"PaymentLinkId":4,"WorkType":{"UserId":4,"Title":"Title","Id":8},"Quantity":7.260521264802104,"Tax":{"Percentage":9.702963800023566,"UserId":0,"Id":0,"Name":"Name"},"TaxId":5,"TotalAmount":6.073898085781152,"Cost":0.2025324113236393,"DiscountAmount":6.628464275087742,"WorkTypeId":3,"TaxAmount":7.933506881737151,"DiscountPercentage":4.258773108174356,"Id":1,"SubTotalAmount":9.132027271330688}],"Id":7,"Client":{"UiLanguageId":2,"Email":"Email","Address":"Address","UserId":7,"ClientCurrencyId":1,"Vat":"Vat","ClientCountryId":6,"DefaultDueDateInDays":5,"PhoneNumber":"PhoneNumber","Id":5,"CompanyRegistrationNumber":"CompanyRegistrationNumber","Name":"Name"},"SubTotalAmount":0.43431398824148815}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/paymentlink/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_payment_link_api_new(client):
    """Test case for payment_link_api_new

    Create a payment link
    """
    body = {"Invoice":{"ShouldSendReminders":True,"InvoiceCategoryId":3,"Payments":[{"PaidOn":"2000-01-23T04:56:07.000+00:00","Type":"Other","ReferenceId":"ReferenceId","Amount":8.969578798196912,"Note":"Note","IsAutomatic":True,"Id":7,"InvoiceId":3},{"PaidOn":"2000-01-23T04:56:07.000+00:00","Type":"Other","ReferenceId":"ReferenceId","Amount":8.969578798196912,"Note":"Note","IsAutomatic":True,"Id":7,"InvoiceId":3}],"Attachments":[{"Type":"External","OriginalFileName":"OriginalFileName","Size":5,"Id":1,"InvoiceId":4,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"},{"Type":"External","OriginalFileName":"OriginalFileName","Size":5,"Id":1,"InvoiceId":4,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"}],"CurrencyId":6,"Duedate":"2000-01-23T04:56:07.000+00:00","TaxAmount":5.533258397034986,"Number":"Number","PaymentGateways":[{"Id":0,"Name":"Name"},{"Id":0,"Name":"Name"}],"AccessToken":"AccessToken","RecurringProfileId":3,"ClientId":9,"Items":[{"Description":"Description","TaxPercentage":7.143538047012306,"Quantity":5.944895607614016,"TaxId":3,"TotalAmount":0.8851374739011653,"InvoiceId":6,"Cost":6.965117697638846,"DiscountAmount":1.284659006116532,"WorkTypeId":7,"TaxAmount":3.353193347011243,"DiscountPercentage":2.8841621266687802,"Id":6,"SubTotalAmount":6.704019297950036},{"Description":"Description","TaxPercentage":7.143538047012306,"Quantity":5.944895607614016,"TaxId":3,"TotalAmount":0.8851374739011653,"InvoiceId":6,"Cost":6.965117697638846,"DiscountAmount":1.284659006116532,"WorkTypeId":7,"TaxAmount":3.353193347011243,"DiscountPercentage":2.8841621266687802,"Id":6,"SubTotalAmount":6.704019297950036}],"Notes":"Notes","Activities":[{"Type":"Created","EstimationNumber":"EstimationNumber","Message":"Message","UserId":7,"EstimationId":1,"OrderNumber":"OrderNumber","Id":1,"InvoiceNumber":"InvoiceNumber","InvoiceId":1,"OrderId":6,"Link":"Link"},{"Type":"Created","EstimationNumber":"EstimationNumber","Message":"Message","UserId":7,"EstimationId":1,"OrderNumber":"OrderNumber","Id":1,"InvoiceNumber":"InvoiceNumber","InvoiceId":1,"OrderId":6,"Link":"Link"}],"Status":"Draft","ClonedFromId":9,"PaymentLinkId":4,"EstimationId":9,"PoNumber":"PoNumber","Terms":"Terms","TotalAmount":3.2588565619047607,"OrderId":6,"DiscountAmount":8.762042012749001,"EnablePartialPayments":True,"IssuedOn":"2000-01-23T04:56:07.000+00:00","UserId":4,"Id":6,"IsDigitallySigned":True,"SubTotalAmount":7.04836565559697},"User":{"Status":"Normal","SubscriptionPlan":{"SystemCancelationReason":"FailToCaptureFee","Recurrence":"Monthly","IsActive":True,"OrderIdentifier":"OrderIdentifier","SaleId":5,"TrialNumberOfDays":7,"HasDuePaymentSince":"2000-01-23T04:56:07.000+00:00","Name":"Name","CurrencyCode":"CurrencyCode","Identifier":"Identifier","Version":3,"HasDuePayment":True,"TrialStartsOn":"2000-01-23T04:56:07.000+00:00","Features":["Api","Api"],"CancellatedOn":"2000-01-23T04:56:07.000+00:00","Status":"ActiveTrial","OnHold":True,"ExternalIdentifier":"ExternalIdentifier","LastPaymentOn":"2000-01-23T04:56:07.000+00:00","MaxClients":3,"TrialEndsOn":"2000-01-23T04:56:07.000+00:00","CouponCode":"CouponCode","Price":9.897492629215506,"UserId":0,"IsLifetime":True,"Id":3},"VerifiedOn":"2000-01-23T04:56:07.000+00:00","Email":"Email","LastSeenOn":"2000-01-23T04:56:07.000+00:00","PasswordSalt":"PasswordSalt","ReferrerKey":"ReferrerKey","IsLocked":True,"HasBeenOnboarded":True,"ActionNotificationsLastReadOn":"2000-01-23T04:56:07.000+00:00","ExternalConnections":[{"ExternalUsername":"ExternalUsername","AccessToken":"AccessToken","UserId":6,"ExpiresOn":"2000-01-23T04:56:07.000+00:00","AccessTokenSecret":"AccessTokenSecret","Data":"Data","ExternalUserId":"ExternalUserId","Id":8,"Provider":"Provider"},{"ExternalUsername":"ExternalUsername","AccessToken":"AccessToken","UserId":6,"ExpiresOn":"2000-01-23T04:56:07.000+00:00","AccessTokenSecret":"AccessTokenSecret","Data":"Data","ExternalUserId":"ExternalUserId","Id":8,"Provider":"Provider"}],"ReferralPath":"ReferralPath","Name":"Name","YearsOfExperience":"One","Type":"Anonymous","ReferredUsers":8,"Username":"Username","KnowledgeNotificationsLastReadOn":"2000-01-23T04:56:07.000+00:00","Id":4,"IsVerified":True,"Settings":{"EnableClientPortal":True,"EnablePredictiveInvoicing":True,"Address":"Address","Iban":"Iban","StoreCurrencyId":0,"StoreEmail":"StoreEmail","StoreCurrency":{"Symbol":"Symbol","Value":"Value","Id":3,"Code":"Code","Name":"Name"},"CurrencySymbol":"CurrencySymbol","StoreDescription":"StoreDescription","Currency":{"Symbol":"Symbol","Value":"Value","Id":3,"Code":"Code","Name":"Name"},"StoreCheckoutFields":"ShowMinimumRequiredFields","CountryId":1,"UserSignature":"UserSignature","StoreCustomJavaScript":"StoreCustomJavaScript","StoreLanguageId":5,"EnableRecurringInvoicing":True,"StoreName":"StoreName","Terms":"Terms","Cname":"Cname","StorePurchaseEmailMessage":"StorePurchaseEmailMessage","StoreColorHex":"StoreColorHex","Profession":"Other","BackgroundImage":"BackgroundImage","InvoiceTemplate":"Default","Country":{"Value":"Value","Id":9,"Name":"Name"},"Swift":"Swift","Id":8,"StoreLanguage":{"Id":5,"Name":"Name","UiCulture":"UiCulture"},"StorePurchaseThankYouMessage":"StorePurchaseThankYouMessage","ApiKey":"ApiKey","Bank":"Bank","HasInvoiceLogo":True,"CurrencyId":3,"CompanyRegistrationNumber":"CompanyRegistrationNumber","ReferralProgram":"Enabled","StoreUrl":"StoreUrl","DoNotTrack":True,"DefaultDueDateInDays":9,"BankAccount":"BankAccount","ReceiveSmsNotifications":True,"VatNumber":"VatNumber","DefaultDateFormat":"DefaultDateFormat","StoreTextColorHex":"StoreTextColorHex","YearsOfExperience":7,"AccountantEmail":"AccountantEmail","UserId":8,"InvoiceTemplateColorHex":"InvoiceTemplateColorHex","ApiSecret":"ApiSecret","PhoneNumber":"PhoneNumber","SubscribeToProductEmails":True},"Password":"Password"},"TotalAmount":1.7325933120207193,"CurrencyId":2,"DiscountAmount":4.145608029883936,"TaxAmount":2.9409642974827896,"Number":"Number","AccessToken":"AccessToken","UserId":2,"Currency":{"Symbol":"Symbol","Value":"Value","Id":3,"Code":"Code","Name":"Name"},"ClientId":9,"Items":[{"TaxPercentage":4.86315908102884,"PaymentLinkId":4,"WorkType":{"UserId":4,"Title":"Title","Id":8},"Quantity":7.260521264802104,"Tax":{"Percentage":9.702963800023566,"UserId":0,"Id":0,"Name":"Name"},"TaxId":5,"TotalAmount":6.073898085781152,"Cost":0.2025324113236393,"DiscountAmount":6.628464275087742,"WorkTypeId":3,"TaxAmount":7.933506881737151,"DiscountPercentage":4.258773108174356,"Id":1,"SubTotalAmount":9.132027271330688},{"TaxPercentage":4.86315908102884,"PaymentLinkId":4,"WorkType":{"UserId":4,"Title":"Title","Id":8},"Quantity":7.260521264802104,"Tax":{"Percentage":9.702963800023566,"UserId":0,"Id":0,"Name":"Name"},"TaxId":5,"TotalAmount":6.073898085781152,"Cost":0.2025324113236393,"DiscountAmount":6.628464275087742,"WorkTypeId":3,"TaxAmount":7.933506881737151,"DiscountPercentage":4.258773108174356,"Id":1,"SubTotalAmount":9.132027271330688}],"Id":7,"Client":{"UiLanguageId":2,"Email":"Email","Address":"Address","UserId":7,"ClientCurrencyId":1,"Vat":"Vat","ClientCountryId":6,"DefaultDueDateInDays":5,"PhoneNumber":"PhoneNumber","Id":5,"CompanyRegistrationNumber":"CompanyRegistrationNumber","Name":"Name"},"SubTotalAmount":0.43431398824148815}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/paymentlink/new',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payment_link_api_uri(client):
    """Test case for payment_link_api_uri

    Return the unique url to the client's payment link
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/paymentlink/uri',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

