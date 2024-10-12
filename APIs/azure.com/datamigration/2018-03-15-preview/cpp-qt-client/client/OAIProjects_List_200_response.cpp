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

#include "OAIProjects_List_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProjects_List_200_response::OAIProjects_List_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProjects_List_200_response::OAIProjects_List_200_response() {
    this->initializeModel();
}

OAIProjects_List_200_response::~OAIProjects_List_200_response() {}

void OAIProjects_List_200_response::initializeModel() {

    m_next_link_isSet = false;
    m_next_link_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIProjects_List_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProjects_List_200_response::fromJsonObject(QJsonObject json) {

    m_next_link_isValid = ::OpenAPI::fromJsonValue(m_next_link, json[QString("nextLink")]);
    m_next_link_isSet = !json[QString("nextLink")].isNull() && m_next_link_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIProjects_List_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProjects_List_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_next_link_isSet) {
        obj.insert(QString("nextLink"), ::OpenAPI::toJsonValue(m_next_link));
    }
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIProjects_List_200_response::getNextLink() const {
    return m_next_link;
}
void OAIProjects_List_200_response::setNextLink(const QString &next_link) {
    m_next_link = next_link;
    m_next_link_isSet = true;
}

bool OAIProjects_List_200_response::is_next_link_Set() const{
    return m_next_link_isSet;
}

bool OAIProjects_List_200_response::is_next_link_Valid() const{
    return m_next_link_isValid;
}

QList<OAIProjects_List_200_response_value_inner> OAIProjects_List_200_response::getValue() const {
    return m_value;
}
void OAIProjects_List_200_response::setValue(const QList<OAIProjects_List_200_response_value_inner> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIProjects_List_200_response::is_value_Set() const{
    return m_value_isSet;
}

bool OAIProjects_List_200_response::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIProjects_List_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_next_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProjects_List_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
