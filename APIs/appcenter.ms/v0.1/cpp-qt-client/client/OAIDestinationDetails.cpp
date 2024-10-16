/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDestinationDetails.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDestinationDetails::OAIDestinationDetails(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDestinationDetails::OAIDestinationDetails() {
    this->initializeModel();
}

OAIDestinationDetails::~OAIDestinationDetails() {}

void OAIDestinationDetails::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIDestinationDetails::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDestinationDetails::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIDestinationDetails::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDestinationDetails::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIDestinationDetails::getId() const {
    return m_id;
}
void OAIDestinationDetails::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIDestinationDetails::is_id_Set() const{
    return m_id_isSet;
}

bool OAIDestinationDetails::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIDestinationDetails::getType() const {
    return m_type;
}
void OAIDestinationDetails::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIDestinationDetails::is_type_Set() const{
    return m_type_isSet;
}

bool OAIDestinationDetails::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIDestinationDetails::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDestinationDetails::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
