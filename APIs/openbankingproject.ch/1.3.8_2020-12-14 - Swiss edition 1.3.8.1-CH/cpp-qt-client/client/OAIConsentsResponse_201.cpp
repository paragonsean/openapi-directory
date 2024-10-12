/**
 * Swiss NextGen Banking API-Framework
 * # Summary The **Swiss NextGen API** is based on the NextGenPSD2 *Framework Version 1.3.4* of the Berlin Group which offers a modern, open, harmonised and interoperable set of Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely. The NextGen Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.  The Swiss edtion refines the message formats specific to Switzerland and defines some matching examples.  The possible Approaches are:   * Redirect SCA Approach   * *(Not recommended by obp.ch community) OAuth SCA Approach*   * *(Not recommended by obp.ch community) Decoupled SCA Approach*   * *(Not recommended by obp.ch community) Embedded SCA Approach without SCA method*   * *(Not recommended by obp.ch community) Embedded SCA Approach with only one SCA method available*   * *(Not recommended by obp.ch community) Embedded SCA Approach with Selection of a SCA method*    Not every message defined in this API definition is necessary for all approaches.   Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional   Therefore for a particular implementation of a compliant API it is only necessary to support   a certain subset of the methods defined in this API definition.    **Please have a look at the implementation guidelines if you are not sure   which message has to be used for the approach you are going to use.**  ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the [Berlin Group API](https://www.berlin-group.org/nextgenpsd2-downloads).**   It is not a replacement in any sense.   The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group API. * **This API definition contains the REST-API for requests from the PISP to the ASPSP.** * **This API definition contains the messages for all different approaches defined in the Implementation Guidelines.** * According to the OpenAPI-Specification [https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md]      \"If in is \"header\" and the name field is \"Accept\", \"Content-Type\" or \"Authorization\", the parameter definition SHALL be ignored.\"    The element \"Accept\" will not be defined in this file at any place.    The elements \"Content-Type\" and \"Authorization\" are implicitly defined by the OpenApi tags \"content\" and \"security\".  * There are several predefined types which might occur in payment initiation messages,   but are not used in the standard JSON messages in the Implementation Guidelines.   Therefore they are not used in the corresponding messages in this file either.   We added them for the convenience of the user.   If there is a payment product, which needs these fields, one can easily use the predefined types.   But the ASPSP need not to accept them in general.  * **We omit the definition of all standard HTTP header elements (mandatory/optional/conditional)   except they are mentioned in the Implementation Guidelines.**   Therefore the implementer might add these in his own realisation of a comlient API in addition to the elements defined in this file.  ## General Remarks on Data Types  The Berlin Group definition of UTF-8 strings in context of the API have to support at least the following characters  a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  0 1 2 3 4 5 6 7 8 9  / - ? : ( ) . , ' +  Space 
 *
 * The version of the OpenAPI document: 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 * Contact: info@obp.ch
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIConsentsResponse_201.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConsentsResponse_201::OAIConsentsResponse_201(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConsentsResponse_201::OAIConsentsResponse_201() {
    this->initializeModel();
}

OAIConsentsResponse_201::~OAIConsentsResponse_201() {}

void OAIConsentsResponse_201::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_challenge_data_isSet = false;
    m_challenge_data_isValid = false;

    m_chosen_sca_method_isSet = false;
    m_chosen_sca_method_isValid = false;

    m_consent_id_isSet = false;
    m_consent_id_isValid = false;

    m_consent_status_isSet = false;
    m_consent_status_isValid = false;

    m_psu_message_isSet = false;
    m_psu_message_isValid = false;

    m_sca_methods_isSet = false;
    m_sca_methods_isValid = false;
}

void OAIConsentsResponse_201::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConsentsResponse_201::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_challenge_data_isValid = ::OpenAPI::fromJsonValue(m_challenge_data, json[QString("challengeData")]);
    m_challenge_data_isSet = !json[QString("challengeData")].isNull() && m_challenge_data_isValid;

    m_chosen_sca_method_isValid = ::OpenAPI::fromJsonValue(m_chosen_sca_method, json[QString("chosenScaMethod")]);
    m_chosen_sca_method_isSet = !json[QString("chosenScaMethod")].isNull() && m_chosen_sca_method_isValid;

    m_consent_id_isValid = ::OpenAPI::fromJsonValue(m_consent_id, json[QString("consentId")]);
    m_consent_id_isSet = !json[QString("consentId")].isNull() && m_consent_id_isValid;

    m_consent_status_isValid = ::OpenAPI::fromJsonValue(m_consent_status, json[QString("consentStatus")]);
    m_consent_status_isSet = !json[QString("consentStatus")].isNull() && m_consent_status_isValid;

    m_psu_message_isValid = ::OpenAPI::fromJsonValue(m_psu_message, json[QString("psuMessage")]);
    m_psu_message_isSet = !json[QString("psuMessage")].isNull() && m_psu_message_isValid;

    m_sca_methods_isValid = ::OpenAPI::fromJsonValue(m_sca_methods, json[QString("scaMethods")]);
    m_sca_methods_isSet = !json[QString("scaMethods")].isNull() && m_sca_methods_isValid;
}

QString OAIConsentsResponse_201::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConsentsResponse_201::asJsonObject() const {
    QJsonObject obj;
    if (m__links.isSet()) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_challenge_data.isSet()) {
        obj.insert(QString("challengeData"), ::OpenAPI::toJsonValue(m_challenge_data));
    }
    if (m_chosen_sca_method.isSet()) {
        obj.insert(QString("chosenScaMethod"), ::OpenAPI::toJsonValue(m_chosen_sca_method));
    }
    if (m_consent_id_isSet) {
        obj.insert(QString("consentId"), ::OpenAPI::toJsonValue(m_consent_id));
    }
    if (m_consent_status.isSet()) {
        obj.insert(QString("consentStatus"), ::OpenAPI::toJsonValue(m_consent_status));
    }
    if (m_psu_message_isSet) {
        obj.insert(QString("psuMessage"), ::OpenAPI::toJsonValue(m_psu_message));
    }
    if (m_sca_methods.size() > 0) {
        obj.insert(QString("scaMethods"), ::OpenAPI::toJsonValue(m_sca_methods));
    }
    return obj;
}

OAI_linksConsents OAIConsentsResponse_201::getLinks() const {
    return m__links;
}
void OAIConsentsResponse_201::setLinks(const OAI_linksConsents &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIConsentsResponse_201::is__links_Set() const{
    return m__links_isSet;
}

bool OAIConsentsResponse_201::is__links_Valid() const{
    return m__links_isValid;
}

OAIChallengeData OAIConsentsResponse_201::getChallengeData() const {
    return m_challenge_data;
}
void OAIConsentsResponse_201::setChallengeData(const OAIChallengeData &challenge_data) {
    m_challenge_data = challenge_data;
    m_challenge_data_isSet = true;
}

bool OAIConsentsResponse_201::is_challenge_data_Set() const{
    return m_challenge_data_isSet;
}

bool OAIConsentsResponse_201::is_challenge_data_Valid() const{
    return m_challenge_data_isValid;
}

OAIAuthenticationObject OAIConsentsResponse_201::getChosenScaMethod() const {
    return m_chosen_sca_method;
}
void OAIConsentsResponse_201::setChosenScaMethod(const OAIAuthenticationObject &chosen_sca_method) {
    m_chosen_sca_method = chosen_sca_method;
    m_chosen_sca_method_isSet = true;
}

bool OAIConsentsResponse_201::is_chosen_sca_method_Set() const{
    return m_chosen_sca_method_isSet;
}

bool OAIConsentsResponse_201::is_chosen_sca_method_Valid() const{
    return m_chosen_sca_method_isValid;
}

QString OAIConsentsResponse_201::getConsentId() const {
    return m_consent_id;
}
void OAIConsentsResponse_201::setConsentId(const QString &consent_id) {
    m_consent_id = consent_id;
    m_consent_id_isSet = true;
}

bool OAIConsentsResponse_201::is_consent_id_Set() const{
    return m_consent_id_isSet;
}

bool OAIConsentsResponse_201::is_consent_id_Valid() const{
    return m_consent_id_isValid;
}

OAIConsentStatus OAIConsentsResponse_201::getConsentStatus() const {
    return m_consent_status;
}
void OAIConsentsResponse_201::setConsentStatus(const OAIConsentStatus &consent_status) {
    m_consent_status = consent_status;
    m_consent_status_isSet = true;
}

bool OAIConsentsResponse_201::is_consent_status_Set() const{
    return m_consent_status_isSet;
}

bool OAIConsentsResponse_201::is_consent_status_Valid() const{
    return m_consent_status_isValid;
}

QString OAIConsentsResponse_201::getPsuMessage() const {
    return m_psu_message;
}
void OAIConsentsResponse_201::setPsuMessage(const QString &psu_message) {
    m_psu_message = psu_message;
    m_psu_message_isSet = true;
}

bool OAIConsentsResponse_201::is_psu_message_Set() const{
    return m_psu_message_isSet;
}

bool OAIConsentsResponse_201::is_psu_message_Valid() const{
    return m_psu_message_isValid;
}

QList<OAIAuthenticationObject> OAIConsentsResponse_201::getScaMethods() const {
    return m_sca_methods;
}
void OAIConsentsResponse_201::setScaMethods(const QList<OAIAuthenticationObject> &sca_methods) {
    m_sca_methods = sca_methods;
    m_sca_methods_isSet = true;
}

bool OAIConsentsResponse_201::is_sca_methods_Set() const{
    return m_sca_methods_isSet;
}

bool OAIConsentsResponse_201::is_sca_methods_Valid() const{
    return m_sca_methods_isValid;
}

bool OAIConsentsResponse_201::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_challenge_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_chosen_sca_method.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_consent_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_consent_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_psu_message_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sca_methods.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConsentsResponse_201::isValid() const {
    // only required properties are required for the object to be considered valid
    return m__links_isValid && m_consent_id_isValid && m_consent_status_isValid && true;
}

} // namespace OpenAPI
