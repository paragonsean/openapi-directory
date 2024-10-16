/**
 * TinyUID.com
 * Paste a Long URL link to shorten it
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: contact@tinyuid.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI_v1_shorten_post_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_v1_shorten_post_200_response::OAI_v1_shorten_post_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_v1_shorten_post_200_response::OAI_v1_shorten_post_200_response() {
    this->initializeModel();
}

OAI_v1_shorten_post_200_response::~OAI_v1_shorten_post_200_response() {}

void OAI_v1_shorten_post_200_response::initializeModel() {

    m_result_url_isSet = false;
    m_result_url_isValid = false;
}

void OAI_v1_shorten_post_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_v1_shorten_post_200_response::fromJsonObject(QJsonObject json) {

    m_result_url_isValid = ::OpenAPI::fromJsonValue(m_result_url, json[QString("result_url")]);
    m_result_url_isSet = !json[QString("result_url")].isNull() && m_result_url_isValid;
}

QString OAI_v1_shorten_post_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_v1_shorten_post_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_result_url_isSet) {
        obj.insert(QString("result_url"), ::OpenAPI::toJsonValue(m_result_url));
    }
    return obj;
}

QString OAI_v1_shorten_post_200_response::getResultUrl() const {
    return m_result_url;
}
void OAI_v1_shorten_post_200_response::setResultUrl(const QString &result_url) {
    m_result_url = result_url;
    m_result_url_isSet = true;
}

bool OAI_v1_shorten_post_200_response::is_result_url_Set() const{
    return m_result_url_isSet;
}

bool OAI_v1_shorten_post_200_response::is_result_url_Valid() const{
    return m_result_url_isValid;
}

bool OAI_v1_shorten_post_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_result_url_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_v1_shorten_post_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_result_url_isValid && true;
}

} // namespace OpenAPI
