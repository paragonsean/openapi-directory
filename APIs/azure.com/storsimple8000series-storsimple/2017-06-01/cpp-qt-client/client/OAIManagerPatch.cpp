/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIManagerPatch.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIManagerPatch::OAIManagerPatch(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIManagerPatch::OAIManagerPatch() {
    this->initializeModel();
}

OAIManagerPatch::~OAIManagerPatch() {}

void OAIManagerPatch::initializeModel() {

    m_tags_isSet = false;
    m_tags_isValid = false;
}

void OAIManagerPatch::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIManagerPatch::fromJsonObject(QJsonObject json) {

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;
}

QString OAIManagerPatch::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIManagerPatch::asJsonObject() const {
    QJsonObject obj;
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    return obj;
}

QMap<QString, QString> OAIManagerPatch::getTags() const {
    return m_tags;
}
void OAIManagerPatch::setTags(const QMap<QString, QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIManagerPatch::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIManagerPatch::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAIManagerPatch::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIManagerPatch::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
