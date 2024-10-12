/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEndpoint_post_users_invites.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEndpoint_post_users_invites::OAIEndpoint_post_users_invites(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEndpoint_post_users_invites::OAIEndpoint_post_users_invites() {
    this->initializeModel();
}

OAIEndpoint_post_users_invites::~OAIEndpoint_post_users_invites() {}

void OAIEndpoint_post_users_invites::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_success_isSet = false;
    m_success_isValid = false;
}

void OAIEndpoint_post_users_invites::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEndpoint_post_users_invites::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_success_isValid = ::OpenAPI::fromJsonValue(m_success, json[QString("success")]);
    m_success_isSet = !json[QString("success")].isNull() && m_success_isValid;
}

QString OAIEndpoint_post_users_invites::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEndpoint_post_users_invites::asJsonObject() const {
    QJsonObject obj;
    if (m_data.isSet()) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_success_isSet) {
        obj.insert(QString("success"), ::OpenAPI::toJsonValue(m_success));
    }
    return obj;
}

OAIEndpoint_post_users_invites_data OAIEndpoint_post_users_invites::getData() const {
    return m_data;
}
void OAIEndpoint_post_users_invites::setData(const OAIEndpoint_post_users_invites_data &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIEndpoint_post_users_invites::is_data_Set() const{
    return m_data_isSet;
}

bool OAIEndpoint_post_users_invites::is_data_Valid() const{
    return m_data_isValid;
}

bool OAIEndpoint_post_users_invites::isSuccess() const {
    return m_success;
}
void OAIEndpoint_post_users_invites::setSuccess(const bool &success) {
    m_success = success;
    m_success_isSet = true;
}

bool OAIEndpoint_post_users_invites::is_success_Set() const{
    return m_success_isSet;
}

bool OAIEndpoint_post_users_invites::is_success_Valid() const{
    return m_success_isValid;
}

bool OAIEndpoint_post_users_invites::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_success_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEndpoint_post_users_invites::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
