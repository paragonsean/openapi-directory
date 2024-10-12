/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWebhookV2EventData.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWebhookV2EventData::OAIWebhookV2EventData(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWebhookV2EventData::OAIWebhookV2EventData() {
    this->initializeModel();
}

OAIWebhookV2EventData::~OAIWebhookV2EventData() {}

void OAIWebhookV2EventData::initializeModel() {

    m_form_details_isSet = false;
    m_form_details_isValid = false;

    m_resources_isSet = false;
    m_resources_isValid = false;

    m_share_isSet = false;
    m_share_isValid = false;

    m_transfer_status_isSet = false;
    m_transfer_status_isValid = false;
}

void OAIWebhookV2EventData::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWebhookV2EventData::fromJsonObject(QJsonObject json) {

    m_form_details_isValid = ::OpenAPI::fromJsonValue(m_form_details, json[QString("formDetails")]);
    m_form_details_isSet = !json[QString("formDetails")].isNull() && m_form_details_isValid;

    m_resources_isValid = ::OpenAPI::fromJsonValue(m_resources, json[QString("resources")]);
    m_resources_isSet = !json[QString("resources")].isNull() && m_resources_isValid;

    m_share_isValid = ::OpenAPI::fromJsonValue(m_share, json[QString("share")]);
    m_share_isSet = !json[QString("share")].isNull() && m_share_isValid;

    m_transfer_status_isValid = ::OpenAPI::fromJsonValue(m_transfer_status, json[QString("transferStatus")]);
    m_transfer_status_isSet = !json[QString("transferStatus")].isNull() && m_transfer_status_isValid;
}

QString OAIWebhookV2EventData::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWebhookV2EventData::asJsonObject() const {
    QJsonObject obj;
    if (m_form_details.size() > 0) {
        obj.insert(QString("formDetails"), ::OpenAPI::toJsonValue(m_form_details));
    }
    if (m_resources.size() > 0) {
        obj.insert(QString("resources"), ::OpenAPI::toJsonValue(m_resources));
    }
    if (m_share.size() > 0) {
        obj.insert(QString("share"), ::OpenAPI::toJsonValue(m_share));
    }
    if (m_transfer_status_isSet) {
        obj.insert(QString("transferStatus"), ::OpenAPI::toJsonValue(m_transfer_status));
    }
    return obj;
}

QList<OAIObject> OAIWebhookV2EventData::getFormDetails() const {
    return m_form_details;
}
void OAIWebhookV2EventData::setFormDetails(const QList<OAIObject> &form_details) {
    m_form_details = form_details;
    m_form_details_isSet = true;
}

bool OAIWebhookV2EventData::is_form_details_Set() const{
    return m_form_details_isSet;
}

bool OAIWebhookV2EventData::is_form_details_Valid() const{
    return m_form_details_isValid;
}

QList<OAIWebhookV2EventData_resources_inner> OAIWebhookV2EventData::getResources() const {
    return m_resources;
}
void OAIWebhookV2EventData::setResources(const QList<OAIWebhookV2EventData_resources_inner> &resources) {
    m_resources = resources;
    m_resources_isSet = true;
}

bool OAIWebhookV2EventData::is_resources_Set() const{
    return m_resources_isSet;
}

bool OAIWebhookV2EventData::is_resources_Valid() const{
    return m_resources_isValid;
}

QList<OAIWebhookV2EventData_share_inner> OAIWebhookV2EventData::getShare() const {
    return m_share;
}
void OAIWebhookV2EventData::setShare(const QList<OAIWebhookV2EventData_share_inner> &share) {
    m_share = share;
    m_share_isSet = true;
}

bool OAIWebhookV2EventData::is_share_Set() const{
    return m_share_isSet;
}

bool OAIWebhookV2EventData::is_share_Valid() const{
    return m_share_isValid;
}

QString OAIWebhookV2EventData::getTransferStatus() const {
    return m_transfer_status;
}
void OAIWebhookV2EventData::setTransferStatus(const QString &transfer_status) {
    m_transfer_status = transfer_status;
    m_transfer_status_isSet = true;
}

bool OAIWebhookV2EventData::is_transfer_status_Set() const{
    return m_transfer_status_isSet;
}

bool OAIWebhookV2EventData::is_transfer_status_Valid() const{
    return m_transfer_status_isValid;
}

bool OAIWebhookV2EventData::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_form_details.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_resources.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_share.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_transfer_status_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWebhookV2EventData::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
