/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIFieldSelector.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFieldSelector::OAIFieldSelector(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFieldSelector::OAIFieldSelector() {
    this->initializeModel();
}

OAIFieldSelector::~OAIFieldSelector() {}

void OAIFieldSelector::initializeModel() {

    m_fields_isSet = false;
    m_fields_isValid = false;
}

void OAIFieldSelector::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFieldSelector::fromJsonObject(QJsonObject json) {

    m_fields_isValid = ::OpenAPI::fromJsonValue(m_fields, json[QString("fields")]);
    m_fields_isSet = !json[QString("fields")].isNull() && m_fields_isValid;
}

QString OAIFieldSelector::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFieldSelector::asJsonObject() const {
    QJsonObject obj;
    if (m_fields.size() > 0) {
        obj.insert(QString("fields"), ::OpenAPI::toJsonValue(m_fields));
    }
    return obj;
}

QList<OAIFieldReference> OAIFieldSelector::getFields() const {
    return m_fields;
}
void OAIFieldSelector::setFields(const QList<OAIFieldReference> &fields) {
    m_fields = fields;
    m_fields_isSet = true;
}

bool OAIFieldSelector::is_fields_Set() const{
    return m_fields_isSet;
}

bool OAIFieldSelector::is_fields_Valid() const{
    return m_fields_isValid;
}

bool OAIFieldSelector::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIFieldSelector::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
