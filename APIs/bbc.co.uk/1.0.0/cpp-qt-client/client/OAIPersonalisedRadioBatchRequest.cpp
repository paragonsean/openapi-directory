/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPersonalisedRadioBatchRequest.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPersonalisedRadioBatchRequest::OAIPersonalisedRadioBatchRequest(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPersonalisedRadioBatchRequest::OAIPersonalisedRadioBatchRequest() {
    this->initializeModel();
}

OAIPersonalisedRadioBatchRequest::~OAIPersonalisedRadioBatchRequest() {}

void OAIPersonalisedRadioBatchRequest::initializeModel() {

    m_action_isSet = false;
    m_action_isValid = false;

    m_added_at_isSet = false;
    m_added_at_isValid = false;

    m_context_isSet = false;
    m_context_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_metadata_isSet = false;
    m_metadata_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIPersonalisedRadioBatchRequest::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPersonalisedRadioBatchRequest::fromJsonObject(QJsonObject json) {

    m_action_isValid = ::OpenAPI::fromJsonValue(m_action, json[QString("action")]);
    m_action_isSet = !json[QString("action")].isNull() && m_action_isValid;

    m_added_at_isValid = ::OpenAPI::fromJsonValue(m_added_at, json[QString("added_at")]);
    m_added_at_isSet = !json[QString("added_at")].isNull() && m_added_at_isValid;

    m_context_isValid = ::OpenAPI::fromJsonValue(m_context, json[QString("context")]);
    m_context_isSet = !json[QString("context")].isNull() && m_context_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_metadata_isValid = ::OpenAPI::fromJsonValue(m_metadata, json[QString("metadata")]);
    m_metadata_isSet = !json[QString("metadata")].isNull() && m_metadata_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIPersonalisedRadioBatchRequest::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPersonalisedRadioBatchRequest::asJsonObject() const {
    QJsonObject obj;
    if (m_action_isSet) {
        obj.insert(QString("action"), ::OpenAPI::toJsonValue(m_action));
    }
    if (m_added_at_isSet) {
        obj.insert(QString("added_at"), ::OpenAPI::toJsonValue(m_added_at));
    }
    if (m_context_isSet) {
        obj.insert(QString("context"), ::OpenAPI::toJsonValue(m_context));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_metadata.isSet()) {
        obj.insert(QString("metadata"), ::OpenAPI::toJsonValue(m_metadata));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIPersonalisedRadioBatchRequest::getAction() const {
    return m_action;
}
void OAIPersonalisedRadioBatchRequest::setAction(const QString &action) {
    m_action = action;
    m_action_isSet = true;
}

bool OAIPersonalisedRadioBatchRequest::is_action_Set() const{
    return m_action_isSet;
}

bool OAIPersonalisedRadioBatchRequest::is_action_Valid() const{
    return m_action_isValid;
}

QString OAIPersonalisedRadioBatchRequest::getAddedAt() const {
    return m_added_at;
}
void OAIPersonalisedRadioBatchRequest::setAddedAt(const QString &added_at) {
    m_added_at = added_at;
    m_added_at_isSet = true;
}

bool OAIPersonalisedRadioBatchRequest::is_added_at_Set() const{
    return m_added_at_isSet;
}

bool OAIPersonalisedRadioBatchRequest::is_added_at_Valid() const{
    return m_added_at_isValid;
}

QString OAIPersonalisedRadioBatchRequest::getContext() const {
    return m_context;
}
void OAIPersonalisedRadioBatchRequest::setContext(const QString &context) {
    m_context = context;
    m_context_isSet = true;
}

bool OAIPersonalisedRadioBatchRequest::is_context_Set() const{
    return m_context_isSet;
}

bool OAIPersonalisedRadioBatchRequest::is_context_Valid() const{
    return m_context_isValid;
}

QString OAIPersonalisedRadioBatchRequest::getId() const {
    return m_id;
}
void OAIPersonalisedRadioBatchRequest::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIPersonalisedRadioBatchRequest::is_id_Set() const{
    return m_id_isSet;
}

bool OAIPersonalisedRadioBatchRequest::is_id_Valid() const{
    return m_id_isValid;
}

OAIPersonalisedRadioMetaData OAIPersonalisedRadioBatchRequest::getMetadata() const {
    return m_metadata;
}
void OAIPersonalisedRadioBatchRequest::setMetadata(const OAIPersonalisedRadioMetaData &metadata) {
    m_metadata = metadata;
    m_metadata_isSet = true;
}

bool OAIPersonalisedRadioBatchRequest::is_metadata_Set() const{
    return m_metadata_isSet;
}

bool OAIPersonalisedRadioBatchRequest::is_metadata_Valid() const{
    return m_metadata_isValid;
}

QString OAIPersonalisedRadioBatchRequest::getType() const {
    return m_type;
}
void OAIPersonalisedRadioBatchRequest::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPersonalisedRadioBatchRequest::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPersonalisedRadioBatchRequest::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIPersonalisedRadioBatchRequest::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_added_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_context_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_metadata.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPersonalisedRadioBatchRequest::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_action_isValid && true;
}

} // namespace OpenAPI
