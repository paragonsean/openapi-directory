/**
 * Mailscript
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.4.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAddActionCombineRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAddActionCombineRequest::OAIAddActionCombineRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAddActionCombineRequest::OAIAddActionCombineRequest() {
    this->initializeModel();
}

OAIAddActionCombineRequest::~OAIAddActionCombineRequest() {}

void OAIAddActionCombineRequest::initializeModel() {

    m_list_isSet = false;
    m_list_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIAddActionCombineRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAddActionCombineRequest::fromJsonObject(QJsonObject json) {

    m_list_isValid = ::OpenAPI::fromJsonValue(m_list, json[QString("list")]);
    m_list_isSet = !json[QString("list")].isNull() && m_list_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIAddActionCombineRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAddActionCombineRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_list.size() > 0) {
        obj.insert(QString("list"), ::OpenAPI::toJsonValue(m_list));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QList<QString> OAIAddActionCombineRequest::getList() const {
    return m_list;
}
void OAIAddActionCombineRequest::setList(const QList<QString> &list) {
    m_list = list;
    m_list_isSet = true;
}

bool OAIAddActionCombineRequest::is_list_Set() const{
    return m_list_isSet;
}

bool OAIAddActionCombineRequest::is_list_Valid() const{
    return m_list_isValid;
}

QString OAIAddActionCombineRequest::getName() const {
    return m_name;
}
void OAIAddActionCombineRequest::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIAddActionCombineRequest::is_name_Set() const{
    return m_name_isSet;
}

bool OAIAddActionCombineRequest::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIAddActionCombineRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_list.size() > 0) {
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

bool OAIAddActionCombineRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_list_isValid && m_name_isValid && true;
}

} // namespace OpenAPI
