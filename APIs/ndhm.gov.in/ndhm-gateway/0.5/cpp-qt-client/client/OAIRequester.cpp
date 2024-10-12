/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRequester.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRequester::OAIRequester(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRequester::OAIRequester() {
    this->initializeModel();
}

OAIRequester::~OAIRequester() {}

void OAIRequester::initializeModel() {

    m_identifier_isSet = false;
    m_identifier_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIRequester::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRequester::fromJsonObject(QJsonObject json) {

    m_identifier_isValid = ::OpenAPI::fromJsonValue(m_identifier, json[QString("identifier")]);
    m_identifier_isSet = !json[QString("identifier")].isNull() && m_identifier_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIRequester::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRequester::asJsonObject() const {
    QJsonObject obj;
    if (m_identifier.isSet()) {
        obj.insert(QString("identifier"), ::OpenAPI::toJsonValue(m_identifier));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

OAIRequester_identifier OAIRequester::getIdentifier() const {
    return m_identifier;
}
void OAIRequester::setIdentifier(const OAIRequester_identifier &identifier) {
    m_identifier = identifier;
    m_identifier_isSet = true;
}

bool OAIRequester::is_identifier_Set() const{
    return m_identifier_isSet;
}

bool OAIRequester::is_identifier_Valid() const{
    return m_identifier_isValid;
}

QString OAIRequester::getName() const {
    return m_name;
}
void OAIRequester::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIRequester::is_name_Set() const{
    return m_name_isSet;
}

bool OAIRequester::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIRequester::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_identifier.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRequester::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
