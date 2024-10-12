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

#include "OAICartSimulation_200_response_items_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICartSimulation_200_response_items_inner::OAICartSimulation_200_response_items_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICartSimulation_200_response_items_inner::OAICartSimulation_200_response_items_inner() {
    this->initializeModel();
}

OAICartSimulation_200_response_items_inner::~OAICartSimulation_200_response_items_inner() {}

void OAICartSimulation_200_response_items_inner::initializeModel() {

    m_availability_isSet = false;
    m_availability_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_list_price_isSet = false;
    m_list_price_isValid = false;

    m_measurement_unit_isSet = false;
    m_measurement_unit_isValid = false;

    m_offerings_isSet = false;
    m_offerings_isValid = false;

    m_parent_assembly_binding_isSet = false;
    m_parent_assembly_binding_isValid = false;

    m_parent_item_index_isSet = false;
    m_parent_item_index_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_price_definition_isSet = false;
    m_price_definition_isValid = false;

    m_price_tags_isSet = false;
    m_price_tags_isValid = false;

    m_price_valid_until_isSet = false;
    m_price_valid_until_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_request_index_isSet = false;
    m_request_index_isValid = false;

    m_reward_value_isSet = false;
    m_reward_value_isValid = false;

    m_seller_isSet = false;
    m_seller_isValid = false;

    m_seller_chain_isSet = false;
    m_seller_chain_isValid = false;

    m_selling_price_isSet = false;
    m_selling_price_isValid = false;

    m_tax_isSet = false;
    m_tax_isValid = false;

    m_unit_multiplier_isSet = false;
    m_unit_multiplier_isValid = false;
}

void OAICartSimulation_200_response_items_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICartSimulation_200_response_items_inner::fromJsonObject(QJsonObject json) {

    m_availability_isValid = ::OpenAPI::fromJsonValue(m_availability, json[QString("availability")]);
    m_availability_isSet = !json[QString("availability")].isNull() && m_availability_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_list_price_isValid = ::OpenAPI::fromJsonValue(m_list_price, json[QString("listPrice")]);
    m_list_price_isSet = !json[QString("listPrice")].isNull() && m_list_price_isValid;

    m_measurement_unit_isValid = ::OpenAPI::fromJsonValue(m_measurement_unit, json[QString("measurementUnit")]);
    m_measurement_unit_isSet = !json[QString("measurementUnit")].isNull() && m_measurement_unit_isValid;

    m_offerings_isValid = ::OpenAPI::fromJsonValue(m_offerings, json[QString("offerings")]);
    m_offerings_isSet = !json[QString("offerings")].isNull() && m_offerings_isValid;

    m_parent_assembly_binding_isValid = ::OpenAPI::fromJsonValue(m_parent_assembly_binding, json[QString("parentAssemblyBinding")]);
    m_parent_assembly_binding_isSet = !json[QString("parentAssemblyBinding")].isNull() && m_parent_assembly_binding_isValid;

    m_parent_item_index_isValid = ::OpenAPI::fromJsonValue(m_parent_item_index, json[QString("parentItemIndex")]);
    m_parent_item_index_isSet = !json[QString("parentItemIndex")].isNull() && m_parent_item_index_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_price_definition_isValid = ::OpenAPI::fromJsonValue(m_price_definition, json[QString("priceDefinition")]);
    m_price_definition_isSet = !json[QString("priceDefinition")].isNull() && m_price_definition_isValid;

    m_price_tags_isValid = ::OpenAPI::fromJsonValue(m_price_tags, json[QString("priceTags")]);
    m_price_tags_isSet = !json[QString("priceTags")].isNull() && m_price_tags_isValid;

    m_price_valid_until_isValid = ::OpenAPI::fromJsonValue(m_price_valid_until, json[QString("priceValidUntil")]);
    m_price_valid_until_isSet = !json[QString("priceValidUntil")].isNull() && m_price_valid_until_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_request_index_isValid = ::OpenAPI::fromJsonValue(m_request_index, json[QString("requestIndex")]);
    m_request_index_isSet = !json[QString("requestIndex")].isNull() && m_request_index_isValid;

    m_reward_value_isValid = ::OpenAPI::fromJsonValue(m_reward_value, json[QString("rewardValue")]);
    m_reward_value_isSet = !json[QString("rewardValue")].isNull() && m_reward_value_isValid;

    m_seller_isValid = ::OpenAPI::fromJsonValue(m_seller, json[QString("seller")]);
    m_seller_isSet = !json[QString("seller")].isNull() && m_seller_isValid;

    m_seller_chain_isValid = ::OpenAPI::fromJsonValue(m_seller_chain, json[QString("sellerChain")]);
    m_seller_chain_isSet = !json[QString("sellerChain")].isNull() && m_seller_chain_isValid;

    m_selling_price_isValid = ::OpenAPI::fromJsonValue(m_selling_price, json[QString("sellingPrice")]);
    m_selling_price_isSet = !json[QString("sellingPrice")].isNull() && m_selling_price_isValid;

    m_tax_isValid = ::OpenAPI::fromJsonValue(m_tax, json[QString("tax")]);
    m_tax_isSet = !json[QString("tax")].isNull() && m_tax_isValid;

    m_unit_multiplier_isValid = ::OpenAPI::fromJsonValue(m_unit_multiplier, json[QString("unitMultiplier")]);
    m_unit_multiplier_isSet = !json[QString("unitMultiplier")].isNull() && m_unit_multiplier_isValid;
}

QString OAICartSimulation_200_response_items_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICartSimulation_200_response_items_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_availability_isSet) {
        obj.insert(QString("availability"), ::OpenAPI::toJsonValue(m_availability));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_list_price_isSet) {
        obj.insert(QString("listPrice"), ::OpenAPI::toJsonValue(m_list_price));
    }
    if (m_measurement_unit_isSet) {
        obj.insert(QString("measurementUnit"), ::OpenAPI::toJsonValue(m_measurement_unit));
    }
    if (m_offerings.size() > 0) {
        obj.insert(QString("offerings"), ::OpenAPI::toJsonValue(m_offerings));
    }
    if (m_parent_assembly_binding_isSet) {
        obj.insert(QString("parentAssemblyBinding"), ::OpenAPI::toJsonValue(m_parent_assembly_binding));
    }
    if (m_parent_item_index_isSet) {
        obj.insert(QString("parentItemIndex"), ::OpenAPI::toJsonValue(m_parent_item_index));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_price_definition.isSet()) {
        obj.insert(QString("priceDefinition"), ::OpenAPI::toJsonValue(m_price_definition));
    }
    if (m_price_tags.size() > 0) {
        obj.insert(QString("priceTags"), ::OpenAPI::toJsonValue(m_price_tags));
    }
    if (m_price_valid_until_isSet) {
        obj.insert(QString("priceValidUntil"), ::OpenAPI::toJsonValue(m_price_valid_until));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_request_index_isSet) {
        obj.insert(QString("requestIndex"), ::OpenAPI::toJsonValue(m_request_index));
    }
    if (m_reward_value_isSet) {
        obj.insert(QString("rewardValue"), ::OpenAPI::toJsonValue(m_reward_value));
    }
    if (m_seller_isSet) {
        obj.insert(QString("seller"), ::OpenAPI::toJsonValue(m_seller));
    }
    if (m_seller_chain.size() > 0) {
        obj.insert(QString("sellerChain"), ::OpenAPI::toJsonValue(m_seller_chain));
    }
    if (m_selling_price_isSet) {
        obj.insert(QString("sellingPrice"), ::OpenAPI::toJsonValue(m_selling_price));
    }
    if (m_tax_isSet) {
        obj.insert(QString("tax"), ::OpenAPI::toJsonValue(m_tax));
    }
    if (m_unit_multiplier_isSet) {
        obj.insert(QString("unitMultiplier"), ::OpenAPI::toJsonValue(m_unit_multiplier));
    }
    return obj;
}

QString OAICartSimulation_200_response_items_inner::getAvailability() const {
    return m_availability;
}
void OAICartSimulation_200_response_items_inner::setAvailability(const QString &availability) {
    m_availability = availability;
    m_availability_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_availability_Set() const{
    return m_availability_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_availability_Valid() const{
    return m_availability_isValid;
}

QString OAICartSimulation_200_response_items_inner::getId() const {
    return m_id;
}
void OAICartSimulation_200_response_items_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAICartSimulation_200_response_items_inner::getListPrice() const {
    return m_list_price;
}
void OAICartSimulation_200_response_items_inner::setListPrice(const qint32 &list_price) {
    m_list_price = list_price;
    m_list_price_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_list_price_Set() const{
    return m_list_price_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_list_price_Valid() const{
    return m_list_price_isValid;
}

QString OAICartSimulation_200_response_items_inner::getMeasurementUnit() const {
    return m_measurement_unit;
}
void OAICartSimulation_200_response_items_inner::setMeasurementUnit(const QString &measurement_unit) {
    m_measurement_unit = measurement_unit;
    m_measurement_unit_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_measurement_unit_Set() const{
    return m_measurement_unit_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_measurement_unit_Valid() const{
    return m_measurement_unit_isValid;
}

QList<QJsonValue> OAICartSimulation_200_response_items_inner::getOfferings() const {
    return m_offerings;
}
void OAICartSimulation_200_response_items_inner::setOfferings(const QList<QJsonValue> &offerings) {
    m_offerings = offerings;
    m_offerings_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_offerings_Set() const{
    return m_offerings_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_offerings_Valid() const{
    return m_offerings_isValid;
}

QString OAICartSimulation_200_response_items_inner::getParentAssemblyBinding() const {
    return m_parent_assembly_binding;
}
void OAICartSimulation_200_response_items_inner::setParentAssemblyBinding(const QString &parent_assembly_binding) {
    m_parent_assembly_binding = parent_assembly_binding;
    m_parent_assembly_binding_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_parent_assembly_binding_Set() const{
    return m_parent_assembly_binding_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_parent_assembly_binding_Valid() const{
    return m_parent_assembly_binding_isValid;
}

qint32 OAICartSimulation_200_response_items_inner::getParentItemIndex() const {
    return m_parent_item_index;
}
void OAICartSimulation_200_response_items_inner::setParentItemIndex(const qint32 &parent_item_index) {
    m_parent_item_index = parent_item_index;
    m_parent_item_index_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_parent_item_index_Set() const{
    return m_parent_item_index_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_parent_item_index_Valid() const{
    return m_parent_item_index_isValid;
}

qint32 OAICartSimulation_200_response_items_inner::getPrice() const {
    return m_price;
}
void OAICartSimulation_200_response_items_inner::setPrice(const qint32 &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_price_Set() const{
    return m_price_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_price_Valid() const{
    return m_price_isValid;
}

OAIAddCoupons_200_response_items_inner_priceDefinition OAICartSimulation_200_response_items_inner::getPriceDefinition() const {
    return m_price_definition;
}
void OAICartSimulation_200_response_items_inner::setPriceDefinition(const OAIAddCoupons_200_response_items_inner_priceDefinition &price_definition) {
    m_price_definition = price_definition;
    m_price_definition_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_price_definition_Set() const{
    return m_price_definition_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_price_definition_Valid() const{
    return m_price_definition_isValid;
}

QList<OAICartSimulation_200_response_items_inner_priceTags_inner> OAICartSimulation_200_response_items_inner::getPriceTags() const {
    return m_price_tags;
}
void OAICartSimulation_200_response_items_inner::setPriceTags(const QList<OAICartSimulation_200_response_items_inner_priceTags_inner> &price_tags) {
    m_price_tags = price_tags;
    m_price_tags_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_price_tags_Set() const{
    return m_price_tags_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_price_tags_Valid() const{
    return m_price_tags_isValid;
}

QString OAICartSimulation_200_response_items_inner::getPriceValidUntil() const {
    return m_price_valid_until;
}
void OAICartSimulation_200_response_items_inner::setPriceValidUntil(const QString &price_valid_until) {
    m_price_valid_until = price_valid_until;
    m_price_valid_until_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_price_valid_until_Set() const{
    return m_price_valid_until_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_price_valid_until_Valid() const{
    return m_price_valid_until_isValid;
}

qint32 OAICartSimulation_200_response_items_inner::getQuantity() const {
    return m_quantity;
}
void OAICartSimulation_200_response_items_inner::setQuantity(const qint32 &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_quantity_Valid() const{
    return m_quantity_isValid;
}

qint32 OAICartSimulation_200_response_items_inner::getRequestIndex() const {
    return m_request_index;
}
void OAICartSimulation_200_response_items_inner::setRequestIndex(const qint32 &request_index) {
    m_request_index = request_index;
    m_request_index_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_request_index_Set() const{
    return m_request_index_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_request_index_Valid() const{
    return m_request_index_isValid;
}

qint32 OAICartSimulation_200_response_items_inner::getRewardValue() const {
    return m_reward_value;
}
void OAICartSimulation_200_response_items_inner::setRewardValue(const qint32 &reward_value) {
    m_reward_value = reward_value;
    m_reward_value_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_reward_value_Set() const{
    return m_reward_value_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_reward_value_Valid() const{
    return m_reward_value_isValid;
}

QString OAICartSimulation_200_response_items_inner::getSeller() const {
    return m_seller;
}
void OAICartSimulation_200_response_items_inner::setSeller(const QString &seller) {
    m_seller = seller;
    m_seller_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_seller_Set() const{
    return m_seller_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_seller_Valid() const{
    return m_seller_isValid;
}

QList<QString> OAICartSimulation_200_response_items_inner::getSellerChain() const {
    return m_seller_chain;
}
void OAICartSimulation_200_response_items_inner::setSellerChain(const QList<QString> &seller_chain) {
    m_seller_chain = seller_chain;
    m_seller_chain_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_seller_chain_Set() const{
    return m_seller_chain_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_seller_chain_Valid() const{
    return m_seller_chain_isValid;
}

qint32 OAICartSimulation_200_response_items_inner::getSellingPrice() const {
    return m_selling_price;
}
void OAICartSimulation_200_response_items_inner::setSellingPrice(const qint32 &selling_price) {
    m_selling_price = selling_price;
    m_selling_price_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_selling_price_Set() const{
    return m_selling_price_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_selling_price_Valid() const{
    return m_selling_price_isValid;
}

qint32 OAICartSimulation_200_response_items_inner::getTax() const {
    return m_tax;
}
void OAICartSimulation_200_response_items_inner::setTax(const qint32 &tax) {
    m_tax = tax;
    m_tax_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_tax_Set() const{
    return m_tax_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_tax_Valid() const{
    return m_tax_isValid;
}

qint32 OAICartSimulation_200_response_items_inner::getUnitMultiplier() const {
    return m_unit_multiplier;
}
void OAICartSimulation_200_response_items_inner::setUnitMultiplier(const qint32 &unit_multiplier) {
    m_unit_multiplier = unit_multiplier;
    m_unit_multiplier_isSet = true;
}

bool OAICartSimulation_200_response_items_inner::is_unit_multiplier_Set() const{
    return m_unit_multiplier_isSet;
}

bool OAICartSimulation_200_response_items_inner::is_unit_multiplier_Valid() const{
    return m_unit_multiplier_isValid;
}

bool OAICartSimulation_200_response_items_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_availability_isSet) {
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

        if (m_measurement_unit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_offerings.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_assembly_binding_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_item_index_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_definition.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_valid_until_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_request_index_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reward_value_isSet) {
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

        if (m_selling_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_multiplier_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICartSimulation_200_response_items_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
