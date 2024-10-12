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

#include "OAIItems_200_response_marketingData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIItems_200_response_marketingData::OAIItems_200_response_marketingData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIItems_200_response_marketingData::OAIItems_200_response_marketingData() {
    this->initializeModel();
}

OAIItems_200_response_marketingData::~OAIItems_200_response_marketingData() {}

void OAIItems_200_response_marketingData::initializeModel() {

    m_coupon_isSet = false;
    m_coupon_isValid = false;

    m_utm_campaign_isSet = false;
    m_utm_campaign_isValid = false;

    m_utm_medium_isSet = false;
    m_utm_medium_isValid = false;

    m_utm_source_isSet = false;
    m_utm_source_isValid = false;

    m_utmi_campaign_isSet = false;
    m_utmi_campaign_isValid = false;

    m_utmi_page_isSet = false;
    m_utmi_page_isValid = false;

    m_utmi_part_isSet = false;
    m_utmi_part_isValid = false;
}

void OAIItems_200_response_marketingData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIItems_200_response_marketingData::fromJsonObject(QJsonObject json) {

    m_coupon_isValid = ::OpenAPI::fromJsonValue(m_coupon, json[QString("coupon")]);
    m_coupon_isSet = !json[QString("coupon")].isNull() && m_coupon_isValid;

    m_utm_campaign_isValid = ::OpenAPI::fromJsonValue(m_utm_campaign, json[QString("utmCampaign")]);
    m_utm_campaign_isSet = !json[QString("utmCampaign")].isNull() && m_utm_campaign_isValid;

    m_utm_medium_isValid = ::OpenAPI::fromJsonValue(m_utm_medium, json[QString("utmMedium")]);
    m_utm_medium_isSet = !json[QString("utmMedium")].isNull() && m_utm_medium_isValid;

    m_utm_source_isValid = ::OpenAPI::fromJsonValue(m_utm_source, json[QString("utmSource")]);
    m_utm_source_isSet = !json[QString("utmSource")].isNull() && m_utm_source_isValid;

    m_utmi_campaign_isValid = ::OpenAPI::fromJsonValue(m_utmi_campaign, json[QString("utmiCampaign")]);
    m_utmi_campaign_isSet = !json[QString("utmiCampaign")].isNull() && m_utmi_campaign_isValid;

    m_utmi_page_isValid = ::OpenAPI::fromJsonValue(m_utmi_page, json[QString("utmiPage")]);
    m_utmi_page_isSet = !json[QString("utmiPage")].isNull() && m_utmi_page_isValid;

    m_utmi_part_isValid = ::OpenAPI::fromJsonValue(m_utmi_part, json[QString("utmiPart")]);
    m_utmi_part_isSet = !json[QString("utmiPart")].isNull() && m_utmi_part_isValid;
}

QString OAIItems_200_response_marketingData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIItems_200_response_marketingData::asJsonObject() const {
    QJsonObject obj;
    if (m_coupon_isSet) {
        obj.insert(QString("coupon"), ::OpenAPI::toJsonValue(m_coupon));
    }
    if (m_utm_campaign_isSet) {
        obj.insert(QString("utmCampaign"), ::OpenAPI::toJsonValue(m_utm_campaign));
    }
    if (m_utm_medium_isSet) {
        obj.insert(QString("utmMedium"), ::OpenAPI::toJsonValue(m_utm_medium));
    }
    if (m_utm_source_isSet) {
        obj.insert(QString("utmSource"), ::OpenAPI::toJsonValue(m_utm_source));
    }
    if (m_utmi_campaign_isSet) {
        obj.insert(QString("utmiCampaign"), ::OpenAPI::toJsonValue(m_utmi_campaign));
    }
    if (m_utmi_page_isSet) {
        obj.insert(QString("utmiPage"), ::OpenAPI::toJsonValue(m_utmi_page));
    }
    if (m_utmi_part_isSet) {
        obj.insert(QString("utmiPart"), ::OpenAPI::toJsonValue(m_utmi_part));
    }
    return obj;
}

QString OAIItems_200_response_marketingData::getCoupon() const {
    return m_coupon;
}
void OAIItems_200_response_marketingData::setCoupon(const QString &coupon) {
    m_coupon = coupon;
    m_coupon_isSet = true;
}

bool OAIItems_200_response_marketingData::is_coupon_Set() const{
    return m_coupon_isSet;
}

bool OAIItems_200_response_marketingData::is_coupon_Valid() const{
    return m_coupon_isValid;
}

QString OAIItems_200_response_marketingData::getUtmCampaign() const {
    return m_utm_campaign;
}
void OAIItems_200_response_marketingData::setUtmCampaign(const QString &utm_campaign) {
    m_utm_campaign = utm_campaign;
    m_utm_campaign_isSet = true;
}

bool OAIItems_200_response_marketingData::is_utm_campaign_Set() const{
    return m_utm_campaign_isSet;
}

bool OAIItems_200_response_marketingData::is_utm_campaign_Valid() const{
    return m_utm_campaign_isValid;
}

QString OAIItems_200_response_marketingData::getUtmMedium() const {
    return m_utm_medium;
}
void OAIItems_200_response_marketingData::setUtmMedium(const QString &utm_medium) {
    m_utm_medium = utm_medium;
    m_utm_medium_isSet = true;
}

bool OAIItems_200_response_marketingData::is_utm_medium_Set() const{
    return m_utm_medium_isSet;
}

bool OAIItems_200_response_marketingData::is_utm_medium_Valid() const{
    return m_utm_medium_isValid;
}

QString OAIItems_200_response_marketingData::getUtmSource() const {
    return m_utm_source;
}
void OAIItems_200_response_marketingData::setUtmSource(const QString &utm_source) {
    m_utm_source = utm_source;
    m_utm_source_isSet = true;
}

bool OAIItems_200_response_marketingData::is_utm_source_Set() const{
    return m_utm_source_isSet;
}

bool OAIItems_200_response_marketingData::is_utm_source_Valid() const{
    return m_utm_source_isValid;
}

QString OAIItems_200_response_marketingData::getUtmiCampaign() const {
    return m_utmi_campaign;
}
void OAIItems_200_response_marketingData::setUtmiCampaign(const QString &utmi_campaign) {
    m_utmi_campaign = utmi_campaign;
    m_utmi_campaign_isSet = true;
}

bool OAIItems_200_response_marketingData::is_utmi_campaign_Set() const{
    return m_utmi_campaign_isSet;
}

bool OAIItems_200_response_marketingData::is_utmi_campaign_Valid() const{
    return m_utmi_campaign_isValid;
}

QString OAIItems_200_response_marketingData::getUtmiPage() const {
    return m_utmi_page;
}
void OAIItems_200_response_marketingData::setUtmiPage(const QString &utmi_page) {
    m_utmi_page = utmi_page;
    m_utmi_page_isSet = true;
}

bool OAIItems_200_response_marketingData::is_utmi_page_Set() const{
    return m_utmi_page_isSet;
}

bool OAIItems_200_response_marketingData::is_utmi_page_Valid() const{
    return m_utmi_page_isValid;
}

QString OAIItems_200_response_marketingData::getUtmiPart() const {
    return m_utmi_part;
}
void OAIItems_200_response_marketingData::setUtmiPart(const QString &utmi_part) {
    m_utmi_part = utmi_part;
    m_utmi_part_isSet = true;
}

bool OAIItems_200_response_marketingData::is_utmi_part_Set() const{
    return m_utmi_part_isSet;
}

bool OAIItems_200_response_marketingData::is_utmi_part_Valid() const{
    return m_utmi_part_isValid;
}

bool OAIItems_200_response_marketingData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_coupon_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_utm_campaign_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_utm_medium_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_utm_source_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_utmi_campaign_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_utmi_page_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_utmi_part_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIItems_200_response_marketingData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
