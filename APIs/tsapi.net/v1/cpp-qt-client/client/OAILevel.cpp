/**
 * TSAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILevel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILevel::OAILevel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILevel::OAILevel() {
    this->initializeModel();
}

OAILevel::~OAILevel() {}

void OAILevel::initializeModel() {

    m_ident_isSet = false;
    m_ident_isValid = false;
}

void OAILevel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILevel::fromJsonObject(QJsonObject json) {

    m_ident_isValid = ::OpenAPI::fromJsonValue(m_ident, json[QString("ident")]);
    m_ident_isSet = !json[QString("ident")].isNull() && m_ident_isValid;
}

QString OAILevel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILevel::asJsonObject() const {
    QJsonObject obj;
    if (m_ident_isSet) {
        obj.insert(QString("ident"), ::OpenAPI::toJsonValue(m_ident));
    }
    return obj;
}

QString OAILevel::getIdent() const {
    return m_ident;
}
void OAILevel::setIdent(const QString &ident) {
    m_ident = ident;
    m_ident_isSet = true;
}

bool OAILevel::is_ident_Set() const{
    return m_ident_isSet;
}

bool OAILevel::is_ident_Valid() const{
    return m_ident_isValid;
}

bool OAILevel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ident_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILevel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
