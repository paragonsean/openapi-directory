/**
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAddPaymentData_request_payments_inner.h
 *
 * 
 */

#ifndef OAIAddPaymentData_request_payments_inner_H
#define OAIAddPaymentData_request_payments_inner_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAddPaymentData_request_payments_inner : public OAIObject {
public:
    OAIAddPaymentData_request_payments_inner();
    OAIAddPaymentData_request_payments_inner(QString json);
    ~OAIAddPaymentData_request_payments_inner() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getGroup() const;
    void setGroup(const QString &group);
    bool is_group_Set() const;
    bool is_group_Valid() const;

    bool isHasDefaultBillingAddress() const;
    void setHasDefaultBillingAddress(const bool &has_default_billing_address);
    bool is_has_default_billing_address_Set() const;
    bool is_has_default_billing_address_Valid() const;

    qint32 getInstallments() const;
    void setInstallments(const qint32 &installments);
    bool is_installments_Set() const;
    bool is_installments_Valid() const;

    double getInstallmentsInterestRate() const;
    void setInstallmentsInterestRate(const double &installments_interest_rate);
    bool is_installments_interest_rate_Set() const;
    bool is_installments_interest_rate_Valid() const;

    qint32 getInstallmentsValue() const;
    void setInstallmentsValue(const qint32 &installments_value);
    bool is_installments_value_Set() const;
    bool is_installments_value_Valid() const;

    qint32 getPaymentSystem() const;
    void setPaymentSystem(const qint32 &payment_system);
    bool is_payment_system_Set() const;
    bool is_payment_system_Valid() const;

    QString getPaymentSystemName() const;
    void setPaymentSystemName(const QString &payment_system_name);
    bool is_payment_system_name_Set() const;
    bool is_payment_system_name_Valid() const;

    qint32 getReferenceValue() const;
    void setReferenceValue(const qint32 &reference_value);
    bool is_reference_value_Set() const;
    bool is_reference_value_Valid() const;

    qint32 getValue() const;
    void setValue(const qint32 &value);
    bool is_value_Set() const;
    bool is_value_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_group;
    bool m_group_isSet;
    bool m_group_isValid;

    bool m_has_default_billing_address;
    bool m_has_default_billing_address_isSet;
    bool m_has_default_billing_address_isValid;

    qint32 m_installments;
    bool m_installments_isSet;
    bool m_installments_isValid;

    double m_installments_interest_rate;
    bool m_installments_interest_rate_isSet;
    bool m_installments_interest_rate_isValid;

    qint32 m_installments_value;
    bool m_installments_value_isSet;
    bool m_installments_value_isValid;

    qint32 m_payment_system;
    bool m_payment_system_isSet;
    bool m_payment_system_isValid;

    QString m_payment_system_name;
    bool m_payment_system_name_isSet;
    bool m_payment_system_name_isValid;

    qint32 m_reference_value;
    bool m_reference_value_isSet;
    bool m_reference_value_isValid;

    qint32 m_value;
    bool m_value_isSet;
    bool m_value_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAddPaymentData_request_payments_inner)

#endif // OAIAddPaymentData_request_payments_inner_H
