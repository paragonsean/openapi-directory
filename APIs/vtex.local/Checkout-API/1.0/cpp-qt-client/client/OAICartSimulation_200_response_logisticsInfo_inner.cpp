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

#include "OAICartSimulation_200_response_logisticsInfo_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICartSimulation_200_response_logisticsInfo_inner::OAICartSimulation_200_response_logisticsInfo_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICartSimulation_200_response_logisticsInfo_inner::OAICartSimulation_200_response_logisticsInfo_inner() {
    this->initializeModel();
}

OAICartSimulation_200_response_logisticsInfo_inner::~OAICartSimulation_200_response_logisticsInfo_inner() {}

void OAICartSimulation_200_response_logisticsInfo_inner::initializeModel() {

    m_address_id_isSet = false;
    m_address_id_isValid = false;

    m_delivery_channels_isSet = false;
    m_delivery_channels_isValid = false;

    m_item_index_isSet = false;
    m_item_index_isValid = false;

    m_item_metadata_isSet = false;
    m_item_metadata_isValid = false;

    m_messages_isSet = false;
    m_messages_isValid = false;

    m_pickup_points_isSet = false;
    m_pickup_points_isValid = false;

    m_purchase_conditions_isSet = false;
    m_purchase_conditions_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_selected_delivery_channel_isSet = false;
    m_selected_delivery_channel_isValid = false;

    m_selected_sla_isSet = false;
    m_selected_sla_isValid = false;

    m_ships_to_isSet = false;
    m_ships_to_isValid = false;

    m_slas_isSet = false;
    m_slas_isValid = false;

    m_subscription_data_isSet = false;
    m_subscription_data_isValid = false;

    m_totals_isSet = false;
    m_totals_isValid = false;
}

void OAICartSimulation_200_response_logisticsInfo_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICartSimulation_200_response_logisticsInfo_inner::fromJsonObject(QJsonObject json) {

    m_address_id_isValid = ::OpenAPI::fromJsonValue(m_address_id, json[QString("addressId")]);
    m_address_id_isSet = !json[QString("addressId")].isNull() && m_address_id_isValid;

    m_delivery_channels_isValid = ::OpenAPI::fromJsonValue(m_delivery_channels, json[QString("deliveryChannels")]);
    m_delivery_channels_isSet = !json[QString("deliveryChannels")].isNull() && m_delivery_channels_isValid;

    m_item_index_isValid = ::OpenAPI::fromJsonValue(m_item_index, json[QString("itemIndex")]);
    m_item_index_isSet = !json[QString("itemIndex")].isNull() && m_item_index_isValid;

    m_item_metadata_isValid = ::OpenAPI::fromJsonValue(m_item_metadata, json[QString("itemMetadata")]);
    m_item_metadata_isSet = !json[QString("itemMetadata")].isNull() && m_item_metadata_isValid;

    m_messages_isValid = ::OpenAPI::fromJsonValue(m_messages, json[QString("messages")]);
    m_messages_isSet = !json[QString("messages")].isNull() && m_messages_isValid;

    m_pickup_points_isValid = ::OpenAPI::fromJsonValue(m_pickup_points, json[QString("pickupPoints")]);
    m_pickup_points_isSet = !json[QString("pickupPoints")].isNull() && m_pickup_points_isValid;

    m_purchase_conditions_isValid = ::OpenAPI::fromJsonValue(m_purchase_conditions, json[QString("purchaseConditions")]);
    m_purchase_conditions_isSet = !json[QString("purchaseConditions")].isNull() && m_purchase_conditions_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_selected_delivery_channel_isValid = ::OpenAPI::fromJsonValue(m_selected_delivery_channel, json[QString("selectedDeliveryChannel")]);
    m_selected_delivery_channel_isSet = !json[QString("selectedDeliveryChannel")].isNull() && m_selected_delivery_channel_isValid;

    m_selected_sla_isValid = ::OpenAPI::fromJsonValue(m_selected_sla, json[QString("selectedSla")]);
    m_selected_sla_isSet = !json[QString("selectedSla")].isNull() && m_selected_sla_isValid;

    m_ships_to_isValid = ::OpenAPI::fromJsonValue(m_ships_to, json[QString("shipsTo")]);
    m_ships_to_isSet = !json[QString("shipsTo")].isNull() && m_ships_to_isValid;

    m_slas_isValid = ::OpenAPI::fromJsonValue(m_slas, json[QString("slas")]);
    m_slas_isSet = !json[QString("slas")].isNull() && m_slas_isValid;

    m_subscription_data_isValid = ::OpenAPI::fromJsonValue(m_subscription_data, json[QString("subscriptionData")]);
    m_subscription_data_isSet = !json[QString("subscriptionData")].isNull() && m_subscription_data_isValid;

    m_totals_isValid = ::OpenAPI::fromJsonValue(m_totals, json[QString("totals")]);
    m_totals_isSet = !json[QString("totals")].isNull() && m_totals_isValid;
}

QString OAICartSimulation_200_response_logisticsInfo_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICartSimulation_200_response_logisticsInfo_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_address_id_isSet) {
        obj.insert(QString("addressId"), ::OpenAPI::toJsonValue(m_address_id));
    }
    if (m_delivery_channels.size() > 0) {
        obj.insert(QString("deliveryChannels"), ::OpenAPI::toJsonValue(m_delivery_channels));
    }
    if (m_item_index_isSet) {
        obj.insert(QString("itemIndex"), ::OpenAPI::toJsonValue(m_item_index));
    }
    if (m_item_metadata.isSet()) {
        obj.insert(QString("itemMetadata"), ::OpenAPI::toJsonValue(m_item_metadata));
    }
    if (m_messages.size() > 0) {
        obj.insert(QString("messages"), ::OpenAPI::toJsonValue(m_messages));
    }
    if (m_pickup_points.size() > 0) {
        obj.insert(QString("pickupPoints"), ::OpenAPI::toJsonValue(m_pickup_points));
    }
    if (m_purchase_conditions.isSet()) {
        obj.insert(QString("purchaseConditions"), ::OpenAPI::toJsonValue(m_purchase_conditions));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_selected_delivery_channel_isSet) {
        obj.insert(QString("selectedDeliveryChannel"), ::OpenAPI::toJsonValue(m_selected_delivery_channel));
    }
    if (m_selected_sla_isSet) {
        obj.insert(QString("selectedSla"), ::OpenAPI::toJsonValue(m_selected_sla));
    }
    if (m_ships_to.size() > 0) {
        obj.insert(QString("shipsTo"), ::OpenAPI::toJsonValue(m_ships_to));
    }
    if (m_slas.size() > 0) {
        obj.insert(QString("slas"), ::OpenAPI::toJsonValue(m_slas));
    }
    if (m_subscription_data_isSet) {
        obj.insert(QString("subscriptionData"), ::OpenAPI::toJsonValue(m_subscription_data));
    }
    if (m_totals.size() > 0) {
        obj.insert(QString("totals"), ::OpenAPI::toJsonValue(m_totals));
    }
    return obj;
}

QString OAICartSimulation_200_response_logisticsInfo_inner::getAddressId() const {
    return m_address_id;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setAddressId(const QString &address_id) {
    m_address_id = address_id;
    m_address_id_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_address_id_Set() const{
    return m_address_id_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_address_id_Valid() const{
    return m_address_id_isValid;
}

QList<OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_deliveryChannels_inner> OAICartSimulation_200_response_logisticsInfo_inner::getDeliveryChannels() const {
    return m_delivery_channels;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setDeliveryChannels(const QList<OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_deliveryChannels_inner> &delivery_channels) {
    m_delivery_channels = delivery_channels;
    m_delivery_channels_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_delivery_channels_Set() const{
    return m_delivery_channels_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_delivery_channels_Valid() const{
    return m_delivery_channels_isValid;
}

qint32 OAICartSimulation_200_response_logisticsInfo_inner::getItemIndex() const {
    return m_item_index;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setItemIndex(const qint32 &item_index) {
    m_item_index = item_index;
    m_item_index_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_item_index_Set() const{
    return m_item_index_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_item_index_Valid() const{
    return m_item_index_isValid;
}

OAICartSimulation_200_response_logisticsInfo_inner_itemMetadata OAICartSimulation_200_response_logisticsInfo_inner::getItemMetadata() const {
    return m_item_metadata;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setItemMetadata(const OAICartSimulation_200_response_logisticsInfo_inner_itemMetadata &item_metadata) {
    m_item_metadata = item_metadata;
    m_item_metadata_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_item_metadata_Set() const{
    return m_item_metadata_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_item_metadata_Valid() const{
    return m_item_metadata_isValid;
}

QList<QJsonValue> OAICartSimulation_200_response_logisticsInfo_inner::getMessages() const {
    return m_messages;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setMessages(const QList<QJsonValue> &messages) {
    m_messages = messages;
    m_messages_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_messages_Set() const{
    return m_messages_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_messages_Valid() const{
    return m_messages_isValid;
}

QList<QJsonValue> OAICartSimulation_200_response_logisticsInfo_inner::getPickupPoints() const {
    return m_pickup_points;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setPickupPoints(const QList<QJsonValue> &pickup_points) {
    m_pickup_points = pickup_points;
    m_pickup_points_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_pickup_points_Set() const{
    return m_pickup_points_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_pickup_points_Valid() const{
    return m_pickup_points_isValid;
}

OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions OAICartSimulation_200_response_logisticsInfo_inner::getPurchaseConditions() const {
    return m_purchase_conditions;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setPurchaseConditions(const OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions &purchase_conditions) {
    m_purchase_conditions = purchase_conditions;
    m_purchase_conditions_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_purchase_conditions_Set() const{
    return m_purchase_conditions_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_purchase_conditions_Valid() const{
    return m_purchase_conditions_isValid;
}

qint32 OAICartSimulation_200_response_logisticsInfo_inner::getQuantity() const {
    return m_quantity;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setQuantity(const qint32 &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_quantity_Valid() const{
    return m_quantity_isValid;
}

QString OAICartSimulation_200_response_logisticsInfo_inner::getSelectedDeliveryChannel() const {
    return m_selected_delivery_channel;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setSelectedDeliveryChannel(const QString &selected_delivery_channel) {
    m_selected_delivery_channel = selected_delivery_channel;
    m_selected_delivery_channel_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_selected_delivery_channel_Set() const{
    return m_selected_delivery_channel_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_selected_delivery_channel_Valid() const{
    return m_selected_delivery_channel_isValid;
}

QString OAICartSimulation_200_response_logisticsInfo_inner::getSelectedSla() const {
    return m_selected_sla;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setSelectedSla(const QString &selected_sla) {
    m_selected_sla = selected_sla;
    m_selected_sla_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_selected_sla_Set() const{
    return m_selected_sla_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_selected_sla_Valid() const{
    return m_selected_sla_isValid;
}

QList<QJsonValue> OAICartSimulation_200_response_logisticsInfo_inner::getShipsTo() const {
    return m_ships_to;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setShipsTo(const QList<QJsonValue> &ships_to) {
    m_ships_to = ships_to;
    m_ships_to_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_ships_to_Set() const{
    return m_ships_to_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_ships_to_Valid() const{
    return m_ships_to_isValid;
}

QList<OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner> OAICartSimulation_200_response_logisticsInfo_inner::getSlas() const {
    return m_slas;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setSlas(const QList<OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner> &slas) {
    m_slas = slas;
    m_slas_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_slas_Set() const{
    return m_slas_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_slas_Valid() const{
    return m_slas_isValid;
}

OAIObject OAICartSimulation_200_response_logisticsInfo_inner::getSubscriptionData() const {
    return m_subscription_data;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setSubscriptionData(const OAIObject &subscription_data) {
    m_subscription_data = subscription_data;
    m_subscription_data_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_subscription_data_Set() const{
    return m_subscription_data_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_subscription_data_Valid() const{
    return m_subscription_data_isValid;
}

QList<OAICartSimulation_200_response_logisticsInfo_inner_totals_inner> OAICartSimulation_200_response_logisticsInfo_inner::getTotals() const {
    return m_totals;
}
void OAICartSimulation_200_response_logisticsInfo_inner::setTotals(const QList<OAICartSimulation_200_response_logisticsInfo_inner_totals_inner> &totals) {
    m_totals = totals;
    m_totals_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_totals_Set() const{
    return m_totals_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::is_totals_Valid() const{
    return m_totals_isValid;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_delivery_channels.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_item_index_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_item_metadata.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_messages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_pickup_points.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_purchase_conditions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
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

        if (m_ships_to.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_slas.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_subscription_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_totals.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICartSimulation_200_response_logisticsInfo_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
