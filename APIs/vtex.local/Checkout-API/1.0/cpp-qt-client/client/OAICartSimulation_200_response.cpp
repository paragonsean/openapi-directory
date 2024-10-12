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

#include "OAICartSimulation_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICartSimulation_200_response::OAICartSimulation_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICartSimulation_200_response::OAICartSimulation_200_response() {
    this->initializeModel();
}

OAICartSimulation_200_response::~OAICartSimulation_200_response() {}

void OAICartSimulation_200_response::initializeModel() {

    m_country_isSet = false;
    m_country_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_logistics_info_isSet = false;
    m_logistics_info_isValid = false;

    m_marketing_data_isSet = false;
    m_marketing_data_isValid = false;

    m_payment_data_isSet = false;
    m_payment_data_isValid = false;

    m_postal_code_isSet = false;
    m_postal_code_isValid = false;

    m_rates_and_benefits_data_isSet = false;
    m_rates_and_benefits_data_isValid = false;

    m_selectable_gifts_isSet = false;
    m_selectable_gifts_isValid = false;
}

void OAICartSimulation_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICartSimulation_200_response::fromJsonObject(QJsonObject json) {

    m_country_isValid = ::OpenAPI::fromJsonValue(m_country, json[QString("country")]);
    m_country_isSet = !json[QString("country")].isNull() && m_country_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_logistics_info_isValid = ::OpenAPI::fromJsonValue(m_logistics_info, json[QString("logisticsInfo")]);
    m_logistics_info_isSet = !json[QString("logisticsInfo")].isNull() && m_logistics_info_isValid;

    m_marketing_data_isValid = ::OpenAPI::fromJsonValue(m_marketing_data, json[QString("marketingData")]);
    m_marketing_data_isSet = !json[QString("marketingData")].isNull() && m_marketing_data_isValid;

    m_payment_data_isValid = ::OpenAPI::fromJsonValue(m_payment_data, json[QString("paymentData")]);
    m_payment_data_isSet = !json[QString("paymentData")].isNull() && m_payment_data_isValid;

    m_postal_code_isValid = ::OpenAPI::fromJsonValue(m_postal_code, json[QString("postalCode")]);
    m_postal_code_isSet = !json[QString("postalCode")].isNull() && m_postal_code_isValid;

    m_rates_and_benefits_data_isValid = ::OpenAPI::fromJsonValue(m_rates_and_benefits_data, json[QString("ratesAndBenefitsData")]);
    m_rates_and_benefits_data_isSet = !json[QString("ratesAndBenefitsData")].isNull() && m_rates_and_benefits_data_isValid;

    m_selectable_gifts_isValid = ::OpenAPI::fromJsonValue(m_selectable_gifts, json[QString("selectableGifts")]);
    m_selectable_gifts_isSet = !json[QString("selectableGifts")].isNull() && m_selectable_gifts_isValid;
}

QString OAICartSimulation_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICartSimulation_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_country_isSet) {
        obj.insert(QString("country"), ::OpenAPI::toJsonValue(m_country));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_logistics_info.size() > 0) {
        obj.insert(QString("logisticsInfo"), ::OpenAPI::toJsonValue(m_logistics_info));
    }
    if (m_marketing_data_isSet) {
        obj.insert(QString("marketingData"), ::OpenAPI::toJsonValue(m_marketing_data));
    }
    if (m_payment_data.isSet()) {
        obj.insert(QString("paymentData"), ::OpenAPI::toJsonValue(m_payment_data));
    }
    if (m_postal_code_isSet) {
        obj.insert(QString("postalCode"), ::OpenAPI::toJsonValue(m_postal_code));
    }
    if (m_rates_and_benefits_data.isSet()) {
        obj.insert(QString("ratesAndBenefitsData"), ::OpenAPI::toJsonValue(m_rates_and_benefits_data));
    }
    if (m_selectable_gifts.size() > 0) {
        obj.insert(QString("selectableGifts"), ::OpenAPI::toJsonValue(m_selectable_gifts));
    }
    return obj;
}

QString OAICartSimulation_200_response::getCountry() const {
    return m_country;
}
void OAICartSimulation_200_response::setCountry(const QString &country) {
    m_country = country;
    m_country_isSet = true;
}

bool OAICartSimulation_200_response::is_country_Set() const{
    return m_country_isSet;
}

bool OAICartSimulation_200_response::is_country_Valid() const{
    return m_country_isValid;
}

QList<OAICartSimulation_200_response_items_inner> OAICartSimulation_200_response::getItems() const {
    return m_items;
}
void OAICartSimulation_200_response::setItems(const QList<OAICartSimulation_200_response_items_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAICartSimulation_200_response::is_items_Set() const{
    return m_items_isSet;
}

bool OAICartSimulation_200_response::is_items_Valid() const{
    return m_items_isValid;
}

QList<OAICartSimulation_200_response_logisticsInfo_inner> OAICartSimulation_200_response::getLogisticsInfo() const {
    return m_logistics_info;
}
void OAICartSimulation_200_response::setLogisticsInfo(const QList<OAICartSimulation_200_response_logisticsInfo_inner> &logistics_info) {
    m_logistics_info = logistics_info;
    m_logistics_info_isSet = true;
}

bool OAICartSimulation_200_response::is_logistics_info_Set() const{
    return m_logistics_info_isSet;
}

bool OAICartSimulation_200_response::is_logistics_info_Valid() const{
    return m_logistics_info_isValid;
}

OAIObject OAICartSimulation_200_response::getMarketingData() const {
    return m_marketing_data;
}
void OAICartSimulation_200_response::setMarketingData(const OAIObject &marketing_data) {
    m_marketing_data = marketing_data;
    m_marketing_data_isSet = true;
}

bool OAICartSimulation_200_response::is_marketing_data_Set() const{
    return m_marketing_data_isSet;
}

bool OAICartSimulation_200_response::is_marketing_data_Valid() const{
    return m_marketing_data_isValid;
}

OAICartSimulation_200_response_paymentData OAICartSimulation_200_response::getPaymentData() const {
    return m_payment_data;
}
void OAICartSimulation_200_response::setPaymentData(const OAICartSimulation_200_response_paymentData &payment_data) {
    m_payment_data = payment_data;
    m_payment_data_isSet = true;
}

bool OAICartSimulation_200_response::is_payment_data_Set() const{
    return m_payment_data_isSet;
}

bool OAICartSimulation_200_response::is_payment_data_Valid() const{
    return m_payment_data_isValid;
}

QString OAICartSimulation_200_response::getPostalCode() const {
    return m_postal_code;
}
void OAICartSimulation_200_response::setPostalCode(const QString &postal_code) {
    m_postal_code = postal_code;
    m_postal_code_isSet = true;
}

bool OAICartSimulation_200_response::is_postal_code_Set() const{
    return m_postal_code_isSet;
}

bool OAICartSimulation_200_response::is_postal_code_Valid() const{
    return m_postal_code_isValid;
}

OAICartSimulation_200_response_ratesAndBenefitsData OAICartSimulation_200_response::getRatesAndBenefitsData() const {
    return m_rates_and_benefits_data;
}
void OAICartSimulation_200_response::setRatesAndBenefitsData(const OAICartSimulation_200_response_ratesAndBenefitsData &rates_and_benefits_data) {
    m_rates_and_benefits_data = rates_and_benefits_data;
    m_rates_and_benefits_data_isSet = true;
}

bool OAICartSimulation_200_response::is_rates_and_benefits_data_Set() const{
    return m_rates_and_benefits_data_isSet;
}

bool OAICartSimulation_200_response::is_rates_and_benefits_data_Valid() const{
    return m_rates_and_benefits_data_isValid;
}

QList<QJsonValue> OAICartSimulation_200_response::getSelectableGifts() const {
    return m_selectable_gifts;
}
void OAICartSimulation_200_response::setSelectableGifts(const QList<QJsonValue> &selectable_gifts) {
    m_selectable_gifts = selectable_gifts;
    m_selectable_gifts_isSet = true;
}

bool OAICartSimulation_200_response::is_selectable_gifts_Set() const{
    return m_selectable_gifts_isSet;
}

bool OAICartSimulation_200_response::is_selectable_gifts_Valid() const{
    return m_selectable_gifts_isValid;
}

bool OAICartSimulation_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_country_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_logistics_info.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_marketing_data_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_postal_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rates_and_benefits_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_selectable_gifts.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICartSimulation_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
