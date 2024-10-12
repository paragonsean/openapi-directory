/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFileId.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFileId::OAIFileId(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFileId::OAIFileId() {
    this->initializeModel();
}

OAIFileId::~OAIFileId() {}

void OAIFileId::initializeModel() {

    m_file_id_isSet = false;
    m_file_id_isValid = false;
}

void OAIFileId::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFileId::fromJsonObject(QJsonObject json) {

    m_file_id_isValid = ::OpenAPI::fromJsonValue(m_file_id, json[QString("file_id")]);
    m_file_id_isSet = !json[QString("file_id")].isNull() && m_file_id_isValid;
}

QString OAIFileId::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFileId::asJsonObject() const {
    QJsonObject obj;
    if (m_file_id_isSet) {
        obj.insert(QString("file_id"), ::OpenAPI::toJsonValue(m_file_id));
    }
    return obj;
}

qint64 OAIFileId::getFileId() const {
    return m_file_id;
}
void OAIFileId::setFileId(const qint64 &file_id) {
    m_file_id = file_id;
    m_file_id_isSet = true;
}

bool OAIFileId::is_file_id_Set() const{
    return m_file_id_isSet;
}

bool OAIFileId::is_file_id_Valid() const{
    return m_file_id_isValid;
}

bool OAIFileId::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_file_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFileId::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
