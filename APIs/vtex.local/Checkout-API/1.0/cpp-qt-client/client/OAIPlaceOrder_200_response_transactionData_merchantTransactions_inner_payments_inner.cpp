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

#include "OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner() {
    this->initializeModel();
}

OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::~OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner() {}

void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::initializeModel() {

    m_account_id_isSet = false;
    m_account_id_isValid = false;

    m_bin_isSet = false;
    m_bin_isValid = false;

    m_gift_card_id_isSet = false;
    m_gift_card_id_isValid = false;

    m_gift_card_provider_isSet = false;
    m_gift_card_provider_isValid = false;

    m_gift_card_redemption_code_isSet = false;
    m_gift_card_redemption_code_isValid = false;

    m_payment_system_isSet = false;
    m_payment_system_isValid = false;

    m_reference_value_isSet = false;
    m_reference_value_isValid = false;

    m_token_id_isSet = false;
    m_token_id_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::fromJsonObject(QJsonObject json) {

    m_account_id_isValid = ::OpenAPI::fromJsonValue(m_account_id, json[QString("accountId")]);
    m_account_id_isSet = !json[QString("accountId")].isNull() && m_account_id_isValid;

    m_bin_isValid = ::OpenAPI::fromJsonValue(m_bin, json[QString("bin")]);
    m_bin_isSet = !json[QString("bin")].isNull() && m_bin_isValid;

    m_gift_card_id_isValid = ::OpenAPI::fromJsonValue(m_gift_card_id, json[QString("giftCardId")]);
    m_gift_card_id_isSet = !json[QString("giftCardId")].isNull() && m_gift_card_id_isValid;

    m_gift_card_provider_isValid = ::OpenAPI::fromJsonValue(m_gift_card_provider, json[QString("giftCardProvider")]);
    m_gift_card_provider_isSet = !json[QString("giftCardProvider")].isNull() && m_gift_card_provider_isValid;

    m_gift_card_redemption_code_isValid = ::OpenAPI::fromJsonValue(m_gift_card_redemption_code, json[QString("giftCardRedemptionCode")]);
    m_gift_card_redemption_code_isSet = !json[QString("giftCardRedemptionCode")].isNull() && m_gift_card_redemption_code_isValid;

    m_payment_system_isValid = ::OpenAPI::fromJsonValue(m_payment_system, json[QString("paymentSystem")]);
    m_payment_system_isSet = !json[QString("paymentSystem")].isNull() && m_payment_system_isValid;

    m_reference_value_isValid = ::OpenAPI::fromJsonValue(m_reference_value, json[QString("referenceValue")]);
    m_reference_value_isSet = !json[QString("referenceValue")].isNull() && m_reference_value_isValid;

    m_token_id_isValid = ::OpenAPI::fromJsonValue(m_token_id, json[QString("tokenId")]);
    m_token_id_isSet = !json[QString("tokenId")].isNull() && m_token_id_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_account_id_isSet) {
        obj.insert(QString("accountId"), ::OpenAPI::toJsonValue(m_account_id));
    }
    if (m_bin_isSet) {
        obj.insert(QString("bin"), ::OpenAPI::toJsonValue(m_bin));
    }
    if (m_gift_card_id_isSet) {
        obj.insert(QString("giftCardId"), ::OpenAPI::toJsonValue(m_gift_card_id));
    }
    if (m_gift_card_provider_isSet) {
        obj.insert(QString("giftCardProvider"), ::OpenAPI::toJsonValue(m_gift_card_provider));
    }
    if (m_gift_card_redemption_code_isSet) {
        obj.insert(QString("giftCardRedemptionCode"), ::OpenAPI::toJsonValue(m_gift_card_redemption_code));
    }
    if (m_payment_system_isSet) {
        obj.insert(QString("paymentSystem"), ::OpenAPI::toJsonValue(m_payment_system));
    }
    if (m_reference_value_isSet) {
        obj.insert(QString("referenceValue"), ::OpenAPI::toJsonValue(m_reference_value));
    }
    if (m_token_id_isSet) {
        obj.insert(QString("tokenId"), ::OpenAPI::toJsonValue(m_token_id));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::getAccountId() const {
    return m_account_id;
}
void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::setAccountId(const QString &account_id) {
    m_account_id = account_id;
    m_account_id_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_account_id_Set() const{
    return m_account_id_isSet;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_account_id_Valid() const{
    return m_account_id_isValid;
}

QString OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::getBin() const {
    return m_bin;
}
void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::setBin(const QString &bin) {
    m_bin = bin;
    m_bin_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_bin_Set() const{
    return m_bin_isSet;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_bin_Valid() const{
    return m_bin_isValid;
}

QString OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::getGiftCardId() const {
    return m_gift_card_id;
}
void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::setGiftCardId(const QString &gift_card_id) {
    m_gift_card_id = gift_card_id;
    m_gift_card_id_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_gift_card_id_Set() const{
    return m_gift_card_id_isSet;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_gift_card_id_Valid() const{
    return m_gift_card_id_isValid;
}

QString OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::getGiftCardProvider() const {
    return m_gift_card_provider;
}
void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::setGiftCardProvider(const QString &gift_card_provider) {
    m_gift_card_provider = gift_card_provider;
    m_gift_card_provider_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_gift_card_provider_Set() const{
    return m_gift_card_provider_isSet;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_gift_card_provider_Valid() const{
    return m_gift_card_provider_isValid;
}

QString OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::getGiftCardRedemptionCode() const {
    return m_gift_card_redemption_code;
}
void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::setGiftCardRedemptionCode(const QString &gift_card_redemption_code) {
    m_gift_card_redemption_code = gift_card_redemption_code;
    m_gift_card_redemption_code_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_gift_card_redemption_code_Set() const{
    return m_gift_card_redemption_code_isSet;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_gift_card_redemption_code_Valid() const{
    return m_gift_card_redemption_code_isValid;
}

QString OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::getPaymentSystem() const {
    return m_payment_system;
}
void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::setPaymentSystem(const QString &payment_system) {
    m_payment_system = payment_system;
    m_payment_system_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_payment_system_Set() const{
    return m_payment_system_isSet;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_payment_system_Valid() const{
    return m_payment_system_isValid;
}

qint32 OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::getReferenceValue() const {
    return m_reference_value;
}
void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::setReferenceValue(const qint32 &reference_value) {
    m_reference_value = reference_value;
    m_reference_value_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_reference_value_Set() const{
    return m_reference_value_isSet;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_reference_value_Valid() const{
    return m_reference_value_isValid;
}

QString OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::getTokenId() const {
    return m_token_id;
}
void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::setTokenId(const QString &token_id) {
    m_token_id = token_id;
    m_token_id_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_token_id_Set() const{
    return m_token_id_isSet;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_token_id_Valid() const{
    return m_token_id_isValid;
}

qint32 OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::getValue() const {
    return m_value;
}
void OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_bin_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_card_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_card_provider_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gift_card_redemption_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_system_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_id_isSet) {
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

bool OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner_payments_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
