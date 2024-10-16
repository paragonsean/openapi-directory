/**
 * LetMC Api V2, Basic (Tier 2)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-basic-tier
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIViewingBookingModel.h
 *
 * Represents a viewing booking slot
 */

#ifndef OAIViewingBookingModel_H
#define OAIViewingBookingModel_H

#include <QJsonObject>

#include <QDateTime>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIViewingBookingModel : public OAIObject {
public:
    OAIViewingBookingModel();
    OAIViewingBookingModel(QString json);
    ~OAIViewingBookingModel() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QDateTime getEnd() const;
    void setEnd(const QDateTime &end);
    bool is_end_Set() const;
    bool is_end_Valid() const;

    QString getStaffId() const;
    void setStaffId(const QString &staff_id);
    bool is_staff_id_Set() const;
    bool is_staff_id_Valid() const;

    QString getStaffName() const;
    void setStaffName(const QString &staff_name);
    bool is_staff_name_Set() const;
    bool is_staff_name_Valid() const;

    QDateTime getStart() const;
    void setStart(const QDateTime &start);
    bool is_start_Set() const;
    bool is_start_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QDateTime m_end;
    bool m_end_isSet;
    bool m_end_isValid;

    QString m_staff_id;
    bool m_staff_id_isSet;
    bool m_staff_id_isValid;

    QString m_staff_name;
    bool m_staff_name_isSet;
    bool m_staff_name_isValid;

    QDateTime m_start;
    bool m_start_isSet;
    bool m_start_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIViewingBookingModel)

#endif // OAIViewingBookingModel_H
