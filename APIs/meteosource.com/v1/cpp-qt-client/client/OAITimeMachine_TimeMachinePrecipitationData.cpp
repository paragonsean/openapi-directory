/**
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITimeMachine_TimeMachinePrecipitationData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITimeMachine_TimeMachinePrecipitationData::OAITimeMachine_TimeMachinePrecipitationData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITimeMachine_TimeMachinePrecipitationData::OAITimeMachine_TimeMachinePrecipitationData() {
    this->initializeModel();
}

OAITimeMachine_TimeMachinePrecipitationData::~OAITimeMachine_TimeMachinePrecipitationData() {}

void OAITimeMachine_TimeMachinePrecipitationData::initializeModel() {

    m_total_isSet = false;
    m_total_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAITimeMachine_TimeMachinePrecipitationData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITimeMachine_TimeMachinePrecipitationData::fromJsonObject(QJsonObject json) {

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAITimeMachine_TimeMachinePrecipitationData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITimeMachine_TimeMachinePrecipitationData::asJsonObject() const {
    QJsonObject obj;
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    if (m_type.isSet()) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

double OAITimeMachine_TimeMachinePrecipitationData::getTotal() const {
    return m_total;
}
void OAITimeMachine_TimeMachinePrecipitationData::setTotal(const double &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAITimeMachine_TimeMachinePrecipitationData::is_total_Set() const{
    return m_total_isSet;
}

bool OAITimeMachine_TimeMachinePrecipitationData::is_total_Valid() const{
    return m_total_isValid;
}

OAIHttpFileElement OAITimeMachine_TimeMachinePrecipitationData::getType() const {
    return m_type;
}
void OAITimeMachine_TimeMachinePrecipitationData::setType(const OAIHttpFileElement &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAITimeMachine_TimeMachinePrecipitationData::is_type_Set() const{
    return m_type_isSet;
}

bool OAITimeMachine_TimeMachinePrecipitationData::is_type_Valid() const{
    return m_type_isValid;
}

bool OAITimeMachine_TimeMachinePrecipitationData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITimeMachine_TimeMachinePrecipitationData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
