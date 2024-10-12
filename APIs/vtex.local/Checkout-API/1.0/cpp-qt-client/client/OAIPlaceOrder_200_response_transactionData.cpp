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

#include "OAIPlaceOrder_200_response_transactionData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaceOrder_200_response_transactionData::OAIPlaceOrder_200_response_transactionData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaceOrder_200_response_transactionData::OAIPlaceOrder_200_response_transactionData() {
    this->initializeModel();
}

OAIPlaceOrder_200_response_transactionData::~OAIPlaceOrder_200_response_transactionData() {}

void OAIPlaceOrder_200_response_transactionData::initializeModel() {

    m_gateway_callback_template_path_isSet = false;
    m_gateway_callback_template_path_isValid = false;

    m_merchant_transactions_isSet = false;
    m_merchant_transactions_isValid = false;

    m_receiver_uri_isSet = false;
    m_receiver_uri_isValid = false;
}

void OAIPlaceOrder_200_response_transactionData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaceOrder_200_response_transactionData::fromJsonObject(QJsonObject json) {

    m_gateway_callback_template_path_isValid = ::OpenAPI::fromJsonValue(m_gateway_callback_template_path, json[QString("gatewayCallbackTemplatePath")]);
    m_gateway_callback_template_path_isSet = !json[QString("gatewayCallbackTemplatePath")].isNull() && m_gateway_callback_template_path_isValid;

    m_merchant_transactions_isValid = ::OpenAPI::fromJsonValue(m_merchant_transactions, json[QString("merchantTransactions")]);
    m_merchant_transactions_isSet = !json[QString("merchantTransactions")].isNull() && m_merchant_transactions_isValid;

    m_receiver_uri_isValid = ::OpenAPI::fromJsonValue(m_receiver_uri, json[QString("receiverUri")]);
    m_receiver_uri_isSet = !json[QString("receiverUri")].isNull() && m_receiver_uri_isValid;
}

QString OAIPlaceOrder_200_response_transactionData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaceOrder_200_response_transactionData::asJsonObject() const {
    QJsonObject obj;
    if (m_gateway_callback_template_path_isSet) {
        obj.insert(QString("gatewayCallbackTemplatePath"), ::OpenAPI::toJsonValue(m_gateway_callback_template_path));
    }
    if (m_merchant_transactions.size() > 0) {
        obj.insert(QString("merchantTransactions"), ::OpenAPI::toJsonValue(m_merchant_transactions));
    }
    if (m_receiver_uri_isSet) {
        obj.insert(QString("receiverUri"), ::OpenAPI::toJsonValue(m_receiver_uri));
    }
    return obj;
}

QString OAIPlaceOrder_200_response_transactionData::getGatewayCallbackTemplatePath() const {
    return m_gateway_callback_template_path;
}
void OAIPlaceOrder_200_response_transactionData::setGatewayCallbackTemplatePath(const QString &gateway_callback_template_path) {
    m_gateway_callback_template_path = gateway_callback_template_path;
    m_gateway_callback_template_path_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData::is_gateway_callback_template_path_Set() const{
    return m_gateway_callback_template_path_isSet;
}

bool OAIPlaceOrder_200_response_transactionData::is_gateway_callback_template_path_Valid() const{
    return m_gateway_callback_template_path_isValid;
}

QList<OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner> OAIPlaceOrder_200_response_transactionData::getMerchantTransactions() const {
    return m_merchant_transactions;
}
void OAIPlaceOrder_200_response_transactionData::setMerchantTransactions(const QList<OAIPlaceOrder_200_response_transactionData_merchantTransactions_inner> &merchant_transactions) {
    m_merchant_transactions = merchant_transactions;
    m_merchant_transactions_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData::is_merchant_transactions_Set() const{
    return m_merchant_transactions_isSet;
}

bool OAIPlaceOrder_200_response_transactionData::is_merchant_transactions_Valid() const{
    return m_merchant_transactions_isValid;
}

QString OAIPlaceOrder_200_response_transactionData::getReceiverUri() const {
    return m_receiver_uri;
}
void OAIPlaceOrder_200_response_transactionData::setReceiverUri(const QString &receiver_uri) {
    m_receiver_uri = receiver_uri;
    m_receiver_uri_isSet = true;
}

bool OAIPlaceOrder_200_response_transactionData::is_receiver_uri_Set() const{
    return m_receiver_uri_isSet;
}

bool OAIPlaceOrder_200_response_transactionData::is_receiver_uri_Valid() const{
    return m_receiver_uri_isValid;
}

bool OAIPlaceOrder_200_response_transactionData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_gateway_callback_template_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_merchant_transactions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_receiver_uri_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlaceOrder_200_response_transactionData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
