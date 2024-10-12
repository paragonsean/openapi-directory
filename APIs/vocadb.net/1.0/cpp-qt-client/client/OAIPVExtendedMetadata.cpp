/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPVExtendedMetadata.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPVExtendedMetadata::OAIPVExtendedMetadata(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPVExtendedMetadata::OAIPVExtendedMetadata() {
    this->initializeModel();
}

OAIPVExtendedMetadata::~OAIPVExtendedMetadata() {}

void OAIPVExtendedMetadata::initializeModel() {

    m_json_isSet = false;
    m_json_isValid = false;
}

void OAIPVExtendedMetadata::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPVExtendedMetadata::fromJsonObject(QJsonObject json) {

    m_json_isValid = ::OpenAPI::fromJsonValue(m_json, json[QString("json")]);
    m_json_isSet = !json[QString("json")].isNull() && m_json_isValid;
}

QString OAIPVExtendedMetadata::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPVExtendedMetadata::asJsonObject() const {
    QJsonObject obj;
    if (m_json_isSet) {
        obj.insert(QString("json"), ::OpenAPI::toJsonValue(m_json));
    }
    return obj;
}

QString OAIPVExtendedMetadata::getJson() const {
    return m_json;
}
void OAIPVExtendedMetadata::setJson(const QString &json) {
    m_json = json;
    m_json_isSet = true;
}

bool OAIPVExtendedMetadata::is_json_Set() const{
    return m_json_isSet;
}

bool OAIPVExtendedMetadata::is_json_Valid() const{
    return m_json_isValid;
}

bool OAIPVExtendedMetadata::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_json_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPVExtendedMetadata::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
