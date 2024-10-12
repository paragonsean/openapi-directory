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

#include "OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner() {
    this->initializeModel();
}

OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::~OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner() {}

void OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::initializeModel() {

    m_courier_id_isSet = false;
    m_courier_id_isValid = false;

    m_courier_name_isSet = false;
    m_courier_name_isValid = false;

    m_dock_id_isSet = false;
    m_dock_id_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_warehouse_id_isSet = false;
    m_warehouse_id_isValid = false;
}

void OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::fromJsonObject(QJsonObject json) {

    m_courier_id_isValid = ::OpenAPI::fromJsonValue(m_courier_id, json[QString("courierId")]);
    m_courier_id_isSet = !json[QString("courierId")].isNull() && m_courier_id_isValid;

    m_courier_name_isValid = ::OpenAPI::fromJsonValue(m_courier_name, json[QString("courierName")]);
    m_courier_name_isSet = !json[QString("courierName")].isNull() && m_courier_name_isValid;

    m_dock_id_isValid = ::OpenAPI::fromJsonValue(m_dock_id, json[QString("dockId")]);
    m_dock_id_isSet = !json[QString("dockId")].isNull() && m_dock_id_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_warehouse_id_isValid = ::OpenAPI::fromJsonValue(m_warehouse_id, json[QString("warehouseId")]);
    m_warehouse_id_isSet = !json[QString("warehouseId")].isNull() && m_warehouse_id_isValid;
}

QString OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_courier_id_isSet) {
        obj.insert(QString("courierId"), ::OpenAPI::toJsonValue(m_courier_id));
    }
    if (m_courier_name_isSet) {
        obj.insert(QString("courierName"), ::OpenAPI::toJsonValue(m_courier_name));
    }
    if (m_dock_id_isSet) {
        obj.insert(QString("dockId"), ::OpenAPI::toJsonValue(m_dock_id));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_warehouse_id_isSet) {
        obj.insert(QString("warehouseId"), ::OpenAPI::toJsonValue(m_warehouse_id));
    }
    return obj;
}

QString OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::getCourierId() const {
    return m_courier_id;
}
void OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::setCourierId(const QString &courier_id) {
    m_courier_id = courier_id;
    m_courier_id_isSet = true;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::is_courier_id_Set() const{
    return m_courier_id_isSet;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::is_courier_id_Valid() const{
    return m_courier_id_isValid;
}

QString OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::getCourierName() const {
    return m_courier_name;
}
void OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::setCourierName(const QString &courier_name) {
    m_courier_name = courier_name;
    m_courier_name_isSet = true;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::is_courier_name_Set() const{
    return m_courier_name_isSet;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::is_courier_name_Valid() const{
    return m_courier_name_isValid;
}

QString OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::getDockId() const {
    return m_dock_id;
}
void OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::setDockId(const QString &dock_id) {
    m_dock_id = dock_id;
    m_dock_id_isSet = true;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::is_dock_id_Set() const{
    return m_dock_id_isSet;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::is_dock_id_Valid() const{
    return m_dock_id_isValid;
}

qint32 OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::getQuantity() const {
    return m_quantity;
}
void OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::setQuantity(const qint32 &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::is_quantity_Valid() const{
    return m_quantity_isValid;
}

QString OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::getWarehouseId() const {
    return m_warehouse_id;
}
void OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::setWarehouseId(const QString &warehouse_id) {
    m_warehouse_id = warehouse_id;
    m_warehouse_id_isSet = true;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::is_warehouse_id_Set() const{
    return m_warehouse_id_isSet;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::is_warehouse_id_Valid() const{
    return m_warehouse_id_isValid;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_courier_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_courier_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dock_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_warehouse_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddCoupons_200_response_shippingData_logisticsInfo_inner_slas_inner_deliveryIds_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
