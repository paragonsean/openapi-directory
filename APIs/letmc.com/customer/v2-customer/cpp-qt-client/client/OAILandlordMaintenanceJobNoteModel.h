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
 * OAILandlordMaintenanceJobNoteModel.h
 *
 * Maintenance Job Note Helper Model:-
 */

#ifndef OAILandlordMaintenanceJobNoteModel_H
#define OAILandlordMaintenanceJobNoteModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAILandlordMaintenanceJobNoteModel : public OAIObject {
public:
    OAILandlordMaintenanceJobNoteModel();
    OAILandlordMaintenanceJobNoteModel(QString json);
    ~OAILandlordMaintenanceJobNoteModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getCreatedAt() const;
    void setCreatedAt(const QDateTime &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getNoteContents() const;
    void setNoteContents(const QString &note_contents);
    bool is_note_contents_Set() const;
    bool is_note_contents_Valid() const;

    QString getOid() const;
    void setOid(const QString &oid);
    bool is_oid_Set() const;
    bool is_oid_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_note_contents;
    bool m_note_contents_isSet;
    bool m_note_contents_isValid;

    QString m_oid;
    bool m_oid_isSet;
    bool m_oid_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILandlordMaintenanceJobNoteModel)

#endif // OAILandlordMaintenanceJobNoteModel_H
