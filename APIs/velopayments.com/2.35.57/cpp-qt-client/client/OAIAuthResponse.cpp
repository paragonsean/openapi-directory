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

#include "OAIAuthResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuthResponse::OAIAuthResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuthResponse::OAIAuthResponse() {
    this->initializeModel();
}

OAIAuthResponse::~OAIAuthResponse() {}

void OAIAuthResponse::initializeModel() {

    m_access_token_isSet = false;
    m_access_token_isValid = false;

    m_entity_ids_isSet = false;
    m_entity_ids_isValid = false;

    m_expires_in_isSet = false;
    m_expires_in_isValid = false;

    m_refresh_token_isSet = false;
    m_refresh_token_isValid = false;

    m_scope_isSet = false;
    m_scope_isValid = false;

    m_token_type_isSet = false;
    m_token_type_isValid = false;
}

void OAIAuthResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuthResponse::fromJsonObject(QJsonObject json) {

    m_access_token_isValid = ::OpenAPI::fromJsonValue(m_access_token, json[QString("access_token")]);
    m_access_token_isSet = !json[QString("access_token")].isNull() && m_access_token_isValid;

    m_entity_ids_isValid = ::OpenAPI::fromJsonValue(m_entity_ids, json[QString("entityIds")]);
    m_entity_ids_isSet = !json[QString("entityIds")].isNull() && m_entity_ids_isValid;

    m_expires_in_isValid = ::OpenAPI::fromJsonValue(m_expires_in, json[QString("expires_in")]);
    m_expires_in_isSet = !json[QString("expires_in")].isNull() && m_expires_in_isValid;

    m_refresh_token_isValid = ::OpenAPI::fromJsonValue(m_refresh_token, json[QString("refresh_token")]);
    m_refresh_token_isSet = !json[QString("refresh_token")].isNull() && m_refresh_token_isValid;

    m_scope_isValid = ::OpenAPI::fromJsonValue(m_scope, json[QString("scope")]);
    m_scope_isSet = !json[QString("scope")].isNull() && m_scope_isValid;

    m_token_type_isValid = ::OpenAPI::fromJsonValue(m_token_type, json[QString("token_type")]);
    m_token_type_isSet = !json[QString("token_type")].isNull() && m_token_type_isValid;
}

QString OAIAuthResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuthResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_access_token_isSet) {
        obj.insert(QString("access_token"), ::OpenAPI::toJsonValue(m_access_token));
    }
    if (m_entity_ids.size() > 0) {
        obj.insert(QString("entityIds"), ::OpenAPI::toJsonValue(m_entity_ids));
    }
    if (m_expires_in_isSet) {
        obj.insert(QString("expires_in"), ::OpenAPI::toJsonValue(m_expires_in));
    }
    if (m_refresh_token_isSet) {
        obj.insert(QString("refresh_token"), ::OpenAPI::toJsonValue(m_refresh_token));
    }
    if (m_scope_isSet) {
        obj.insert(QString("scope"), ::OpenAPI::toJsonValue(m_scope));
    }
    if (m_token_type_isSet) {
        obj.insert(QString("token_type"), ::OpenAPI::toJsonValue(m_token_type));
    }
    return obj;
}

QString OAIAuthResponse::getAccessToken() const {
    return m_access_token;
}
void OAIAuthResponse::setAccessToken(const QString &access_token) {
    m_access_token = access_token;
    m_access_token_isSet = true;
}

bool OAIAuthResponse::is_access_token_Set() const{
    return m_access_token_isSet;
}

bool OAIAuthResponse::is_access_token_Valid() const{
    return m_access_token_isValid;
}

QList<QString> OAIAuthResponse::getEntityIds() const {
    return m_entity_ids;
}
void OAIAuthResponse::setEntityIds(const QList<QString> &entity_ids) {
    m_entity_ids = entity_ids;
    m_entity_ids_isSet = true;
}

bool OAIAuthResponse::is_entity_ids_Set() const{
    return m_entity_ids_isSet;
}

bool OAIAuthResponse::is_entity_ids_Valid() const{
    return m_entity_ids_isValid;
}

double OAIAuthResponse::getExpiresIn() const {
    return m_expires_in;
}
void OAIAuthResponse::setExpiresIn(const double &expires_in) {
    m_expires_in = expires_in;
    m_expires_in_isSet = true;
}

bool OAIAuthResponse::is_expires_in_Set() const{
    return m_expires_in_isSet;
}

bool OAIAuthResponse::is_expires_in_Valid() const{
    return m_expires_in_isValid;
}

QString OAIAuthResponse::getRefreshToken() const {
    return m_refresh_token;
}
void OAIAuthResponse::setRefreshToken(const QString &refresh_token) {
    m_refresh_token = refresh_token;
    m_refresh_token_isSet = true;
}

bool OAIAuthResponse::is_refresh_token_Set() const{
    return m_refresh_token_isSet;
}

bool OAIAuthResponse::is_refresh_token_Valid() const{
    return m_refresh_token_isValid;
}

QString OAIAuthResponse::getScope() const {
    return m_scope;
}
void OAIAuthResponse::setScope(const QString &scope) {
    m_scope = scope;
    m_scope_isSet = true;
}

bool OAIAuthResponse::is_scope_Set() const{
    return m_scope_isSet;
}

bool OAIAuthResponse::is_scope_Valid() const{
    return m_scope_isValid;
}

QString OAIAuthResponse::getTokenType() const {
    return m_token_type;
}
void OAIAuthResponse::setTokenType(const QString &token_type) {
    m_token_type = token_type;
    m_token_type_isSet = true;
}

bool OAIAuthResponse::is_token_type_Set() const{
    return m_token_type_isSet;
}

bool OAIAuthResponse::is_token_type_Valid() const{
    return m_token_type_isValid;
}

bool OAIAuthResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_access_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity_ids.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_expires_in_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_refresh_token_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scope_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_token_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAuthResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_access_token_isValid && m_token_type_isValid && true;
}

} // namespace OpenAPI
