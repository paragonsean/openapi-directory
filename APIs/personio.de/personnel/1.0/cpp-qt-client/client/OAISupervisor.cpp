/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISupervisor.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISupervisor::OAISupervisor(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISupervisor::OAISupervisor() {
    this->initializeModel();
}

OAISupervisor::~OAISupervisor() {}

void OAISupervisor::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;
}

void OAISupervisor::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISupervisor::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;
}

QString OAISupervisor::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISupervisor::asJsonObject() const {
    QJsonObject obj;
    if (m_value.isSet()) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    return obj;
}

OAIEmployee OAISupervisor::getValue() const {
    return m_value;
}
void OAISupervisor::setValue(const OAIEmployee &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAISupervisor::is_value_Set() const{
    return m_value_isSet;
}

bool OAISupervisor::is_value_Valid() const{
    return m_value_isValid;
}

QString OAISupervisor::getLabel() const {
    return m_label;
}
void OAISupervisor::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAISupervisor::is_label_Set() const{
    return m_label_isSet;
}

bool OAISupervisor::is_label_Valid() const{
    return m_label_isValid;
}

bool OAISupervisor::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_value.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISupervisor::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_label_isValid && true;
}

} // namespace OpenAPI
