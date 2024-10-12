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
 * OAICartSimulation_200_response_paymentData.h
 *
 * Payment data information.
 */

#ifndef OAICartSimulation_200_response_paymentData_H
#define OAICartSimulation_200_response_paymentData_H

#include <QJsonObject>

#include "OAICartSimulation_200_response_paymentData_paymentSystems_inner.h"
#include "OAIObject.h"
#include <QJsonValue>
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICartSimulation_200_response_paymentData_paymentSystems_inner;

class OAICartSimulation_200_response_paymentData : public OAIObject {
public:
    OAICartSimulation_200_response_paymentData();
    OAICartSimulation_200_response_paymentData(QString json);
    ~OAICartSimulation_200_response_paymentData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<QJsonValue> getAvailableAccounts() const;
    void setAvailableAccounts(const QList<QJsonValue> &available_accounts);
    bool is_available_accounts_Set() const;
    bool is_available_accounts_Valid() const;

    OAIObject getAvailableAssociations() const;
    void setAvailableAssociations(const OAIObject &available_associations);
    bool is_available_associations_Set() const;
    bool is_available_associations_Valid() const;

    QList<QJsonValue> getAvailableTokens() const;
    void setAvailableTokens(const QList<QJsonValue> &available_tokens);
    bool is_available_tokens_Set() const;
    bool is_available_tokens_Valid() const;

    QList<QJsonValue> getGiftCardMessages() const;
    void setGiftCardMessages(const QList<QJsonValue> &gift_card_messages);
    bool is_gift_card_messages_Set() const;
    bool is_gift_card_messages_Valid() const;

    QList<QJsonValue> getGiftCards() const;
    void setGiftCards(const QList<QJsonValue> &gift_cards);
    bool is_gift_cards_Set() const;
    bool is_gift_cards_Valid() const;

    QList<QJsonValue> getInstallmentOptions() const;
    void setInstallmentOptions(const QList<QJsonValue> &installment_options);
    bool is_installment_options_Set() const;
    bool is_installment_options_Valid() const;

    QList<OAICartSimulation_200_response_paymentData_paymentSystems_inner> getPaymentSystems() const;
    void setPaymentSystems(const QList<OAICartSimulation_200_response_paymentData_paymentSystems_inner> &payment_systems);
    bool is_payment_systems_Set() const;
    bool is_payment_systems_Valid() const;

    QList<QJsonValue> getPayments() const;
    void setPayments(const QList<QJsonValue> &payments);
    bool is_payments_Set() const;
    bool is_payments_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<QJsonValue> m_available_accounts;
    bool m_available_accounts_isSet;
    bool m_available_accounts_isValid;

    OAIObject m_available_associations;
    bool m_available_associations_isSet;
    bool m_available_associations_isValid;

    QList<QJsonValue> m_available_tokens;
    bool m_available_tokens_isSet;
    bool m_available_tokens_isValid;

    QList<QJsonValue> m_gift_card_messages;
    bool m_gift_card_messages_isSet;
    bool m_gift_card_messages_isValid;

    QList<QJsonValue> m_gift_cards;
    bool m_gift_cards_isSet;
    bool m_gift_cards_isValid;

    QList<QJsonValue> m_installment_options;
    bool m_installment_options_isSet;
    bool m_installment_options_isValid;

    QList<OAICartSimulation_200_response_paymentData_paymentSystems_inner> m_payment_systems;
    bool m_payment_systems_isSet;
    bool m_payment_systems_isValid;

    QList<QJsonValue> m_payments;
    bool m_payments_isSet;
    bool m_payments_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICartSimulation_200_response_paymentData)

#endif // OAICartSimulation_200_response_paymentData_H
