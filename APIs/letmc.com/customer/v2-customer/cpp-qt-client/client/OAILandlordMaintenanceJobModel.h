/**
 * agentOS Api V2, Customer Login Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-customer
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILandlordMaintenanceJobModel.h
 *
 * Maintenance Job
 */

#ifndef OAILandlordMaintenanceJobModel_H
#define OAILandlordMaintenanceJobModel_H

#include <QJsonObject>

#include "OAILandlordMaintenanceJobNoteModel.h"
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILandlordMaintenanceJobNoteModel;

class OAILandlordMaintenanceJobModel : public OAIObject {
public:
    OAILandlordMaintenanceJobModel();
    OAILandlordMaintenanceJobModel(QString json);
    ~OAILandlordMaintenanceJobModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAssignedTo() const;
    void setAssignedTo(const QString &assigned_to);
    bool is_assigned_to_Set() const;
    bool is_assigned_to_Valid() const;

    QDateTime getClosedDate() const;
    void setClosedDate(const QDateTime &closed_date);
    bool is_closed_date_Set() const;
    bool is_closed_date_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    QList<OAILandlordMaintenanceJobNoteModel> getMaintenanceNotes() const;
    void setMaintenanceNotes(const QList<OAILandlordMaintenanceJobNoteModel> &maintenance_notes);
    bool is_maintenance_notes_Set() const;
    bool is_maintenance_notes_Valid() const;

    QString getProperty() const;
    void setProperty(const QString &property);
    bool is_property_Set() const;
    bool is_property_Valid() const;

    QDateTime getReported() const;
    void setReported(const QDateTime &reported);
    bool is_reported_Set() const;
    bool is_reported_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_assigned_to;
    bool m_assigned_to_isSet;
    bool m_assigned_to_isValid;

    QDateTime m_closed_date;
    bool m_closed_date_isSet;
    bool m_closed_date_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    QList<OAILandlordMaintenanceJobNoteModel> m_maintenance_notes;
    bool m_maintenance_notes_isSet;
    bool m_maintenance_notes_isValid;

    QString m_property;
    bool m_property_isSet;
    bool m_property_isValid;

    QDateTime m_reported;
    bool m_reported_isSet;
    bool m_reported_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILandlordMaintenanceJobModel)

#endif // OAILandlordMaintenanceJobModel_H
