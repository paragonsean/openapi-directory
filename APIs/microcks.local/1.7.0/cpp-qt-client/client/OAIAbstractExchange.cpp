/**
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAbstractExchange.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAbstractExchange::OAIAbstractExchange(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAbstractExchange::OAIAbstractExchange() {
    this->initializeModel();
}

OAIAbstractExchange::~OAIAbstractExchange() {}

void OAIAbstractExchange::initializeModel() {

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIAbstractExchange::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAbstractExchange::fromJsonObject(QJsonObject json) {

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIAbstractExchange::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAbstractExchange::asJsonObject() const {
    QJsonObject obj;
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIAbstractExchange::getType() const {
    return m_type;
}
void OAIAbstractExchange::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIAbstractExchange::is_type_Set() const{
    return m_type_isSet;
}

bool OAIAbstractExchange::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIAbstractExchange::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAbstractExchange::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_type_isValid && true;
}

} // namespace OpenAPI
