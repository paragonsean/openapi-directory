/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITestCloudFileHashDeprecated.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITestCloudFileHashDeprecated::OAITestCloudFileHashDeprecated(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITestCloudFileHashDeprecated::OAITestCloudFileHashDeprecated() {
    this->initializeModel();
}

OAITestCloudFileHashDeprecated::~OAITestCloudFileHashDeprecated() {}

void OAITestCloudFileHashDeprecated::initializeModel() {

    m_byte_range_isSet = false;
    m_byte_range_isValid = false;

    m_checksum_isSet = false;
    m_checksum_isValid = false;

    m_file_type_isSet = false;
    m_file_type_isValid = false;

    m_relative_path_isSet = false;
    m_relative_path_isValid = false;
}

void OAITestCloudFileHashDeprecated::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITestCloudFileHashDeprecated::fromJsonObject(QJsonObject json) {

    m_byte_range_isValid = ::OpenAPI::fromJsonValue(m_byte_range, json[QString("byte_range")]);
    m_byte_range_isSet = !json[QString("byte_range")].isNull() && m_byte_range_isValid;

    m_checksum_isValid = ::OpenAPI::fromJsonValue(m_checksum, json[QString("checksum")]);
    m_checksum_isSet = !json[QString("checksum")].isNull() && m_checksum_isValid;

    m_file_type_isValid = ::OpenAPI::fromJsonValue(m_file_type, json[QString("file_type")]);
    m_file_type_isSet = !json[QString("file_type")].isNull() && m_file_type_isValid;

    m_relative_path_isValid = ::OpenAPI::fromJsonValue(m_relative_path, json[QString("relative_path")]);
    m_relative_path_isSet = !json[QString("relative_path")].isNull() && m_relative_path_isValid;
}

QString OAITestCloudFileHashDeprecated::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITestCloudFileHashDeprecated::asJsonObject() const {
    QJsonObject obj;
    if (m_byte_range_isSet) {
        obj.insert(QString("byte_range"), ::OpenAPI::toJsonValue(m_byte_range));
    }
    if (m_checksum_isSet) {
        obj.insert(QString("checksum"), ::OpenAPI::toJsonValue(m_checksum));
    }
    if (m_file_type_isSet) {
        obj.insert(QString("file_type"), ::OpenAPI::toJsonValue(m_file_type));
    }
    if (m_relative_path_isSet) {
        obj.insert(QString("relative_path"), ::OpenAPI::toJsonValue(m_relative_path));
    }
    return obj;
}

QString OAITestCloudFileHashDeprecated::getByteRange() const {
    return m_byte_range;
}
void OAITestCloudFileHashDeprecated::setByteRange(const QString &byte_range) {
    m_byte_range = byte_range;
    m_byte_range_isSet = true;
}

bool OAITestCloudFileHashDeprecated::is_byte_range_Set() const{
    return m_byte_range_isSet;
}

bool OAITestCloudFileHashDeprecated::is_byte_range_Valid() const{
    return m_byte_range_isValid;
}

QString OAITestCloudFileHashDeprecated::getChecksum() const {
    return m_checksum;
}
void OAITestCloudFileHashDeprecated::setChecksum(const QString &checksum) {
    m_checksum = checksum;
    m_checksum_isSet = true;
}

bool OAITestCloudFileHashDeprecated::is_checksum_Set() const{
    return m_checksum_isSet;
}

bool OAITestCloudFileHashDeprecated::is_checksum_Valid() const{
    return m_checksum_isValid;
}

QString OAITestCloudFileHashDeprecated::getFileType() const {
    return m_file_type;
}
void OAITestCloudFileHashDeprecated::setFileType(const QString &file_type) {
    m_file_type = file_type;
    m_file_type_isSet = true;
}

bool OAITestCloudFileHashDeprecated::is_file_type_Set() const{
    return m_file_type_isSet;
}

bool OAITestCloudFileHashDeprecated::is_file_type_Valid() const{
    return m_file_type_isValid;
}

QString OAITestCloudFileHashDeprecated::getRelativePath() const {
    return m_relative_path;
}
void OAITestCloudFileHashDeprecated::setRelativePath(const QString &relative_path) {
    m_relative_path = relative_path;
    m_relative_path_isSet = true;
}

bool OAITestCloudFileHashDeprecated::is_relative_path_Set() const{
    return m_relative_path_isSet;
}

bool OAITestCloudFileHashDeprecated::is_relative_path_Valid() const{
    return m_relative_path_isValid;
}

bool OAITestCloudFileHashDeprecated::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_byte_range_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_checksum_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_relative_path_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITestCloudFileHashDeprecated::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_checksum_isValid && m_file_type_isValid && m_relative_path_isValid && true;
}

} // namespace OpenAPI
