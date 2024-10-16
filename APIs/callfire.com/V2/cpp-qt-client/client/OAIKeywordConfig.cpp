/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIKeywordConfig.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIKeywordConfig::OAIKeywordConfig(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIKeywordConfig::OAIKeywordConfig() {
    this->initializeModel();
}

OAIKeywordConfig::~OAIKeywordConfig() {}

void OAIKeywordConfig::initializeModel() {

    m_keyword_isSet = false;
    m_keyword_isValid = false;

    m_text_inbound_config_isSet = false;
    m_text_inbound_config_isValid = false;
}

void OAIKeywordConfig::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIKeywordConfig::fromJsonObject(QJsonObject json) {

    m_keyword_isValid = ::OpenAPI::fromJsonValue(m_keyword, json[QString("keyword")]);
    m_keyword_isSet = !json[QString("keyword")].isNull() && m_keyword_isValid;

    m_text_inbound_config_isValid = ::OpenAPI::fromJsonValue(m_text_inbound_config, json[QString("textInboundConfig")]);
    m_text_inbound_config_isSet = !json[QString("textInboundConfig")].isNull() && m_text_inbound_config_isValid;
}

QString OAIKeywordConfig::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIKeywordConfig::asJsonObject() const {
    QJsonObject obj;
    if (m_keyword_isSet) {
        obj.insert(QString("keyword"), ::OpenAPI::toJsonValue(m_keyword));
    }
    if (m_text_inbound_config.isSet()) {
        obj.insert(QString("textInboundConfig"), ::OpenAPI::toJsonValue(m_text_inbound_config));
    }
    return obj;
}

QString OAIKeywordConfig::getKeyword() const {
    return m_keyword;
}
void OAIKeywordConfig::setKeyword(const QString &keyword) {
    m_keyword = keyword;
    m_keyword_isSet = true;
}

bool OAIKeywordConfig::is_keyword_Set() const{
    return m_keyword_isSet;
}

bool OAIKeywordConfig::is_keyword_Valid() const{
    return m_keyword_isValid;
}

OAITextInboundConfig OAIKeywordConfig::getTextInboundConfig() const {
    return m_text_inbound_config;
}
void OAIKeywordConfig::setTextInboundConfig(const OAITextInboundConfig &text_inbound_config) {
    m_text_inbound_config = text_inbound_config;
    m_text_inbound_config_isSet = true;
}

bool OAIKeywordConfig::is_text_inbound_config_Set() const{
    return m_text_inbound_config_isSet;
}

bool OAIKeywordConfig::is_text_inbound_config_Valid() const{
    return m_text_inbound_config_isValid;
}

bool OAIKeywordConfig::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_keyword_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_inbound_config.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIKeywordConfig::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
