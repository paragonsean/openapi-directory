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

#include "OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner() {
    this->initializeModel();
}

OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::~OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner() {}

void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::initializeModel() {

    m_delivery_channel_isSet = false;
    m_delivery_channel_isValid = false;

    m_delivery_ids_isSet = false;
    m_delivery_ids_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_list_price_isSet = false;
    m_list_price_isValid = false;

    m_lock_ttl_isSet = false;
    m_lock_ttl_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_pickup_distance_isSet = false;
    m_pickup_distance_isValid = false;

    m_pickup_point_id_isSet = false;
    m_pickup_point_id_isValid = false;

    m_pickup_store_info_isSet = false;
    m_pickup_store_info_isValid = false;

    m_polygon_name_isSet = false;
    m_polygon_name_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_shipping_estimate_isSet = false;
    m_shipping_estimate_isValid = false;

    m_shipping_estimate_date_isSet = false;
    m_shipping_estimate_date_isValid = false;

    m_tax_isSet = false;
    m_tax_isValid = false;

    m_transit_time_isSet = false;
    m_transit_time_isValid = false;
}

void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::fromJsonObject(QJsonObject json) {

    m_delivery_channel_isValid = ::OpenAPI::fromJsonValue(m_delivery_channel, json[QString("deliveryChannel")]);
    m_delivery_channel_isSet = !json[QString("deliveryChannel")].isNull() && m_delivery_channel_isValid;

    m_delivery_ids_isValid = ::OpenAPI::fromJsonValue(m_delivery_ids, json[QString("deliveryIds")]);
    m_delivery_ids_isSet = !json[QString("deliveryIds")].isNull() && m_delivery_ids_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_list_price_isValid = ::OpenAPI::fromJsonValue(m_list_price, json[QString("listPrice")]);
    m_list_price_isSet = !json[QString("listPrice")].isNull() && m_list_price_isValid;

    m_lock_ttl_isValid = ::OpenAPI::fromJsonValue(m_lock_ttl, json[QString("lockTTL")]);
    m_lock_ttl_isSet = !json[QString("lockTTL")].isNull() && m_lock_ttl_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_pickup_distance_isValid = ::OpenAPI::fromJsonValue(m_pickup_distance, json[QString("pickupDistance")]);
    m_pickup_distance_isSet = !json[QString("pickupDistance")].isNull() && m_pickup_distance_isValid;

    m_pickup_point_id_isValid = ::OpenAPI::fromJsonValue(m_pickup_point_id, json[QString("pickupPointId")]);
    m_pickup_point_id_isSet = !json[QString("pickupPointId")].isNull() && m_pickup_point_id_isValid;

    m_pickup_store_info_isValid = ::OpenAPI::fromJsonValue(m_pickup_store_info, json[QString("pickupStoreInfo")]);
    m_pickup_store_info_isSet = !json[QString("pickupStoreInfo")].isNull() && m_pickup_store_info_isValid;

    m_polygon_name_isValid = ::OpenAPI::fromJsonValue(m_polygon_name, json[QString("polygonName")]);
    m_polygon_name_isSet = !json[QString("polygonName")].isNull() && m_polygon_name_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_shipping_estimate_isValid = ::OpenAPI::fromJsonValue(m_shipping_estimate, json[QString("shippingEstimate")]);
    m_shipping_estimate_isSet = !json[QString("shippingEstimate")].isNull() && m_shipping_estimate_isValid;

    m_shipping_estimate_date_isValid = ::OpenAPI::fromJsonValue(m_shipping_estimate_date, json[QString("shippingEstimateDate")]);
    m_shipping_estimate_date_isSet = !json[QString("shippingEstimateDate")].isNull() && m_shipping_estimate_date_isValid;

    m_tax_isValid = ::OpenAPI::fromJsonValue(m_tax, json[QString("tax")]);
    m_tax_isSet = !json[QString("tax")].isNull() && m_tax_isValid;

    m_transit_time_isValid = ::OpenAPI::fromJsonValue(m_transit_time, json[QString("transitTime")]);
    m_transit_time_isSet = !json[QString("transitTime")].isNull() && m_transit_time_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_delivery_channel_isSet) {
        obj.insert(QString("deliveryChannel"), ::OpenAPI::toJsonValue(m_delivery_channel));
    }
    if (m_delivery_ids.size() > 0) {
        obj.insert(QString("deliveryIds"), ::OpenAPI::toJsonValue(m_delivery_ids));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_list_price_isSet) {
        obj.insert(QString("listPrice"), ::OpenAPI::toJsonValue(m_list_price));
    }
    if (m_lock_ttl_isSet) {
        obj.insert(QString("lockTTL"), ::OpenAPI::toJsonValue(m_lock_ttl));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_pickup_distance_isSet) {
        obj.insert(QString("pickupDistance"), ::OpenAPI::toJsonValue(m_pickup_distance));
    }
    if (m_pickup_point_id_isSet) {
        obj.insert(QString("pickupPointId"), ::OpenAPI::toJsonValue(m_pickup_point_id));
    }
    if (m_pickup_store_info.isSet()) {
        obj.insert(QString("pickupStoreInfo"), ::OpenAPI::toJsonValue(m_pickup_store_info));
    }
    if (m_polygon_name_isSet) {
        obj.insert(QString("polygonName"), ::OpenAPI::toJsonValue(m_polygon_name));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_shipping_estimate_isSet) {
        obj.insert(QString("shippingEstimate"), ::OpenAPI::toJsonValue(m_shipping_estimate));
    }
    if (m_shipping_estimate_date_isSet) {
        obj.insert(QString("shippingEstimateDate"), ::OpenAPI::toJsonValue(m_shipping_estimate_date));
    }
    if (m_tax_isSet) {
        obj.insert(QString("tax"), ::OpenAPI::toJsonValue(m_tax));
    }
    if (m_transit_time_isSet) {
        obj.insert(QString("transitTime"), ::OpenAPI::toJsonValue(m_transit_time));
    }
    return obj;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getDeliveryChannel() const {
    return m_delivery_channel;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setDeliveryChannel(const QString &delivery_channel) {
    m_delivery_channel = delivery_channel;
    m_delivery_channel_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_delivery_channel_Set() const{
    return m_delivery_channel_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_delivery_channel_Valid() const{
    return m_delivery_channel_isValid;
}

QList<OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner> OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getDeliveryIds() const {
    return m_delivery_ids;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setDeliveryIds(const QList<OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner> &delivery_ids) {
    m_delivery_ids = delivery_ids;
    m_delivery_ids_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_delivery_ids_Set() const{
    return m_delivery_ids_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_delivery_ids_Valid() const{
    return m_delivery_ids_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getId() const {
    return m_id;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getListPrice() const {
    return m_list_price;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setListPrice(const qint32 &list_price) {
    m_list_price = list_price;
    m_list_price_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_list_price_Set() const{
    return m_list_price_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_list_price_Valid() const{
    return m_list_price_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getLockTtl() const {
    return m_lock_ttl;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setLockTtl(const QString &lock_ttl) {
    m_lock_ttl = lock_ttl;
    m_lock_ttl_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_lock_ttl_Set() const{
    return m_lock_ttl_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_lock_ttl_Valid() const{
    return m_lock_ttl_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getName() const {
    return m_name;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getPickupDistance() const {
    return m_pickup_distance;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setPickupDistance(const qint32 &pickup_distance) {
    m_pickup_distance = pickup_distance;
    m_pickup_distance_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_pickup_distance_Set() const{
    return m_pickup_distance_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_pickup_distance_Valid() const{
    return m_pickup_distance_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getPickupPointId() const {
    return m_pickup_point_id;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setPickupPointId(const QString &pickup_point_id) {
    m_pickup_point_id = pickup_point_id;
    m_pickup_point_id_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_pickup_point_id_Set() const{
    return m_pickup_point_id_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_pickup_point_id_Valid() const{
    return m_pickup_point_id_isValid;
}

OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getPickupStoreInfo() const {
    return m_pickup_store_info;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setPickupStoreInfo(const OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner_pickupStoreInfo &pickup_store_info) {
    m_pickup_store_info = pickup_store_info;
    m_pickup_store_info_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_pickup_store_info_Set() const{
    return m_pickup_store_info_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_pickup_store_info_Valid() const{
    return m_pickup_store_info_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getPolygonName() const {
    return m_polygon_name;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setPolygonName(const QString &polygon_name) {
    m_polygon_name = polygon_name;
    m_polygon_name_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_polygon_name_Set() const{
    return m_polygon_name_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_polygon_name_Valid() const{
    return m_polygon_name_isValid;
}

qint32 OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getPrice() const {
    return m_price;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setPrice(const qint32 &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_price_Set() const{
    return m_price_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_price_Valid() const{
    return m_price_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getShippingEstimate() const {
    return m_shipping_estimate;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setShippingEstimate(const QString &shipping_estimate) {
    m_shipping_estimate = shipping_estimate;
    m_shipping_estimate_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_shipping_estimate_Set() const{
    return m_shipping_estimate_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_shipping_estimate_Valid() const{
    return m_shipping_estimate_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getShippingEstimateDate() const {
    return m_shipping_estimate_date;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setShippingEstimateDate(const QString &shipping_estimate_date) {
    m_shipping_estimate_date = shipping_estimate_date;
    m_shipping_estimate_date_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_shipping_estimate_date_Set() const{
    return m_shipping_estimate_date_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_shipping_estimate_date_Valid() const{
    return m_shipping_estimate_date_isValid;
}

qint32 OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getTax() const {
    return m_tax;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setTax(const qint32 &tax) {
    m_tax = tax;
    m_tax_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_tax_Set() const{
    return m_tax_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_tax_Valid() const{
    return m_tax_isValid;
}

QString OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::getTransitTime() const {
    return m_transit_time;
}
void OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::setTransitTime(const QString &transit_time) {
    m_transit_time = transit_time;
    m_transit_time_isSet = true;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_transit_time_Set() const{
    return m_transit_time_isSet;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::is_transit_time_Valid() const{
    return m_transit_time_isValid;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_delivery_channel_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_delivery_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_list_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lock_ttl_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pickup_distance_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pickup_point_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pickup_store_info.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_polygon_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_estimate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_estimate_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transit_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIItemsUpdate_200_response_shippingData_logisticsInfo_inner_slas_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
