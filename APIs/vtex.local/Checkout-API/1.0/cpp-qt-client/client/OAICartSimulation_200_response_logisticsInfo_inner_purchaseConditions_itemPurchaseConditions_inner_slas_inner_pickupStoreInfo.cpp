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

#include "OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo() {
    this->initializeModel();
}

OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::~OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo() {}

void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::initializeModel() {

    m_additional_info_isSet = false;
    m_additional_info_isValid = false;

    m_address_isSet = false;
    m_address_isValid = false;

    m_dock_id_isSet = false;
    m_dock_id_isValid = false;

    m_friendly_name_isSet = false;
    m_friendly_name_isValid = false;

    m_is_pickup_store_isSet = false;
    m_is_pickup_store_isValid = false;
}

void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::fromJsonObject(QJsonObject json) {

    m_additional_info_isValid = ::OpenAPI::fromJsonValue(m_additional_info, json[QString("additionalInfo")]);
    m_additional_info_isSet = !json[QString("additionalInfo")].isNull() && m_additional_info_isValid;

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_dock_id_isValid = ::OpenAPI::fromJsonValue(m_dock_id, json[QString("dockId")]);
    m_dock_id_isSet = !json[QString("dockId")].isNull() && m_dock_id_isValid;

    m_friendly_name_isValid = ::OpenAPI::fromJsonValue(m_friendly_name, json[QString("friendlyName")]);
    m_friendly_name_isSet = !json[QString("friendlyName")].isNull() && m_friendly_name_isValid;

    m_is_pickup_store_isValid = ::OpenAPI::fromJsonValue(m_is_pickup_store, json[QString("isPickupStore")]);
    m_is_pickup_store_isSet = !json[QString("isPickupStore")].isNull() && m_is_pickup_store_isValid;
}

QString OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_additional_info_isSet) {
        obj.insert(QString("additionalInfo"), ::OpenAPI::toJsonValue(m_additional_info));
    }
    if (m_address_isSet) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_dock_id_isSet) {
        obj.insert(QString("dockId"), ::OpenAPI::toJsonValue(m_dock_id));
    }
    if (m_friendly_name_isSet) {
        obj.insert(QString("friendlyName"), ::OpenAPI::toJsonValue(m_friendly_name));
    }
    if (m_is_pickup_store_isSet) {
        obj.insert(QString("isPickupStore"), ::OpenAPI::toJsonValue(m_is_pickup_store));
    }
    return obj;
}

QString OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::getAdditionalInfo() const {
    return m_additional_info;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::setAdditionalInfo(const QString &additional_info) {
    m_additional_info = additional_info;
    m_additional_info_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::is_additional_info_Set() const{
    return m_additional_info_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::is_additional_info_Valid() const{
    return m_additional_info_isValid;
}

OAIObject OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::getAddress() const {
    return m_address;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::setAddress(const OAIObject &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::is_address_Set() const{
    return m_address_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::is_address_Valid() const{
    return m_address_isValid;
}

QString OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::getDockId() const {
    return m_dock_id;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::setDockId(const QString &dock_id) {
    m_dock_id = dock_id;
    m_dock_id_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::is_dock_id_Set() const{
    return m_dock_id_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::is_dock_id_Valid() const{
    return m_dock_id_isValid;
}

QString OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::getFriendlyName() const {
    return m_friendly_name;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::setFriendlyName(const QString &friendly_name) {
    m_friendly_name = friendly_name;
    m_friendly_name_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::is_friendly_name_Set() const{
    return m_friendly_name_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::is_friendly_name_Valid() const{
    return m_friendly_name_isValid;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::isIsPickupStore() const {
    return m_is_pickup_store;
}
void OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::setIsPickupStore(const bool &is_pickup_store) {
    m_is_pickup_store = is_pickup_store;
    m_is_pickup_store_isSet = true;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::is_is_pickup_store_Set() const{
    return m_is_pickup_store_isSet;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::is_is_pickup_store_Valid() const{
    return m_is_pickup_store_isValid;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_additional_info_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dock_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_friendly_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_pickup_store_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICartSimulation_200_response_logisticsInfo_inner_purchaseConditions_itemPurchaseConditions_inner_slas_inner_pickupStoreInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
