/**
 * agentOS API V3, Diary Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-diary
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDiaryAppointmentModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDiaryAppointmentModel::OAIDiaryAppointmentModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDiaryAppointmentModel::OAIDiaryAppointmentModel() {
    this->initializeModel();
}

OAIDiaryAppointmentModel::~OAIDiaryAppointmentModel() {}

void OAIDiaryAppointmentModel::initializeModel() {

    m_appointment_type_isSet = false;
    m_appointment_type_isValid = false;

    m_cancelled_isSet = false;
    m_cancelled_isValid = false;

    m_comment_isSet = false;
    m_comment_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_e_tag_isSet = false;
    m_e_tag_isValid = false;

    m_end_isSet = false;
    m_end_isValid = false;

    m_linked_guest_isSet = false;
    m_linked_guest_isValid = false;

    m_linked_properties_isSet = false;
    m_linked_properties_isValid = false;

    m_next_recurring_date_isSet = false;
    m_next_recurring_date_isValid = false;

    m_oid_isSet = false;
    m_oid_isValid = false;

    m_recurrence_isSet = false;
    m_recurrence_isValid = false;

    m_recurrence_type_isSet = false;
    m_recurrence_type_isValid = false;

    m_remind_at_isSet = false;
    m_remind_at_isValid = false;

    m_remind_before_isSet = false;
    m_remind_before_isValid = false;

    m_staff_isSet = false;
    m_staff_isValid = false;

    m_start_isSet = false;
    m_start_isValid = false;

    m_subject_isSet = false;
    m_subject_isValid = false;
}

void OAIDiaryAppointmentModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDiaryAppointmentModel::fromJsonObject(QJsonObject json) {

    m_appointment_type_isValid = ::OpenAPI::fromJsonValue(m_appointment_type, json[QString("AppointmentType")]);
    m_appointment_type_isSet = !json[QString("AppointmentType")].isNull() && m_appointment_type_isValid;

    m_cancelled_isValid = ::OpenAPI::fromJsonValue(m_cancelled, json[QString("Cancelled")]);
    m_cancelled_isSet = !json[QString("Cancelled")].isNull() && m_cancelled_isValid;

    m_comment_isValid = ::OpenAPI::fromJsonValue(m_comment, json[QString("Comment")]);
    m_comment_isSet = !json[QString("Comment")].isNull() && m_comment_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("CreatedAt")]);
    m_created_at_isSet = !json[QString("CreatedAt")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("CreatedBy")]);
    m_created_by_isSet = !json[QString("CreatedBy")].isNull() && m_created_by_isValid;

    m_e_tag_isValid = ::OpenAPI::fromJsonValue(m_e_tag, json[QString("ETag")]);
    m_e_tag_isSet = !json[QString("ETag")].isNull() && m_e_tag_isValid;

    m_end_isValid = ::OpenAPI::fromJsonValue(m_end, json[QString("End")]);
    m_end_isSet = !json[QString("End")].isNull() && m_end_isValid;

    m_linked_guest_isValid = ::OpenAPI::fromJsonValue(m_linked_guest, json[QString("LinkedGuest")]);
    m_linked_guest_isSet = !json[QString("LinkedGuest")].isNull() && m_linked_guest_isValid;

    m_linked_properties_isValid = ::OpenAPI::fromJsonValue(m_linked_properties, json[QString("LinkedProperties")]);
    m_linked_properties_isSet = !json[QString("LinkedProperties")].isNull() && m_linked_properties_isValid;

    m_next_recurring_date_isValid = ::OpenAPI::fromJsonValue(m_next_recurring_date, json[QString("NextRecurringDate")]);
    m_next_recurring_date_isSet = !json[QString("NextRecurringDate")].isNull() && m_next_recurring_date_isValid;

    m_oid_isValid = ::OpenAPI::fromJsonValue(m_oid, json[QString("OID")]);
    m_oid_isSet = !json[QString("OID")].isNull() && m_oid_isValid;

    m_recurrence_isValid = ::OpenAPI::fromJsonValue(m_recurrence, json[QString("Recurrence")]);
    m_recurrence_isSet = !json[QString("Recurrence")].isNull() && m_recurrence_isValid;

    m_recurrence_type_isValid = ::OpenAPI::fromJsonValue(m_recurrence_type, json[QString("RecurrenceType")]);
    m_recurrence_type_isSet = !json[QString("RecurrenceType")].isNull() && m_recurrence_type_isValid;

    m_remind_at_isValid = ::OpenAPI::fromJsonValue(m_remind_at, json[QString("RemindAt")]);
    m_remind_at_isSet = !json[QString("RemindAt")].isNull() && m_remind_at_isValid;

    m_remind_before_isValid = ::OpenAPI::fromJsonValue(m_remind_before, json[QString("RemindBefore")]);
    m_remind_before_isSet = !json[QString("RemindBefore")].isNull() && m_remind_before_isValid;

    m_staff_isValid = ::OpenAPI::fromJsonValue(m_staff, json[QString("Staff")]);
    m_staff_isSet = !json[QString("Staff")].isNull() && m_staff_isValid;

    m_start_isValid = ::OpenAPI::fromJsonValue(m_start, json[QString("Start")]);
    m_start_isSet = !json[QString("Start")].isNull() && m_start_isValid;

    m_subject_isValid = ::OpenAPI::fromJsonValue(m_subject, json[QString("Subject")]);
    m_subject_isSet = !json[QString("Subject")].isNull() && m_subject_isValid;
}

QString OAIDiaryAppointmentModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDiaryAppointmentModel::asJsonObject() const {
    QJsonObject obj;
    if (m_appointment_type_isSet) {
        obj.insert(QString("AppointmentType"), ::OpenAPI::toJsonValue(m_appointment_type));
    }
    if (m_cancelled_isSet) {
        obj.insert(QString("Cancelled"), ::OpenAPI::toJsonValue(m_cancelled));
    }
    if (m_comment_isSet) {
        obj.insert(QString("Comment"), ::OpenAPI::toJsonValue(m_comment));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("CreatedAt"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_created_by_isSet) {
        obj.insert(QString("CreatedBy"), ::OpenAPI::toJsonValue(m_created_by));
    }
    if (m_e_tag_isSet) {
        obj.insert(QString("ETag"), ::OpenAPI::toJsonValue(m_e_tag));
    }
    if (m_end_isSet) {
        obj.insert(QString("End"), ::OpenAPI::toJsonValue(m_end));
    }
    if (m_linked_guest.size() > 0) {
        obj.insert(QString("LinkedGuest"), ::OpenAPI::toJsonValue(m_linked_guest));
    }
    if (m_linked_properties.size() > 0) {
        obj.insert(QString("LinkedProperties"), ::OpenAPI::toJsonValue(m_linked_properties));
    }
    if (m_next_recurring_date_isSet) {
        obj.insert(QString("NextRecurringDate"), ::OpenAPI::toJsonValue(m_next_recurring_date));
    }
    if (m_oid_isSet) {
        obj.insert(QString("OID"), ::OpenAPI::toJsonValue(m_oid));
    }
    if (m_recurrence_isSet) {
        obj.insert(QString("Recurrence"), ::OpenAPI::toJsonValue(m_recurrence));
    }
    if (m_recurrence_type_isSet) {
        obj.insert(QString("RecurrenceType"), ::OpenAPI::toJsonValue(m_recurrence_type));
    }
    if (m_remind_at_isSet) {
        obj.insert(QString("RemindAt"), ::OpenAPI::toJsonValue(m_remind_at));
    }
    if (m_remind_before_isSet) {
        obj.insert(QString("RemindBefore"), ::OpenAPI::toJsonValue(m_remind_before));
    }
    if (m_staff_isSet) {
        obj.insert(QString("Staff"), ::OpenAPI::toJsonValue(m_staff));
    }
    if (m_start_isSet) {
        obj.insert(QString("Start"), ::OpenAPI::toJsonValue(m_start));
    }
    if (m_subject_isSet) {
        obj.insert(QString("Subject"), ::OpenAPI::toJsonValue(m_subject));
    }
    return obj;
}

QString OAIDiaryAppointmentModel::getAppointmentType() const {
    return m_appointment_type;
}
void OAIDiaryAppointmentModel::setAppointmentType(const QString &appointment_type) {
    m_appointment_type = appointment_type;
    m_appointment_type_isSet = true;
}

bool OAIDiaryAppointmentModel::is_appointment_type_Set() const{
    return m_appointment_type_isSet;
}

bool OAIDiaryAppointmentModel::is_appointment_type_Valid() const{
    return m_appointment_type_isValid;
}

bool OAIDiaryAppointmentModel::isCancelled() const {
    return m_cancelled;
}
void OAIDiaryAppointmentModel::setCancelled(const bool &cancelled) {
    m_cancelled = cancelled;
    m_cancelled_isSet = true;
}

bool OAIDiaryAppointmentModel::is_cancelled_Set() const{
    return m_cancelled_isSet;
}

bool OAIDiaryAppointmentModel::is_cancelled_Valid() const{
    return m_cancelled_isValid;
}

QString OAIDiaryAppointmentModel::getComment() const {
    return m_comment;
}
void OAIDiaryAppointmentModel::setComment(const QString &comment) {
    m_comment = comment;
    m_comment_isSet = true;
}

bool OAIDiaryAppointmentModel::is_comment_Set() const{
    return m_comment_isSet;
}

bool OAIDiaryAppointmentModel::is_comment_Valid() const{
    return m_comment_isValid;
}

QDateTime OAIDiaryAppointmentModel::getCreatedAt() const {
    return m_created_at;
}
void OAIDiaryAppointmentModel::setCreatedAt(const QDateTime &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIDiaryAppointmentModel::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIDiaryAppointmentModel::is_created_at_Valid() const{
    return m_created_at_isValid;
}

QString OAIDiaryAppointmentModel::getCreatedBy() const {
    return m_created_by;
}
void OAIDiaryAppointmentModel::setCreatedBy(const QString &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIDiaryAppointmentModel::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIDiaryAppointmentModel::is_created_by_Valid() const{
    return m_created_by_isValid;
}

QString OAIDiaryAppointmentModel::getETag() const {
    return m_e_tag;
}
void OAIDiaryAppointmentModel::setETag(const QString &e_tag) {
    m_e_tag = e_tag;
    m_e_tag_isSet = true;
}

bool OAIDiaryAppointmentModel::is_e_tag_Set() const{
    return m_e_tag_isSet;
}

bool OAIDiaryAppointmentModel::is_e_tag_Valid() const{
    return m_e_tag_isValid;
}

QDateTime OAIDiaryAppointmentModel::getEnd() const {
    return m_end;
}
void OAIDiaryAppointmentModel::setEnd(const QDateTime &end) {
    m_end = end;
    m_end_isSet = true;
}

bool OAIDiaryAppointmentModel::is_end_Set() const{
    return m_end_isSet;
}

bool OAIDiaryAppointmentModel::is_end_Valid() const{
    return m_end_isValid;
}

QList<OAILinkedGuestModel> OAIDiaryAppointmentModel::getLinkedGuest() const {
    return m_linked_guest;
}
void OAIDiaryAppointmentModel::setLinkedGuest(const QList<OAILinkedGuestModel> &linked_guest) {
    m_linked_guest = linked_guest;
    m_linked_guest_isSet = true;
}

bool OAIDiaryAppointmentModel::is_linked_guest_Set() const{
    return m_linked_guest_isSet;
}

bool OAIDiaryAppointmentModel::is_linked_guest_Valid() const{
    return m_linked_guest_isValid;
}

QList<OAILinkedPropertiesModel> OAIDiaryAppointmentModel::getLinkedProperties() const {
    return m_linked_properties;
}
void OAIDiaryAppointmentModel::setLinkedProperties(const QList<OAILinkedPropertiesModel> &linked_properties) {
    m_linked_properties = linked_properties;
    m_linked_properties_isSet = true;
}

bool OAIDiaryAppointmentModel::is_linked_properties_Set() const{
    return m_linked_properties_isSet;
}

bool OAIDiaryAppointmentModel::is_linked_properties_Valid() const{
    return m_linked_properties_isValid;
}

QDateTime OAIDiaryAppointmentModel::getNextRecurringDate() const {
    return m_next_recurring_date;
}
void OAIDiaryAppointmentModel::setNextRecurringDate(const QDateTime &next_recurring_date) {
    m_next_recurring_date = next_recurring_date;
    m_next_recurring_date_isSet = true;
}

bool OAIDiaryAppointmentModel::is_next_recurring_date_Set() const{
    return m_next_recurring_date_isSet;
}

bool OAIDiaryAppointmentModel::is_next_recurring_date_Valid() const{
    return m_next_recurring_date_isValid;
}

QString OAIDiaryAppointmentModel::getOid() const {
    return m_oid;
}
void OAIDiaryAppointmentModel::setOid(const QString &oid) {
    m_oid = oid;
    m_oid_isSet = true;
}

bool OAIDiaryAppointmentModel::is_oid_Set() const{
    return m_oid_isSet;
}

bool OAIDiaryAppointmentModel::is_oid_Valid() const{
    return m_oid_isValid;
}

qint32 OAIDiaryAppointmentModel::getRecurrence() const {
    return m_recurrence;
}
void OAIDiaryAppointmentModel::setRecurrence(const qint32 &recurrence) {
    m_recurrence = recurrence;
    m_recurrence_isSet = true;
}

bool OAIDiaryAppointmentModel::is_recurrence_Set() const{
    return m_recurrence_isSet;
}

bool OAIDiaryAppointmentModel::is_recurrence_Valid() const{
    return m_recurrence_isValid;
}

QString OAIDiaryAppointmentModel::getRecurrenceType() const {
    return m_recurrence_type;
}
void OAIDiaryAppointmentModel::setRecurrenceType(const QString &recurrence_type) {
    m_recurrence_type = recurrence_type;
    m_recurrence_type_isSet = true;
}

bool OAIDiaryAppointmentModel::is_recurrence_type_Set() const{
    return m_recurrence_type_isSet;
}

bool OAIDiaryAppointmentModel::is_recurrence_type_Valid() const{
    return m_recurrence_type_isValid;
}

QDateTime OAIDiaryAppointmentModel::getRemindAt() const {
    return m_remind_at;
}
void OAIDiaryAppointmentModel::setRemindAt(const QDateTime &remind_at) {
    m_remind_at = remind_at;
    m_remind_at_isSet = true;
}

bool OAIDiaryAppointmentModel::is_remind_at_Set() const{
    return m_remind_at_isSet;
}

bool OAIDiaryAppointmentModel::is_remind_at_Valid() const{
    return m_remind_at_isValid;
}

QString OAIDiaryAppointmentModel::getRemindBefore() const {
    return m_remind_before;
}
void OAIDiaryAppointmentModel::setRemindBefore(const QString &remind_before) {
    m_remind_before = remind_before;
    m_remind_before_isSet = true;
}

bool OAIDiaryAppointmentModel::is_remind_before_Set() const{
    return m_remind_before_isSet;
}

bool OAIDiaryAppointmentModel::is_remind_before_Valid() const{
    return m_remind_before_isValid;
}

QString OAIDiaryAppointmentModel::getStaff() const {
    return m_staff;
}
void OAIDiaryAppointmentModel::setStaff(const QString &staff) {
    m_staff = staff;
    m_staff_isSet = true;
}

bool OAIDiaryAppointmentModel::is_staff_Set() const{
    return m_staff_isSet;
}

bool OAIDiaryAppointmentModel::is_staff_Valid() const{
    return m_staff_isValid;
}

QDateTime OAIDiaryAppointmentModel::getStart() const {
    return m_start;
}
void OAIDiaryAppointmentModel::setStart(const QDateTime &start) {
    m_start = start;
    m_start_isSet = true;
}

bool OAIDiaryAppointmentModel::is_start_Set() const{
    return m_start_isSet;
}

bool OAIDiaryAppointmentModel::is_start_Valid() const{
    return m_start_isValid;
}

QString OAIDiaryAppointmentModel::getSubject() const {
    return m_subject;
}
void OAIDiaryAppointmentModel::setSubject(const QString &subject) {
    m_subject = subject;
    m_subject_isSet = true;
}

bool OAIDiaryAppointmentModel::is_subject_Set() const{
    return m_subject_isSet;
}

bool OAIDiaryAppointmentModel::is_subject_Valid() const{
    return m_subject_isValid;
}

bool OAIDiaryAppointmentModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_appointment_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cancelled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_e_tag_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_linked_guest.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_linked_properties.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_recurring_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_oid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurrence_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recurrence_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_remind_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_remind_before_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_staff_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_start_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_subject_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDiaryAppointmentModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
