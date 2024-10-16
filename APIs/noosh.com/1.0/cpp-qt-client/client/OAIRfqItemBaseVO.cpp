/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRfqItemBaseVO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRfqItemBaseVO::OAIRfqItemBaseVO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRfqItemBaseVO::OAIRfqItemBaseVO() {
    this->initializeModel();
}

OAIRfqItemBaseVO::~OAIRfqItemBaseVO() {}

void OAIRfqItemBaseVO::initializeModel() {

    m_job_id_isSet = false;
    m_job_id_isValid = false;

    m_rfq_item_id_isSet = false;
    m_rfq_item_id_isValid = false;

    m_spec_isSet = false;
    m_spec_isValid = false;
}

void OAIRfqItemBaseVO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRfqItemBaseVO::fromJsonObject(QJsonObject json) {

    m_job_id_isValid = ::OpenAPI::fromJsonValue(m_job_id, json[QString("job_id")]);
    m_job_id_isSet = !json[QString("job_id")].isNull() && m_job_id_isValid;

    m_rfq_item_id_isValid = ::OpenAPI::fromJsonValue(m_rfq_item_id, json[QString("rfq_item_id")]);
    m_rfq_item_id_isSet = !json[QString("rfq_item_id")].isNull() && m_rfq_item_id_isValid;

    m_spec_isValid = ::OpenAPI::fromJsonValue(m_spec, json[QString("spec")]);
    m_spec_isSet = !json[QString("spec")].isNull() && m_spec_isValid;
}

QString OAIRfqItemBaseVO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRfqItemBaseVO::asJsonObject() const {
    QJsonObject obj;
    if (m_job_id_isSet) {
        obj.insert(QString("job_id"), ::OpenAPI::toJsonValue(m_job_id));
    }
    if (m_rfq_item_id_isSet) {
        obj.insert(QString("rfq_item_id"), ::OpenAPI::toJsonValue(m_rfq_item_id));
    }
    if (m_spec.isSet()) {
        obj.insert(QString("spec"), ::OpenAPI::toJsonValue(m_spec));
    }
    return obj;
}

qint64 OAIRfqItemBaseVO::getJobId() const {
    return m_job_id;
}
void OAIRfqItemBaseVO::setJobId(const qint64 &job_id) {
    m_job_id = job_id;
    m_job_id_isSet = true;
}

bool OAIRfqItemBaseVO::is_job_id_Set() const{
    return m_job_id_isSet;
}

bool OAIRfqItemBaseVO::is_job_id_Valid() const{
    return m_job_id_isValid;
}

qint64 OAIRfqItemBaseVO::getRfqItemId() const {
    return m_rfq_item_id;
}
void OAIRfqItemBaseVO::setRfqItemId(const qint64 &rfq_item_id) {
    m_rfq_item_id = rfq_item_id;
    m_rfq_item_id_isSet = true;
}

bool OAIRfqItemBaseVO::is_rfq_item_id_Set() const{
    return m_rfq_item_id_isSet;
}

bool OAIRfqItemBaseVO::is_rfq_item_id_Valid() const{
    return m_rfq_item_id_isValid;
}

OAIErgoSpecSimpleVO OAIRfqItemBaseVO::getSpec() const {
    return m_spec;
}
void OAIRfqItemBaseVO::setSpec(const OAIErgoSpecSimpleVO &spec) {
    m_spec = spec;
    m_spec_isSet = true;
}

bool OAIRfqItemBaseVO::is_spec_Set() const{
    return m_spec_isSet;
}

bool OAIRfqItemBaseVO::is_spec_Valid() const{
    return m_spec_isValid;
}

bool OAIRfqItemBaseVO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_job_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rfq_item_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_spec.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRfqItemBaseVO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
