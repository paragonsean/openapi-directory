/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIModel::OAIModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIModel::OAIModel() {
    this->initializeModel();
}

OAIModel::~OAIModel() {}

void OAIModel::initializeModel() {

    m_created_time_isSet = false;
    m_created_time_isValid = false;

    m_datasets_isSet = false;
    m_datasets_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_experiment_name_isSet = false;
    m_experiment_name_isValid = false;

    m_framework_isSet = false;
    m_framework_isValid = false;

    m_framework_version_isSet = false;
    m_framework_version_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_kv_tags_isSet = false;
    m_kv_tags_isValid = false;

    m_mime_type_isSet = false;
    m_mime_type_isValid = false;

    m_modified_time_isSet = false;
    m_modified_time_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_parent_model_id_isSet = false;
    m_parent_model_id_isValid = false;

    m_properties_isSet = false;
    m_properties_isValid = false;

    m_run_id_isSet = false;
    m_run_id_isValid = false;

    m_unpack_isSet = false;
    m_unpack_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIModel::fromJsonObject(QJsonObject json) {

    m_created_time_isValid = ::OpenAPI::fromJsonValue(m_created_time, json[QString("createdTime")]);
    m_created_time_isSet = !json[QString("createdTime")].isNull() && m_created_time_isValid;

    m_datasets_isValid = ::OpenAPI::fromJsonValue(m_datasets, json[QString("datasets")]);
    m_datasets_isSet = !json[QString("datasets")].isNull() && m_datasets_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_experiment_name_isValid = ::OpenAPI::fromJsonValue(m_experiment_name, json[QString("experimentName")]);
    m_experiment_name_isSet = !json[QString("experimentName")].isNull() && m_experiment_name_isValid;

    m_framework_isValid = ::OpenAPI::fromJsonValue(m_framework, json[QString("framework")]);
    m_framework_isSet = !json[QString("framework")].isNull() && m_framework_isValid;

    m_framework_version_isValid = ::OpenAPI::fromJsonValue(m_framework_version, json[QString("frameworkVersion")]);
    m_framework_version_isSet = !json[QString("frameworkVersion")].isNull() && m_framework_version_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_kv_tags_isValid = ::OpenAPI::fromJsonValue(m_kv_tags, json[QString("kvTags")]);
    m_kv_tags_isSet = !json[QString("kvTags")].isNull() && m_kv_tags_isValid;

    m_mime_type_isValid = ::OpenAPI::fromJsonValue(m_mime_type, json[QString("mimeType")]);
    m_mime_type_isSet = !json[QString("mimeType")].isNull() && m_mime_type_isValid;

    m_modified_time_isValid = ::OpenAPI::fromJsonValue(m_modified_time, json[QString("modifiedTime")]);
    m_modified_time_isSet = !json[QString("modifiedTime")].isNull() && m_modified_time_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_parent_model_id_isValid = ::OpenAPI::fromJsonValue(m_parent_model_id, json[QString("parentModelId")]);
    m_parent_model_id_isSet = !json[QString("parentModelId")].isNull() && m_parent_model_id_isValid;

    m_properties_isValid = ::OpenAPI::fromJsonValue(m_properties, json[QString("properties")]);
    m_properties_isSet = !json[QString("properties")].isNull() && m_properties_isValid;

    m_run_id_isValid = ::OpenAPI::fromJsonValue(m_run_id, json[QString("runId")]);
    m_run_id_isSet = !json[QString("runId")].isNull() && m_run_id_isValid;

    m_unpack_isValid = ::OpenAPI::fromJsonValue(m_unpack, json[QString("unpack")]);
    m_unpack_isSet = !json[QString("unpack")].isNull() && m_unpack_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIModel::asJsonObject() const {
    QJsonObject obj;
    if (m_created_time_isSet) {
        obj.insert(QString("createdTime"), ::OpenAPI::toJsonValue(m_created_time));
    }
    if (m_datasets.size() > 0) {
        obj.insert(QString("datasets"), ::OpenAPI::toJsonValue(m_datasets));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_experiment_name_isSet) {
        obj.insert(QString("experimentName"), ::OpenAPI::toJsonValue(m_experiment_name));
    }
    if (m_framework_isSet) {
        obj.insert(QString("framework"), ::OpenAPI::toJsonValue(m_framework));
    }
    if (m_framework_version_isSet) {
        obj.insert(QString("frameworkVersion"), ::OpenAPI::toJsonValue(m_framework_version));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_kv_tags.size() > 0) {
        obj.insert(QString("kvTags"), ::OpenAPI::toJsonValue(m_kv_tags));
    }
    if (m_mime_type_isSet) {
        obj.insert(QString("mimeType"), ::OpenAPI::toJsonValue(m_mime_type));
    }
    if (m_modified_time_isSet) {
        obj.insert(QString("modifiedTime"), ::OpenAPI::toJsonValue(m_modified_time));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_parent_model_id_isSet) {
        obj.insert(QString("parentModelId"), ::OpenAPI::toJsonValue(m_parent_model_id));
    }
    if (m_properties.size() > 0) {
        obj.insert(QString("properties"), ::OpenAPI::toJsonValue(m_properties));
    }
    if (m_run_id_isSet) {
        obj.insert(QString("runId"), ::OpenAPI::toJsonValue(m_run_id));
    }
    if (m_unpack_isSet) {
        obj.insert(QString("unpack"), ::OpenAPI::toJsonValue(m_unpack));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QDateTime OAIModel::getCreatedTime() const {
    return m_created_time;
}
void OAIModel::setCreatedTime(const QDateTime &created_time) {
    m_created_time = created_time;
    m_created_time_isSet = true;
}

bool OAIModel::is_created_time_Set() const{
    return m_created_time_isSet;
}

bool OAIModel::is_created_time_Valid() const{
    return m_created_time_isValid;
}

QList<OAIDatasetReference> OAIModel::getDatasets() const {
    return m_datasets;
}
void OAIModel::setDatasets(const QList<OAIDatasetReference> &datasets) {
    m_datasets = datasets;
    m_datasets_isSet = true;
}

bool OAIModel::is_datasets_Set() const{
    return m_datasets_isSet;
}

bool OAIModel::is_datasets_Valid() const{
    return m_datasets_isValid;
}

QString OAIModel::getDescription() const {
    return m_description;
}
void OAIModel::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIModel::is_description_Set() const{
    return m_description_isSet;
}

bool OAIModel::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIModel::getExperimentName() const {
    return m_experiment_name;
}
void OAIModel::setExperimentName(const QString &experiment_name) {
    m_experiment_name = experiment_name;
    m_experiment_name_isSet = true;
}

bool OAIModel::is_experiment_name_Set() const{
    return m_experiment_name_isSet;
}

bool OAIModel::is_experiment_name_Valid() const{
    return m_experiment_name_isValid;
}

QString OAIModel::getFramework() const {
    return m_framework;
}
void OAIModel::setFramework(const QString &framework) {
    m_framework = framework;
    m_framework_isSet = true;
}

bool OAIModel::is_framework_Set() const{
    return m_framework_isSet;
}

bool OAIModel::is_framework_Valid() const{
    return m_framework_isValid;
}

QString OAIModel::getFrameworkVersion() const {
    return m_framework_version;
}
void OAIModel::setFrameworkVersion(const QString &framework_version) {
    m_framework_version = framework_version;
    m_framework_version_isSet = true;
}

bool OAIModel::is_framework_version_Set() const{
    return m_framework_version_isSet;
}

bool OAIModel::is_framework_version_Valid() const{
    return m_framework_version_isValid;
}

QString OAIModel::getId() const {
    return m_id;
}
void OAIModel::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIModel::is_id_Set() const{
    return m_id_isSet;
}

bool OAIModel::is_id_Valid() const{
    return m_id_isValid;
}

QMap<QString, QString> OAIModel::getKvTags() const {
    return m_kv_tags;
}
void OAIModel::setKvTags(const QMap<QString, QString> &kv_tags) {
    m_kv_tags = kv_tags;
    m_kv_tags_isSet = true;
}

bool OAIModel::is_kv_tags_Set() const{
    return m_kv_tags_isSet;
}

bool OAIModel::is_kv_tags_Valid() const{
    return m_kv_tags_isValid;
}

QString OAIModel::getMimeType() const {
    return m_mime_type;
}
void OAIModel::setMimeType(const QString &mime_type) {
    m_mime_type = mime_type;
    m_mime_type_isSet = true;
}

bool OAIModel::is_mime_type_Set() const{
    return m_mime_type_isSet;
}

bool OAIModel::is_mime_type_Valid() const{
    return m_mime_type_isValid;
}

QDateTime OAIModel::getModifiedTime() const {
    return m_modified_time;
}
void OAIModel::setModifiedTime(const QDateTime &modified_time) {
    m_modified_time = modified_time;
    m_modified_time_isSet = true;
}

bool OAIModel::is_modified_time_Set() const{
    return m_modified_time_isSet;
}

bool OAIModel::is_modified_time_Valid() const{
    return m_modified_time_isValid;
}

QString OAIModel::getName() const {
    return m_name;
}
void OAIModel::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIModel::is_name_Set() const{
    return m_name_isSet;
}

bool OAIModel::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIModel::getParentModelId() const {
    return m_parent_model_id;
}
void OAIModel::setParentModelId(const QString &parent_model_id) {
    m_parent_model_id = parent_model_id;
    m_parent_model_id_isSet = true;
}

bool OAIModel::is_parent_model_id_Set() const{
    return m_parent_model_id_isSet;
}

bool OAIModel::is_parent_model_id_Valid() const{
    return m_parent_model_id_isValid;
}

QMap<QString, QString> OAIModel::getProperties() const {
    return m_properties;
}
void OAIModel::setProperties(const QMap<QString, QString> &properties) {
    m_properties = properties;
    m_properties_isSet = true;
}

bool OAIModel::is_properties_Set() const{
    return m_properties_isSet;
}

bool OAIModel::is_properties_Valid() const{
    return m_properties_isValid;
}

QString OAIModel::getRunId() const {
    return m_run_id;
}
void OAIModel::setRunId(const QString &run_id) {
    m_run_id = run_id;
    m_run_id_isSet = true;
}

bool OAIModel::is_run_id_Set() const{
    return m_run_id_isSet;
}

bool OAIModel::is_run_id_Valid() const{
    return m_run_id_isValid;
}

bool OAIModel::isUnpack() const {
    return m_unpack;
}
void OAIModel::setUnpack(const bool &unpack) {
    m_unpack = unpack;
    m_unpack_isSet = true;
}

bool OAIModel::is_unpack_Set() const{
    return m_unpack_isSet;
}

bool OAIModel::is_unpack_Valid() const{
    return m_unpack_isValid;
}

QString OAIModel::getUrl() const {
    return m_url;
}
void OAIModel::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIModel::is_url_Set() const{
    return m_url_isSet;
}

bool OAIModel::is_url_Valid() const{
    return m_url_isValid;
}

qint64 OAIModel::getVersion() const {
    return m_version;
}
void OAIModel::setVersion(const qint64 &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIModel::is_version_Set() const{
    return m_version_isSet;
}

bool OAIModel::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datasets.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_experiment_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_framework_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_framework_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_kv_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_mime_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_parent_model_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_run_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unpack_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_mime_type_isValid && m_name_isValid && m_url_isValid && true;
}

} // namespace OpenAPI
