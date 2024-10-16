/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateContactListRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateContactListRequest::OAIUpdateContactListRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateContactListRequest::OAIUpdateContactListRequest() {
    this->initializeModel();
}

OAIUpdateContactListRequest::~OAIUpdateContactListRequest() {}

void OAIUpdateContactListRequest::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIUpdateContactListRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateContactListRequest::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIUpdateContactListRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateContactListRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIUpdateContactListRequest::getName() const {
    return m_name;
}
void OAIUpdateContactListRequest::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateContactListRequest::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateContactListRequest::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIUpdateContactListRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateContactListRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
