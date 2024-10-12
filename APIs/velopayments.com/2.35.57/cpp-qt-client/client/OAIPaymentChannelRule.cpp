/**
 * Velo Payments APIs
 * ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response. 
 *
 * The version of the OpenAPI document: 2.35.57
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPaymentChannelRule.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPaymentChannelRule::OAIPaymentChannelRule(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPaymentChannelRule::OAIPaymentChannelRule() {
    this->initializeModel();
}

OAIPaymentChannelRule::~OAIPaymentChannelRule() {}

void OAIPaymentChannelRule::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_display_name_isSet = false;
    m_display_name_isValid = false;

    m_display_order_isSet = false;
    m_display_order_isValid = false;

    m_element_isSet = false;
    m_element_isValid = false;

    m_max_length_isSet = false;
    m_max_length_isValid = false;

    m_min_length_isSet = false;
    m_min_length_isValid = false;

    m_required_isSet = false;
    m_required_isValid = false;

    m_validation_isSet = false;
    m_validation_isValid = false;
}

void OAIPaymentChannelRule::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPaymentChannelRule::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_display_name_isValid = ::OpenAPI::fromJsonValue(m_display_name, json[QString("displayName")]);
    m_display_name_isSet = !json[QString("displayName")].isNull() && m_display_name_isValid;

    m_display_order_isValid = ::OpenAPI::fromJsonValue(m_display_order, json[QString("displayOrder")]);
    m_display_order_isSet = !json[QString("displayOrder")].isNull() && m_display_order_isValid;

    m_element_isValid = ::OpenAPI::fromJsonValue(m_element, json[QString("element")]);
    m_element_isSet = !json[QString("element")].isNull() && m_element_isValid;

    m_max_length_isValid = ::OpenAPI::fromJsonValue(m_max_length, json[QString("maxLength")]);
    m_max_length_isSet = !json[QString("maxLength")].isNull() && m_max_length_isValid;

    m_min_length_isValid = ::OpenAPI::fromJsonValue(m_min_length, json[QString("minLength")]);
    m_min_length_isSet = !json[QString("minLength")].isNull() && m_min_length_isValid;

    m_required_isValid = ::OpenAPI::fromJsonValue(m_required, json[QString("required")]);
    m_required_isSet = !json[QString("required")].isNull() && m_required_isValid;

    m_validation_isValid = ::OpenAPI::fromJsonValue(m_validation, json[QString("validation")]);
    m_validation_isSet = !json[QString("validation")].isNull() && m_validation_isValid;
}

QString OAIPaymentChannelRule::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPaymentChannelRule::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_display_name_isSet) {
        obj.insert(QString("displayName"), ::OpenAPI::toJsonValue(m_display_name));
    }
    if (m_display_order_isSet) {
        obj.insert(QString("displayOrder"), ::OpenAPI::toJsonValue(m_display_order));
    }
    if (m_element_isSet) {
        obj.insert(QString("element"), ::OpenAPI::toJsonValue(m_element));
    }
    if (m_max_length_isSet) {
        obj.insert(QString("maxLength"), ::OpenAPI::toJsonValue(m_max_length));
    }
    if (m_min_length_isSet) {
        obj.insert(QString("minLength"), ::OpenAPI::toJsonValue(m_min_length));
    }
    if (m_required_isSet) {
        obj.insert(QString("required"), ::OpenAPI::toJsonValue(m_required));
    }
    if (m_validation_isSet) {
        obj.insert(QString("validation"), ::OpenAPI::toJsonValue(m_validation));
    }
    return obj;
}

QString OAIPaymentChannelRule::getDescription() const {
    return m_description;
}
void OAIPaymentChannelRule::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIPaymentChannelRule::is_description_Set() const{
    return m_description_isSet;
}

bool OAIPaymentChannelRule::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIPaymentChannelRule::getDisplayName() const {
    return m_display_name;
}
void OAIPaymentChannelRule::setDisplayName(const QString &display_name) {
    m_display_name = display_name;
    m_display_name_isSet = true;
}

bool OAIPaymentChannelRule::is_display_name_Set() const{
    return m_display_name_isSet;
}

bool OAIPaymentChannelRule::is_display_name_Valid() const{
    return m_display_name_isValid;
}

qint32 OAIPaymentChannelRule::getDisplayOrder() const {
    return m_display_order;
}
void OAIPaymentChannelRule::setDisplayOrder(const qint32 &display_order) {
    m_display_order = display_order;
    m_display_order_isSet = true;
}

bool OAIPaymentChannelRule::is_display_order_Set() const{
    return m_display_order_isSet;
}

bool OAIPaymentChannelRule::is_display_order_Valid() const{
    return m_display_order_isValid;
}

QString OAIPaymentChannelRule::getElement() const {
    return m_element;
}
void OAIPaymentChannelRule::setElement(const QString &element) {
    m_element = element;
    m_element_isSet = true;
}

bool OAIPaymentChannelRule::is_element_Set() const{
    return m_element_isSet;
}

bool OAIPaymentChannelRule::is_element_Valid() const{
    return m_element_isValid;
}

qint32 OAIPaymentChannelRule::getMaxLength() const {
    return m_max_length;
}
void OAIPaymentChannelRule::setMaxLength(const qint32 &max_length) {
    m_max_length = max_length;
    m_max_length_isSet = true;
}

bool OAIPaymentChannelRule::is_max_length_Set() const{
    return m_max_length_isSet;
}

bool OAIPaymentChannelRule::is_max_length_Valid() const{
    return m_max_length_isValid;
}

qint32 OAIPaymentChannelRule::getMinLength() const {
    return m_min_length;
}
void OAIPaymentChannelRule::setMinLength(const qint32 &min_length) {
    m_min_length = min_length;
    m_min_length_isSet = true;
}

bool OAIPaymentChannelRule::is_min_length_Set() const{
    return m_min_length_isSet;
}

bool OAIPaymentChannelRule::is_min_length_Valid() const{
    return m_min_length_isValid;
}

bool OAIPaymentChannelRule::isRequired() const {
    return m_required;
}
void OAIPaymentChannelRule::setRequired(const bool &required) {
    m_required = required;
    m_required_isSet = true;
}

bool OAIPaymentChannelRule::is_required_Set() const{
    return m_required_isSet;
}

bool OAIPaymentChannelRule::is_required_Valid() const{
    return m_required_isValid;
}

QString OAIPaymentChannelRule::getValidation() const {
    return m_validation;
}
void OAIPaymentChannelRule::setValidation(const QString &validation) {
    m_validation = validation;
    m_validation_isSet = true;
}

bool OAIPaymentChannelRule::is_validation_Set() const{
    return m_validation_isSet;
}

bool OAIPaymentChannelRule::is_validation_Valid() const{
    return m_validation_isValid;
}

bool OAIPaymentChannelRule::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_display_order_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_element_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_max_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_min_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_required_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_validation_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPaymentChannelRule::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_display_name_isValid && m_element_isValid && m_required_isValid && m_validation_isValid && true;
}

} // namespace OpenAPI
