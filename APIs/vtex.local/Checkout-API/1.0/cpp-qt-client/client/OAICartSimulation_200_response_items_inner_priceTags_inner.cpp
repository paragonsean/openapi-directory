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

#include "OAICartSimulation_200_response_items_inner_priceTags_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICartSimulation_200_response_items_inner_priceTags_inner::OAICartSimulation_200_response_items_inner_priceTags_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICartSimulation_200_response_items_inner_priceTags_inner::OAICartSimulation_200_response_items_inner_priceTags_inner() {
    this->initializeModel();
}

OAICartSimulation_200_response_items_inner_priceTags_inner::~OAICartSimulation_200_response_items_inner_priceTags_inner() {}

void OAICartSimulation_200_response_items_inner_priceTags_inner::initializeModel() {

    m_identifier_isSet = false;
    m_identifier_isValid = false;

    m_is_percentual_isSet = false;
    m_is_percentual_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_owner_isSet = false;
    m_owner_isValid = false;

    m_raw_value_isSet = false;
    m_raw_value_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAICartSimulation_200_response_items_inner_priceTags_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICartSimulation_200_response_items_inner_priceTags_inner::fromJsonObject(QJsonObject json) {

    m_identifier_isValid = ::OpenAPI::fromJsonValue(m_identifier, json[QString("identifier")]);
    m_identifier_isSet = !json[QString("identifier")].isNull() && m_identifier_isValid;

    m_is_percentual_isValid = ::OpenAPI::fromJsonValue(m_is_percentual, json[QString("isPercentual")]);
    m_is_percentual_isSet = !json[QString("isPercentual")].isNull() && m_is_percentual_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_owner_isValid = ::OpenAPI::fromJsonValue(m_owner, json[QString("owner")]);
    m_owner_isSet = !json[QString("owner")].isNull() && m_owner_isValid;

    m_raw_value_isValid = ::OpenAPI::fromJsonValue(m_raw_value, json[QString("rawValue")]);
    m_raw_value_isSet = !json[QString("rawValue")].isNull() && m_raw_value_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAICartSimulation_200_response_items_inner_priceTags_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICartSimulation_200_response_items_inner_priceTags_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_identifier_isSet) {
        obj.insert(QString("identifier"), ::OpenAPI::toJsonValue(m_identifier));
    }
    if (m_is_percentual_isSet) {
        obj.insert(QString("isPercentual"), ::OpenAPI::toJsonValue(m_is_percentual));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_owner_isSet) {
        obj.insert(QString("owner"), ::OpenAPI::toJsonValue(m_owner));
    }
    if (m_raw_value_isSet) {
        obj.insert(QString("rawValue"), ::OpenAPI::toJsonValue(m_raw_value));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAICartSimulation_200_response_items_inner_priceTags_inner::getIdentifier() const {
    return m_identifier;
}
void OAICartSimulation_200_response_items_inner_priceTags_inner::setIdentifier(const QString &identifier) {
    m_identifier = identifier;
    m_identifier_isSet = true;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_identifier_Set() const{
    return m_identifier_isSet;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_identifier_Valid() const{
    return m_identifier_isValid;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::isIsPercentual() const {
    return m_is_percentual;
}
void OAICartSimulation_200_response_items_inner_priceTags_inner::setIsPercentual(const bool &is_percentual) {
    m_is_percentual = is_percentual;
    m_is_percentual_isSet = true;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_is_percentual_Set() const{
    return m_is_percentual_isSet;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_is_percentual_Valid() const{
    return m_is_percentual_isValid;
}

QString OAICartSimulation_200_response_items_inner_priceTags_inner::getName() const {
    return m_name;
}
void OAICartSimulation_200_response_items_inner_priceTags_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICartSimulation_200_response_items_inner_priceTags_inner::getOwner() const {
    return m_owner;
}
void OAICartSimulation_200_response_items_inner_priceTags_inner::setOwner(const QString &owner) {
    m_owner = owner;
    m_owner_isSet = true;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_owner_Set() const{
    return m_owner_isSet;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_owner_Valid() const{
    return m_owner_isValid;
}

qint32 OAICartSimulation_200_response_items_inner_priceTags_inner::getRawValue() const {
    return m_raw_value;
}
void OAICartSimulation_200_response_items_inner_priceTags_inner::setRawValue(const qint32 &raw_value) {
    m_raw_value = raw_value;
    m_raw_value_isSet = true;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_raw_value_Set() const{
    return m_raw_value_isSet;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_raw_value_Valid() const{
    return m_raw_value_isValid;
}

qint32 OAICartSimulation_200_response_items_inner_priceTags_inner::getValue() const {
    return m_value;
}
void OAICartSimulation_200_response_items_inner_priceTags_inner::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_value_Set() const{
    return m_value_isSet;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::is_value_Valid() const{
    return m_value_isValid;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_identifier_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_percentual_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_owner_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_raw_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICartSimulation_200_response_items_inner_priceTags_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
