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

#include "OAITasks_List_200_response_value_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITasks_List_200_response_value_inner::OAITasks_List_200_response_value_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITasks_List_200_response_value_inner::OAITasks_List_200_response_value_inner() {
    this->initializeModel();
}

OAITasks_List_200_response_value_inner::~OAITasks_List_200_response_value_inner() {}

void OAITasks_List_200_response_value_inner::initializeModel() {

    m_etag_isSet = false;
    m_etag_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;
}

void OAITasks_List_200_response_value_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITasks_List_200_response_value_inner::fromJsonObject(QJsonObject json) {

    m_etag_isValid = ::OpenAPI::fromJsonValue(m_etag, json[QString("etag")]);
    m_etag_isSet = !json[QString("etag")].isNull() && m_etag_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;
}

QString OAITasks_List_200_response_value_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITasks_List_200_response_value_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_etag_isSet) {
        obj.insert(QString("etag"), ::OpenAPI::toJsonValue(m_etag));
    }
    if (m_properties.isSet()) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    return obj;
}

QString OAITasks_List_200_response_value_inner::getEtag() const {
    return m_etag;
}
void OAITasks_List_200_response_value_inner::setEtag(const QString &etag) {
    m_etag = etag;
    m_etag_isSet = true;
}

bool OAITasks_List_200_response_value_inner::is_etag_Set() const{
    return m_etag_isSet;
}

bool OAITasks_List_200_response_value_inner::is_etag_Valid() const{
    return m_etag_isValid;
}

OAITasks_List_200_response_value_inner_properties OAITasks_List_200_response_value_inner::getProperties() const {
    return m_properties;
}
void OAITasks_List_200_response_value_inner::setProperties(const OAITasks_List_200_response_value_inner_properties &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAITasks_List_200_response_value_inner::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAITasks_List_200_response_value_inner::is_properties_Valid() const{
    return m_properties_isValid;
}

bool OAITasks_List_200_response_value_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_etag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITasks_List_200_response_value_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
