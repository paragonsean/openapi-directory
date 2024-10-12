/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIManagerList.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIManagerList::OAIManagerList(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIManagerList::OAIManagerList() {
    this->initializeModel();
}

OAIManagerList::~OAIManagerList() {}

void OAIManagerList::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIManagerList::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIManagerList::fromJsonObject(QJsonObject json) {

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIManagerList::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIManagerList::asJsonObject() const {
    QJsonObject obj;
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QList<OAIManager> OAIManagerList::getValue() const {
    return m_value;
}
void OAIManagerList::setValue(const QList<OAIManager> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIManagerList::is_value_Set() const{
    return m_value_isSet;
}

bool OAIManagerList::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIManagerList::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIManagerList::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid && true;
}

} // namespace OpenAPI
