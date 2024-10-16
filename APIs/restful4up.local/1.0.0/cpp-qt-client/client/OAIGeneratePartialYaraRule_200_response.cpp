/**
 * RESTful4Up
 * RESTful API 4 Unipacker
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGeneratePartialYaraRule_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGeneratePartialYaraRule_200_response::OAIGeneratePartialYaraRule_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGeneratePartialYaraRule_200_response::OAIGeneratePartialYaraRule_200_response() {
    this->initializeModel();
}

OAIGeneratePartialYaraRule_200_response::~OAIGeneratePartialYaraRule_200_response() {}

void OAIGeneratePartialYaraRule_200_response::initializeModel() {

    m_rule_isSet = false;
    m_rule_isValid = false;
}

void OAIGeneratePartialYaraRule_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGeneratePartialYaraRule_200_response::fromJsonObject(QJsonObject json) {

    m_rule_isValid = ::OpenAPI::fromJsonValue(m_rule, json[QString("rule")]);
    m_rule_isSet = !json[QString("rule")].isNull() && m_rule_isValid;
}

QString OAIGeneratePartialYaraRule_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGeneratePartialYaraRule_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_rule.isSet()) {
        obj.insert(QString("rule"), ::OpenAPI::toJsonValue(m_rule));
    }
    return obj;
}

OAIYara OAIGeneratePartialYaraRule_200_response::getRule() const {
    return m_rule;
}
void OAIGeneratePartialYaraRule_200_response::setRule(const OAIYara &rule) {
    m_rule = rule;
    m_rule_isSet = true;
}

bool OAIGeneratePartialYaraRule_200_response::is_rule_Set() const{
    return m_rule_isSet;
}

bool OAIGeneratePartialYaraRule_200_response::is_rule_Valid() const{
    return m_rule_isValid;
}

bool OAIGeneratePartialYaraRule_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_rule.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGeneratePartialYaraRule_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
