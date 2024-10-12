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

#include "OAIAddCoupons_200_response_items_inner_additionalInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddCoupons_200_response_items_inner_additionalInfo::OAIAddCoupons_200_response_items_inner_additionalInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddCoupons_200_response_items_inner_additionalInfo::OAIAddCoupons_200_response_items_inner_additionalInfo() {
    this->initializeModel();
}

OAIAddCoupons_200_response_items_inner_additionalInfo::~OAIAddCoupons_200_response_items_inner_additionalInfo() {}

void OAIAddCoupons_200_response_items_inner_additionalInfo::initializeModel() {

    m_brand_id_isSet = false;
    m_brand_id_isValid = false;

    m_brand_name_isSet = false;
    m_brand_name_isValid = false;

    m_dimension_isSet = false;
    m_dimension_isValid = false;

    m_offering_info_isSet = false;
    m_offering_info_isValid = false;

    m_offering_type_isSet = false;
    m_offering_type_isValid = false;

    m_offering_type_id_isSet = false;
    m_offering_type_id_isValid = false;
}

void OAIAddCoupons_200_response_items_inner_additionalInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddCoupons_200_response_items_inner_additionalInfo::fromJsonObject(QJsonObject json) {

    m_brand_id_isValid = ::OpenAPI::fromJsonValue(m_brand_id, json[QString("brandId")]);
    m_brand_id_isSet = !json[QString("brandId")].isNull() && m_brand_id_isValid;

    m_brand_name_isValid = ::OpenAPI::fromJsonValue(m_brand_name, json[QString("brandName")]);
    m_brand_name_isSet = !json[QString("brandName")].isNull() && m_brand_name_isValid;

    m_dimension_isValid = ::OpenAPI::fromJsonValue(m_dimension, json[QString("dimension")]);
    m_dimension_isSet = !json[QString("dimension")].isNull() && m_dimension_isValid;

    m_offering_info_isValid = ::OpenAPI::fromJsonValue(m_offering_info, json[QString("offeringInfo")]);
    m_offering_info_isSet = !json[QString("offeringInfo")].isNull() && m_offering_info_isValid;

    m_offering_type_isValid = ::OpenAPI::fromJsonValue(m_offering_type, json[QString("offeringType")]);
    m_offering_type_isSet = !json[QString("offeringType")].isNull() && m_offering_type_isValid;

    m_offering_type_id_isValid = ::OpenAPI::fromJsonValue(m_offering_type_id, json[QString("offeringTypeId")]);
    m_offering_type_id_isSet = !json[QString("offeringTypeId")].isNull() && m_offering_type_id_isValid;
}

QString OAIAddCoupons_200_response_items_inner_additionalInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddCoupons_200_response_items_inner_additionalInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_brand_id_isSet) {
        obj.insert(QString("brandId"), ::OpenAPI::toJsonValue(m_brand_id));
    }
    if (m_brand_name_isSet) {
        obj.insert(QString("brandName"), ::OpenAPI::toJsonValue(m_brand_name));
    }
    if (m_dimension_isSet) {
        obj.insert(QString("dimension"), ::OpenAPI::toJsonValue(m_dimension));
    }
    if (m_offering_info_isSet) {
        obj.insert(QString("offeringInfo"), ::OpenAPI::toJsonValue(m_offering_info));
    }
    if (m_offering_type_isSet) {
        obj.insert(QString("offeringType"), ::OpenAPI::toJsonValue(m_offering_type));
    }
    if (m_offering_type_id_isSet) {
        obj.insert(QString("offeringTypeId"), ::OpenAPI::toJsonValue(m_offering_type_id));
    }
    return obj;
}

QString OAIAddCoupons_200_response_items_inner_additionalInfo::getBrandId() const {
    return m_brand_id;
}
void OAIAddCoupons_200_response_items_inner_additionalInfo::setBrandId(const QString &brand_id) {
    m_brand_id = brand_id;
    m_brand_id_isSet = true;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_brand_id_Set() const{
    return m_brand_id_isSet;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_brand_id_Valid() const{
    return m_brand_id_isValid;
}

QString OAIAddCoupons_200_response_items_inner_additionalInfo::getBrandName() const {
    return m_brand_name;
}
void OAIAddCoupons_200_response_items_inner_additionalInfo::setBrandName(const QString &brand_name) {
    m_brand_name = brand_name;
    m_brand_name_isSet = true;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_brand_name_Set() const{
    return m_brand_name_isSet;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_brand_name_Valid() const{
    return m_brand_name_isValid;
}

QString OAIAddCoupons_200_response_items_inner_additionalInfo::getDimension() const {
    return m_dimension;
}
void OAIAddCoupons_200_response_items_inner_additionalInfo::setDimension(const QString &dimension) {
    m_dimension = dimension;
    m_dimension_isSet = true;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_dimension_Set() const{
    return m_dimension_isSet;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_dimension_Valid() const{
    return m_dimension_isValid;
}

QString OAIAddCoupons_200_response_items_inner_additionalInfo::getOfferingInfo() const {
    return m_offering_info;
}
void OAIAddCoupons_200_response_items_inner_additionalInfo::setOfferingInfo(const QString &offering_info) {
    m_offering_info = offering_info;
    m_offering_info_isSet = true;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_offering_info_Set() const{
    return m_offering_info_isSet;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_offering_info_Valid() const{
    return m_offering_info_isValid;
}

QString OAIAddCoupons_200_response_items_inner_additionalInfo::getOfferingType() const {
    return m_offering_type;
}
void OAIAddCoupons_200_response_items_inner_additionalInfo::setOfferingType(const QString &offering_type) {
    m_offering_type = offering_type;
    m_offering_type_isSet = true;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_offering_type_Set() const{
    return m_offering_type_isSet;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_offering_type_Valid() const{
    return m_offering_type_isValid;
}

QString OAIAddCoupons_200_response_items_inner_additionalInfo::getOfferingTypeId() const {
    return m_offering_type_id;
}
void OAIAddCoupons_200_response_items_inner_additionalInfo::setOfferingTypeId(const QString &offering_type_id) {
    m_offering_type_id = offering_type_id;
    m_offering_type_id_isSet = true;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_offering_type_id_Set() const{
    return m_offering_type_id_isSet;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::is_offering_type_id_Valid() const{
    return m_offering_type_id_isValid;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_brand_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_brand_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_dimension_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offering_info_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offering_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offering_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddCoupons_200_response_items_inner_additionalInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
