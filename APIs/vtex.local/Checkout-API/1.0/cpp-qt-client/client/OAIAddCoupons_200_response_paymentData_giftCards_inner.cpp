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

#include "OAIAddCoupons_200_response_paymentData_giftCards_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddCoupons_200_response_paymentData_giftCards_inner::OAIAddCoupons_200_response_paymentData_giftCards_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddCoupons_200_response_paymentData_giftCards_inner::OAIAddCoupons_200_response_paymentData_giftCards_inner() {
    this->initializeModel();
}

OAIAddCoupons_200_response_paymentData_giftCards_inner::~OAIAddCoupons_200_response_paymentData_giftCards_inner() {}

void OAIAddCoupons_200_response_paymentData_giftCards_inner::initializeModel() {

    m_balance_isSet = false;
    m_balance_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_in_use_isSet = false;
    m_in_use_isValid = false;

    m_is_special_card_isSet = false;
    m_is_special_card_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_redemption_code_isSet = false;
    m_redemption_code_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIAddCoupons_200_response_paymentData_giftCards_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddCoupons_200_response_paymentData_giftCards_inner::fromJsonObject(QJsonObject json) {

    m_balance_isValid = ::OpenAPI::fromJsonValue(m_balance, json[QString("balance")]);
    m_balance_isSet = !json[QString("balance")].isNull() && m_balance_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_in_use_isValid = ::OpenAPI::fromJsonValue(m_in_use, json[QString("inUse")]);
    m_in_use_isSet = !json[QString("inUse")].isNull() && m_in_use_isValid;

    m_is_special_card_isValid = ::OpenAPI::fromJsonValue(m_is_special_card, json[QString("isSpecialCard")]);
    m_is_special_card_isSet = !json[QString("isSpecialCard")].isNull() && m_is_special_card_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_redemption_code_isValid = ::OpenAPI::fromJsonValue(m_redemption_code, json[QString("redemptionCode")]);
    m_redemption_code_isSet = !json[QString("redemptionCode")].isNull() && m_redemption_code_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIAddCoupons_200_response_paymentData_giftCards_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddCoupons_200_response_paymentData_giftCards_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_balance_isSet) {
        obj.insert(QString("balance"), ::OpenAPI::toJsonValue(m_balance));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_in_use_isSet) {
        obj.insert(QString("inUse"), ::OpenAPI::toJsonValue(m_in_use));
    }
    if (m_is_special_card_isSet) {
        obj.insert(QString("isSpecialCard"), ::OpenAPI::toJsonValue(m_is_special_card));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_redemption_code_isSet) {
        obj.insert(QString("redemptionCode"), ::OpenAPI::toJsonValue(m_redemption_code));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

qint32 OAIAddCoupons_200_response_paymentData_giftCards_inner::getBalance() const {
    return m_balance;
}
void OAIAddCoupons_200_response_paymentData_giftCards_inner::setBalance(const qint32 &balance) {
    m_balance = balance;
    m_balance_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_balance_Set() const{
    return m_balance_isSet;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_balance_Valid() const{
    return m_balance_isValid;
}

QString OAIAddCoupons_200_response_paymentData_giftCards_inner::getId() const {
    return m_id;
}
void OAIAddCoupons_200_response_paymentData_giftCards_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::isInUse() const {
    return m_in_use;
}
void OAIAddCoupons_200_response_paymentData_giftCards_inner::setInUse(const bool &in_use) {
    m_in_use = in_use;
    m_in_use_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_in_use_Set() const{
    return m_in_use_isSet;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_in_use_Valid() const{
    return m_in_use_isValid;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::isIsSpecialCard() const {
    return m_is_special_card;
}
void OAIAddCoupons_200_response_paymentData_giftCards_inner::setIsSpecialCard(const bool &is_special_card) {
    m_is_special_card = is_special_card;
    m_is_special_card_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_is_special_card_Set() const{
    return m_is_special_card_isSet;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_is_special_card_Valid() const{
    return m_is_special_card_isValid;
}

QString OAIAddCoupons_200_response_paymentData_giftCards_inner::getName() const {
    return m_name;
}
void OAIAddCoupons_200_response_paymentData_giftCards_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAddCoupons_200_response_paymentData_giftCards_inner::getRedemptionCode() const {
    return m_redemption_code;
}
void OAIAddCoupons_200_response_paymentData_giftCards_inner::setRedemptionCode(const QString &redemption_code) {
    m_redemption_code = redemption_code;
    m_redemption_code_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_redemption_code_Set() const{
    return m_redemption_code_isSet;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_redemption_code_Valid() const{
    return m_redemption_code_isValid;
}

qint32 OAIAddCoupons_200_response_paymentData_giftCards_inner::getValue() const {
    return m_value;
}
void OAIAddCoupons_200_response_paymentData_giftCards_inner::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_balance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_in_use_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_special_card_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_redemption_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddCoupons_200_response_paymentData_giftCards_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
