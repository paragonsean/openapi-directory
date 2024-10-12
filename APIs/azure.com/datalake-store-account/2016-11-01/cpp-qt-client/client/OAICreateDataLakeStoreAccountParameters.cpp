/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2016-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICreateDataLakeStoreAccountParameters.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICreateDataLakeStoreAccountParameters::OAICreateDataLakeStoreAccountParameters(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICreateDataLakeStoreAccountParameters::OAICreateDataLakeStoreAccountParameters() {
    this->initializeModel();
}

OAICreateDataLakeStoreAccountParameters::~OAICreateDataLakeStoreAccountParameters() {}

void OAICreateDataLakeStoreAccountParameters::initializeModel() {

    m_identity_isSet = false;
    m_identity_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;
}

void OAICreateDataLakeStoreAccountParameters::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICreateDataLakeStoreAccountParameters::fromJsonObject(QJsonObject json) {

    m_identity_isValid = ::OpenAPI::fromJsonValue(m_identity, json[QString("identity")]);
    m_identity_isSet = !json[QString("identity")].isNull() && m_identity_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;
}

QString OAICreateDataLakeStoreAccountParameters::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICreateDataLakeStoreAccountParameters::asJsonObject() const {
    QJsonObject obj;
    if (m_identity.isSet()) {
        obj.insert(QString("identity"), ::OpenAPI::toJsonValue(m_identity));
    }
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    return obj;
}

OAIEncryptionIdentity OAICreateDataLakeStoreAccountParameters::getIdentity() const {
    return m_identity;
}
void OAICreateDataLakeStoreAccountParameters::setIdentity(const OAIEncryptionIdentity &identity) {
    m_identity = identity;
    m_identity_isSet = true;
}

bool OAICreateDataLakeStoreAccountParameters::is_identity_Set() const{
    return m_identity_isSet;
}

bool OAICreateDataLakeStoreAccountParameters::is_identity_Valid() const{
    return m_identity_isValid;
}

QString OAICreateDataLakeStoreAccountParameters::getLocation() const {
    return m_location;
}
void OAICreateDataLakeStoreAccountParameters::setLocation(const QString &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAICreateDataLakeStoreAccountParameters::is_location_Set() const{
    return m_location_isSet;
}

bool OAICreateDataLakeStoreAccountParameters::is_location_Valid() const{
    return m_location_isValid;
}

OAICreateDataLakeStoreAccountProperties OAICreateDataLakeStoreAccountParameters::getProperties() const {
    return m_properties;
}
void OAICreateDataLakeStoreAccountParameters::setProperties(const OAICreateDataLakeStoreAccountProperties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAICreateDataLakeStoreAccountParameters::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAICreateDataLakeStoreAccountParameters::is_properties_Valid() const{
    return m_properties_isValid;
}

QMap<QString, QString> OAICreateDataLakeStoreAccountParameters::getTags() const {
    return m_tags;
}
void OAICreateDataLakeStoreAccountParameters::setTags(const QMap<QString, QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAICreateDataLakeStoreAccountParameters::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAICreateDataLakeStoreAccountParameters::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAICreateDataLakeStoreAccountParameters::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_identity.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICreateDataLakeStoreAccountParameters::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_location_isValid && true;
}

} // namespace OpenAPI
