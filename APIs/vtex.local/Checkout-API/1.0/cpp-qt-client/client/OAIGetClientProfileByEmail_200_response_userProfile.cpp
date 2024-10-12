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

#include "OAIGetClientProfileByEmail_200_response_userProfile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetClientProfileByEmail_200_response_userProfile::OAIGetClientProfileByEmail_200_response_userProfile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetClientProfileByEmail_200_response_userProfile::OAIGetClientProfileByEmail_200_response_userProfile() {
    this->initializeModel();
}

OAIGetClientProfileByEmail_200_response_userProfile::~OAIGetClientProfileByEmail_200_response_userProfile() {}

void OAIGetClientProfileByEmail_200_response_userProfile::initializeModel() {

    m_corporate_document_isSet = false;
    m_corporate_document_isValid = false;

    m_corporate_name_isSet = false;
    m_corporate_name_isValid = false;

    m_corporate_phone_isSet = false;
    m_corporate_phone_isValid = false;

    m_customer_class_isSet = false;
    m_customer_class_isValid = false;

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

    m_profile_complete_on_loading_isSet = false;
    m_profile_complete_on_loading_isValid = false;

    m_profile_error_on_loading_isSet = false;
    m_profile_error_on_loading_isValid = false;

    m_state_inscription_isSet = false;
    m_state_inscription_isValid = false;

    m_trade_name_isSet = false;
    m_trade_name_isValid = false;
}

void OAIGetClientProfileByEmail_200_response_userProfile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetClientProfileByEmail_200_response_userProfile::fromJsonObject(QJsonObject json) {

    m_corporate_document_isValid = ::OpenAPI::fromJsonValue(m_corporate_document, json[QString("corporateDocument")]);
    m_corporate_document_isSet = !json[QString("corporateDocument")].isNull() && m_corporate_document_isValid;

    m_corporate_name_isValid = ::OpenAPI::fromJsonValue(m_corporate_name, json[QString("corporateName")]);
    m_corporate_name_isSet = !json[QString("corporateName")].isNull() && m_corporate_name_isValid;

    m_corporate_phone_isValid = ::OpenAPI::fromJsonValue(m_corporate_phone, json[QString("corporatePhone")]);
    m_corporate_phone_isSet = !json[QString("corporatePhone")].isNull() && m_corporate_phone_isValid;

    m_customer_class_isValid = ::OpenAPI::fromJsonValue(m_customer_class, json[QString("customerClass")]);
    m_customer_class_isSet = !json[QString("customerClass")].isNull() && m_customer_class_isValid;

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

    m_profile_complete_on_loading_isValid = ::OpenAPI::fromJsonValue(m_profile_complete_on_loading, json[QString("profileCompleteOnLoading")]);
    m_profile_complete_on_loading_isSet = !json[QString("profileCompleteOnLoading")].isNull() && m_profile_complete_on_loading_isValid;

    m_profile_error_on_loading_isValid = ::OpenAPI::fromJsonValue(m_profile_error_on_loading, json[QString("profileErrorOnLoading")]);
    m_profile_error_on_loading_isSet = !json[QString("profileErrorOnLoading")].isNull() && m_profile_error_on_loading_isValid;

    m_state_inscription_isValid = ::OpenAPI::fromJsonValue(m_state_inscription, json[QString("stateInscription")]);
    m_state_inscription_isSet = !json[QString("stateInscription")].isNull() && m_state_inscription_isValid;

    m_trade_name_isValid = ::OpenAPI::fromJsonValue(m_trade_name, json[QString("tradeName")]);
    m_trade_name_isSet = !json[QString("tradeName")].isNull() && m_trade_name_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetClientProfileByEmail_200_response_userProfile::asJsonObject() const {
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
    if (m_customer_class_isSet) {
        obj.insert(QString("customerClass"), ::OpenAPI::toJsonValue(m_customer_class));
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
    if (m_profile_complete_on_loading_isSet) {
        obj.insert(QString("profileCompleteOnLoading"), ::OpenAPI::toJsonValue(m_profile_complete_on_loading));
    }
    if (m_profile_error_on_loading_isSet) {
        obj.insert(QString("profileErrorOnLoading"), ::OpenAPI::toJsonValue(m_profile_error_on_loading));
    }
    if (m_state_inscription_isSet) {
        obj.insert(QString("stateInscription"), ::OpenAPI::toJsonValue(m_state_inscription));
    }
    if (m_trade_name_isSet) {
        obj.insert(QString("tradeName"), ::OpenAPI::toJsonValue(m_trade_name));
    }
    return obj;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getCorporateDocument() const {
    return m_corporate_document;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setCorporateDocument(const QString &corporate_document) {
    m_corporate_document = corporate_document;
    m_corporate_document_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_corporate_document_Set() const{
    return m_corporate_document_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_corporate_document_Valid() const{
    return m_corporate_document_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getCorporateName() const {
    return m_corporate_name;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setCorporateName(const QString &corporate_name) {
    m_corporate_name = corporate_name;
    m_corporate_name_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_corporate_name_Set() const{
    return m_corporate_name_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_corporate_name_Valid() const{
    return m_corporate_name_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getCorporatePhone() const {
    return m_corporate_phone;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setCorporatePhone(const QString &corporate_phone) {
    m_corporate_phone = corporate_phone;
    m_corporate_phone_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_corporate_phone_Set() const{
    return m_corporate_phone_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_corporate_phone_Valid() const{
    return m_corporate_phone_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getCustomerClass() const {
    return m_customer_class;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setCustomerClass(const QString &customer_class) {
    m_customer_class = customer_class;
    m_customer_class_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_customer_class_Set() const{
    return m_customer_class_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_customer_class_Valid() const{
    return m_customer_class_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getDocument() const {
    return m_document;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setDocument(const QString &document) {
    m_document = document;
    m_document_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_document_Set() const{
    return m_document_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_document_Valid() const{
    return m_document_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getDocumentType() const {
    return m_document_type;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setDocumentType(const QString &document_type) {
    m_document_type = document_type;
    m_document_type_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_document_type_Set() const{
    return m_document_type_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_document_type_Valid() const{
    return m_document_type_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getEmail() const {
    return m_email;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_email_Set() const{
    return m_email_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_email_Valid() const{
    return m_email_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getFirstName() const {
    return m_first_name;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_first_name_Valid() const{
    return m_first_name_isValid;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::isIsCorporate() const {
    return m_is_corporate;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setIsCorporate(const bool &is_corporate) {
    m_is_corporate = is_corporate;
    m_is_corporate_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_is_corporate_Set() const{
    return m_is_corporate_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_is_corporate_Valid() const{
    return m_is_corporate_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getLastName() const {
    return m_last_name;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getPhone() const {
    return m_phone;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setPhone(const QString &phone) {
    m_phone = phone;
    m_phone_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_phone_Set() const{
    return m_phone_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_phone_Valid() const{
    return m_phone_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getProfileCompleteOnLoading() const {
    return m_profile_complete_on_loading;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setProfileCompleteOnLoading(const QString &profile_complete_on_loading) {
    m_profile_complete_on_loading = profile_complete_on_loading;
    m_profile_complete_on_loading_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_profile_complete_on_loading_Set() const{
    return m_profile_complete_on_loading_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_profile_complete_on_loading_Valid() const{
    return m_profile_complete_on_loading_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getProfileErrorOnLoading() const {
    return m_profile_error_on_loading;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setProfileErrorOnLoading(const QString &profile_error_on_loading) {
    m_profile_error_on_loading = profile_error_on_loading;
    m_profile_error_on_loading_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_profile_error_on_loading_Set() const{
    return m_profile_error_on_loading_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_profile_error_on_loading_Valid() const{
    return m_profile_error_on_loading_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getStateInscription() const {
    return m_state_inscription;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setStateInscription(const QString &state_inscription) {
    m_state_inscription = state_inscription;
    m_state_inscription_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_state_inscription_Set() const{
    return m_state_inscription_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_state_inscription_Valid() const{
    return m_state_inscription_isValid;
}

QString OAIGetClientProfileByEmail_200_response_userProfile::getTradeName() const {
    return m_trade_name;
}
void OAIGetClientProfileByEmail_200_response_userProfile::setTradeName(const QString &trade_name) {
    m_trade_name = trade_name;
    m_trade_name_isSet = true;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_trade_name_Set() const{
    return m_trade_name_isSet;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::is_trade_name_Valid() const{
    return m_trade_name_isValid;
}

bool OAIGetClientProfileByEmail_200_response_userProfile::isSet() const {
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

        if (m_customer_class_isSet) {
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

        if (m_profile_complete_on_loading_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile_error_on_loading_isSet) {
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

bool OAIGetClientProfileByEmail_200_response_userProfile::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
