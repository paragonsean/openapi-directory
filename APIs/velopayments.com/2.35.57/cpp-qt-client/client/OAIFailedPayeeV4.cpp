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

#include "OAIFailedPayeeV4.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFailedPayeeV4::OAIFailedPayeeV4(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFailedPayeeV4::OAIFailedPayeeV4() {
    this->initializeModel();
}

OAIFailedPayeeV4::~OAIFailedPayeeV4() {}

void OAIFailedPayeeV4::initializeModel() {

    m_address_isSet = false;
    m_address_isValid = false;

    m_challenge_isSet = false;
    m_challenge_isValid = false;

    m_company_isSet = false;
    m_company_isValid = false;

    m_email_isSet = false;
    m_email_isValid = false;

    m_individual_isSet = false;
    m_individual_isValid = false;

    m_language_isSet = false;
    m_language_isValid = false;

    m_payee_id_isSet = false;
    m_payee_id_isValid = false;

    m_payment_channel_isSet = false;
    m_payment_channel_isValid = false;

    m_payor_refs_isSet = false;
    m_payor_refs_isValid = false;

    m_remote_id_isSet = false;
    m_remote_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIFailedPayeeV4::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFailedPayeeV4::fromJsonObject(QJsonObject json) {

    m_address_isValid = ::OpenAPI::fromJsonValue(m_address, json[QString("address")]);
    m_address_isSet = !json[QString("address")].isNull() && m_address_isValid;

    m_challenge_isValid = ::OpenAPI::fromJsonValue(m_challenge, json[QString("challenge")]);
    m_challenge_isSet = !json[QString("challenge")].isNull() && m_challenge_isValid;

    m_company_isValid = ::OpenAPI::fromJsonValue(m_company, json[QString("company")]);
    m_company_isSet = !json[QString("company")].isNull() && m_company_isValid;

    m_email_isValid = ::OpenAPI::fromJsonValue(m_email, json[QString("email")]);
    m_email_isSet = !json[QString("email")].isNull() && m_email_isValid;

    m_individual_isValid = ::OpenAPI::fromJsonValue(m_individual, json[QString("individual")]);
    m_individual_isSet = !json[QString("individual")].isNull() && m_individual_isValid;

    m_language_isValid = ::OpenAPI::fromJsonValue(m_language, json[QString("language")]);
    m_language_isSet = !json[QString("language")].isNull() && m_language_isValid;

    m_payee_id_isValid = ::OpenAPI::fromJsonValue(m_payee_id, json[QString("payeeId")]);
    m_payee_id_isSet = !json[QString("payeeId")].isNull() && m_payee_id_isValid;

    m_payment_channel_isValid = ::OpenAPI::fromJsonValue(m_payment_channel, json[QString("paymentChannel")]);
    m_payment_channel_isSet = !json[QString("paymentChannel")].isNull() && m_payment_channel_isValid;

    m_payor_refs_isValid = ::OpenAPI::fromJsonValue(m_payor_refs, json[QString("payorRefs")]);
    m_payor_refs_isSet = !json[QString("payorRefs")].isNull() && m_payor_refs_isValid;

    m_remote_id_isValid = ::OpenAPI::fromJsonValue(m_remote_id, json[QString("remoteId")]);
    m_remote_id_isSet = !json[QString("remoteId")].isNull() && m_remote_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIFailedPayeeV4::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFailedPayeeV4::asJsonObject() const {
    QJsonObject obj;
    if (m_address.isSet()) {
        obj.insert(QString("address"), ::OpenAPI::toJsonValue(m_address));
    }
    if (m_challenge.isSet()) {
        obj.insert(QString("challenge"), ::OpenAPI::toJsonValue(m_challenge));
    }
    if (m_company.isSet()) {
        obj.insert(QString("company"), ::OpenAPI::toJsonValue(m_company));
    }
    if (m_email_isSet) {
        obj.insert(QString("email"), ::OpenAPI::toJsonValue(m_email));
    }
    if (m_individual.isSet()) {
        obj.insert(QString("individual"), ::OpenAPI::toJsonValue(m_individual));
    }
    if (m_language_isSet) {
        obj.insert(QString("language"), ::OpenAPI::toJsonValue(m_language));
    }
    if (m_payee_id_isSet) {
        obj.insert(QString("payeeId"), ::OpenAPI::toJsonValue(m_payee_id));
    }
    if (m_payment_channel.isSet()) {
        obj.insert(QString("paymentChannel"), ::OpenAPI::toJsonValue(m_payment_channel));
    }
    if (m_payor_refs.size() > 0) {
        obj.insert(QString("payorRefs"), ::OpenAPI::toJsonValue(m_payor_refs));
    }
    if (m_remote_id_isSet) {
        obj.insert(QString("remoteId"), ::OpenAPI::toJsonValue(m_remote_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAICreatePayeeAddressV4 OAIFailedPayeeV4::getAddress() const {
    return m_address;
}
void OAIFailedPayeeV4::setAddress(const OAICreatePayeeAddressV4 &address) {
    m_address = address;
    m_address_isSet = true;
}

bool OAIFailedPayeeV4::is_address_Set() const{
    return m_address_isSet;
}

bool OAIFailedPayeeV4::is_address_Valid() const{
    return m_address_isValid;
}

OAIChallengeV4 OAIFailedPayeeV4::getChallenge() const {
    return m_challenge;
}
void OAIFailedPayeeV4::setChallenge(const OAIChallengeV4 &challenge) {
    m_challenge = challenge;
    m_challenge_isSet = true;
}

bool OAIFailedPayeeV4::is_challenge_Set() const{
    return m_challenge_isSet;
}

bool OAIFailedPayeeV4::is_challenge_Valid() const{
    return m_challenge_isValid;
}

OAICompanyV4 OAIFailedPayeeV4::getCompany() const {
    return m_company;
}
void OAIFailedPayeeV4::setCompany(const OAICompanyV4 &company) {
    m_company = company;
    m_company_isSet = true;
}

bool OAIFailedPayeeV4::is_company_Set() const{
    return m_company_isSet;
}

bool OAIFailedPayeeV4::is_company_Valid() const{
    return m_company_isValid;
}

QString OAIFailedPayeeV4::getEmail() const {
    return m_email;
}
void OAIFailedPayeeV4::setEmail(const QString &email) {
    m_email = email;
    m_email_isSet = true;
}

bool OAIFailedPayeeV4::is_email_Set() const{
    return m_email_isSet;
}

bool OAIFailedPayeeV4::is_email_Valid() const{
    return m_email_isValid;
}

OAICreateIndividualV4 OAIFailedPayeeV4::getIndividual() const {
    return m_individual;
}
void OAIFailedPayeeV4::setIndividual(const OAICreateIndividualV4 &individual) {
    m_individual = individual;
    m_individual_isSet = true;
}

bool OAIFailedPayeeV4::is_individual_Set() const{
    return m_individual_isSet;
}

bool OAIFailedPayeeV4::is_individual_Valid() const{
    return m_individual_isValid;
}

QString OAIFailedPayeeV4::getLanguage() const {
    return m_language;
}
void OAIFailedPayeeV4::setLanguage(const QString &language) {
    m_language = language;
    m_language_isSet = true;
}

bool OAIFailedPayeeV4::is_language_Set() const{
    return m_language_isSet;
}

bool OAIFailedPayeeV4::is_language_Valid() const{
    return m_language_isValid;
}

QString OAIFailedPayeeV4::getPayeeId() const {
    return m_payee_id;
}
void OAIFailedPayeeV4::setPayeeId(const QString &payee_id) {
    m_payee_id = payee_id;
    m_payee_id_isSet = true;
}

bool OAIFailedPayeeV4::is_payee_id_Set() const{
    return m_payee_id_isSet;
}

bool OAIFailedPayeeV4::is_payee_id_Valid() const{
    return m_payee_id_isValid;
}

OAICreatePaymentChannelV4 OAIFailedPayeeV4::getPaymentChannel() const {
    return m_payment_channel;
}
void OAIFailedPayeeV4::setPaymentChannel(const OAICreatePaymentChannelV4 &payment_channel) {
    m_payment_channel = payment_channel;
    m_payment_channel_isSet = true;
}

bool OAIFailedPayeeV4::is_payment_channel_Set() const{
    return m_payment_channel_isSet;
}

bool OAIFailedPayeeV4::is_payment_channel_Valid() const{
    return m_payment_channel_isValid;
}

QList<OAIPayeePayorRefV4> OAIFailedPayeeV4::getPayorRefs() const {
    return m_payor_refs;
}
void OAIFailedPayeeV4::setPayorRefs(const QList<OAIPayeePayorRefV4> &payor_refs) {
    m_payor_refs = payor_refs;
    m_payor_refs_isSet = true;
}

bool OAIFailedPayeeV4::is_payor_refs_Set() const{
    return m_payor_refs_isSet;
}

bool OAIFailedPayeeV4::is_payor_refs_Valid() const{
    return m_payor_refs_isValid;
}

QString OAIFailedPayeeV4::getRemoteId() const {
    return m_remote_id;
}
void OAIFailedPayeeV4::setRemoteId(const QString &remote_id) {
    m_remote_id = remote_id;
    m_remote_id_isSet = true;
}

bool OAIFailedPayeeV4::is_remote_id_Set() const{
    return m_remote_id_isSet;
}

bool OAIFailedPayeeV4::is_remote_id_Valid() const{
    return m_remote_id_isValid;
}

QString OAIFailedPayeeV4::getType() const {
    return m_type;
}
void OAIFailedPayeeV4::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIFailedPayeeV4::is_type_Set() const{
    return m_type_isSet;
}

bool OAIFailedPayeeV4::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIFailedPayeeV4::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_address.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_challenge.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_company.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_individual.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payee_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_channel.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_payor_refs.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_remote_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFailedPayeeV4::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
