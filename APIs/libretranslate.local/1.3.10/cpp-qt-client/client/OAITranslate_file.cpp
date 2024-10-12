/**
 * LibreTranslate
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.3.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITranslate_file.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITranslate_file::OAITranslate_file(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITranslate_file::OAITranslate_file() {
    this->initializeModel();
}

OAITranslate_file::~OAITranslate_file() {}

void OAITranslate_file::initializeModel() {

    m_translated_file_url_isSet = false;
    m_translated_file_url_isValid = false;
}

void OAITranslate_file::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITranslate_file::fromJsonObject(QJsonObject json) {

    m_translated_file_url_isValid = ::OpenAPI::fromJsonValue(m_translated_file_url, json[QString("translatedFileUrl")]);
    m_translated_file_url_isSet = !json[QString("translatedFileUrl")].isNull() && m_translated_file_url_isValid;
}

QString OAITranslate_file::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITranslate_file::asJsonObject() const {
    QJsonObject obj;
    if (m_translated_file_url_isSet) {
        obj.insert(QString("translatedFileUrl"), ::OpenAPI::toJsonValue(m_translated_file_url));
    }
    return obj;
}

QString OAITranslate_file::getTranslatedFileUrl() const {
    return m_translated_file_url;
}
void OAITranslate_file::setTranslatedFileUrl(const QString &translated_file_url) {
    m_translated_file_url = translated_file_url;
    m_translated_file_url_isSet = true;
}

bool OAITranslate_file::is_translated_file_url_Set() const{
    return m_translated_file_url_isSet;
}

bool OAITranslate_file::is_translated_file_url_Valid() const{
    return m_translated_file_url_isValid;
}

bool OAITranslate_file::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_translated_file_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITranslate_file::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
