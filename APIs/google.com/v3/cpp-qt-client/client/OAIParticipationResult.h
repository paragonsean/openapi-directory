/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIParticipationResult.h
 *
 * Represents a result from querying for participation stats for an account.
 */

#ifndef OAIParticipationResult_H
#define OAIParticipationResult_H

#include <QJsonObject>

#include "OAIKey.h"
#include "OAIMissedParticipationCountDetails.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIKey;
class OAIMissedParticipationCountDetails;

class OAIParticipationResult : public OAIObject {
public:
    OAIParticipationResult();
    OAIParticipationResult(QString json);
    ~OAIParticipationResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIKey getKey() const;
    void setKey(const OAIKey &key);
    bool is_key_Set() const;
    bool is_key_Valid() const;

    QString getMissedParticipationCount() const;
    void setMissedParticipationCount(const QString &missed_participation_count);
    bool is_missed_participation_count_Set() const;
    bool is_missed_participation_count_Valid() const;

    OAIMissedParticipationCountDetails getMissedParticipationCountDetails() const;
    void setMissedParticipationCountDetails(const OAIMissedParticipationCountDetails &missed_participation_count_details);
    bool is_missed_participation_count_details_Set() const;
    bool is_missed_participation_count_details_Valid() const;

    QString getOpportunityCount() const;
    void setOpportunityCount(const QString &opportunity_count);
    bool is_opportunity_count_Set() const;
    bool is_opportunity_count_Valid() const;

    QString getParticipationCount() const;
    void setParticipationCount(const QString &participation_count);
    bool is_participation_count_Set() const;
    bool is_participation_count_Valid() const;

    double getParticipationPercent() const;
    void setParticipationPercent(const double &participation_percent);
    bool is_participation_percent_Set() const;
    bool is_participation_percent_Valid() const;

    QString getPartnerHotelDisplayName() const;
    void setPartnerHotelDisplayName(const QString &partner_hotel_display_name);
    bool is_partner_hotel_display_name_Set() const;
    bool is_partner_hotel_display_name_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIKey m_key;
    bool m_key_isSet;
    bool m_key_isValid;

    QString m_missed_participation_count;
    bool m_missed_participation_count_isSet;
    bool m_missed_participation_count_isValid;

    OAIMissedParticipationCountDetails m_missed_participation_count_details;
    bool m_missed_participation_count_details_isSet;
    bool m_missed_participation_count_details_isValid;

    QString m_opportunity_count;
    bool m_opportunity_count_isSet;
    bool m_opportunity_count_isValid;

    QString m_participation_count;
    bool m_participation_count_isSet;
    bool m_participation_count_isValid;

    double m_participation_percent;
    bool m_participation_percent_isSet;
    bool m_participation_percent_isValid;

    QString m_partner_hotel_display_name;
    bool m_partner_hotel_display_name_isSet;
    bool m_partner_hotel_display_name_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIParticipationResult)

#endif // OAIParticipationResult_H
