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

#include "OAIPlaceOrder_request_clientProfileData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlaceOrder_request_clientProfileData::OAIPlaceOrder_request_clientProfileData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlaceOrder_request_clientProfileData::OAIPlaceOrder_request_clientProfileData() {
    this->initializeModel();
}

OAIPlaceOrder_request_clientProfileData::~OAIPlaceOrder_request_clientProfileData() {}

void OAIPlaceOrder_request_clientProfileData::initializeModel() {

    m_corporate_document_isSet = false;
    m_corporate_document_isValid = false;

    m_corporate_name_isSet = false;
    m_corporate_name_isValid = false;

    m_corporate_phone_isSet = false;
    m_corporate_phone_isValid = false;

    m_document_isSet = false;
    m_document_isValid = false;

    m_document_type_isSet = false;
    m_document_type_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_is_corporate_isSet = false;
    m_is_corporate_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_phone_isSet = false;
    m_phone_isValid = false;

    m_state_inscription_isSet = false;
    m_state_inscription_isValid = false;

    m_trade_name_isSet = false;
    m_trade_name_isValid = false;
}

void OAIPlaceOrder_request_clientProfileData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlaceOrder_request_clientProfileData::fromJsonObject(QJsonObject json) {

    m_corporate_document_isValid = ::OpenAPI::fromJsonValue(m_corporate_document, json[QString("corporateDocument")]);
    m_corporate_document_isSet = !json[QString("corporateDocument")].isNull() && m_corporate_document_isValid;

    m_corporate_name_isValid = ::OpenAPI::fromJsonValue(m_corporate_name, json[QString("corporateName")]);
    m_corporate_name_isSet = !json[QString("corporateName")].isNull() && m_corporate_name_isValid;

    m_corporate_phone_isValid = ::OpenAPI::fromJsonValue(m_corporate_phone, json[QString("corporatePhone")]);
    m_corporate_phone_isSet = !json[QString("corporatePhone")].isNull() && m_corporate_phone_isValid;

    m_document_isValid = ::OpenAPI::fromJsonValue(m_document, json[QString("document")]);
    m_document_isSet = !json[QString("document")].isNull() && m_document_isValid;

    m_document_type_isValid = ::OpenAPI::fromJsonValue(m_document_type, json[QString("documentType")]);
    m_document_type_isSet = !json[QString("documentType")].isNull() && m_document_type_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("firstName")]);
    m_first_name_isSet = !json[QString("firstName")].isNull() && m_first_name_isValid;

    m_is_corporate_isValid = ::OpenAPI::fromJsonValue(m_is_corporate, json[QString("isCorporate")]);
    m_is_corporate_isSet = !json[QString("isCorporate")].isNull() && m_is_corporate_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("lastName")]);
    m_last_name_isSet = !json[QString("lastName")].isNull() && m_last_name_isValid;

    m_phone_isValid = ::OpenAPI::fromJsonValue(m_phone, json[QString("phone")]);
    m_phone_isSet = !json[QString("phone")].isNull() && m_phone_isValid;

    m_state_inscription_isValid = ::OpenAPI::fromJsonValue(m_state_inscription, json[QString("stateInscription")]);
    m_state_inscription_isSet = !json[QString("stateInscription")].isNull() && m_state_inscription_isValid;

    m_trade_name_isValid = ::OpenAPI::fromJsonValue(m_trade_name, json[QString("tradeName")]);
    m_trade_name_isSet = !json[QString("tradeName")].isNull() && m_trade_name_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlaceOrder_request_clientProfileData::asJsonObject() const {
    QJsonObject obj;
    if (m_corporate_document_isSet) {
        obj.insert(QString("corporateDocument"), ::OpenAPI::toJsonValue(m_corporate_document));
    }
    if (m_corporate_name_isSet) {
        obj.insert(QString("corporateName"), ::OpenAPI::toJsonValue(m_corporate_name));
    }
    if (m_corporate_phone_isSet) {
        obj.insert(QString("corporatePhone"), ::OpenAPI::toJsonValue(m_corporate_phone));
    }
    if (m_document_isSet) {
        obj.insert(QString("document"), ::OpenAPI::toJsonValue(m_document));
    }
    if (m_document_type_isSet) {
        obj.insert(QString("documentType"), ::OpenAPI::toJsonValue(m_document_type));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("firstName"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_is_corporate_isSet) {
        obj.insert(QString("isCorporate"), ::OpenAPI::toJsonValue(m_is_corporate));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("lastName"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_phone_isSet) {
        obj.insert(QString("phone"), ::OpenAPI::toJsonValue(m_phone));
    }
    if (m_state_inscription_isSet) {
        obj.insert(QString("stateInscription"), ::OpenAPI::toJsonValue(m_state_inscription));
    }
    if (m_trade_name_isSet) {
        obj.insert(QString("tradeName"), ::OpenAPI::toJsonValue(m_trade_name));
    }
    return obj;
}

QString OAIPlaceOrder_request_clientProfileData::getCorporateDocument() const {
    return m_corporate_document;
}
void OAIPlaceOrder_request_clientProfileData::setCorporateDocument(const QString &corporate_document) {
    m_corporate_document = corporate_document;
    m_corporate_document_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_corporate_document_Set() const{
    return m_corporate_document_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_corporate_document_Valid() const{
    return m_corporate_document_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::getCorporateName() const {
    return m_corporate_name;
}
void OAIPlaceOrder_request_clientProfileData::setCorporateName(const QString &corporate_name) {
    m_corporate_name = corporate_name;
    m_corporate_name_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_corporate_name_Set() const{
    return m_corporate_name_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_corporate_name_Valid() const{
    return m_corporate_name_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::getCorporatePhone() const {
    return m_corporate_phone;
}
void OAIPlaceOrder_request_clientProfileData::setCorporatePhone(const QString &corporate_phone) {
    m_corporate_phone = corporate_phone;
    m_corporate_phone_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_corporate_phone_Set() const{
    return m_corporate_phone_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_corporate_phone_Valid() const{
    return m_corporate_phone_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::getDocument() const {
    return m_document;
}
void OAIPlaceOrder_request_clientProfileData::setDocument(const QString &document) {
    m_document = document;
    m_document_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_document_Set() const{
    return m_document_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_document_Valid() const{
    return m_document_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::getDocumentType() const {
    return m_document_type;
}
void OAIPlaceOrder_request_clientProfileData::setDocumentType(const QString &document_type) {
    m_document_type = document_type;
    m_document_type_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_document_type_Set() const{
    return m_document_type_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_document_type_Valid() const{
    return m_document_type_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::getEmail() const {
    return m_email;
}
void OAIPlaceOrder_request_clientProfileData::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_email_Set() const{
    return m_email_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::getFirstName() const {
    return m_first_name;
}
void OAIPlaceOrder_request_clientProfileData::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_first_name_Valid() const{
    return m_first_name_isValid;
}

bool OAIPlaceOrder_request_clientProfileData::isIsCorporate() const {
    return m_is_corporate;
}
void OAIPlaceOrder_request_clientProfileData::setIsCorporate(const bool &is_corporate) {
    m_is_corporate = is_corporate;
    m_is_corporate_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_is_corporate_Set() const{
    return m_is_corporate_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_is_corporate_Valid() const{
    return m_is_corporate_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::getLastName() const {
    return m_last_name;
}
void OAIPlaceOrder_request_clientProfileData::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::getPhone() const {
    return m_phone;
}
void OAIPlaceOrder_request_clientProfileData::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_phone_Valid() const{
    return m_phone_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::getStateInscription() const {
    return m_state_inscription;
}
void OAIPlaceOrder_request_clientProfileData::setStateInscription(const QString &state_inscription) {
    m_state_inscription = state_inscription;
    m_state_inscription_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_state_inscription_Set() const{
    return m_state_inscription_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_state_inscription_Valid() const{
    return m_state_inscription_isValid;
}

QString OAIPlaceOrder_request_clientProfileData::getTradeName() const {
    return m_trade_name;
}
void OAIPlaceOrder_request_clientProfileData::setTradeName(const QString &trade_name) {
    m_trade_name = trade_name;
    m_trade_name_isSet = true;
}

bool OAIPlaceOrder_request_clientProfileData::is_trade_name_Set() const{
    return m_trade_name_isSet;
}

bool OAIPlaceOrder_request_clientProfileData::is_trade_name_Valid() const{
    return m_trade_name_isValid;
}

bool OAIPlaceOrder_request_clientProfileData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_corporate_document_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_corporate_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_corporate_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_document_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_document_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_corporate_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_inscription_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trade_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlaceOrder_request_clientProfileData::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_email_isValid && true;
}

} // namespace OpenAPI
