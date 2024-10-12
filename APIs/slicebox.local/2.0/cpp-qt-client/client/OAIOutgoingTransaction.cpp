/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOutgoingTransaction.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOutgoingTransaction::OAIOutgoingTransaction(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOutgoingTransaction::OAIOutgoingTransaction() {
    this->initializeModel();
}

OAIOutgoingTransaction::~OAIOutgoingTransaction() {}

void OAIOutgoingTransaction::initializeModel() {

    m_box_id_isSet = false;
    m_box_id_isValid = false;

    m_box_name_isSet = false;
    m_box_name_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_profile_isSet = false;
    m_profile_isValid = false;

    m_sent_image_count_isSet = false;
    m_sent_image_count_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_total_image_count_isSet = false;
    m_total_image_count_isValid = false;

    m_updated_isSet = false;
    m_updated_isValid = false;
}

void OAIOutgoingTransaction::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOutgoingTransaction::fromJsonObject(QJsonObject json) {

    m_box_id_isValid = ::OpenAPI::fromJsonValue(m_box_id, json[QString("boxId")]);
    m_box_id_isSet = !json[QString("boxId")].isNull() && m_box_id_isValid;

    m_box_name_isValid = ::OpenAPI::fromJsonValue(m_box_name, json[QString("boxName")]);
    m_box_name_isSet = !json[QString("boxName")].isNull() && m_box_name_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_profile_isValid = ::OpenAPI::fromJsonValue(m_profile, json[QString("profile")]);
    m_profile_isSet = !json[QString("profile")].isNull() && m_profile_isValid;

    m_sent_image_count_isValid = ::OpenAPI::fromJsonValue(m_sent_image_count, json[QString("sentImageCount")]);
    m_sent_image_count_isSet = !json[QString("sentImageCount")].isNull() && m_sent_image_count_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_total_image_count_isValid = ::OpenAPI::fromJsonValue(m_total_image_count, json[QString("totalImageCount")]);
    m_total_image_count_isSet = !json[QString("totalImageCount")].isNull() && m_total_image_count_isValid;

    m_updated_isValid = ::OpenAPI::fromJsonValue(m_updated, json[QString("updated")]);
    m_updated_isSet = !json[QString("updated")].isNull() && m_updated_isValid;
}

QString OAIOutgoingTransaction::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOutgoingTransaction::asJsonObject() const {
    QJsonObject obj;
    if (m_box_id_isSet) {
        obj.insert(QString("boxId"), ::OpenAPI::toJsonValue(m_box_id));
    }
    if (m_box_name_isSet) {
        obj.insert(QString("boxName"), ::OpenAPI::toJsonValue(m_box_name));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_profile.isSet()) {
        obj.insert(QString("profile"), ::OpenAPI::toJsonValue(m_profile));
    }
    if (m_sent_image_count_isSet) {
        obj.insert(QString("sentImageCount"), ::OpenAPI::toJsonValue(m_sent_image_count));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_total_image_count_isSet) {
        obj.insert(QString("totalImageCount"), ::OpenAPI::toJsonValue(m_total_image_count));
    }
    if (m_updated_isSet) {
        obj.insert(QString("updated"), ::OpenAPI::toJsonValue(m_updated));
    }
    return obj;
}

qint64 OAIOutgoingTransaction::getBoxId() const {
    return m_box_id;
}
void OAIOutgoingTransaction::setBoxId(const qint64 &box_id) {
    m_box_id = box_id;
    m_box_id_isSet = true;
}

bool OAIOutgoingTransaction::is_box_id_Set() const{
    return m_box_id_isSet;
}

bool OAIOutgoingTransaction::is_box_id_Valid() const{
    return m_box_id_isValid;
}

QString OAIOutgoingTransaction::getBoxName() const {
    return m_box_name;
}
void OAIOutgoingTransaction::setBoxName(const QString &box_name) {
    m_box_name = box_name;
    m_box_name_isSet = true;
}

bool OAIOutgoingTransaction::is_box_name_Set() const{
    return m_box_name_isSet;
}

bool OAIOutgoingTransaction::is_box_name_Valid() const{
    return m_box_name_isValid;
}

qint64 OAIOutgoingTransaction::getId() const {
    return m_id;
}
void OAIOutgoingTransaction::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIOutgoingTransaction::is_id_Set() const{
    return m_id_isSet;
}

bool OAIOutgoingTransaction::is_id_Valid() const{
    return m_id_isValid;
}

OAIAnonymizationProfile OAIOutgoingTransaction::getProfile() const {
    return m_profile;
}
void OAIOutgoingTransaction::setProfile(const OAIAnonymizationProfile &profile) {
    m_profile = profile;
    m_profile_isSet = true;
}

bool OAIOutgoingTransaction::is_profile_Set() const{
    return m_profile_isSet;
}

bool OAIOutgoingTransaction::is_profile_Valid() const{
    return m_profile_isValid;
}

qint64 OAIOutgoingTransaction::getSentImageCount() const {
    return m_sent_image_count;
}
void OAIOutgoingTransaction::setSentImageCount(const qint64 &sent_image_count) {
    m_sent_image_count = sent_image_count;
    m_sent_image_count_isSet = true;
}

bool OAIOutgoingTransaction::is_sent_image_count_Set() const{
    return m_sent_image_count_isSet;
}

bool OAIOutgoingTransaction::is_sent_image_count_Valid() const{
    return m_sent_image_count_isValid;
}

QString OAIOutgoingTransaction::getStatus() const {
    return m_status;
}
void OAIOutgoingTransaction::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIOutgoingTransaction::is_status_Set() const{
    return m_status_isSet;
}

bool OAIOutgoingTransaction::is_status_Valid() const{
    return m_status_isValid;
}

qint64 OAIOutgoingTransaction::getTotalImageCount() const {
    return m_total_image_count;
}
void OAIOutgoingTransaction::setTotalImageCount(const qint64 &total_image_count) {
    m_total_image_count = total_image_count;
    m_total_image_count_isSet = true;
}

bool OAIOutgoingTransaction::is_total_image_count_Set() const{
    return m_total_image_count_isSet;
}

bool OAIOutgoingTransaction::is_total_image_count_Valid() const{
    return m_total_image_count_isValid;
}

qint64 OAIOutgoingTransaction::getUpdated() const {
    return m_updated;
}
void OAIOutgoingTransaction::setUpdated(const qint64 &updated) {
    m_updated = updated;
    m_updated_isSet = true;
}

bool OAIOutgoingTransaction::is_updated_Set() const{
    return m_updated_isSet;
}

bool OAIOutgoingTransaction::is_updated_Valid() const{
    return m_updated_isValid;
}

bool OAIOutgoingTransaction::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_box_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_box_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_profile.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_sent_image_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_image_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOutgoingTransaction::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
