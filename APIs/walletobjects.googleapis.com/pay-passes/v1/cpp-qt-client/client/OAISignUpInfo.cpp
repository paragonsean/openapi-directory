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

#include "OAISignUpInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISignUpInfo::OAISignUpInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISignUpInfo::OAISignUpInfo() {
    this->initializeModel();
}

OAISignUpInfo::~OAISignUpInfo() {}

void OAISignUpInfo::initializeModel() {

    m_class_id_isSet = false;
    m_class_id_isValid = false;
}

void OAISignUpInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISignUpInfo::fromJsonObject(QJsonObject json) {

    m_class_id_isValid = ::OpenAPI::fromJsonValue(m_class_id, json[QString("classId")]);
    m_class_id_isSet = !json[QString("classId")].isNull() && m_class_id_isValid;
}

QString OAISignUpInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISignUpInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_class_id_isSet) {
        obj.insert(QString("classId"), ::OpenAPI::toJsonValue(m_class_id));
    }
    return obj;
}

QString OAISignUpInfo::getClassId() const {
    return m_class_id;
}
void OAISignUpInfo::setClassId(const QString &class_id) {
    m_class_id = class_id;
    m_class_id_isSet = true;
}

bool OAISignUpInfo::is_class_id_Set() const{
    return m_class_id_isSet;
}

bool OAISignUpInfo::is_class_id_Valid() const{
    return m_class_id_isValid;
}

bool OAISignUpInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_class_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISignUpInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
