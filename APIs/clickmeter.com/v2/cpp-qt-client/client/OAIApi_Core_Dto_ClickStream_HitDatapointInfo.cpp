/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApi_Core_Dto_ClickStream_HitDatapointInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApi_Core_Dto_ClickStream_HitDatapointInfo::OAIApi_Core_Dto_ClickStream_HitDatapointInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApi_Core_Dto_ClickStream_HitDatapointInfo::OAIApi_Core_Dto_ClickStream_HitDatapointInfo() {
    this->initializeModel();
}

OAIApi_Core_Dto_ClickStream_HitDatapointInfo::~OAIApi_Core_Dto_ClickStream_HitDatapointInfo() {}

void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::initializeModel() {

    m_creation_date_isSet = false;
    m_creation_date_isValid = false;

    m_datapoint_favourite_isSet = false;
    m_datapoint_favourite_isValid = false;

    m_datapoint_id_isSet = false;
    m_datapoint_id_isValid = false;

    m_datapoint_name_isSet = false;
    m_datapoint_name_isValid = false;

    m_datapoint_title_isSet = false;
    m_datapoint_title_isValid = false;

    m_datapoint_type_isSet = false;
    m_datapoint_type_isValid = false;

    m_destination_url_isSet = false;
    m_destination_url_isValid = false;

    m_group_id_isSet = false;
    m_group_id_isValid = false;

    m_group_name_isSet = false;
    m_group_name_isValid = false;

    m_is_ab_test_isSet = false;
    m_is_ab_test_isValid = false;

    m_is_private_shared_isSet = false;
    m_is_private_shared_isValid = false;

    m_is_public_isSet = false;
    m_is_public_isValid = false;

    m_notes_isSet = false;
    m_notes_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;

    m_tracking_code_isSet = false;
    m_tracking_code_isValid = false;
}

void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::fromJsonObject(QJsonObject json) {

    m_creation_date_isValid = ::OpenAPI::fromJsonValue(m_creation_date, json[QString("creationDate")]);
    m_creation_date_isSet = !json[QString("creationDate")].isNull() && m_creation_date_isValid;

    m_datapoint_favourite_isValid = ::OpenAPI::fromJsonValue(m_datapoint_favourite, json[QString("datapointFavourite")]);
    m_datapoint_favourite_isSet = !json[QString("datapointFavourite")].isNull() && m_datapoint_favourite_isValid;

    m_datapoint_id_isValid = ::OpenAPI::fromJsonValue(m_datapoint_id, json[QString("datapointId")]);
    m_datapoint_id_isSet = !json[QString("datapointId")].isNull() && m_datapoint_id_isValid;

    m_datapoint_name_isValid = ::OpenAPI::fromJsonValue(m_datapoint_name, json[QString("datapointName")]);
    m_datapoint_name_isSet = !json[QString("datapointName")].isNull() && m_datapoint_name_isValid;

    m_datapoint_title_isValid = ::OpenAPI::fromJsonValue(m_datapoint_title, json[QString("datapointTitle")]);
    m_datapoint_title_isSet = !json[QString("datapointTitle")].isNull() && m_datapoint_title_isValid;

    m_datapoint_type_isValid = ::OpenAPI::fromJsonValue(m_datapoint_type, json[QString("datapointType")]);
    m_datapoint_type_isSet = !json[QString("datapointType")].isNull() && m_datapoint_type_isValid;

    m_destination_url_isValid = ::OpenAPI::fromJsonValue(m_destination_url, json[QString("destinationUrl")]);
    m_destination_url_isSet = !json[QString("destinationUrl")].isNull() && m_destination_url_isValid;

    m_group_id_isValid = ::OpenAPI::fromJsonValue(m_group_id, json[QString("groupId")]);
    m_group_id_isSet = !json[QString("groupId")].isNull() && m_group_id_isValid;

    m_group_name_isValid = ::OpenAPI::fromJsonValue(m_group_name, json[QString("groupName")]);
    m_group_name_isSet = !json[QString("groupName")].isNull() && m_group_name_isValid;

    m_is_ab_test_isValid = ::OpenAPI::fromJsonValue(m_is_ab_test, json[QString("isABTest")]);
    m_is_ab_test_isSet = !json[QString("isABTest")].isNull() && m_is_ab_test_isValid;

    m_is_private_shared_isValid = ::OpenAPI::fromJsonValue(m_is_private_shared, json[QString("isPrivateShared")]);
    m_is_private_shared_isSet = !json[QString("isPrivateShared")].isNull() && m_is_private_shared_isValid;

    m_is_public_isValid = ::OpenAPI::fromJsonValue(m_is_public, json[QString("isPublic")]);
    m_is_public_isSet = !json[QString("isPublic")].isNull() && m_is_public_isValid;

    m_notes_isValid = ::OpenAPI::fromJsonValue(m_notes, json[QString("notes")]);
    m_notes_isSet = !json[QString("notes")].isNull() && m_notes_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;

    m_tracking_code_isValid = ::OpenAPI::fromJsonValue(m_tracking_code, json[QString("trackingCode")]);
    m_tracking_code_isSet = !json[QString("trackingCode")].isNull() && m_tracking_code_isValid;
}

QString OAIApi_Core_Dto_ClickStream_HitDatapointInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApi_Core_Dto_ClickStream_HitDatapointInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_creation_date_isSet) {
        obj.insert(QString("creationDate"), ::OpenAPI::toJsonValue(m_creation_date));
    }
    if (m_datapoint_favourite_isSet) {
        obj.insert(QString("datapointFavourite"), ::OpenAPI::toJsonValue(m_datapoint_favourite));
    }
    if (m_datapoint_id_isSet) {
        obj.insert(QString("datapointId"), ::OpenAPI::toJsonValue(m_datapoint_id));
    }
    if (m_datapoint_name_isSet) {
        obj.insert(QString("datapointName"), ::OpenAPI::toJsonValue(m_datapoint_name));
    }
    if (m_datapoint_title_isSet) {
        obj.insert(QString("datapointTitle"), ::OpenAPI::toJsonValue(m_datapoint_title));
    }
    if (m_datapoint_type_isSet) {
        obj.insert(QString("datapointType"), ::OpenAPI::toJsonValue(m_datapoint_type));
    }
    if (m_destination_url_isSet) {
        obj.insert(QString("destinationUrl"), ::OpenAPI::toJsonValue(m_destination_url));
    }
    if (m_group_id_isSet) {
        obj.insert(QString("groupId"), ::OpenAPI::toJsonValue(m_group_id));
    }
    if (m_group_name_isSet) {
        obj.insert(QString("groupName"), ::OpenAPI::toJsonValue(m_group_name));
    }
    if (m_is_ab_test_isSet) {
        obj.insert(QString("isABTest"), ::OpenAPI::toJsonValue(m_is_ab_test));
    }
    if (m_is_private_shared_isSet) {
        obj.insert(QString("isPrivateShared"), ::OpenAPI::toJsonValue(m_is_private_shared));
    }
    if (m_is_public_isSet) {
        obj.insert(QString("isPublic"), ::OpenAPI::toJsonValue(m_is_public));
    }
    if (m_notes_isSet) {
        obj.insert(QString("notes"), ::OpenAPI::toJsonValue(m_notes));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    if (m_tracking_code_isSet) {
        obj.insert(QString("trackingCode"), ::OpenAPI::toJsonValue(m_tracking_code));
    }
    return obj;
}

QString OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getCreationDate() const {
    return m_creation_date;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setCreationDate(const QString &creation_date) {
    m_creation_date = creation_date;
    m_creation_date_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_creation_date_Set() const{
    return m_creation_date_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_creation_date_Valid() const{
    return m_creation_date_isValid;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::isDatapointFavourite() const {
    return m_datapoint_favourite;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setDatapointFavourite(const bool &datapoint_favourite) {
    m_datapoint_favourite = datapoint_favourite;
    m_datapoint_favourite_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_datapoint_favourite_Set() const{
    return m_datapoint_favourite_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_datapoint_favourite_Valid() const{
    return m_datapoint_favourite_isValid;
}

qint64 OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getDatapointId() const {
    return m_datapoint_id;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setDatapointId(const qint64 &datapoint_id) {
    m_datapoint_id = datapoint_id;
    m_datapoint_id_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_datapoint_id_Set() const{
    return m_datapoint_id_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_datapoint_id_Valid() const{
    return m_datapoint_id_isValid;
}

QString OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getDatapointName() const {
    return m_datapoint_name;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setDatapointName(const QString &datapoint_name) {
    m_datapoint_name = datapoint_name;
    m_datapoint_name_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_datapoint_name_Set() const{
    return m_datapoint_name_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_datapoint_name_Valid() const{
    return m_datapoint_name_isValid;
}

QString OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getDatapointTitle() const {
    return m_datapoint_title;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setDatapointTitle(const QString &datapoint_title) {
    m_datapoint_title = datapoint_title;
    m_datapoint_title_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_datapoint_title_Set() const{
    return m_datapoint_title_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_datapoint_title_Valid() const{
    return m_datapoint_title_isValid;
}

QString OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getDatapointType() const {
    return m_datapoint_type;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setDatapointType(const QString &datapoint_type) {
    m_datapoint_type = datapoint_type;
    m_datapoint_type_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_datapoint_type_Set() const{
    return m_datapoint_type_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_datapoint_type_Valid() const{
    return m_datapoint_type_isValid;
}

QString OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getDestinationUrl() const {
    return m_destination_url;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setDestinationUrl(const QString &destination_url) {
    m_destination_url = destination_url;
    m_destination_url_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_destination_url_Set() const{
    return m_destination_url_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_destination_url_Valid() const{
    return m_destination_url_isValid;
}

qint64 OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getGroupId() const {
    return m_group_id;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setGroupId(const qint64 &group_id) {
    m_group_id = group_id;
    m_group_id_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_group_id_Set() const{
    return m_group_id_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_group_id_Valid() const{
    return m_group_id_isValid;
}

QString OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getGroupName() const {
    return m_group_name;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setGroupName(const QString &group_name) {
    m_group_name = group_name;
    m_group_name_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_group_name_Set() const{
    return m_group_name_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_group_name_Valid() const{
    return m_group_name_isValid;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::isIsAbTest() const {
    return m_is_ab_test;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setIsAbTest(const bool &is_ab_test) {
    m_is_ab_test = is_ab_test;
    m_is_ab_test_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_is_ab_test_Set() const{
    return m_is_ab_test_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_is_ab_test_Valid() const{
    return m_is_ab_test_isValid;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::isIsPrivateShared() const {
    return m_is_private_shared;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setIsPrivateShared(const bool &is_private_shared) {
    m_is_private_shared = is_private_shared;
    m_is_private_shared_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_is_private_shared_Set() const{
    return m_is_private_shared_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_is_private_shared_Valid() const{
    return m_is_private_shared_isValid;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::isIsPublic() const {
    return m_is_public;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setIsPublic(const bool &is_public) {
    m_is_public = is_public;
    m_is_public_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_is_public_Set() const{
    return m_is_public_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_is_public_Valid() const{
    return m_is_public_isValid;
}

QString OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getNotes() const {
    return m_notes;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setNotes(const QString &notes) {
    m_notes = notes;
    m_notes_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_notes_Set() const{
    return m_notes_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_notes_Valid() const{
    return m_notes_isValid;
}

QString OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getStatus() const {
    return m_status;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setStatus(const QString &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_status_Set() const{
    return m_status_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_status_Valid() const{
    return m_status_isValid;
}

QList<OAIApi_Core_Dto_Tags_Tag> OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getTags() const {
    return m_tags;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setTags(const QList<OAIApi_Core_Dto_Tags_Tag> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_tags_Valid() const{
    return m_tags_isValid;
}

QString OAIApi_Core_Dto_ClickStream_HitDatapointInfo::getTrackingCode() const {
    return m_tracking_code;
}
void OAIApi_Core_Dto_ClickStream_HitDatapointInfo::setTrackingCode(const QString &tracking_code) {
    m_tracking_code = tracking_code;
    m_tracking_code_isSet = true;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_tracking_code_Set() const{
    return m_tracking_code_isSet;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::is_tracking_code_Valid() const{
    return m_tracking_code_isValid;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_creation_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datapoint_favourite_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datapoint_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datapoint_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datapoint_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_datapoint_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_destination_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_group_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_ab_test_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_private_shared_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_public_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_notes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tracking_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApi_Core_Dto_ClickStream_HitDatapointInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
