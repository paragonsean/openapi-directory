/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWatchedDirectory.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWatchedDirectory::OAIWatchedDirectory(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWatchedDirectory::OAIWatchedDirectory() {
    this->initializeModel();
}

OAIWatchedDirectory::~OAIWatchedDirectory() {}

void OAIWatchedDirectory::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_path_isSet = false;
    m_path_isValid = false;
}

void OAIWatchedDirectory::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWatchedDirectory::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_path_isValid = ::OpenAPI::fromJsonValue(m_path, json[QString("path")]);
    m_path_isSet = !json[QString("path")].isNull() && m_path_isValid;
}

QString OAIWatchedDirectory::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWatchedDirectory::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_path_isSet) {
        obj.insert(QString("path"), ::OpenAPI::toJsonValue(m_path));
    }
    return obj;
}

qint64 OAIWatchedDirectory::getId() const {
    return m_id;
}
void OAIWatchedDirectory::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIWatchedDirectory::is_id_Set() const{
    return m_id_isSet;
}

bool OAIWatchedDirectory::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIWatchedDirectory::getPath() const {
    return m_path;
}
void OAIWatchedDirectory::setPath(const QString &path) {
    m_path = path;
    m_path_isSet = true;
}

bool OAIWatchedDirectory::is_path_Set() const{
    return m_path_isSet;
}

bool OAIWatchedDirectory::is_path_Valid() const{
    return m_path_isValid;
}

bool OAIWatchedDirectory::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWatchedDirectory::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
