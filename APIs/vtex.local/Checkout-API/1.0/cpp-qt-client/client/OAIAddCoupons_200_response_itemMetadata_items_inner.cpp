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

#include "OAIAddCoupons_200_response_itemMetadata_items_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddCoupons_200_response_itemMetadata_items_inner::OAIAddCoupons_200_response_itemMetadata_items_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddCoupons_200_response_itemMetadata_items_inner::OAIAddCoupons_200_response_itemMetadata_items_inner() {
    this->initializeModel();
}

OAIAddCoupons_200_response_itemMetadata_items_inner::~OAIAddCoupons_200_response_itemMetadata_items_inner() {}

void OAIAddCoupons_200_response_itemMetadata_items_inner::initializeModel() {

    m_detail_url_isSet = false;
    m_detail_url_isValid = false;

    m_ean_isSet = false;
    m_ean_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_url_isSet = false;
    m_image_url_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_ref_id_isSet = false;
    m_ref_id_isValid = false;

    m_seller_isSet = false;
    m_seller_isValid = false;

    m_sku_name_isSet = false;
    m_sku_name_isValid = false;
}

void OAIAddCoupons_200_response_itemMetadata_items_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddCoupons_200_response_itemMetadata_items_inner::fromJsonObject(QJsonObject json) {

    m_detail_url_isValid = ::OpenAPI::fromJsonValue(m_detail_url, json[QString("detailUrl")]);
    m_detail_url_isSet = !json[QString("detailUrl")].isNull() && m_detail_url_isValid;

    m_ean_isValid = ::OpenAPI::fromJsonValue(m_ean, json[QString("ean")]);
    m_ean_isSet = !json[QString("ean")].isNull() && m_ean_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_url_isValid = ::OpenAPI::fromJsonValue(m_image_url, json[QString("imageUrl")]);
    m_image_url_isSet = !json[QString("imageUrl")].isNull() && m_image_url_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("productId")]);
    m_product_id_isSet = !json[QString("productId")].isNull() && m_product_id_isValid;

    m_ref_id_isValid = ::OpenAPI::fromJsonValue(m_ref_id, json[QString("refId")]);
    m_ref_id_isSet = !json[QString("refId")].isNull() && m_ref_id_isValid;

    m_seller_isValid = ::OpenAPI::fromJsonValue(m_seller, json[QString("seller")]);
    m_seller_isSet = !json[QString("seller")].isNull() && m_seller_isValid;

    m_sku_name_isValid = ::OpenAPI::fromJsonValue(m_sku_name, json[QString("skuName")]);
    m_sku_name_isSet = !json[QString("skuName")].isNull() && m_sku_name_isValid;
}

QString OAIAddCoupons_200_response_itemMetadata_items_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddCoupons_200_response_itemMetadata_items_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_detail_url_isSet) {
        obj.insert(QString("detailUrl"), ::OpenAPI::toJsonValue(m_detail_url));
    }
    if (m_ean_isSet) {
        obj.insert(QString("ean"), ::OpenAPI::toJsonValue(m_ean));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_url_isSet) {
        obj.insert(QString("imageUrl"), ::OpenAPI::toJsonValue(m_image_url));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("productId"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_ref_id_isSet) {
        obj.insert(QString("refId"), ::OpenAPI::toJsonValue(m_ref_id));
    }
    if (m_seller_isSet) {
        obj.insert(QString("seller"), ::OpenAPI::toJsonValue(m_seller));
    }
    if (m_sku_name_isSet) {
        obj.insert(QString("skuName"), ::OpenAPI::toJsonValue(m_sku_name));
    }
    return obj;
}

QString OAIAddCoupons_200_response_itemMetadata_items_inner::getDetailUrl() const {
    return m_detail_url;
}
void OAIAddCoupons_200_response_itemMetadata_items_inner::setDetailUrl(const QString &detail_url) {
    m_detail_url = detail_url;
    m_detail_url_isSet = true;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_detail_url_Set() const{
    return m_detail_url_isSet;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_detail_url_Valid() const{
    return m_detail_url_isValid;
}

QString OAIAddCoupons_200_response_itemMetadata_items_inner::getEan() const {
    return m_ean;
}
void OAIAddCoupons_200_response_itemMetadata_items_inner::setEan(const QString &ean) {
    m_ean = ean;
    m_ean_isSet = true;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_ean_Set() const{
    return m_ean_isSet;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_ean_Valid() const{
    return m_ean_isValid;
}

QString OAIAddCoupons_200_response_itemMetadata_items_inner::getId() const {
    return m_id;
}
void OAIAddCoupons_200_response_itemMetadata_items_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIAddCoupons_200_response_itemMetadata_items_inner::getImageUrl() const {
    return m_image_url;
}
void OAIAddCoupons_200_response_itemMetadata_items_inner::setImageUrl(const QString &image_url) {
    m_image_url = image_url;
    m_image_url_isSet = true;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_image_url_Set() const{
    return m_image_url_isSet;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_image_url_Valid() const{
    return m_image_url_isValid;
}

QString OAIAddCoupons_200_response_itemMetadata_items_inner::getName() const {
    return m_name;
}
void OAIAddCoupons_200_response_itemMetadata_items_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIAddCoupons_200_response_itemMetadata_items_inner::getProductId() const {
    return m_product_id;
}
void OAIAddCoupons_200_response_itemMetadata_items_inner::setProductId(const QString &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_product_id_Valid() const{
    return m_product_id_isValid;
}

QString OAIAddCoupons_200_response_itemMetadata_items_inner::getRefId() const {
    return m_ref_id;
}
void OAIAddCoupons_200_response_itemMetadata_items_inner::setRefId(const QString &ref_id) {
    m_ref_id = ref_id;
    m_ref_id_isSet = true;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_ref_id_Set() const{
    return m_ref_id_isSet;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_ref_id_Valid() const{
    return m_ref_id_isValid;
}

QString OAIAddCoupons_200_response_itemMetadata_items_inner::getSeller() const {
    return m_seller;
}
void OAIAddCoupons_200_response_itemMetadata_items_inner::setSeller(const QString &seller) {
    m_seller = seller;
    m_seller_isSet = true;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_seller_Set() const{
    return m_seller_isSet;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_seller_Valid() const{
    return m_seller_isValid;
}

QString OAIAddCoupons_200_response_itemMetadata_items_inner::getSkuName() const {
    return m_sku_name;
}
void OAIAddCoupons_200_response_itemMetadata_items_inner::setSkuName(const QString &sku_name) {
    m_sku_name = sku_name;
    m_sku_name_isSet = true;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_sku_name_Set() const{
    return m_sku_name_isSet;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::is_sku_name_Valid() const{
    return m_sku_name_isValid;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_detail_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ean_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ref_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_seller_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAddCoupons_200_response_itemMetadata_items_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
