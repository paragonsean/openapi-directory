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

#include "OAIOffice.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOffice::OAIOffice(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOffice::OAIOffice() {
    this->initializeModel();
}

OAIOffice::~OAIOffice() {}

void OAIOffice::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;
}

void OAIOffice::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOffice::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;
}

QString OAIOffice::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOffice::asJsonObject() const {
    QJsonObject obj;
    if (m_value.isSet()) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    return obj;
}

OAIObject OAIOffice::getValue() const {
    return m_value;
}
void OAIOffice::setValue(const OAIObject &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIOffice::is_value_Set() const{
    return m_value_isSet;
}

bool OAIOffice::is_value_Valid() const{
    return m_value_isValid;
}

QString OAIOffice::getLabel() const {
    return m_label;
}
void OAIOffice::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIOffice::is_label_Set() const{
    return m_label_isSet;
}

bool OAIOffice::is_label_Valid() const{
    return m_label_isValid;
}

bool OAIOffice::isSet() const {
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

bool OAIOffice::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_label_isValid && true;
}

} // namespace OpenAPI
