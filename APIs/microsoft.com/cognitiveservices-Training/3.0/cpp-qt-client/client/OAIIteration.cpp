/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIteration.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIteration::OAIIteration(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIteration::OAIIteration() {
    this->initializeModel();
}

OAIIteration::~OAIIteration() {}

void OAIIteration::initializeModel() {

    m_classification_type_isSet = false;
    m_classification_type_isValid = false;

    m_created_isSet = false;
    m_created_isValid = false;

    m_domain_id_isSet = false;
    m_domain_id_isValid = false;

    m_exportable_isSet = false;
    m_exportable_isValid = false;

    m_exportable_to_isSet = false;
    m_exportable_to_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_last_modified_isSet = false;
    m_last_modified_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_original_publish_resource_id_isSet = false;
    m_original_publish_resource_id_isValid = false;

    m_project_id_isSet = false;
    m_project_id_isValid = false;

    m_publish_name_isSet = false;
    m_publish_name_isValid = false;

    m_reserved_budget_in_hours_isSet = false;
    m_reserved_budget_in_hours_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_trained_at_isSet = false;
    m_trained_at_isValid = false;

    m_training_type_isSet = false;
    m_training_type_isValid = false;
}

void OAIIteration::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIteration::fromJsonObject(QJsonObject json) {

    m_classification_type_isValid = ::OpenAPI::fromJsonValue(m_classification_type, json[QString("classificationType")]);
    m_classification_type_isSet = !json[QString("classificationType")].isNull() && m_classification_type_isValid;

    m_created_isValid = ::OpenAPI::fromJsonValue(m_created, json[QString("created")]);
    m_created_isSet = !json[QString("created")].isNull() && m_created_isValid;

    m_domain_id_isValid = ::OpenAPI::fromJsonValue(m_domain_id, json[QString("domainId")]);
    m_domain_id_isSet = !json[QString("domainId")].isNull() && m_domain_id_isValid;

    m_exportable_isValid = ::OpenAPI::fromJsonValue(m_exportable, json[QString("exportable")]);
    m_exportable_isSet = !json[QString("exportable")].isNull() && m_exportable_isValid;

    m_exportable_to_isValid = ::OpenAPI::fromJsonValue(m_exportable_to, json[QString("exportableTo")]);
    m_exportable_to_isSet = !json[QString("exportableTo")].isNull() && m_exportable_to_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_last_modified_isValid = ::OpenAPI::fromJsonValue(m_last_modified, json[QString("lastModified")]);
    m_last_modified_isSet = !json[QString("lastModified")].isNull() && m_last_modified_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_original_publish_resource_id_isValid = ::OpenAPI::fromJsonValue(m_original_publish_resource_id, json[QString("originalPublishResourceId")]);
    m_original_publish_resource_id_isSet = !json[QString("originalPublishResourceId")].isNull() && m_original_publish_resource_id_isValid;

    m_project_id_isValid = ::OpenAPI::fromJsonValue(m_project_id, json[QString("projectId")]);
    m_project_id_isSet = !json[QString("projectId")].isNull() && m_project_id_isValid;

    m_publish_name_isValid = ::OpenAPI::fromJsonValue(m_publish_name, json[QString("publishName")]);
    m_publish_name_isSet = !json[QString("publishName")].isNull() && m_publish_name_isValid;

    m_reserved_budget_in_hours_isValid = ::OpenAPI::fromJsonValue(m_reserved_budget_in_hours, json[QString("reservedBudgetInHours")]);
    m_reserved_budget_in_hours_isSet = !json[QString("reservedBudgetInHours")].isNull() && m_reserved_budget_in_hours_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_trained_at_isValid = ::OpenAPI::fromJsonValue(m_trained_at, json[QString("trainedAt")]);
    m_trained_at_isSet = !json[QString("trainedAt")].isNull() && m_trained_at_isValid;

    m_training_type_isValid = ::OpenAPI::fromJsonValue(m_training_type, json[QString("trainingType")]);
    m_training_type_isSet = !json[QString("trainingType")].isNull() && m_training_type_isValid;
}

QString OAIIteration::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIteration::asJsonObject() const {
    QJsonObject obj;
    if (m_classification_type_isSet) {
        obj.insert(QString("classificationType"), ::OpenAPI::toJsonValue(m_classification_type));
    }
    if (m_created_isSet) {
        obj.insert(QString("created"), ::OpenAPI::toJsonValue(m_created));
    }
    if (m_domain_id_isSet) {
        obj.insert(QString("domainId"), ::OpenAPI::toJsonValue(m_domain_id));
    }
    if (m_exportable_isSet) {
        obj.insert(QString("exportable"), ::OpenAPI::toJsonValue(m_exportable));
    }
    if (m_exportable_to.size() > 0) {
        obj.insert(QString("exportableTo"), ::OpenAPI::toJsonValue(m_exportable_to));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_last_modified_isSet) {
        obj.insert(QString("lastModified"), ::OpenAPI::toJsonValue(m_last_modified));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_original_publish_resource_id_isSet) {
        obj.insert(QString("originalPublishResourceId"), ::OpenAPI::toJsonValue(m_original_publish_resource_id));
    }
    if (m_project_id_isSet) {
        obj.insert(QString("projectId"), ::OpenAPI::toJsonValue(m_project_id));
    }
    if (m_publish_name_isSet) {
        obj.insert(QString("publishName"), ::OpenAPI::toJsonValue(m_publish_name));
    }
    if (m_reserved_budget_in_hours_isSet) {
        obj.insert(QString("reservedBudgetInHours"), ::OpenAPI::toJsonValue(m_reserved_budget_in_hours));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_trained_at_isSet) {
        obj.insert(QString("trainedAt"), ::OpenAPI::toJsonValue(m_trained_at));
    }
    if (m_training_type_isSet) {
        obj.insert(QString("trainingType"), ::OpenAPI::toJsonValue(m_training_type));
    }
    return obj;
}

QString OAIIteration::getClassificationType() const {
    return m_classification_type;
}
void OAIIteration::setClassificationType(const QString &classification_type) {
    m_classification_type = classification_type;
    m_classification_type_isSet = true;
}

bool OAIIteration::is_classification_type_Set() const{
    return m_classification_type_isSet;
}

bool OAIIteration::is_classification_type_Valid() const{
    return m_classification_type_isValid;
}

QDateTime OAIIteration::getCreated() const {
    return m_created;
}
void OAIIteration::setCreated(const QDateTime &created) {
    m_created = created;
    m_created_isSet = true;
}

bool OAIIteration::is_created_Set() const{
    return m_created_isSet;
}

bool OAIIteration::is_created_Valid() const{
    return m_created_isValid;
}

QString OAIIteration::getDomainId() const {
    return m_domain_id;
}
void OAIIteration::setDomainId(const QString &domain_id) {
    m_domain_id = domain_id;
    m_domain_id_isSet = true;
}

bool OAIIteration::is_domain_id_Set() const{
    return m_domain_id_isSet;
}

bool OAIIteration::is_domain_id_Valid() const{
    return m_domain_id_isValid;
}

bool OAIIteration::isExportable() const {
    return m_exportable;
}
void OAIIteration::setExportable(const bool &exportable) {
    m_exportable = exportable;
    m_exportable_isSet = true;
}

bool OAIIteration::is_exportable_Set() const{
    return m_exportable_isSet;
}

bool OAIIteration::is_exportable_Valid() const{
    return m_exportable_isValid;
}

QList<QString> OAIIteration::getExportableTo() const {
    return m_exportable_to;
}
void OAIIteration::setExportableTo(const QList<QString> &exportable_to) {
    m_exportable_to = exportable_to;
    m_exportable_to_isSet = true;
}

bool OAIIteration::is_exportable_to_Set() const{
    return m_exportable_to_isSet;
}

bool OAIIteration::is_exportable_to_Valid() const{
    return m_exportable_to_isValid;
}

QString OAIIteration::getId() const {
    return m_id;
}
void OAIIteration::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIIteration::is_id_Set() const{
    return m_id_isSet;
}

bool OAIIteration::is_id_Valid() const{
    return m_id_isValid;
}

QDateTime OAIIteration::getLastModified() const {
    return m_last_modified;
}
void OAIIteration::setLastModified(const QDateTime &last_modified) {
    m_last_modified = last_modified;
    m_last_modified_isSet = true;
}

bool OAIIteration::is_last_modified_Set() const{
    return m_last_modified_isSet;
}

bool OAIIteration::is_last_modified_Valid() const{
    return m_last_modified_isValid;
}

QString OAIIteration::getName() const {
    return m_name;
}
void OAIIteration::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIIteration::is_name_Set() const{
    return m_name_isSet;
}

bool OAIIteration::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIIteration::getOriginalPublishResourceId() const {
    return m_original_publish_resource_id;
}
void OAIIteration::setOriginalPublishResourceId(const QString &original_publish_resource_id) {
    m_original_publish_resource_id = original_publish_resource_id;
    m_original_publish_resource_id_isSet = true;
}

bool OAIIteration::is_original_publish_resource_id_Set() const{
    return m_original_publish_resource_id_isSet;
}

bool OAIIteration::is_original_publish_resource_id_Valid() const{
    return m_original_publish_resource_id_isValid;
}

QString OAIIteration::getProjectId() const {
    return m_project_id;
}
void OAIIteration::setProjectId(const QString &project_id) {
    m_project_id = project_id;
    m_project_id_isSet = true;
}

bool OAIIteration::is_project_id_Set() const{
    return m_project_id_isSet;
}

bool OAIIteration::is_project_id_Valid() const{
    return m_project_id_isValid;
}

QString OAIIteration::getPublishName() const {
    return m_publish_name;
}
void OAIIteration::setPublishName(const QString &publish_name) {
    m_publish_name = publish_name;
    m_publish_name_isSet = true;
}

bool OAIIteration::is_publish_name_Set() const{
    return m_publish_name_isSet;
}

bool OAIIteration::is_publish_name_Valid() const{
    return m_publish_name_isValid;
}

qint32 OAIIteration::getReservedBudgetInHours() const {
    return m_reserved_budget_in_hours;
}
void OAIIteration::setReservedBudgetInHours(const qint32 &reserved_budget_in_hours) {
    m_reserved_budget_in_hours = reserved_budget_in_hours;
    m_reserved_budget_in_hours_isSet = true;
}

bool OAIIteration::is_reserved_budget_in_hours_Set() const{
    return m_reserved_budget_in_hours_isSet;
}

bool OAIIteration::is_reserved_budget_in_hours_Valid() const{
    return m_reserved_budget_in_hours_isValid;
}

QString OAIIteration::getStatus() const {
    return m_status;
}
void OAIIteration::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIIteration::is_status_Set() const{
    return m_status_isSet;
}

bool OAIIteration::is_status_Valid() const{
    return m_status_isValid;
}

QDateTime OAIIteration::getTrainedAt() const {
    return m_trained_at;
}
void OAIIteration::setTrainedAt(const QDateTime &trained_at) {
    m_trained_at = trained_at;
    m_trained_at_isSet = true;
}

bool OAIIteration::is_trained_at_Set() const{
    return m_trained_at_isSet;
}

bool OAIIteration::is_trained_at_Valid() const{
    return m_trained_at_isValid;
}

QString OAIIteration::getTrainingType() const {
    return m_training_type;
}
void OAIIteration::setTrainingType(const QString &training_type) {
    m_training_type = training_type;
    m_training_type_isSet = true;
}

bool OAIIteration::is_training_type_Set() const{
    return m_training_type_isSet;
}

bool OAIIteration::is_training_type_Valid() const{
    return m_training_type_isValid;
}

bool OAIIteration::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_classification_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_domain_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exportable_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_exportable_to.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_modified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_original_publish_resource_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_project_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publish_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reserved_budget_in_hours_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_trained_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_training_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIteration::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_name_isValid && true;
}

} // namespace OpenAPI
