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

#include "OAIGetAllInputsResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetAllInputsResponse::OAIGetAllInputsResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetAllInputsResponse::OAIGetAllInputsResponse() {
    this->initializeModel();
}

OAIGetAllInputsResponse::~OAIGetAllInputsResponse() {}

void OAIGetAllInputsResponse::initializeModel() {

    m_list_isSet = false;
    m_list_isValid = false;
}

void OAIGetAllInputsResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetAllInputsResponse::fromJsonObject(QJsonObject json) {

    m_list_isValid = ::OpenAPI::fromJsonValue(m_list, json[QString("list")]);
    m_list_isSet = !json[QString("list")].isNull() && m_list_isValid;
}

QString OAIGetAllInputsResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetAllInputsResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_list.size() > 0) {
        obj.insert(QString("list"), ::OpenAPI::toJsonValue(m_list));
    }
    return obj;
}

QList<OAIGetAllInputsResponse_list_inner> OAIGetAllInputsResponse::getList() const {
    return m_list;
}
void OAIGetAllInputsResponse::setList(const QList<OAIGetAllInputsResponse_list_inner> &list) {
    m_list = list;
    m_list_isSet = true;
}

bool OAIGetAllInputsResponse::is_list_Set() const{
    return m_list_isSet;
}

bool OAIGetAllInputsResponse::is_list_Valid() const{
    return m_list_isValid;
}

bool OAIGetAllInputsResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetAllInputsResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_list_isValid && true;
}

} // namespace OpenAPI
