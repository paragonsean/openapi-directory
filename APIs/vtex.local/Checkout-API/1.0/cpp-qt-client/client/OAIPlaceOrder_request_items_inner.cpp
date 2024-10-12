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

#include "OAIPlaceOrder_request_items_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaceOrder_request_items_inner::OAIPlaceOrder_request_items_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaceOrder_request_items_inner::OAIPlaceOrder_request_items_inner() {
    this->initializeModel();
}

OAIPlaceOrder_request_items_inner::~OAIPlaceOrder_request_items_inner() {}

void OAIPlaceOrder_request_items_inner::initializeModel() {

    m_attachments_isSet = false;
    m_attachments_isValid = false;

    m_bundle_items_isSet = false;
    m_bundle_items_isValid = false;

    m_commission_isSet = false;
    m_commission_isValid = false;

    m_freight_commission_isSet = false;
    m_freight_commission_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_gift_isSet = false;
    m_is_gift_isValid = false;

    m_item_attachment_isSet = false;
    m_item_attachment_isValid = false;

    m_measurement_unit_isSet = false;
    m_measurement_unit_isValid = false;

    m_price_isSet = false;
    m_price_isValid = false;

    m_price_tags_isSet = false;
    m_price_tags_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_seller_isSet = false;
    m_seller_isValid = false;

    m_unit_multiplier_isSet = false;
    m_unit_multiplier_isValid = false;
}

void OAIPlaceOrder_request_items_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaceOrder_request_items_inner::fromJsonObject(QJsonObject json) {

    m_attachments_isValid = ::OpenAPI::fromJsonValue(m_attachments, json[QString("attachments")]);
    m_attachments_isSet = !json[QString("attachments")].isNull() && m_attachments_isValid;

    m_bundle_items_isValid = ::OpenAPI::fromJsonValue(m_bundle_items, json[QString("bundleItems")]);
    m_bundle_items_isSet = !json[QString("bundleItems")].isNull() && m_bundle_items_isValid;

    m_commission_isValid = ::OpenAPI::fromJsonValue(m_commission, json[QString("commission")]);
    m_commission_isSet = !json[QString("commission")].isNull() && m_commission_isValid;

    m_freight_commission_isValid = ::OpenAPI::fromJsonValue(m_freight_commission, json[QString("freightCommission")]);
    m_freight_commission_isSet = !json[QString("freightCommission")].isNull() && m_freight_commission_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_gift_isValid = ::OpenAPI::fromJsonValue(m_is_gift, json[QString("isGift")]);
    m_is_gift_isSet = !json[QString("isGift")].isNull() && m_is_gift_isValid;

    m_item_attachment_isValid = ::OpenAPI::fromJsonValue(m_item_attachment, json[QString("itemAttachment")]);
    m_item_attachment_isSet = !json[QString("itemAttachment")].isNull() && m_item_attachment_isValid;

    m_measurement_unit_isValid = ::OpenAPI::fromJsonValue(m_measurement_unit, json[QString("measurementUnit")]);
    m_measurement_unit_isSet = !json[QString("measurementUnit")].isNull() && m_measurement_unit_isValid;

    m_price_isValid = ::OpenAPI::fromJsonValue(m_price, json[QString("price")]);
    m_price_isSet = !json[QString("price")].isNull() && m_price_isValid;

    m_price_tags_isValid = ::OpenAPI::fromJsonValue(m_price_tags, json[QString("priceTags")]);
    m_price_tags_isSet = !json[QString("priceTags")].isNull() && m_price_tags_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_seller_isValid = ::OpenAPI::fromJsonValue(m_seller, json[QString("seller")]);
    m_seller_isSet = !json[QString("seller")].isNull() && m_seller_isValid;

    m_unit_multiplier_isValid = ::OpenAPI::fromJsonValue(m_unit_multiplier, json[QString("unitMultiplier")]);
    m_unit_multiplier_isSet = !json[QString("unitMultiplier")].isNull() && m_unit_multiplier_isValid;
}

QString OAIPlaceOrder_request_items_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaceOrder_request_items_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_attachments.size() > 0) {
        obj.insert(QString("attachments"), ::OpenAPI::toJsonValue(m_attachments));
    }
    if (m_bundle_items.size() > 0) {
        obj.insert(QString("bundleItems"), ::OpenAPI::toJsonValue(m_bundle_items));
    }
    if (m_commission_isSet) {
        obj.insert(QString("commission"), ::OpenAPI::toJsonValue(m_commission));
    }
    if (m_freight_commission_isSet) {
        obj.insert(QString("freightCommission"), ::OpenAPI::toJsonValue(m_freight_commission));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_gift_isSet) {
        obj.insert(QString("isGift"), ::OpenAPI::toJsonValue(m_is_gift));
    }
    if (m_item_attachment.isSet()) {
        obj.insert(QString("itemAttachment"), ::OpenAPI::toJsonValue(m_item_attachment));
    }
    if (m_measurement_unit_isSet) {
        obj.insert(QString("measurementUnit"), ::OpenAPI::toJsonValue(m_measurement_unit));
    }
    if (m_price_isSet) {
        obj.insert(QString("price"), ::OpenAPI::toJsonValue(m_price));
    }
    if (m_price_tags.size() > 0) {
        obj.insert(QString("priceTags"), ::OpenAPI::toJsonValue(m_price_tags));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_seller_isSet) {
        obj.insert(QString("seller"), ::OpenAPI::toJsonValue(m_seller));
    }
    if (m_unit_multiplier_isSet) {
        obj.insert(QString("unitMultiplier"), ::OpenAPI::toJsonValue(m_unit_multiplier));
    }
    return obj;
}

QList<QString> OAIPlaceOrder_request_items_inner::getAttachments() const {
    return m_attachments;
}
void OAIPlaceOrder_request_items_inner::setAttachments(const QList<QString> &attachments) {
    m_attachments = attachments;
    m_attachments_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_attachments_Set() const{
    return m_attachments_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_attachments_Valid() const{
    return m_attachments_isValid;
}

QList<OAIPlaceOrder_request_items_inner_bundleItems_inner> OAIPlaceOrder_request_items_inner::getBundleItems() const {
    return m_bundle_items;
}
void OAIPlaceOrder_request_items_inner::setBundleItems(const QList<OAIPlaceOrder_request_items_inner_bundleItems_inner> &bundle_items) {
    m_bundle_items = bundle_items;
    m_bundle_items_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_bundle_items_Set() const{
    return m_bundle_items_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_bundle_items_Valid() const{
    return m_bundle_items_isValid;
}

qint32 OAIPlaceOrder_request_items_inner::getCommission() const {
    return m_commission;
}
void OAIPlaceOrder_request_items_inner::setCommission(const qint32 &commission) {
    m_commission = commission;
    m_commission_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_commission_Set() const{
    return m_commission_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_commission_Valid() const{
    return m_commission_isValid;
}

qint32 OAIPlaceOrder_request_items_inner::getFreightCommission() const {
    return m_freight_commission;
}
void OAIPlaceOrder_request_items_inner::setFreightCommission(const qint32 &freight_commission) {
    m_freight_commission = freight_commission;
    m_freight_commission_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_freight_commission_Set() const{
    return m_freight_commission_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_freight_commission_Valid() const{
    return m_freight_commission_isValid;
}

QString OAIPlaceOrder_request_items_inner::getId() const {
    return m_id;
}
void OAIPlaceOrder_request_items_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIPlaceOrder_request_items_inner::isIsGift() const {
    return m_is_gift;
}
void OAIPlaceOrder_request_items_inner::setIsGift(const bool &is_gift) {
    m_is_gift = is_gift;
    m_is_gift_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_is_gift_Set() const{
    return m_is_gift_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_is_gift_Valid() const{
    return m_is_gift_isValid;
}

OAIPlaceOrder_request_items_inner_itemAttachment OAIPlaceOrder_request_items_inner::getItemAttachment() const {
    return m_item_attachment;
}
void OAIPlaceOrder_request_items_inner::setItemAttachment(const OAIPlaceOrder_request_items_inner_itemAttachment &item_attachment) {
    m_item_attachment = item_attachment;
    m_item_attachment_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_item_attachment_Set() const{
    return m_item_attachment_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_item_attachment_Valid() const{
    return m_item_attachment_isValid;
}

QString OAIPlaceOrder_request_items_inner::getMeasurementUnit() const {
    return m_measurement_unit;
}
void OAIPlaceOrder_request_items_inner::setMeasurementUnit(const QString &measurement_unit) {
    m_measurement_unit = measurement_unit;
    m_measurement_unit_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_measurement_unit_Set() const{
    return m_measurement_unit_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_measurement_unit_Valid() const{
    return m_measurement_unit_isValid;
}

qint32 OAIPlaceOrder_request_items_inner::getPrice() const {
    return m_price;
}
void OAIPlaceOrder_request_items_inner::setPrice(const qint32 &price) {
    m_price = price;
    m_price_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_price_Set() const{
    return m_price_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_price_Valid() const{
    return m_price_isValid;
}

QList<OAIPlaceOrder_request_items_inner_priceTags_inner> OAIPlaceOrder_request_items_inner::getPriceTags() const {
    return m_price_tags;
}
void OAIPlaceOrder_request_items_inner::setPriceTags(const QList<OAIPlaceOrder_request_items_inner_priceTags_inner> &price_tags) {
    m_price_tags = price_tags;
    m_price_tags_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_price_tags_Set() const{
    return m_price_tags_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_price_tags_Valid() const{
    return m_price_tags_isValid;
}

qint32 OAIPlaceOrder_request_items_inner::getQuantity() const {
    return m_quantity;
}
void OAIPlaceOrder_request_items_inner::setQuantity(const qint32 &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_quantity_Valid() const{
    return m_quantity_isValid;
}

QString OAIPlaceOrder_request_items_inner::getSeller() const {
    return m_seller;
}
void OAIPlaceOrder_request_items_inner::setSeller(const QString &seller) {
    m_seller = seller;
    m_seller_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_seller_Set() const{
    return m_seller_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_seller_Valid() const{
    return m_seller_isValid;
}

qint32 OAIPlaceOrder_request_items_inner::getUnitMultiplier() const {
    return m_unit_multiplier;
}
void OAIPlaceOrder_request_items_inner::setUnitMultiplier(const qint32 &unit_multiplier) {
    m_unit_multiplier = unit_multiplier;
    m_unit_multiplier_isSet = true;
}

bool OAIPlaceOrder_request_items_inner::is_unit_multiplier_Set() const{
    return m_unit_multiplier_isSet;
}

bool OAIPlaceOrder_request_items_inner::is_unit_multiplier_Valid() const{
    return m_unit_multiplier_isValid;
}

bool OAIPlaceOrder_request_items_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_attachments.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_bundle_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_commission_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_freight_commission_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_gift_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_item_attachment.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_measurement_unit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_price_tags.size() > 0) {
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

        if (m_unit_multiplier_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlaceOrder_request_items_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_quantity_isValid && m_seller_isValid && true;
}

} // namespace OpenAPI
