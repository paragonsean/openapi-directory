/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITraveler.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITraveler::OAITraveler(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITraveler::OAITraveler() {
    this->initializeModel();
}

OAITraveler::~OAITraveler() {}

void OAITraveler::initializeModel() {

    m_associated_adult_id_isSet = false;
    m_associated_adult_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_traveler_type_isSet = false;
    m_traveler_type_isValid = false;
}

void OAITraveler::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITraveler::fromJsonObject(QJsonObject json) {

    m_associated_adult_id_isValid = ::OpenAPI::fromJsonValue(m_associated_adult_id, json[QString("associatedAdultId")]);
    m_associated_adult_id_isSet = !json[QString("associatedAdultId")].isNull() && m_associated_adult_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_traveler_type_isValid = ::OpenAPI::fromJsonValue(m_traveler_type, json[QString("travelerType")]);
    m_traveler_type_isSet = !json[QString("travelerType")].isNull() && m_traveler_type_isValid;
}

QString OAITraveler::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITraveler::asJsonObject() const {
    QJsonObject obj;
    if (m_associated_adult_id_isSet) {
        obj.insert(QString("associatedAdultId"), ::OpenAPI::toJsonValue(m_associated_adult_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_traveler_type.isSet()) {
        obj.insert(QString("travelerType"), ::OpenAPI::toJsonValue(m_traveler_type));
    }
    return obj;
}

QString OAITraveler::getAssociatedAdultId() const {
    return m_associated_adult_id;
}
void OAITraveler::setAssociatedAdultId(const QString &associated_adult_id) {
    m_associated_adult_id = associated_adult_id;
    m_associated_adult_id_isSet = true;
}

bool OAITraveler::is_associated_adult_id_Set() const{
    return m_associated_adult_id_isSet;
}

bool OAITraveler::is_associated_adult_id_Valid() const{
    return m_associated_adult_id_isValid;
}

QString OAITraveler::getId() const {
    return m_id;
}
void OAITraveler::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITraveler::is_id_Set() const{
    return m_id_isSet;
}

bool OAITraveler::is_id_Valid() const{
    return m_id_isValid;
}

OAITravelerType OAITraveler::getTravelerType() const {
    return m_traveler_type;
}
void OAITraveler::setTravelerType(const OAITravelerType &traveler_type) {
    m_traveler_type = traveler_type;
    m_traveler_type_isSet = true;
}

bool OAITraveler::is_traveler_type_Set() const{
    return m_traveler_type_isSet;
}

bool OAITraveler::is_traveler_type_Valid() const{
    return m_traveler_type_isValid;
}

bool OAITraveler::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_associated_adult_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_traveler_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITraveler::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_traveler_type_isValid && true;
}

} // namespace OpenAPI
