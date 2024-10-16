/**
 * SheerSEO API
 * Sheerseo API has 2 stages:<br>First stage - initiating the task: You fill in your task and receive in return the task id. <br>Second stage - collecting the results: send a request containing the task ids you got at the first stage and collecting the results.
 *
 * The version of the OpenAPI document: 0.0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISerpCollectResponse_tasks_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISerpCollectResponse_tasks_inner::OAISerpCollectResponse_tasks_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISerpCollectResponse_tasks_inner::OAISerpCollectResponse_tasks_inner() {
    this->initializeModel();
}

OAISerpCollectResponse_tasks_inner::~OAISerpCollectResponse_tasks_inner() {}

void OAISerpCollectResponse_tasks_inner::initializeModel() {

    m_task_id_isSet = false;
    m_task_id_isValid = false;
}

void OAISerpCollectResponse_tasks_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISerpCollectResponse_tasks_inner::fromJsonObject(QJsonObject json) {

    m_task_id_isValid = ::OpenAPI::fromJsonValue(m_task_id, json[QString("task_id")]);
    m_task_id_isSet = !json[QString("task_id")].isNull() && m_task_id_isValid;
}

QString OAISerpCollectResponse_tasks_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISerpCollectResponse_tasks_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_task_id.isSet()) {
        obj.insert(QString("task_id"), ::OpenAPI::toJsonValue(m_task_id));
    }
    return obj;
}

OAISerpCollectResponse_tasks_inner_task_id OAISerpCollectResponse_tasks_inner::getTaskId() const {
    return m_task_id;
}
void OAISerpCollectResponse_tasks_inner::setTaskId(const OAISerpCollectResponse_tasks_inner_task_id &task_id) {
    m_task_id = task_id;
    m_task_id_isSet = true;
}

bool OAISerpCollectResponse_tasks_inner::is_task_id_Set() const{
    return m_task_id_isSet;
}

bool OAISerpCollectResponse_tasks_inner::is_task_id_Valid() const{
    return m_task_id_isValid;
}

bool OAISerpCollectResponse_tasks_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_task_id.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISerpCollectResponse_tasks_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
