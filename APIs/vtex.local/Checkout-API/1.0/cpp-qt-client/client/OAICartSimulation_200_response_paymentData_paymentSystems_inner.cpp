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

#include "OAICartSimulation_200_response_paymentData_paymentSystems_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICartSimulation_200_response_paymentData_paymentSystems_inner::OAICartSimulation_200_response_paymentData_paymentSystems_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICartSimulation_200_response_paymentData_paymentSystems_inner::OAICartSimulation_200_response_paymentData_paymentSystems_inner() {
    this->initializeModel();
}

OAICartSimulation_200_response_paymentData_paymentSystems_inner::~OAICartSimulation_200_response_paymentData_paymentSystems_inner() {}

void OAICartSimulation_200_response_paymentData_paymentSystems_inner::initializeModel() {

    m_available_payments_isSet = false;
    m_available_payments_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_display_document_isSet = false;
    m_display_document_isValid = false;

    m_due_date_isSet = false;
    m_due_date_isValid = false;

    m_group_name_isSet = false;
    m_group_name_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_custom_isSet = false;
    m_is_custom_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_requires_authentication_isSet = false;
    m_requires_authentication_isValid = false;

    m_requires_document_isSet = false;
    m_requires_document_isValid = false;

    m_string_id_isSet = false;
    m_string_id_isValid = false;

    m_r_template_isSet = false;
    m_r_template_isValid = false;

    m_validator_isSet = false;
    m_validator_isValid = false;
}

void OAICartSimulation_200_response_paymentData_paymentSystems_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICartSimulation_200_response_paymentData_paymentSystems_inner::fromJsonObject(QJsonObject json) {

    m_available_payments_isValid = ::OpenAPI::fromJsonValue(m_available_payments, json[QString("availablePayments")]);
    m_available_payments_isSet = !json[QString("availablePayments")].isNull() && m_available_payments_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_display_document_isValid = ::OpenAPI::fromJsonValue(m_display_document, json[QString("displayDocument")]);
    m_display_document_isSet = !json[QString("displayDocument")].isNull() && m_display_document_isValid;

    m_due_date_isValid = ::OpenAPI::fromJsonValue(m_due_date, json[QString("dueDate")]);
    m_due_date_isSet = !json[QString("dueDate")].isNull() && m_due_date_isValid;

    m_group_name_isValid = ::OpenAPI::fromJsonValue(m_group_name, json[QString("groupName")]);
    m_group_name_isSet = !json[QString("groupName")].isNull() && m_group_name_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_custom_isValid = ::OpenAPI::fromJsonValue(m_is_custom, json[QString("isCustom")]);
    m_is_custom_isSet = !json[QString("isCustom")].isNull() && m_is_custom_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_requires_authentication_isValid = ::OpenAPI::fromJsonValue(m_requires_authentication, json[QString("requiresAuthentication")]);
    m_requires_authentication_isSet = !json[QString("requiresAuthentication")].isNull() && m_requires_authentication_isValid;

    m_requires_document_isValid = ::OpenAPI::fromJsonValue(m_requires_document, json[QString("requiresDocument")]);
    m_requires_document_isSet = !json[QString("requiresDocument")].isNull() && m_requires_document_isValid;

    m_string_id_isValid = ::OpenAPI::fromJsonValue(m_string_id, json[QString("stringId")]);
    m_string_id_isSet = !json[QString("stringId")].isNull() && m_string_id_isValid;

    m_r_template_isValid = ::OpenAPI::fromJsonValue(m_r_template, json[QString("template")]);
    m_r_template_isSet = !json[QString("template")].isNull() && m_r_template_isValid;

    m_validator_isValid = ::OpenAPI::fromJsonValue(m_validator, json[QString("validator")]);
    m_validator_isSet = !json[QString("validator")].isNull() && m_validator_isValid;
}

QString OAICartSimulation_200_response_paymentData_paymentSystems_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICartSimulation_200_response_paymentData_paymentSystems_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_available_payments_isSet) {
        obj.insert(QString("availablePayments"), ::OpenAPI::toJsonValue(m_available_payments));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_display_document_isSet) {
        obj.insert(QString("displayDocument"), ::OpenAPI::toJsonValue(m_display_document));
    }
    if (m_due_date_isSet) {
        obj.insert(QString("dueDate"), ::OpenAPI::toJsonValue(m_due_date));
    }
    if (m_group_name_isSet) {
        obj.insert(QString("groupName"), ::OpenAPI::toJsonValue(m_group_name));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_custom_isSet) {
        obj.insert(QString("isCustom"), ::OpenAPI::toJsonValue(m_is_custom));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_requires_authentication_isSet) {
        obj.insert(QString("requiresAuthentication"), ::OpenAPI::toJsonValue(m_requires_authentication));
    }
    if (m_requires_document_isSet) {
        obj.insert(QString("requiresDocument"), ::OpenAPI::toJsonValue(m_requires_document));
    }
    if (m_string_id_isSet) {
        obj.insert(QString("stringId"), ::OpenAPI::toJsonValue(m_string_id));
    }
    if (m_r_template_isSet) {
        obj.insert(QString("template"), ::OpenAPI::toJsonValue(m_r_template));
    }
    if (m_validator_isSet) {
        obj.insert(QString("validator"), ::OpenAPI::toJsonValue(m_validator));
    }
    return obj;
}

QString OAICartSimulation_200_response_paymentData_paymentSystems_inner::getAvailablePayments() const {
    return m_available_payments;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setAvailablePayments(const QString &available_payments) {
    m_available_payments = available_payments;
    m_available_payments_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_available_payments_Set() const{
    return m_available_payments_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_available_payments_Valid() const{
    return m_available_payments_isValid;
}

QString OAICartSimulation_200_response_paymentData_paymentSystems_inner::getDescription() const {
    return m_description;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_description_Valid() const{
    return m_description_isValid;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::isDisplayDocument() const {
    return m_display_document;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setDisplayDocument(const bool &display_document) {
    m_display_document = display_document;
    m_display_document_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_display_document_Set() const{
    return m_display_document_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_display_document_Valid() const{
    return m_display_document_isValid;
}

QString OAICartSimulation_200_response_paymentData_paymentSystems_inner::getDueDate() const {
    return m_due_date;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setDueDate(const QString &due_date) {
    m_due_date = due_date;
    m_due_date_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_due_date_Set() const{
    return m_due_date_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_due_date_Valid() const{
    return m_due_date_isValid;
}

QString OAICartSimulation_200_response_paymentData_paymentSystems_inner::getGroupName() const {
    return m_group_name;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setGroupName(const QString &group_name) {
    m_group_name = group_name;
    m_group_name_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_group_name_Set() const{
    return m_group_name_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_group_name_Valid() const{
    return m_group_name_isValid;
}

qint32 OAICartSimulation_200_response_paymentData_paymentSystems_inner::getId() const {
    return m_id;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_id_Valid() const{
    return m_id_isValid;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::isIsCustom() const {
    return m_is_custom;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setIsCustom(const bool &is_custom) {
    m_is_custom = is_custom;
    m_is_custom_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_is_custom_Set() const{
    return m_is_custom_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_is_custom_Valid() const{
    return m_is_custom_isValid;
}

QString OAICartSimulation_200_response_paymentData_paymentSystems_inner::getName() const {
    return m_name;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_name_Valid() const{
    return m_name_isValid;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::isRequiresAuthentication() const {
    return m_requires_authentication;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setRequiresAuthentication(const bool &requires_authentication) {
    m_requires_authentication = requires_authentication;
    m_requires_authentication_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_requires_authentication_Set() const{
    return m_requires_authentication_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_requires_authentication_Valid() const{
    return m_requires_authentication_isValid;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::isRequiresDocument() const {
    return m_requires_document;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setRequiresDocument(const bool &requires_document) {
    m_requires_document = requires_document;
    m_requires_document_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_requires_document_Set() const{
    return m_requires_document_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_requires_document_Valid() const{
    return m_requires_document_isValid;
}

QString OAICartSimulation_200_response_paymentData_paymentSystems_inner::getStringId() const {
    return m_string_id;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setStringId(const QString &string_id) {
    m_string_id = string_id;
    m_string_id_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_string_id_Set() const{
    return m_string_id_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_string_id_Valid() const{
    return m_string_id_isValid;
}

QString OAICartSimulation_200_response_paymentData_paymentSystems_inner::getRTemplate() const {
    return m_r_template;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setRTemplate(const QString &r_template) {
    m_r_template = r_template;
    m_r_template_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_r_template_Set() const{
    return m_r_template_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_r_template_Valid() const{
    return m_r_template_isValid;
}

OAIObject OAICartSimulation_200_response_paymentData_paymentSystems_inner::getValidator() const {
    return m_validator;
}
void OAICartSimulation_200_response_paymentData_paymentSystems_inner::setValidator(const OAIObject &validator) {
    m_validator = validator;
    m_validator_isSet = true;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_validator_Set() const{
    return m_validator_isSet;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::is_validator_Valid() const{
    return m_validator_isValid;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_available_payments_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_document_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_due_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_custom_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_requires_authentication_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_requires_document_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_string_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_template_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_validator_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICartSimulation_200_response_paymentData_paymentSystems_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
