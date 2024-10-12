/**
 * Azure Data Migration Service Resource Provider
 * The Data Migration Service helps people migrate their data from on-premise database servers to Azure, or from older database software to newer software. The service manages one or more workers that are joined to a customer's virtual network, which is assumed to provide connectivity to their databases. To avoid frequent updates to the resource provider, data migration tasks are implemented by the resource provider in a generic way as task resources, each of which has a task type (which identifies the type of work to run), input, and output. The client is responsible for providing appropriate task type and inputs, which will be passed through unexamined to the machines that implement the functionality, and for understanding the output, which is passed back unexamined to the client.
 *
 * The version of the OpenAPI document: 2018-03-15-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo() {
    this->initializeModel();
}

OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::~OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo() {}

void OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::initializeModel() {

    m_password_isSet = false;
    m_password_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_user_name_isSet = false;
    m_user_name_isValid = false;
}

void OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::fromJsonObject(QJsonObject json) {

    m_password_isValid = ::OpenAPI::fromJsonValue(m_password, json[QString("password")]);
    m_password_isSet = !json[QString("password")].isNull() && m_password_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_user_name_isValid = ::OpenAPI::fromJsonValue(m_user_name, json[QString("userName")]);
    m_user_name_isSet = !json[QString("userName")].isNull() && m_user_name_isValid;
}

QString OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_password_isSet) {
        obj.insert(QString("password"), ::OpenAPI::toJsonValue(m_password));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_user_name_isSet) {
        obj.insert(QString("userName"), ::OpenAPI::toJsonValue(m_user_name));
    }
    return obj;
}

QString OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::getPassword() const {
    return m_password;
}
void OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::setPassword(const QString &password) {
    m_password = password;
    m_password_isSet = true;
}

bool OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::is_password_Set() const{
    return m_password_isSet;
}

bool OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::is_password_Valid() const{
    return m_password_isValid;
}

QString OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::getType() const {
    return m_type;
}
void OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::is_type_Set() const{
    return m_type_isSet;
}

bool OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::getUserName() const {
    return m_user_name;
}
void OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::setUserName(const QString &user_name) {
    m_user_name = user_name;
    m_user_name_isSet = true;
}

bool OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::is_user_name_Set() const{
    return m_user_name_isSet;
}

bool OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::is_user_name_Valid() const{
    return m_user_name_isValid;
}

bool OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_password_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProjects_List_200_response_value_inner_properties_sourceConnectionInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_type_isValid && true;
}

} // namespace OpenAPI
