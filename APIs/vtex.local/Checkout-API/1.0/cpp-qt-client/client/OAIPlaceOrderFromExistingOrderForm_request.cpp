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

#include "OAIPlaceOrderFromExistingOrderForm_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaceOrderFromExistingOrderForm_request::OAIPlaceOrderFromExistingOrderForm_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaceOrderFromExistingOrderForm_request::OAIPlaceOrderFromExistingOrderForm_request() {
    this->initializeModel();
}

OAIPlaceOrderFromExistingOrderForm_request::~OAIPlaceOrderFromExistingOrderForm_request() {}

void OAIPlaceOrderFromExistingOrderForm_request::initializeModel() {

    m_interest_value_isSet = false;
    m_interest_value_isValid = false;

    m_optin_news_letter_isSet = false;
    m_optin_news_letter_isValid = false;

    m_reference_id_isSet = false;
    m_reference_id_isValid = false;

    m_reference_value_isSet = false;
    m_reference_value_isValid = false;

    m_save_personal_data_isSet = false;
    m_save_personal_data_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIPlaceOrderFromExistingOrderForm_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaceOrderFromExistingOrderForm_request::fromJsonObject(QJsonObject json) {

    m_interest_value_isValid = ::OpenAPI::fromJsonValue(m_interest_value, json[QString("interestValue")]);
    m_interest_value_isSet = !json[QString("interestValue")].isNull() && m_interest_value_isValid;

    m_optin_news_letter_isValid = ::OpenAPI::fromJsonValue(m_optin_news_letter, json[QString("optinNewsLetter")]);
    m_optin_news_letter_isSet = !json[QString("optinNewsLetter")].isNull() && m_optin_news_letter_isValid;

    m_reference_id_isValid = ::OpenAPI::fromJsonValue(m_reference_id, json[QString("referenceId")]);
    m_reference_id_isSet = !json[QString("referenceId")].isNull() && m_reference_id_isValid;

    m_reference_value_isValid = ::OpenAPI::fromJsonValue(m_reference_value, json[QString("referenceValue")]);
    m_reference_value_isSet = !json[QString("referenceValue")].isNull() && m_reference_value_isValid;

    m_save_personal_data_isValid = ::OpenAPI::fromJsonValue(m_save_personal_data, json[QString("savePersonalData")]);
    m_save_personal_data_isSet = !json[QString("savePersonalData")].isNull() && m_save_personal_data_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIPlaceOrderFromExistingOrderForm_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaceOrderFromExistingOrderForm_request::asJsonObject() const {
    QJsonObject obj;
    if (m_interest_value_isSet) {
        obj.insert(QString("interestValue"), ::OpenAPI::toJsonValue(m_interest_value));
    }
    if (m_optin_news_letter_isSet) {
        obj.insert(QString("optinNewsLetter"), ::OpenAPI::toJsonValue(m_optin_news_letter));
    }
    if (m_reference_id_isSet) {
        obj.insert(QString("referenceId"), ::OpenAPI::toJsonValue(m_reference_id));
    }
    if (m_reference_value_isSet) {
        obj.insert(QString("referenceValue"), ::OpenAPI::toJsonValue(m_reference_value));
    }
    if (m_save_personal_data_isSet) {
        obj.insert(QString("savePersonalData"), ::OpenAPI::toJsonValue(m_save_personal_data));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

qint32 OAIPlaceOrderFromExistingOrderForm_request::getInterestValue() const {
    return m_interest_value;
}
void OAIPlaceOrderFromExistingOrderForm_request::setInterestValue(const qint32 &interest_value) {
    m_interest_value = interest_value;
    m_interest_value_isSet = true;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_interest_value_Set() const{
    return m_interest_value_isSet;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_interest_value_Valid() const{
    return m_interest_value_isValid;
}

bool OAIPlaceOrderFromExistingOrderForm_request::isOptinNewsLetter() const {
    return m_optin_news_letter;
}
void OAIPlaceOrderFromExistingOrderForm_request::setOptinNewsLetter(const bool &optin_news_letter) {
    m_optin_news_letter = optin_news_letter;
    m_optin_news_letter_isSet = true;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_optin_news_letter_Set() const{
    return m_optin_news_letter_isSet;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_optin_news_letter_Valid() const{
    return m_optin_news_letter_isValid;
}

QString OAIPlaceOrderFromExistingOrderForm_request::getReferenceId() const {
    return m_reference_id;
}
void OAIPlaceOrderFromExistingOrderForm_request::setReferenceId(const QString &reference_id) {
    m_reference_id = reference_id;
    m_reference_id_isSet = true;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_reference_id_Set() const{
    return m_reference_id_isSet;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_reference_id_Valid() const{
    return m_reference_id_isValid;
}

qint32 OAIPlaceOrderFromExistingOrderForm_request::getReferenceValue() const {
    return m_reference_value;
}
void OAIPlaceOrderFromExistingOrderForm_request::setReferenceValue(const qint32 &reference_value) {
    m_reference_value = reference_value;
    m_reference_value_isSet = true;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_reference_value_Set() const{
    return m_reference_value_isSet;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_reference_value_Valid() const{
    return m_reference_value_isValid;
}

bool OAIPlaceOrderFromExistingOrderForm_request::isSavePersonalData() const {
    return m_save_personal_data;
}
void OAIPlaceOrderFromExistingOrderForm_request::setSavePersonalData(const bool &save_personal_data) {
    m_save_personal_data = save_personal_data;
    m_save_personal_data_isSet = true;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_save_personal_data_Set() const{
    return m_save_personal_data_isSet;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_save_personal_data_Valid() const{
    return m_save_personal_data_isValid;
}

qint32 OAIPlaceOrderFromExistingOrderForm_request::getValue() const {
    return m_value;
}
void OAIPlaceOrderFromExistingOrderForm_request::setValue(const qint32 &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_value_Set() const{
    return m_value_isSet;
}

bool OAIPlaceOrderFromExistingOrderForm_request::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIPlaceOrderFromExistingOrderForm_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_interest_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_optin_news_letter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_value_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_save_personal_data_isSet) {
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

bool OAIPlaceOrderFromExistingOrderForm_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_interest_value_isValid && m_reference_id_isValid && m_reference_value_isValid && m_value_isValid && true;
}

} // namespace OpenAPI
