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

#include "OAIItems_request_orderItems_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIItems_request_orderItems_inner::OAIItems_request_orderItems_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIItems_request_orderItems_inner::OAIItems_request_orderItems_inner() {
    this->initializeModel();
}

OAIItems_request_orderItems_inner::~OAIItems_request_orderItems_inner() {}

void OAIItems_request_orderItems_inner::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_index_isSet = false;
    m_index_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_seller_isSet = false;
    m_seller_isValid = false;
}

void OAIItems_request_orderItems_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIItems_request_orderItems_inner::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_index_isValid = ::OpenAPI::fromJsonValue(m_index, json[QString("index")]);
    m_index_isSet = !json[QString("index")].isNull() && m_index_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_seller_isValid = ::OpenAPI::fromJsonValue(m_seller, json[QString("seller")]);
    m_seller_isSet = !json[QString("seller")].isNull() && m_seller_isValid;
}

QString OAIItems_request_orderItems_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIItems_request_orderItems_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_index_isSet) {
        obj.insert(QString("index"), ::OpenAPI::toJsonValue(m_index));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_seller_isSet) {
        obj.insert(QString("seller"), ::OpenAPI::toJsonValue(m_seller));
    }
    return obj;
}

QString OAIItems_request_orderItems_inner::getId() const {
    return m_id;
}
void OAIItems_request_orderItems_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIItems_request_orderItems_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIItems_request_orderItems_inner::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIItems_request_orderItems_inner::getIndex() const {
    return m_index;
}
void OAIItems_request_orderItems_inner::setIndex(const qint32 &index) {
    m_index = index;
    m_index_isSet = true;
}

bool OAIItems_request_orderItems_inner::is_index_Set() const{
    return m_index_isSet;
}

bool OAIItems_request_orderItems_inner::is_index_Valid() const{
    return m_index_isValid;
}

qint32 OAIItems_request_orderItems_inner::getPrice() const {
    return m_price;
}
void OAIItems_request_orderItems_inner::setPrice(const qint32 &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIItems_request_orderItems_inner::is_price_Set() const{
    return m_price_isSet;
}

bool OAIItems_request_orderItems_inner::is_price_Valid() const{
    return m_price_isValid;
}

qint32 OAIItems_request_orderItems_inner::getQuantity() const {
    return m_quantity;
}
void OAIItems_request_orderItems_inner::setQuantity(const qint32 &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIItems_request_orderItems_inner::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIItems_request_orderItems_inner::is_quantity_Valid() const{
    return m_quantity_isValid;
}

QString OAIItems_request_orderItems_inner::getSeller() const {
    return m_seller;
}
void OAIItems_request_orderItems_inner::setSeller(const QString &seller) {
    m_seller = seller;
    m_seller_isSet = true;
}

bool OAIItems_request_orderItems_inner::is_seller_Set() const{
    return m_seller_isSet;
}

bool OAIItems_request_orderItems_inner::is_seller_Valid() const{
    return m_seller_isValid;
}

bool OAIItems_request_orderItems_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_index_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIItems_request_orderItems_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_index_isValid && m_quantity_isValid && m_seller_isValid && true;
}

} // namespace OpenAPI
