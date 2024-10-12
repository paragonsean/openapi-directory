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

#include "OAIAddCoupons_200_response_paymentData_transactions_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddCoupons_200_response_paymentData_transactions_inner::OAIAddCoupons_200_response_paymentData_transactions_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddCoupons_200_response_paymentData_transactions_inner::OAIAddCoupons_200_response_paymentData_transactions_inner() {
    this->initializeModel();
}

OAIAddCoupons_200_response_paymentData_transactions_inner::~OAIAddCoupons_200_response_paymentData_transactions_inner() {}

void OAIAddCoupons_200_response_paymentData_transactions_inner::initializeModel() {

    m_is_active_isSet = false;
    m_is_active_isValid = false;

    m_merchant_name_isSet = false;
    m_merchant_name_isValid = false;

    m_payments_isSet = false;
    m_payments_isValid = false;

    m_shared_transaction_isSet = false;
    m_shared_transaction_isValid = false;

    m_transaction_id_isSet = false;
    m_transaction_id_isValid = false;
}

void OAIAddCoupons_200_response_paymentData_transactions_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddCoupons_200_response_paymentData_transactions_inner::fromJsonObject(QJsonObject json) {

    m_is_active_isValid = ::OpenAPI::fromJsonValue(m_is_active, json[QString("isActive")]);
    m_is_active_isSet = !json[QString("isActive")].isNull() && m_is_active_isValid;

    m_merchant_name_isValid = ::OpenAPI::fromJsonValue(m_merchant_name, json[QString("merchantName")]);
    m_merchant_name_isSet = !json[QString("merchantName")].isNull() && m_merchant_name_isValid;

    m_payments_isValid = ::OpenAPI::fromJsonValue(m_payments, json[QString("payments")]);
    m_payments_isSet = !json[QString("payments")].isNull() && m_payments_isValid;

    m_shared_transaction_isValid = ::OpenAPI::fromJsonValue(m_shared_transaction, json[QString("sharedTransaction")]);
    m_shared_transaction_isSet = !json[QString("sharedTransaction")].isNull() && m_shared_transaction_isValid;

    m_transaction_id_isValid = ::OpenAPI::fromJsonValue(m_transaction_id, json[QString("transactionId")]);
    m_transaction_id_isSet = !json[QString("transactionId")].isNull() && m_transaction_id_isValid;
}

QString OAIAddCoupons_200_response_paymentData_transactions_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddCoupons_200_response_paymentData_transactions_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_is_active_isSet) {
        obj.insert(QString("isActive"), ::OpenAPI::toJsonValue(m_is_active));
    }
    if (m_merchant_name_isSet) {
        obj.insert(QString("merchantName"), ::OpenAPI::toJsonValue(m_merchant_name));
    }
    if (m_payments.size() > 0) {
        obj.insert(QString("payments"), ::OpenAPI::toJsonValue(m_payments));
    }
    if (m_shared_transaction_isSet) {
        obj.insert(QString("sharedTransaction"), ::OpenAPI::toJsonValue(m_shared_transaction));
    }
    if (m_transaction_id_isSet) {
        obj.insert(QString("transactionId"), ::OpenAPI::toJsonValue(m_transaction_id));
    }
    return obj;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::isIsActive() const {
    return m_is_active;
}
void OAIAddCoupons_200_response_paymentData_transactions_inner::setIsActive(const bool &is_active) {
    m_is_active = is_active;
    m_is_active_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::is_is_active_Set() const{
    return m_is_active_isSet;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::is_is_active_Valid() const{
    return m_is_active_isValid;
}

QString OAIAddCoupons_200_response_paymentData_transactions_inner::getMerchantName() const {
    return m_merchant_name;
}
void OAIAddCoupons_200_response_paymentData_transactions_inner::setMerchantName(const QString &merchant_name) {
    m_merchant_name = merchant_name;
    m_merchant_name_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::is_merchant_name_Set() const{
    return m_merchant_name_isSet;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::is_merchant_name_Valid() const{
    return m_merchant_name_isValid;
}

QList<OAIAddCoupons_200_response_paymentData_transactions_inner_payments_inner> OAIAddCoupons_200_response_paymentData_transactions_inner::getPayments() const {
    return m_payments;
}
void OAIAddCoupons_200_response_paymentData_transactions_inner::setPayments(const QList<OAIAddCoupons_200_response_paymentData_transactions_inner_payments_inner> &payments) {
    m_payments = payments;
    m_payments_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::is_payments_Set() const{
    return m_payments_isSet;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::is_payments_Valid() const{
    return m_payments_isValid;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::isSharedTransaction() const {
    return m_shared_transaction;
}
void OAIAddCoupons_200_response_paymentData_transactions_inner::setSharedTransaction(const bool &shared_transaction) {
    m_shared_transaction = shared_transaction;
    m_shared_transaction_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::is_shared_transaction_Set() const{
    return m_shared_transaction_isSet;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::is_shared_transaction_Valid() const{
    return m_shared_transaction_isValid;
}

QString OAIAddCoupons_200_response_paymentData_transactions_inner::getTransactionId() const {
    return m_transaction_id;
}
void OAIAddCoupons_200_response_paymentData_transactions_inner::setTransactionId(const QString &transaction_id) {
    m_transaction_id = transaction_id;
    m_transaction_id_isSet = true;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::is_transaction_id_Set() const{
    return m_transaction_id_isSet;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::is_transaction_id_Valid() const{
    return m_transaction_id_isValid;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_is_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_shared_transaction_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddCoupons_200_response_paymentData_transactions_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
