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

#include "OAIPlaceOrder_request_paymentData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaceOrder_request_paymentData::OAIPlaceOrder_request_paymentData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaceOrder_request_paymentData::OAIPlaceOrder_request_paymentData() {
    this->initializeModel();
}

OAIPlaceOrder_request_paymentData::~OAIPlaceOrder_request_paymentData() {}

void OAIPlaceOrder_request_paymentData::initializeModel() {

    m_gift_card_messages_isSet = false;
    m_gift_card_messages_isValid = false;

    m_gift_cards_isSet = false;
    m_gift_cards_isValid = false;

    m_payment_systems_isSet = false;
    m_payment_systems_isValid = false;

    m_payments_isSet = false;
    m_payments_isValid = false;

    m_update_status_isSet = false;
    m_update_status_isValid = false;
}

void OAIPlaceOrder_request_paymentData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaceOrder_request_paymentData::fromJsonObject(QJsonObject json) {

    m_gift_card_messages_isValid = ::OpenAPI::fromJsonValue(m_gift_card_messages, json[QString("giftCardMessages")]);
    m_gift_card_messages_isSet = !json[QString("giftCardMessages")].isNull() && m_gift_card_messages_isValid;

    m_gift_cards_isValid = ::OpenAPI::fromJsonValue(m_gift_cards, json[QString("giftCards")]);
    m_gift_cards_isSet = !json[QString("giftCards")].isNull() && m_gift_cards_isValid;

    m_payment_systems_isValid = ::OpenAPI::fromJsonValue(m_payment_systems, json[QString("paymentSystems")]);
    m_payment_systems_isSet = !json[QString("paymentSystems")].isNull() && m_payment_systems_isValid;

    m_payments_isValid = ::OpenAPI::fromJsonValue(m_payments, json[QString("payments")]);
    m_payments_isSet = !json[QString("payments")].isNull() && m_payments_isValid;

    m_update_status_isValid = ::OpenAPI::fromJsonValue(m_update_status, json[QString("updateStatus")]);
    m_update_status_isSet = !json[QString("updateStatus")].isNull() && m_update_status_isValid;
}

QString OAIPlaceOrder_request_paymentData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaceOrder_request_paymentData::asJsonObject() const {
    QJsonObject obj;
    if (m_gift_card_messages.size() > 0) {
        obj.insert(QString("giftCardMessages"), ::OpenAPI::toJsonValue(m_gift_card_messages));
    }
    if (m_gift_cards.size() > 0) {
        obj.insert(QString("giftCards"), ::OpenAPI::toJsonValue(m_gift_cards));
    }
    if (m_payment_systems.size() > 0) {
        obj.insert(QString("paymentSystems"), ::OpenAPI::toJsonValue(m_payment_systems));
    }
    if (m_payments.size() > 0) {
        obj.insert(QString("payments"), ::OpenAPI::toJsonValue(m_payments));
    }
    if (m_update_status_isSet) {
        obj.insert(QString("updateStatus"), ::OpenAPI::toJsonValue(m_update_status));
    }
    return obj;
}

QList<QJsonValue> OAIPlaceOrder_request_paymentData::getGiftCardMessages() const {
    return m_gift_card_messages;
}
void OAIPlaceOrder_request_paymentData::setGiftCardMessages(const QList<QJsonValue> &gift_card_messages) {
    m_gift_card_messages = gift_card_messages;
    m_gift_card_messages_isSet = true;
}

bool OAIPlaceOrder_request_paymentData::is_gift_card_messages_Set() const{
    return m_gift_card_messages_isSet;
}

bool OAIPlaceOrder_request_paymentData::is_gift_card_messages_Valid() const{
    return m_gift_card_messages_isValid;
}

QList<OAIPlaceOrder_request_paymentData_giftCards_inner> OAIPlaceOrder_request_paymentData::getGiftCards() const {
    return m_gift_cards;
}
void OAIPlaceOrder_request_paymentData::setGiftCards(const QList<OAIPlaceOrder_request_paymentData_giftCards_inner> &gift_cards) {
    m_gift_cards = gift_cards;
    m_gift_cards_isSet = true;
}

bool OAIPlaceOrder_request_paymentData::is_gift_cards_Set() const{
    return m_gift_cards_isSet;
}

bool OAIPlaceOrder_request_paymentData::is_gift_cards_Valid() const{
    return m_gift_cards_isValid;
}

QList<OAIPlaceOrder_request_paymentData_paymentSystems_inner> OAIPlaceOrder_request_paymentData::getPaymentSystems() const {
    return m_payment_systems;
}
void OAIPlaceOrder_request_paymentData::setPaymentSystems(const QList<OAIPlaceOrder_request_paymentData_paymentSystems_inner> &payment_systems) {
    m_payment_systems = payment_systems;
    m_payment_systems_isSet = true;
}

bool OAIPlaceOrder_request_paymentData::is_payment_systems_Set() const{
    return m_payment_systems_isSet;
}

bool OAIPlaceOrder_request_paymentData::is_payment_systems_Valid() const{
    return m_payment_systems_isValid;
}

QList<OAIPlaceOrder_request_paymentData_payments_inner> OAIPlaceOrder_request_paymentData::getPayments() const {
    return m_payments;
}
void OAIPlaceOrder_request_paymentData::setPayments(const QList<OAIPlaceOrder_request_paymentData_payments_inner> &payments) {
    m_payments = payments;
    m_payments_isSet = true;
}

bool OAIPlaceOrder_request_paymentData::is_payments_Set() const{
    return m_payments_isSet;
}

bool OAIPlaceOrder_request_paymentData::is_payments_Valid() const{
    return m_payments_isValid;
}

QString OAIPlaceOrder_request_paymentData::getUpdateStatus() const {
    return m_update_status;
}
void OAIPlaceOrder_request_paymentData::setUpdateStatus(const QString &update_status) {
    m_update_status = update_status;
    m_update_status_isSet = true;
}

bool OAIPlaceOrder_request_paymentData::is_update_status_Set() const{
    return m_update_status_isSet;
}

bool OAIPlaceOrder_request_paymentData::is_update_status_Valid() const{
    return m_update_status_isValid;
}

bool OAIPlaceOrder_request_paymentData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_gift_card_messages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_cards.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_systems.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_payments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_update_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlaceOrder_request_paymentData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_payments_isValid && true;
}

} // namespace OpenAPI
