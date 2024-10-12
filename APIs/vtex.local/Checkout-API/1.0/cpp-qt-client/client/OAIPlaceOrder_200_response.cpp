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

#include "OAIPlaceOrder_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaceOrder_200_response::OAIPlaceOrder_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaceOrder_200_response::OAIPlaceOrder_200_response() {
    this->initializeModel();
}

OAIPlaceOrder_200_response::~OAIPlaceOrder_200_response() {}

void OAIPlaceOrder_200_response::initializeModel() {

    m_order_form_isSet = false;
    m_order_form_isValid = false;

    m_orders_isSet = false;
    m_orders_isValid = false;

    m_transaction_data_isSet = false;
    m_transaction_data_isValid = false;
}

void OAIPlaceOrder_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaceOrder_200_response::fromJsonObject(QJsonObject json) {

    m_order_form_isValid = ::OpenAPI::fromJsonValue(m_order_form, json[QString("orderForm")]);
    m_order_form_isSet = !json[QString("orderForm")].isNull() && m_order_form_isValid;

    m_orders_isValid = ::OpenAPI::fromJsonValue(m_orders, json[QString("orders")]);
    m_orders_isSet = !json[QString("orders")].isNull() && m_orders_isValid;

    m_transaction_data_isValid = ::OpenAPI::fromJsonValue(m_transaction_data, json[QString("transactionData")]);
    m_transaction_data_isSet = !json[QString("transactionData")].isNull() && m_transaction_data_isValid;
}

QString OAIPlaceOrder_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaceOrder_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_order_form_isSet) {
        obj.insert(QString("orderForm"), ::OpenAPI::toJsonValue(m_order_form));
    }
    if (m_orders.size() > 0) {
        obj.insert(QString("orders"), ::OpenAPI::toJsonValue(m_orders));
    }
    if (m_transaction_data.isSet()) {
        obj.insert(QString("transactionData"), ::OpenAPI::toJsonValue(m_transaction_data));
    }
    return obj;
}

QString OAIPlaceOrder_200_response::getOrderForm() const {
    return m_order_form;
}
void OAIPlaceOrder_200_response::setOrderForm(const QString &order_form) {
    m_order_form = order_form;
    m_order_form_isSet = true;
}

bool OAIPlaceOrder_200_response::is_order_form_Set() const{
    return m_order_form_isSet;
}

bool OAIPlaceOrder_200_response::is_order_form_Valid() const{
    return m_order_form_isValid;
}

QList<OAIPlaceOrder_200_response_orders_inner> OAIPlaceOrder_200_response::getOrders() const {
    return m_orders;
}
void OAIPlaceOrder_200_response::setOrders(const QList<OAIPlaceOrder_200_response_orders_inner> &orders) {
    m_orders = orders;
    m_orders_isSet = true;
}

bool OAIPlaceOrder_200_response::is_orders_Set() const{
    return m_orders_isSet;
}

bool OAIPlaceOrder_200_response::is_orders_Valid() const{
    return m_orders_isValid;
}

OAIPlaceOrder_200_response_transactionData OAIPlaceOrder_200_response::getTransactionData() const {
    return m_transaction_data;
}
void OAIPlaceOrder_200_response::setTransactionData(const OAIPlaceOrder_200_response_transactionData &transaction_data) {
    m_transaction_data = transaction_data;
    m_transaction_data_isSet = true;
}

bool OAIPlaceOrder_200_response::is_transaction_data_Set() const{
    return m_transaction_data_isSet;
}

bool OAIPlaceOrder_200_response::is_transaction_data_Valid() const{
    return m_transaction_data_isValid;
}

bool OAIPlaceOrder_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_order_form_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_orders.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_data.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlaceOrder_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
