/**
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPatientDemographic.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientDemographic::OAIPatientDemographic(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientDemographic::OAIPatientDemographic() {
    this->initializeModel();
}

OAIPatientDemographic::~OAIPatientDemographic() {}

void OAIPatientDemographic::initializeModel() {

    m_date_of_birth_isSet = false;
    m_date_of_birth_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_identifier_isSet = false;
    m_identifier_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIPatientDemographic::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientDemographic::fromJsonObject(QJsonObject json) {

    m_date_of_birth_isValid = ::OpenAPI::fromJsonValue(m_date_of_birth, json[QString("dateOfBirth")]);
    m_date_of_birth_isSet = !json[QString("dateOfBirth")].isNull() && m_date_of_birth_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_identifier_isValid = ::OpenAPI::fromJsonValue(m_identifier, json[QString("identifier")]);
    m_identifier_isSet = !json[QString("identifier")].isNull() && m_identifier_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIPatientDemographic::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientDemographic::asJsonObject() const {
    QJsonObject obj;
    if (m_date_of_birth_isSet) {
        obj.insert(QString("dateOfBirth"), ::OpenAPI::toJsonValue(m_date_of_birth));
    }
    if (m_gender.isSet()) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_identifier.isSet()) {
        obj.insert(QString("identifier"), ::OpenAPI::toJsonValue(m_identifier));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIPatientDemographic::getDateOfBirth() const {
    return m_date_of_birth;
}
void OAIPatientDemographic::setDateOfBirth(const QString &date_of_birth) {
    m_date_of_birth = date_of_birth;
    m_date_of_birth_isSet = true;
}

bool OAIPatientDemographic::is_date_of_birth_Set() const{
    return m_date_of_birth_isSet;
}

bool OAIPatientDemographic::is_date_of_birth_Valid() const{
    return m_date_of_birth_isValid;
}

OAIPatientGender OAIPatientDemographic::getGender() const {
    return m_gender;
}
void OAIPatientDemographic::setGender(const OAIPatientGender &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIPatientDemographic::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIPatientDemographic::is_gender_Valid() const{
    return m_gender_isValid;
}

OAIAuthConfirmIdentifier OAIPatientDemographic::getIdentifier() const {
    return m_identifier;
}
void OAIPatientDemographic::setIdentifier(const OAIAuthConfirmIdentifier &identifier) {
    m_identifier = identifier;
    m_identifier_isSet = true;
}

bool OAIPatientDemographic::is_identifier_Set() const{
    return m_identifier_isSet;
}

bool OAIPatientDemographic::is_identifier_Valid() const{
    return m_identifier_isValid;
}

QString OAIPatientDemographic::getName() const {
    return m_name;
}
void OAIPatientDemographic::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPatientDemographic::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPatientDemographic::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIPatientDemographic::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_date_of_birth_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_identifier.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientDemographic::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_date_of_birth_isValid && m_gender_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
