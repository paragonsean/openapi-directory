/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIShareRedemption.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIShareRedemption::OAIIShareRedemption(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIShareRedemption::OAIIShareRedemption() {
    this->initializeModel();
}

OAIIShareRedemption::~OAIIShareRedemption() {}

void OAIIShareRedemption::initializeModel() {

    m_activity_data_isSet = false;
    m_activity_data_isValid = false;

    m_share_id_isSet = false;
    m_share_id_isValid = false;

    m_share_type_isSet = false;
    m_share_type_isValid = false;

    m_shareholder_isSet = false;
    m_shareholder_isValid = false;
}

void OAIIShareRedemption::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIShareRedemption::fromJsonObject(QJsonObject json) {

    m_activity_data_isValid = ::OpenAPI::fromJsonValue(m_activity_data, json[QString("activityData")]);
    m_activity_data_isSet = !json[QString("activityData")].isNull() && m_activity_data_isValid;

    m_share_id_isValid = ::OpenAPI::fromJsonValue(m_share_id, json[QString("shareId")]);
    m_share_id_isSet = !json[QString("shareId")].isNull() && m_share_id_isValid;

    m_share_type_isValid = ::OpenAPI::fromJsonValue(m_share_type, json[QString("shareType")]);
    m_share_type_isSet = !json[QString("shareType")].isNull() && m_share_type_isValid;

    m_shareholder_isValid = ::OpenAPI::fromJsonValue(m_shareholder, json[QString("shareholder")]);
    m_shareholder_isSet = !json[QString("shareholder")].isNull() && m_shareholder_isValid;
}

QString OAIIShareRedemption::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIShareRedemption::asJsonObject() const {
    QJsonObject obj;
    if (m_activity_data.isSet()) {
        obj.insert(QString("activityData"), ::OpenAPI::toJsonValue(m_activity_data));
    }
    if (m_share_id_isSet) {
        obj.insert(QString("shareId"), ::OpenAPI::toJsonValue(m_share_id));
    }
    if (m_share_type.isSet()) {
        obj.insert(QString("shareType"), ::OpenAPI::toJsonValue(m_share_type));
    }
    if (m_shareholder_isSet) {
        obj.insert(QString("shareholder"), ::OpenAPI::toJsonValue(m_shareholder));
    }
    return obj;
}

OAIIActivityData OAIIShareRedemption::getActivityData() const {
    return m_activity_data;
}
void OAIIShareRedemption::setActivityData(const OAIIActivityData &activity_data) {
    m_activity_data = activity_data;
    m_activity_data_isSet = true;
}

bool OAIIShareRedemption::is_activity_data_Set() const{
    return m_activity_data_isSet;
}

bool OAIIShareRedemption::is_activity_data_Valid() const{
    return m_activity_data_isValid;
}

qint32 OAIIShareRedemption::getShareId() const {
    return m_share_id;
}
void OAIIShareRedemption::setShareId(const qint32 &share_id) {
    m_share_id = share_id;
    m_share_id_isSet = true;
}

bool OAIIShareRedemption::is_share_id_Set() const{
    return m_share_id_isSet;
}

bool OAIIShareRedemption::is_share_id_Valid() const{
    return m_share_id_isValid;
}

OAIFormattedEnumType_PrivateCorporationShareType OAIIShareRedemption::getShareType() const {
    return m_share_type;
}
void OAIIShareRedemption::setShareType(const OAIFormattedEnumType_PrivateCorporationShareType &share_type) {
    m_share_type = share_type;
    m_share_type_isSet = true;
}

bool OAIIShareRedemption::is_share_type_Set() const{
    return m_share_type_isSet;
}

bool OAIIShareRedemption::is_share_type_Valid() const{
    return m_share_type_isValid;
}

QString OAIIShareRedemption::getShareholder() const {
    return m_shareholder;
}
void OAIIShareRedemption::setShareholder(const QString &shareholder) {
    m_shareholder = shareholder;
    m_shareholder_isSet = true;
}

bool OAIIShareRedemption::is_shareholder_Set() const{
    return m_shareholder_isSet;
}

bool OAIIShareRedemption::is_shareholder_Valid() const{
    return m_shareholder_isValid;
}

bool OAIIShareRedemption::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_activity_data.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_share_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_share_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_shareholder_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIShareRedemption::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
