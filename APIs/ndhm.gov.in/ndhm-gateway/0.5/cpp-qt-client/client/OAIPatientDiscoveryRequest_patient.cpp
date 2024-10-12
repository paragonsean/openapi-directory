/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPatientDiscoveryRequest_patient.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientDiscoveryRequest_patient::OAIPatientDiscoveryRequest_patient(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientDiscoveryRequest_patient::OAIPatientDiscoveryRequest_patient() {
    this->initializeModel();
}

OAIPatientDiscoveryRequest_patient::~OAIPatientDiscoveryRequest_patient() {}

void OAIPatientDiscoveryRequest_patient::initializeModel() {

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_unverified_identifiers_isSet = false;
    m_unverified_identifiers_isValid = false;

    m_verified_identifiers_isSet = false;
    m_verified_identifiers_isValid = false;

    m_year_of_birth_isSet = false;
    m_year_of_birth_isValid = false;
}

void OAIPatientDiscoveryRequest_patient::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientDiscoveryRequest_patient::fromJsonObject(QJsonObject json) {

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_unverified_identifiers_isValid = ::OpenAPI::fromJsonValue(m_unverified_identifiers, json[QString("unverifiedIdentifiers")]);
    m_unverified_identifiers_isSet = !json[QString("unverifiedIdentifiers")].isNull() && m_unverified_identifiers_isValid;

    m_verified_identifiers_isValid = ::OpenAPI::fromJsonValue(m_verified_identifiers, json[QString("verifiedIdentifiers")]);
    m_verified_identifiers_isSet = !json[QString("verifiedIdentifiers")].isNull() && m_verified_identifiers_isValid;

    m_year_of_birth_isValid = ::OpenAPI::fromJsonValue(m_year_of_birth, json[QString("yearOfBirth")]);
    m_year_of_birth_isSet = !json[QString("yearOfBirth")].isNull() && m_year_of_birth_isValid;
}

QString OAIPatientDiscoveryRequest_patient::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientDiscoveryRequest_patient::asJsonObject() const {
    QJsonObject obj;
    if (m_gender.isSet()) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_unverified_identifiers.size() > 0) {
        obj.insert(QString("unverifiedIdentifiers"), ::OpenAPI::toJsonValue(m_unverified_identifiers));
    }
    if (m_verified_identifiers.size() > 0) {
        obj.insert(QString("verifiedIdentifiers"), ::OpenAPI::toJsonValue(m_verified_identifiers));
    }
    if (m_year_of_birth_isSet) {
        obj.insert(QString("yearOfBirth"), ::OpenAPI::toJsonValue(m_year_of_birth));
    }
    return obj;
}

OAIPatientGender OAIPatientDiscoveryRequest_patient::getGender() const {
    return m_gender;
}
void OAIPatientDiscoveryRequest_patient::setGender(const OAIPatientGender &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIPatientDiscoveryRequest_patient::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIPatientDiscoveryRequest_patient::is_gender_Valid() const{
    return m_gender_isValid;
}

QString OAIPatientDiscoveryRequest_patient::getId() const {
    return m_id;
}
void OAIPatientDiscoveryRequest_patient::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPatientDiscoveryRequest_patient::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPatientDiscoveryRequest_patient::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIPatientDiscoveryRequest_patient::getName() const {
    return m_name;
}
void OAIPatientDiscoveryRequest_patient::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIPatientDiscoveryRequest_patient::is_name_Set() const{
    return m_name_isSet;
}

bool OAIPatientDiscoveryRequest_patient::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIIdentifier> OAIPatientDiscoveryRequest_patient::getUnverifiedIdentifiers() const {
    return m_unverified_identifiers;
}
void OAIPatientDiscoveryRequest_patient::setUnverifiedIdentifiers(const QList<OAIIdentifier> &unverified_identifiers) {
    m_unverified_identifiers = unverified_identifiers;
    m_unverified_identifiers_isSet = true;
}

bool OAIPatientDiscoveryRequest_patient::is_unverified_identifiers_Set() const{
    return m_unverified_identifiers_isSet;
}

bool OAIPatientDiscoveryRequest_patient::is_unverified_identifiers_Valid() const{
    return m_unverified_identifiers_isValid;
}

QList<OAIIdentifier> OAIPatientDiscoveryRequest_patient::getVerifiedIdentifiers() const {
    return m_verified_identifiers;
}
void OAIPatientDiscoveryRequest_patient::setVerifiedIdentifiers(const QList<OAIIdentifier> &verified_identifiers) {
    m_verified_identifiers = verified_identifiers;
    m_verified_identifiers_isSet = true;
}

bool OAIPatientDiscoveryRequest_patient::is_verified_identifiers_Set() const{
    return m_verified_identifiers_isSet;
}

bool OAIPatientDiscoveryRequest_patient::is_verified_identifiers_Valid() const{
    return m_verified_identifiers_isValid;
}

qint32 OAIPatientDiscoveryRequest_patient::getYearOfBirth() const {
    return m_year_of_birth;
}
void OAIPatientDiscoveryRequest_patient::setYearOfBirth(const qint32 &year_of_birth) {
    m_year_of_birth = year_of_birth;
    m_year_of_birth_isSet = true;
}

bool OAIPatientDiscoveryRequest_patient::is_year_of_birth_Set() const{
    return m_year_of_birth_isSet;
}

bool OAIPatientDiscoveryRequest_patient::is_year_of_birth_Valid() const{
    return m_year_of_birth_isValid;
}

bool OAIPatientDiscoveryRequest_patient::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_gender.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unverified_identifiers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_verified_identifiers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_year_of_birth_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientDiscoveryRequest_patient::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_gender_isValid && m_id_isValid && m_name_isValid && m_verified_identifiers_isValid && m_year_of_birth_isValid && true;
}

} // namespace OpenAPI
