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

#include "OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner() {
    this->initializeModel();
}

OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::~OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner() {}

void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_list_price_isSet = false;
    m_list_price_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_seller_isSet = false;
    m_seller_isValid = false;

    m_seller_chain_isSet = false;
    m_seller_chain_isValid = false;

    m_slas_isSet = false;
    m_slas_isValid = false;
}

void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_list_price_isValid = ::OpenAPI::fromJsonValue(m_list_price, json[QString("listPrice")]);
    m_list_price_isSet = !json[QString("listPrice")].isNull() && m_list_price_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_seller_isValid = ::OpenAPI::fromJsonValue(m_seller, json[QString("seller")]);
    m_seller_isSet = !json[QString("seller")].isNull() && m_seller_isValid;

    m_seller_chain_isValid = ::OpenAPI::fromJsonValue(m_seller_chain, json[QString("sellerChain")]);
    m_seller_chain_isSet = !json[QString("sellerChain")].isNull() && m_seller_chain_isValid;

    m_slas_isValid = ::OpenAPI::fromJsonValue(m_slas, json[QString("slas")]);
    m_slas_isSet = !json[QString("slas")].isNull() && m_slas_isValid;
}

QString OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_list_price_isSet) {
        obj.insert(QString("listPrice"), ::OpenAPI::toJsonValue(m_list_price));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_seller_isSet) {
        obj.insert(QString("seller"), ::OpenAPI::toJsonValue(m_seller));
    }
    if (m_seller_chain.size() > 0) {
        obj.insert(QString("sellerChain"), ::OpenAPI::toJsonValue(m_seller_chain));
    }
    if (m_slas.size() > 0) {
        obj.insert(QString("slas"), ::OpenAPI::toJsonValue(m_slas));
    }
    return obj;
}

QString OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::getId() const {
    return m_id;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::getListPrice() const {
    return m_list_price;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::setListPrice(const qint32 &list_price) {
    m_list_price = list_price;
    m_list_price_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_list_price_Set() const{
    return m_list_price_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_list_price_Valid() const{
    return m_list_price_isValid;
}

qint32 OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::getPrice() const {
    return m_price;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::setPrice(const qint32 &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_price_Set() const{
    return m_price_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_price_Valid() const{
    return m_price_isValid;
}

QString OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::getSeller() const {
    return m_seller;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::setSeller(const QString &seller) {
    m_seller = seller;
    m_seller_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_seller_Set() const{
    return m_seller_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_seller_Valid() const{
    return m_seller_isValid;
}

QList<QJsonValue> OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::getSellerChain() const {
    return m_seller_chain;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::setSellerChain(const QList<QJsonValue> &seller_chain) {
    m_seller_chain = seller_chain;
    m_seller_chain_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_seller_chain_Set() const{
    return m_seller_chain_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_seller_chain_Valid() const{
    return m_seller_chain_isValid;
}

QList<OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner> OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::getSlas() const {
    return m_slas;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::setSlas(const QList<OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner> &slas) {
    m_slas = slas;
    m_slas_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_slas_Set() const{
    return m_slas_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::is_slas_Valid() const{
    return m_slas_isValid;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_list_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller_chain.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_slas.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
