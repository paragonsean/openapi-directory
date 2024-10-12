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

#include "OAIPlaceOrder_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaceOrder_request::OAIPlaceOrder_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaceOrder_request::OAIPlaceOrder_request() {
    this->initializeModel();
}

OAIPlaceOrder_request::~OAIPlaceOrder_request() {}

void OAIPlaceOrder_request::initializeModel() {

    m_client_profile_data_isSet = false;
    m_client_profile_data_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_marketing_data_isSet = false;
    m_marketing_data_isValid = false;

    m_open_text_field_isSet = false;
    m_open_text_field_isValid = false;

    m_payment_data_isSet = false;
    m_payment_data_isValid = false;

    m_sales_associate_data_isSet = false;
    m_sales_associate_data_isValid = false;

    m_shipping_data_isSet = false;
    m_shipping_data_isValid = false;
}

void OAIPlaceOrder_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaceOrder_request::fromJsonObject(QJsonObject json) {

    m_client_profile_data_isValid = ::OpenAPI::fromJsonValue(m_client_profile_data, json[QString("clientProfileData")]);
    m_client_profile_data_isSet = !json[QString("clientProfileData")].isNull() && m_client_profile_data_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("items")]);
    m_items_isSet = !json[QString("items")].isNull() && m_items_isValid;

    m_marketing_data_isValid = ::OpenAPI::fromJsonValue(m_marketing_data, json[QString("marketingData")]);
    m_marketing_data_isSet = !json[QString("marketingData")].isNull() && m_marketing_data_isValid;

    m_open_text_field_isValid = ::OpenAPI::fromJsonValue(m_open_text_field, json[QString("openTextField")]);
    m_open_text_field_isSet = !json[QString("openTextField")].isNull() && m_open_text_field_isValid;

    m_payment_data_isValid = ::OpenAPI::fromJsonValue(m_payment_data, json[QString("paymentData")]);
    m_payment_data_isSet = !json[QString("paymentData")].isNull() && m_payment_data_isValid;

    m_sales_associate_data_isValid = ::OpenAPI::fromJsonValue(m_sales_associate_data, json[QString("salesAssociateData")]);
    m_sales_associate_data_isSet = !json[QString("salesAssociateData")].isNull() && m_sales_associate_data_isValid;

    m_shipping_data_isValid = ::OpenAPI::fromJsonValue(m_shipping_data, json[QString("shippingData")]);
    m_shipping_data_isSet = !json[QString("shippingData")].isNull() && m_shipping_data_isValid;
}

QString OAIPlaceOrder_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaceOrder_request::asJsonObject() const {
    QJsonObject obj;
    if (m_client_profile_data.isSet()) {
        obj.insert(QString("clientProfileData"), ::OpenAPI::toJsonValue(m_client_profile_data));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_marketing_data.isSet()) {
        obj.insert(QString("marketingData"), ::OpenAPI::toJsonValue(m_marketing_data));
    }
    if (m_open_text_field_isSet) {
        obj.insert(QString("openTextField"), ::OpenAPI::toJsonValue(m_open_text_field));
    }
    if (m_payment_data.isSet()) {
        obj.insert(QString("paymentData"), ::OpenAPI::toJsonValue(m_payment_data));
    }
    if (m_sales_associate_data.isSet()) {
        obj.insert(QString("salesAssociateData"), ::OpenAPI::toJsonValue(m_sales_associate_data));
    }
    if (m_shipping_data.isSet()) {
        obj.insert(QString("shippingData"), ::OpenAPI::toJsonValue(m_shipping_data));
    }
    return obj;
}

OAIPlaceOrder_request_clientProfileData OAIPlaceOrder_request::getClientProfileData() const {
    return m_client_profile_data;
}
void OAIPlaceOrder_request::setClientProfileData(const OAIPlaceOrder_request_clientProfileData &client_profile_data) {
    m_client_profile_data = client_profile_data;
    m_client_profile_data_isSet = true;
}

bool OAIPlaceOrder_request::is_client_profile_data_Set() const{
    return m_client_profile_data_isSet;
}

bool OAIPlaceOrder_request::is_client_profile_data_Valid() const{
    return m_client_profile_data_isValid;
}

QList<OAIPlaceOrder_request_items_inner> OAIPlaceOrder_request::getItems() const {
    return m_items;
}
void OAIPlaceOrder_request::setItems(const QList<OAIPlaceOrder_request_items_inner> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIPlaceOrder_request::is_items_Set() const{
    return m_items_isSet;
}

bool OAIPlaceOrder_request::is_items_Valid() const{
    return m_items_isValid;
}

OAIPlaceOrder_request_marketingData OAIPlaceOrder_request::getMarketingData() const {
    return m_marketing_data;
}
void OAIPlaceOrder_request::setMarketingData(const OAIPlaceOrder_request_marketingData &marketing_data) {
    m_marketing_data = marketing_data;
    m_marketing_data_isSet = true;
}

bool OAIPlaceOrder_request::is_marketing_data_Set() const{
    return m_marketing_data_isSet;
}

bool OAIPlaceOrder_request::is_marketing_data_Valid() const{
    return m_marketing_data_isValid;
}

QString OAIPlaceOrder_request::getOpenTextField() const {
    return m_open_text_field;
}
void OAIPlaceOrder_request::setOpenTextField(const QString &open_text_field) {
    m_open_text_field = open_text_field;
    m_open_text_field_isSet = true;
}

bool OAIPlaceOrder_request::is_open_text_field_Set() const{
    return m_open_text_field_isSet;
}

bool OAIPlaceOrder_request::is_open_text_field_Valid() const{
    return m_open_text_field_isValid;
}

OAIPlaceOrder_request_paymentData OAIPlaceOrder_request::getPaymentData() const {
    return m_payment_data;
}
void OAIPlaceOrder_request::setPaymentData(const OAIPlaceOrder_request_paymentData &payment_data) {
    m_payment_data = payment_data;
    m_payment_data_isSet = true;
}

bool OAIPlaceOrder_request::is_payment_data_Set() const{
    return m_payment_data_isSet;
}

bool OAIPlaceOrder_request::is_payment_data_Valid() const{
    return m_payment_data_isValid;
}

OAIAddMerchantContextData_request_salesAssociateData OAIPlaceOrder_request::getSalesAssociateData() const {
    return m_sales_associate_data;
}
void OAIPlaceOrder_request::setSalesAssociateData(const OAIAddMerchantContextData_request_salesAssociateData &sales_associate_data) {
    m_sales_associate_data = sales_associate_data;
    m_sales_associate_data_isSet = true;
}

bool OAIPlaceOrder_request::is_sales_associate_data_Set() const{
    return m_sales_associate_data_isSet;
}

bool OAIPlaceOrder_request::is_sales_associate_data_Valid() const{
    return m_sales_associate_data_isValid;
}

OAIPlaceOrder_request_shippingData OAIPlaceOrder_request::getShippingData() const {
    return m_shipping_data;
}
void OAIPlaceOrder_request::setShippingData(const OAIPlaceOrder_request_shippingData &shipping_data) {
    m_shipping_data = shipping_data;
    m_shipping_data_isSet = true;
}

bool OAIPlaceOrder_request::is_shipping_data_Set() const{
    return m_shipping_data_isSet;
}

bool OAIPlaceOrder_request::is_shipping_data_Valid() const{
    return m_shipping_data_isValid;
}

bool OAIPlaceOrder_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_profile_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_marketing_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_open_text_field_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_associate_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_data.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlaceOrder_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_client_profile_data_isValid && m_items_isValid && m_payment_data_isValid && m_shipping_data_isValid && true;
}

} // namespace OpenAPI
