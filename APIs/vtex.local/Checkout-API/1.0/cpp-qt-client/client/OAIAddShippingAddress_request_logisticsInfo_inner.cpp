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

#include "OAIAddShippingAddress_request_logisticsInfo_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddShippingAddress_request_logisticsInfo_inner::OAIAddShippingAddress_request_logisticsInfo_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddShippingAddress_request_logisticsInfo_inner::OAIAddShippingAddress_request_logisticsInfo_inner() {
    this->initializeModel();
}

OAIAddShippingAddress_request_logisticsInfo_inner::~OAIAddShippingAddress_request_logisticsInfo_inner() {}

void OAIAddShippingAddress_request_logisticsInfo_inner::initializeModel() {

    m_item_index_isSet = false;
    m_item_index_isValid = false;

    m_selected_delivery_channel_isSet = false;
    m_selected_delivery_channel_isValid = false;

    m_selected_sla_isSet = false;
    m_selected_sla_isValid = false;
}

void OAIAddShippingAddress_request_logisticsInfo_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddShippingAddress_request_logisticsInfo_inner::fromJsonObject(QJsonObject json) {

    m_item_index_isValid = ::OpenAPI::fromJsonValue(m_item_index, json[QString("itemIndex")]);
    m_item_index_isSet = !json[QString("itemIndex")].isNull() && m_item_index_isValid;

    m_selected_delivery_channel_isValid = ::OpenAPI::fromJsonValue(m_selected_delivery_channel, json[QString("selectedDeliveryChannel")]);
    m_selected_delivery_channel_isSet = !json[QString("selectedDeliveryChannel")].isNull() && m_selected_delivery_channel_isValid;

    m_selected_sla_isValid = ::OpenAPI::fromJsonValue(m_selected_sla, json[QString("selectedSla")]);
    m_selected_sla_isSet = !json[QString("selectedSla")].isNull() && m_selected_sla_isValid;
}

QString OAIAddShippingAddress_request_logisticsInfo_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddShippingAddress_request_logisticsInfo_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_item_index_isSet) {
        obj.insert(QString("itemIndex"), ::OpenAPI::toJsonValue(m_item_index));
    }
    if (m_selected_delivery_channel_isSet) {
        obj.insert(QString("selectedDeliveryChannel"), ::OpenAPI::toJsonValue(m_selected_delivery_channel));
    }
    if (m_selected_sla_isSet) {
        obj.insert(QString("selectedSla"), ::OpenAPI::toJsonValue(m_selected_sla));
    }
    return obj;
}

qint32 OAIAddShippingAddress_request_logisticsInfo_inner::getItemIndex() const {
    return m_item_index;
}
void OAIAddShippingAddress_request_logisticsInfo_inner::setItemIndex(const qint32 &item_index) {
    m_item_index = item_index;
    m_item_index_isSet = true;
}

bool OAIAddShippingAddress_request_logisticsInfo_inner::is_item_index_Set() const{
    return m_item_index_isSet;
}

bool OAIAddShippingAddress_request_logisticsInfo_inner::is_item_index_Valid() const{
    return m_item_index_isValid;
}

QString OAIAddShippingAddress_request_logisticsInfo_inner::getSelectedDeliveryChannel() const {
    return m_selected_delivery_channel;
}
void OAIAddShippingAddress_request_logisticsInfo_inner::setSelectedDeliveryChannel(const QString &selected_delivery_channel) {
    m_selected_delivery_channel = selected_delivery_channel;
    m_selected_delivery_channel_isSet = true;
}

bool OAIAddShippingAddress_request_logisticsInfo_inner::is_selected_delivery_channel_Set() const{
    return m_selected_delivery_channel_isSet;
}

bool OAIAddShippingAddress_request_logisticsInfo_inner::is_selected_delivery_channel_Valid() const{
    return m_selected_delivery_channel_isValid;
}

QString OAIAddShippingAddress_request_logisticsInfo_inner::getSelectedSla() const {
    return m_selected_sla;
}
void OAIAddShippingAddress_request_logisticsInfo_inner::setSelectedSla(const QString &selected_sla) {
    m_selected_sla = selected_sla;
    m_selected_sla_isSet = true;
}

bool OAIAddShippingAddress_request_logisticsInfo_inner::is_selected_sla_Set() const{
    return m_selected_sla_isSet;
}

bool OAIAddShippingAddress_request_logisticsInfo_inner::is_selected_sla_Valid() const{
    return m_selected_sla_isValid;
}

bool OAIAddShippingAddress_request_logisticsInfo_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_item_index_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_selected_delivery_channel_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_selected_sla_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddShippingAddress_request_logisticsInfo_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
